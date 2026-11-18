---
name: set-up-copywriting
description: Draft voice and tone, copy rules and microcopy.
---

# Set up copywriting

Writes how the product sounds and the rules its text follows, so text written by different people and agents reads as one product.

## When to use

- Setting up a project, from [set-up-project](../set-up-project/SKILL.md), or when this area is missing or partial.
- Not for: changing an area that is done; edit its files.

## Inputs

- Existing text in the product, its website or its documents, and the user's answers.

## Steps

1. Creating `knowledge/copywriting/` creates a domain: if the user did not choose it in [set-up-project](../set-up-project/SKILL.md), get their [approval](../../../knowledge/agents/autonomy.md#approval) first.
2. Read `knowledge/product/` and existing text, and note the patterns the text already follows.
3. Following the [question rules](../set-up-project/SKILL.md#judgment), find out what applies to this project: who the product sounds like, how tone changes with the situation, the channels it writes for, and any rules the user already applies.
4. Sum up what you understood in a few lines, and let the user correct it before drafting.
5. Copy [README.md](assets/copywriting/README.md) and [voice-and-tone.md](assets/copywriting/voice-and-tone.md) to `knowledge/copywriting/` and fill in `voice-and-tone.md`, removing the sections that do not apply.
6. If the existing text or answers show rules, copy [copy-rules.md](assets/copywriting/copy-rules.md) there and fill them in, keeping only the sections that apply. Keep Buttons and links and Error messages only if the project has an interface.
7. If the project has an interface with recurring short text, copy [microcopy.md](assets/copywriting/microcopy.md) there with real examples.
8. Follow each template's usage comment, then remove the comment.
9. Show the user the drafts and apply their corrections. Leave a fill-in comment wherever an answer is not known yet.
10. Route the new files and run the checker, following [maintain-structure](../maintain-structure/SKILL.md).

## Done when

- `voice-and-tone.md` has its Voice section filled in.
- Every new file passes the checker, and the user knows which fill-in comments remain.
