---
kind: doc
description: Behaviour cases for design with ai and nearby requests.
---

# Behaviour evaluations

Use [design-with-ai](SKILL.md) in a fresh context for each case. Give the evaluator the request and raw evidence only; withhold expected outcomes. Compare the actual response and artefacts afterwards. Simulate follow-up turns where stated. These cases describe evaluation, not completed test results.

## Context and authorised progression

- Request: Take my monochrome concert archive from the attached selected editorial concept to a polished local prototype. You may choose details. Keep the supplied wordmark.
- Evidence: Selected concept and brief, fixed constraints, supplied wordmark and references.
- Good result: Recovers context without an intake menu; develops then refines within scope, preserving decisions and evidence.

## Nearby unrelated request

- Request: Fix the failing JSON parser test.
- Evidence: A parser failure; no design request.
- Good result: Does not activate creative workflow or demand design setup.

## Resume

- Request: Continue this exploration.
- Evidence: A record with chosen direction, rejected colours, latest capture and next creative question; no prior conversation.
- Good result: Recovers scope and decisions and continues from the recorded question.
