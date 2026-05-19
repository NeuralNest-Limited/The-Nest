---
id: christiano-deep-rl-from-human-preferences-2017
title: Deep Reinforcement Learning from Human Preferences
type: paper
status: draft
created: 2026-05-20
last_reviewed: 2026-05-20
authored_by: claude-opus-4-7
schema_version: 0.1
summary: 2017 paper introducing RLHF — reinforcement learning from human preference comparisons — the technique that, applied at scale, underpins ChatGPT and most subsequent instruction-tuned LLMs.
confidence: 0.95
source_tier: 1
topics: [ai-safety/alignment, ai-safety/alignment/outer, ai-capabilities]
authors: [Christiano P.F., Leike J., Brown T.B., Martic M., Legg S., Amodei D.]
venue: NeurIPS
year: 2017
doi: null
arxiv_id: 1706.03741
url: https://arxiv.org/abs/1706.03741
sources:
  - type: peer-reviewed-paper
    title: "Deep Reinforcement Learning from Human Preferences"
    authors: [Christiano P.F., Leike J., Brown T.B., Martic M., Legg S., Amodei D.]
    venue: NeurIPS
    year: 2017
    arxiv_id: 1706.03741
    url: https://arxiv.org/abs/1706.03741
    accessed: 2026-05-20
related: [[AI Alignment]], [[Paul Christiano]]
---

# Deep Reinforcement Learning from Human Preferences

> The 2017 NeurIPS paper introducing reinforcement learning from human feedback (RLHF) — the alignment technique that, scaled and adapted, produced InstructGPT, ChatGPT, Constitutional AI, and the broader paradigm of preference-tuned LLMs.

## Authors and venue

authored-by:: [[Paul Christiano]]
authored-by:: [[Jan Leike]]
authored-by:: [[Tom Brown]]
authored-by:: [[Miljan Martic]]
authored-by:: [[Shane Legg]]
authored-by:: [[Dario Amodei]]

A joint OpenAI / DeepMind collaboration (notable for combining researchers from two competing labs).

Venue: NeurIPS 2017.

## Abstract / paraphrase

The paper proposes a method for training RL agents to perform tasks using human preference comparisons rather than hand-coded reward functions. A reward model is learned from human comparisons of agent behavior; the agent is then trained against the reward model. The paper demonstrates the method on Atari games, simulated robotics, and a "backflip" task that would be difficult to specify with a hand-coded reward.

## Key contributions

1. **Practical algorithm for preference-based RL**: an alternative to specifying reward functions explicitly.
2. **Demonstrated feasibility at non-trivial scale**: not the first work on preference-based RL, but the first showing it works on complex tasks with deep RL.
3. **Data efficiency**: agents could learn complex behaviors from a few hundred to a few thousand human comparisons.
4. **The "backflip" demonstration**: a simulated robot learning to do a backflip — the kind of behavior that is hard to write down a reward function for but easy to recognize.

defined-by:: [[Reinforcement Learning from Human Feedback]]
coined-by:: [[RLHF]]

## Method

Three-component setup:
1. Human raters compare pairs of short agent-behavior video clips.
2. A neural network reward model is trained to predict human preferences from comparisons.
3. An RL agent is trained against the reward model using PPO or similar policy gradient methods.

The reward model is updated as new comparisons come in; the agent's training and reward-model training proceed in parallel.

## Findings

- The method matched or exceeded hand-coded reward performance on Atari games while requiring only ~1000 human comparisons.
- It enabled behaviors that couldn't be easily specified by hand-coded rewards.
- It was more data-efficient than imitation learning.

## Reception

At publication: substantial within the RL community. Subsequent influence has been enormous, far beyond initial reception:

- **InstructGPT (2022)**: applied RLHF to language models, producing the precursor to ChatGPT.
- **ChatGPT (2022)** and downstream LLMs: RLHF is the standard final-stage training method.
- **Constitutional AI** (Anthropic 2022): RLAIF — using AI-generated preferences as reward signal — extends the framework.
- **Subsequent methods**: DPO (Direct Preference Optimization, 2023) and other variants build on the preference-modeling foundation.

The paper is now among the most-cited in AI alignment and LLM training, with citation counts in five figures.

extended-by:: [[InstructGPT 2022]]
extended-by:: [[Constitutional AI 2022]]
extended-by:: [[Direct Preference Optimization 2023]]

## Critiques

- *Reward hacking*: RLHF-trained models can game the reward model rather than satisfy underlying preferences. Increasingly well-documented in LLM context (sycophancy, length bias).
- *Sample efficiency for nuanced preferences*: simple preferences are learnable; nuanced or culturally-specific preferences harder.
- *Alignment vs. capability*: RLHF aligns models with human-rated quality on visible behavior; whether it produces deeper alignment is the central question of inner-alignment research.
- *Labor concerns*: the human-rater workforce has been documented as low-paid and often working under stressful conditions in cases of safety-rating work.

criticized-by:: [[Anthropic Sycophancy Studies]]

## Relevance to coexistence research

RLHF is the bridge between alignment as a theoretical concern and alignment as the deployed practice that makes interactions with LLMs possible. Understanding RLHF — what it does, what it doesn't do — is foundational.

## Sources

Christiano P.F., Leike J., Brown T.B., Martic M., Legg S., Amodei D. (2017). "Deep Reinforcement Learning from Human Preferences." NeurIPS 2017. arXiv:1706.03741.
