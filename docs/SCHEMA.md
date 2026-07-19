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
source_type: article | video | chat | file
ingested: 2026-07-18
sha256: <hex digest of body content>
---
```

## Tag Taxonomy

### Domains
- ai, ml, llm, deep-learning, nlp, computer-vision, gemini, generative-ai
- biotech, genomics, dna, nanotechnology, synthetic-biology
- finance, trading, economics, cryptocurrency, risk-management
- devops, infrastructure, security, reliability, monitoring
- psychology, neuroscience, cognitive-science, behavior
- hermes, automation, workflow, knowledge-management

### Topics

- architecture, training, inference, alignment, safety, evaluation, fine-tuning, automation, multimodal
- bioinformatics, computational-biology, sequencing, data-science
- crispr, protein-design, drug-discovery, reproducibility, dna-extraction, molecular-biology, laboratory-technique
- cell-biology, tissue-culture, genomics, dna-sequencing, long-read-sequencing, nanopore-sequencing, tissue-preparation
- liquid-biopsy, diagnostics, microbiology, ecology, environmental-science, biotechnology, biology, biochemistry
- genetics, biodiversity, conservation, ecosystems, cell-line, pcr, quality-control
- markets, portfolio, analysis, algorithmic-trading
- kubernetes, ci-cd, observability, site-reliability
- learning, decision-making, therapy, cognitive-bias, criminal-behavior, forensic-psychology
- hong-kong, media-ethics, celebrity-privacy, blackmail, legal-science, forensic-science, dna-evidence
- criminal-justice, crime-investigation, legal-cases, dangerous-person-2-0, dangerous-person-2.0
- celebrity, television-personality, blackmail-victim, serial-offender, criminal
- research-methodology, youtube-research, qgn-method, prompt-engineering, fine-tuning, model-comparison

### Meta
- research, opinion, tutorial, reference, news, analysis, comparison, setup, writing, documentation, guide, knowledge-base, sustainability, validation, scientific-method, researcher, computer-science, research-tools, ai, open-science, reproducibility-crisis, research-crisis, reproducibility

**Rule**: Every tag must appear in this taxonomy. Add new tags here first.

## Page Classification

Pages are organized into a recursive classification hierarchy. The `classification` frontmatter field specifies where a page sits in this tree. This makes topics easier to understand, navigate, and maintain.

### Concept Classifications

```
concepts/
├── biotechnology/
│   ├── molecular-biology/
│   │   ├── dna-operations/        # DNA extraction, PCR, sequencing prep
│   │   └── omics/                 # Genomics, bioinformatics
│   ├── sequencing/                # Nanopore, long-read, adaptive sampling
│   ├── laboratory-methods/        # Sample prep, quality control, cell culture
│   └── environmental-biology/     # Ecology, conservation, environmental monitoring
├── psychology/
│   ├── forensic-psychology/       # Criminal behavior, criminal psychology
│   └── media-ethics/              # Celebrity privacy, blackmail
├── legal-science/
│   └── forensic-evidence/         # DNA evidence, legal frameworks
├── research-methodology/
│   ├── knowledge-management/      # Knowledge preservation, systems
│   └── reproducibility/           # Reproducibility crisis, validation
└── systems/
    └── knowledge-systems/         # Neural Nexus, personal KBs
├── artificial-intelligence/       # Future: AI/ML concepts
│   ├── large-language-models/    # LLMs, foundation models
│   ├── multimodal-ai/             # Text, image, audio models
│   ├── ai-safety/                # Alignment, ethics, safety
│   └── generative-ai/            # Gemini, Claude, GPT, etc.

### Entity Classifications

```
entities/
├── person/
│   ├── researcher/                # Scientists, academics
│   ├── legal-figure/              # Criminals, legal case subjects
│   └── media-figure/              # Celebrities, public figures
├── organization/                  # Institutions, companies
├── location/                      # Places, jurisdictions
└── object/                        # Tools, artifacts, datasets
```

### Rules

1. **Every concept and entity must have a `classification` field** in frontmatter
2. **Classification is a dot-path** — e.g., `classification: biotechnology.molecular-biology.dna-operations`
3. **Minimum depth 2** — at least `category.subcategory`
4. **The tree is extensible** — add new branches as content grows
5. **Review regularly** — the lint script validates classifications against SCHEMA.md
6. **Sub-classifications can nest recursively** — no depth limit

### Concept Classification Reference

| Classification | Pages |
|---|---|
| `biotechnology.molecular-biology.dna-operations` | dna-extraction, dna-extraction-methodologies, pcr, tissue-specific-dna-extraction |
| `biotechnology.molecular-biology.omics` | genomics |
|| `biotechnology.sequencing` | nanopore-sequencing, adaptive-sampling |
|| `biotechnology.laboratory-methods` | sample-preparation, cell-line-culture |
|| `biotechnology.environmental-biology` | ecology, conservation-biology, environmental-dna-analysis, environmental-monitoring |
|| `psychology.forensic-psychology` | criminal-psychology-behavior-patterns |
|| `psychology.media-ethics` | celebrity-privacy-media-ethics |
|| `legal-science.forensic-evidence` | dna-evidence-hong-kong-legal-system |
|| `research-methodology.knowledge-management` | knowledge-preservation, dangerous-person-2-0-research-overview, dangerous-person-2-0-research-project |
|| `research-methodology.reproducibility` | reproducibility-crisis |
|| `systems.knowledge-systems` | neural-nexus, molecular-biology |
|| `artificial-intelligence.generative-ai` | gemini |

### Entity Classification Reference

| Classification | Pages |
|---|---|
| `person.researcher` | penn-rainford |
| `person.legal-figure` | lam-kwok-wai-tuen-mun-rapist |
| `person.media-figure` | x-television-celebrity |

## Content Types

### Ideas
- **Purpose**: Raw thoughts, brainstorming, unprocessed notes
- **Threshold**: No minimum - create for any thought worth keeping
- **Structure**: Quick bullets, minimal structure
- **Example**: "Idea for optimizing RAG retrieval with hierarchical clustering"

### Findings
- **Purpose**: Processed insights from research/analysis
- **Threshold**: Create when processing reveals novel insight
- **Structure**: Problem → Analysis → Conclusion → Sources
- **Example**: "Video analysis revealed 3 key patterns in agent workflows"

### Readings
- **Purpose**: Summaries of books, papers, videos
- **Threshold**: Create for every ingested source
- **Structure**: Title, source, key points, quotes, related pages
- **Example**: "LLM Wiki video notes with 5 key takeaways"

### Entities
- **Purpose**: People, organizations, tools, projects
- **Threshold**: Mentioned in 2+ sources OR central to 1 source
- **Structure**: Overview, key facts, relationships, sources
- **Example**: "Andrej Karpathy - AI researcher, former Tesla Autopilot director"

### Concepts
- **Purpose**: Technical concepts, theories, frameworks
- **Threshold**: Explained in depth OR appears in 3+ sources
- **Structure**: Definition, current state, open questions, related concepts
- **Example**: "Transformer architecture - self-attention mechanism, multi-head attention, positional encoding"

### Comparisons
- **Purpose**: Side-by-side analyses
- **Threshold**: Whenever comparing 2+ items
- **Structure**: What compared, dimensions, verdict, sources
- **Example**: "Obsidian vs Notion vs Roam Research for knowledge management"

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

- **Target**: 50-150 lines per page
- **Split**: When exceeding 200 lines
- **Archive**: Move to `_archive/` when fully superseded