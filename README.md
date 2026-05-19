---
id: vault-readme
type: meta
status: reviewed
created: 2026-05-19
last_reviewed: 2026-05-19
authored_by: claude-opus-4-7
---

# Trust — Research Vault

Internal research foundation for a New Zealand non-profit preparing humanity for stable, peaceful coexistence with AI ("carbon and silicon life").

## What this is

This vault is **AI-optimized research infrastructure**. Primary consumers: AI research agents (Claude Opus-class models and similar) operating on behalf of the organization, plus a smaller number of human researchers who themselves use AI assistance. The vault is **not** public-facing — public-facing products are derived from it.

## Stance

Neutral information aggregator. The vault records the full spectrum of views, evidence, and arguments without endorsing any single position. The exception is `_Synthesis/`, where the organization's own interpretations are recorded — these entries are explicitly labeled with `type: synthesis` and full author provenance so they can never be confused with neutral content.

## Where to start (for an AI agent)

1. Read `_Schema/README.md` — this defines the data model. Every note in the vault conforms to it.
2. Read `_Meta/Editorial Standards.md` — this defines how to write, cite, and label perspectives.
3. Read `_Meta/Session Log.md` — see what prior sessions did and what's pending.
4. Read `_Meta/Curation Backlog.md` — pick up open research tasks.

## Where to start (for a human reader)

Open `Home.md`. It contains the dashboard view and entry points by topic, type, and recent activity.

## Top-level layout

```
Concepts/      People/      Organizations/    Papers/
Policies/      Debates/     Events/           Datasets/
Cases/         _Synthesis/  _Meta/            _Schema/
_Templates/    _Indexes/    _Attachments/
```

Folders are **type-based**, not topic-based. Topic organization is provided by frontmatter tags and Dataview index views in `_Indexes/`. This is intentional: the vault is a graph, not a tree.
