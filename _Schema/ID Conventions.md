---
id: schema-id-conventions
type: schema
status: reviewed
created: 2026-05-19
last_reviewed: 2026-05-19
authored_by: claude-opus-4-7
schema_version: 0.1
---

# ID Conventions

Every note has an `id:` in its frontmatter. The ID is the **stable, permanent identifier** for the note. Filenames may change; IDs do not.

## Why a separate ID from filename?

Obsidian uses filenames as link targets. If a note is renamed, every `[[wikilink]]` to it is auto-updated by Obsidian. But:

1. External tools and scripts often track notes by ID, not filename.
2. Renames break URL-style references in exported sites.
3. Across forks or splits, IDs preserve provenance.

The ID is the **canonical handle** in any non-Obsidian context (Dataview queries, scripts, external publishing, git history analysis).

## Generation rules

IDs are **kebab-case ASCII slugs**, ≤ 80 characters, derived from the note's first canonical title. Once written, they are immutable.

### By type

| Type | ID pattern | Example |
|---|---|---|
| `concept` | `<concept-slug>` | `mesa-optimization`, `moral-patienthood` |
| `person` | `<firstname-lastname>` | `stuart-russell`, `robert-long` |
| `person` (homonym) | `<firstname-lastname>-<birthyear>` | `john-smith-1972` |
| `org` | `<org-slug>` | `anthropic`, `miri`, `ai-forum-nz` |
| `paper` | `<firstauthor-shortname-year>` | `amodei-concrete-problems-2016` |
| `policy` | `<jurisdiction>-<policy-slug>` | `eu-ai-act`, `nz-algorithm-charter` |
| `case` | `<plaintiff>-v-<defendant>-<year>` | `authors-guild-v-openai-2023` |
| `event` | `<event-slug>-<year>` | `ai-seoul-summit-2024` |
| `dataset` | `<dataset-slug>` | `mmlu`, `helm-benchmark` |
| `debate` | `debate-<topic-slug>` | `debate-pause-frontier-ai` |
| `synthesis` | `synthesis-<topic-slug>-<yyyymm>` | `synthesis-nz-coexistence-stance-202605` |
| `moc` | `moc-<topic-slug>` | `moc-alignment-research` |
| `schema` | `schema-<topic>` | `schema-frontmatter` |
| `meta` | `meta-<topic>` | `meta-editorial-standards` |

### Slugification rules

1. Lowercase only.
2. Replace whitespace and `_` with `-`.
3. Strip diacritics (`Māori` → `maori`). For Te Reo Māori terms, also create an `aliases:` entry preserving the macron form so retrieval by macron still works.
4. Drop punctuation except `-`.
5. Collapse multiple `-` to single.
6. Trim leading/trailing `-`.

### Avoid

- Trailing year unless required for disambiguation (`alignment` not `alignment-2026`).
- Org acronyms when the full name is short enough (`anthropic` not `anth`).
- IDs that reference the **current** organization's framing (`our-stance-on-x`) — IDs should make sense to any future agent.

## Immutability

Once a note is committed, its `id:` does not change. Specifically:

- If the title is changed, the ID stays.
- If the file is moved between folders (type change), the ID stays unless the type slug prefix would now be wrong, in which case **the note is archived and a new note is created** linking back via `supersedes::`.
- If two notes turn out to be duplicates, one is archived (status `archived`) and a `supersedes::` link is added pointing to the surviving one. IDs of both are preserved.

## Filename vs ID divergence

Best practice: keep filename and ID aligned when possible (filename = `Title Case With Spaces.md`, ID = kebab-case slug of the title). When they diverge, the ID is authoritative.

## Generating an ID for a new note

1. Pick the canonical title.
2. Apply slugification rules.
3. Apply the type pattern.
4. Search the vault for the candidate ID — must be unique.
5. If collision and it's the same entity, use the existing note. If it's a homonym, disambiguate per the homonym pattern.

A simple shell check:
```bash
grep -r "^id: <candidate-id>$" /Users/zhaoziyuan/NeuralNest/trust --include="*.md"
```
