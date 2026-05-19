---
id: superposition
title: Superposition (in neural networks)
type: concept
status: draft
created: 2026-05-20
last_reviewed: 2026-05-20
authored_by: claude-opus-4-7
schema_version: 0.1
summary: The phenomenon in which neural networks represent more distinct features than they have dimensions by encoding features in non-orthogonal directions — producing polysemantic neurons and complicating interpretability.
confidence: 0.85
source_tier: 1
topics: [ai-safety/interpretability/mechanistic, ai-safety/interpretability]
perspective: neutral
aliases: [feature superposition, polysemantic neurons]
sources:
  - type: preprint
    title: "Toy Models of Superposition"
    authors: [Elhage N., Hume T., Olsson C., et al.]
    venue: Anthropic
    year: 2022
    arxiv_id: 2209.10652
    url: https://transformer-circuits.pub/2022/toy_model/
    accessed: 2026-05-20
  - type: expert-blog
    title: "Privileged Bases in the Transformer Residual Stream"
    authors: [Elhage N., et al.]
    venue: Anthropic
    year: 2023
    accessed: 2026-05-20
related: [[Mechanistic Interpretability]], [[Sparse Autoencoders]]
---

# Superposition

> Neural networks routinely represent more distinct features than they have dimensions, by encoding features in non-orthogonal (overlapping) directions. The mechanism explains polysemantic neurons and motivates Sparse Autoencoders.

## Origin

The phenomenon was observed earlier in connectionist literature, but formalized for contemporary deep learning by Elhage et al. (2022) "Toy Models of Superposition" at Anthropic. The paper trains a small synthetic model with explicit feature ground-truth and shows that under sparsity assumptions, networks reliably learn to compress more features than dimensions allow.

defined-by:: [[Elhage Toy Models of Superposition 2022]]
coined-by:: [[Chris Olah]] (programme-level)

## Core claim

If feature inputs are sufficiently sparse (only a few features active at a time), a network with $d$ dimensions can usefully represent more than $d$ features by:

1. Choosing feature directions to be near-orthogonal but not perfectly orthogonal.
2. Accepting some "interference noise" when multiple features are simultaneously active.
3. Trading off representation capacity vs. interference, with sparsity in input distribution determining the optimal trade-off.

The result is that individual neurons (basis directions) often correspond to mixtures of features rather than single concepts — "polysemantic" neurons. This makes naïve circuit analysis (one neuron = one concept) misleading.

## Implications

- **For interpretability**: cannot interpret a polysemantic neuron as encoding a single concept. Must decompose into a feature basis that may be larger than the neuron basis. See [[Sparse Autoencoders]].
- **For capability**: superposition may be central to how networks fit large vocabularies of concepts into limited parameter counts.
- **For safety evaluations**: behavioral probes targeting "one neuron = one concept" fail when superposition holds.

extends:: [[Mechanistic Interpretability]]

## Variants and refinements

- **Toy superposition**: synthetic settings (Elhage 2022) where the truth is known.
- **Empirical superposition**: observed in real models including Pythia, GPT-2, Claude, Llama families.
- **Privileged-basis vs. non-privileged-basis** distinction (Elhage et al. 2023): in some transformer components (residual stream), no canonical basis is preferred and features are encoded in arbitrary directions; in others (per-MLP nonlinearities), the basis is privileged by the architecture.

## Evidence

- The 2022 toy-models paper provides ground-truth controlled experiments.
- Sparse autoencoders applied to frontier models (Templeton et al. 2024 — Claude 3 Sonnet) recover millions of monosemantic features, supporting the superposition hypothesis.
- Cross-model studies (Pythia, GPT-2 small) consistently show polysemantic neurons that decompose via SAE into more interpretable bases.

## Critiques

- **Decomposition uniqueness**: SAEs find *a* monosemantic basis; it's not provably *the* basis the network is using.
- **Scaling**: as models grow, the number of features may grow faster than SAE training can capture cleanly.
- **Interpretation labour**: even after decomposition, labelling millions of features is expensive (Anthropic uses LLMs to auto-label, with verification).

## Open questions

- What determines optimal sparsity / capacity trade-off in real training distributions?
- Are there architectures (e.g., explicitly sparse activations) that avoid superposition and ease interpretability without capability cost?
- Is the "feature" the right unit of analysis, or are interpretable units more like trajectories / programs?

## Relationships

instance-of:: [[Mechanistic Interpretability]]
defined-by:: [[Elhage Toy Models of Superposition 2022]]
prerequisite-of:: [[Sparse Autoencoders]]
applies-to:: [[Frontier Model Interpretability]]
