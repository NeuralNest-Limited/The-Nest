---
id: responsible-scaling-policy
title: Responsible Scaling Policy (RSP)
type: concept
status: draft
created: 2026-05-20
last_reviewed: 2026-05-20
authored_by: claude-opus-4-7
schema_version: 0.1
summary: A safety framework — originated by Anthropic, adopted with variants by OpenAI and Google DeepMind — that commits a frontier lab to specific safety measures triggered by demonstrated capability thresholds, intended to scale safety as capability grows.
confidence: 0.9
source_tier: 1
topics: [ai-safety/evaluation, governance/self-regulation, ai-safety]
perspective: neutral
aliases: [RSP, Anthropic RSP, capability thresholds, frontier safety framework]
sources:
  - type: official-statement
    title: "Anthropic's Responsible Scaling Policy"
    venue: anthropic.com
    year: 2023
    accessed: 2026-05-20
  - type: official-statement
    title: "Preparedness Framework"
    venue: openai.com
    year: 2023
    accessed: 2026-05-20
  - type: official-statement
    title: "Frontier Safety Framework"
    venue: deepmind.google
    year: 2024
    accessed: 2026-05-20
related: [[ASL Levels]], [[Anthropic]], [[AI Safety]]
---

# Responsible Scaling Policy (RSP)

> A self-regulatory commitment in which a frontier AI lab promises specific safety measures that trigger when models demonstrate specific capabilities — intended to bind future deployment decisions in advance of the capability emerging.

## Origin

Articulated by Anthropic in September 2023 as the original "Responsible Scaling Policy." OpenAI followed with the "Preparedness Framework" in December 2023; Google DeepMind released the "Frontier Safety Framework" in May 2024. These three are similar in structure though differ in detail. The umbrella term "RSP" is sometimes used generically; "Frontier Safety Frameworks" is also generic.

defined-by:: [[Anthropic RSP 2023]]
coined-by:: [[Dario Amodei]] / [[Anthropic]]

## Core claim

The RSP framework rests on four ideas:

1. **Capability thresholds**: define specific dangerous capabilities (e.g., uplift in CBRN-weapon development, autonomous-agent capabilities, capacity to evade oversight) and the evaluations that detect them.
2. **Pre-commitment**: specify in advance the safety measures that must be in place before deploying models above each threshold.
3. **Pause clause**: if a model demonstrates a threshold capability without the corresponding safety measures available, deployment pauses.
4. **Public commitment**: the policy is published; performance against it is auditable.

The thesis: rather than retroactively responding to dangerous capabilities, lock in safety commitments now, when capabilities aren't yet at the threshold and incentives to follow the policy haven't sharpened.

## Variants across frontier labs

| Lab | Name | Threshold structure | Notable distinctives |
|---|---|---|---|
| Anthropic | RSP | ASL (AI Safety Levels) 1–4+ | Most-developed public version; multiple revisions |
| OpenAI | Preparedness Framework | Four risk categories × four levels | Tracks per-domain rather than overall level |
| Google DeepMind | Frontier Safety Framework | Critical Capability Levels (CCLs) | Less prescriptive on triggered actions |

extends:: [[AI Safety]]
defined-by:: [[ASL Levels]]

## Evaluation methods

RSPs depend on dangerous-capability evaluations conducted before training runs cross thresholds:

- **Bio capability evals**: testing knowledge that could uplift bioweapon development.
- **Cyber capability evals**: offensive cybersecurity tasks.
- **Autonomous-agent evals** ([[METR]] tasks, Apollo Research, internal lab evals): how independently can the model conduct multi-step research and engineering work.
- **Persuasion / deception evals**: targeted behaviors relevant to alignment concerns.

Frontier labs publish methodology details; results are typically published with redactions for sensitive findings.

cites:: [[Apollo Research]]
cites:: [[METR]]
applies-to:: [[Frontier Model Training]]

## Critiques

- **Voluntary self-regulation**: RSPs are not legally binding. A lab in commercial trouble could simply revise the policy. Critics argue this is a fundamental weakness.
- **Threshold gaming**: defining the threshold is itself the alignment-critical decision. If thresholds are set too high, the framework is theatre; too low, it constrains capability uneconomically.
- **Evaluation reliability**: assessment depends on capability evaluations being able to detect the capability — which may be hard for capabilities involving deception, situational awareness, or long-horizon planning.
- **Public version vs internal**: the public RSP may not match internal practice; auditability requires third-party verification (UK AISI, US AISI pre-deployment access partially addresses this).
- **Race-to-the-bottom risk**: if competitors don't adopt similar policies, pre-commitment may be unilateral disadvantage. The 2024 internal Anthropic / OpenAI / DeepMind partial-coordination on frameworks attempts to address this.

criticized-by:: [[Eliezer Yudkowsky]] (insufficient given x-risk)
criticized-by:: [[Yann LeCun]] (excessive given lack of demonstrated risk)

## Notable revisions

- **Anthropic RSP v1.0** (Sept 2023): initial framework with ASL-1 through ASL-4 definitions.
- **Anthropic RSP v2.0** (Oct 2024): substantial revision adding more capability thresholds, clearer evaluation triggers, governance commitments.
- Future revisions expected as capability levels and evaluation methods mature.

## Open questions

- Can RSPs be made legally binding? (US AISI / UK AISI evaluation partnerships partially address but lack enforcement.)
- What evaluation methodologies are robust to deceptive alignment?
- How do RSPs interact with [[debate-pause-frontier-ai]] — is RSP-style pre-commitment a reasonable middle ground or insufficient response?
- What governance is appropriate for the case where a lab decides to revise its RSP downward under commercial pressure?

## Relationships

instance-of:: [[AI Safety]]
extends:: [[ASL Levels]]
applies-to:: [[Frontier Model Training]]
applies-to:: [[debate-pause-frontier-ai]]
related:: [[UK AISI]]
related:: [[US AISI]]
related:: [[Apollo Research]]
related:: [[METR]]
