---
id: sparse-autoencoders
title: Sparse Autoencoders (in mechanistic interpretability)
type: concept
status: draft
created: 2026-05-20
last_reviewed: 2026-05-20
authored_by: claude-opus-4-7
schema_version: 0.1
summary: A technique for decomposing neural-network activations into a larger basis of sparsely-activating, individually-interpretable features — the dominant tool for handling superposition at scale.
confidence: 0.85
source_tier: 1
topics: [ai-safety/interpretability/mechanistic, ai-safety/interpretability]
perspective: neutral
aliases: [SAE, sparse autoencoder, sparse coding, sparse dictionary learning]
sources:
  - type: preprint
    title: "Towards Monosemanticity: Decomposing Language Models With Dictionary Learning"
    authors: [Bricken T., Templeton A., Batson J., et al.]
    venue: Anthropic
    year: 2023
    url: https://transformer-circuits.pub/2023/monosemantic-features/
    accessed: 2026-05-20
  - type: preprint
    title: "Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet"
    authors: [Templeton A., Conerly T., Marcus J., et al.]
    venue: Anthropic
    year: 2024
    url: https://transformer-circuits.pub/2024/scaling-monosemanticity/
    accessed: 2026-05-20
  - type: preprint
    title: "Sparse Autoencoders Find Highly Interpretable Features in Language Models"
    authors: [Cunningham H., Ewart A., Riggs L., Huben R., Sharkey L.]
    venue: arXiv
    year: 2023
    arxiv_id: 2309.08600
    accessed: 2026-05-20
related: [[Mechanistic Interpretability]], [[Superposition]]
---

# Sparse Autoencoders

> An autoencoder trained with a sparsity penalty whose hidden layer has *more* dimensions than the input — used to decompose neural-network activations into a basis of individually-interpretable, sparsely-activating features.

## Origin

Sparse coding has a long history in computational neuroscience and classical ML. Its application to large-language-model interpretability was developed in 2023 in parallel by Anthropic (Bricken et al. "Towards Monosemanticity," 2023) and Cunningham et al. (independent 2023 paper). Scaled to frontier models in Anthropic's 2024 "Scaling Monosemanticity" work on Claude 3 Sonnet.

defined-by:: [[Anthropic Towards Monosemanticity 2023]]
extended-by:: [[Templeton Scaling Monosemanticity 2024]]

## Core claim

Given an activation vector $x \in \mathbb{R}^d$ from inside a neural network:

1. Train an autoencoder $f(g(x)) \approx x$ where the hidden representation $g(x) \in \mathbb{R}^D$ has $D \gg d$ dimensions.
2. Impose a sparsity penalty (typically L1 on $g(x)$) — most hidden units inactive at any time.
3. The learned basis vectors (columns of $f$) correspond to interpretable features; the sparse activation pattern says which features are present in a given input.

The expanded basis lets SAEs recover features the network is encoding in superposition — features that are non-orthogonal in the original $d$-dimensional space but orthogonal-ish in the expanded $D$-dimensional one.

extends:: [[Superposition]]

## Variants and refinements

- **L1-penalty SAEs**: original formulation; suffers from "shrinkage" (features pulled toward zero).
- **Gated SAEs** (Rajamanoharan et al. 2024, DeepMind): separate magnitude and gating decisions; better fidelity.
- **TopK SAEs** (Gao et al. 2024, OpenAI): hard-thresholded sparsity instead of L1.
- **JumpReLU SAEs**: another sparsity formulation.
- **Crosscoders / Transcoders**: variants that operate across layers or across models.

## Evidence

- Anthropic's "Scaling Monosemanticity" (2024) extracted millions of features from Claude 3 Sonnet — many human-interpretable upon manual inspection, with associated activations and example contexts.
- Features have been identified for concrete concepts ("Golden Gate Bridge," "code in Python"), abstract concepts ("uncertainty," "deception"), and behaviors ("sycophancy," "refusal").
- Causal interventions (clamping a feature ON or OFF) produce predictable changes in model outputs — demonstrating the features are causally implicated, not merely correlational labels.

## Critiques

- **Decomposition non-uniqueness**: an SAE finds *a* monosemantic decomposition; that may not be *the* basis the network is using internally.
- **Feature labelling cost**: identifying millions of features manually is infeasible; automated labelling (using LLMs to interpret each feature's activations) introduces another layer of indirection.
- **Reconstruction fidelity gap**: SAEs trade reconstruction loss for interpretability — the "clean" features may not capture everything the original activations contained.
- **Scaling cost**: training SAEs on frontier models requires substantial compute.
- **Dependence on observed features**: SAEs find features in the training distribution; they may miss features that activate only on rare or adversarial inputs.

## Open questions

- What's the relationship between SAE-discovered features and the "true" features the network uses? Are SAEs finding ground truth or useful approximations?
- Can SAEs scale to identify safety-relevant features (deception, mesa-optimization signatures) reliably?
- How should SAE outputs be aggregated for safety-relevant decisions — feature-by-feature monitoring at deployment?

## Relationships

instance-of:: [[Mechanistic Interpretability]]
extends:: [[Superposition]]
defined-by:: [[Anthropic Towards Monosemanticity 2023]]
applies-to:: [[Deceptive Alignment]]
applies-to:: [[Frontier Model Evaluation]]
