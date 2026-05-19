---
id: mechanistic-interpretability
title: Mechanistic Interpretability
type: concept
status: draft
created: 2026-05-20
last_reviewed: 2026-05-20
authored_by: claude-opus-4-7
schema_version: 0.1
summary: A research programme aiming to reverse-engineer neural-network computations into human-understandable algorithms — identifying features, circuits, and their causal relationships rather than only relating inputs to outputs.
confidence: 0.9
source_tier: 1
topics: [ai-safety/interpretability/mechanistic, ai-safety/interpretability, ai-safety]
perspective: neutral
aliases: [mech interp, mechanistic interp]
sources:
  - type: expert-blog
    title: "Zoom In: An Introduction to Circuits"
    authors: [Olah C., Cammarata N., Schubert L., Goh G., Petrov M., Carter S.]
    venue: Distill
    year: 2020
    url: https://distill.pub/2020/circuits/zoom-in/
    accessed: 2026-05-20
  - type: preprint
    title: "A Mathematical Framework for Transformer Circuits"
    authors: [Elhage N., Nanda N., Olsson C., et al.]
    venue: Anthropic
    year: 2021
    url: https://transformer-circuits.pub/2021/framework/
    accessed: 2026-05-20
related: [[Interpretability]], [[Chris Olah]], [[Superposition]], [[Sparse Autoencoders]]
---

# Mechanistic Interpretability

> Reverse-engineer the internal computations of neural networks into human-understandable algorithms — identifying *features* (interpretable directions in activation space), *circuits* (subgraphs of computation implementing specific functions), and their causal relationships.

## Origin

The mechanistic interpretability research programme was articulated by Chris Olah and collaborators across OpenAI (2017–2020, the "circuits thread" on Distill) and Anthropic (2021–present, transformer-circuits.pub). Predecessors include feature-visualization work (Olah et al. 2017), neural network polytope analyses, and earlier vision-model interpretability research.

coined-by:: [[Chris Olah]]
defined-by:: [[Olah Circuits Zoom-In 2020]]

## Core claim

Mechanistic interpretability rests on three commitments:

1. **Neural networks compute interpretable algorithms** — they are not black boxes in principle, only in current understanding.
2. **The right abstractions can recover these algorithms** — *features* and *circuits* are the proposed unit of analysis (analogous to gates and circuits in classical computing).
3. **Reverse-engineering should be causal, not just correlational** — interventions on internal activations should produce predictable changes in outputs, demonstrating mechanism.

This contrasts with *behavioral interpretability* (predicting model behavior from inputs without claiming internal mechanism) and with simpler *attribution* approaches (e.g., gradient-based saliency).

## Key concepts

- **Feature**: a direction in activation space corresponding to an interpretable concept (e.g., "Golden Gate Bridge," "code in Python," "uncertainty").
- **Circuit**: a subgraph of model computation implementing a specific function (e.g., induction heads doing in-context copying; name-mover heads doing indirect object identification).
- **Superposition**: networks representing more features than they have dimensions, by encoding features in non-orthogonal directions. See [[Superposition]].
- **Polysemantic / monosemantic**: neurons responding to multiple unrelated concepts (polysemantic) vs. a single concept (monosemantic). Superposition tends to produce polysemantic neurons.
- **Sparse autoencoders (SAEs)**: technique for decomposing polysemantic activations into a larger basis of monosemantic features. See [[Sparse Autoencoders]].
- **Activation patching / causal interventions**: replacing internal activations to test which components causally produce which behaviors.

defined-by:: [[Superposition]]
defined-by:: [[Sparse Autoencoders]]

## Progress and milestones

- **Vision circuits** (Olah et al. 2020): identified curve detectors, dog-head detectors, etc. with causal interventions.
- **Transformer Mathematical Framework** (Elhage et al. 2021): formal decomposition of transformer computation.
- **Induction Heads** (Olsson et al. 2022): identified a circuit responsible for in-context learning behavior.
- **IOI Circuit** (Wang et al. 2022): mapped circuit for indirect-object identification in GPT-2.
- **Toy Models of Superposition** (Elhage et al. 2022): formalized superposition phenomenon.
- **Scaling Monosemanticity** (Templeton et al. 2024): SAEs scaled to Claude 3 Sonnet, extracting millions of interpretable features.
- **Function vectors** (Hendel et al. 2023, Todd et al. 2023): single activation directions encoding entire tasks.

## Institutional landscape

- **Anthropic interpretability team** (Olah et al.) — leading programme; transformer-circuits.pub.
- **Google DeepMind** — Nanda, Conmy; mechanistic interpretability papers on Gemma.
- **Apollo Research** — interpretability for deception evaluations.
- **Academic groups** — MIT, Berkeley, Cambridge, EleutherAI Pythia analyses.
- **Conjecture / Redwood Research** — shorter-term alignment-relevant tooling.

## Critiques

- **Tractability ceiling**: skeptics argue full mechanistic understanding of frontier models may be infeasible.
- **Scaling lag**: each generation of capability adds parameters faster than interpretability tools scale.
- **Safety relevance gap**: identifying circuits doesn't automatically predict downstream safety failures.
- **Distraction risk**: interpretability findings may provide safety theatre — performance of understanding without actually catching dangerous models.

criticized-by:: [[Stephen Casper]] ("Black-Box Access is Insufficient...")

## Open questions

- Can mech interp catch [[Deceptive Alignment]] before deployment?
- Is full mechanistic decomposition possible at frontier scale, or only partial circuit analysis?
- What's the relationship between SAE features and human-meaningful concepts — do SAEs find the "right" features or artifacts of the autoencoder?
- Does training affect interpretability (e.g., do RLHF-trained models develop circuits unique to that training)?

## Relationships

instance-of:: [[Interpretability]]
defined-by:: [[Olah Circuits Zoom-In 2020]]
extends:: [[Superposition]]
extends:: [[Sparse Autoencoders]]
applies-to:: [[Deceptive Alignment]]
applies-to:: [[Frontier Model Evaluation]]
related:: [[Activation Patching]]
