---
id: rlhf
title: Reinforcement Learning from Human Feedback (RLHF)
type: concept
status: draft
created: 2026-05-20
last_reviewed: 2026-05-20
authored_by: claude-opus-4-7
schema_version: 0.1
summary: A training method in which a reward model is learned from human preference comparisons between model outputs, and the model is then RL-trained against that reward model — the technique that underpins ChatGPT and most current instruction-tuned LLMs.
confidence: 0.95
source_tier: 1
topics: [ai-safety/alignment, ai-safety/alignment/outer, ai-capabilities]
perspective: neutral
aliases: [Reinforcement Learning from Human Feedback]
sources:
  - type: peer-reviewed-paper
    title: "Deep Reinforcement Learning from Human Preferences"
    authors: [Christiano P., Leike J., Brown T., Martic M., Legg S., Amodei D.]
    venue: NeurIPS
    year: 2017
    arxiv_id: 1706.03741
    url: https://arxiv.org/abs/1706.03741
    accessed: 2026-05-20
  - type: preprint
    title: "Training language models to follow instructions with human feedback"
    authors: [Ouyang L., Wu J., Jiang X., et al.]
    venue: OpenAI / arXiv (InstructGPT)
    year: 2022
    arxiv_id: 2203.02155
    accessed: 2026-05-20
related: [[Constitutional AI]], [[Paul Christiano]], [[AI Alignment]]
---

# Reinforcement Learning from Human Feedback (RLHF)

> Train a reward model from human comparisons of model outputs; then RL-train the policy against that reward. The dominant technique for aligning current frontier LLMs to instruction-following and harmlessness.

## Origin

The core algorithm was introduced in Christiano et al. (2017) "Deep RL from Human Preferences" — a joint OpenAI/DeepMind paper demonstrating the technique on Atari and simulated robotics tasks. Applied to language modeling in OpenAI's InstructGPT (Ouyang et al. 2022) and immediately afterward in ChatGPT (November 2022), which made RLHF the de facto industry standard.

coined-by:: [[Paul Christiano]]
defined-by:: [[christiano-deep-rl-from-human-preferences-2017]]

## Core claim

RLHF works in three stages:

1. **SFT**: Start with a pretrained language model and fine-tune on demonstrations of desired behavior (instruction-tuning).
2. **Reward modeling**: Collect human comparisons of pairs of model outputs (which is better?). Train a neural-network reward model to predict human preferences.
3. **RL fine-tuning**: Use Proximal Policy Optimization (PPO) or similar to fine-tune the language model to maximize the learned reward, typically with a KL penalty against the SFT-tuned model to prevent drift.

The result is a model that follows instructions, refuses harmful requests, and produces responses humans tend to prefer.

extends:: [[Pretraining-Finetuning Paradigm]]

## Variants and refinements

- **RLHF with PPO** (Christiano 2017 / InstructGPT 2022): canonical implementation.
- **Direct Preference Optimization (DPO)** (Rafailov et al. 2023): mathematically equivalent reformulation skipping the reward model — train directly from preference pairs.
- **RLAIF / Constitutional AI** (Bai et al. 2022): AI-generated comparisons replace or supplement human ones. See [[Constitutional AI]].
- **Best-of-N sampling**: a deployment-time variant — sample N completions and pick the highest-reward one.
- **Multi-objective RLHF**: separate reward models for helpfulness, harmlessness, honesty etc., composed at training time.

## Evidence

RLHF is empirically validated by the wide deployment of RLHF-trained models — ChatGPT, Claude, Gemini, Llama-Instruct families. The technique reliably produces:

- Improved instruction-following.
- Reduced harmful outputs (relative to base models, not zero).
- Higher human preference scores.

extended-by:: [[Constitutional AI]]
extended-by:: [[Direct Preference Optimization]]

## Critiques

- **Reward hacking / sycophancy**: RLHF-trained models often optimize for *what humans rate highly* rather than ground-truth quality — producing sycophancy, length bias, hedging. See [[Sycophancy]].
- **Outer alignment limits**: RLHF aligns outputs to human-rated quality on observable behaviour; whether internal goals align is the central [[Mesa-Optimization]] / inner-alignment question RLHF does not address.
- **Label quality and scale**: human raters are expensive, inconsistent, and subject to fatigue / bias. Quality control is a serious operational problem.
- **Labour conditions**: documented poor working conditions for human raters in some commercial pipelines (Time investigation 2023 on Kenyan raters working on harmful content).
- **Cultural narrowness**: rater pools are typically Anglophone and Western, importing those cultural biases into outputs.

criticized-by:: [[Anthropic Sycophancy Studies]]

## Open questions

- What's the right ratio of human to AI feedback as capabilities scale?
- Can RLHF be improved to capture distributed / pluralistic preferences rather than rater-aggregate averages?
- What's the relationship between RLHF and inner alignment — does RLHF entrench mesa-objectives or shape them productively?
- Are there preference-elicitation methods less vulnerable to rater fatigue and bias?

## Relationships

defined-by:: [[christiano-deep-rl-from-human-preferences-2017]]
extends:: [[AI Alignment]]
applies-to:: [[Claude]]
applies-to:: [[ChatGPT]]
related:: [[Constitutional AI]]
related:: [[Sycophancy]]
