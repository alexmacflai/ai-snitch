---
kind: doc
description: Proposed record fields, evidence standards, chronology and editorial state transitions.
---

# Pattern and evidence model

## Separate evidence from editorial state

Use two axes. `evidence_class` is `candidate`, `reported-association` or `empirical-association`; `editorial_status` is `draft`, `active`, `deprecated` or `reactivated`. An empirical finding is bounded by its study setting and is never an authorship verdict. A popular belief can be documented honestly without being endorsed as empirically reliable.

The following is a proposed JSON data contract, not an implemented schema.

| Record | Required fields and constraints |
|---|---|
| Pattern | `schema_version`, immutable `id`, `slug`, `title`, `description`, `category`, `language`, `evidence_class`, `editorial_status`, `scope`, `caveat`, `source_ids`, `examples`, `dates`, `history`, `review` |
| Example | `text`, `kind` (`invented` or `quotation`), `explanation`; quotations additionally need `source_id`, locator and reuse basis |
| Source | `id`, canonical `url`, title, author/publisher, source type, `published_at` nullable, date precision, `retrieved_at`, locator, short relevant extract or paraphrase, reuse note, and access status |
| Claim link | `source_id`, claim supported, evidence role, study scope/model/prompt/corpus where applicable, limitations, independence group and counterevidence |
| Dates | `first_recorded_here`, `earliest_source_found` nullable, `first_observed` nullable, precision, basis source IDs and `last_reviewed`; unknown stays null |
| History event | timestamp, prior/new state, reason, supporting source IDs and reviewer |
| Review | reviewer, review date, decision, rationale and next review date |
| Candidate | ID, discovery timestamp, query/feed and run ID, source pointers, suspected pattern, evidence gaps, triage decision; no public claim implied |

Keep claim-to-source links explicit rather than assuming every source supports every sentence. Stable IDs survive renaming. Slug changes need redirects. Increment schema version for incompatible changes; export release version is separate.

## Publication gates

A candidate stays outside the site until a human reads the actual source, checks the claim and dates, searches for counterexamples and supplies a caveat. Search snippets alone do not pass. Prefer two independent attributable reports for a public-perception entry. One good primary study can support an empirical entry within that study's scope; record peer-review/version status, method, comparison population and limitations. Syndicated reports and posts repeating one claim count as one origin.

One attributable report may be shown only as a specifically attributed single report, with that limitation explicit. It must not be labelled a general consensus. Repeated model samples may support a reproducible observation when model, date, prompt, sample method and comparison are recorded, but do not establish population prevalence.

Do not invent confidence percentages. Evidence class describes support, not detector accuracy. No single stylistic habit, or count of habits, establishes AI authorship.

## Date semantics

“Earliest source we found” is a bounded research result, never the invention date or first occurrence on the internet. Record search coverage and distinguish source publication from collection date. For month/year precision store the precision rather than manufacturing a day. A later source describing earlier behaviour supports an attributed retrospective claim, with both dates visible. The current three user examples have no verified origin dates.

## Lifecycle

`draft → active`: publication gate satisfied and reviewer approves. `active/reactivated → deprecated`: evidence superseded, association no longer useful, or claim unsupported; keep the page and explain why. Time alone never proves a pattern disappeared. Mark overdue entries “Review overdue” without claiming disappearance.

`deprecated → reactivated`: fresh, independently assessed evidence plus a reason for renewed relevance; preserve all earlier events. Reactivated entries can be deprecated again. Duplicate drafts merge into a stable canonical ID. Material errors are corrected promptly with a visible correction event. Withdrawal from the guide does not erase the historical record; sensitive or improperly reused material may require removal.

Review active entries every quarter and after material counterevidence. A source disappearing prompts access-status review, not automatic erasure or proof that the claim is false. Generated exports include current approved guidance; archive releases preserve former guidance and reasons for change.
