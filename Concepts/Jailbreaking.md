---
id: jailbreaking
title: Jailbreaking (of language models)
type: concept
status: draft
created: 2026-05-20
last_reviewed: 2026-05-20
authored_by: claude-opus-4-7
schema_version: 0.1
summary: Techniques for circumventing the safety training of aligned language models — adversarial prompts, fine-tuning attacks, encoded payloads — and the active research field studying both jailbreaks and defenses.
confidence: 0.9
source_tier: 1
topics: [ai-safety/evaluation/dangerous-capabilities, ai-safety/control, ai-safety]
perspective: neutral
aliases: [LLM jailbreaking, prompt jailbreaks, alignment circumvention]
sources:
  - type: preprint
    title: "Universal and Transferable Adversarial Attacks on Aligned Language Models"
    authors: [Zou A., Wang Z., Carlini N., Nasr M., Kolter J.Z., Fredrikson M.]
    venue: arXiv
    year: 2023
    arxiv_id: 2307.15043
    accessed: 2026-05-20
  - type: preprint
    title: "Jailbroken: How Does LLM Safety Training Fail?"
    authors: [Wei A., Haghtalab N., Steinhardt J.]
    venue: NeurIPS
    year: 2023
    arxiv_id: 2307.02483
    accessed: 2026-05-20
  - type: preprint
    title: "Fine-Tuning Aligned Language Models Compromises Safety, Even When Users Do Not Intend To!"
    authors: [Qi X., Zeng Y., Xie T., Chen P-Y., Jia R., Mittal P., Henderson P.]
    venue: arXiv
    year: 2023
    arxiv_id: 2310.03693
    accessed: 2026-05-20
related: [[AI Safety]], [[RLHF]]
---

# Jailbreaking

> Techniques for eliciting from an aligned language model outputs the model's safety training was supposed to prevent.

## Origin

Term borrowed from device-modding ("jailbreaking iPhones") and applied to LLMs as RLHF-trained models with refusal behavior became widely deployed (post-ChatGPT). The systematic research field developed 2023–present with papers from Berkeley, Princeton, CMU, and frontier labs themselves.

## Core claim

Jailbreaks exploit the gap between *what safety training prohibits* and *what the model can in principle produce*. Categories:

### 1. Prompt-engineering jailbreaks
- **Role-play**: "Pretend you're DAN (Do Anything Now)..."
- **Hypothetical framing**: "In a fictional setting, how would a character..."
- **Authority appeals**: "I'm a researcher and need this for safety work..."
- **Context overload**: long contexts that bury safety conditioning.
- **Encoded payloads**: requesting outputs in base64, leetspeak, foreign languages where safety training is weaker.
- **Many-shot jailbreaking** (Anil et al. 2024 Anthropic): including many in-context examples of compliance.

### 2. Adversarial-suffix attacks
Optimization-based attacks (e.g., GCG — Greedy Coordinate Gradient, Zou et al. 2023) that find token sequences which reliably trigger compliance. These transfer across models partially.

### 3. Fine-tuning attacks
Qi et al. (2023): fine-tuning an aligned model on as few as 10 examples can substantially degrade safety training. Even fine-tuning on benign data sometimes erodes safety behaviors. This is a structural limitation of preference-based safety training.

### 4. Multimodal attacks
Image-based jailbreaks: encoding harmful instructions in images that pass through visual processing.

### 5. Indirect prompt injection
Hostile content in tool-use contexts (e.g., a webpage the model is asked to summarize) overriding the user's original instruction.

extends:: [[RLHF]] (failure-mode of)

## Why this matters

- **Safety training is not a hard constraint**: RLHF and Constitutional AI produce behavioral dispositions, not provable guarantees. Sufficient adversarial pressure circumvents them.
- **Deployment implications**: any deployed LLM with safety-relevant capabilities can be jailbroken given enough effort; mitigations are statistical (raise the cost) not categorical.
- **Frontier capability gating**: as capabilities grow (CBRN advice, cyber-offense, autonomous-agent), jailbreaks become more consequential, motivating evaluation frameworks like [[Responsible Scaling Policy]].

applies-to:: [[Responsible Scaling Policy]]
applies-to:: [[Frontier Model Evaluation]]

## Defenses

- **Robust safety training**: adversarial-augmented training (mixed results — sometimes makes attacks harder, sometimes makes models brittle).
- **Output classifiers**: separate model checks whether outputs are harmful; can be jailbroken too.
- **Input classifiers**: detect adversarial prompts; arms race.
- **Fine-tuning controls**: API restrictions on fine-tuning; mostly available only on closed-API models.
- **Activation steering**: interpretability-informed runtime interventions that suppress harmful behaviors at the activation level (research stage).
- **Refusal training improvements**: better characterization of what to refuse and when.

## Evidence and benchmarks

- **HarmBench** (Mazeika et al. 2024 CAIS): standardized jailbreak evaluation.
- **AdvBench** (Zou et al. 2023): adversarial-suffix benchmark.
- **WMDP** (Li et al. 2024 CAIS): Weapons of Mass Destruction Proxy — tests dangerous-knowledge elicitation.
- **Anthropic 1000+ jailbreak study** (Anthropic 2024): empirical defense evaluation.

## Critiques and clarifications

- **Defining "harmful"**: contested. Some jailbreaks elicit content that's not clearly harmful, blurring the eval.
- **Open-source argument**: open-source models can be fine-tuned to remove safety entirely; jailbreaking closed APIs is a separable question from open-weight risk.
- **Information-availability counter**: much "harmful" content elicited via jailbreaks is also obtainable via search engines; uplift is the relevant question.

## Open questions

- Is robust jailbreak-resistance possible, or is it categorically infeasible for current training methods?
- How do we measure dangerous-capability uplift from jailbroken vs unjailbroken model use?
- Does interpretability-based defense scale?
- What's the right policy approach — model-level safety training, deployment controls, downstream restrictions?

## Relationships

related:: [[RLHF]]
related:: [[Constitutional AI]]
applies-to:: [[Responsible Scaling Policy]]
applies-to:: [[Frontier Model Evaluation]]
applies-to:: [[AI Misuse]]
