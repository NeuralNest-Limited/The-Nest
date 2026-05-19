---
id: meta-source-tier-system
type: meta
status: reviewed
created: 2026-05-19
last_reviewed: 2026-05-19
authored_by: claude-opus-4-7
schema_version: 0.1
---

# Source Tier System

Every source in a note's `sources:` array carries a `type:` (what kind of source) and contributes to the note's `source_tier:` (lowest tier number among its sources, i.e. best tier).

The tier expresses **epistemic weight**, not topical relevance.

## Tiers

### Tier 1 — Highest epistemic weight

- Peer-reviewed papers in established venues
- Books from academic publishers
- Government / IGO official documents (treaty texts, regulations as enacted, official court decisions)
- Standards body publications (IEEE, ISO, NIST AI RMF)
- Direct primary data (datasets, model weights with documentation)

Examples: Nature/Science, NeurIPS/ICML/ICLR proceedings, UN reports, EU AI Act text, NIST AI Risk Management Framework, MIT Press / Oxford UP / Cambridge UP books.

### Tier 2 — Strong secondary

- Reports from established research organizations (AI labs' technical reports, RAND, Brookings, Future of Humanity Institute legacy work, GovAI papers)
- Investigative journalism in publications with strong editorial standards (Bloomberg, Reuters investigative, FT, Wired long-form, MIT Technology Review feature)
- Authoritative reference works (SEP — Stanford Encyclopedia of Philosophy)
- Conference talks by primary researchers (with video / slides available)
- White papers from major AI labs (Anthropic, OpenAI, DeepMind, Google Research)
- Multilateral organisation drafts and discussion papers (OECD, UNESCO drafts)

### Tier 3 — Expert commentary

- Researcher blogs and Substacks (e.g., AI Snake Oil, Import AI, Astral Codex Ten, Marginal Revolution on AI topics, Anthropic blog posts that are not formal papers)
- LessWrong / Alignment Forum posts authored by recognized researchers
- Podcasts featuring primary experts (Dwarkesh, 80,000 Hours, Lex Fridman with AI guests)
- Op-eds by named domain experts in mainstream outlets

Distinction from T2: the institutional editorial layer is thinner, but the author has recognized expertise.

### Tier 4 — General journalism and reporting

- News articles in mainstream outlets without specialized AI desks
- Industry trade publications
- Wire-service coverage
- Wikipedia (excellent for chronology and starting points, but trace claims to underlying sources before relying on them)

### Tier 5 — Observational / anecdotal

- Social media posts (X, Mastodon, Reddit) — even from notable figures
- Forum threads (Hacker News, r/LocalLLaMA)
- Anonymous blog posts
- Marketing material
- AI model outputs (when included as evidence, the model and prompt must be recorded)

T5 sources are valid for **documenting that a phenomenon exists** (e.g., "X became viral on Twitter on date Y"), not for establishing facts about the world.

## How to assign `source_tier` to a note

The note's `source_tier:` is the **lowest (best) tier** among its sources. Rationale: if any T1 source supports the core claim, the note inherits T1 weight. But the body must transparently acknowledge what is supported by what — see `_Meta/Editorial Standards.md` §3.

For a note built entirely on T3 sources, `source_tier: 3` and the body should signal that the claims are at the level of expert opinion rather than peer-reviewed finding.

## When tiers conflict

If T1 and T4 sources disagree:

- Lead with the T1 account.
- Note the T4 account explicitly and label it (e.g., "Reporting in [outlet] suggested otherwise, but lacked sourcing").
- Do not silently exclude the T4 account — readers should see the discrepancy.

If two T1 sources disagree:

- Present both. This is normal scientific disagreement.
- If a `debate` note exists or is warranted, link to or create it.

## Tier inflation and deflation

Avoid:

- **Tier inflation**: citing a researcher's blog post as if it were peer-reviewed because the researcher has authored peer-reviewed work elsewhere.
- **Tier deflation**: dismissing a strong primary source because it appeared in an outlet that also publishes T4 content.

The tier attaches to the specific source artifact, not to its author's overall reputation.

## Source `type` values (used in `sources:` arrays)

```
peer-reviewed-paper
preprint
book
white-paper
government-document
official-statement
court-decision
standards-document
expert-blog
substack
news-article
investigative-journalism
podcast
video
conference-talk
dataset
social-media
forum-post
wiki
model-output
internal-document
```

These should be moved into `_Schema/Vocabulary.md` once we're certain the list is stable. For now, they're authoritative here.
