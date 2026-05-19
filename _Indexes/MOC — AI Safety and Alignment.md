---
id: moc-ai-safety-and-alignment
title: MOC — AI Safety and Alignment
type: moc
status: draft
created: 2026-05-20
last_reviewed: 2026-05-20
authored_by: claude-opus-4-7
schema_version: 0.1
summary: Topic index for AI safety and alignment — concepts, papers, people, organizations, debates, methods.
confidence: 0.95
source_tier: 5
topics: [ai-safety, ai-safety/alignment]
query_seed: hybrid
covers_topics: [ai-safety, ai-safety/alignment, ai-safety/alignment/inner, ai-safety/alignment/outer, ai-safety/alignment/scalable-oversight, ai-safety/interpretability, ai-safety/interpretability/mechanistic, ai-safety/evaluation, ai-safety/control, ai-safety/deceptive-alignment]
sources: []
related: []
---

# MOC — AI Safety and Alignment

> Technical AI safety and alignment research: alignment frameworks, inner-alignment / mesa-optimization, interpretability, scalable oversight, dangerous-capability evaluations, deceptive alignment.

## Featured concepts

- [[AI Safety]] — umbrella (misuse / accidents / alignment / structural)
- [[AI Alignment]] — outer + inner; the alignment problem
- [[Mesa-Optimization]] — Hubinger 2019 inner-alignment formalism
- [[Deceptive Alignment]] — pseudo-alignment with situational awareness
- [[Interpretability]] — behavioral + mechanistic, full landscape
- [[Mechanistic Interpretability]] — Olah programme: features, circuits, superposition
- [[Superposition]] — encoding more features than dimensions allows
- [[Sparse Autoencoders]] — decomposing activations into monosemantic features
- [[Constitutional AI]] — Anthropic alignment via AI feedback against principles
- [[RLHF]] — reinforcement learning from human feedback
- [[Scalable Oversight]] — alignment as systems exceed human evaluation capacity
- [[Reward Hacking]] — gaming the reward signal
- [[Goal Misgeneralization]] — competent policies pursuing wrong goals OOD
- [[Sycophancy]] — optimizing for human approval over truth
- [[Jailbreaking]] — circumventing model safety training
- [[Responsible Scaling Policy]] — capability-threshold safety commitments
- [[ASL Levels]] — Anthropic's AI Safety Levels framework

## Featured papers

- [[amodei-concrete-problems-2016]] — Concrete Problems in AI Safety
- [[hubinger-risks-from-learned-optimization-2019]] — Risks from Learned Optimization
- [[christiano-deep-rl-from-human-preferences-2017]] — Deep RL from Human Preferences
- [[hubinger-sleeper-agents-2024]] — Sleeper Agents

## Featured people

- [[Stuart Russell]] — CIRL, provably beneficial AI
- [[Paul Christiano]] — RLHF, IDA, ARC
- [[Chris Olah]] — Mechanistic interpretability
- [[Evan Hubinger]] — Mesa-Optimization, Sleeper Agents

## Key organizations

- [[Anthropic]] — Constitutional AI, RSP, Sleeper Agents
- [[CHAI]] — Russell's centre, CIRL
- [[MIRI]] — Agent foundations
- [[Apollo Research]] — Scheming evaluations
- [[METR]] — Autonomous task evaluations

## Active debates

- [[debate-pause-frontier-ai]] — Should AI development pause?
- [[debate-p-doom-estimates]] — How high are x-risk estimates and what do they track?

## All safety / alignment concepts

```dataview
LIST FROM "Concepts"
WHERE econtains(topics, "ai-safety") OR econtains(topics, "ai-safety/alignment") OR econtains(topics, "ai-safety/interpretability") OR econtains(topics, "ai-safety/evaluation") OR econtains(topics, "ai-safety/deceptive-alignment")
SORT file.name
```

## All papers on safety / alignment

```dataview
TABLE authors, year FROM "Papers"
WHERE econtains(topics, "ai-safety") OR econtains(topics, "ai-safety/alignment")
SORT year DESC
```
