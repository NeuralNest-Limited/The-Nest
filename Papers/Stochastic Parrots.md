---
id: bender-stochastic-parrots-2021
title: "On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?"
type: paper
status: draft
created: 2026-05-20
last_reviewed: 2026-05-20
authored_by: claude-opus-4-7
schema_version: 0.1
summary: 2021 FAccT paper critiquing large language models on environmental, social, financial, and epistemological grounds; the proximate cause of Google's firing of co-authors Gebru and Mitchell.
confidence: 0.95
source_tier: 1
topics: [ai-ethics, ai-ethics/bias, ai-ethics/transparency, society/labor]
authors: [Bender E.M., Gebru T., McMillan-Major A., Mitchell M.]
venue: FAccT
year: 2021
doi: 10.1145/3442188.3445922
arxiv_id: null
url: null
sources:
  - type: peer-reviewed-paper
    title: "On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?"
    authors: [Bender E.M., Gebru T., McMillan-Major A., Mitchell M.]
    venue: ACM FAccT
    year: 2021
    doi: 10.1145/3442188.3445922
    accessed: 2026-05-20
related: [[Timnit Gebru]], [[Margaret Mitchell]], [[Emily Bender]]
---

# On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?

> The 2021 FAccT paper that articulated systemic critiques of large language models — environmental costs, training-data biases, false fluency, displacement of more impactful research — and whose internal Google review controversy led to the firings of Gebru and Mitchell.

## Authors and venue

authored-by:: [[Emily Bender]]
authored-by:: [[Timnit Gebru]]
authored-by:: [[Angelina McMillan-Major]]
authored-by:: [[Margaret Mitchell]]

Venue: ACM Conference on Fairness, Accountability, and Transparency (FAccT) 2021. The paper was initially submitted with two additional Google co-authors who were removed during Google's internal review process — a sequence of events that became central to the subsequent firings.

## Abstract / paraphrase

The paper raises concerns about large language models (LLMs) across four dimensions:

1. **Environmental and financial costs**: training large models consumes significant energy and water; benefits accrue to well-resourced organizations while costs are borne broadly.
2. **Massive datasets**: large web-scraped training corpora are difficult to audit, reproduce inequities, and may exclude marginalized voices.
3. **Research opportunity costs**: dominant-paradigm scale-up displaces attention from smaller, more accountable models and more diverse research directions.
4. **Stochastic parrots**: large language models that produce fluent text without understanding mislead users about the nature of model output and risk being treated as authoritative information sources.

## Key contributions

1. **Coining "stochastic parrots"** as a critical frame for LLM fluency: producing plausible text from statistical patterns without comprehension.
2. **Environmental impact analysis**: explicit cost framing.
3. **Bias analysis**: how training-data composition produces biased outputs and amplifies marginalization.
4. **Methodological critique**: bigger-is-better as paradigm vs. accountable, documented, smaller systems.

coined-by:: [[Stochastic Parrots]]

## Method

Critical synthesis paper. Reviews prior literature on each of the four concern areas, articulates the connections, and makes recommendations (data documentation, environmental reporting, research-direction diversification).

## Findings

Conclusions (selected):

- Costs of LLM training and deployment are inequitably distributed.
- Bias in training data produces measurable downstream harm; debiasing techniques are incomplete.
- Fluent-text generation creates new categories of misuse and misperception.
- The research community should diversify investments beyond scale-up.

## Reception

The paper itself is widely cited and influential within FAccT and adjacent communities. But the more significant fact about the paper is its controversy:

- Google's internal review process objected to portions of the paper.
- Timnit Gebru, a co-author and Google employee, was fired in December 2020 after disputes about the review.
- Margaret Mitchell, also a co-author and Google employee, was fired in February 2021.
- The events catalyzed substantial industry-academia tensions; subsequent corporate AI ethics research has been viewed through this lens.

The paper became a touchstone in broader debates about:
- Corporate research independence.
- Censorship of researcher critique.
- Whether the FAccT framing or the safety / alignment framing should structure responses to AI risk.

criticized-by:: portions of the safety / alignment community for prioritization disagreements (rather than substantive disagreement with most documented concerns)

## Critiques

- *Within FAccT*: foundational and respected.
- *From mainstream ML*: many in capability research accepted environmental and bias concerns while disputing some characterizations of LLM cognition.
- *From safety / alignment*: cordial intellectual disagreement; safety / alignment frames emphasise different risks but rarely dispute the documented ones.
- *Methodological*: some critiques that the "stochastic parrots" framing under-states what current models do, though authors and others argue this characterization remains apt for the specific question of comprehension.

## Relevance to coexistence research

The paper articulates the FAccT-side framing of AI concerns — environmental costs, embedded power, labor exploitation, documentation. Coexistence research that ignores these dimensions risks reproducing the priorities-dispute the paper foregrounds.

## Sources

Bender E.M., Gebru T., McMillan-Major A., Mitchell M. (2021). "On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?" Proceedings of FAccT 2021.
