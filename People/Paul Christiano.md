---
id: paul-christiano
title: Paul Christiano
type: person
status: draft
created: 2026-05-20
last_reviewed: 2026-05-20
authored_by: claude-opus-4-7
schema_version: 0.1
summary: AI safety researcher; inventor of RLHF and Iterated Distillation and Amplification (IDA); founder of the Alignment Research Center (ARC, which spun out METR); founding head of the US AISI safety team.
confidence: 0.9
source_tier: 2
topics: [ai-safety/alignment, ai-safety, ai-safety/evaluation]
aliases: [Paul F. Christiano]
birth_year: null
death_year: null
nationality: [American]
affiliations: [[US AISI]], [[Alignment Research Center]], [[OpenAI]] (former)
roles: [researcher, founder]
expertise_areas: [ai-safety/alignment, ai-safety/alignment/scalable-oversight, ai-safety/evaluation]
sources:
  - type: peer-reviewed-paper
    title: "Deep Reinforcement Learning from Human Preferences"
    authors: [Christiano P., Leike J., Brown T., Martic M., Legg S., Amodei D.]
    venue: NeurIPS
    year: 2017
    arxiv_id: 1706.03741
    accessed: 2026-05-20
  - type: preprint
    title: "Supervising strong learners by amplifying weak experts"
    authors: [Christiano P., Shlegeris B., Amodei D.]
    venue: arXiv
    year: 2018
    arxiv_id: 1810.08575
    accessed: 2026-05-20
  - type: expert-blog
    title: "What does it take to catch a Chinchilla? Verifying compute"
    authors: [Christiano P., et al.]
    venue: ARC
    year: 2023
    accessed: 2026-05-20
related: [[RLHF]], [[Scalable Oversight]], [[Anthropic]]
---

# Paul Christiano

> AI safety researcher whose technical contributions — RLHF (2017), Iterated Distillation and Amplification (IDA, 2018), and the founding of evaluation organizations ARC and METR — shape much of contemporary alignment practice and frontier-model evaluation infrastructure.

## Background

PhD in theoretical computer science from UC Berkeley (2017). Researcher at OpenAI 2017–2021, leading the alignment team. Departed in 2021 to found the Alignment Research Center (ARC), focused on theoretical alignment and evaluation work. In 2024 became the founding head of the AI safety team at the US AI Safety Institute within NIST.

affiliated-with:: [[US AISI]]
affiliated-with:: [[Alignment Research Center]]
affiliated-with:: [[OpenAI]] (former)

## Contributions

### RLHF (2017)
First author of "Deep Reinforcement Learning from Human Preferences" — the paper introducing the technique that, scaled and adapted, produced InstructGPT, ChatGPT, and the broader paradigm of preference-tuned LLMs.

authored-by:: [[christiano-deep-rl-from-human-preferences-2017]]
coined-by:: [[RLHF]]

### Iterated Distillation and Amplification (IDA, 2018)
Co-authored "Supervising strong learners by amplifying weak experts" — the foundational paper for IDA, a major scalable-oversight proposal. Subsequent informal essays on factored cognition extended the framework.

defined-by:: [[Scalable Oversight]]
coined-by:: [[Iterated Distillation and Amplification]]

### AI Safety via Debate (2018)
Co-author with Geoffrey Irving and Dario Amodei.

### Alignment Research Center (ARC) — founding (2021)
Founded ARC after leaving OpenAI to focus on theoretical alignment problems (Eliciting Latent Knowledge, heuristic arguments) and evaluation work. ARC Evals spun out as METR in 2024.

### US AISI safety team — founding head (2024)
Among the most-credentialed AI safety researchers to take a US government role. The US AISI's evaluation methodology development benefits from Christiano's prior experience at ARC Evals / METR.

## Positions

`perspective: cautious`

Christiano's stated p(doom)-style probabilities have been in the 10–50% range across public statements, with significant emphasis on epistemic humility about such numbers. He is well-known for steelmanning multiple positions and for sharply distinguishing technical from strategic claims.

Notable writings:
- "What failure looks like" (LessWrong, 2019) — articulating two failure scenarios (Part I: subtle misalignment; Part II: outright takeover).
- ELK (Eliciting Latent Knowledge) reports — ARC's research agenda on alignment for capable systems.

proponent-of:: [[Scalable Oversight]]
proponent-of:: [[Frontier Model Evaluation]]

## Reception

Among the most-respected technical voices in AI safety. Reception:

- *Within safety community*: foundational figure. Both LessWrong-adjacent rationalist communities and academic ML safety circles cite Christiano heavily.
- *Within mainstream ML*: respected as a technical contributor; RLHF citation alone is enormous.
- *Public role at US AISI*: significant signalling for the US government's seriousness about AI safety expertise.

## Sources

- ai-alignment.com — Christiano's blog
- ARC publications (alignment.org)
- "Deep RL from Human Preferences" (2017)
- IDA and Debate papers (2018)
- US AISI public materials
