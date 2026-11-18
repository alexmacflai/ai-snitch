---
kind: doc
description: The implemented JSON contract, semantic checks, publication eligibility and test commands.
---

# Evidence validation

The pilot is a single local bundle in [content/pilot.json](../../content/pilot.json). It contains sources, pattern drafts and candidate records. A future generator must not publish this bundle wholesale.

## Contract

[schemas/evidence.schema.json](../../schemas/evidence.schema.json) uses JSON Schema Draft 2020-12 with closed objects and reusable definitions. Version `1.0.0` is the first implemented contract. It covers source provenance, claim-to-source links, invented or quoted examples, date precision, editorial history, human review metadata and candidates. Sources distinguish first-person reports, guidance, studies and publication records; records from the same study share an independence group.

Unknown dates are `{ "value": null, "precision": "unknown" }`. Month and year precision stay partial. The validator checks actual calendar dates and compares intervals without substituting an invented day. `earliest_source_found` describes inspected support, not the first-ever use; `first_observed` remains unknown in all pilot drafts.

Source `published_at` refers to the pinned version reviewed. Initial-submission dates for older versions can be noted separately but do not retroactively date findings from a later version. An effective date or URL directory is not proof of publication date.

## Validation

[tools/validate_content.py](../../tools/validate_content.py) applies the schema using the free local `jsonschema` library, then checks duplicate IDs/slugs/JSON keys, references, real dates, review chronology, history transitions and evidence gates. The library is a development dependency, not a hosted service; the content validator no longer uses the standard library alone. The framework checker remains independent and needs no package installation. The [library documentation](https://python-jsonschema.readthedocs.io/en/stable/validate/) explains why the implementation explicitly enables format checking.

Non-candidate associations need accessible, relevant-text-reviewed support. Empirical associations need a primary study with method/comparison metadata. Multiple-report claims require different independence groups; reprints and proceedings records from one study do not add independent evidence. Quoted examples require source, locator and reuse basis. The pilot uses invented examples and paraphrases.

Lifecycle checks reject direct draft-to-reactivated changes, mismatched terminal status and reactivation without fresh text-reviewed supporting evidence. Quarterly review dates are editorial reminders; they do not automatically retire patterns.

`eligible_patterns(bundle)` fails closed on validation errors and selects only approved active/reactivated records. Candidates, drafts and deprecated records are excluded from current-rules eligibility. Deprecated pages may eventually appear in a separate historical archive; no archive generator exists. Eligibility is a local guard, not a deployment system or proof that a recorded approver identity is authentic. Actual approvals must be verified in the editorial review process.

## Running

Use Python 3.9 or later and the isolated setup in [setup](../setup.md). Run:

```sh
.venv/bin/python tools/validate_content.py
.venv/bin/python -m unittest discover -s tests
```

The CLI accepts an optional alternative bundle path and returns a non-zero status on invalid input. Tests in [tests/test_evidence.py](../../tests/test_evidence.py) cover real pilot data plus synthetic positive/negative fixtures. Synthetic lifecycle approvals never alter pilot content. There is no source fetcher, site builder, publication command or schedule yet.
