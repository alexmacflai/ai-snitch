---
kind: report
description: Source assessment, editorial outcomes, search coverage and validation evidence for the unpublished pilot.
---

# Phase 1 evidence pilot

## Summary

Created a machine-readable evidence contract, local validator and three supported drafts: one bounded empirical vocabulary association and two specifically attributed reported associations. One broad seed is retained as a candidate; one stronger detector interpretation is rejected. All pattern records are draft, all publication approvals are false and zero records are eligible for publication. Nothing was uploaded, scheduled or published.

The two initial vocabulary leads were combined into one entry because the studies address overlapping lexical habits. They do not justify two independent editing rules merely to reach a target entry count. The pilot reaches three supported drafts without treating them as approved public content.

## Evidence

### Review outcomes

| Record | Assessment | Remaining boundary |
|---|---|---|
| `em-dash-habit` | Reported association, attributed to an inspected forum post; institutional guidance supplies context | No model-wide prevalence or authorship claim |
| `contrastive-framing` | Reported association, explicitly attributed to JCQ guidance | No quantitative model comparison appraised for this construction |
| `delve-style-vocabulary` | Empirical association bounded by a scientific-writing task; related corpus study provides context | No present-day, cross-genre or individual-authorship generalisation |
| `bombastic-emotion` | Retain as candidate | Narrow emotion/hype/unsupported significance into an operational definition before making a claim |
| `contrast-proves-ai` | Reject detector interpretation | Retain the weaker attributed-association draft and rejection rationale |

The structured records, claim links, examples, limitations, dates and triage decisions are in [pilot.json](../../content/pilot.json). None carries a human approval. Draft tone and example usefulness still need Alex's review.

### Primary-source trail

- [Opening forum post, 24 March 2025](https://community.openai.com/t/what-are-your-strategies-for-spotting-ai-writing/1150515): direct evidence that a participant reports an em-dash association. It is not an official provider finding. The earliest inspected dated support for this draft is recorded with a bounded-search qualification.
- [JCQ guidance](https://www.jcq.org.uk/wp-content/uploads/sites/2/2026/10/AI-Use-in-Assessments_Sep26_v5.pdf.pdf), printed pages 26–28: extracted relevant tables and adjacent caveats were reviewed. Effective September 2026 is distinct from an unknown publication date. No precision was inferred from the October URL directory. Direct local PDF retrieval returned HTTP 403; web text was available, but visual PDF inspection was not verified. No quoted source examples were copied.
- [Juzek and Ward, arXiv v1](https://arxiv.org/html/2412.11385v1): relevant methods, results and limitations reviewed. The task supports a bounded lexical association; its proposed causal explanation remains unresolved. [COLING metadata](https://aclanthology.org/2025.coling-main.426/) confirms later publication at month precision. It is the same study, not independent corroboration; proceedings text was not version-compared.
- [Kobak and colleagues, arXiv v5](https://arxiv.org/html/2406.07016v5): relevant corpus methods and limitations reviewed. [Version history](https://arxiv.org/abs/2406.07016) distinguishes the initial June 2024 submission, July 2025 version and journal reference. The reviewed version's date is stored separately from the historical initial submission; its findings were not backdated.

These are source assessments, not dataset replications or a systematic review. Research notes and source summaries are paraphrases. There is no fabricated detection accuracy, origin date or retirement/reactivation event in the real records.

### Search coverage and unadopted leads

Manual web searches on 18 November 2026 included `em dash AI`, `AI stylistic contrast`, `it's not it's AI writing author`, `LLM exaggerated writing style`, and the two vocabulary-paper identifiers. Searches prioritised attributable originals, primary papers and institutional guidance; snippets were discovery aids. They were not accepted as empirical evidence.

An [April 2025 forum discussion](https://community.openai.com/t/prevent-chatgpt-from-using-dashes-and-indented-bullet-points/1232370) was inspected as an additional anecdote, but not counted as independent empirical validation. An [editor's Inc. column](https://www.inc.com/jessica-stillman/this-sentence-structure-is-a-dead-giveaway-that-ai-wrote-it/91275389) and its Fast Company reprint were found for contrastive framing; they share an origin and were not needed to establish the narrower JCQ-attributed draft. Their detector framing was not adopted.

A newer [congressional em-dash preprint](https://arxiv.org/abs/2608.05889) was discovered, but the full text was not appraised: the attempted HTML version returned 404. It remains a research lead, not support in the pilot. Source discovery was bounded and cannot establish the first-ever report or claim no contrary studies exist.

Counterexample review considered the legitimate human use cautions in the inspected guidance, the corpus paper's inability to identify individual assisted abstracts and the lexical study's task and causal limitations. Broader rhetorical history, multilingual usage and newer models still need dedicated review. The search was not exhaustive.

### Validation

The [schema and validator](../engineering/content-validation.md) were exercised against real records and 27 regression tests. Tests cover missing sources, precision/calendar errors, duplicate records/keys, undeclared claim links, quoted-example provenance, unsupported empirical classification, repeated-origin evidence, human approval metadata, retirement/reactivation and candidate exclusion. Positive lifecycle fixtures are synthetic and stay in tests.

The implementation uses `jsonschema==4.25.1`, installed in a temporary isolated Python 3.9 environment. The newer documentation version was not available to this interpreter; the pinned compatible release installed successfully. No API key, paid account or service purchase was needed. Schema validation checks structure and recorded decisions; it cannot prove a source's truth or an approver's identity.

## Assumptions

- A conservative single-attributed-report draft is useful before wider corroboration is available.
- A single pilot JSON bundle is sufficient at this scale; it contains unpublished candidates, so a future build must use explicit eligibility filtering.
- English remains the initial language; no demographic or genre coverage is established.

## Open questions and next steps

Alex can review the three draft descriptions, invented examples and source-scoped claims. Licence choice and public publication approval remain unresolved and do not block local research. Retain the broad emotional/bombastic seed until it is narrower and supported. Before any site publication, review source versions, verify the visual PDF table if needed and implement/test explicit build exclusion of candidates and unapproved drafts. The next implementation phase is the local static prototype; no automatic continuation or deployment was enabled.
