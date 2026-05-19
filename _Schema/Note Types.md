---
id: schema-note-types
type: schema
status: reviewed
created: 2026-05-19
last_reviewed: 2026-05-19
authored_by: claude-opus-4-7
schema_version: 0.1
---

# Note Types

Every note declares a `type:` field. The type determines which folder it lives in, which template was used, and which additional frontmatter fields are required.

## Canonical types

| `type` | Folder | Represents | Examples |
|---|---|---|---|
| `concept` | `Concepts/` | An idea, term, theory, framework, mechanism, or distinction | Alignment, Mesa-Optimization, Moral Patienthood |
| `person` | `People/` | An individual contributor — researcher, philosopher, policymaker, founder | Stuart Russell, Robert Long, Margaret Mitchell |
| `org` | `Organizations/` | An institution, lab, NGO, company, agency, consortium | Anthropic, MIRI, AI Forum NZ |
| `paper` | `Papers/` | A research paper, preprint, technical report, or book | "Concrete Problems in AI Safety" (Amodei et al. 2016) |
| `policy` | `Policies/` | A law, regulation, charter, executive order, or formal framework | EU AI Act, NZ Algorithm Charter |
| `debate` | `Debates/` | A structured presentation of opposing positions on an open question | "Should AI development pause?" |
| `event` | `Events/` | A conference, incident, launch, milestone, or dated occurrence | NeurIPS 2024, GPT-4 release, AI Seoul Summit |
| `dataset` | `Datasets/` | A research dataset or empirical corpus | HELM benchmark, MMLU |
| `case` | `Cases/` | A legal case or documented real-world incident | Authors Guild v OpenAI, Air Canada chatbot case |
| `synthesis` | `_Synthesis/` | An interpretation, judgment, or position **authored by the organization** — never neutral | "Why we believe X" — see `_Meta/Editorial Standards.md` |
| `moc` | `_Indexes/` | A Map of Content — curated index or query view | "MOC — Alignment Research" |
| `schema` | `_Schema/` | A schema or operating-system file (this category) | This file |
| `meta` | `_Meta/` | An editorial, operational, or process document | Editorial Standards, Source Tier System |

## Type selection rules

- A note has **exactly one** `type`. If it seems to need two, split it into two notes.
- Prefer the more specific type. A paper that introduces a concept produces **two** notes — a `paper` note for the artifact and a `concept` note for the idea — linked via `defined-by::` and `cites::`.
- Never use `concept` as a catch-all for "stuff that's not the other types." If no type fits, propose a new type by editing this file (and bump schema version).

## Synthesis is special

`type: synthesis` is the **only** type that may express a position the organization endorses. All other types stay descriptive. A synthesis note must also carry `endorsed_by:` (an array of human or AI identifiers with provenance) — see [[Frontmatter Schema]].
