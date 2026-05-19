---
id: meta-style-guide
type: meta
status: reviewed
created: 2026-05-19
last_reviewed: 2026-05-19
authored_by: claude-opus-4-7
schema_version: 0.1
---

# Style Guide — AI-Optimized Writing

This vault is primarily read by LLM agents performing retrieval-augmented research. Human readability is **explicitly deprioritized**. Optimize for:

1. **RAG chunking quality** — predictable structure means clean chunk boundaries.
2. **Direct quotability** — agents will lift sentences as evidence.
3. **Structural queryability** — typed metadata is more valuable than prose.
4. **Atomicity** — one idea per file makes precise retrieval possible.

## Length

- **Concept / paper / policy notes**: 200–1500 words body. If approaching 1500, consider splitting.
- **Person / org notes**: 150–800 words.
- **Debate notes**: 300–2000 words (positions sub-sections).
- **Synthesis notes**: 300–3000 words.
- **Stub notes**: < 100 words with `status: stub`.

Hard ceiling: 3000 words per note. Beyond that, split into linked atomic notes.

## Structure

Default section structure for a `concept` note:

```markdown
---
<frontmatter>
---

# Title

> One-line definition or claim (the abstract).

## Origin

When/where the concept emerged. Who introduced it. (`coined-by::`)

## Core claim

The substantive content. Plain prose. Atomic sub-claims as bullets where appropriate.

## Variants and refinements

Distinct formulations and who proposed them.

## Evidence

What empirical or theoretical evidence supports the concept. Cite sources.

## Critiques

Substantive criticisms and their authors. Steel-manned. (`criticized-by::`, `contradicts::`)

## Open questions

Specifically what is unresolved.

## Relationships

Typed inline links: `supports::`, `contradicts::`, `extends::`, etc.

## Sources

(If not in frontmatter, or for in-line citation expansion.)
```

Adjust section names per type — see [[_Templates/Concept Template]] etc. — but **keep section headings stable across notes of the same type**. This is what makes Dataview queries like "give me the Critiques section of every alignment concept" possible.

## Voice

- Third person. Descriptive. No "I think", "we argue", "obviously."
- Present tense for live claims, past tense for historical events.
- Hedged when warranted ("X suggests", "evidence indicates") — not for stylistic softening.
- No rhetorical questions, no metaphor-driven openings, no narrative hooks. Open with the definition.

## Sentences

- Each sentence should ideally encode one fact.
- Long compound sentences are harder for chunkers and harder to lift as evidence. Break.
- Define jargon on first use within a note (or link to the defining note). Do not assume readers have read prerequisites — they may be agents arriving via RAG with only this chunk loaded.

## Markdown conventions

- Headings: `#` for title (matches frontmatter `title:`), `##` for major sections, `###` sparingly for sub-sections.
- Lists: `-` for unordered. `1.` for ordered when sequence is meaningful.
- Bold for **defined terms** on first appearance.
- Italics for *emphasis*, sparingly.
- Code blocks for verbatim quotes, formulas, citations, model outputs.
- Block quotes (`>`) for important external quotations with attribution.
- Tables for comparing positions, listing variants, or anything tabular.

## What not to write

- Filler: "It's important to note that..." → just write the note.
- Throat-clearing: "In this section we will discuss..." → discuss it.
- Recapping: "As mentioned above..." → the chunk may not include "above."
- Padding: "various", "numerous", "many scholars have argued" without specifics.
- Editorial tone: "fascinatingly," "tellingly," "ironically" — these inject stance.
- AI tells in human-facing prose: "Let me explain..." "I hope this helps." — this is not a chat. Just write.

## Citations in prose

Inline: `(Russell 2019)` or `(Amodei et al. 2016)` — author-year style. Full reference lives in `sources:` frontmatter.

For direct quotes: `> "exact quote" — Source, page/section.`

## Linking discipline

- Link **early** in a note when introducing a term that has its own entry. Don't bury links in the relationships section if the term first appears in paragraph 1.
- Don't over-link: linking the same term five times in one note is noise. Link first occurrence, plus any occurrence in a sectional heading.
- Prefer typed relationships (`extends::`) over bare `[[wikilinks]]` when the relationship has semantic content.

## When unsure

Default to: shorter, more structured, more atomic, more linked. The vault is a graph, not an essay collection.
