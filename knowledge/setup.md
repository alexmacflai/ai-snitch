---
kind: doc
description: Current local checks and the boundary between planning and future application setup.
---

# Setup

## Setting up

The public repository is [alexmacflai/ai-snitch](https://github.com/alexmacflai/ai-snitch), with `main` as its default branch. The local `origin` remote points to it. Its GitHub description, topics and website link are empty; no licence file is present and GitHub reports no licence. GitHub Pages is not enabled. Licensing remains an [open decision](product/rollout.md#open-decisions).

The workspace contains planning documents, an unpublished evidence pilot, its schema/validator and the copied Agent Development Framework. Use Python 3.9 or later. The framework checker uses the standard library; evidence validation uses the free local development dependency in `requirements-dev.txt`. No API credentials, database, site or hosting configuration is installed.

For evidence work, create an isolated environment and install its dependency:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python tools/validate_content.py
```

From the project root, run `python3 knowledge/tools/adf.py check` to verify the documentation environment.

## Commands

| Task | Command |
|---|---|
| Structural check | `python3 knowledge/tools/adf.py check` |
| Refresh routing after document changes | `python3 knowledge/tools/adf.py route` |
| Check routing | `python3 knowledge/tools/adf.py route --check` |
| Validate evidence | `.venv/bin/python tools/validate_content.py` |
| Test evidence contract | `.venv/bin/python -m unittest discover -s tests` |

Application build and preview commands are not documented yet. The optional hook is described in [tools](tools/README.md).

## Shared resources

Nothing to set up yet. No ports, test accounts or shared databases are allocated.

## Known problems

Protected `.agents/` writes required sandbox escalation during initial copying; that copy succeeded. Future tool sessions should inspect permissions rather than assume access.

Dependency installation needs package-index access; restricted network execution may require escalation. The evidence pilot was verified in `/private/tmp/ai-snitch-phase1-venv`, not a checked-in environment. Recreate `.venv` using the commands above.
