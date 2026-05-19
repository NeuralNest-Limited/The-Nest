---
id: moc-organizations
title: MOC — Organizations
type: moc
status: reviewed
created: 2026-05-19
last_reviewed: 2026-05-19
authored_by: claude-opus-4-7
schema_version: 0.1
summary: Index of organization-type notes.
confidence: 0.95
source_tier: 5
topics: [meta/curation]
query_seed: dataview
covers_topics: []
sources: []
related: []
---

# MOC — Organizations

## Featured

- [[Anthropic]]
- [[MIRI]]

## All organizations

```dataview
TABLE org_kind, headquarters, founded
FROM "Organizations"
SORT founded ASC
```

## By kind

```dataview
LIST
FROM "Organizations"
WHERE org_kind = "company"
SORT file.name
```

```dataview
LIST
FROM "Organizations"
WHERE org_kind = "academic" OR org_kind = "ngo"
SORT file.name
```

```dataview
LIST
FROM "Organizations"
WHERE org_kind = "gov" OR org_kind = "igo"
SORT file.name
```
