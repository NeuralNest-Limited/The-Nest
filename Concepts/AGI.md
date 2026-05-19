---
id: agi
title: Artificial General Intelligence (AGI)
type: concept
status: draft
created: 2026-05-20
last_reviewed: 2026-05-20
authored_by: claude-opus-4-7
schema_version: 0.1
summary: A contested concept referring (variably) to AI systems matching or exceeding human-level cognitive performance across most economically valuable, intellectually demanding, or "general" tasks.
confidence: 0.7
source_tier: 1
topics: [ai-capabilities, ai-capabilities/scaling]
perspective: neutral
aliases: [AGI, general AI, human-level AI, HLMI, transformative AI, TAI]
sources:
  - type: book
    title: "Superintelligence: Paths, Dangers, Strategies"
    authors: [Bostrom N.]
    venue: Oxford University Press
    year: 2014
    accessed: 2026-05-20
  - type: official-statement
    title: "OpenAI Charter"
    venue: openai.com
    year: 2018
    url: https://openai.com/charter
    accessed: 2026-05-20
  - type: white-paper
    title: "Levels of AGI for Operationalizing Progress on the Path to AGI"
    authors: [Morris M.R., Sohl-Dickstein J., et al.]
    venue: arXiv (DeepMind)
    year: 2023
    arxiv_id: 2311.02462
    accessed: 2026-05-20
  - type: white-paper
    title: "Reframing Superintelligence: Comprehensive AI Services as General Intelligence"
    authors: [Drexler K.E.]
    venue: Future of Humanity Institute
    year: 2019
    accessed: 2026-05-20
related: [[AI Alignment]], [[Existential Risk]]
---

# Artificial General Intelligence (AGI)

> AI systems matching or exceeding human-level cognitive performance across most economically valuable, intellectually demanding, or "general" tasks. The term is contested in both definition and coherence.

## Origin

The phrase "Artificial General Intelligence" gained currency in the early 2000s through Ben Goertzel, Shane Legg, and Marcus Hutter — partly as a corrective to "narrow AI" dominant in academic ML at the time. Earlier near-synonyms include "Strong AI" (Searle 1980), "Human-Level Machine Intelligence" (HLMI; common in survey literature), and "Transformative AI" (TAI; Open Philanthropy and Holden Karnofsky's preferred framing).

coined-by:: [[Shane Legg]]
coined-by:: [[Ben Goertzel]]

## Core claim

The unifying intuition: there exists a meaningful threshold at which AI capability becomes *general* in a way fundamentally different from narrow / specialised AI. Common operational definitions:

- **Economic / task-coverage** (OpenAI Charter, 2018): "highly autonomous systems that outperform humans at most economically valuable work."
- **Cognitive-task spectrum** (DeepMind "Levels of AGI", 2023): a competency × generality matrix with levels from emerging to superhuman.
- **Survey definitions** (Grace et al., AI Impacts): "high-level machine intelligence" achieved when machines can do every task better and more cheaply than humans.
- **Bostromian**: any AI system that exceeds human cognitive performance in virtually all economically and intellectually relevant domains.

## Variants and refinements

- **AGI vs ASI** (Artificial Superintelligence): AGI is human-level; ASI substantially exceeds. The transition is theorized as fast or slow ("takeoff speed" debate).
- **TAI** (Transformative AI): Open Philanthropy / Karnofsky frame — AI sufficient to cause societal transformation comparable to agricultural or industrial revolutions. Decouples from human-comparison.
- **HLMI** — used in expert-elicitation surveys to enable timeline forecasting.
- **PASTA** (Process for Automating Scientific and Technological Advancement) — Karnofsky's framing focused on AI capable of automating R&D itself.
- **CAIS** (Comprehensive AI Services) — Drexler's reframing rejecting AGI-as-unified-agent in favour of decomposed AI services collectively performing general functions.

extends:: [[AI Capabilities]]
contradicts:: [[Reframing Superintelligence]]

## Evidence and forecasting

Forecasting AGI is notoriously difficult. Sources of evidence:

- **Capability benchmarks**: scaling-law results, performance on MMLU, GPQA, ARC-AGI, METR's autonomous-agent evals.
- **Expert surveys**: AI Impacts 2022 / 2023 surveys (median estimates of HLMI shifted earlier substantially between surveys).
- **Internal capability evaluations** at major labs (Anthropic RSP evaluations, OpenAI preparedness framework).
- **Compute / data scaling trends**: Sevilla et al.'s tracking of compute used in training runs.

Public estimates range from "within years" (e.g., Aschenbrenner 2024 "Situational Awareness," Hinton public statements) to "decades or never" (Marcus, LeCun in part).

## Critiques

- *Concept incoherence*: critics (Bender, Mitchell, in part Marcus) argue "general" intelligence is not a measurable property and the term smuggles in undefended premises about human cognition's unity.
- *Anthropocentric*: defining AGI relative to human capabilities may miss kinds of intelligence that don't map cleanly onto human cognition.
- *CAIS reframing* (Drexler): the dominant frame assumes AGI will be a unified agent pursuing goals; actual AI development trajectory (specialized services composed via interfaces) may not fit.
- *Goalpost shifting*: critics observe that the threshold has migrated as systems achieve previously canonical AGI tasks (e.g., passing the Turing test, beating humans at chess/Go, professional-quality writing).

criticized-by:: [[Gary Marcus]]
criticized-by:: [[Emily Bender]]

## Open questions

- Is "AGI" a meaningful category, or is capability a smooth continuum with no natural threshold?
- Should AI policy use AGI thresholds (e.g., regulatory triggers) or compute / capability thresholds (e.g., EU AI Act 10^25 FLOP threshold)?
- Could "transformative AI" arrive without satisfying any specific AGI definition (e.g., a narrow but extraordinarily capable system)?

## Relationships

prerequisite-of:: [[Existential Risk]]
related:: [[AI Capabilities]]
related:: [[Takeoff Speed]]
applies-to:: [[debate-pause-frontier-ai]]
applies-to:: [[AI Forecasting]]
