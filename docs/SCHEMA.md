# Neural Nexus Schema

## Domain
Multi-domain knowledge base: AI/ML, biotechnology, finance, psychology, devops, personal notes

## Conventions
- **File names**: lowercase, hyphens, no spaces (e.g., `transformer-architecture.md`)
- **Frontmatter**: Every page must have YAML frontmatter (see below)
- **Wikilinks**: Use `[[page-name]]` for internal links (Obsidian-style)
  - Internal page: `[[page-name]]`
  - Link to header: `[[page-name#Header]]`
  - Custom text: `[[page-name|display text]]`
  - External URL: `[text](https://example.com/)`
  - Minimum 2 outbound `[[wikilinks]]` per page
- **Citations**: All pages derived from external material MUST cite sources
  - Frontmatter `sources:` field: list raw source files (e.g., `sources: [raw/articles/source.md]`)
  - Inline provenance: `^[raw/articles/source.md]` at paragraph level for specific claims
  - Readings and findings: MUST have sources (lint error if missing)
  - Concepts, entities, comparisons: SHOULD have sources when derived from material (lint warning)
  - Ideas: sources optional (original thoughts)
  - External URLs in prose should be captured to `raw/` and cited, not left as bare links
- **Updates**: Always bump `updated` date when modifying
- **Catalog**: Add every new page to `index-catalog.md`
- **Log**: Append every action to `log.md`
- **Raw sources**: Never modify files in `raw/` — they are immutable. Corrections go in wiki pages.

## Frontmatter Template

```yaml
---
title: Page Title
created: 2026-07-18
updated: 2026-07-18
type: entity | concept | idea | finding | reading | comparison
classification: category.subcategory[.subsubcategory]  # required for concept/entity
domain: ai | biotech | finance | devops | psychology | general
tags: [from taxonomy below]
sources: [raw/articles/source-name.md]
confidence: high | medium | low
status: draft | active | archived
reviewed: 2026-07-18
backlinks: []
---
```

### Raw Source Frontmatter

```yaml
---
source_url: https://example.com/article
source_type: article | video | podcast | paper | book
author: Author Name
publication_date: 2026-07-18
ingested_date: 2026-07-18
transcript_available: true
---
```

## Classification System

### Entity Classification Reference

|| Classification | Pages ||
||---|---||
|| `person.researcher` | penn-rainford ||
|| `person.legal-figure` | lam-kwok-wai-tuen-mun-rapist ||
|| `person.media-figure` | x-television-celebrity ||
|| `organization.insurance-provider` | bowtie-insurance ||

### Domain Classification

|| Domain | Subcategories ||
||---|---||
|| `ai` | ml, nlp, computer-vision, robotics, ethics ||
|| `biotech` | genetics, molecular-biology, bioinformatics, diagnostics ||
|| `finance` | investing, trading, economics, risk-management ||
|| `psychology` | cognitive-science, mental-health, therapy ||
|| `devops` | infrastructure, security, automation, monitoring ||
|| `general` | cross-domain, interdisciplinary ||

### Content Type Classification

|| Type | Description | Examples ||
||---|---|---||
|| `entity` | People, organizations, tools, projects | Andrej Karpathy, Tesla, PyTorch ||
|| `concept` | Technical concepts, theories, frameworks | Transformer architecture, attention mechanism ||
|| `idea` | Raw thoughts, brainstorming, unprocessed notes | Idea for optimizing RAG retrieval ||
|| `finding` | Processed insights from research/analysis | Video analysis revealed 3 key patterns ||
|| `reading` | Summaries of books, papers, videos | LLM Wiki video notes with 5 key takeaways ||
|| `comparison` | Side-by-side analyses | Obsidian vs Notion vs Roam Research ||

## Taxonomy

### Core Topics
youtube
youtube-creator
educational-content
content-creation
internet-culture
youtube-algorithm
digital-media
digital-society
mental-health
digital-marketing
wellness
online-controversy
digital-analysis
internet-anarchist
daves-garage
tutorial

### Technology & Programming
programming
technology
algorithm
gaming
slot-machine
automotive
hardware
software
networking

### Business & Finance
finance
money
investing
economics
business
market
risk
portfolio
diversification
inflation
privacy

### Health & Psychology
healthy-gamer-gg
mental_health
therapy
psychology
relationships
self_improvement
anxiety
depression
mindfulness

### Philosophy & Society
philosophy
society
social-media
current-events
ethics

### Science & Research
science
research
technology-impact
ai
artificial-intelligence
technology-ethics

### Media & Entertainment
podcast
video-summary
discussion
debate
entertainment
media

## Page Creation Rules

1. **Ideas**: No minimum threshold - create freely
2. **Readings**: One per source - always create
3. **Entities**: 2+ source mentions OR central to 1 source
4. **Concepts**: Deep explanation OR 3+ source appearances
5. **Findings**: Novel insight from processing
6. **Comparisons**: When analyzing 2+ items

## Update Policy

When new information conflicts with existing content:
1. Check dates - newer sources supersede older
2. If contradictory, note both with dates and sources
3. Mark in frontmatter: `contradictions: [page-name]`
4. Flag for user review during lint

## Quality Signals

- **confidence**: high (well-supported across sources), medium (some support), low (single source or opinion)
- **contested**: true when unresolved contradictions exist
- **status**: draft (new/unpolished), active (stable), archived (superseded)
- **reviewed**: ISO date of last truth/validity check. Update after verifying page content against current sources. Lint flags pages not reviewed in 180 days, or updated after last review.

## Review Process

Periodically (at least every 6 months), review each active page:
1. Re-read the page and its cited sources
2. Check if information is still accurate / current
3. Check for contradictions with newer pages
4. Update content if needed, bump `updated` date
5. Set `reviewed: YYYY-MM-DD` (today's date)
6. If page is no longer accurate and can't be fixed → set `status: archived`

The lint script enforces this:
- Active pages without `reviewed` → warning
- Pages where `updated > reviewed` → warning (content changed since last review)
- Pages not reviewed in 180+ days → info

## Copyright

Raw source files in `raw/` may contain copyrighted material. Rules:
- Raw sources are for personal research use only — not redistributed via the public GitHub Pages site
- The published wiki pages (concepts, entities, etc.) contain synthesis and quotes under fair use
- When quoting, keep quotes short (<100 words) and always cite the source
- If you receive a takedown request, remove the raw source immediately
- Do not reproduce full articles — summarize and quote selectively

## Page Size

Maintain reasonable page sizes:
- **Maximum**: 10,000 words per page
- **Optimal**: 2,000-5,000 words
- **Split**: If exceeding maximum, split into logical subpages
- **Navigation**: Use `[[wikilinks]]` to connect related content

## Tag Usage Guidelines

1. **Use specific tags** - Choose the most specific tag that applies to your content
2. **Use multiple tags** - Content can have multiple relevant tags
3. **Follow naming conventions** - Use lowercase with hyphens for multi-word tags
4. **Avoid custom tags** - Use only tags defined in this schema
5. **Update schema** - When adding new tags, update this document

## Maintenance

This schema should be updated as new content categories emerge and the knowledge base grows.