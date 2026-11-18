---
name: design-with-ai
description: Develop distinctive designs through collaborative ideation, prototyping and refinement.
---

# Design with AI

Coordinates an ongoing creative collaboration. Each stage may span multiple turns; an answer alone does not finish it.

## When to use

- Taking an idea through several creative stages, or resuming an exploration.
- For one named stage, use that stage directly. Not for research, feature specification or ordinary implementation.

## Inputs

- The request, available project guidance, references and any existing exploration record.

## Steps

1. Read [workflow.md](workflow.md). Recover the goal, endpoint, constraints, authorised scope and current stage from context or the existing record. Do not repeat settled intake.
2. Enter [ideate-design](../ideate-design/SKILL.md), [develop-design](../develop-design/SKILL.md) or [refine-design](../refine-design/SKILL.md), according to what is missing. Load its instructions; do not merely recommend its name.
3. Follow that stage across turns, updating the same record. Use [prompting.md](prompting.md) when briefing a generator, implementer or critic.
4. At a stage boundary, compare evidence with the stage's done criteria and the requested endpoint. Continue when authorised, ask for an undelegated choice, or return to an earlier stage when the concept needs reconsideration.
5. Present the result with evidence, decisions, unresolved work and verification limits. Leave a recoverable handoff if interrupted.

## Done when

- The requested endpoint is evidenced and the record reflects it.
- Outstanding work is explicit; paused or blocked work is not called complete.

## Read first

- [Behaviour evaluations](evaluations.md) when testing or changing this skill.
