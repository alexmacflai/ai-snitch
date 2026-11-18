---
kind: doc
description: Recommended implementation phases, acceptance gates and unresolved owner decisions.
---

# Rollout and open decisions

## Phase 0: local setup and research

This task installs the reusable framework, records confirmed intent, separates proposed architecture from implemented state, and checks routing and structure. Research establishes a feasible zero-cost baseline. No public pattern catalogue, site or scheduled process is claimed complete.

## Phase 1: evidence pilot

Review the three user seeds plus the research leads in the [feasibility report](../reports/2026-11-18-feasibility.md). Aim for three to five publishable entries, but do not fill a quota by weakening the evidence gate. Keep unsupported seeds as candidates. Prove that one empirical and one reported-association entry can be represented with honest dates, limitations and a lifecycle event. Review tone and invented examples with Alex.

Deliver a JSON schema, representative content fixtures and validation covering missing sources, invalid state transitions and unknown dates. Decide the code/content licence and quotation policy before distributing content.

## Phase 2: static prototype

Implement the recommended Python generator with semantic templates, pattern index and detail pages, source references, status/history and a concise explanation of evidential limits. Add search/filter only if the pilot needs it. Generate Markdown/JSON exports from the same records. Provide local run/build commands, automated schema checks and preview screenshots. Verify keyboard use, small screens, contrast, link/base-path correctness and candidate exclusion. No hosted API or database is needed.

## Phase 3: manual publishing pilot

After explicit publication authorisation, use the GitHub connector to create or select a public repository, inspect Actions/Pages settings, add validation and Pages deployment on approved changes, and verify the deployed site and generated exports. Keep the included GitHub domain. Confirm spending controls, artifact retention and that no paid runner/service is enabled. Do not publish internal notes accidentally.

## Phase 4: scouting pilot

Implement a manual scout first, test deduplication, overlap dates, partial failure, hostile content, response-size limits and rate-limit recovery with fixtures. Inspect one real run's provenance and relevance before enabling the proposed weekly schedule. Compare the first four weekly batches for noise and missed topics. Start with the review-log publication mode, adjust sources/cadence if useful, then consider draft PRs. Verify failure visibility and manual recovery. Do not promise continuous unattended availability.

## Phase 5: reusable guidance

Release versioned rules and an optional skill with applicability, caveats and exceptions. Add a self-review step to copy changes; test an integrating project using a pinned export. Choose an update mechanism only when a real consumer needs it. Track correction quality and editorial effort rather than invented detection performance.

## Open decisions

| Decision | Recommendation or boundary |
|---|---|
| Public repository and account | Recommended for free Pages/standard Actions; confirm destination before remote creation |
| Editorial publication mode | Review log first, automatic deploy after human approval |
| Cadence | Weekly scout, monthly review, quarterly entry review; enable only when authorised |
| Internal privacy | Public-safe unpublished leads may live in public source; confidential evidence stays outside it |
| Licence | Decide separately for code, original content and rules; retain third-party attribution/reuse restrictions |
| Audience/language | Begin in English for writers/editors/designers/developers; validate these hypotheses |
| Look and feel | Undecided; voice is proposed, no visual system or approved screen exists |
| Optional AI | Omit from baseline; reconsider only if the free-only requirement and quotas can be enforced |

The next executable task is Phase 1: create the schema and evidence pilot locally. No further product questionnaire is needed to start it once implementation is requested.
