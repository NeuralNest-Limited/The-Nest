---
id: schema-validation
type: schema
status: reviewed
created: 2026-05-19
last_reviewed: 2026-05-19
authored_by: claude-opus-4-7
schema_version: 0.1
---

# Validation Rules

A note is **well-formed** iff all rules below pass. Future tooling (a `validate.py` script in `_Meta/Tools/`) will enforce these automatically. For now, agents self-validate before commit.

## Block A — YAML

1. The note begins with a `---` line.
2. A second `---` line closes the frontmatter, with no blank line before it.
3. The block between them parses as valid YAML.
4. No duplicate keys.
5. Date fields are ISO-8601 (`YYYY-MM-DD`).

## Block B — Universal required fields

For every note:
- `id` (string, matches kebab-case pattern from [[ID Conventions]])
- `title` (string)
- `type` (token from [[Note Types]])
- `status` (token from [[Vocabulary]])
- `created` (ISO date)
- `last_reviewed` (ISO date)
- `authored_by` (token or array of tokens)
- `schema_version` (string)

## Block C — Content-bearing required fields

For notes with `status` in `{draft, reviewed, needs-update, contested}` (i.e., NOT stub/archived):
- `summary` (string, ≤ 280 chars)
- `topics` (non-empty array, every member ∈ [[Vocabulary]] topics)

If the note makes empirical claims:
- `confidence` (float 0.0–1.0)
- `source_tier` (int 1–5)
- `sources` (non-empty array of well-formed source objects)

## Block D — Type-specific required fields

See [[Frontmatter Schema]] §"Type-specific REQUIRED extensions". Each note type adds its own required fields.

Validators must:
1. Read `type:` from frontmatter.
2. Look up the type's required field set.
3. Confirm each field is present and well-typed.

## Block E — Controlled vocabulary

For every field whose values are constrained by [[Vocabulary]]:
- The value resolves to a defined token.
- Hierarchical topics: if `ai-safety/alignment/inner` is used, `ai-safety/alignment` and `ai-safety` must also exist in `Vocabulary.md` (they don't have to be tagged on the note).

## Block F — Relationships

For every `RELATION:: [[Target]]` in the body:
- `RELATION` is a known relation from [[Relationship Types]] OR `related::` / `see-also::`.
- `[[Target]]` resolves to an existing note in the vault (no dangling links in `reviewed` status notes). Stubs and drafts MAY have dangling links — these become curation backlog items.

## Block G — Source objects

Each entry in `sources:` has at minimum:
- `type` (one of [[Vocabulary]] source types — TODO: add formal list)
- `title` (string)
- one of `{url, doi, arxiv_id}` resolving to something verifiable
- `accessed` (ISO date) if the source is web-based

## Block H — Stance discipline

For `type: concept | paper | policy | event | etc.` (descriptive types):
- `perspective:` if present must be `neutral` or `descriptive`, OR the note must explicitly flag in body that it is summarizing a single position (e.g., "## Summary of the cautious position on X").
- The note body must not endorse a contested position. If it does, the note should be converted to `type: synthesis` and moved to `_Synthesis/`.

For `type: synthesis`:
- `perspective:` is required and may be any value.
- `endorsed_by:` is required.
- `endorsement_status:` is required.

## Block I — ID uniqueness

Across the entire vault, `id` values are unique. The validator must check for duplicates.

## Block J — Status hygiene

- A note with `status: needs-update` must have at least one `needs_attention:` flag explaining what needs updating.
- A note with `status: archived` must have a `supersedes::` link to its successor (if any).
- A note with `status: contested` must link to a `debate` note via `position-in::` or contain its own debate structure.

## Severity levels

Failures are classified:

| Severity | Action |
|---|---|
| **ERROR** | Block A, B, D, I failures. Note cannot be committed in this state. |
| **WARN** | Block C, E (unknown vocab term), F (dangling links in `reviewed` notes), G failures. Allowed but logged. |
| **INFO** | Block H, J subtleties. Surfaced to curators for follow-up. |

## Until tooling exists

Each authoring AI self-validates by:
1. Re-reading the note after writing.
2. Checking each block above.
3. If any ERROR-level check fails, fixing before commit.
4. If any WARN-level check fails, adding a `needs_attention:` entry.
