"""Evidence contract tests, including deliberately invalid editorial decisions."""
import copy
import json
import tempfile
import unittest
from pathlib import Path
from tools.validate_content import ROOT, eligible_patterns, load_json, validate


class EvidenceTests(unittest.TestCase):
    def setUp(self):
        self.bundle = load_json(ROOT / 'content/pilot.json')

    def errors(self, fragment):
        self.assertTrue(any(fragment in e for e in validate(self.bundle)), validate(self.bundle))

    def approve(self):
        """Synthetic approval fixture only; never write this into pilot content."""
        p = self.bundle['patterns'][0]
        p.update(editorial_status='active', publication_approved=True)
        p['history'].append(dict(date='2026-11-18', **{'from': 'draft', 'to': 'active'},
                                reason='Synthetic human approval fixture', source_ids=list(p['source_ids']), actor='Fixture editor'))
        p['review'].update(decision='approved', approved_by='Fixture editor', approved_at='2026-11-18',
                           approval_reference='test fixture only, not a real approval')
        return p

    def test_pilot_accepts_unknown_dates_and_exports_nothing(self):
        self.assertEqual([], validate(self.bundle))
        self.assertEqual([], eligible_patterns(self.bundle))
        self.assertTrue(all(not p['publication_approved'] for p in self.bundle['patterns']))

    def test_missing_source(self):
        self.bundle['sources'] = self.bundle['sources'][1:]
        self.errors('missing source')

    def test_undeclared_claim_source(self):
        self.bundle['patterns'][0]['claims'][0]['source_id'] = 'elsewhere'
        self.errors('source not declared')

    def test_duplicate_ids_and_slugs(self):
        self.bundle['patterns'].append(copy.deepcopy(self.bundle['patterns'][0]))
        self.errors('duplicate ID')
        self.errors('duplicate slug')

    def test_unknown_date_cannot_have_value(self):
        self.bundle['sources'][1]['published_at']['value'] = '2026-09-01'
        self.errors("type 'null'")

    def test_calendar_dates_are_checked(self):
        self.bundle['sources'][0]['published_at']['value'] = '2025-02-30'
        self.errors('day is out of range')

    def test_precision_must_match(self):
        self.bundle['sources'][0]['published_at']['precision'] = 'month'
        self.errors('precision does not match')

    def test_partial_month_is_valid(self):
        self.bundle['sources'][0]['published_at'] = {'value':'2025-03', 'precision':'month'}
        self.bundle['patterns'][0]['dates']['earliest_source_found']['date'] = {'value':'2025-03', 'precision':'month'}
        self.assertEqual([], validate(self.bundle))

    def test_known_dates_need_basis(self):
        self.bundle['patterns'][0]['dates']['first_observed']['date'] = {'value':'2025', 'precision':'year'}
        self.errors('known date requires source basis')

    def test_earliest_date_must_match_source(self):
        self.bundle['patterns'][0]['dates']['earliest_source_found']['date']['value'] = '2024-03-24'
        self.errors('must match a cited source')

    def test_invalid_initial_transition(self):
        self.bundle['patterns'][0]['history'][0]['to'] = 'active'
        self.errors('invalid lifecycle transition')

    def test_history_must_match_current_state(self):
        self.bundle['patterns'][0]['editorial_status'] = 'reactivated'
        self.errors('history does not end')

    def test_review_chronology(self):
        self.bundle['patterns'][0]['review']['next_review_at'] = '2026-01-01'
        self.errors('review chronology')

    def test_quotation_needs_provenance_and_reuse_basis(self):
        self.bundle['patterns'][0]['examples'][0]['kind'] = 'quotation'
        self.errors('required property')

    def test_invented_example_cannot_impersonate_quotation(self):
        self.bundle['patterns'][0]['examples'][0]['source_id'] = 'community-em-dash-2025'
        self.errors('should not be valid')

    def test_schema_rejects_unrecognised_accuracy_field(self):
        self.bundle['patterns'][0]['accuracy'] = 0.99
        self.errors('Additional properties')

    def test_whitespace_is_not_evidence(self):
        self.bundle['patterns'][0]['claims'][0]['claim'] = '   '
        self.errors('does not match')

    def test_empirical_claim_needs_reviewed_primary_study(self):
        self.bundle['patterns'][0].update(evidence_class='empirical-association', association_scope='bounded-study')
        self.errors('requires a reviewed primary study')

    def test_abstract_only_does_not_pass_publication_evidence_gate(self):
        self.bundle['sources'][2]['review_depth'] = 'abstract-only'
        self.errors('text-reviewed supporting evidence')

    def test_syndicated_or_same_study_sources_are_not_independent(self):
        p = self.bundle['patterns'][0]
        duplicate = copy.deepcopy(self.bundle['sources'][0])
        duplicate['id'] = 'same-report-reprint'
        self.bundle['sources'].append(duplicate)
        p['source_ids'].append(duplicate['id'])
        p['claims'].append(dict(p['claims'][0], source_id=duplicate['id']))
        p['association_scope'] = 'multiple-attributed-reports'
        self.errors('at least two independence groups')

    def test_candidate_cannot_be_approved(self):
        self.bundle['candidates'][0]['publication_approved'] = True
        self.errors('False was expected')
        self.assertEqual([], eligible_patterns(self.bundle))

    def test_human_approval_is_required(self):
        p = self.approve()
        p['review']['approval_reference'] = None
        self.errors('documented human approval')
        self.assertEqual([], eligible_patterns(self.bundle))

    def test_approved_fixture_passes_and_candidates_are_excluded(self):
        p = self.approve()
        self.assertEqual([], validate(self.bundle))
        self.assertEqual([p['id']], [r['id'] for r in eligible_patterns(self.bundle)])

    def test_retirement_retains_history_but_leaves_current_rules(self):
        p = self.approve()
        p['history'].append(dict(date='2026-11-18', **{'from':'active','to':'deprecated'},
                                reason='Synthetic evidence superseded', source_ids=list(p['source_ids']), actor='Fixture editor'))
        p['editorial_status'] = 'deprecated'
        self.assertEqual([], validate(self.bundle))
        self.assertEqual([], eligible_patterns(self.bundle))

    def test_reactivation_without_fresh_evidence_fails(self):
        p = self.approve()
        for old, new in [('active','deprecated'),('deprecated','reactivated')]:
            p['history'].append(dict(date='2026-11-18', **{'from':old,'to':new}, reason='Synthetic transition',
                                    source_ids=list(p['source_ids']), actor='Fixture editor'))
        p['editorial_status'] = 'reactivated'
        self.errors('fresh evidence')

    def test_reactivation_accepts_fresh_reviewed_evidence(self):
        p = self.approve()
        p['history'].append(dict(date='2026-11-18', **{'from':'active','to':'deprecated'},
                                reason='Synthetic retirement', source_ids=list(p['source_ids']), actor='Fixture editor'))
        fresh = copy.deepcopy(self.bundle['sources'][0])
        fresh.update(id='fresh-independent-report', independence_group='fresh-independent-author')
        self.bundle['sources'].append(fresh)
        p['source_ids'].append(fresh['id'])
        p['claims'].append(dict(p['claims'][0], source_id=fresh['id']))
        p['history'].append(dict(date='2026-11-18', **{'from':'deprecated','to':'reactivated'},
                                reason='Synthetic fresh evidence', source_ids=[fresh['id']], actor='Fixture editor'))
        p['editorial_status'] = 'reactivated'
        self.assertEqual([], validate(self.bundle))
        fresh['review_depth'] = 'abstract-only'
        self.errors('fresh reviewed evidence')

    def test_duplicate_json_keys_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            p = Path(folder) / 'duplicate.json'
            p.write_text('{"id":"one","id":"two"}')
            with self.assertRaisesRegex(ValueError, 'duplicate JSON key'):
                load_json(p)


if __name__ == '__main__':
    unittest.main()
