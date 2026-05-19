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
- **bl-057** — `synthesis`: Initial organizational stance on coexistence — first draft. Status: `done` (2026-05-19 → [[synthesis-coexistence-stance-202605]]).

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
- Batch 1 total: 65 items (bl-001 to bl-065) — all done
- Batch 2 total: 50 items (bl-066 to bl-115) — open, see below
- Maintainer: rotate per session; session-on-entry agent prunes stale claims and reorganizes if needed.

---

# Batch 2 (added 2026-05-20-003, autonomous session)

Generated after Batch 1 cleared. Same format. New IDs continue from bl-066.

## Priority 1 (Batch 2) — Plug structural gaps and demo unused note types

- **bl-066** — `person`: Sam Altman (OpenAI CEO; central to Nov 2023 crisis). Status: `open`.
- **bl-067** — `person`: Ilya Sutskever (OpenAI co-founder, chief scientist until 2024; central to Nov 2023; Safe Superintelligence Inc.). Status: `open`.
- **bl-068** — `person`: Yann LeCun (Meta chief AI scientist; Turing Award; paradigm anti-x-risk voice). Status: `open`.
- **bl-069** — `person`: Mustafa Suleyman (DeepMind co-founder, Inflection AI, now Microsoft AI). Status: `open`.
- **bl-070** — `person`: Dan Hendrycks (CAIS founder, CAIS extinction statement organizer, WMDP). Status: `open`.
- **bl-071** — `person`: Beth Barnes (ARC Evals / METR founder). Status: `open`.
- **bl-072** — `dataset`: MMLU (Hendrycks et al. 2020) — demo of `dataset` note type. Status: `open`.
- **bl-073** — `event`: AI Bletchley Summit (November 2023) — demo of `event` note type; founding of UK AISI. Status: `open`.
- **bl-074** — `case`: Authors Guild v OpenAI (2023, US, ongoing) — demo of `case` note type; LLM training copyright. Status: `open`.
- **bl-075** — `case`: Air Canada chatbot case (Moffat v Air Canada, 2024, BC Canada) — small claims tribunal held company liable for chatbot misrepresentation. Status: `open`.

## Priority 2 (Batch 2) — Technical depth

- **bl-076** — `concept`: Chain-of-Thought Reasoning. Status: `open`.
- **bl-077** — `concept`: In-Context Learning. Status: `open`.
- **bl-078** — `concept`: Activation Patching (mechanistic interpretability technique). Status: `open`.
- **bl-079** — `concept`: Linear Probing / Probing Classifiers. Status: `open`.
- **bl-080** — `concept`: Function Vectors / Task Vectors. Status: `open`.
- **bl-081** — `concept`: Knowledge Distillation. Status: `open`.
- **bl-082** — `concept`: Constitutional AI sub-techniques (Critique-Revision, Self-Constitutional, Collective Constitutional AI). Status: `open`.

## Priority 2 (Batch 2) — Consciousness theories (each as own concept, currently mentioned in Consciousness in AI but no atomic notes)

- **bl-083** — `concept`: Global Workspace Theory (Baars, Dehaene). Status: `open`.
- **bl-084** — `concept`: Higher-Order Theory of Consciousness (Rosenthal, Lau). Status: `open`.
- **bl-085** — `concept`: Attention Schema Theory (Graziano). Status: `open`.
- **bl-086** — `concept`: Integrated Information Theory (Tononi). Status: `open`.
- **bl-087** — `concept`: Predictive Processing / Active Inference (Friston, Clark, Seth). Status: `open`.

## Priority 2 (Batch 2) — Missing key papers

- **bl-088** — `paper`: Bai et al. 2022 "Constitutional AI" (Anthropic). Status: `open`.
- **bl-089** — `paper`: Elhage et al. 2022 "Toy Models of Superposition" (Anthropic). Status: `open`.
- **bl-090** — `paper`: Templeton et al. 2024 "Scaling Monosemanticity" (Anthropic). Status: `open`.
- **bl-091** — `paper`: Ouyang et al. 2022 "InstructGPT" (OpenAI). Status: `open`.
- **bl-092** — `paper`: Carlsmith 2021 "Is Power-Seeking AI an Existential Risk?" (Open Philanthropy). Status: `open`.
- **bl-093** — `paper`: Cotra 2020 "Bio Anchors" / forecasting transformative AI timelines. Status: `open`.
- **bl-094** — `paper`: Ord 2020 *The Precipice* (book). Status: `open`.
- **bl-095** — `paper`: Sharma et al. 2023 "Towards Understanding Sycophancy in Language Models" (Anthropic). Status: `open`.

## Priority 2 (Batch 2) — Missing key orgs

- **bl-096** — `org`: DAIR Institute (Gebru, Hanna; ex-Google ethical AI). Status: `open`.
- **bl-097** — `org`: Eleos AI Research (Long; AI welfare). Status: `open`.
- **bl-098** — `org`: Center on Long-Term Risk (CLR; s-risk research). Status: `open`.
- **bl-099** — `org`: 80,000 Hours (EA career advice; AI safety pipeline). Status: `open`.
- **bl-100** — `org`: Redwood Research (alignment + interpretability). Status: `open`.

## Priority 3 (Batch 2) — Synthesis and meta

- **bl-101** — `synthesis`: On AI authorship as research method (the project's own meta-stance; v0.1). Status: `open`. Requires human endorsement.
- **bl-102** — `synthesis`: On precautionary AI welfare practices in frontier labs (org position on Long et al. framework). Status: `open`. Requires human endorsement.
- **bl-103** — `synthesis`: On the relationship between near-term harms and long-term risks (bridging FAccT and safety positions). Status: `open`. Requires human endorsement.

## Priority 3 (Batch 2) — Empirical corpus building

- **bl-104** — `dataset`: Empirical record of model responses on key alignment-relevant prompts (a corpus we ourselves build; reproducible record of Claude / GPT / Gemini behavior on a fixed prompt set across model generations). Status: `open`.
- **bl-105** — `dataset`: WMDP (Weapons of Mass Destruction Proxy) — CAIS 2024 dangerous-knowledge benchmark. Status: `open`.
- **bl-106** — `dataset`: METR Task Suite — autonomous-task evaluation benchmark. Status: `open`.
- **bl-107** — `dataset`: HarmBench — jailbreak evaluation benchmark. Status: `open`.

## Priority 3 (Batch 2) — Additional policies and cases

- **bl-108** — `policy`: California SB 1047 / state-level US AI laws (Colorado AI Act, TX TRAIGA, etc.). Status: `open`.
- **bl-109** — `policy`: Korea AI Basic Act (2024). Status: `open`.
- **bl-110** — `case`: NYT v OpenAI / Microsoft (2023, US, ongoing) — copyright over training corpora. Status: `open`.

## Priority 4 (Batch 2) — Schema and infrastructure

- **bl-111** — `meta`: Schema v0.2 candidate revisions (consolidate `source_type` into Vocabulary.md; tighten `events` and `dataset` type-specific fields after first uses; add `language:` field; consider whether to add `superseded_by:` as inverse of `supersedes::`). Status: `open`.
- **bl-112** — `meta`: Write `validate.py` script to enforce Validation Rules automatically; integrate with git pre-commit hook. Status: `open`.
- **bl-113** — `meta`: Decide Obsidian Publish / Quartz / other web-mirror strategy for browseable public access without Obsidian. Status: `open`. Requires user input.
- **bl-114** — `meta`: Translation strategy — should The Nest have a Chinese mirror? te reo Māori summary? Status: `open`. Requires user input.
- **bl-115** — `meta`: Status promotion pass — have a different `authored_by:` identity (fresh Claude session or human) walk through priority-1 notes and promote from draft to reviewed per Curation Workflow §"Review protocol". Status: `open`.
