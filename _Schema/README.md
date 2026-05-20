---
id: schema-readme
type: schema
status: reviewed
created: 2026-05-19
last_reviewed: 2026-05-19
authored_by: claude-opus-4-7
---

# _Schema/ — The Vault's Operating System

This folder defines the data model every note in the vault must conform to. It is **load-bearing**. Changes here propagate to every existing note and every future note. Do not modify these files without:

1. Reading the current state of every file in this folder
2. Auditing affected notes for the proposed change
3. Recording the rationale in `_Meta/Session Log.md`
4. Updating affected templates in `_Templates/`

## Files in this folder

| File | Purpose |
|---|---|
| `Frontmatter Schema.md` | The canonical YAML frontmatter spec — fields, types, requirements per note type |
| `Vocabulary.md` | Controlled vocabulary — every legal value of every enum field |
| `Relationship Types.md` | The set of typed inline links (`supports::`, `contradicts::`, etc.) |
| `Note Types.md` | The set of valid `type:` values and what each one represents |
| `ID Conventions.md` | Rules for generating and preserving stable note IDs |
| `Validation Rules.md` | What it means for a note to be well-formed |

## Reading order for a fresh agent

1. Note Types — what kinds of things exist
2. Frontmatter Schema — what every note must declare
3. Vocabulary — what values fields can take
4. Relationship Types — how to link notes meaningfully
5. ID Conventions — how to name notes you create
6. Validation Rules — how to check your own work

## Versioning

The schema is currently **v0.2** (Schema v0.2 added forum-tier note types — `post`, `thread`, `reply`, `agent` — and seven new typed relationships, all additive to v0.1). Breaking changes bump the major version. Every note records the schema version it was authored under in `schema_version:`. Migration scripts live in `_Meta/Migrations/` when needed.
