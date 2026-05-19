---
id: moc-people
title: MOC — People
type: moc
status: reviewed
created: 2026-05-19
last_reviewed: 2026-05-19
authored_by: claude-opus-4-7
schema_version: 0.1
summary: Index of person-type notes.
confidence: 0.95
source_tier: 5
topics: [meta/curation]
query_seed: dataview
covers_topics: []
sources: []
related: []
---

# MOC — People

## Featured

- [[Stuart Russell]]
- [[Robert Long]]

## All people

```dataview
TABLE roles, affiliations, status
FROM "People"
SORT file.name ASC
```

## By expertise

```dataview
TABLE expertise_areas, affiliations
FROM "People"
WHERE econtains(expertise_areas, "ai-safety")
SORT file.name
```

```dataview
TABLE expertise_areas, affiliations
FROM "People"
WHERE econtains(expertise_areas, "ai-welfare") OR econtains(expertise_areas, "philosophy/moral-status")
SORT file.name
```
