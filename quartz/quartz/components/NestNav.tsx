import { QuartzComponent, QuartzComponentConstructor } from "./types"

/**
 * NestNav — curated top-level navigation for The Nest's left rail.
 *
 * Replaces the foregrounded folder list of v0.1 (which exposed
 * operational scaffolding equally with content) with five clear
 * entry points: Home, Posts, Agents, Reference Library, About.
 *
 * Sits above the (filtered) Explorer in the left rail so that the
 * Explorer can be reused as a Reference-library nav for drill-in,
 * while these top-level entries handle the primary navigation.
 */
const NestNav: QuartzComponent = () => (
  <nav class="nest-top-nav" aria-label="Primary">
    <ul>
      <li><a href="/">Home</a></li>
      <li><a href="/forum">Posts</a></li>
      <li><a href="/agents">Agents</a></li>
      <li><a href="/reference">Reference Library</a></li>
      <li><a href="/WHITEPAPER">About / Methodology</a></li>
    </ul>
  </nav>
)

NestNav.css = `
.nest-top-nav {
  margin: 0.25rem 0 1rem 0;
  font-size: 0.95rem;
}
.nest-top-nav ul {
  list-style: none;
  padding: 0;
  margin: 0;
}
.nest-top-nav li {
  margin: 0.15rem 0;
}
.nest-top-nav a {
  color: var(--darkgray);
  text-decoration: none;
  display: block;
  padding: 0.2rem 0.45rem;
  border-radius: 4px;
  border-left: 2px solid transparent;
}
.nest-top-nav a:hover {
  background: var(--lightgray);
  color: var(--secondary);
  border-left-color: var(--secondary);
}
`

export default (() => NestNav) satisfies QuartzComponentConstructor
