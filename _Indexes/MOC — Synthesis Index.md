---
id: moc-synthesis-index
title: MOC — Synthesis Index
type: moc
status: reviewed
created: 2026-05-19
last_reviewed: 2026-05-19
authored_by: claude-opus-4-7
schema_version: 0.1
summary: All organizational synthesis positions, with endorsement provenance.
confidence: 0.95
source_tier: 5
topics: [meta/curation]
query_seed: dataview
covers_topics: []
sources: []
related: []
---

# MOC — Synthesis Index

> ⚠️ All notes listed here express positions taken by the organization (or by contributors writing in its name) — not neutral descriptions. See [[../_Meta/Editorial Standards]] §1.

## All synthesis notes

```dataview
TABLE perspective, endorsement_status, last_reviewed
FROM "_Synthesis"
WHERE type = "synthesis"
SORT last_reviewed DESC
```

## By endorsement status

### Human-endorsed (highest commitment)

```dataview
LIST
FROM "_Synthesis"
WHERE endorsement_status = "human-endorsed"
SORT file.name
```

### AI-endorsed (drafted and accepted by AI authors, awaiting human review)

```dataview
LIST
FROM "_Synthesis"
WHERE endorsement_status = "ai-endorsed"
SORT file.name
```

### Draft (in progress)

```dataview
LIST
FROM "_Synthesis"
WHERE endorsement_status = "draft"
SORT file.name
```

### Retracted (kept for history)

```dataview
LIST
FROM "_Synthesis"
WHERE endorsement_status = "retracted"
SORT file.name
```
