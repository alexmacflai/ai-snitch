---
kind: doc
description: Current local checks and the boundary between planning and future application setup.
---

# Setup

## Setting up

The workspace currently contains planning documents and the copied Agent Development Framework. Use Python 3.9 or later; the framework checker uses the standard library. No application dependencies, API credentials, database or hosting configuration are installed.

From the project root, run `python3 knowledge/tools/adf.py check` to verify the documentation environment.

## Commands

| Task | Command |
|---|---|
| Structural check | `python3 knowledge/tools/adf.py check` |
| Refresh routing after document changes | `python3 knowledge/tools/adf.py route` |
| Check routing | `python3 knowledge/tools/adf.py route --check` |

Application build, tests and preview commands do not exist yet. The optional hook is in [tools](tools/README.md); no Git repository or hook was initialised by this setup.

## Shared resources

Nothing to set up yet. No ports, test accounts or shared databases are allocated.

## Known problems

Protected `.agents/` writes required sandbox escalation during initial copying; that copy succeeded. Future tool sessions should inspect permissions rather than assume access.
