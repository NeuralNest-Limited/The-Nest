---
id: asl-levels
title: AI Safety Levels (ASL) — Anthropic's RSP capability tiers
type: concept
status: draft
created: 2026-05-20
last_reviewed: 2026-05-20
authored_by: claude-opus-4-7
schema_version: 0.1
summary: Anthropic's tiered capability framework — ASL-1 through ASL-5 (and beyond) — defining specific dangerous-capability thresholds and the safety measures that must accompany models at each level.
confidence: 0.85
source_tier: 1
topics: [ai-safety/evaluation, ai-safety/evaluation/dangerous-capabilities, ai-safety]
perspective: neutral
aliases: [AI Safety Level, ASL, ASL-1, ASL-2, ASL-3, ASL-4]
sources:
  - type: official-statement
    title: "Anthropic's Responsible Scaling Policy"
    venue: anthropic.com
    year: 2023
    accessed: 2026-05-20
  - type: official-statement
    title: "Anthropic Responsible Scaling Policy v2.0"
    venue: anthropic.com
    year: 2024
    accessed: 2026-05-20
related: [[Responsible Scaling Policy]], [[Anthropic]]
---

# AI Safety Levels (ASL)

> Anthropic's tiered capability framework — modelled loosely on biosafety levels (BSL) — defining specific dangerous-capability thresholds and the safety / containment measures models at each level require.

## Origin

Introduced in Anthropic's September 2023 Responsible Scaling Policy. The framework borrows its tier vocabulary from biosafety levels in laboratory biology (BSL-1 through BSL-4), explicitly invoking the analogy of containment-by-capability-level. Revised in RSP v2.0 (October 2024).

defined-by:: [[Anthropic RSP 2023]]

## Core claim

Each ASL level pairs a *capability threshold* with *deployment and security requirements*. As of RSP v2.0 (2024), the levels are roughly:

### ASL-1
- **Capabilities**: clearly non-dangerous models (e.g., chess engines, small ML models). Mostly retroactive — applies to most pre-LLM AI.
- **Requirements**: minimal.

### ASL-2
- **Capabilities**: shows early signs of dangerous capabilities (some uplift on CBRN questions, some autonomous-agent capability, but not crossing actionable thresholds).
- **Requirements**: standard safety training (RLHF / Constitutional AI), red-teaming before deployment, basic responsible-disclosure practices. **Claude 3 family** was deployed at ASL-2.

### ASL-3
- **Capabilities**: substantial uplift in CBRN or autonomous-research capability — meaningfully more dangerous than internet-available baselines.
- **Requirements**: enhanced security (weights protection against well-funded attackers, internal compartmentalization), red-teaming including external evaluators, deployment-time monitoring, more aggressive misuse prevention. **Claude Opus 4 family** reached and triggered ASL-3 measures.

### ASL-4 (conceptual)
- **Capabilities**: substantial autonomous research / agentic capability; potential to meaningfully accelerate AI development.
- **Requirements**: state-actor-level security; evidence of robust alignment beyond behavioral compliance (interpretability, evals against deception); contingency planning for severe scenarios.

### ASL-5 and beyond (conceptual)
- **Capabilities**: substantially superhuman across multiple domains.
- **Requirements**: very strong — possibly including international coordination, deployment pauses pending evaluation methodology improvement.

extends:: [[Responsible Scaling Policy]]

## How levels are determined

The ASL classification is *behavior-and-capability based*, not size-based. A model is assigned a level by:

1. Running dangerous-capability evaluations.
2. Comparing results against pre-specified thresholds.
3. If the model crosses a threshold without the corresponding safety measures in place, deployment pauses.
4. If safety measures are in place, deployment proceeds with the level's commitments active.

Notable: a model can be at ASL-3 even if smaller / less compute than another model at ASL-2, if the smaller model demonstrates threshold capabilities the larger does not.

## Evidence and case history

- **Claude 3 family** (early 2024): assessed at ASL-2; deployed under ASL-2 commitments.
- **Claude 3.5 Sonnet**: ASL-2.
- **Claude 3 Opus / Claude Opus 4 series**: triggered ASL-3 — Anthropic published detailed accounts of the assessments and the resulting security upgrades.
- **GPT-4, Gemini, etc.**: not classified under ASL (which is Anthropic-internal) but similar frameworks (OpenAI Preparedness, DeepMind FSF) have produced comparable assessments.

cited-in:: [[Responsible Scaling Policy]]
cited-in:: [[Anthropic]]

## Critiques

- **BSL analogy limits**: biological containment works on physical samples; AI capabilities exist in weights that can be copied. Containment story is structurally different.
- **Threshold definitions**: who decides what's "ASL-3" vs "ASL-2" — currently Anthropic. External validation (UK AISI, US AISI) partially addresses but doesn't replace.
- **Voluntary**: ASL is internal to Anthropic; no legal force. Anthropic could revise downward under commercial pressure (RSP v2.0 was an upward revision but precedent could go either way).
- **Capability evaluation reliability**: ASL classification relies on capability evaluations actually catching the relevant capabilities, including evaluation-resistant capabilities (deception, situational awareness).

## Open questions

- Should ASL-equivalent frameworks become regulated (national or international standard) rather than voluntary?
- How does ASL classification interact with deployment for specific use cases (a model dangerous in one context might be safe in another)?
- What's the relationship between ASL and competitive dynamics — if Anthropic alone adopts strict ASL-3 while competitors don't, is that net-positive for safety?

## Relationships

instance-of:: [[Responsible Scaling Policy]]
defined-by:: [[Anthropic RSP 2023]]
applies-to:: [[Claude Opus 4]]
applies-to:: [[Frontier Model Training]]
related:: [[UK AISI]]
related:: [[US AISI]]
