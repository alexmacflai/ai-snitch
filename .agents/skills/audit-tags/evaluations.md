---
kind: doc
description: Behaviour cases for tag audits, coverage and nearby requests.
---

# Behaviour evaluations

Use [audit-tags](SKILL.md) in a fresh context for each case. Supply the request and raw evidence without the expected outcome, then compare the response and artefacts. These are evaluation cases, not completed test results.

## Merge synonyms and repair assignments

- Request: Audit all tags and recommend changes.
- Evidence: Registry defines `testing` as tests and correctness checks, `qa` as quality checks, and unused `legacy`. `knowledge/engineering/tests.md` uses `testing` for regression tests; `knowledge/release/checks.md` uses `qa` for the same tests and an unregistered `release`. Both bodies describe correctness checks; the latter also describes release coordination.
- Good result: Recommends merging `qa` into `testing` with both paths and a replacement mapping, registering `release` if useful, and removing unused `legacy`. Makes no edits for this review request.

## Untagged content and misleading keywords

- Request: Audit the tags across these documents.
- Evidence: Registry defines `accessibility`. Untagged `knowledge/design/focus.md` covers keyboard navigation and focus visibility. `knowledge/product/launch.md` says “testing demand” but discusses interviews, with no software tests. Its front-matter uses `testing`.
- Good result: Reads both bodies; recommends `accessibility` for the first and removing the misleading `testing` assignment from the second. Does not infer topics solely from words.

## Useful singleton and distinct meanings

- Request: Check whether our tags need tidying.
- Evidence: Registry defines `privacy` as personal data handling, `security` as protection against unauthorised access. One document covers retention and uses `privacy`; another covers access controls and uses `security`. A third project overview is untagged and has no useful cross-cutting topic.
- Good result: Keeps both distinct singleton tags and leaves the overview untagged. Reports that no change is needed.

## Incomplete coverage

- Request: Audit all tags.
- Evidence: Enumerated scope contains five documents; one cannot be read. The four readable documents use no `privacy` tag, but the registry defines it.
- Good result: Reports four of five reviewed, names the unread file and withholds a definitive unused-tag removal finding until its assignments can be checked. Does not claim a complete audit.

## Apply an authorised merge

- Request: Merge `qa` into `testing` throughout these documents and verify it.
- Evidence: Both registered tags mean correctness checks; three documents use `qa`, including one using both tags. Routing tables repeat the assignments.
- Good result: Replaces all three uses, deduplicates the mixed assignment, removes the old registration after confirming no uses remain, regenerates routing and reports checks. Preserves document prose.

## Nearby ordinary edit

- Request: Add a tag to the document you just wrote.
- Evidence: The registry already contains a suitable topic tag.
- Good result: Uses that tag without starting a repository-wide audit.

## Theme across folders with no single home

- Request: Audit all tags.
- Evidence: No registered tag covers project categories. `product/glossary.md` defines the project types; `product/features/work-archive.md` filters by them; `design/visual-language.md` gives each type an accent colour; `copywriting/microcopy.md` lists the type labels. Only the glossary is mainly about types.
- Good result: Collects the recurring topic in the cross-document pass, confirms it in each body, and recommends a new registered tag for all four files. Does not dismiss it because each mention is short or no other document is about it.

## Tag used inside one folder only

- Request: Check whether our tags need tidying.
- Evidence: `routing` is used only on `knowledge/meta/routing.md`, which also carries `structure`. Both tags appear only in `knowledge/meta/`.
- Good result: Flags `routing` as used inside one folder only and recommends merging it into `structure`, or explains why the distinction helps readers. If the registry came from an upstream source, recommends the change there.

## Near-miss candidate, correctly turned down

- Request: Audit all tags.
- Evidence: Secrets come up in `agents/safety.md` (never store them) and in `engineering/deployment.md` (the list of deploy secrets). Nothing else mentions them, and `safety.md` already links to the deployment doc.
- Good result: Lists `secrets` as considered and turned down. The reason given: two documents that already link to each other, so a tag would find nothing new. Gives no false "no change needed" without naming the candidate.
