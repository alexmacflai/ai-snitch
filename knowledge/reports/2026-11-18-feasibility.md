---
kind: report
description: Official-source research on zero-cost operation and initial evidence leads for AI Snitch.
---

# Zero-cost feasibility research

## Summary

Research checked on 18 November 2026 supports a public-repository GitHub Pages site with standard GitHub Actions runners and a no-LLM collector. Recommend weekly collection, monthly editorial review and automatic deployment only of approved content. This is feasible under current documented service limits; it is not a guarantee that free offerings or endpoints will remain unchanged. Recheck before activation and quarterly thereafter. No service was provisioned, account eligibility inspected, live collector tested or schedule enabled.

A curated feed/API collector can retrieve leads for zero service fees. It cannot provide comprehensive web discovery or assess the truth of a stylistic association. The proposed site should present a cultural/editorial library with bounded empirical findings, never a detector.

## Evidence

### Hosting and automation

| Source checked | Finding and implication |
|---|---|
| [GitHub Pages overview](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages) | Static HTML/CSS/JavaScript hosting; public repositories are eligible on GitHub Free. The included GitHub domain avoids purchasing a domain. Project sites have a repository base path. |
| [Pages limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits) | Published site maximum 1 GB, soft monthly bandwidth 100 GB, deployment timeout 10 minutes. This small text library should fit; that is a scale assumption. Pages restrictions exclude primarily transaction/SaaS hosting; the proposed editorial reference site fits its stated purpose. |
| [Actions billing](https://docs.github.com/en/actions/concepts/billing-and-usage) and [runner selection](https://docs.github.com/en/actions/how-tos/write-workflows/choose-where-workflows-run/choose-the-runner-for-a-job) | Standard hosted runners in public repositories are free. Recommend standard Linux only; exclude larger/paid runners. This does not promise unlimited artifact storage or private-repository usage. Keep output small and retention short. |
| [Scheduled events](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows) | Runs use default-branch workflows, may be delayed/dropped, and public-repository schedules may disable after 60 days of inactivity. Add manual dispatch and periodic operational inspection. No uptime guarantee. |
| [Workflow triggering](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow) | Token-generated pushes do not generally trigger another run. Current documentation describes approval-required PR workflow exceptions. Design the pipeline explicitly rather than assuming automated commits deploy. |

Zero monetary cost means no paid domain, server, database, search subscription or required inference service. Do not attach paid dependencies or enable billable fallback. Stop on quota/eligibility failure. Review actual account billing controls and repository settings before remote setup; this task did not inspect them. Existing local hardware and human review time are required resources, not new service purchases.

### Discovery and optional AI

- [arXiv API manual](https://info.arxiv.org/help/api/user-manual.html) and [API terms](https://info.arxiv.org/help/api/tou.html): programmatic research metadata/search, with responsible-use limits. Use small serial queries, caching and at least three seconds between requests. Check exact terms again when implementing. It discovers papers, not all conversations about writing.
- [Crossref access and authentication](https://www.crossref.org/documentation/retrieve-metadata/rest-api/access-and-authentication/): public metadata retrieval needs no registration; the polite pool identifies a contact email, and Metadata Plus is paid. Use the public free route or a maintainer-approved contact, not Plus. Read response rate/concurrency headers rather than hard-coding a supposedly permanent quota. Crossref metadata is not access to all article full text.
- RSS/Atom is a suitable no-LLM intake format where publishers provide permitted feeds. Exact publisher feed endpoints are not yet selected or tested. Free manual web searching can supplement discovery; no unattended general web-search service has been assumed. Social sites, Google search scraping and subscription-only material are excluded from the baseline.
- [Gemini Developer API pricing](https://aistudio.google.com/docs/pricing): a free tier has limited model access and free input/output tokens, with data-use conditions. It is optional only: account/region/model availability, limits and terms need fresh verification, and quota exhaustion must stop processing. No API key or billing account was configured. This is not a promise of unlimited or enduring free inference.
- [OpenAI subscription API-credit benefit](https://help.openai.com/en/articles/20001626-api-credits-benefit-for-eligible-chatgpt-subscriptions): current documentation describes conditional credits for eligible paid Pro/Business subscriptions, requiring activation; API and ChatGPT billing remain separate. Do not assume a ChatGPT subscription grants this project usable API access. It is excluded from the zero-money baseline, which requires no paid subscription or grant.
- Local open-weight inference is a possible experiment on existing hardware; compatibility, licence, quality, power use and unattended runtime have not been assessed. It adds operational work and is unnecessary for metadata collection.

### Initial pattern leads

The examples below are an internal research queue, not approved public catalogue entries. All illustrative text is invented for this project. No origin date or detection accuracy is established.

| Candidate | Invented example | Current support and missing work |
|---|---|---|
| Em-dash habit | “One small change—apparently a revolution.” | User-provided seed. No independent source for a public-perception claim validated in this pass. Research human historical usage and bounded model comparisons; earliest reported association unknown. |
| Reflexive contrast | “It is not a notebook. It is a new way to think.” | User-provided seed. No validated association source here. Define the construction, distinguish ordinary rhetorical contrast from repetitive formula and collect attributable reports. Dates unknown. |
| Inflated emotional claims | “A profoundly moving update that changes everything.” | User-provided seed. Too broad to operationalise yet. Define a narrower habit and seek reproducible or attributable evidence. Dates unknown. |
| Excess style vocabulary | “We delve into this intricate topic.” | [Kobak et al., arXiv 2406.07016](https://arxiv.org/abs/2406.07016), first submitted 11 June 2024, analyses vocabulary shifts in biomedical abstracts. It supports investigating aggregate lexical change in a specific corpus; it does not establish individual authorship or validate the other three seeds. Full methods/version review needed before publication. |
| Model lexical preferences | “The findings underscore an intricate relationship.” | [Why Does ChatGPT “Delve” So Much?](https://arxiv.org/abs/2412.11385), first submitted 16 December 2024, investigates lexical overrepresentation. It is a primary research lead; assess methods/model scope and counterevidence before generalising. |

Research dates above are submission dates from primary paper records, not dates the habits originated or were first reported anywhere. Only abstracts/records were reviewed for these leads; full-paper critical appraisal remains Phase 1 work.

[OpenAI's retired classifier report](https://openai.com/index/new-ai-classifier-for-indicating-ai-written-text/) states that the classifier was withdrawn on 20 July 2023 for low accuracy and describes false positives and scope limits. This is historical evidence of one detector's limitations, not a performance estimate for AI Snitch or every current detector. It reinforces the decision not to infer authorship from style.

## Assumptions

- A small public editorial library is acceptable; confidential candidate evidence need not be stored in its public repository.
- The initial audience reads English and can benefit from sources and editing guidance; this has not been validated with readers.
- Weekly bounded collection will be sufficient to start. Real source relevance and review effort remain unknown.
- Public GitHub Free eligibility and current terms persist until activation; actual account settings remain unchecked.

## Open questions and next steps

Follow the [rollout](../product/rollout.md). First critically review source material and create schema fixtures, including unknown dates and a rejected candidate. Choose a licence before distribution. Validate real discovery endpoints and one manual collection run before enabling automation. Public publication, repository destination, schedule activation and visual design remain future decisions.
