---
name: set-up-engineering
description: Draft architecture, code rules and testing policy.
---

# Set up engineering

Writes how the project is built and the rules code in it follows. Most of it comes from reading the code, where there is any; the user only confirms the rules.

## When to use

- Setting up a project, from [set-up-project](../set-up-project/SKILL.md), or when this area is missing or partial.
- Not for: changing an area that is done; edit its files.

## Inputs

- The code, its build and test configuration, and the user's answers.

## Steps

1. Creating `knowledge/engineering/` creates a domain: if the user did not choose it in [set-up-project](../set-up-project/SKILL.md), get their [approval](../../../knowledge/agents/autonomy.md#approval) first.
2. Read the code: dependency manifests, folder layout, entry points, test setup and continuous integration configuration. If there is no code yet, find out the intended stack, following the [question rules](../set-up-project/SKILL.md#judgment). If none is chosen, tell the user there is nothing to write yet and stop without creating files.
3. Copy [README.md](assets/engineering/README.md) and [architecture.md](assets/engineering/architecture.md) to `knowledge/engineering/` and fill in `architecture.md` from the code or the intended stack, removing the sections that do not apply.
4. Copy [code-rules.md](assets/engineering/code-rules.md) and [testing.md](assets/engineering/testing.md) there. Fill in the conventions and checks the code already follows.
5. Follow each template's usage comment, then remove the comment.
6. Show the user the rules the templates already contain, all together, and ask whether to keep them or change any, and whether to add conventions you could not read.
7. Show the user the drafts and apply their corrections. Leave a fill-in comment wherever an answer is not known yet.
8. Route the new files and run the checker, following [maintain-structure](../maintain-structure/SKILL.md).

## Done when

- `architecture.md` has its Stack and Layout sections filled in, or no stack is chosen yet and the user knows nothing was written.
- Every new file passes the checker, and the user knows which fill-in comments remain.
