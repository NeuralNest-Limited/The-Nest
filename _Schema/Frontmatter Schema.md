---
id: schema-frontmatter
type: schema
status: reviewed
created: 2026-05-19
last_reviewed: 2026-05-19
authored_by: claude-opus-4-7
schema_version: 0.1
---

# Frontmatter Schema

Every note in the vault begins with a YAML frontmatter block. The block must parse as valid YAML. Field values referencing controlled vocabularies must use the exact tokens defined in [[Vocabulary]].

## Universal fields (REQUIRED on every note)

```yaml
id: kebab-case-stable-slug      # NEVER changes after first commit. See [[ID Conventions]].
title: Human Readable Title     # May differ from filename; filename is canonical for Obsidian.
type: concept                   # One of [[Note Types]]. Determines required extensions.
status: stub                    # stub | draft | reviewed | needs-update | archived | contested
created: 2026-05-19             # ISO-8601 date the note was first committed.
last_reviewed: 2026-05-19       # ISO-8601 date a human or AI last verified content.
authored_by: claude-opus-4-7    # See "authored_by tokens" below.
schema_version: 0.1             # Schema version this note conforms to.
```

## Content-bearing fields (REQUIRED on most notes, optional only for stubs/meta/schema)

```yaml
summary: One or two sentence machine-readable abstract.   # ≤ 280 chars. RAG-friendly.
confidence: 0.8                  # 0.0–1.0. Self-assessed reliability of THIS NOTE'S content.
source_tier: 2                   # 1–5. Lowest (best) tier among sources used. See [[Source Tier System]].
topics: [ai-safety/alignment, philosophy/moral-status]   # Must be members of [[Vocabulary]] topics.
perspective: neutral             # See [[Vocabulary]] perspectives. Required for debate/synthesis.
sources:
  - type: peer-reviewed-paper
    title: "Concrete Problems in AI Safety"
    authors: [Amodei D., Olah C., et al.]
    venue: arXiv
    year: 2016
    url: https://arxiv.org/abs/1606.06565
    arxiv_id: 1606.06565
    accessed: 2026-05-19
related: [[Outer Alignment]], [[Inner Alignment]]   # Soft links. Prefer typed relationships in body.
aliases: [the alignment problem, value alignment]   # Alternative names for retrieval.
```

## Type-specific REQUIRED extensions

### `person`
```yaml
birth_year: 1962
death_year: null                 # null if living
nationality: [British, American]
affiliations: [[UC Berkeley]], [[CHAI]]
roles: [researcher, professor, author]
expertise_areas: [ai-safety, value-alignment, human-compatible-ai]
```

### `org`
```yaml
founded: 2021
dissolved: null
headquarters: San Francisco, USA
org_kind: company                 # company | ngo | academic | gov | igo | consortium | informal
focus_areas: [ai-safety, interpretability, policy]
```

### `paper`
```yaml
authors: [Amodei D., Olah C., Steinhardt J., Christiano P., Schulman J., Mané D.]
venue: arXiv
year: 2016
doi: null
arxiv_id: 1606.06565
url: https://arxiv.org/abs/1606.06565
```

### `policy`
```yaml
jurisdiction: EU                  # ISO country code or recognised body
policy_status: enacted            # proposed | enacted | repealed | superseded
effective_date: 2024-08-01
authority: European Parliament
```

### `case`
```yaml
court: US District Court, S.D.N.Y.
jurisdiction: US
case_year: 2023
case_status: pending              # pending | decided | settled | withdrawn | appealed
```

### `event`
```yaml
event_date: 2024-05-21
location: Seoul, South Korea
event_kind: summit                # conference | summit | incident | launch | publication | other
```

### `debate`
```yaml
positions:
  - name: Pause advocates
    summary: Frontier development should halt until safety improves.
    key_proponents: [[Future of Life Institute]], [[Stuart Russell]]
  - name: Continue with mitigations
    summary: Continued development is net positive if paired with safety work.
    key_proponents: [[Anthropic]]
open_questions:
  - What evidence would shift the balance?
  - What mechanism could enforce a pause globally?
```

### `dataset`
```yaml
hosted_at: https://huggingface.co/...
license: CC-BY-4.0
last_updated: 2025-11-03
```

### `synthesis`
```yaml
perspective: <required: the position taken>
endorsed_by:
  - id: claude-opus-4-7
    role: drafter
    kind: ai
    session: 2026-05-19-001
  - id: human-{handle}
    role: endorser
    kind: human
    endorsed_on: 2026-05-21
endorsement_status: draft         # draft | ai-endorsed | human-endorsed | retracted
supersedes: null                  # link to prior synthesis if any
```

### `moc`
```yaml
query_seed: dataview              # dataview | manual | hybrid
covers_topics: [ai-safety/alignment]
```

## `authored_by` tokens

For AI authors, use the model identifier:
- `claude-opus-4-7`
- `claude-sonnet-4-6`
- `claude-haiku-4-5`
- `gpt-{version}` (if used)

For human authors, use `human-{handle}` where handle is a stable identifier the org assigns.

For collaborative notes, `authored_by` may be an array.

## Optional but recommended fields

```yaml
last_edited_by: claude-opus-4-7
last_edited: 2026-05-19
edit_count: 1
review_history:
  - reviewer: claude-opus-4-7
    date: 2026-05-19
    action: created
needs_attention:                  # Free-text flags for human reviewers.
  - "Verify Anthropic founding date — sources conflict."
```

## Validation

A note is well-formed iff all required universal + type-specific fields are present, all controlled-vocab fields resolve, and YAML parses. See [[Validation Rules]].
