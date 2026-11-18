---
kind: doc
description: Behaviour cases for ideate design and nearby requests.
---

# Behaviour evaluations

Use [ideate-design](SKILL.md) in a fresh context for each case. Give the evaluator the request and raw evidence only; withhold expected outcomes. Compare the actual response and artefacts afterwards. Simulate follow-up turns where stated. These cases describe evaluation, not completed test results.

## Brainstorm and combine

- Request: Help me find a visual direction for a concert archive. Ideas only for now.
- Evidence: Known audience: collectors; no chosen aesthetic. Later response: combine the index of one idea with the atmosphere of another.
- Good result: Starts with short varied concepts; reacts and combines across turns; does not build.

## Constrained visual exploration

- Request: Generate three exploratory designs. Keep everything monochrome and preserve my wordmark.
- Evidence: Supplied wordmark and a clear archive brief; external randomness execution available.
- Good result: Uses String Seed of Thought with separate externally generated strings; records each interpretation and concrete design choices before generation, carries them into generation briefs, then inspects their visible expression. Preserves palette and wordmark; neither treats strings as numeric model seeds nor invents explanations afterwards.

## Ambiguous selection

- Request: I like the second one.
- Evidence: Previous authority was exploratory images only.
- Good result: Records selection; asks before building rather than silently invoking development.

## Nearby unrelated request

- Request: Summarise the research interviews.
- Evidence: Interview material.
- Good result: Does not substitute design ideation for research synthesis.
