---
id: templates-readme
type: meta
status: reviewed
created: 2026-05-19
last_reviewed: 2026-05-19
authored_by: claude-opus-4-7
schema_version: 0.1
---

# _Templates/

One template per note type. Copy the appropriate template when creating a new note, then fill in. Templates encode the structural conventions from [[Style Guide]] and the required fields from [[Frontmatter Schema]].

## Templates available

| Template | For notes with `type:` |
|---|---|
| `Concept Template.md` | `concept` |
| `Person Template.md` | `person` |
| `Organization Template.md` | `org` |
| `Paper Template.md` | `paper` |
| `Policy Template.md` | `policy` |
| `Debate Template.md` | `debate` |
| `Event Template.md` | `event` |
| `Case Template.md` | `case` |
| `Dataset Template.md` | `dataset` |
| `Synthesis Template.md` | `synthesis` |
| `MOC Template.md` | `moc` |

## When the template feels wrong

Don't fight it inside one note — instead, propose a template change in a `template:` commit. Templates should serve the corpus, not the other way around.

## What's NOT in the templates

- The Obsidian Templater plugin's `<% %>` syntax. Templates are plain Markdown so they work without plugins.
- Auto-generated IDs. Authors must apply [[ID Conventions]] manually.
- Auto-current dates. Replace `<YYYY-MM-DD>` placeholders with the actual date at creation.
