---
classification: systems.knowledge-systems
confidence: high
created: 2026-07-18
domain: hermes
reviewed: 2026-07-18
sources: []
status: active
tags:
- general
title: Neural Nexus
type: concept
updated: 2026-07-18
---



# Neural Nexus

## Definition

Neural Nexus is a personal knowledge base system that combines LLM Wiki semantic structuring, Obsidian-style wikilink navigation, MkDocs Material web interface, and Hermes Agent automation — all hosted free on GitHub Pages.

## Architecture

Three-layer structure:

1. **Raw Sources** (`raw/`): Immutable source material — articles, video transcripts, chat logs
2. **Wiki Pages** (`concepts/`, `entities/`, `ideas/`, `findings/`, `readings/`, `comparisons/`): Processed knowledge
3. **Schema** (`SCHEMA.md`): Structure conventions, tag taxonomy, page creation rules

## Key Features

- 6 content types with creation thresholds
- `wikilink` interlinking (Obsidian-style, server-side rendering via MkDocs hook)
- Interactive D3.js knowledge graph
- Full-text search
- Citation enforcement (readings/findings must cite sources)
- Review tracking (periodic truth/validity checks via `reviewed` field)
- Active link discovery (finds missing connections between pages)
- Automated ingestion via Hermes Agent
- Free GitHub Pages hosting with CI/CD

## Maintenance

- **Daily**: RSS ingestion via cron
- **Weekly**: Lint + link discovery + auto-apply high-confidence suggestions
- **Monthly**: Truth/validity review of stale pages, archive old drafts
- **On push**: CI runs lint → build graph → build catalog → MkDocs build → deploy

## Related

- [About Neural Nexus](concepts/neural-nexus.md)
- [Knowledge Preservation](concepts/knowledge-preservation.md)
- [Reproducibility Crisis](concepts/reproducibility-crisis.md)
- [molecular-biology](concepts/molecular-biology.md)

## Related Pages

- [concepts/molecular-biology](concepts/molecular-biology.md)
- [references/setup-guide](references/setup-guide.md)
- [references/writing-guide](references/writing-guide.md)


## See also

- [[architecture]]
- [[knowledge-preservation]]
- [[reproducibility-crisis]]