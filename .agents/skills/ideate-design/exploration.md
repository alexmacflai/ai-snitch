---
kind: doc
description: Exploration through ambitious references, unfinished ideas, combinations and String Seed of Thought.
---

# Design exploration

Used by [ideate-design](SKILL.md). Brief ideas leave room for imagination. Describe concepts with enough specificity to provoke a reaction, without prematurely specifying every screen.

For an existing idea, elicit concrete references and reactions: what should feel tactile, surprising, calm or precise; what feels tacky or overdone; what must remain familiar. Avoid asking for “unique” without a direction. Offer an opinion with reasons, while distinguishing it from the person's taste.

Generate a varied set, then help combine selected qualities. A recording-console idea and an editorial index might contribute different interaction and organisational principles; test whether the combination is coherent rather than adding both sets of decoration. Vary information hierarchy, spatial organisation, interaction or metaphor before colour alone.

## String Seed of Thought

String Seed of Thought uses an externally generated random string as creative inspiration. The agent interprets patterns in the string into a direction, then expresses that direction in the generated design. The string is not an image model's numeric seed parameter, a palette generator or a deterministic layout algorithm.

Run [seed.py](scripts/seed.py) with the needed count; it uses operating-system-backed randomness. If this helper is unavailable but code execution exists, use an equivalent external randomness source and record it. Never present a model-invented string as externally random.

The path from seed to design is explicit:

1. List fixed decisions and open choices before looking at the strings. User decisions take precedence over every seed interpretation.
2. Generate a separate string for each alternative. Look for clusters, repetitions, alternating characters, gaps between numbers or other subpatterns that suggest a rhythm, material, metaphor or organising principle. There is no fixed character-to-design dictionary; use creative judgement.
3. Translate that interpretation into concrete decisions for open choices: composition, hierarchy, typography, imagery or interaction. Write these into the generation brief before generating the design. If another tool or agent makes the design, pass the interpreted direction and decisions to it; a bare string is insufficient guidance.
4. Generate the design from that brief, then inspect whether the intended choices appear and the fixed constraints hold. Rework a generic or near-duplicate result rather than merely assigning it a new seed.
5. Save the seed, interpretation, intended design decisions and rendered outcome together in the exploration record. Distinguish the planned influence from what the output actually demonstrates; do not invent a seed explanation after making the design.

For example, with monochrome and a wordmark fixed, repeated compact clusters might suggest a catalogue: dense aligned rows, a narrow index column and small typographic labels. A string with long runs interrupted by isolated characters might suggest an editorial composition: one dominant subject, broad pauses and sparse secondary navigation. These are illustrative interpretations, not automatic mappings. Both directions preserve monochrome and the wordmark while changing the open structural choices.

Keep strings out of the visible product. A seed is a creative stimulus and provenance, not a guarantee of reproducibility, originality or quality. This use is for visual exploration; ordinary brainstorming can begin with short verbal concepts without seeds.

Use [creative prompting](../design-with-ai/prompting.md) for executable briefs. Compare actual outputs. Reject near-duplicates and explain the change in exploration strategy. Ask focused questions such as which organising principle feels promising, then vary that direction or combine it with another. Retain every experiment, including discarded ones, without implying approval.
