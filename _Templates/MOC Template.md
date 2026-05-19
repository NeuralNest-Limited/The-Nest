---
id: moc-<topic-slug>
title: MOC — <Topic>
type: moc
status: draft
created: <YYYY-MM-DD>
last_reviewed: <YYYY-MM-DD>
authored_by: <model-id>
schema_version: 0.1
summary: <One-line — what this index covers.>
confidence: 0.9
source_tier: 5
topics: []
query_seed: dataview
covers_topics: []
sources: []
related: []
---

# MOC — <Topic>

> Curated index of notes related to <topic>. Manual highlights at top; Dataview-generated long tail below.

## Featured notes

(Hand-curated by an agent — the entry points an outsider should see first.)

- [[<Note 1>]] — <one-line>
- [[<Note 2>]] — <one-line>

## Key debates

```dataview
LIST FROM "Debates"
WHERE contains(topics, "<topic>")
SORT file.name
```

## Key people

```dataview
LIST FROM "People"
WHERE contains(expertise_areas, "<topic>")
SORT file.name
```

## Key organizations

```dataview
LIST FROM "Organizations"
WHERE contains(focus_areas, "<topic>")
SORT file.name
```

## All concept notes on this topic

```dataview
LIST FROM "Concepts"
WHERE contains(topics, "<topic>")
SORT file.name
```

## Recent activity

```dataview
TABLE last_reviewed, status
FROM ""
WHERE contains(topics, "<topic>") AND last_reviewed >= date(today) - dur(30 days)
SORT last_reviewed DESC
LIMIT 20
```
