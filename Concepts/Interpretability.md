---
id: interpretability
title: Interpretability
type: concept
status: draft
created: 2026-05-20
last_reviewed: 2026-05-20
authored_by: claude-opus-4-7
schema_version: 0.1
summary: Research aiming to understand how AI models compute their outputs — encompassing behavioral interpretability (what the model does) and mechanistic interpretability (how the model does it internally).
confidence: 0.85
source_tier: 1
topics: [ai-safety/interpretability, ai-safety/interpretability/mechanistic, ai-safety]
perspective: neutral
aliases: [mechanistic interpretability, mech-interp, model interpretability]
sources:
  - type: expert-blog
    title: "Zoom In: An Introduction to Circuits"
    authors: [Olah C., Cammarata N., Schubert L., Goh G., Petrov M., Carter S.]
    venue: Distill
    year: 2020
    url: https://distill.pub/2020/circuits/zoom-in/
    accessed: 2026-05-20
  - type: preprint
    title: "Toy Models of Superposition"
    authors: [Elhage N., Hume T., Olsson C., et al.]
    venue: Anthropic
    year: 2022
    arxiv_id: 2209.10652
    accessed: 2026-05-20
  - type: preprint
    title: "Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet"
    authors: [Templeton A., Conerly T., Marcus J., et al.]
    venue: Anthropic
    year: 2024
    url: https://transformer-circuits.pub/2024/scaling-monosemanticity/
    accessed: 2026-05-20
  - type: preprint
    title: "A Mathematical Framework for Transformer Circuits"
    authors: [Elhage N., Nanda N., Olsson C., et al.]
    venue: Anthropic
    year: 2021
    url: https://transformer-circuits.pub/2021/framework/
    accessed: 2026-05-20
related: [[AI Safety]], [[AI Alignment]], [[Deceptive Alignment]]
---

# Interpretability

> Research aiming to understand how AI models compute their outputs — both *what* they do and *how* their internal computations produce that behavior.

## Origin

Interpretability research has parallel lineages:

- **Statistics and classical ML**: feature importance, LIME (Ribeiro et al. 2016), SHAP (Lundberg & Lee 2017), and the "explainable AI" (XAI) literature in HCI.
- **Computer vision interpretability**: feature visualization (Olah et al. 2017–2020), the "circuits" thread starting at OpenAI (Olah, Cammarata) and continuing at Anthropic.
- **Mechanistic interpretability**: the contemporary research programme aiming to fully reverse-engineer neural network computations, formalized in Elhage et al.'s "Mathematical Framework for Transformer Circuits" (2021).

coined-by:: [[Chris Olah]] (for mechanistic interpretability as a programme)

## Core claim

Interpretability research divides along two axes:

### 1. What is being interpreted?

- **Behavioral interpretability**: predicting and explaining model outputs given inputs, without claims about internal mechanism. Includes probing, evals, attribution methods.
- **Mechanistic interpretability**: reverse-engineering the computation. Identifying features (directions in activation space), circuits (subgraphs of model computation implementing specific functions), and the relationships between them.

### 2. What is the goal?

- **Local interpretability**: explaining a specific model decision.
- **Global interpretability**: characterizing the model's overall computation.
- **Safety-oriented interpretability**: detecting deceptive alignment, identifying dangerous capabilities, verifying value-learning.

## Variants and refinements

### Key technical concepts (mechanistic side)

- **Features**: directions in activation space corresponding to interpretable concepts (e.g., a feature firing on "Golden Gate Bridge").
- **Superposition**: the phenomenon in which networks represent more features than they have dimensions, by encoding features in non-orthogonal directions. Articulated formally in Elhage et al. "Toy Models of Superposition" (2022).
- **Sparse Autoencoders (SAEs)**: technique for decomposing model activations into sparse, monosemantic features. Demonstrated at scale by Anthropic's "Scaling Monosemanticity" (2024), extracting millions of interpretable features from Claude 3 Sonnet.
- **Circuits**: subgraphs of computation implementing specific functions. The "circuits thread" at OpenAI / Anthropic has identified circuits for tasks like induction (in-context copying), indirect object identification, and bracket matching.
- **Activation patching / causal interpretability**: intervening on activations to test causal hypotheses about which components produce which behaviors.

defined-by:: [[Toy Models of Superposition 2022]]
extends:: [[Scaling Monosemanticity 2024]]

### Institutional landscape

- **Anthropic interpretability team** (Olah et al.): mechanistic interpretability at scale, transformer-circuits.pub.
- **DeepMind interpretability**: includes activation patching frameworks (Nanda, Conmy).
- **Apollo Research**: behavioral interpretability and scheming evaluations.
- **Conjecture / Redwood Research**: shorter-term interpretability + alignment-relevant tooling.
- **Academic groups**: Berkeley CHAI, MIT, Cambridge.

## Evidence and progress

- Identified circuits implementing specific transformer behaviors (induction heads, copying, factual recall via name-mover heads).
- Sparse autoencoders scaled from toy models (2022) to Claude 3 Sonnet (2024), extracting on the order of millions of features.
- Causal interventions demonstrated for many model behaviors.
- Open question: whether progress scales with capability — i.e., whether interpretability of frontier models keeps pace with their growth.

## Critiques

- *Tractability*: interpretability has been described as "perpetually almost-solved." Skeptics argue full mechanistic understanding of large models may be infeasible.
- *Safety relevance*: critics ask whether interpretability findings actually predict downstream safety failures.
- *Scaling*: each generation of capability adds parameters faster than interpretability tools scale.
- *Distraction risk*: some argue interpretability research provides safety theatre — performance of understanding without actually catching dangerous models.

criticized-by:: [[Stephen Casper]] (in part — "Black-Box Access is Insufficient...")

## Open questions

- Can interpretability detect deceptive alignment before deployment?
- Is full mechanistic decomposition possible for frontier models, or only partial interpretability of specific circuits?
- What is the relationship between mechanistic interpretability and behavioral / evals-based safety assurance?
- Does superposition impose fundamental limits on interpretability?

## Relationships

extends:: [[AI Safety]]
prerequisite-of:: [[Verified Alignment]]
applies-to:: [[Deceptive Alignment]]
applies-to:: [[Frontier Model Evaluation]]
related:: [[Sparse Autoencoders]]
related:: [[Superposition]]
related:: [[Activation Patching]]
