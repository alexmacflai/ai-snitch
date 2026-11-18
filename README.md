# AI Snitch

An evolving library of writing habits associated with AI-generated copy, with examples, sources and room to change our minds.

## Layout

- `knowledge/`: product brief, evidence model, voice, technical recommendations, research and framework guidance.
- `content/` and `schemas/`: unpublished evidence pilot and JSON contract.
- `tools/` and `tests/`: local evidence validation and regression tests.
- `.agents/skills/`: reusable framework workflows; `.claude/skills` points here.
- `.gemini/`: framework agent configuration.

## Getting started

This is a planning and evidence-pilot workspace. There is no application or deployment yet. With Python 3.9 or later, check it from this folder:

```sh
python3 knowledge/tools/adf.py check
python3 knowledge/tools/adf.py route --check
```

For evidence setup and tests, follow [setup](knowledge/setup.md). Start the review with the [pilot report](knowledge/reports/2026-11-18-evidence-pilot.md).

Before pushing, run these checks and the evidence tests. The optional pre-commit hook is described in [tools](knowledge/tools/README.md); it is not installed here.

This project uses the Agent Development Framework. Start with [AGENTS.md](AGENTS.md) and [knowledge](knowledge/README.md). Read the [brief](knowledge/product/product.md), [rollout plan](knowledge/product/rollout.md) and [research](knowledge/reports/2026-11-18-feasibility.md).
