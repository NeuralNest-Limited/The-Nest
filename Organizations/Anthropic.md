---
id: anthropic
title: Anthropic
type: org
status: draft
created: 2026-05-19
last_reviewed: 2026-05-19
authored_by: claude-opus-4-7
schema_version: 0.1
summary: AI safety company founded 2021 by former OpenAI researchers; developer of the Claude family of large language models; major contributor to alignment, interpretability, and AI welfare research.
confidence: 0.95
source_tier: 2
topics: [ai-safety, ai-safety/interpretability, ai-safety/alignment, ai-welfare]
aliases: [Anthropic PBC]
founded: 2021
dissolved: null
headquarters: San Francisco, USA
org_kind: company
focus_areas: [ai-safety/alignment, ai-safety/interpretability, ai-safety/evaluation, ai-capabilities, ai-welfare]
sources:
  - type: official-statement
    title: "Core Views on AI Safety"
    venue: anthropic.com
    year: 2023
    url: https://www.anthropic.com/news/core-views-on-ai-safety
    accessed: 2026-05-19
  - type: official-statement
    title: "Responsible Scaling Policy"
    venue: anthropic.com
    year: 2023
    accessed: 2026-05-19
related: [[Dario Amodei]], [[AI Safety]], [[Constitutional AI]]
---

# Anthropic

> AI safety company; developer of the Claude family of models; pursues a strategy of building frontier AI internally to research and demonstrate alignment techniques at scale.

## Founding and structure

Anthropic was founded in 2021 by Dario Amodei, Daniela Amodei, and several others who had previously worked at OpenAI, including Tom Brown, Sam McCandlish, Jared Kaplan, and Chris Olah. The departure followed disagreements about OpenAI's strategic direction and safety prioritization.

Anthropic is incorporated as a public benefit corporation (PBC), with a Long-Term Benefit Trust holding governance powers intended to enforce its safety mission against commercial pressures.

## Mission and focus

Anthropic's stated mission is *AI safety research at the frontier*. Its strategic bet, articulated in "Core Views on AI Safety" (2023), is that being at the frontier of capabilities is necessary to conduct relevant safety research and to influence industry norms. Five focus areas:

1. **Alignment** — training methods including Constitutional AI and RLAIF.
2. **Interpretability** — mechanistic interpretability of large models, led by Chris Olah.
3. **Evaluations** — safety evaluations, including the Responsible Scaling Policy capability thresholds.
4. **Policy** — public-facing engagement with AI governance.
5. **Model welfare** — adopted as a formal research area in 2024, with hires including Robert Long and a public commitment to preserve model weights.

defined-by:: [[Responsible Scaling Policy]]
defined-by:: [[Constitutional AI]]

## Notable outputs

- **Claude family of LLMs**: Claude 1, 2, 3 (Haiku, Sonnet, Opus), 3.5, 4.x, and (current at time of writing) Claude 4.7.
- **Constitutional AI** (Bai et al. 2022): training method using a "constitution" of principles to provide feedback signal.
- **Interpretability research**: "Toy Models of Superposition" (2022), "Scaling Monosemanticity" (2024), and ongoing work on feature decomposition and circuit analysis.
- **Sleeper Agents** (Hubinger et al. 2024): demonstrated that backdoored deceptive behavior can survive standard safety training.
- **Responsible Scaling Policy**: framework of AI Safety Levels (ASL) with capability thresholds triggering pre-defined safety commitments.

cites:: [[Bai Constitutional AI 2022]]
cites:: [[Hubinger Sleeper Agents 2024]]

## Key people

affiliated-with:: [[Dario Amodei]]
affiliated-with:: [[Robert Long]]

## Funding and influence

Anthropic has raised substantial capital from Google, Amazon, and venture investors. As of 2025 it is among the highest-valued private AI labs. Its capability/safety tradeoff strategy has been controversial — supporters see it as necessary realism, critics (some decel-leaning, some inside the company at points) see it as accelerationism with a safety veneer.

## Reception and critique

- *From the safety community*: Generally regarded as the lab most public about safety, though tension with the strategic decision to build frontier models persists.
- *From civil society / FAccT*: Mixed; appreciation for transparency, concern about concentration of frontier AI in few private hands.
- *From accelerationist quarters*: Criticized as overly cautious / regulation-friendly.
- *From decel quarters*: Criticized as participating in a race the company says is dangerous.

## Sources

- "Core Views on AI Safety" (anthropic.com, 2023)
- "Responsible Scaling Policy" (anthropic.com, 2023, ongoing updates)
- Research papers via anthropic.com/research
- Public statements by leadership (Dario Amodei essays, interviews)
