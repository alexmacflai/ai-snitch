---
name: set-up-project
description: Set up a project's knowledge, one area at a time.
---

# Set up a project

A short wizard for the start of a project. It first works out what the project is, then proposes which areas are worth setting up, and sets up the ones the user agrees to, asking only what this project needs. It gathers enough for agents to explore and work on the project, not a full definition.

## When to use

- A new project, a project that has just adopted the framework, or one with areas still missing.
- Not for: extending an area that is done; edit its files.

## Inputs

- The project's files, and the user's answers.

## Judgment

These rules apply to the wizard and to every `set-up-` skill. Work out what to ask from what you know about this project; there are no project types to choose from.

- Treat every area and topic as something to find out only if it applies to this project.
- Don't ask what the context already answers. Someone keeping a list of the songs they are working on has no audience, so don't ask about one. Say what you inferred, so the user can correct it.
- Ask a few questions at a time, only those whose answer would change the drafts, and let each answer shape the next. There is no minimum.
- Don't ask again what the user has said or a file already says, including answers given for another area.
- Make each question answerable from the message alone: plain words, no framework terms or file paths.
- Accept "doesn't apply" and "don't know yet" as answers. If it doesn't apply, remove its section. If it isn't known yet, leave its fill-in comment.

## Steps

1. Read what exists: `README.md`, `AGENTS.md`, the code, existing documentation and anything the user points to. If the project already has its own docs, follow [existing-projects.md](../../../knowledge/meta/existing-projects.md).
2. If that does not show what the project is, ask one open question before anything else: what it is, and why the user is making it.
3. Say back in a few lines what you understood, including what you inferred, and let the user correct it.
4. Fill in the project sentence and the language in `AGENTS.md`, unless they are already filled in. Take the language from the project's files or how the user writes.
5. Set up the root `README.md`, following [project-readme.md](../../../knowledge/meta/project-readme.md). If there is none, draft one from [the template](assets/README.md) and what the repository shows. If there is one, propose how to adapt it, what moves out of it and where each part goes, then wait for the user's approval.
6. Find each area's status from its files. Missing: none of its files exist. Partial: a file still has a `<!-- fill in` comment. Done: neither. `knowledge/setup.md` ships with the framework, so Environment is never missing.

   | Area | Files | Sub-skill |
   |---|---|---|
   | Product | `knowledge/product/` | [set-up-product](../set-up-product/SKILL.md) |
   | Copywriting | `knowledge/copywriting/` | [set-up-copywriting](../set-up-copywriting/SKILL.md) |
   | Design | `knowledge/design/` | [set-up-design](../set-up-design/SKILL.md) |
   | Engineering | `knowledge/engineering/` | [set-up-engineering](../set-up-engineering/SKILL.md) |
   | Environment | `knowledge/setup.md` | [set-up-environment](../set-up-environment/SKILL.md) |

7. In one message, propose which areas that are not done to set up now and which to leave out, with a one-line reason for each that comes from what the project is. Say in plain words that setting up copywriting, design or engineering adds a folder for it. The user's agreement approves creating that domain. If the project needs an area these do not cover, propose it too.
8. Run the sub-skill for each agreed area, one at a time. Finish one before starting the next. For another area, follow [maintain-structure](../maintain-structure/SKILL.md) and the rules above.
9. If the user wants to set up an area by hand, give them the path to its sub-skill's `assets/` folder, which holds the templates.

## Done when

- `AGENTS.md` says what the project is, and the root `README.md` follows [project-readme.md](../../../knowledge/meta/project-readme.md) or the user approved keeping it as it is.
- Each agreed area has at least its sub-skill's minimum.
- Areas left out have no files in `knowledge/`, except `setup.md`.
- The checker reports no errors, and the user has the status of every area.
