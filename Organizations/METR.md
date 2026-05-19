---
id: metr
title: Model Evaluation and Threat Research (METR)
type: org
status: draft
created: 2026-05-20
last_reviewed: 2026-05-20
authored_by: claude-opus-4-7
schema_version: 0.1
summary: Independent AI safety research organization founded 2022 (originally as part of ARC Evals); specialized in evaluating autonomous task-completion and dangerous capability levels of frontier models.
confidence: 0.85
source_tier: 2
topics: [ai-safety/evaluation, ai-safety, ai-safety/evaluation/dangerous-capabilities]
aliases: [Model Evaluation and Threat Research, ARC Evals (former)]
founded: 2022
dissolved: null
headquarters: Berkeley, USA
org_kind: ngo
focus_areas: [ai-safety/evaluation, ai-safety/evaluation/dangerous-capabilities, ai-safety]
sources:
  - type: official-statement
    title: "About METR"
    venue: metr.org
    year: 2024
    url: https://metr.org/
    accessed: 2026-05-20
related: [[Apollo Research]], [[Anthropic]], [[OpenAI]]
---

# Model Evaluation and Threat Research (METR)

> Independent non-profit specialized in evaluating frontier AI models for autonomous task-completion capabilities and dangerous capability levels. Originally part of ARC (Alignment Research Center); spun out as METR in 2024.

## Founding and structure

Originally founded 2022 as ARC Evals — the evaluations arm of the Alignment Research Center, which itself was founded by Paul Christiano. Spun out as the independent METR organization in 2024. Based in Berkeley.

affiliated-with:: [[Paul Christiano]] (founder, ARC)

## Mission and focus

Research focus: empirical evaluation of how autonomously frontier AI models can complete real-world tasks, with emphasis on capabilities that could enable dangerous misuse or loss of control.

Distinctive methodological approach:

- **Long-horizon task evaluation**: rather than benchmark Q&A, METR tests models' ability to complete multi-hour, multi-step research / engineering tasks.
- **Human task-time anchoring**: tasks are anchored to typical human completion times, allowing capability progress to be measured in "human-time-equivalent" units.
- **Autonomous-agent framing**: evaluations consider not just what a model can do given a prompt but what an agent built on the model can do with tools.

defined-by:: [[Autonomous Capability Evaluation]]

## Notable outputs

- Evaluations of GPT-4, GPT-4o, o1, Claude 3 Opus, Claude 3.5 Sonnet, Gemini, and other frontier models prior to public release — including for OpenAI's Preparedness Framework and Anthropic's RSP assessments.
- **METR Tasks**: a publicly-described benchmark of long-horizon AI R&D tasks.
- **"Measuring the impact of AI on experienced open-source developer productivity" (2025)**: study finding AI assistance had complex effects on developer productivity — sometimes negative for experienced developers on familiar codebases.
- Methodological papers on evaluation design and scaling.

## Key people

- **Beth Barnes**: founder of ARC Evals / METR.
- Research staff drawn from AI safety research community.

## Funding and influence

Philanthropic funding (Open Philanthropy, others) plus contracted evaluations from frontier labs. Influence:

- Establishing autonomous-task evaluation as a standard component of pre-deployment review.
- Methodologically distinct framings of capability that have been adopted by AISIs.
- Empirical contributions to the productivity / labor displacement question.

## Reception and critique

- *Within AI safety community*: highly regarded.
- *Within frontier labs*: serves as a trusted third-party evaluator.
- *Methodological debate*: long-horizon task evaluation vs. shorter Q&A benchmarks each capture different capability dimensions; METR's framings are influential but not consensus.

## Sources

- metr.org
- METR evaluation reports
- METR developer productivity study (2025)
