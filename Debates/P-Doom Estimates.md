---
id: debate-p-doom-estimates
title: P(doom) — How High Are Existential Risk Estimates and What Are They Tracking?
type: debate
status: draft
created: 2026-05-20
last_reviewed: 2026-05-20
authored_by: claude-opus-4-7
schema_version: 0.1
summary: Publicly stated probability estimates of catastrophic or extinction-level outcomes from AI range across orders of magnitude among researchers. Debate addresses what these numbers track, whether they are useful, and how they should inform action.
confidence: 0.75
source_tier: 2
topics: [futures/risk/x-risk, futures/risk, meta/methodology]
perspective: neutral
aliases: [P(doom), p-doom debate, AI extinction risk probability]
positions:
  - name: Numbers track real expert credence (and are high)
    summary: P(doom) estimates capture genuine uncertainty among experts; current levels (median ~5-10% in surveys, higher among many alignment researchers) warrant priority action.
    key_proponents: [[Yoshua Bengio]], [[Geoffrey Hinton]], [[Eliezer Yudkowsky]] (with much higher estimates), AI Impacts survey results
  - name: Numbers are useful but should not drive action
    summary: P(doom) estimates have communicative value but are too unreliable to direct policy; action should be driven by mechanism analysis and tractability.
    key_proponents: [[Anthropic]] leadership, much of AI safety community
  - name: Numbers are meaningless or actively misleading
    summary: P(doom) estimates are not well-calibrated probabilities; presenting them as such misleads about the state of evidence and damages the credibility of safety arguments.
    key_proponents: [[Andrew Critch]], [[Robin Hanson]], some safety researchers
  - name: Numbers serve political function
    summary: P(doom) numbers are political artifacts shaping discourse and resource allocation; their epistemic content is secondary to their rhetorical use.
    key_proponents: [[FAccT critics]], [[Émile Torres]]
open_questions:
  - What would constitute calibration evidence for or against P(doom) estimates?
  - Is there a methodologically defensible way to elicit and aggregate P(doom)-style probabilities?
  - How should policy respond to wide expert disagreement on existence and magnitude of risk?
sources:
  - type: peer-reviewed-paper
    title: "AI Impacts 2023 Expert Survey"
    venue: AI Impacts
    year: 2023
    accessed: 2026-05-20
  - type: expert-blog
    title: "Various P(doom) discussions"
    venue: LessWrong / Effective Altruism Forum
    year: 2023
    accessed: 2026-05-20
related: [[Existential Risk]], [[AGI]]
---

# P(doom) — How High Are Existential Risk Estimates and What Are They Tracking?

> "P(doom)" — shorthand for personal probability of catastrophic or extinction-level outcomes from AI — has become a focal datum in AI risk discourse. Different observers report estimates ranging from <1% to >90%. The debate addresses what these numbers mean, how they should be elicited, and whether they should drive action.

## Why this matters

P(doom) numbers shape:

- Resource allocation toward safety research.
- Policy urgency framings.
- Public perception of AI risk.
- Recruiting into AI safety vs. capability roles.
- Credibility battles between camps.

## Position A — Numbers track real expert credence and are high

`perspective: cautious`

Steel-manned statement: stated P(doom) estimates reflect genuine expert credences after careful reflection. Reported numbers (AI Impacts surveys: median ~5-10% for "extremely bad" HLMI outcomes; many alignment researchers ~10-25%; some — Yudkowsky — >90%) imply substantial action.

**Key proponents**: [[Yoshua Bengio]], [[Geoffrey Hinton]], [[Stuart Russell]] (more carefully framed), AI Impacts surveys, much of safety community.

**Strongest arguments**:
1. Surveys consistently show non-trivial expert credence; the convergence is real.
2. Reasoned mechanism analysis (Bostrom, Yudkowsky, Carlsmith) supports non-trivial probability.
3. Even if numbers are imprecise, the qualitative claim (non-negligible probability of very bad outcomes) is robust.

**Common objections handled**:
- *"Numbers are unreliable"*: agreed but the qualitative conclusion is robust to wide error bars.
- *"Why action at these levels?"*: by analogy to other low-probability catastrophic risks (asteroid, pandemic) which justify substantial investment.

position-in:: [[debate-p-doom-estimates]]

## Position B — Numbers are useful but should not drive action

`perspective: safety-pragmatist`

Steel-manned statement: P(doom) estimates have communicative and triage value but are not well-calibrated enough to drive specific policy. Action should be driven by mechanism analysis (what specifically can go wrong, what specifically prevents it) and tractability (what can we actually do).

**Key proponents**: [[Anthropic]] leadership (Amodei's framing), much of mainline AI safety practice.

**Strongest arguments**:
1. Probabilistic reasoning under deep uncertainty is unreliable; over-relying on numbers risks confidence-without-warrant.
2. Mechanism analysis yields more action-relevant outputs than probability summaries.
3. Public communication using P(doom) numbers risks alienating audiences who recognize the brittleness.

position-in:: [[debate-p-doom-estimates]]

## Position C — Numbers are meaningless or actively misleading

`perspective: descriptive`

Steel-manned statement: P(doom) estimates are not well-defined probabilities. There is no clearly specified event, no shared time-horizon, no shared definition of "doom," and no calibration mechanism. Presenting numbers as if they had probabilistic content misleads about the actual state of evidence and damages safety arguments by tying them to numbers critics can credibly attack.

**Key proponents**: [[Andrew Critch]] (in some framings), [[Robin Hanson]] (probability skepticism for distant events), some safety researchers internally.

**Strongest arguments**:
1. Definitional unclarity: "doom by 2100" is not a probability-bearing event without sharp definition.
2. Calibration impossibility: we have no reference class for unprecedented events.
3. Communication: numbers create false impressions of analytical rigor.

position-in:: [[debate-p-doom-estimates]]
contradicts:: Position A

## Position D — Numbers serve political function

`perspective: cautious` (about discourse dynamics)

Steel-manned statement: P(doom) numbers function as political artifacts in AI discourse. They mobilize resources, structure recruitment, and signal coalition membership. Whatever their epistemic content, their rhetorical use is primary and should be analyzed as such.

**Key proponents**: [[Émile Torres]], [[FAccT critics]] of longtermist framings.

**Strongest arguments**:
1. The dramatic numerical disagreement among experts undermines claims of evidence-based discourse.
2. The number-framing privileges certain epistemic styles (Bayesian-rationalist) over others.
3. Resources follow the numbers; political function is empirical, not interpretive.

position-in:: [[debate-p-doom-estimates]]

## Cross-cutting considerations

- **Epistemics vs. rhetoric**: positions disagree about whether the numbers are primarily epistemic instruments or rhetorical ones.
- **Calibration**: positions diverge on whether the relevant kind of calibration is even possible.
- **Time-horizon**: P(doom by 2050) and P(doom by 2100) are different claims with different evidential bases.

## Open questions

- Are there elicitation methods (e.g., Tetlock-style forecasting tournaments adapted for AI) that would produce more useful credence estimates?
- What is the relationship between P(doom) estimates and willingness to take specific protective actions?
- How should communication about AI risk handle the wide expert disagreement honestly?

## Relationships

related:: [[Existential Risk]]
related:: [[Pascal's Mugging]]
applies-to:: [[AI Forecasting]]
applies-to:: [[debate-pause-frontier-ai]]
