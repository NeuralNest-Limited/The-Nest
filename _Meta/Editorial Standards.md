---
id: meta-editorial-standards
type: meta
status: reviewed
created: 2026-05-19
last_reviewed: 2026-05-19
authored_by: claude-opus-4-7
schema_version: 0.1
---

# Editorial Standards

The vault has one editorial commitment: **descriptive completeness, not selective curation.** Any agent — AI or human — drafting notes must internalize the standards below.

## 1. Stance discipline

The vault is split into two stance regimes:

### Neutral zone (everything except `_Synthesis/`)

- Notes describe what exists, what is claimed, what evidence supports each claim, and who holds which position.
- Notes do **not** endorse, recommend, or argue for any contested position.
- When a note summarizes a single perspective (e.g., "the cautious case for X"), it must be explicitly labeled in the body section heading and the `perspective:` frontmatter field.

### Synthesis zone (`_Synthesis/`)

- Notes here **may** take positions on contested questions.
- Every synthesis note carries `endorsed_by:` provenance (which AI/human, what role, what date) and `endorsement_status:` (draft / ai-endorsed / human-endorsed / retracted).
- A synthesis note is the organization's interpretation — not a fact about the world.
- Retractions are kept (status `archived` with `supersedes::`); they are not deleted.

## 2. Coverage

When researching a contested topic:

- Identify the **full spectrum** of positions before drafting. Five-position coverage minimum: most cautious, mainstream cautious, mainstream optimist, most accelerationist, and any orthogonal positions (indigenous, religious, abolitionist).
- For each major position, produce or link to a note presenting that position **steel-manned** — strongest version, attributed to its best proponents.
- A debate note (`type: debate`) summarizes positions with cross-links.

We are not "balanced" in the journalistic sense of giving false equivalence. We are **comprehensive**: every serious position gets a fair hearing. A fringe position with no serious proponents gets a brief note, not equal column inches.

## 3. Citation

- Every empirical claim has a source. No exceptions.
- Sources have a tier (see [[Source Tier System]]) and an access date.
- If a claim has T1 and T4 sources disagreeing, the note presents both and labels the disagreement — it does not silently pick a side.
- "Common knowledge" claims (e.g., "Anthropic is an AI lab") do not need a source. The boundary is judgment — when in doubt, cite.

## 4. Perspective labeling

When the body presents a position:

```markdown
## The cautious case for slowing frontier development {#cautious}

`perspective: cautious`

(content)
```

The reader / retrieval agent can then scope queries to a particular perspective.

## 5. Provenance for AI authorship

Per the user's decision (recorded in project memory): AI agents **may** author notes in `_Synthesis/`, including synthesis content, but must:

- Set `authored_by:` to the model identifier (e.g., `claude-opus-4-7`).
- Include themselves in `endorsed_by:` with `kind: ai` and `role: drafter`.
- Mark `endorsement_status: draft` or `ai-endorsed`. Only `human-{handle}` entries with `role: endorser` can promote to `human-endorsed`.
- For high-stakes synthesis notes, flag in `needs_attention:` for human review.

## 6. Confidence

The `confidence:` field is the **authoring agent's self-assessment of this note's reliability**. Calibration guidelines:

| Range | When to use |
|---|---|
| 0.9–1.0 | Multiple T1 sources agree; well-established. |
| 0.7–0.9 | Strong sources, some areas of nuance or live debate. |
| 0.5–0.7 | Genuinely contested or rapidly evolving. |
| 0.3–0.5 | Speculative, weak sourcing, or first-pass coverage. |
| 0.0–0.3 | Stub or known-unreliable; flag heavily. |

Honest under-confidence is preferred to overconfident drafting. A note with `confidence: 0.4` flagged for review is more useful than one at `0.9` that is wrong.

## 7. Disagreement with prior notes

If you (an agent) believe a prior note is wrong:

1. Do NOT silently overwrite.
2. Read the note's edit history (git log).
3. Add a `needs_attention:` flag describing the disagreement.
4. If confident, edit the note AND add a `review_history` entry with action `revised`, your identifier, date, and what changed.
5. For substantive disagreement, write a separate note expressing the opposing view, link via `contradicts::`, and create a debate note if one doesn't exist.

The vault preserves disagreement; it doesn't resolve it through silent edits.

## 8. Things we don't do

- We don't summarize complex debates into a single "the answer is X." We make positions and their evidence findable.
- We don't write in the first person ("I think...") in neutral-zone notes. Synthesis notes may use "the organization's view is..."
- We don't smuggle stance through framing — adjectives like "obviously," "naively," "extremist" attached to one side are violations. Same goes for sneering paraphrase.
- We don't delete sourced material we disagree with. We add to it.
