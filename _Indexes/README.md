---
id: indexes-readme
type: meta
status: reviewed
created: 2026-05-19
last_reviewed: 2026-05-19
authored_by: claude-opus-4-7
schema_version: 0.1
---

# _Indexes/ — Maps of Content

MOC (Map of Content) notes are curated indexes. They contain:

1. **Hand-curated** featured notes — the entry points an outsider should see first.
2. **Dataview-generated** comprehensive lists — auto-refreshing whenever frontmatter changes.

This hybrid (manual highlights + automatic long tail) is the heart of how the vault stays navigable as it scales. Authors curate the top; the system maintains the bottom.

## MOCs in this folder

By type (one per note type):
- `MOC — Concepts.md`
- `MOC — People.md`
- `MOC — Organizations.md`
- `MOC — Papers.md`
- `MOC — Policies.md`
- `MOC — Debates.md`
- `MOC — Events.md`
- `MOC — Cases.md`
- `MOC — Datasets.md`

By major topic (filled in as note coverage grows):
- `MOC — AI Safety and Alignment.md`
- `MOC — AI Welfare and Moral Status.md`
- `MOC — Governance and Policy.md`
- `MOC — Philosophy of Mind.md`
- `MOC — Society and Economy.md`
- `MOC — Aotearoa NZ Lens.md`
- `MOC — Worldviews and Traditions.md`
- `MOC — Futures and Scenarios.md`

Special views:
- `MOC — Spectrum of Views.md` — perspective-faceted index
- `MOC — Synthesis Index.md` — all `_Synthesis/` notes by topic and endorsement status
- `MOC — Recent Activity.md` — recently created/edited notes

## Dataview note

MOCs assume the [Dataview](https://github.com/blacksmithgu/obsidian-dataview) Obsidian plugin is installed. Queries use the DQL syntax. If Dataview is not installed, the manual sections still work; the auto-generated sections render as plain code blocks.

## Adding a new MOC

When a topic accumulates ~5+ notes, consider creating an MOC for it. Start from [[../_Templates/MOC Template]].
