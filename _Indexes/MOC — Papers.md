---
id: moc-papers
title: MOC — Papers
type: moc
status: reviewed
created: 2026-05-19
last_reviewed: 2026-05-19
authored_by: claude-opus-4-7
schema_version: 0.1
summary: Index of paper/book notes.
confidence: 0.95
source_tier: 5
topics: [meta/curation]
query_seed: dataview
covers_topics: []
sources: []
related: []
---

# MOC — Papers

## Featured

- [[Concrete Problems in AI Safety]]

## All papers by year

```dataview
TABLE authors, venue, year
FROM "Papers"
SORT year DESC
```

## By topic

```dataview
LIST
FROM "Papers"
WHERE econtains(topics, "ai-safety/alignment")
SORT year DESC
```
