---
name: audit-tags
description: Audit registries and documents for useful, consistent topic tags.
---

# Audit tags

Reviews tags against document content and recommends merges, renames, additions and removals that improve discovery across folders. It looks at each document and at topics that only show up across many documents.

## When to use

- Reviewing a project's tags and their application across documents.
- Not for: tagging a document during ordinary work; follow the tag rules directly.

## Inputs

- The project root and any requested scope. Default to all Markdown in `knowledge/` and `.agents/skills/`, plus registries referenced by those files.

## Steps

1. Read the project's entry points and tag rules, starting at [knowledge/meta/](../../../knowledge/meta/README.md). Identify the applicable registries and any approval requirements.
2. Enumerate the documents and registries before reviewing. Keep copied projects, archives and source trees separate where their registries or purposes differ. `SKILL.md` files carry no tags: skim them only for references to tags or registries. For files copied unchanged from an upstream source, such as framework skills and templates, recommend changes upstream rather than local edits. Record exclusions and unreadable files; never present a partial review as a full audit.
3. Build a tag inventory: each name, definition, registry, the files whose front-matter uses it, and the folders those files are in. Flag unregistered uses, duplicate or conflicting definitions, unused registrations and tags used inside one folder only. Do not count generated routing tables, examples or body mentions as tag assignments.
4. Read every document's body in scope, including untagged documents. Work in batches if needed, maintaining a coverage list. For each document, note its substantive topics. Test each existing assignment: would someone searching for this topic want this document? A passing mention fails.
5. Look across all the documents. From the topic notes, collect topics, entities and rules that recur in more than one folder. Include themes no single document is about, and invariants or rules restated in several places. A term that recurs across folders is a lead, not evidence; confirm the topic in the bodies. For each candidate, decide:
   - **Reuse** an existing tag only when a reader looking for this topic would search for that tag. Close in meaning is not enough.
   - **Add** a new registered tag when no existing tag would be searched for. A single source with links to it does not replace a tag: links lead to the rule, a tag finds every place the topic comes up.
   - **Reject** it, with the reason and evidence.
6. Compare meanings and actual uses across the inventory. Recommend:
   - **Merge** near-synonyms when one definition fits all affected documents; preserve distinctions that help readers find different topics.
   - **Rename** misleading or inconsistent names, naming the replacement and its definition.
   - **Add** missing assignments and the new tags from step 5.
   - **Remove** irrelevant assignments, redundant labels or unused registrations. A useful tag with one document is valid; usage count alone is not a reason to remove it. A tag used inside one folder only is a candidate for merging or removal, because tags exist to find material across folders.
7. Report coverage and findings in chat unless another output was requested. For each finding, give the action, old and proposed tag or definition, affected file paths, content evidence and discovery benefit. Distinguish registry changes from assignment changes. List every candidate considered and rejected, with its reason. Do not manufacture findings to fill a quota, and do not drop a candidate without a stated reason. Say when no change is justified.
8. If the user requested implementation, apply changes within that authorisation and the project's approval rules. Update every affected assignment and registry together; remove an old registration only after its uses are gone. Preserve document bodies. Regenerate routing and run the project's checks. Otherwise finish with recommendations.

## Done when

- Every document and registry in scope is accounted for as read or explicitly not reviewed.
- Every topic that recurs across folders has a decision (reuse, add or reject) with its reason.
- Recommendations are grounded in document content, with precise affected paths and replacement mappings.
- Applied changes, if requested, have consistent registries, assignments and routing, with check results reported.

Behaviour cases: [evaluations.md](evaluations.md).
