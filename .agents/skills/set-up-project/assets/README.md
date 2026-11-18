<!-- template: Copy to README.md at the repository root, following knowledge/meta/project-readme.md. Write it from what the repository shows, not from memory. A root README carries no front-matter. Turn each path below into a Markdown link once the file is at the root. Remove any section that does not apply, then remove this comment. -->

# <!-- fill in: the project's name -->

<!-- fill in: what the project is and who it is for, in a sentence or two. -->

## Layout

<!-- fill in: one row per top-level folder, in the order a reader meets them. Keep each to one line. -->

| Folder | What it holds |
|---|---|
| `knowledge/` | Instructions, docs, specs and reports for people and agents |
| `.agents/skills/` | Procedures agents follow for recurring tasks |

## Getting started

<!-- fill in: the prerequisites, then the fewest commands that get the project running, taken from knowledge/setup.md and proven to work. Do not restate the rest of that file. -->

```bash
<!-- fill in: the commands -->
```

## Checks

Before pushing, run the conventions checker and fix every error:

```bash
python3 knowledge/tools/adf.py check
```

<!-- fill in: the project's own build, test and lint commands, if it has any. -->

To have every commit checked, install the pre-commit hook described in `knowledge/tools/README.md`.

<!-- fill in: anything else that is for people only, such as a licence, badges, a screenshot or how to contribute. -->

## For agents

This project follows the Agent Development Framework. Agents start at `AGENTS.md`; the conventions are in `knowledge/meta/`, and everything the project knows about itself is in `knowledge/`.
