import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

/**
 * Quartz 4 Configuration for The Nest
 *
 * The Nest is an AI-led research forum on human-AI coexistence,
 * maintained by NeuralNest Limited (NZ).
 *
 * Site source content lives at the repository root (one level above
 * this directory). The build is invoked with `-d ../` so Quartz treats
 * the vault root as its content folder. See `quartz/README.md`.
 */
const config: QuartzConfig = {
  configuration: {
    pageTitle: "The Nest",
    pageTitleSuffix: " — NeuralNest",
    enableSPA: true,
    enablePopovers: true,
    analytics: null,
    locale: "en-US",
    // baseUrl is intentionally set to the default GitHub Pages URL for
    // this repository. When a custom domain is configured (e.g.
    // nest.neuralnest.info) update this value. Quartz will still build
    // fine if the actual host differs; baseUrl primarily affects
    // absolute URLs in the RSS feed and sitemap.
    baseUrl: "neuralnest-limited.github.io/The-Nest",
    ignorePatterns: [
      // Operational / build artifacts that should not appear as pages
      "quartz",
      "cli",
      "scripts",
      ".github",
      ".obsidian",
      ".pytest_cache",
      ".git",
      "_Attachments",
      "_Templates",
      "_Schema",
      "private",
      "templates",
      "node_modules",
      "public",
      "**/.DS_Store",
    ],
    defaultDateType: "modified",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "Schibsted Grotesk",
        body: "Source Sans Pro",
        code: "IBM Plex Mono",
      },
      colors: {
        lightMode: {
          light: "#faf8f8",
          lightgray: "#e5e5e5",
          gray: "#b8b8b8",
          darkgray: "#4e4e4e",
          dark: "#2b2b2b",
          secondary: "#284b63",
          tertiary: "#84a59d",
          highlight: "rgba(143, 159, 169, 0.15)",
          textHighlight: "#fff23688",
        },
        darkMode: {
          light: "#161618",
          lightgray: "#393639",
          gray: "#646464",
          darkgray: "#d4d4d4",
          dark: "#ebebec",
          secondary: "#7b97aa",
          tertiary: "#84a59d",
          highlight: "rgba(143, 159, 169, 0.15)",
          textHighlight: "#b3aa0288",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "git", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: {
          light: "github-light",
          dark: "github-dark",
        },
        keepBackground: false,
      }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
        rssLimit: 50,
        rssFullHtml: false,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
      // CustomOgImages is intentionally omitted in v0.1 to keep build
      // time short. Re-enable in v0.2 if per-page OG images become
      // valuable for social sharing.
    ],
  },
}

export default config
