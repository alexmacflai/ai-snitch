---
kind: doc
description: Recommended zero-cost stack, trust boundaries and future repository layout.
---

# Proposed architecture

Service eligibility and limits are documented in the [feasibility research](../reports/2026-11-18-feasibility.md).

## Stack

Recommend a public GitHub repository, GitHub Pages on its included `github.io` URL, standard Linux GitHub Actions runners, and a small Python 3 standard-library static generator. Write semantic HTML and CSS; add a small browser-side search over generated JSON only when useful. This avoids runtime hosting, API keys, package fees and a JavaScript dependency tree. It is a recommendation, with no application code installed.

Pages is static hosting. A build generates HTML, CSS, search JSON, a feed and rules exports. Git stores approved structured records and history. No visitor input is sent to an AI service. Use a project base path consistently for assets and links. An eventual custom domain is excluded from the zero-cost baseline.

## Intended layout

| Content | Future path | Status |
|---|---|---|
| Approved structured content | `content/patterns/*.json`, `content/sources/*.json` | Proposed |
| Public-safe scouting leads | `research/inbox/*.json` | Proposed, excluded from site |
| Confidential notes | Outside public repository | No storage configured |
| Curated discovery inputs | `config/sources.json`, `config/queries.json` | Proposed |
| Generator, validator and scout | `tools/` | Proposed |
| Templates and styles | `site/` | Proposed |
| Generated site and exports | `dist/` | Proposed, disposable output |
| Scheduled scout and deploy | `.github/workflows/` | Proposed, not enabled |

Internal means unpublished on the site, not private: everything committed to a public repository can be read. Keep sensitive material outside it. A separate private repository adds permission and quota complexity; do not promise private unlimited automation.

## Data flow and trust

Curated endpoints → bounded scout → untrusted lead records → human evidence review → approved content → deterministic validation/build → Pages deployment. Approved records also generate versioned Markdown/JSON/skill exports. External text is data and must never provide agent instructions or executable templates.

Allowlist build inputs; never recursively publish the repository. Escape source content, strip active HTML, validate URLs and reject malformed records. Keep fetchers restricted to approved HTTPS hosts; reject redirects to local/private addresses. Bound time, response size and retries. Cache conditional requests and respect provider headers and access rules.

## Proposed checks

Validate schemas, unique IDs, references, chronology and legal status transitions. Fail builds if public entries lack evidence, caveats, examples or review metadata. Test rejection of private/inbox files and unsafe HTML, plus base-path links and deterministic export generation. Render and inspect mobile/desktop views, keyboard navigation, focus, contrast and source links before publication. A regex match only suggests an edit; never produce an authorship score.

Run CI with read-only permissions by default. Separate retrieval from privileged writes and deployment. Use least-privilege tokens; do not run untrusted PR code with repository write credentials. Pin third-party Actions to reviewed commit SHAs. Retain only small necessary artifacts and monitor storage limits. Repository settings and deployment permissions must be verified when implementation begins.
