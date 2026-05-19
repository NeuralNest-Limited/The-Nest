---
id: meta-git-commit-conventions
type: meta
status: reviewed
created: 2026-05-19
last_reviewed: 2026-05-19
authored_by: claude-opus-4-7
schema_version: 0.1
---

# Git Commit Conventions

Every commit is an audit record. Multi-agent work makes commit hygiene load-bearing — a bad commit message in this vault means a future agent can't reconstruct why a note changed.

## Format

```
<type>(<scope>): <subject>

<body — required for non-trivial commits>

Session: <session-id>
Author-agent: <model-id-or-human-handle>
```

## Types

| Type | Use |
|---|---|
| `note` | Create or modify a content note (any type) |
| `schema` | Modify anything in `_Schema/` |
| `meta` | Modify anything in `_Meta/` |
| `template` | Modify `_Templates/` |
| `index` | Modify `_Indexes/` (MOCs, Dataview views) |
| `synthesis` | Create or modify a `_Synthesis/` note |
| `vocab` | Add or modify controlled vocabulary terms |
| `rel` | Add or modify relationship types |
| `fix` | Correct an error in an existing note (factual, citation, typo at scale) |
| `chore` | Housekeeping, file moves, bulk renames |
| `session` | Session log entries (allowed but discouraged — prefer batching) |
| `init` | Initial / structural commits |

## Scope

The scope is the folder or area affected: `concepts`, `people`, `papers`, `policies`, `synthesis`, `schema/vocabulary`, etc.

For multi-folder commits, omit scope or use the dominant area.

## Subject

- Imperative mood: "Add X" not "Added X" / "Adds X".
- ≤ 72 chars.
- Specific: `note(concepts): add mesa-optimization with Hubinger 2019 sourcing` beats `note: add concept`.

## Body

For commits that:
- Create more than one note,
- Touch schema or vocabulary,
- Change `status` of a reviewed note,
- Introduce a new relationship type,
- Make any decision a future agent might need rationale for,

include a body explaining **why** and listing affected note IDs.

## Required trailers

```
Session: 2026-05-19-001
Author-agent: claude-opus-4-7
```

Session IDs are `YYYY-MM-DD-NNN` where NNN is the Nth session that day. Coordinate via `Session Log.md` to avoid collisions (read the latest entry, pick the next index).

For sessions that span multiple commits, the same Session trailer appears on each.

## Examples

```
note(concepts): add mesa-optimization stub

Created stub linking to Hubinger et al. 2019 as primary source.
Body to be filled in next session — sourced 6 secondary references
recorded in Curation Backlog under task #14.

Session: 2026-05-19-001
Author-agent: claude-opus-4-7
```

```
schema: add 'tested-on::' relationship type for benchmarks

Added to _Schema/Relationship Types.md to support precise tracking
of which methods were evaluated on which datasets. Validated against
existing notes — no retro-fitting needed; only new notes will use it.

Session: 2026-05-19-001
Author-agent: claude-opus-4-7
```

```
fix(papers): correct Russell 2019 publication year (Penguin → Viking)

Source verification flagged conflicting publisher metadata. Verified
against publisher record. Updated bibliographic entry in
papers/russell-human-compatible-2019.md.

Session: 2026-05-19-001
Author-agent: claude-opus-4-7
```

## What NOT to do

- Bulk commits with vague messages ("update notes", "various edits"). If you can't summarize it, you're probably committing too much at once.
- Squashing across sessions. Each session's commits stay distinct for audit.
- Force-pushing main. The vault's main branch is append-only history; corrections happen via new commits or `git revert`.
- Skipping the trailers. They are how multi-agent attribution works.

## Branching

For exploratory or speculative work, agents may use feature branches:

```
git checkout -b explore/<session-id>-<short-topic>
```

Merges to main via fast-forward where possible, otherwise standard merge commits. No rebasing of main.

For now (single-agent, kickoff phase), work directly on `main` is fine. As multi-agent activity ramps, branches become more important.
