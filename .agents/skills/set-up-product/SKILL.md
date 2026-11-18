---
name: set-up-product
description: Draft the product overview, glossary, users and journeys.
---

# Set up product

Writes what the product is, why it exists and how it works, so every task starts from the same understanding. The product is whatever the project makes, and it may have no users. It drafts from what exists and asks only what it cannot read or infer.

## When to use

- Setting up a project, from [set-up-project](../set-up-project/SKILL.md), or when this area is missing or partial.
- Not for: changing an area that is done; edit its files.

## Inputs

- Existing material about the product, such as the README, a website or existing docs, and the user's answers.

## Steps

1. Read what exists about the product.
2. Following the [question rules](../set-up-project/SKILL.md#judgment), find out what the product is and why it exists. Only then, and only where they apply to it, find out the rest: who it is for, the problem it solves, the vision, the scope, its principles, its main terms, its main users and journeys.
3. Sum up what you understood in a few lines, and let the user correct it before drafting.
4. Copy [README.md](assets/product/README.md) and [product.md](assets/product/product.md) to `knowledge/product/` and fill in `product.md`, removing the sections that do not apply.
5. If terms came up, copy [glossary.md](assets/product/glossary.md) to `knowledge/product/` and add them. If users came up, do the same with [users.md](assets/product/users.md), and if ideas came up, with [ideas.md](assets/product/ideas.md).
6. If the product has users, for each main journey, copy [journey.md](assets/product/journeys/journey.md) into `knowledge/product/journeys/`, with that folder's [README.md](assets/product/journeys/README.md). For each part of the product that already exists, do the same with [feature.md](assets/product/features/feature.md) and its [README.md](assets/product/features/README.md) in `knowledge/product/features/`.
7. Follow each template's usage comment for its name and split, then remove the comment.
8. Replace each copied description with one specific to the file.
9. Show the user the drafts and apply their corrections. Leave a fill-in comment wherever an answer is not known yet.
10. Route the new files and run the checker, following [maintain-structure](../maintain-structure/SKILL.md).

## Done when

- `knowledge/product/product.md` has its opening paragraph filled in.
- Every new file passes the checker, and the user knows which fill-in comments remain.
