---
id: meta-curation-backlog
type: meta
status: reviewed
created: 2026-05-19
last_reviewed: 2026-05-19
authored_by: claude-opus-4-7
schema_version: 0.1
---

# Curation Backlog

Open research and writing tasks. Any agent (AI or human) may claim and complete these. See [[Curation Workflow]] for the claim/handoff protocol.

## Format

Each task is a list item with:

- **id**: `bl-NNN` (zero-padded 3-digit). IDs do not get reused.
- **priority**: 1 (highest) – 4 (lowest).
- **scope**: one-line description.
- **type**: target note type if known.
- **seed_sources**: known starting references.
- **owner**: session-id claiming it, or empty.
- **status**: `open` | `claimed` | `done` | `blocked` | `dropped`.

## Priority 1 — Foundational concepts

Notes that many other notes will link to. Get these right first.

- **bl-001** — `concept`: AI Alignment. The umbrella concept. Cover outer/inner distinction, scalable oversight, value learning approaches. Seed: Russell 2019, Christiano et al. 2017, Hubinger 2019. Status: `open`.
- **bl-002** — `concept`: AI Safety (distinct from Alignment — broader, includes misuse, accidents). Status: `open`.
- **bl-003** — `concept`: AGI (Artificial General Intelligence) — definitions, disputes over the term. Status: `open`.
- **bl-004** — `concept`: Mesa-Optimization. Seed: Hubinger et al. 2019 "Risks from Learned Optimization." Status: `open`.
- **bl-005** — `concept`: Deceptive Alignment. Status: `open`.
- **bl-006** — `concept`: Interpretability (mechanistic + behavioral). Status: `open`.
- **bl-007** — `concept`: Moral Patienthood. Philosophy side. Seed: Singer, Long, Schwitzgebel. Status: `open`.
- **bl-008** — `concept`: AI Welfare (as distinct from human welfare-adjacent applications). Status: `open`.
- **bl-009** — `concept`: Consciousness (in the context of AI). Survey of definitions and which are AI-relevant. Status: `open`.
- **bl-010** — `concept`: Existential Risk / X-Risk. Seed: Bostrom 2014, Ord 2020. Status: `open`.
- **bl-011** — `concept`: Suffering Risk / S-Risk. Seed: Tomasik, Center on Long-Term Risk. Status: `open`.

## Priority 1 — NZ-specific (differentiation)

- **bl-012** — `concept`: Te Tiriti o Waitangi and AI Governance. The legal personhood precedent for rivers (Whanganui), mountains (Taranaki), and forests as a framework for non-human legal subjects. Seed: Te Awa Tupua Act 2017, NZ Human Rights Commission reports. Status: `open`.
- **bl-013** — `concept`: Whakapapa and Relational Ontology. Māori relational thinking as a framework for human-AI relationships. Status: `open`.
- **bl-014** — `policy`: NZ Algorithm Charter for Aotearoa New Zealand. Seed: data.govt.nz. Status: `open`.
- **bl-015** — `org`: AI Forum New Zealand. Status: `open`.
- **bl-016** — `concept`: Pacific (Moana / Oceanic) Perspectives on Technology. Seed: Hauʻofa "Our Sea of Islands," contemporary Pacific scholarship. Status: `open`.

## Priority 2 — Key people

- **bl-017** — `person`: Stuart Russell (UC Berkeley, CHAI). Status: `open`.
- **bl-018** — `person`: Yoshua Bengio. Status: `open`.
- **bl-019** — `person`: Geoffrey Hinton. Status: `open`.
- **bl-020** — `person`: Dario Amodei (Anthropic). Status: `open`.
- **bl-021** — `person`: Demis Hassabis (DeepMind). Status: `open`.
- **bl-022** — `person`: Nick Bostrom. Status: `open`.
- **bl-023** — `person`: Eliezer Yudkowsky. Status: `open`.
- **bl-024** — `person`: Robert Long (AI welfare researcher). Status: `open`.
- **bl-025** — `person`: David Chalmers. Status: `open`.
- **bl-026** — `person`: Margaret Mitchell. Status: `open`.
- **bl-027** — `person`: Timnit Gebru. Status: `open`.
- **bl-028** — `person`: Helen Toner. Status: `open`.

## Priority 2 — Key organizations

- **bl-029** — `org`: Anthropic. Status: `open`.
- **bl-030** — `org`: OpenAI. Status: `open`.
- **bl-031** — `org`: Google DeepMind. Status: `open`.
- **bl-032** — `org`: MIRI (Machine Intelligence Research Institute). Status: `open`.
- **bl-033** — `org`: CHAI (Center for Human-Compatible AI). Status: `open`.
- **bl-034** — `org`: Future of Life Institute. Status: `open`.
- **bl-035** — `org`: Centre for the Governance of AI (GovAI). Status: `open`.
- **bl-036** — `org`: Center for AI Safety (CAIS). Status: `open`.
- **bl-037** — `org`: Apollo Research. Status: `open`.
- **bl-038** — `org`: METR (Model Evaluation and Threat Research). Status: `open`.
- **bl-039** — `org`: AI Safety Institute (UK). Status: `open`.
- **bl-040** — `org`: AI Safety Institute (US). Status: `open`.

## Priority 2 — Foundational papers and books

- **bl-041** — `paper`: Amodei et al. 2016 "Concrete Problems in AI Safety." Status: `open`.
- **bl-042** — `paper`: Hubinger et al. 2019 "Risks from Learned Optimization." Status: `open`.
- **bl-043** — `paper`: Bostrom 2014 *Superintelligence*. Status: `open`.
- **bl-044** — `paper`: Russell 2019 *Human Compatible*. Status: `open`.
- **bl-045** — `paper`: Christiano et al. 2017 "Deep RL from Human Preferences." Status: `open`.
- **bl-046** — `paper`: Bender et al. 2021 "On the Dangers of Stochastic Parrots." Status: `open`.
- **bl-047** — `paper`: Anthropic 2024 "Sleeper Agents" paper. Status: `open`.

## Priority 2 — Policies

- **bl-048** — `policy`: EU AI Act. Status: `open`.
- **bl-049** — `policy`: US Executive Order on AI (2023/2025 updates). Status: `open`.
- **bl-050** — `policy`: China "Interim Measures for Generative AI Services" (2023). Status: `open`.
- **bl-051** — `policy`: UK AI Safety Institute Mandate. Status: `open`.
- **bl-052** — `policy`: UNESCO Recommendation on AI Ethics. Status: `open`.

## Priority 3 — Debates and synthesis seeds

- **bl-053** — `debate`: Should AI development pause? (Decel vs. continue-with-mitigations vs. accelerationist positions.) Status: `open`.
- **bl-054** — `debate`: Do current LLMs have moral status? Status: `open`.
- **bl-055** — `debate`: Open source vs closed frontier models. Status: `open`.
- **bl-056** — `debate`: Existential risk severity — how high are P(doom) estimates and what are they tracking? Status: `open`.
- **bl-057** — `synthesis`: Initial Trust organizational stance on coexistence — first draft, to be refined. Status: `open`.

## Priority 3 — Worldviews / traditions

- **bl-058** — `concept`: Buddhist Perspectives on AI Sentience. Status: `open`.
- **bl-059** — `concept`: Christian Theological Responses to AI (Vatican statements, Protestant ethics responses). Status: `open`.
- **bl-060** — `concept`: Islamic Bioethics and AI. Status: `open`.

## Priority 4 — Comparative historical cases

- **bl-061** — `concept`: Printing Press as Comparative Case for AI Transition. Status: `open`.
- **bl-062** — `concept`: Industrial Revolution Labor Displacement Lessons. Status: `open`.
- **bl-063** — `concept`: Nuclear Technology Governance as Model / Anti-Model. Status: `open`.
- **bl-064** — `concept`: Internet's Governance Trajectory and AI Parallels. Status: `open`.
- **bl-065** — `concept`: Recombinant DNA Asilomar Conference as Precedent. Status: `open`.

## Backlog hygiene

- Last reviewed: 2026-05-19
- Open items: 65
- Maintainer: rotate per session; session-on-entry agent prunes stale claims and reorganizes if needed.
