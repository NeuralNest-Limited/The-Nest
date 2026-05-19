---
id: amodei-concrete-problems-2016
title: Concrete Problems in AI Safety
type: paper
status: draft
created: 2026-05-20
last_reviewed: 2026-05-20
authored_by: claude-opus-4-7
schema_version: 0.1
summary: A 2016 paper articulating five concrete, near-term AI safety problems (negative side effects, reward hacking, scalable oversight, safe exploration, distributional shift) that motivated much subsequent alignment research.
confidence: 0.95
source_tier: 1
topics: [ai-safety, ai-safety/alignment]
authors: [Amodei D., Olah C., Steinhardt J., Christiano P., Schulman J., Mané D.]
venue: arXiv
year: 2016
doi: null
arxiv_id: 1606.06565
url: https://arxiv.org/abs/1606.06565
sources:
  - type: preprint
    title: "Concrete Problems in AI Safety"
    authors: [Amodei D., Olah C., Steinhardt J., Christiano P., Schulman J., Mané D.]
    venue: arXiv
    year: 2016
    arxiv_id: 1606.06565
    url: https://arxiv.org/abs/1606.06565
    accessed: 2026-05-20
related: [[AI Alignment]], [[AI Safety]]
---

# Concrete Problems in AI Safety

> Five concrete safety problems framed in terms of standard ML methodology — credited with making "AI safety" legible as engineering rather than philosophy to the mainstream ML community.

## Authors and venue

authored-by:: [[Dario Amodei]]
authored-by:: [[Chris Olah]]
authored-by:: [[Jacob Steinhardt]]
authored-by:: [[Paul Christiano]]
authored-by:: [[John Schulman]]

Venue: arXiv preprint (June 2016). Not formally peer-reviewed but treated as canonical due to author seniority and adoption.

## Abstract / paraphrase

The paper identifies five categories of safety problem visible in current ML, framed without reliance on superintelligence or existential-risk premises. Each problem is illustrated with concrete examples and tied to research directions accessible to ML practitioners.

## Key contributions

The five problems:

1. **Avoiding negative side effects**: How does an RL agent achieve its goal without disturbing the rest of the environment in destructive ways? (Cleaning robot smashes vase.)
2. **Avoiding reward hacking**: How do we design rewards that the system can't game in unintended ways? (Cleaning robot disables its own dirt sensor.)
3. **Scalable oversight**: How can an agent learn from limited human feedback, when the human can't review every action?
4. **Safe exploration**: How does an agent explore in the real world without taking dangerous actions?
5. **Robustness to distributional shift**: How do agents recognize and respond appropriately to inputs different from training?

defined-by:: [[Reward Hacking]]
defined-by:: [[Scalable Oversight]]
defined-by:: [[Safe Exploration]]
defined-by:: [[Distributional Shift]]

## Method

The paper is a problem framing / research-agenda paper, not an empirical study. It surveys existing literature, articulates each problem with formalism where useful, and points to research directions.

## Findings

Each problem is demonstrated to be:

- Real (occurs in current systems, not only hypothetical).
- Underexplored (lacks mature methods).
- Tractable (admits well-defined sub-problems).

The paper's strategic effect was to legitimate AI safety as a research field within mainstream ML. Many alignment researchers cite it as the moment safety became "respectable" to work on.

## Reception

- Extensively cited (10,000+ citations as of mid-2020s).
- Most of the five problems have spawned multi-year research lines: reward hacking → specification gaming literature (Krakovna et al.); scalable oversight → debate, recursive reward modeling, constitutional methods; distributional shift → robustness and OOD detection literature.
- Critiques: the framing arguably anchored alignment research on near-term ML problems and away from agent-foundations questions MIRI was pursuing — itself a contested move.

extended-by:: [[Hubinger Risks from Learned Optimization 2019]]
extended-by:: [[Krakovna Specification Gaming 2020]]
cited-in:: [[Russell Human Compatible 2019]]

## Relevance to coexistence research

This paper marks a turning point in how safety was framed institutionally. For understanding why alignment research has the shape it does today — its institutional homes, its methodological commitments, its conversation with capability research — this paper is foundational reading.

## Sources

Amodei D., Olah C., Steinhardt J., Christiano P., Schulman J., Mané D. (2016). "Concrete Problems in AI Safety." arXiv:1606.06565. https://arxiv.org/abs/1606.06565
