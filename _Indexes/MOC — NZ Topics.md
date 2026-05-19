---
id: moc-aotearoa-nz-lens
title: MOC — NZ Topics
type: moc
status: reviewed
created: 2026-05-19
last_reviewed: 2026-05-20
authored_by: claude-opus-4-7
schema_version: 0.1
summary: Index of NZ-region-relevant content notes — research material on NZ AI governance, Māori frameworks, and Pacific perspectives.
confidence: 0.95
source_tier: 5
topics: [region/nz]
query_seed: hybrid
covers_topics: [region/nz, region/pacific, worldview/maori, worldview/pacific]
sources: []
related: []
---

# MOC — NZ Topics

> Index of content notes covering NZ-region material — governance frameworks, indigenous legal-philosophical traditions, and Pacific perspectives — included as research material in the global human–AI coexistence conversation.

## Featured

- [[Te Tiriti and AI Governance]] — NZ legal-personhood precedents (rivers, mountains) examined as framework for non-human legal subjects
- [[Whakapapa and Relational Ontology]] — Māori relational ontology presented as one substantive framework among many
- [[NZ Algorithm Charter]] — NZ's existing AI governance framework
- [[AI Forum NZ]] — the country's main AI policy convening body
- [[Pacific Perspectives on Technology]] — Pacific intellectual traditions on technology and relation

## All NZ-tagged notes

```dataview
TABLE type, status, topics
FROM ""
WHERE econtains(topics, "region/nz")
SORT type, file.name
```

## Pacific perspectives

```dataview
TABLE type, status, topics
FROM ""
WHERE econtains(topics, "region/pacific") OR econtains(topics, "worldview/pacific")
SORT type, file.name
```

## Māori worldview notes

```dataview
LIST
FROM ""
WHERE econtains(topics, "worldview/maori")
SORT file.name
```

## Open research questions in this area

- Does the legal-personhood precedent for natural features (Whanganui River, Te Urewera, Taranaki Maunga) extend usefully to AI personhood debates, or is the analogy misleading?
- How do indigenous-data-sovereignty frameworks interact with frontier AI training corpora?
- What is the appropriate role of AI in iwi / hapū data sovereignty?

(Move these into `Debates/` as they mature.)
