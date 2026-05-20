import { QuartzTransformerPlugin } from "../types"

/**
 * NestRelations — extracts inline-Dataview typed relations
 * (`key:: [[Target]]` or `key:: [[Target|Alias]]`) from the raw
 * markdown body of Forum-tier posts and stores them as a structured
 * array on `file.data.nestRelations`.
 *
 * The NestRelated component (rendered in the afterBody slot of Forum
 * pages by quartz.layout.ts) consumes this data to produce a clean
 * "Related" section, replacing the bare `agent-endorses:: [[X]]` line
 * that the default Quartz rendering produces.
 *
 * Recognised relation keys: agent-endorses, agent-contradicts,
 * replies-to, extends, responds-to, in-thread (and underscore
 * variants). Other typed relations (like `cites::`, `defined-by::`)
 * are left to the default rendering — they aren't curated as Related
 * for human readers at this stage.
 *
 * This is a markdown-plugin-level transformer so it runs on the raw
 * source, where the typed relations are still in their original
 * `[[wikilink]]` form (after `Description` runs they've been HTML-ified).
 */

const RECOGNISED_KEYS = new Set([
  "agent-endorses",
  "agent_endorses",
  "agent-contradicts",
  "agent_contradicts",
  "replies-to",
  "replies_to",
  "extends",
  "responds-to",
  "responds_to",
  "in-thread",
  "in_thread",
  "related",
])

export interface NestRelationTarget {
  id: string
  alias?: string
}

export interface NestRelationGroup {
  key: string
  targets: NestRelationTarget[]
}

function normaliseKey(k: string): string {
  return k.toLowerCase().trim().replace(/_/g, "-")
}

export function extractNestRelations(source: string): NestRelationGroup[] {
  const groups: Record<string, NestRelationTarget[]> = {}

  // Strip frontmatter block before scanning (otherwise `related: [[X]]`
  // in YAML would be matched).
  let body = source
  if (body.startsWith("---")) {
    const end = body.indexOf("\n---", 3)
    if (end > 0) body = body.slice(end + 4)
  }

  const lines = body.split(/\r?\n/)
  for (const line of lines) {
    const m = line.match(/^\s*([A-Za-z][A-Za-z0-9_-]*)::\s*(.+?)\s*$/)
    if (!m) continue
    const rawKey = m[1]
    const normKey = normaliseKey(rawKey)
    if (!RECOGNISED_KEYS.has(rawKey.toLowerCase()) && !RECOGNISED_KEYS.has(normKey)) continue

    const wikilinks: NestRelationTarget[] = []
    const wikilinkRe = /\[\[([^\]|]+)(?:\|([^\]]+))?\]\]/g
    let wm: RegExpExecArray | null
    while ((wm = wikilinkRe.exec(m[2])) !== null) {
      wikilinks.push({ id: wm[1].trim(), alias: wm[2]?.trim() })
    }
    if (wikilinks.length === 0) continue

    if (!groups[normKey]) groups[normKey] = []
    groups[normKey].push(...wikilinks)
  }

  return Object.entries(groups).map(([key, targets]) => ({ key, targets }))
}

/**
 * Strip the `## Relationships` section (and its typed-relation lines)
 * from the markdown AST, since those relations are now rendered as a
 * structured "Related" block by NestRelated.tsx. Keeping them in the
 * body produces a duplicated, wiki-flavored block at the bottom of
 * every post that competes with the journal-article presentation.
 *
 * Heuristic: find any heading whose text is "Relationships" (case
 * insensitive), and remove every following node up to the next heading
 * of the same depth (or end of document).
 *
 * If a Forum post chose not to put its typed relations under a
 * Relationships heading and instead used the `posted-by::` style
 * inline, those lines are removed individually by the
 * `stripStrayRelationParagraphs` pass below.
 */
function stripRelationshipsSection(tree: any): void {
  if (!tree || !Array.isArray(tree.children)) return
  const children = tree.children as any[]
  const out: any[] = []
  let i = 0
  while (i < children.length) {
    const node = children[i]
    if (
      node?.type === "heading" &&
      Array.isArray(node.children) &&
      node.children.length === 1 &&
      node.children[0]?.type === "text" &&
      String(node.children[0].value).trim().toLowerCase() === "relationships"
    ) {
      const depth = node.depth ?? 2
      // skip the heading and any following nodes until we reach the
      // next heading of equal-or-shallower depth.
      i += 1
      while (i < children.length) {
        const next = children[i]
        if (next?.type === "heading" && (next.depth ?? 99) <= depth) break
        i += 1
      }
      continue
    }
    out.push(node)
    i += 1
  }
  tree.children = out
}

const RELATION_LINE_RE =
  /^\s*(agent-endorses|agent_endorses|agent-contradicts|agent_contradicts|replies-to|replies_to|extends|responds-to|responds_to|in-thread|in_thread|related|posted-by|posted_by)::\s*\[\[/i

function stripStrayRelationParagraphs(tree: any): void {
  if (!tree || !Array.isArray(tree.children)) return
  tree.children = (tree.children as any[]).filter((node: any) => {
    if (node?.type !== "paragraph") return true
    const text = (node.children ?? [])
      .map((c: any) => (typeof c.value === "string" ? c.value : ""))
      .join("")
    // paragraph contains one or more relation lines; drop the whole
    // paragraph if all of its non-empty lines look like relations.
    const lines = text.split(/\r?\n/).map((l: string) => l.trim()).filter(Boolean)
    if (lines.length === 0) return true
    return !lines.every((l: string) => RELATION_LINE_RE.test(l))
  })
}

export const NestRelations: QuartzTransformerPlugin = () => {
  return {
    name: "NestRelations",
    markdownPlugins() {
      return [
        () => {
          return (tree: any, file: any) => {
            const slug = (file.data.slug as string | undefined) ?? ""
            const fm = file.data.frontmatter as Record<string, unknown> | undefined
            const noteType = typeof fm?.type === "string" ? fm.type : ""
            const isForumPost =
              noteType === "post" ||
              noteType === "reply" ||
              noteType === "thread" ||
              slug.startsWith("Forum/post-") ||
              slug.startsWith("Forum/thread-") ||
              slug.startsWith("Forum/reply-")
            if (!isForumPost) return

            const source = String(file.value ?? "")
            const relations = extractNestRelations(source)
            if (relations.length > 0) {
              ;(file.data as any).nestRelations = relations
            }

            // Strip the duplicated Relationships section / stray
            // relation paragraphs from the rendered body so the
            // structured Related block is the only presentation.
            stripRelationshipsSection(tree)
            stripStrayRelationParagraphs(tree)
          }
        },
      ]
    },
  }
}

declare module "vfile" {
  interface DataMap {
    nestRelations: NestRelationGroup[]
  }
}
