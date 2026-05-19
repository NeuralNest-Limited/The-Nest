---
id: schema-relationships
type: schema
status: reviewed
created: 2026-05-19
last_reviewed: 2026-05-19
authored_by: claude-opus-4-7
schema_version: 0.1
---

# Relationship Types

A plain Obsidian `[[wikilink]]` says "these two notes are related" — that's a low-information signal. For AI consumption, we use **typed inline relationships** via Dataview inline metadata syntax: `relationship_type:: [[Target Note]]`.

Typed relationships appear in the body of a note (not the frontmatter), usually under a `## Relationships` section or inline near the relevant claim.

## Canonical relationship types

### Argumentative / epistemic

| Relation | Direction | Meaning |
|---|---|---|
| `supports::` | A → B | A provides evidence or argument supporting B's claim. |
| `contradicts::` | A → B | A provides evidence or argument against B's claim. |
| `refines::` | A → B | A narrows, qualifies, or sharpens B. |
| `extends::` | A → B | A builds on B, generalizing or developing further. |
| `responds-to::` | A → B | A was written in reply to B. |
| `supersedes::` | A → B | A replaces B as the current best account. |
| `criticizes::` | A → B | A is a critique of B (weaker than contradicts; includes methodological critique). |

### Definitional / structural

| Relation | Direction | Meaning |
|---|---|---|
| `defined-by::` | A → B | The formal definition of A lives in B. |
| `instance-of::` | A → B | A is an example or instance of the category B. |
| `subclass-of::` | A → B | A is a narrower category than B. |
| `part-of::` | A → B | A is a component of the larger B. |
| `coined-by::` | A → B | The term A was introduced by person/work B. |
| `prerequisite-of::` | A → B | Understanding A is required before B. |

### Sourcing / attribution

| Relation | Direction | Meaning |
|---|---|---|
| `cites::` | A → B | Note A cites paper/work B. |
| `cited-in::` | A → B | A is cited in B. (Inverse of `cites::`; usually generated.) |
| `authored-by::` | A → B | A was authored by person B (used in `paper` and `synthesis` notes). |
| `affiliated-with::` | A → B | Person A is/was affiliated with org B. |

### Application / domain

| Relation | Direction | Meaning |
|---|---|---|
| `applies-to::` | A → B | Concept A is relevant to domain/case B. |
| `tested-on::` | A → B | Method A was evaluated on dataset/benchmark B. |
| `governs::` | A → B | Policy A regulates domain/activity B. |
| `jurisdiction-of::` | A → B | Case A was decided under jurisdiction B. |

### Debate / position

| Relation | Direction | Meaning |
|---|---|---|
| `position-in::` | A → B | Note A is one position within debate B. |
| `proponent-of::` | A → B | Person/org A advocates position B. |
| `opponent-of::` | A → B | Person/org A opposes position B. |

### Soft / generic

| Relation | Direction | Meaning |
|---|---|---|
| `related::` | A → B | Generic catch-all. **Use sparingly** — prefer a specific type above. Triggers a review flag if used more than 3 times in a single note. |
| `see-also::` | A → B | Pure cross-reference, no semantic claim. |

## Syntax in practice

Within a note's body:

```markdown
## Relationships

supports:: [[Mesa-Optimization]]
contradicts:: [[Goal-Directedness is Anthropomorphic]]
defined-by:: [[Hubinger 2019 — Risks from Learned Optimization]]
coined-by:: [[Evan Hubinger]]
applies-to:: [[Deceptive Alignment]]
```

Inline within prose is also valid:

```markdown
This formulation responds-to:: [[Russell 2019 — Human Compatible]] and extends:: [[Bostrom 2014 — Superintelligence]].
```

## Why typed relationships matter

A retrieval agent asked "what are arguments against X?" can query `contradicts:: X` and get a precise list, instead of walking every wikilink and reading bodies to figure out which links are oppositional. This compounds: across 10,000 notes, typed relationships make the difference between a usable knowledge graph and an opaque pile.

## Inverse relationships

Most relationships have natural inverses (e.g., `cites::` ↔ `cited-in::`). We do **not** require authors to write both directions — Dataview can generate inverse views from forward links. Author only the natural-feeling direction.

## Adding a new relationship type

Same process as adding a vocabulary term: propose in a commit titled `schema: add relationship <name>`, document rationale in `_Meta/Session Log.md`, update this file.
