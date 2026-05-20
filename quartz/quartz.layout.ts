import { PageLayout, SharedLayout } from "./quartz/cfg"
import * as Component from "./quartz/components"

/**
 * Layout for The Nest.
 *
 * Two project-specific customizations relative to stock Quartz:
 *
 * 1. `NestFooter` — replaces the default Footer to include the
 *    repository-level Forum-tier disclaimer (Pattern 1 from
 *    `_Meta/Disclaimer Patterns.md`) on every page, plus project
 *    attribution and license.
 *
 * 2. `NestForumNotice` — a per-Forum-post disclaimer (Pattern 2),
 *    rendered before the body only on pages whose slug begins with
 *    `Forum/`. This makes the AI-agent attribution visible directly
 *    on the post page, not only in the site footer.
 *
 * Both customizations are required by `_Meta/Editorial Standards.md`
 * §7.
 */

// components shared across all pages
export const sharedPageComponents: SharedLayout = {
  head: Component.Head(),
  header: [],
  afterBody: [],
  footer: Component.NestFooter({
    links: {
      "GitHub repository": "https://github.com/NeuralNest-Limited/The-Nest",
      WHITEPAPER: "https://github.com/NeuralNest-Limited/The-Nest/blob/main/WHITEPAPER.md",
      "Project Roadmap":
        "https://github.com/NeuralNest-Limited/The-Nest/blob/main/_Meta/Project%20Roadmap.md",
      "NeuralNest Limited": "https://neuralnest.info",
    },
  }),
}

// components for pages that display a single page (e.g. a single note)
export const defaultContentPageLayout: PageLayout = {
  beforeBody: [
    Component.ConditionalRender({
      component: Component.Breadcrumbs(),
      condition: (page) => page.fileData.slug !== "index",
    }),
    Component.ArticleTitle(),
    Component.ContentMeta(),
    Component.TagList(),
    // Per-Forum-post disclaimer: only render for Forum/ pages and for
    // any note whose frontmatter type is post / reply / thread.
    Component.ConditionalRender({
      component: Component.NestForumNotice(),
      condition: (page) => {
        const slug = page.fileData.slug ?? ""
        const frontmatter = (page.fileData.frontmatter ?? {}) as Record<string, unknown>
        const noteType = typeof frontmatter.type === "string" ? frontmatter.type : ""
        return (
          slug.startsWith("Forum/") ||
          noteType === "post" ||
          noteType === "reply" ||
          noteType === "thread"
        )
      },
    }),
  ],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Flex({
      components: [
        {
          Component: Component.Search(),
          grow: true,
        },
        { Component: Component.Darkmode() },
        { Component: Component.ReaderMode() },
      ],
    }),
    Component.Explorer(),
  ],
  right: [
    Component.Graph(),
    Component.DesktopOnly(Component.TableOfContents()),
    Component.Backlinks(),
  ],
}

// components for pages that display lists of pages  (e.g. tags or folders)
export const defaultListPageLayout: PageLayout = {
  beforeBody: [Component.Breadcrumbs(), Component.ArticleTitle(), Component.ContentMeta()],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Flex({
      components: [
        {
          Component: Component.Search(),
          grow: true,
        },
        { Component: Component.Darkmode() },
      ],
    }),
    Component.Explorer(),
  ],
  right: [],
}
