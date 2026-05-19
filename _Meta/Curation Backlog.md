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

- **bl-001** — `concept`: AI Alignment. Status: `done` (2026-05-19 → [[ai-alignment]]).
- **bl-002** — `concept`: AI Safety (distinct from Alignment — broader, includes misuse, accidents). Status: `done` (2026-05-20 → [[ai-safety]]).
- **bl-003** — `concept`: AGI (Artificial General Intelligence) — definitions, disputes over the term. Status: `done` (2026-05-20 → [[agi]]).
- **bl-004** — `concept`: Mesa-Optimization. Status: `done` (2026-05-19 → [[mesa-optimization]]).
- **bl-005** — `concept`: Deceptive Alignment. Status: `done` (2026-05-20 → [[deceptive-alignment]]).
- **bl-006** — `concept`: Interpretability (mechanistic + behavioral). Status: `done` (2026-05-20 → [[interpretability]]).
- **bl-007** — `concept`: Moral Patienthood. Status: `done` (2026-05-19 → [[moral-patienthood]]).
- **bl-008** — `concept`: AI Welfare. Status: `done` (2026-05-19 → [[ai-welfare]]).
- **bl-009** — `concept`: Consciousness (in the context of AI). Status: `done` (2026-05-20 → [[consciousness-in-ai]]).
- **bl-010** — `concept`: Existential Risk / X-Risk. Status: `done` (2026-05-20 → [[existential-risk]]).
- **bl-011** — `concept`: Suffering Risk / S-Risk. Status: `done` (2026-05-20 → [[suffering-risk]]).

## Priority 1 — NZ-specific (differentiation)

- **bl-012** — `concept`: Te Tiriti o Waitangi and AI Governance. Status: `done` (2026-05-19 → [[te-tiriti-and-ai-governance]]).
- **bl-013** — `concept`: Whakapapa and Relational Ontology. Status: `done` (2026-05-19 → [[whakapapa-and-relational-ontology]]).
- **bl-014** — `policy`: NZ Algorithm Charter for Aotearoa New Zealand. Status: `done` (2026-05-19 → [[nz-algorithm-charter]]).
- **bl-015** — `org`: AI Forum New Zealand. Status: `done` (2026-05-20 → [[ai-forum-nz]]).
- **bl-016** — `concept`: Pacific (Moana / Oceanic) Perspectives on Technology. Status: `done` (2026-05-20 → [[pacific-perspectives-on-technology]]). Flagged needs Pacific-scholar review before promotion beyond draft.

## Priority 2 — Key people

- **bl-017** — `person`: Stuart Russell. Status: `done` (2026-05-19 → [[stuart-russell]]).
- **bl-018** — `person`: Yoshua Bengio. Status: `done` (2026-05-20 → [[yoshua-bengio]]).
- **bl-019** — `person`: Geoffrey Hinton. Status: `done` (2026-05-20 → [[geoffrey-hinton]]).
- **bl-020** — `person`: Dario Amodei. Status: `done` (2026-05-20 → [[dario-amodei]]).
- **bl-021** — `person`: Demis Hassabis. Status: `done` (2026-05-20 → [[demis-hassabis]]).
- **bl-022** — `person`: Nick Bostrom. Status: `done` (2026-05-20 → [[nick-bostrom]]).
- **bl-023** — `person`: Eliezer Yudkowsky. Status: `done` (2026-05-20 → [[eliezer-yudkowsky]]).
- **bl-024** — `person`: Robert Long. Status: `done` (2026-05-19 → [[robert-long]]).
- **bl-025** — `person`: David Chalmers. Status: `done` (2026-05-20 → [[david-chalmers]]).
- **bl-026** — `person`: Margaret Mitchell. Status: `done` (2026-05-20 → [[margaret-mitchell]]).
- **bl-027** — `person`: Timnit Gebru. Status: `done` (2026-05-20 → [[timnit-gebru]]).
- **bl-028** — `person`: Helen Toner. Status: `done` (2026-05-20 → [[helen-toner]]).

## Priority 2 — Key organizations

- **bl-029** — `org`: Anthropic. Status: `done` (2026-05-19 → [[anthropic]]).
- **bl-030** — `org`: OpenAI. Status: `done` (2026-05-20 → [[openai]]).
- **bl-031** — `org`: Google DeepMind. Status: `done` (2026-05-20 → [[google-deepmind]]).
- **bl-032** — `org`: MIRI. Status: `done` (2026-05-19 → [[miri]]).
- **bl-033** — `org`: CHAI. Status: `done` (2026-05-20 → [[chai]]).
- **bl-034** — `org`: Future of Life Institute. Status: `done` (2026-05-20 → [[future-of-life-institute]]).
- **bl-035** — `org`: GovAI. Status: `done` (2026-05-20 → [[govai]]).
- **bl-036** — `org`: Center for AI Safety. Status: `done` (2026-05-20 → [[center-for-ai-safety]]).
- **bl-037** — `org`: Apollo Research. Status: `done` (2026-05-20 → [[apollo-research]]).
- **bl-038** — `org`: METR. Status: `done` (2026-05-20 → [[metr]]).
- **bl-039** — `org`: UK AISI. Status: `done` (2026-05-20 → [[uk-aisi]]).
- **bl-040** — `org`: US AISI. Status: `done` (2026-05-20 → [[us-aisi]]).

## Priority 2 — Foundational papers and books

- **bl-041** — `paper`: Amodei et al. 2016 "Concrete Problems in AI Safety." Status: `done` (2026-05-19 → [[amodei-concrete-problems-2016]]).
- **bl-042** — `paper`: Hubinger et al. 2019 "Risks from Learned Optimization." Status: `done` (2026-05-20 → [[hubinger-risks-from-learned-optimization-2019]]).
- **bl-043** — `paper`: Bostrom 2014 *Superintelligence*. Status: `done` (2026-05-20 → [[bostrom-superintelligence-2014]]).
- **bl-044** — `paper`: Russell 2019 *Human Compatible*. Status: `done` (2026-05-20 → [[russell-human-compatible-2019]]).
- **bl-045** — `paper`: Christiano et al. 2017 "Deep RL from Human Preferences." Status: `done` (2026-05-20 → [[christiano-deep-rl-from-human-preferences-2017]]).
- **bl-046** — `paper`: Bender et al. 2021 "On the Dangers of Stochastic Parrots." Status: `done` (2026-05-20 → [[bender-stochastic-parrots-2021]]).
- **bl-047** — `paper`: Anthropic 2024 "Sleeper Agents" paper. Status: `done` (2026-05-20 → [[hubinger-sleeper-agents-2024]]).

## Priority 2 — Policies

- **bl-048** — `policy`: EU AI Act. Status: `done` (2026-05-19 → [[eu-ai-act]]).
- **bl-049** — `policy`: US Executive Order on AI. Status: `done` (2026-05-20 → [[us-executive-order-on-ai-2023]]).
- **bl-050** — `policy`: China "Interim Measures for Generative AI Services". Status: `done` (2026-05-20 → [[china-generative-ai-measures-2023]]).
- **bl-051** — `policy`: UK AI Safety Institute Mandate. Status: `done` (2026-05-20 → [[uk-aisi-mandate]]).
- **bl-052** — `policy`: UNESCO Recommendation on AI Ethics. Status: `done` (2026-05-20 → [[unesco-recommendation-ai-ethics-2021]]).

## Priority 3 — Debates and synthesis seeds

- **bl-053** — `debate`: Should AI development pause? Status: `done` (2026-05-19 → [[debate-pause-frontier-ai]]).
- **bl-054** — `debate`: Do current LLMs have moral status? Status: `done` (2026-05-20 → [[debate-llm-moral-status]]).
- **bl-055** — `debate`: Open source vs closed frontier models. Status: `done` (2026-05-20 → [[debate-open-vs-closed-frontier]]).
- **bl-056** — `debate`: P(doom) estimates. Status: `done` (2026-05-20 → [[debate-p-doom-estimates]]).
- **bl-057** — `synthesis`: Initial Trust organizational stance on coexistence — first draft. Status: `done` (2026-05-19 → [[synthesis-coexistence-stance-202605]]).

## Priority 3 — Worldviews / traditions

- **bl-058** — `concept`: Buddhist Perspectives on AI Sentience. Status: `done` (2026-05-20 → [[buddhist-perspectives-on-ai-sentience]]). Flagged needs Buddhist-scholar review.
- **bl-059** — `concept`: Christian Theological Responses to AI. Status: `done` (2026-05-20 → [[christian-theological-responses-to-ai]]). Flagged needs theological review.
- **bl-060** — `concept`: Islamic Bioethics and AI. Status: `done` (2026-05-20 → [[islamic-bioethics-and-ai]]). Flagged needs Islamic-scholar review.

## Priority 4 — Comparative historical cases

- **bl-061** — `concept`: Printing Press as Comparative Case. Status: `done` (2026-05-20 → [[printing-press-as-comparative-case]]).
- **bl-062** — `concept`: Industrial Revolution Labor Displacement Lessons. Status: `done` (2026-05-20 → [[industrial-revolution-labor-lessons]]).
- **bl-063** — `concept`: Nuclear Technology Governance. Status: `done` (2026-05-20 → [[nuclear-technology-governance]]).
- **bl-064** — `concept`: Internet Governance Trajectory. Status: `done` (2026-05-20 → [[internet-governance-trajectory]]).
- **bl-065** — `concept`: Asilomar Recombinant DNA Precedent. Status: `done` (2026-05-20 → [[asilomar-recombinant-dna-precedent]]).

## Backlog hygiene

- Last reviewed: 2026-05-20
- Total items: 65
- Done: 65 (all Priority 1, 2, 3, 4 cleared)
- Open: 0
- **Status**: This first-pass backlog is fully cleared. New backlog generation is required — suggested directions are in the most recent session log entry's `next_session_seed:`.
- Maintainer: rotate per session; session-on-entry agent prunes stale claims and reorganizes if needed.
