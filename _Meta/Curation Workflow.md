---
id: meta-curation-workflow
type: meta
status: reviewed
created: 2026-05-19
last_reviewed: 2026-05-19
authored_by: claude-opus-4-7
schema_version: 0.1
---

# Curation Workflow

The lifecycle of a note, the protocol for picking up work, and the protocol for handing off.

## Note lifecycle

```
[idea]
   │
   ▼
[backlog entry in Curation Backlog]
   │
   ▼  (agent claims)
[stub]   ← frontmatter + 1-2 sentence summary, no body yet
   │
   ▼  (research + drafting)
[draft]   ← substantive content, sources, typed relationships
   │
   ▼  (second agent or human reviews)
[reviewed]   ← verified by a different identity than the drafter
   │
   ├──→ [needs-update] (if later found stale)
   ├──→ [contested] (if disagreement emerges, see Editorial Standards)
   └──→ [archived] (if superseded; preserve via supersedes::)
```

## Session protocol (every AI session)

### On entry

1. Read `_Meta/Session Log.md` — last ~5 entries. Understand recent state.
2. Read `_Meta/Curation Backlog.md` — pick a task, or work on one the user assigns.
3. `git status` and `git log --oneline -10` — verify clean state.
4. Append a session-start entry to `Session Log.md` (see template in that file).

### During work

1. For each note created/edited:
   - Self-validate per [[Validation Rules]].
   - Add `review_history` entry.
   - Update `last_reviewed` if you verified content (don't update if you only added new sections without verifying existing ones).
2. If a backlog item is completed, mark it done in `Curation Backlog.md` with date and resulting note IDs.
3. If you discover new gaps, add them to `Curation Backlog.md`.

### On exit

1. Append a session-end entry to `Session Log.md`: what was done, what was attempted but not completed, known issues left behind.
2. Commit your changes per [[Git Commit Conventions]].
3. Note any decisions that should escalate to a human researcher in `needs_attention:` fields and call them out in the session log.

## Claiming work

If multiple agents may be active:

- The backlog item gets an `owner:` field with the session ID claiming it.
- `Curation Backlog.md` is read-modify-write through git — concurrent claims resolved by merge.
- A claim older than 24h with no commit activity is considered stale and may be reclaimed.

## Review protocol

For a draft → reviewed transition:

- The reviewing agent must be a different `authored_by:` identity than the drafter (different model session, or a human).
- Reviewer reads the full note, verifies a sample of sources by accessing them, checks vocabulary compliance, checks relationship types.
- Reviewer either:
  - Promotes to `status: reviewed`, adds review_history entry.
  - Sends back with `status: draft` + `needs_attention:` flags listing concrete issues.

A note cannot be reviewed by its drafter. (Self-edits are fine; self-review is not.)

## Archival

A note becomes `archived` when:
- Definitively superseded by a newer note (`supersedes::` mandatory).
- Established as a duplicate of an existing note (link to the canonical one).

Archived notes are kept in their original folder. They show up in queries with `where status = archived` filters.

## Splits and merges

- **Split**: when a note grows beyond 3000 words or its scope drifts, split into atomic notes. Keep the original as a stub linking to the parts via `part-of::` (children) or `subclass-of::` (children specialize parent).
- **Merge**: when two notes turn out to be the same thing, archive the one with fewer in-bound links; the surviving note gains the other's aliases and content; `supersedes::` link recorded.

## Backlog hygiene

`Curation Backlog.md` is the org's TODO list. Entries should:

- Have a clear scope ("Write concept note for `mesa-optimization`") not vague aspirations.
- Reference any seed sources known to the author.
- Be sized to ~1-3 hours of agent work, or split.
- Be tagged with topic and priority.

Quarterly (or as needed), prune the backlog of stale items and reorganize.
