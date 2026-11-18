# Agent instructions

AI Snitch is an evolving, evidence-led library of stylistic patterns associated with AI-generated copy. Its purpose is described in `README.md`.

Write in British English.

## Rules for every task

- Before creating or editing a Markdown file in `knowledge/` or `.agents/skills/`, follow [knowledge/meta/](knowledge/meta/README.md).
- Follow [knowledge/agents/](knowledge/agents/README.md): when to act or ask, scope, conflicts, communication, verification, safety and learning.
- Choose guidance by what the work changes, not how the request is worded: work that changes what users read is copywriting work; work that changes how the interface looks or behaves is design work. Reproducing supplied copy or a supplied design exactly needs no domain guidance.
- Before committing, run `python3 knowledge/tools/adf.py check` and fix every error.
- Use the authenticated GitHub connector for GitHub work; do not use `gh` authentication. If unavailable, report the exact recovery step once.
- Keep all project services and operations at zero monetary cost.
- Treat recommendations as proposals until implementation is authorised.

## Routing

| If you are…                               | Read                                                   | Then use |
|-------------------------------------------|--------------------------------------------------------|----------|
| Setting up the project's knowledge        | —                                                      | [set-up-project](.agents/skills/set-up-project/SKILL.md) |
| Starting or picking up a task             | [knowledge/agents/](knowledge/agents/README.md)        | [start-task](.agents/skills/start-task/SKILL.md) |
| Investigating a problem                   | [knowledge/setup.md](knowledge/setup.md)               | [investigate-problem](.agents/skills/investigate-problem/SKILL.md) |
| Verifying work                            | [verification.md](knowledge/agents/verification.md)    | [verify-work](.agents/skills/verify-work/SKILL.md) |
| Planning work that needs a spec           | [writing/specs.md](knowledge/meta/writing/specs.md)    | [write-spec](.agents/skills/write-spec/SKILL.md) |
| Reviewing a change                        | [verification.md](knowledge/agents/verification.md)    | [review-change](.agents/skills/review-change/SKILL.md) |
| Auditing tags across documents            | [tags.md](knowledge/meta/tags.md)                      | [audit-tags](.agents/skills/audit-tags/SKILL.md) |
| Recording how a recurring change is done  | [writing/docs.md](knowledge/meta/writing/docs.md#pattern-docs) | [document-pattern](.agents/skills/document-pattern/SKILL.md) |
| Exploring, developing or refining designs | [.agents/skills/](.agents/skills/README.md)              | [design-with-ai](.agents/skills/design-with-ai/SKILL.md) |
| Editing generic copy while preserving voice | [.agents/skills/](.agents/skills/README.md)            | [humanise-copy](.agents/skills/humanise-copy/SKILL.md) |
| Handing off unfinished work               | —                                                      | [hand-off](.agents/skills/hand-off/SKILL.md) |
| Working alongside other agents            | [parallel-work.md](knowledge/agents/parallel-work.md)  | —        |
| Adding, moving or removing files or domains | [knowledge/meta/](knowledge/meta/README.md)          | [maintain-structure](.agents/skills/maintain-structure/SKILL.md) |
| Setting up, building, testing or running  | [knowledge/setup.md](knowledge/setup.md)               | —        |
| Looking for a skill                       | [.agents/skills/](.agents/skills/README.md)            | —        |
| Defining scope or editing patterns | [product](knowledge/product/README.md) | — |
| Writing public copy | [copywriting](knowledge/copywriting/README.md) | — |
| Planning implementation or scouting | [engineering](knowledge/engineering/README.md) | — |
