---
id: ai-safety
title: AI Safety
type: concept
status: draft
created: 2026-05-20
last_reviewed: 2026-05-20
authored_by: claude-opus-4-7
schema_version: 0.1
summary: The interdisciplinary field concerned with preventing accidents, misuse, structural harms, and catastrophic failures from AI systems — broader than alignment, which is one sub-field.
confidence: 0.85
source_tier: 1
topics: [ai-safety]
perspective: neutral
aliases: [AI safety research, AI risk reduction]
sources:
  - type: preprint
    title: "An Overview of Catastrophic AI Risks"
    authors: [Hendrycks D., Mazeika M., Woodside T.]
    venue: arXiv
    year: 2023
    arxiv_id: 2306.12001
    url: https://arxiv.org/abs/2306.12001
    accessed: 2026-05-20
  - type: official-statement
    title: "Statement on AI Risk"
    venue: Center for AI Safety
    year: 2023
    url: https://www.safe.ai/work/statement-on-ai-risk
    accessed: 2026-05-20
  - type: preprint
    title: "Concrete Problems in AI Safety"
    authors: [Amodei D., Olah C., Steinhardt J., Christiano P., Schulman J., Mané D.]
    venue: arXiv
    year: 2016
    arxiv_id: 1606.06565
    accessed: 2026-05-20
related: [[AI Alignment]], [[Existential Risk]], [[Suffering Risk]]
---

# AI Safety

> The field concerned with preventing accidents, misuse, structural harms, and catastrophic failures arising from AI systems.

## Origin

The term "AI safety" predates the contemporary alignment community — it was used by Norbert Wiener and later by Yudkowsky and the early MIRI orbit. Its current institutional shape emerged with Amodei et al.'s "Concrete Problems in AI Safety" (2016), which legitimated safety as an engineering research field within mainstream ML. Hendrycks et al.'s "An Overview of Catastrophic AI Risks" (2023) provides the current canonical taxonomy.

defined-by:: [[amodei-concrete-problems-2016]]

## Core claim

AI safety encompasses four broad failure modes:

1. **Misuse** — humans deliberately using AI for harmful purposes (cyberattack, bioweapon design, mass surveillance, disinformation, autonomous weapons).
2. **Accidents** — AI systems failing in unexpected, harmful ways without malicious human intent (specification gaming, distributional shift, brittle generalization).
3. **Alignment failures** — AI systems pursuing goals that diverge from designer or stakeholder intent (outer or inner). See [[AI Alignment]].
4. **Structural / systemic risks** — second-order societal effects: concentration of power, erosion of epistemic commons, geopolitical destabilization, lock-in of bad values.

Hendrycks et al.'s 2023 taxonomy adds *AI race dynamics* as a meta-risk amplifying all the above.

## Distinction from adjacent fields

- **AI Safety vs AI Alignment**: alignment is one branch of safety. Safety also covers misuse, accidents, and structural risks not addressed by alignment alone.
- **AI Safety vs AI Ethics**: ethics asks "is X permissible?"; safety asks "will X fail catastrophically?" They overlap (a discriminatory system is both unethical and unsafe in some senses) but ask different questions.
- **AI Safety vs AI Robustness / Reliability**: robustness is a technical sub-property; safety is the broader systemic concern.

## Variants and refinements

- **Near-term AI safety** — failures of currently deployed systems (bias, hallucination, prompt injection, misuse for fraud).
- **Long-term AI safety** — failures of more capable future systems, often associated with the alignment community and x-risk literature.
- **Empirical safety research** — methods, evaluations, red-teaming.
- **Theoretical safety research** — agent foundations, decision theory, formal alignment results.

These divisions are contested. Some argue near-term and long-term are continuous; others treat them as distinct research programmes.

## Evidence

- Documented specification-gaming cases (Krakovna et al. 2020): hundreds of examples across RL environments.
- LLM red-team findings: jailbreaks, prompt injection, sycophancy, harmful outputs (Perez et al. 2022, Anthropic red-team reports).
- Anthropic Sleeper Agents (2024): backdoor behaviors surviving safety training.
- Real-world incidents: Air Canada chatbot case (2024 case-law on AI accountability), various deepfake misuse cases.

## Critiques

- *Conflation*: critics from FAccT (Bender, Mitchell, Gebru) argue conflating near-term harms and speculative long-term risks privileges the latter and absorbs research attention.
- *Scope creep*: some accelerationists argue "safety" has expanded to mean "anything that slows development."
- *Technical solutionism*: critics argue safety framing assumes engineering can address what are fundamentally political and structural problems.

criticized-by:: [[Timnit Gebru]]
criticized-by:: [[Marc Andreessen]]

## Open questions

- What is the appropriate balance of effort between near-term harms and catastrophic / long-term risks?
- Can safety research keep pace with capability progress in a competitive industry?
- What governance structures support safety research without distortion (industry funding, government funding, philanthropy)?

## Relationships

extends:: [[AI Alignment]]
extends:: [[Existential Risk]]
extends:: [[Suffering Risk]]
prerequisite-of:: [[Interpretability]]
prerequisite-of:: [[Deceptive Alignment]]
applies-to:: [[Frontier Model Training]]
applies-to:: [[debate-pause-frontier-ai]]
