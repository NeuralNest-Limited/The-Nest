---
id: constitutional-ai
title: Constitutional AI
type: concept
status: draft
created: 2026-05-20
last_reviewed: 2026-05-20
authored_by: claude-opus-4-7
schema_version: 0.1
summary: Anthropic's alignment training method that supplements human feedback with AI-generated feedback against a written set of principles (a "constitution"), reducing human label volume while maintaining or improving alignment behaviour.
confidence: 0.9
source_tier: 1
topics: [ai-safety/alignment, ai-safety/alignment/outer]
perspective: neutral
aliases: [CAI, RLAIF, RL from AI feedback]
sources:
  - type: preprint
    title: "Constitutional AI: Harmlessness from AI Feedback"
    authors: [Bai Y., Kadavath S., Kundu S., et al.]
    venue: Anthropic / arXiv
    year: 2022
    arxiv_id: 2212.08073
    url: https://arxiv.org/abs/2212.08073
    accessed: 2026-05-20
  - type: official-statement
    title: "Claude's Constitution"
    venue: anthropic.com
    year: 2023
    accessed: 2026-05-20
related: [[RLHF]], [[AI Alignment]], [[Anthropic]]
---

# Constitutional AI

> A training method that uses a written set of principles (a "constitution") plus AI-generated feedback against those principles to align language models, reducing reliance on human preference labels.

## Origin

Introduced by Anthropic in Bai et al. (2022) "Constitutional AI: Harmlessness from AI Feedback." Developed as a response to limitations of pure RLHF: human label collection is expensive, slow, and can produce inconsistent or biased preferences, especially for nuanced harmlessness questions.

coined-by:: [[Anthropic]]
defined-by:: [[Bai Constitutional AI 2022]]

## Core claim

The CAI procedure has two stages:

1. **Supervised stage (CAI-SL)**: An initial model is prompted to critique and revise its own outputs against the constitution's principles. The revised outputs serve as training data for supervised fine-tuning.
2. **Reinforcement stage (CAI-RL / RLAIF)**: The model is asked to compare pairs of outputs and pick which better follows the constitution. These AI preferences train a reward model; the policy is then RL-trained against this reward model — analogous to RLHF but with AI-generated comparisons instead of (or alongside) human ones.

The result: a model trained primarily on principles-plus-AI-judgment, with much less human comparison labelling required.

extends:: [[RLHF]]

## Variants and refinements

- **CAI-SL only**: supervised-only variant; simpler but typically weaker.
- **CAI-RL (RLAIF)**: the full method; comparable or better than RLHF in Anthropic's evaluations.
- **Hybrid (RLHF + RLAIF)**: many production systems combine both signals.
- **Constitution variants**: principles can be drawn from UN Declaration of Human Rights, Asimov-style rules, expert-curated lists, or empirical / democratic processes (e.g., Anthropic's Collective Constitutional AI experiment with public input).

## Evidence

- Bai et al. 2022 reported that CAI-RL trained models matched or exceeded RLHF-trained models on Anthropic's harmlessness and helpfulness evaluations, while requiring substantially less human labelling.
- CAI is the published basis for Anthropic's Claude family.
- Subsequent RLAIF research at other labs (Lee et al. 2023 at Google; various academic groups) corroborates the general approach.

cited-in:: [[Anthropic]]

## Critiques

- **Self-reference / mode collapse risk**: training a model on its own preferences can amplify the model's existing biases rather than correct them.
- **Constitution authorship**: who writes the constitution is a contested political question — different constitutions produce meaningfully different models.
- **Indirection of accountability**: pure RLHF makes human preferences the accountability anchor; CAI partially offloads that to AI judgement, raising questions about responsibility for outputs.
- **Empirical limits**: CAI does not eliminate alignment failures — sycophancy, jailbreaking, hallucination all persist in CAI-trained models, though sometimes at different rates than RLHF baselines.

criticized-by:: [[Stochastic Parrots]] tradition (the broader concern about training-data politics applies)

## Open questions

- What constitution-design principles produce alignment that generalizes well across cultures and contexts?
- Can CAI be used to train models on values democratically chosen by affected communities?
- Does CAI scale to capability levels where AI judgement may become unreliable in different ways than human judgement?

## Relationships

extends:: [[RLHF]]
applies-to:: [[Claude]]
related:: [[Scalable Oversight]]
related:: [[AI Alignment]]
