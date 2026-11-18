"""Validate local evidence bundles; never fetch sources or publish content."""
import argparse
import calendar
import json
import re
import sys
from datetime import date
from pathlib import Path

try:
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError:
    raise SystemExit('Install development dependencies: python3 -m pip install -r requirements-dev.txt')

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / 'schemas/evidence.schema.json'
TRANSITIONS = {(None, 'draft'), ('draft', 'active'), ('active', 'deprecated'),
               ('reactivated', 'deprecated'), ('deprecated', 'reactivated')}


def load_json(path):
    """Reject duplicate JSON keys rather than silently replacing evidence."""
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError('duplicate JSON key: ' + key)
            result[key] = value
        return result
    return json.loads(Path(path).read_text(encoding='utf-8'), object_pairs_hook=pairs)


def date_interval(partial):
    """Return calendar bounds without inventing precision for unknown dates."""
    value, precision = partial['value'], partial['precision']
    if precision == 'unknown':
        if value is not None:
            raise ValueError('unknown date must be null')
        return None
    patterns = {'day': r'\d{4}-\d{2}-\d{2}', 'month': r'\d{4}-\d{2}', 'year': r'\d{4}'}
    if not isinstance(value, str) or not re.fullmatch(patterns[precision], value):
        raise ValueError('date precision does not match value')
    parts = [int(p) for p in value.split('-')]
    if precision == 'day':
        start = end = date(*parts)
    elif precision == 'month':
        year, month = parts
        start, end = date(year, month, 1), date(year, month, calendar.monthrange(year, month)[1])
    else:
        start, end = date(parts[0], 1, 1), date(parts[0], 12, 31)
    return start, end


def validate(bundle):
    schema = load_json(SCHEMA)
    Draft202012Validator.check_schema(schema)
    errors = []
    for error in Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(bundle):
        path = '.'.join(map(str, error.absolute_path)) or '$'
        errors.append(f'{path}: {error.message}')
    if errors:
        return errors  # Do not attempt semantics on structurally invalid input.

    def fail(label, message):
        errors.append(f'{label}: {message}')

    records = bundle['sources'] + bundle['patterns'] + bundle['candidates']
    seen = set()
    for record in records:
        if record['id'] in seen:
            fail(record['id'], 'duplicate ID across catalogue')
        seen.add(record['id'])
    sources = {s['id']: s for s in bundle['sources']}
    patterns = {p['id']: p for p in bundle['patterns']}
    slugs = [p['slug'] for p in bundle['patterns']]
    if len(slugs) != len(set(slugs)):
        fail('patterns', 'duplicate slug')
    source_dates = {}
    for s in bundle['sources']:
        try:
            source_dates[s['id']] = date_interval(s['published_at'])
            bounds = source_dates[s['id']]
            if bounds and bounds[0] > date.fromisoformat(s['retrieved_at']):
                fail(s['id'], 'publication date is after retrieval')
        except ValueError as error:
            fail(s['id'], str(error))
        if s['source_type'] == 'primary-study' and s['study'] is None:
            fail(s['id'], 'primary study requires method and comparison metadata')

    for p in bundle['patterns'] + bundle['candidates']:
        label = p['id']
        declared = set(p['source_ids'])
        for sid in declared:
            if sid not in sources:
                fail(label, 'missing source: ' + sid)
        used = {c['source_id'] for c in p['claims']}
        for example in p['examples']:
            if example['kind'] == 'quotation':
                used.add(example['source_id'])
        for sid in used - declared:
            fail(label, 'claim/quotation source not declared: ' + sid)
        if label not in patterns:
            if p['related_pattern_id'] is not None and p['related_pattern_id'] not in patterns:
                fail(label, 'related pattern does not exist')
            continue

        supporting = [c for c in p['claims'] if c['role'] == 'support']
        reviewed_support = [sources[c['source_id']] for c in supporting
                            if c['source_id'] in sources and sources[c['source_id']]['review_depth'] == 'relevant-full-text'
                            and sources[c['source_id']]['access_status'] == 'accessible']
        if p['evidence_class'] != 'candidate' and not reviewed_support:
            fail(label, 'association requires accessible, text-reviewed supporting evidence')
        scope = p['association_scope']
        if p['evidence_class'] == 'candidate':
            if scope != 'unsubstantiated' or p['editorial_status'] != 'draft' or p['publication_approved']:
                fail(label, 'candidate must remain unsubstantiated, draft and unpublished')
        elif p['evidence_class'] == 'empirical-association':
            if scope != 'bounded-study' or not any(s['source_type'] == 'primary-study' and s['study'] for s in reviewed_support):
                fail(label, 'empirical association requires a reviewed primary study and bounded-study scope')
        elif scope not in {'single-attributed-report', 'multiple-attributed-reports'}:
            fail(label, 'reported association requires an attributed-report scope')
        if scope == 'multiple-attributed-reports':
            groups = {s['independence_group'] for s in reviewed_support}
            if len(groups) < 2:
                fail(label, 'multiple reports require at least two independence groups')
        if 'does not establish AI authorship' not in p['caveat']:
            fail(label, 'missing explicit authorship caveat')

        dates = p['dates']
        first = date.fromisoformat(dates['first_recorded_here'])
        last = date.fromisoformat(dates['last_reviewed'])
        review = p['review']
        reviewed = date.fromisoformat(review['reviewed_at'])
        if not first <= last == reviewed <= date.fromisoformat(review['next_review_at']):
            fail(label, 'review chronology is inconsistent')
        for key in ['earliest_source_found', 'first_observed']:
            fact = dates[key]
            for sid in fact['basis_source_ids']:
                if sid not in declared:
                    fail(label, key + ' basis is not a declared source: ' + sid)
            try:
                bounds = date_interval(fact['date'])
                if bounds and not fact['basis_source_ids']:
                    fail(label, key + ' known date requires source basis')
                if bounds and bounds[0] > last:
                    fail(label, key + ' is after review date')
                if key == 'earliest_source_found' and bounds:
                    basis_dates = [source_dates.get(sid) for sid in fact['basis_source_ids']]
                    if not any(b and b == bounds for b in basis_dates):
                        fail(label, 'earliest source date must match a cited source date and precision')
            except ValueError as error:
                fail(label, key + ': ' + str(error))

        state, previous_date = None, first
        for event_index, event in enumerate(p['history']):
            event_date = date.fromisoformat(event['date'])
            if event['from'] != state or (event['from'], event['to']) not in TRANSITIONS:
                fail(label, 'invalid lifecycle transition')
            if not previous_date <= event_date <= last:
                fail(label, 'lifecycle dates are out of order or outside record history')
            event_sources = set(event['source_ids'])
            if not event_sources <= declared:
                fail(label, 'lifecycle source is not declared')
            if event['to'] != 'draft' and not event_sources:
                fail(label, 'lifecycle decision requires evidence')
            if event['to'] == 'reactivated':
                # A fresh reviewed source must accompany renewed relevance.
                earlier_sources = {sid for e in p['history'][:event_index] for sid in e['source_ids']}
                if not event_sources - earlier_sources:
                    fail(label, 'reactivation requires fresh evidence')
                if not (event_sources - earlier_sources) & {s['id'] for s in reviewed_support}:
                    fail(label, 'reactivation requires fresh reviewed evidence supporting the claim')
            state, previous_date = event['to'], event_date
        if state != p['editorial_status']:
            fail(label, 'history does not end at current editorial status')
        if p['editorial_status'] != 'draft' and not p['publication_approved']:
            fail(label, 'non-draft record needs publication approval')
        if p['publication_approved']:
            if p['editorial_status'] == 'draft' or review['decision'] != 'approved' or not all(review[k] for k in ['approved_by', 'approved_at', 'approval_reference']):
                fail(label, 'publication needs non-draft state and documented human approval')
            elif not first <= date.fromisoformat(review['approved_at']) <= reviewed:
                fail(label, 'approval date is outside record history')
        elif review['decision'] == 'approved' or any(review[k] is not None for k in ['approved_by', 'approved_at', 'approval_reference']):
            fail(label, 'unpublished review cannot claim approval')
    return errors


def eligible_patterns(bundle):
    """Fail closed; candidates and unapproved drafts never enter an export."""
    if validate(bundle):
        return []
    return [p for p in bundle['patterns'] if p['publication_approved'] and p['editorial_status'] in {'active', 'reactivated'}]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('path', nargs='?', type=Path, default=ROOT / 'content/pilot.json')
    args = parser.parse_args()
    try:
        bundle = load_json(args.path)
        errors = validate(bundle)
    except (OSError, ValueError) as error:
        print(str(error), file=sys.stderr)
        return 1
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print(f"Valid: {len(bundle['sources'])} sources, {len(bundle['patterns'])} patterns, "
          f"{len(bundle['candidates'])} candidates; {len(eligible_patterns(bundle))} eligible for publication.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
