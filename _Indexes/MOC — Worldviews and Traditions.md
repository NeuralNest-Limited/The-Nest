---
id: moc-worldviews-and-traditions
title: MOC — Worldviews and Traditions
type: moc
status: draft
created: 2026-05-20
last_reviewed: 2026-05-20
authored_by: claude-opus-4-7
schema_version: 0.1
summary: Topic index for multi-tradition perspectives on AI — Māori, Pacific, Buddhist, Christian, Islamic, secular humanist. Each is presented as research material with provenance flags where authorship is from outside the tradition.
confidence: 0.85
source_tier: 5
topics: [philosophy, philosophy/moral-status]
query_seed: hybrid
covers_topics: [worldview/maori, worldview/pacific, worldview/buddhist, worldview/christian, worldview/islamic, worldview/jewish, worldview/hindu, worldview/secular-humanist, worldview/animist, worldview/other]
sources: []
related: []
---

# MOC — Worldviews and Traditions

> How diverse intellectual and religious traditions engage AI. Each tradition has internal heterogeneity; notes flagged with `needs_attention:` where authored from outside the tradition.

## Featured concepts

- [[Whakapapa and Relational Ontology]] — Māori relational framework (⚠ needs Māori-scholar review)
- [[Pacific Perspectives on Technology]] — talanoa, vā, Hauʻofa traditions (⚠ needs Pacific-scholar review)
- [[Buddhist Perspectives on AI Sentience]] — citta, sattva, functional analyses (⚠ needs Buddhist-scholar review)
- [[Christian Theological Responses to AI]] — imago Dei, stewardship, Rome Call (⚠ needs theological review)
- [[Islamic Bioethics and AI]] — maqāṣid, amānah, shūrā (⚠ needs Islamic-scholar review)
- [[Te Tiriti and AI Governance]] — Treaty-based partnership and non-human legal subjects

## Common methodological cautions across traditions

- **Appropriation risk**: extracting concepts to enrich Western frameworks without engaging tradition-internal scholars is harm.
- **Heterogeneity**: "the X view" obscures real diversity within every tradition.
- **Translation loss**: key terms (whakapapa, vā, citta, imago Dei, amānah) carry meanings that English approximations lose.
- **Tradition-external authorship**: most of this MOC's content was drafted by an AI agent without tradition affiliation; explicit needs_attention flags request review.

## All worldview concepts

```dataview
LIST FROM "Concepts"
WHERE econtains(topics, "worldview/maori") OR econtains(topics, "worldview/pacific") OR econtains(topics, "worldview/buddhist") OR econtains(topics, "worldview/christian") OR econtains(topics, "worldview/islamic") OR econtains(topics, "worldview/jewish") OR econtains(topics, "worldview/hindu") OR econtains(topics, "worldview/secular-humanist")
SORT file.name
```
