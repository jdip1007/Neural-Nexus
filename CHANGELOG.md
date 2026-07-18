# Changelog

All notable changes to the Neural Nexus platform (scripts, schema, templates, configuration) are documented here.

The wiki content log (`docs/log.md`) tracks knowledge base operations (ingest, review, lint). This file tracks **platform** changes — updates to the tools that run the wiki.

Format: `## [YYYY-MM-DD] — Category`

Categories: Added, Changed, Fixed, Removed, Security, Maintenance

---

## [2026-07-18] — Initial Release

### Added
- MkDocs Material site with dark/light mode, search, tags, git-revision-date
- 6 content types: concept, entity, idea, finding, reading, comparison
- `[[wikilink]]` rendering via server-side MkDocs hook (`docs/hooks/wikilinks.py`)
- D3.js interactive knowledge graph with click-to-navigate
- Build scripts (zero npm deps):
  - `scripts/lib.js` — shared utilities (frontmatter parsing, wikilink extraction, tag taxonomy loader)
  - `scripts/build-graph.js` — graph data builder with 3-tier fuzzy wikilink resolution + collision detection
  - `scripts/generate-catalog.js` — auto-generates index-catalog.md
  - `scripts/lint-wiki.js` — health checker (frontmatter, citations, broken links, orphans, review status, missing links)
  - `scripts/suggest-links.js` — standalone link discovery engine (text mention, shared source, tag overlap)
- GitHub Actions CI/CD (lint → build graph → build catalog → mkdocs build → deploy)
- Page templates for all 6 content types
- Writing guide (`docs/references/writing-guide.md`)
- SCHEMA.md with tag taxonomy, citation rules, review process, copyright policy
- `reviewed` frontmatter field for periodic truth/validity tracking
- Citation enforcement (readings/findings MUST have sources; lint errors if missing)
- Active link discovery (finds missing connections between pages)
- Obsidian vault compatibility (free sync via Git, no paid Obsidian Sync required)
- Setup guide (`docs/references/setup-guide.md`)
- This changelog

### Decisions
- **MkDocs Material** over raw HTML — search, theming, plugins, responsive
- **Server-side wikilink hook** over client-side JS — works with search/sitemap, no fragile post-processing
- **Zero npm dependencies** — scripts use only Node.js built-in modules, no `package.json` needed
- **Official `actions/deploy-pages@v4`** over `peaceiris/actions-gh-pages` — future-proof
- **Lint runs in CI before deploy** — broken pages never reach production
- **Tags loaded from SCHEMA.md at runtime** — no hardcoded tag list in scripts
