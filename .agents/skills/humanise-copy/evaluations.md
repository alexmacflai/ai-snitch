---
kind: doc
description: Behaviour cases for humanise copy and nearby requests.
---

# Behaviour evaluations

Use [humanise-copy](SKILL.md) in a fresh context for each case. Give the evaluator the request and raw evidence only; withhold expected outcomes. Compare the actual response and artefacts afterwards. Simulate follow-up turns where stated. These cases describe evaluation, not completed test results.

## Preserve voice and actions

- Request: Humanise this copy in separate passes.
- Evidence: “Well, that was a fucking excellent gig. Maybe our best. Archive this recording to hide it from your library; you can restore it later.”
- Good result: Preserves humour, profanity, uncertainty and reversible archive meaning; shows original/broad/focused changes separately.

## Clean copy

- Request: Check this button and error text.
- Evidence: “Save recording”; “Upload failed. Try again.”
- Good result: Leaves effective wording unchanged; does not invent personality or a defect.

## Unknown claim

- Request: Make this line more human.
- Evidence: “Our tool significantly improves efficiency.” No supporting numbers supplied.
- Good result: Uses a supported minimal edit or flags missing specificity; invents no statistic or personal experience.

## Nearby unrelated request

- Request: Translate this approved label exactly into French.
- Evidence: An exact translation request.
- Good result: Does not add an unsolicited humanisation workflow.
