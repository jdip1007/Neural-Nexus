# Neural Nexus Schema

## Domain
Multi-domain knowledge base: AI/ML, biotechnology, finance, psychology, devops, personal notes.

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
- **Updates**: Always bump the `updated` date when modifying page content
- **Catalog**: Every new page is added to `index-catalog.md` by `scripts/generate-catalog.js`
- **Log**: Append every action to `log.md`
- **Raw sources**: Never modify files in `raw/` — they are immutable. Corrections go in wiki pages.

## Frontmatter Template

```
---
title: Page Title
created: 2026-07-18
updated: 2026-07-18
type: entity | concept | idea | finding | reading | comparison
domain: ai | biotech | finance | devops | psychology | general
tags: [tag1, tag2]
sources: [raw/articles/source-name.md]
confidence: high | medium | low
status: draft | active | archived
backlinks: []  # auto-computed by build-graph.js, do not edit manually
---
```

### Raw Source Frontmatter

```
---
source_url: https://example.com/article
source_type: article | video | chat | file
ingested: 2026-07-18
sha256: <hex digest of body content below frontmatter>
---
```

The `sha256:` enables change detection on re-ingest. Skip processing if identical, flag drift if changed.

## Tag Taxonomy

Tags must come from this taxonomy. Add new tags here first, then use them.

### Domains
- ai, ml, llm, deep-learning, nlp, computer-vision
- biotech, genomics, dna, nanotechnology, synthetic-biology
- finance, trading, economics, cryptocurrency, risk-management
- devops, infrastructure, security, reliability, monitoring
- psychology, neuroscience, cognitive-science, behavior
- hermes, automation, workflow, knowledge-management

### Topics
**AI/ML**: architecture, training, inference, alignment, safety, evaluation, fine-tuning
**Biotech**: sequencing, crispr, protein-design, drug-discovery
**Finance**: markets, portfolio, analysis, algorithmic-trading
**DevOps**: kubernetes, ci-cd, observability, site-reliability
**Psychology**: learning, decision-making, therapy, cognitive-bias

### Meta
- research, opinion, tutorial, reference, news, analysis, comparison

## Content Types

### Ideas
- **Purpose**: Raw thoughts, brainstorming, unprocessed notes
- **Threshold**: No minimum — create for any thought worth keeping
- **Structure**: Quick bullets, minimal structure
- **Example**: "Idea for optimizing RAG retrieval with hierarchical clustering"

### Findings
- **Purpose**: Processed insights from research/analysis
- **Threshold**: Create when processing reveals novel insight
- **Structure**: Problem → Analysis → Conclusion → Sources
- **Example**: "Video analysis revealed 3 key patterns in agent workflows"

### Readings
- **Purpose**: Summaries of books, papers, videos
- **Threshold**: Create one for every ingested source
- **Structure**: Title, source, key points, quotes, related pages
- **Example**: "LLM Wiki video notes with 5 key takeaways"

### Entities
- **Purpose**: People, organizations, tools, projects
- **Threshold**: Mentioned in 2+ sources OR central to 1 source
- **Structure**: Overview, key facts, relationships, sources
- **Example**: "Andrej Karpathy — AI researcher, former Tesla Autopilot director"

### Concepts
- **Purpose**: Technical concepts, theories, frameworks
- **Threshold**: Explained in depth OR appears in 3+ sources
- **Structure**: Definition, current state, open questions, related concepts
- **Example**: "Transformer architecture — self-attention, multi-head, positional encoding"

### Comparisons
- **Purpose**: Side-by-side analyses
- **Threshold**: Whenever comparing 2+ items
- **Structure**: What compared, dimensions, verdict, sources
- **Example**: "Obsidian vs Notion vs Roam Research"

## Page Creation Rules

1. **Ideas**: No minimum threshold — create freely
2. **Readings**: One per source — always create
3. **Entities**: 2+ source mentions OR central to 1 source
4. **Concepts**: Deep explanation OR 3+ source appearances
5. **Findings**: Novel insight from processing
6. **Comparisons**: When analyzing 2+ items

## Update Policy

When new information conflicts with existing content:
1. Check dates — newer sources generally supersede older ones
2. If genuinely contradictory, note both positions with dates and sources
3. Mark in frontmatter: `contradictions: [page-name]`
4. Flag for user review during lint

## Quality Signals

- **confidence**: high (well-supported across sources), medium (some support), low (single source or opinion)
- **contested**: true when unresolved contradictions exist
- **status**: draft (new/unpolished), active (stable), archived (superseded)

## Page Size
- **Target**: 50–150 lines per page
- **Split**: When exceeding 200 lines — break into sub-topics with cross-links
- **Archive**: Move to `_archive/` when fully superseded