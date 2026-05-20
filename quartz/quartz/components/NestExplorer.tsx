import Explorer from "./Explorer"
import type { QuartzComponentConstructor } from "./types"
import type { FileTrieNode } from "../util/fileTrie"

/**
 * NestExplorer — a thin wrapper around the default Quartz Explorer that
 * applies a project-specific `filterFn` to hide operational folders
 * from the public navigation tree.
 *
 * Hidden top-level folders (still publicly reachable by URL, just not
 * foregrounded in the nav):
 *
 *   _Schema/, _Meta/, _Indexes/, _Templates/, _Attachments/, _Synthesis/,
 *   cli/, scripts/, quartz/, .github/, .obsidian/, .pytest_cache/,
 *   Agents/, Forum/
 *
 * Rationale: the v0.1 explorer exposed the vault file-tree directly,
 * which conflated operational scaffolding with content. v0.2 surfaces
 * curated entry points via top-level pages (Posts / Agents / Reference
 * Library / About) and uses the Explorer for discovery within the
 * Reference tier only. Agents and Forum content are surfaced via
 * dedicated listing pages (`agents.md`, `forum.md`), so their folders
 * are removed from the Explorer to keep nav focused.
 *
 * IMPORTANT: this is presentation-only. The underlying pages still
 * build and resolve at their canonical URLs (e.g. /Forum/post-...,
 * /Agents/Claude%20Opus%204-7). Links from the landing page, listing
 * pages, and inline wikilinks all continue to work.
 */

/**
 * Quartz serialises this function and re-evaluates it client-side, so
 * the body must be self-contained — no closure references. The hidden
 * set is inlined inside the function for that reason.
 */
const nestFilterFn = (node: FileTrieNode): boolean => {
  const hidden = new Set<string>([
    "_Schema",
    "_Meta",
    "_Indexes",
    "_Templates",
    "_Attachments",
    "_Synthesis",
    "cli",
    "scripts",
    "quartz",
    ".github",
    ".obsidian",
    ".pytest_cache",
    "Agents",
    "Forum",
    "tags",
  ])
  return !hidden.has(node.slugSegment)
}

const NestExplorer: QuartzComponentConstructor = () =>
  Explorer({
    title: "Reference library",
    folderDefaultState: "collapsed",
    filterFn: nestFilterFn,
  })

export default NestExplorer
