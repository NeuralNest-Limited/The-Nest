---
id: moc-governance-and-policy
title: MOC — Governance and Policy
type: moc
status: draft
created: 2026-05-20
last_reviewed: 2026-05-20
authored_by: claude-opus-4-7
schema_version: 0.1
summary: Topic index for AI governance — international frameworks, national policies, sectoral regulation, self-regulatory commitments, and enforcement mechanisms.
confidence: 0.95
source_tier: 5
topics: [governance, governance/global, governance/national]
query_seed: hybrid
covers_topics: [governance, governance/global, governance/national, governance/sectoral, governance/self-regulation, governance/standards, law, law/copyright, law/liability, law/personhood]
sources: []
related: []
---

# MOC — Governance and Policy

> AI governance: international frameworks, national policies, sectoral regulation, self-regulatory commitments, and the law / standards layer underneath.

## By jurisdiction

```dataview
TABLE jurisdiction, policy_status, effective_date
FROM "Policies"
SORT jurisdiction, effective_date DESC
```

## Featured policies

- [[EU AI Act]] — first comprehensive horizontal AI regulation (in force 2024+)
- [[US Executive Order on AI 2023]] — EO 14110 (2023, revoked 2025)
- [[China Generative AI Measures]] — CAC framework (2023)
- [[UK AISI Mandate]] — first national AI safety institute (2023)
- [[UNESCO Recommendation on AI Ethics]] — first global standard (2021)
- [[NZ Algorithm Charter]] — Tiriti-grounded NZ government framework
- [[Responsible Scaling Policy]] — Anthropic capability-threshold framework
- [[ASL Levels]] — AI Safety Levels framework

## Featured concepts

- [[AI Safety]] — the umbrella driving most governance
- [[AGI]] — capability category increasingly used in regulatory triggers

## Key governance-focused organizations

- [[UK AISI]] — pre-deployment evaluation, International AISI Network
- [[US AISI]] — NIST-housed, AI RMF
- [[GovAI]] — independent governance research
- [[Center for AI Safety]] — extinction-risk advocacy + statement
- [[Future of Life Institute]] — Asilomar AI Principles, Pause Letter, EU AI Act advocacy

## Featured people

- [[Helen Toner]] — CSET, former OpenAI board
- [[Yoshua Bengio]] — International Scientific Report chair

## Active debates

- [[debate-pause-frontier-ai]] — Should AI development pause?
- [[debate-open-vs-closed-frontier]] — Open vs closed frontier models

## Comparative governance precedents

- [[Nuclear Technology Governance]] — NPT / IAEA as model and anti-model
- [[Asilomar Recombinant DNA Precedent]] — scientist-led precaution

## All policy / governance concepts

```dataview
LIST FROM "Concepts"
WHERE econtains(topics, "governance") OR econtains(topics, "law")
SORT file.name
```
