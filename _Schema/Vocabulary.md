---
id: schema-vocabulary
type: schema
status: reviewed
created: 2026-05-19
last_reviewed: 2026-05-19
authored_by: claude-opus-4-7
schema_version: 0.1
---

# Controlled Vocabulary

Every enum-valued frontmatter field MUST use a value from the lists below. New values are added by editing this file in a dedicated commit titled `vocab: add <term>` and recording rationale in `_Meta/Session Log.md`.

## `status` values

| Value | Meaning |
|---|---|
| `stub` | Placeholder. Has frontmatter but little or no body. Awaiting research. |
| `draft` | Has substantive content. Not yet reviewed. |
| `reviewed` | Verified by at least one second author (AI or human). |
| `needs-update` | Known to be outdated or incomplete. See `needs_attention:`. |
| `archived` | Superseded by newer note(s). Kept for history. Link via `supersedes::`. |
| `contested` | Content is actively disputed. See a debate note for the alternatives. |

## `perspective` values

These label the **stance taken** by the note's content. Required for `debate` and `synthesis`. Optional for others; use only if the note presents a particular position (e.g., when summarizing one side of a debate).

| Value | Meaning |
|---|---|
| `neutral` | Descriptive only. No normative claims. (Most notes should be this.) |
| `cautious` | Emphasizes risks; favours slow / careful development. |
| `optimist` | Emphasizes benefits; expects positive outcomes. |
| `accelerationist` | Advocates faster development; sees delay itself as harmful. |
| `decel` | Advocates pausing, halting, or reversing AI development. |
| `safety-pragmatist` | Between cautious and accelerationist: develop with safety as constraint. |
| `techno-libertarian` | Favours minimal regulation, individual / market choice. |
| `techno-democratic` | Favours strong democratic governance of AI. |
| `corporate-realist` | Pragmatic industry perspective. |
| `indigenous` | Framework rooted in indigenous knowledge systems. |
| `religious` | Framework rooted in a religious tradition. (Specify which in body.) |
| `abolitionist` | Advocates AI rights, personhood, moral consideration. |
| `posthumanist` | Views human/AI distinction as itself the problem to dissolve. |
| `descriptive` | Reports an empirical observation without normative content. |

## `topics` values (hierarchical, slash-delimited)

Notes may have multiple topics. Use the most specific term that applies; parent topics are implicit. Adding a child term requires its parent to exist.

### AI Technical Core
- `ai-safety`
- `ai-safety/alignment`
- `ai-safety/alignment/outer`
- `ai-safety/alignment/inner`
- `ai-safety/alignment/scalable-oversight`
- `ai-safety/interpretability`
- `ai-safety/interpretability/mechanistic`
- `ai-safety/evaluation`
- `ai-safety/evaluation/dangerous-capabilities`
- `ai-safety/evaluation/alignment-evals`
- `ai-safety/control`
- `ai-safety/deceptive-alignment`
- `ai-capabilities`
- `ai-capabilities/scaling`
- `ai-capabilities/benchmarks`
- `ai-welfare`
- `ai-welfare/moral-patienthood`
- `ai-welfare/suffering`

### Ethics, Governance, Policy
- `ai-ethics`
- `ai-ethics/bias`
- `ai-ethics/fairness`
- `ai-ethics/transparency`
- `ai-ethics/accountability`
- `ai-ethics/privacy`
- `governance`
- `governance/global`
- `governance/national`
- `governance/sectoral`
- `governance/self-regulation`
- `governance/standards`
- `law`
- `law/copyright`
- `law/liability`
- `law/personhood`
- `law/employment`

### Society, Economy, Labor
- `society`
- `society/labor`
- `society/education`
- `society/relationships`
- `society/inequality`
- `society/mental-health`
- `economy`
- `economy/labor-market`
- `economy/post-agi`
- `economy/capital-concentration`
- `economy/ubi`

### Geopolitics, Strategy
- `geopolitics`
- `geopolitics/race`
- `geopolitics/compute`
- `geopolitics/export-controls`
- `geopolitics/military`
- `geopolitics/intelligence`

### Philosophy, Mind
- `philosophy`
- `philosophy/consciousness`
- `philosophy/moral-status`
- `philosophy/personhood`
- `philosophy/identity`
- `philosophy/agency`
- `philosophy/free-will`
- `philosophy/ethics`
- `philosophy/epistemology`

### Worldviews, Traditions
- `worldview/maori`
- `worldview/pacific`
- `worldview/buddhist`
- `worldview/christian`
- `worldview/islamic`
- `worldview/jewish`
- `worldview/hindu`
- `worldview/secular-humanist`
- `worldview/animist`
- `worldview/other`

### History, Comparative
- `history/ai-thought`
- `history/comparative-tech`
- `history/comparative-tech/printing-press`
- `history/comparative-tech/industrial-revolution`
- `history/comparative-tech/nuclear`
- `history/comparative-tech/internet`
- `history/comparative-tech/biotech`

### Environment, Physical
- `environment/energy`
- `environment/water`
- `environment/materials`
- `environment/climate`

### Futures, Scenarios
- `futures/scenarios`
- `futures/risk`
- `futures/risk/x-risk`
- `futures/risk/s-risk`
- `futures/positive`
- `futures/transition`

### Empirical, Relational
- `empirical/model-behavior`
- `empirical/human-ai-relations`
- `empirical/parasocial`
- `empirical/case-study`

### Regions (for `region:` tags or topic prefix)
- `region/nz` (Aotearoa New Zealand — primary local lens)
- `region/pacific`
- `region/us`
- `region/eu`
- `region/uk`
- `region/china`
- `region/india`
- `region/japan`
- `region/global`

### Meta
- `meta/methodology`
- `meta/curation`
- `meta/governance` (vault governance, not AI governance)

## `source_tier` values

See [[Source Tier System]] for definitions. Values: `1`, `2`, `3`, `4`, `5`.

## `org_kind`, `policy_status`, `case_status`, `event_kind`, `endorsement_status`

Defined in [[Frontmatter Schema]]. Listed here for completeness — any new value requires editing both files.

## Maintenance

If you find yourself wanting to use a term not in this file:
1. **Stop**. Do not invent it inline.
2. Check aliases (maybe the concept exists under a different name).
3. If genuinely new, propose addition: edit this file, add to `_Meta/Session Log.md` with rationale, commit as `vocab: add <term>`.
4. Then use it.

This discipline is what keeps retrieval reliable across thousands of notes and dozens of agents.
