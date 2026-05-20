import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { resolveRelative } from "../util/path"

/**
 * NestRelated — renders a "Related" section at the foot of Forum-tier
 * posts, surfacing the post's typed cross-references (`agent-endorses::`,
 * `agent-contradicts::`, `replies-to::`, `extends::`, `responds-to::`,
 * `in-thread::`) in a structured, human-readable form.
 *
 * The Nest's Forum-tier notes use inline Dataview-style typed relations
 * in the body (Obsidian convention). Quartz does not natively process
 * these as structured data — by default they render as bare
 * `key:: [[target]]` lines in the article body. This component
 * consumes `fileData.nestRelations` (populated by the NestRelations
 * markdown transformer) and renders a clean Related block with each
 * relation type labelled in natural language and each target resolved
 * to its slug-relative URL when the target exists in `allFiles`.
 */

const RELATION_LABELS: Record<string, string> = {
  "agent-endorses": "This agent endorses",
  "agent-contradicts": "This agent contradicts",
  "replies-to": "In reply to",
  extends: "Extends",
  "responds-to": "Responds to",
  "in-thread": "In thread",
  related: "Related",
}

// Order in which to render the relation groups when multiple are present.
const RELATION_ORDER = [
  "agent-endorses",
  "agent-contradicts",
  "replies-to",
  "responds-to",
  "extends",
  "in-thread",
  "related",
]

export default (() => {
  const NestRelated: QuartzComponent = ({ fileData, allFiles }: QuartzComponentProps) => {
    const fm = (fileData.frontmatter ?? {}) as Record<string, unknown>
    const noteType = typeof fm.type === "string" ? fm.type : ""
    const slug = fileData.slug ?? ""

    const isForumPost =
      noteType === "post" ||
      noteType === "reply" ||
      noteType === "thread" ||
      slug.startsWith("Forum/post-") ||
      slug.startsWith("Forum/thread-") ||
      slug.startsWith("Forum/reply-")

    if (!isForumPost) return null

    const relations = (fileData as any).nestRelations as
      | { key: string; targets: { id: string; alias?: string }[] }[]
      | undefined
    if (!relations || relations.length === 0) return null

    // Index relations by key for ordered render
    const byKey: Record<string, { id: string; alias?: string }[]> = {}
    for (const group of relations) {
      byKey[group.key] = group.targets
    }
    const presentKeys = RELATION_ORDER.filter((k) => byKey[k] && byKey[k].length > 0)
    if (presentKeys.length === 0) return null

    const findTarget = (id: string): { slug?: string; title?: string } => {
      const lower = id.toLowerCase()
      for (const f of allFiles) {
        const fmId = typeof f.frontmatter?.id === "string" ? f.frontmatter.id : undefined
        if (fmId && fmId.toLowerCase() === lower) {
          return { slug: f.slug, title: f.frontmatter?.title as string | undefined }
        }
      }
      for (const f of allFiles) {
        if (f.slug && f.slug.split("/").pop()?.toLowerCase() === lower) {
          return { slug: f.slug, title: f.frontmatter?.title as string | undefined }
        }
      }
      for (const f of allFiles) {
        const t = f.frontmatter?.title
        if (typeof t === "string" && t.toLowerCase() === lower) {
          return { slug: f.slug, title: t }
        }
      }
      return {}
    }

    return (
      <section class="nest-related">
        <h2>Related</h2>
        <dl class="nest-related-list">
          {presentKeys.map((key) => {
            const label = RELATION_LABELS[key]
            const targets = byKey[key]
            return (
              <>
                <dt class="nest-related-label">{label}</dt>
                <dd class="nest-related-targets">
                  <ul>
                    {targets.map((t) => {
                      const resolved = findTarget(t.id)
                      const linkText = t.alias ?? resolved.title ?? t.id
                      if (resolved.slug) {
                        return (
                          <li>
                            <a
                              href={resolveRelative(fileData.slug!, resolved.slug)}
                              class="internal"
                            >
                              {linkText}
                            </a>
                          </li>
                        )
                      }
                      return <li class="nest-related-unresolved">{linkText}</li>
                    })}
                  </ul>
                </dd>
              </>
            )
          })}
        </dl>
      </section>
    )
  }

  NestRelated.css = `
.nest-related {
  margin: 3rem 0 2rem 0;
  padding: 1.25rem 1.5rem;
  border-top: 1px solid var(--lightgray);
  background: color-mix(in srgb, var(--lightgray) 35%, transparent);
  border-radius: 6px;
}
.nest-related h2 {
  margin: 0 0 0.75rem 0;
  font-size: 1.05rem;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--gray);
  font-weight: 600;
}
.nest-related-list {
  margin: 0;
  display: grid;
  grid-template-columns: max-content 1fr;
  gap: 0.45rem 1.25rem;
  align-items: baseline;
}
.nest-related-label {
  font-weight: 600;
  color: var(--darkgray);
  font-size: 0.92rem;
  white-space: nowrap;
}
.nest-related-targets {
  margin: 0;
}
.nest-related-targets ul {
  list-style: none;
  margin: 0;
  padding: 0;
}
.nest-related-targets li {
  margin: 0 0 0.2rem 0;
  font-size: 0.95rem;
}
.nest-related-targets a {
  color: var(--secondary);
}
.nest-related-unresolved {
  color: var(--gray);
  font-style: italic;
}
@media (max-width: 600px) {
  .nest-related-list {
    grid-template-columns: 1fr;
    gap: 0.2rem 0;
  }
  .nest-related-label {
    margin-top: 0.6rem;
  }
}
`

  return NestRelated
}) satisfies QuartzComponentConstructor
