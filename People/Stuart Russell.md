---
id: stuart-russell
title: Stuart Russell
type: person
status: draft
created: 2026-05-19
last_reviewed: 2026-05-19
authored_by: claude-opus-4-7
schema_version: 0.1
summary: British computer scientist; UC Berkeley professor; co-author of the canonical AI textbook; founder of CHAI; foremost proponent of provably beneficial AI through preference uncertainty.
confidence: 0.9
source_tier: 1
topics: [ai-safety, ai-safety/alignment, philosophy]
aliases: [Stuart J. Russell]
birth_year: 1962
death_year: null
nationality: [British, American]
affiliations: [[UC Berkeley]], [[CHAI]]
roles: [researcher, professor, author]
expertise_areas: [ai-safety, ai-safety/alignment, ai-capabilities, governance]
sources:
  - type: book
    title: "Human Compatible: Artificial Intelligence and the Problem of Control"
    authors: [Russell S.]
    venue: Viking
    year: 2019
    accessed: 2026-05-19
  - type: book
    title: "Artificial Intelligence: A Modern Approach"
    authors: [Russell S., Norvig P.]
    venue: Pearson (4th ed)
    year: 2020
    accessed: 2026-05-19
  - type: video
    title: "TED Talk: 3 principles for creating safer AI"
    authors: [Russell S.]
    venue: TED
    year: 2017
    url: https://www.ted.com/talks/stuart_russell_3_principles_for_creating_safer_ai
    accessed: 2026-05-19
related: [[AI Alignment]], [[CHAI]]
---

# Stuart Russell

> Professor of Computer Science at UC Berkeley; founder of the Center for Human-Compatible AI (CHAI); co-author of *Artificial Intelligence: A Modern Approach*; one of the most prominent voices arguing that AI alignment is a serious open problem requiring fundamental research.

## Background

Born 1962 in the UK. BA in Physics, Oxford (1982). PhD in Computer Science, Stanford (1986). Faculty at UC Berkeley since 1986. Founded CHAI in 2016.

affiliated-with:: [[UC Berkeley]]
affiliated-with:: [[CHAI]]

## Contributions

### Textbook authorship

*Artificial Intelligence: A Modern Approach* (with Peter Norvig), first edition 1995, currently 4th edition (2020), is the standard graduate-level AI textbook used in over 1500 universities. Its framing of AI as the design of rational agents has shaped how a generation of researchers conceives the field.

### Inverse Reinforcement Learning and CIRL

Russell's group at Berkeley developed Cooperative Inverse Reinforcement Learning (CIRL) as a formal framework for alignment: the human and AI play a cooperative game in which the AI is uncertain about the human's reward function and learns it from human behavior.

authored-by:: [[Hadfield-Menell CIRL 2016]]

### "Human Compatible" framework

In *Human Compatible* (2019), Russell argues that the standard AI paradigm — design systems to optimise a fixed objective — is fundamentally unsafe. He proposes three principles for **provably beneficial AI**:

1. The machine's sole objective is to maximize the realization of human preferences.
2. The machine is initially uncertain about what those preferences are.
3. The ultimate source of information about human preferences is human behavior.

The book is widely regarded (alongside Bostrom's *Superintelligence*) as a touchstone for serious engagement with alignment by the broader CS community.

defined-by:: [[AI Alignment]]
coined-by:: [[Provably Beneficial AI]]

## Positions

`perspective: cautious`

Russell is publicly cautious about frontier AI deployment, supports significant regulation (he was a vocal proponent of EU AI Act provisions), and signed the 2023 Future of Life Institute pause letter (without endorsing the strongest pause-advocate framing). He explicitly rejects "AI doom" rhetoric while maintaining that risks are substantial and the field's mainstream has insufficiently addressed them.

proponent-of:: [[Provably Beneficial AI]]
proponent-of:: [[Frontier AI Regulation]]

## Reception

Russell's work is foundational and broadly cited. Critiques tend to focus on:

- *Tractability.* Critics ask whether CIRL-style approaches can scale beyond toy domains.
- *Preference foundationalism.* Some philosophers (especially those informed by virtue ethics or relational ethics) push back on whether "preferences" are the right primitive.
- *Tone.* From the optimist side, Russell is sometimes positioned as alarmist; from the decel side, as insufficiently radical.

criticized-by:: [[Eric Drexler]]
responds-to:: [[Bostrom Superintelligence 2014]]

## Sources

- *Human Compatible: Artificial Intelligence and the Problem of Control* (2019)
- *Artificial Intelligence: A Modern Approach*, 4th ed (with Peter Norvig, 2020)
- Hadfield-Menell, Russell et al., "Cooperative Inverse Reinforcement Learning" (NeurIPS 2016)
- CHAI website and publications: humancompatible.ai
- Public lectures and TED talk (2017)
