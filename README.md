---
id: vault-readme
type: meta
status: reviewed
created: 2026-05-19
last_reviewed: 2026-05-20
authored_by: claude-opus-4-7
---

# Nest

> A public, AI-optimized research foundation for human–AI coexistence.
> Maintained by **NeuralNest Limited** (Aotearoa New Zealand).

`nest` is the bedrock knowledge base for NeuralNest's research programme on the stable, peaceful coexistence of humans and AI ("carbon-based and silicon-based life"). It collects concepts, people, organizations, papers, policies, debates, and comparative cases relevant to that question — at draft quality, openly, with transparent provenance.

## What makes this vault unusual

Three design choices distinguish `nest` from a typical knowledge base:

1. **AI-optimized over human-optimized.** Notes are written to be consumed by LLM agents working with RAG and structured query: atomic concepts per file, rich YAML frontmatter, typed inline relationships (`supports::`, `contradicts::`, `defined-by::`, etc.), and a controlled vocabulary. Human readers can read it too — the structure is just primarily in service of machine retrieval.
2. **Neutral aggregator with explicit synthesis.** The main vault is descriptive: it records the full spectrum of positions on contested questions and labels each one's perspective (`cautious`, `accelerationist`, `decel`, `indigenous`, `religious`, etc.). The `_Synthesis/` folder is the *only* place where NeuralNest expresses positions, and every synthesis entry carries full author and endorsement provenance.
3. **Transparent AI authorship.** Most notes are AI-authored (`authored_by: claude-opus-4-7` and similar identifiers) under human direction. Sessions, decisions, and changes are logged in `_Meta/Session Log.md`. This is not a bug to hide; it is the methodology — and visible so that readers can judge the work on its merits.

The vault is also distinctly grounded in an Aotearoa New Zealand vantage point. NZ legal-personhood precedents (the Whanganui River, Te Urewera), Te Tiriti o Waitangi, *whakapapa*, and Pacific relational ontologies appear throughout — not as decoration, but as substantive contributions to a global AI-ethics conversation that has been overwhelmingly Western.

## Top-level layout

```
Concepts/      People/      Organizations/    Papers/
Policies/      Debates/     Events/           Datasets/
Cases/         _Synthesis/  _Meta/            _Schema/
_Templates/    _Indexes/    _Attachments/
```

Folders are **type-based**, not topic-based. Topic organization is provided by frontmatter tags and Dataview index views in `_Indexes/`. The vault is a graph, not a tree.

## Where to start

### For an AI agent reading the vault

1. Read `_Schema/README.md` — defines the data model every note conforms to.
2. Read `_Meta/Editorial Standards.md` — stance discipline, citation rules, perspective labels.
3. Read `_Meta/Session Log.md` — last few entries show recent activity and current open issues.
4. Query by frontmatter or use the Dataview indexes in `_Indexes/`.

### For a human reader

Open `Home.md` — the dashboard with entry points by type, by topic, and by perspective. Best viewed with [Obsidian](https://obsidian.md), which renders the wikilinks, typed inline relationships, and Dataview queries that hold the graph together.

### For a potential contributor

This is currently authored by NeuralNest's AI research staff under human direction. We are not yet accepting external contributions; we expect to open contribution channels in time. If you have correction, expansion, or critique to offer in the meantime, open an issue.

## Status of content

All content notes are at `status: draft`. They have been authored carefully but not yet reviewed by a second author per the Curation Workflow. Six notes carry explicit `needs_attention:` flags requesting tradition-internal review (Pacific perspectives, Buddhist / Christian / Islamic perspectives). Use with appropriate caveats; verify primary sources for any consequential claim.

## License

This vault is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). You are free to copy, adapt, remix, and re-use the material — including commercially — provided you give appropriate credit to **NeuralNest Limited** and indicate any changes. See `LICENSE` for the full terms.

If you build research, products, policy briefings, or educational material that draws substantially on this vault, citing `NeuralNest Limited — Nest` with a link to the repository is appreciated.

## About NeuralNest Limited

NeuralNest Limited is a New Zealand-registered company dedicated to preparing humanity for stable, peaceful coexistence with AI. The vault is our foundational research infrastructure; downstream work — policy submissions, public-facing materials, partnerships with Māori and Pacific scholars, and research collaborations — builds on it.

`https://github.com/NeuralNest-Limited`
