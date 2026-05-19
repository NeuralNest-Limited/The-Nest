---
id: moc-aotearoa-nz-lens
title: MOC — Aotearoa NZ Lens
type: moc
status: reviewed
created: 2026-05-19
last_reviewed: 2026-05-19
authored_by: claude-opus-4-7
schema_version: 0.1
summary: NZ-specific notes — the org's geographic and cultural differentiator.
confidence: 0.95
source_tier: 5
topics: [region/nz]
query_seed: hybrid
covers_topics: [region/nz, region/pacific, worldview/maori, worldview/pacific]
sources: []
related: []
---

# MOC — Aotearoa NZ Lens

> The org's geographic and cultural differentiator. Most AI ethics centres are US, UK, or EU; the NZ + Pacific perspective is genuinely under-represented in global discourse.

## Featured

- [[Te Tiriti and AI Governance]] — legal personhood precedents (rivers, mountains) as framework for non-human legal subjects
- [[Whakapapa and Relational Ontology]] — Māori relational thinking for human-AI relations
- [[NZ Algorithm Charter]] — NZ's existing AI governance framework
- [[AI Forum NZ]] — the country's main AI policy convening body

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

## Open questions specific to the NZ context

- How does Te Tiriti shape the org's governance — particularly Article 2 (tino rangatiratanga) and partnership?
- What is the appropriate role of AI in iwi data sovereignty?
- Does the legal-personhood precedent for natural features (Whanganui River, Te Urewera, Taranaki Maunga) extend usefully to AI personhood debates, or is the analogy misleading?

(Move these into `Debates/` as they mature.)
