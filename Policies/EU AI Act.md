---
id: eu-ai-act
title: EU AI Act
type: policy
status: draft
created: 2026-05-20
last_reviewed: 2026-05-20
authored_by: claude-opus-4-7
schema_version: 0.1
summary: European Union regulation on artificial intelligence, the world's first comprehensive horizontal AI law; entered into force August 2024 with phased application through 2026 and beyond.
confidence: 0.9
source_tier: 1
topics: [governance, governance/global, region/eu, ai-ethics, ai-safety/evaluation]
aliases: [Artificial Intelligence Act, Regulation (EU) 2024/1689]
jurisdiction: EU
policy_status: enacted
effective_date: 2024-08-01
authority: European Parliament and Council
sources:
  - type: government-document
    title: "Regulation (EU) 2024/1689 of the European Parliament and of the Council laying down harmonised rules on artificial intelligence (Artificial Intelligence Act)"
    venue: Official Journal of the European Union
    year: 2024
    url: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
    accessed: 2026-05-20
related: [[AI Governance]], [[Risk-Based AI Regulation]]
---

# EU AI Act

> The first comprehensive horizontal AI regulation worldwide. Classifies AI systems by risk tier and applies graduated obligations.

## Jurisdiction and authority

Applies in the European Union and to providers placing AI systems on the EU market regardless of where they are established. Adopted by the European Parliament and Council; enforced by national supervisory authorities and the European AI Office (within the Commission).

## Status and timeline

- **April 2021**: Initial European Commission proposal.
- **December 2023**: Political agreement (trilogue).
- **March 2024**: European Parliament formal adoption.
- **July 2024**: Council of the EU formal adoption.
- **August 2024**: Entered into force (Regulation 2024/1689).
- **Phased application**:
  - February 2025: Prohibitions on unacceptable-risk practices in force.
  - August 2025: Obligations for general-purpose AI (GPAI) models in force.
  - August 2026: Most other obligations (high-risk systems) in force.
  - August 2027: Full application including embedded high-risk products.

policy_status: enacted

## Substantive provisions

### Risk tiers

The Act sorts AI systems into four categories:

1. **Unacceptable risk** — prohibited. Includes: social scoring by public authorities, real-time remote biometric ID in public spaces (with exceptions), manipulative or exploitative systems, emotion recognition in workplace/education (with exceptions), untargeted scraping of facial images.
2. **High-risk** — permitted with extensive obligations. Includes: AI in critical infrastructure, education, employment, essential services, law enforcement, migration, justice, democratic processes. Obligations: risk management, data governance, technical documentation, logging, transparency, human oversight, accuracy/robustness/cybersecurity, conformity assessment.
3. **Limited risk** — transparency obligations (e.g., labeling deepfakes, disclosing chatbot interactions).
4. **Minimal risk** — no specific obligations.

### General-Purpose AI (GPAI) models

The Act has a separate regime for general-purpose AI models (Articles 51–55), with stricter obligations for "GPAI models with systemic risk" — defined initially as those trained with > 10^25 FLOPs. Obligations include transparency about training data, copyright compliance, technical documentation, and (for systemic-risk models) model evaluation, adversarial testing, incident reporting, and cybersecurity.

governs:: [[General-Purpose AI Models]]
governs:: [[High-Risk AI Systems]]

### Enforcement

National competent authorities supervise; the AI Office coordinates GPAI oversight. Penalties up to €35 million or 7% of worldwide annual turnover for prohibited-practice breaches.

## Reception

- *Industry*: Mixed. Some welcomed regulatory certainty; many flagged compliance burden, particularly for SMEs and open-source developers. Open-source provisions narrowed late in negotiation but remain debated.
- *Civil society*: Largely supportive, though some advocates (EDRi, AlgorithmWatch) wanted stronger biometric prohibitions and tighter law-enforcement exceptions.
- *Researchers / academics*: Concerns about the speed of evolving GPAI obligations and the practicality of evaluation requirements for frontier models.
- *External jurisdictions*: Watched closely as a possible template; "Brussels effect" anticipated though not certain.

## Related instruments

extends:: [[GDPR]]
related:: [[EU Digital Services Act]]
related:: [[Product Liability Directive]]
related:: [[AI Liability Directive Proposal]]

## Sources

- Official text: Regulation (EU) 2024/1689 (OJ L, 12 July 2024).
- European AI Office: digital-strategy.ec.europa.eu/en/policies/ai-office
- Future of Life Institute summary: artificialintelligenceact.eu
- Numerous legal analyses (Bradford "The Brussels Effect" frame; CEPS commentary; Hogan Lovells / Latham & Watkins industry briefings).
