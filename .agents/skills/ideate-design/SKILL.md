---
name: ideate-design
description: Explore and combine design ideas through conversation and visual experiments.
---

# Ideate a design

Helps a person find a direction worth developing, moving freely between words and exploratory designs.

## When to use

- Brainstorming, articulating a creative idea, generating exploratory designs or combining promising concepts.
- Not for formal research or feature specifications.

## Inputs

- Goal, audience, references, fixed decisions, open choices and prior reactions, where available.

## Steps

1. Read the shared [workflow](../design-with-ai/workflow.md) and [exploration techniques](exploration.md). Recover context before asking questions.
2. Infer the activity. If unclear, briefly offer brainstorming together, sharpening an existing idea, or generating exploratory designs. For an existing idea, help articulate specific, ambitious references and boundaries; for brainstorming, start broad with short, unfinished concepts.
3. For visual explorations, use [String Seed of Thought](exploration.md#string-seed-of-thought). Record fixed decisions and open choices, then generate external random strings with `python3 .agents/skills/ideate-design/scripts/seed.py --count 3` from the project root, adjusting count to the requested alternatives. For each seed, interpret its patterns into a creative direction and concrete choices for the generation brief before making the design. Record seed → interpretation → design choices; preserve user constraints. If execution is unavailable, disclose this and request externally generated seeds or agreement to unseeded exploration; never fabricate tool-generated randomness.
4. Make the alternatives tangible at the requested fidelity using available tools. Attach actual references when supported. Compare concept, hierarchy, composition or interaction; regenerate alternatives that differ only cosmetically. Follow [prompting](../design-with-ai/prompting.md) for generation briefs.
5. Invite focused reactions, interpret what they imply, and combine, vary or discard ideas. Repeat across turns; change activity when words need images or images need explanation. Preserve earlier versions.
6. When a direction is selected, express its identity, evidence, fixed/open choices and next creative question in the record. Hand to [develop-design](../develop-design/SKILL.md) only within authorised scope; otherwise finish the requested ideation or ask whether to develop it.

## Done when

- A direction is selected by the user or under explicit delegated judgement and is clear enough to develop.
- For ideas-only requests, the requested ideas are delivered without forcing visualisation or building. Selection is not implementation approval.

## Read first

- [Behaviour evaluations](evaluations.md) when testing or changing this skill.
