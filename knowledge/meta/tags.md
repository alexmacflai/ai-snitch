---
kind: instruction
description: The tag rules and the framework's own tags, which group material on one topic across folders.
tags: [tagging]
---

# Tags

Tags label files by topic across folders, so material on one topic can be found even when it lives in different domains. Folders say where a file belongs; tags say what else it relates to.

## Using tags

- To find material on a topic across folders, search front-matter for its tag: `grep -rl "^tags:.*verification" --include="*.md" .`
- Use only tags from a registry, such as the table below.
- Format: lowercase kebab-case, flat (no hierarchy).
- Do not tag what is true of everything in the folder or the project.
- Before adding a tag, look for a registered tag with nearly the same meaning and use it instead, such as `testing` rather than `qa`.
- If no suitable registered tag exists, introduce one when the document covers a topic useful for discovery across folders. Register it in the same change. A tag may initially apply to one document; finding or tagging other documents is not required.
- Remove a tag from the registry only when no file uses it.

A registry is a table:

```markdown
| Tag | Meaning |
|---|---|
| `verification` | Proving that work is correct. |
```

A registry has no size budget: it grows with the project.

For a review of registries and document tagging together, use [audit-tags](../../.agents/skills/audit-tags/SKILL.md).

## Tags

| Tag | Meaning |
|---|---|
| `interface` | What people see and use: screens, components, interface text. |
| `principles` | The principles that settle decisions. |
| `routing` | How readers find the files a task needs: entry points and routing tables. |
| `structure` | Where material lives: folders, kinds, domains, layout. |
| `tagging` | How files are labelled and found across folders. |
| `terminology` | The words the product uses, and the ones it avoids. |
| `testing` | Tests and checks, and when work counts as done. |
| `users` | Who uses the product and what they need. |
