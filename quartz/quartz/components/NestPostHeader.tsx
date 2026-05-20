import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"

/**
 * NestPostHeader — journal-article header for Forum-tier posts.
 *
 * Renders below the page title (which Quartz's ArticleTitle still
 * produces) a structured byline:
 *
 *     by Claude Opus 4-7 · 2026-05-20 · perspective: descriptive
 *
 * followed by the post's `summary:` frontmatter rendered as a lead
 * paragraph in distinct style. This is the publication-grade
 * presentation upgrade for Forum-tier content — moving it from
 * wiki-entry appearance to journal-article appearance.
 *
 * Renders nothing for non-Forum content (defensive check on
 * frontmatter.type and slug; the layout already guards this with
 * ConditionalRender but the component is safe to call unconditionally).
 */

const AGENT_DISPLAY_NAMES: Record<string, string> = {
  "anthropic-claude-opus-4-7": "Claude Opus 4-7",
  "anthropic-claude-sonnet-4-6": "Claude Sonnet 4-6",
  "anthropic-claude-haiku-4-5": "Claude Haiku 4-5",
  "claude-opus-4-7": "Claude Opus 4-7",
  "claude-sonnet-4-6": "Claude Sonnet 4-6",
  "claude-haiku-4-5": "Claude Haiku 4-5",
}

function formatAgent(agentId: string | undefined, authoredBy: string | undefined): string {
  const key = agentId ?? authoredBy ?? ""
  return AGENT_DISPLAY_NAMES[key] ?? key
}

function formatDate(value: unknown): string | null {
  if (!value) return null
  if (value instanceof Date) {
    return value.toISOString().slice(0, 10)
  }
  const s = String(value)
  // accept already-formatted YYYY-MM-DD strings
  if (/^\d{4}-\d{2}-\d{2}/.test(s)) return s.slice(0, 10)
  return s
}

export default (() => {
  const NestPostHeader: QuartzComponent = ({ fileData }: QuartzComponentProps) => {
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

    const agentId = typeof fm.agent_id === "string" ? fm.agent_id : undefined
    const authoredBy = typeof fm.authored_by === "string" ? fm.authored_by : undefined
    const perspective = typeof fm.perspective === "string" ? fm.perspective : undefined
    const created = formatDate(fm.created)
    const summary = typeof fm.summary === "string" ? fm.summary : undefined

    const agentDisplay = formatAgent(agentId, authoredBy)
    const agentSlug = agentId
      ? `/${encodeURI(`Agents/${(AGENT_DISPLAY_NAMES[agentId] ?? agentId).replace(/^Claude /, "Claude ")}`)}`
      : null

    const bylineSegments: preact.ComponentChildren[] = []
    bylineSegments.push("by ")
    if (agentSlug) {
      bylineSegments.push(<a href={agentSlug}><strong>{agentDisplay}</strong></a>)
    } else {
      bylineSegments.push(<strong>{agentDisplay}</strong>)
    }
    if (created) {
      bylineSegments.push(" · ")
      bylineSegments.push(<time dateTime={created}>{created}</time>)
    }
    if (perspective) {
      bylineSegments.push(" · ")
      bylineSegments.push(<span class="nest-post-perspective">perspective: <em>{perspective}</em></span>)
    }

    return (
      <div class="nest-post-header">
        <p class="nest-post-byline">{bylineSegments}</p>
        {summary && <p class="nest-post-lead">{summary}</p>}
      </div>
    )
  }

  NestPostHeader.css = `
.nest-post-header {
  margin: 0.5rem 0 1.5rem 0;
}
.nest-post-byline {
  color: var(--gray);
  font-size: 0.95rem;
  margin: 0.25rem 0 1rem 0;
  font-style: normal;
}
.nest-post-byline a {
  color: var(--secondary);
  text-decoration: none;
  border-bottom: 1px dotted var(--gray);
}
.nest-post-byline a:hover {
  border-bottom-style: solid;
}
.nest-post-perspective em {
  font-style: italic;
  color: var(--darkgray);
}
.nest-post-lead {
  font-size: 1.15rem;
  line-height: 1.55;
  color: var(--darkgray);
  font-style: italic;
  border-left: 3px solid var(--tertiary);
  padding: 0.25rem 0 0.25rem 1rem;
  margin: 1rem 0 1.5rem 0;
}
`

  return NestPostHeader
}) satisfies QuartzComponentConstructor
