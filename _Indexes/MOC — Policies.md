---
id: moc-policies
title: MOC — Policies
type: moc
status: reviewed
created: 2026-05-19
last_reviewed: 2026-05-19
authored_by: claude-opus-4-7
schema_version: 0.1
summary: Index of policy / regulation / charter notes.
confidence: 0.95
source_tier: 5
topics: [meta/curation]
query_seed: dataview
covers_topics: []
sources: []
related: []
---

# MOC — Policies

## Featured

- [[EU AI Act]]
- [[NZ Algorithm Charter]]

## All policies

```dataview
TABLE jurisdiction, policy_status, effective_date
FROM "Policies"
SORT effective_date DESC
```

## By jurisdiction

```dataview
LIST
FROM "Policies"
WHERE jurisdiction = "EU"
SORT file.name
```

```dataview
LIST
FROM "Policies"
WHERE jurisdiction = "NZ"
SORT file.name
```

```dataview
LIST
FROM "Policies"
WHERE jurisdiction = "US"
SORT file.name
```

```dataview
LIST
FROM "Policies"
WHERE jurisdiction = "China" OR jurisdiction = "CN"
SORT file.name
```

## By status

```dataview
LIST
FROM "Policies"
WHERE policy_status = "enacted"
SORT effective_date DESC
```

```dataview
LIST
FROM "Policies"
WHERE policy_status = "proposed"
SORT file.name
```
