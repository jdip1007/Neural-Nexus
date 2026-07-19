---
title: Neural Nexus
created: 2026-07-18
updated: 2026-07-18
type: concept
classification: systems.knowledge-systems
domain: hermes
tags: [knowledge-management, workflow, automation]
sources: []
confidence: high
status: active
reviewed: 2026-07-18
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
- `[[wikilink]]` interlinking (Obsidian-style, server-side rendering via MkDocs hook)
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

- [[neural-nexus|About Neural Nexus]]
- [[knowledge-preservation|Knowledge Preservation]]
- [[reproducibility-crisis|Reproducibility Crisis]]
