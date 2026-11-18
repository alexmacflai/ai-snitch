---
kind: instruction
description: What the project's root README contains, what belongs in knowledge/ instead, and when an existing README may be changed.
tags: [routing]
---

# Project README

`README.md` at the repository root is the front door for people, as `AGENTS.md` is for agents. It carries no front-matter.

## Contents

In order:

1. What the project is, in a sentence or two.
2. The top-level layout, one line per folder.
3. How to get it running: prerequisites, then the fewest commands that work.
4. How the project is checked before pushing: `python3 knowledge/tools/adf.py check` and the pre-commit hook in [tools/](../tools/README.md).
5. That the project follows the Agent Development Framework, with links to `AGENTS.md` and [knowledge/](../README.md) for everything else.

Keep whatever else the project needs that is genuinely for people only: a licence, badges, a screenshot, how to contribute.

## What it does not hold

- Rules, procedures, or anything that already lives in `knowledge/`. Link to it instead, as [single source of truth](principles.md#6-single-source-of-truth) requires.
- Project definition, status or plans. Those are docs, specs and reports in `knowledge/`.
- Content repeated from `AGENTS.md`, in either direction.

## Changing an existing README

Change it only with the user's [approval](../agents/autonomy.md#approval). First show the user what moves out of it and where each part goes.
