---
kind: doc
description: Proposed weekly discovery process, publication choices, failure handling and manual review loop.
---

# Scouting and editorial workflow

Provider documentation and limitations are linked in the [feasibility research](../reports/2026-11-18-feasibility.md).

## Recommended cadence

After authorisation to implement and enable it, run one weekly scout at 07:23 UTC each Tuesday (`23 7 * * 2`), away from the start of the hour. This is 08:23 in Amsterdam in winter and 09:23 in summer. Recommend a monthly editorial review and quarterly review of published entries. Weekly collection with occasional review suits a slowly changing library and limits noise. The cadence is a recommendation; no schedule exists.

Use GitHub Actions `schedule` plus `workflow_dispatch` for manual recovery. Scheduled execution is best effort, can be delayed or dropped, and public-repository workflows can be disabled after 60 days without activity. Record each attempted run and inspect run history monthly; do not manufacture activity to imply reliable monitoring.

## Discovery without an LLM

1. Maintain a small allowlist of accessible RSS/Atom feeds and research API queries. Start with arXiv API queries for “AI generated text” with “style”, “lexical” or “linguistic”; use Crossref bibliographic queries for the same topics. Add provider research feeds only after checking their exact endpoints and terms. These APIs discover research, not general web gossip.
2. Fetch bounded pages with timeouts, cache validators and a date overlap for delayed indexing. Respect response headers, back off on 429/5xx and retain per-source cursor state only after successful parsing. arXiv requests should be separated by at least three seconds; recheck current API policy before implementation.
3. Normalise canonical URLs/DOIs/arXiv IDs and deduplicate across runs and versions. Use transparent keyword relevance rules, storing the matched terms and score solely for inbox ordering.
4. Store titles, dates, links and short necessary snippets; avoid full copyrighted article mirrors. Group leads into one review batch, including failures and counts of fetched, new and duplicate records. A successful run with zero leads is distinct from a failed fetch.
5. Preserve the last successful data on partial failure. Use bounded retries and per-source error records. A build must not interpret a failed source as no new evidence.
6. A human follows the links, tests independence, checks contradictions, drafts a claim and approves it under the [evidence model](../product/evidence-model.md). Record rejected/duplicate candidates so they are not repeatedly rediscovered.

No paid general search API is required. Curated feeds and metadata queries are a narrow scouting net, not autonomous comprehensive web search. A monthly manual web search for emerging popular associations fills part of this gap. Do not scrape search-result pages, bypass access controls or rely on undocumented social APIs. Add discovery sources as coverage gaps become clear.

## Publication modes

| Mode | Behaviour | Trade-off |
|---|---|---|
| Review log, recommended first | Scout accumulates public-safe unpublished leads; maintainer applies approved changes monthly | Smallest privilege footprint; unattended collection, human claim review |
| Draft pull request | Scout proposes an inbox batch or draft entry for review | Convenient audit trail; requires write/PR permissions and settings verification; no automatic merge |
| Automatic publication | Machine refreshes already approved mechanical fields after validation | Low-risk metadata only; new claims and lifecycle decisions remain review-gated |

For an entirely automatic editorial site, deterministic retrieval cannot judge evidence or tone. An optional LLM would not remove the need for validation or solve this reliability issue. Recommend automatic collection and automatic deployment of human-approved content, rather than autonomous publication of new claims.

In a future GitHub workflow, isolate collection (read permissions) from the writer (only validated data). Choose a repository review-log branch for durable public-safe batches, or a narrowly scoped PR workflow; verify protected-branch and Actions write settings. Token-generated events may not trigger subsequent workflows: explicitly dispatch the next stage or design a single controlled workflow. Do not assume committing a batch creates a deploy run.

## Feedback loop

Every accepted pattern change regenerates versioned exports. Run a contextual review over site/repository prose, record intentional exceptions and fix selected passages before release. Reader corrections enter the same candidate workflow. External projects pin export versions and decide when to upgrade. Do not let a loose heuristic silently rewrite source quotations, code or intended voice.
