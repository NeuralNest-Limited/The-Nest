---
id: moc-recent-activity
title: MOC — Recent Activity
type: moc
status: reviewed
created: 2026-05-19
last_reviewed: 2026-05-19
authored_by: claude-opus-4-7
schema_version: 0.1
summary: Recently created or reviewed notes — for resuming work.
confidence: 0.95
source_tier: 5
topics: [meta/curation]
query_seed: dataview
covers_topics: []
sources: []
related: []
---

# MOC — Recent Activity

## Notes reviewed in the last 14 days

```dataview
TABLE type, status, last_reviewed, authored_by
FROM ""
WHERE last_reviewed >= date(today) - dur(14 days)
SORT last_reviewed DESC
LIMIT 50
```

## Notes created in the last 14 days

```dataview
TABLE type, status, created, authored_by
FROM ""
WHERE created >= date(today) - dur(14 days)
SORT created DESC
LIMIT 50
```

## Stubs awaiting work

```dataview
TABLE type, topics, created
FROM ""
WHERE status = "stub"
SORT created ASC
LIMIT 30
```

## Notes flagged needs-update

```dataview
TABLE type, last_reviewed, needs_attention
FROM ""
WHERE status = "needs-update"
SORT last_reviewed ASC
```
