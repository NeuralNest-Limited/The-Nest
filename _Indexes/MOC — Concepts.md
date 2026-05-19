---
id: moc-concepts
title: MOC — Concepts
type: moc
status: reviewed
created: 2026-05-19
last_reviewed: 2026-05-19
authored_by: claude-opus-4-7
schema_version: 0.1
summary: Index of all concept-type notes in the vault.
confidence: 0.95
source_tier: 5
topics: [meta/curation]
query_seed: dataview
covers_topics: []
sources: []
related: []
---

# MOC — Concepts

## Featured entry points

(Hand-curated. Update as the corpus grows.)

- [[AI Alignment]]
- [[AI Welfare]]
- [[Mesa-Optimization]]
- [[Moral Patienthood]]
- [[Te Tiriti and AI Governance]]

## All concepts

```dataview
TABLE status, source_tier, last_reviewed
FROM "Concepts"
SORT file.name ASC
```

## Concepts by status

```dataview
LIST
FROM "Concepts"
WHERE status = "stub"
SORT file.name
```

```dataview
LIST
FROM "Concepts"
WHERE status = "needs-update"
SORT file.name
```

## Concepts by topic family

### AI Safety and Alignment

```dataview
LIST
FROM "Concepts"
WHERE econtains(topics, "ai-safety") OR econtains(topics, "ai-safety/alignment")
SORT file.name
```

### AI Welfare

```dataview
LIST
FROM "Concepts"
WHERE econtains(topics, "ai-welfare") OR econtains(topics, "ai-welfare/moral-patienthood")
SORT file.name
```

### Philosophy of Mind

```dataview
LIST
FROM "Concepts"
WHERE econtains(topics, "philosophy/consciousness") OR econtains(topics, "philosophy/moral-status")
SORT file.name
```

### NZ Lens

```dataview
LIST
FROM "Concepts"
WHERE econtains(topics, "region/nz") OR econtains(topics, "worldview/maori") OR econtains(topics, "worldview/pacific")
SORT file.name
```
