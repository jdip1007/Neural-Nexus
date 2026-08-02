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
- biotech, genomics, dna, nanotechnology, synthetic-biology, neuroscience, medical-research, drug-development, sleep-research
- finance, insurance, savings-insurance, trading, economics, cryptocurrency, risk-management, financial-literacy, personal-finance, financial-planning
- devops, infrastructure, security, reliability, monitoring
- psychology, cognitive-science, behavior, mental-health, bpsd, neuropsychiatric-symptoms, person-centered-dementia-care, nonpharmacologic-interventions, deprescribing
- hermes, automation, workflow, knowledge-management
- laboratory, clinical-laboratory, laboratory-regulations, laboratory-developed-tests, ldt
- biology, metabolism, scaling-laws, allometry, ecological-scaling

### Topics

- architecture, training, inference, alignment, safety, evaluation, fine-tuning, automation, multimodal
- bioinformatics, computational-biology, sequencing, data-science, neurodegeneration, alzheimers-disease, tau-pathology, amyloid-beta, neuroimmunology, neuroinflammation, biomarker-discovery, disease-modifying-therapies, therapeutic-antibodies, apoe, biomarkers, cryo-em, post-translational-modifications, targeted-protein-degradation, therapeutic-targeting, gene-therapy, microglia, astrocytes, innate-immunity, adaptive-immunity, neurodevelopment, adolescence, neurology, brain-metabolism, energy-dynamics, REM-sleep, neurovascular-coupling, cerebral-blood-flow, hemodynamics, lactate, pyruvate, ATP, sleep, ANLS, glucose, mitochondria, prion-disease, creutzfeldt-jakob-disease, kuru, infectious-proteins, brain-disease, protein-folding, neurodegenerative-disease, medical-case, medical-youtube-channel, medical-reviewer, hematology, medical-education
- crispr, protein-design, drug-discovery, reproducibility, dna-extraction, molecular-biology, laboratory-technique, nucleic-acid-extraction, respiratory-viruses, qpcr, influenza, rsv, hmpv, adenovirus, laboratory-platform-comparison, clinical-validation, analytical-sensitivity, limit-of-detection
- cell-biology, tissue-culture, genomics, dna-sequencing, long-read-sequencing, nanopore-sequencing, tissue-preparation
- liquid-biopsy, diagnostics, microbiology, ecology, environmental-science, biotechnology, biology, biochemistry
- genetics, biodiversity, conservation, ecosystems, cell-line, pcr, quality-control, gc-rich, dna-amplification, enhancers, betaine, dmso, additives, cold-spring-harbor, bioinformatics-validation, ngs-validation, molecular-diagnostics
- clia, cms, 42-cfr-493, federal-regulations, fda-oversight, fda-approved-tests, fda-approval-process, fda-ldt-oversight, clia-requirements, clia-waived-tests, laboratory-director, proficiency-testing, calibration-verification, method-comparison, bridging-studies, regulatory-compliance, sample-requirements, risk-assessment, accreditation, validation, verification, verification-vs-validation, method-evaluation, method-development, method-implementation, change-control, performance-characteristics, accuracy, precision, sensitivity, specificity, analytical-validation, reference-interval-verification, diagnostic-accuracy, roc-analysis, decision-flow, quality-management, clinical-utility, bias, in-house-tests, aphl, toolkit, statistical-analysis, clinical-virology, manufacturer, laboratory-equipment, in-vitro-diagnostics
- metabolic-scaling, power-law, comparative-physiology, basal-metabolic-rate, scaling-laws, fractal-networks, fractal-geometry, biological-networks, wbe-theory, kleibers-law, surface-law, superseded-theory, theoretical-biology, theoretical-physics, complex-systems, urban-scaling, heartbeats, heart-rate, lifespan, mathematics, historical-biology, historical-biologist, agricultural-science, science-communication, science-education, youtube-educator, youtube-channel, educational-content, veritasium, derek-muller, snatoms, geoffrey-west, scale-book
- markets, portfolio, analysis, algorithmic-trading
- insurance, insurance-products, life-insurance, investment-products, investment-risk, opportunity-cost, insurtech, health-insurance, investment-myths
- kubernetes, ci-cd, observability, site-reliability
- learning, decision-making, therapy, cognitive-bias, criminal-behavior, forensic-psychology, psychiatric-comorbidity, neuropsychopathology, executive-function, prefrontal-cortex, longitudinal-study, connectomics, brain-connectivity, developmental-psychopathology, heritability, neurobiology, comorbidity, intervention, stigma, gender-differences, prevalence, epigenetics, dopamine, cortical-maturation
- hong-kong, media-ethics, celebrity-privacy, blackmail, legal-science, forensic-science, dna-evidence
- criminal-justice, crime-investigation, legal-cases, dangerous-person-2-0, dangerous-person-2.0
- celebrity, television-personality, blackmail-victim, serial-offender, criminal
- research-methodology, youtube-research, qgn-method, prompt-engineering, fine-tuning, model-comparison, university, research-institution, japan, glial-biology, brain-physiology, fluorescence-imaging, university-of-california
- mental-health, trauma, ptsd, autism, neurodiversity, adhd, diagnosis, misdiagnosis, cognitive-disengagement, misconceptions
- dating, relationships, love, friendship, gender, social-dynamics, modern-dating, parenting, communication, social-skills, anxiety, emotions, frustration
- mindset, personal-development, success, stoicism, personality, authenticity, social-perception, impatience, failure, self-perception, intelligence, smart-people, support, dreams, goals, dissociative-identity
- healthygamergg, technology, tohoku-university, brain-energy-dynamics

### Meta
- research, opinion, tutorial, reference, news, analysis, comparison, setup, writing, documentation, guide, knowledge-base, sustainability, validation, scientific-method, researcher, computer-science, research-tools, ai, open-science, reproducibility-crisis, research-crisis, reproducibility, simulation, optimisation, performance, game-development, data-structures, algorithms, rendering, canvas, web-performance, washington-university

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
│   ├── environmental-biology/     # Ecology, conservation, environmental monitoring
│   ├── neuroscience/              # Neurodegeneration, neurobiology, brain research
│   │   ├── neurodegeneration/     # Alzheimer's, tau, amyloid
│   │   └── brain-energy-dynamics/ # REM sleep energy paradox, neurovascular coupling, ANLS
├── psychology/
│   ├── forensic-psychology/       # Criminal behavior, criminal psychology
│   ├── media-ethics/              # Celebrity privacy, blackmail
│   ├── dating/                    # Dating, modern dating, relationships
│   ├── mental-health/            # Mental health, diagnosis, therapy
│   │   └── comorbidity/           # Psychiatric comorbidity, NP factor
│   ├── neuroscience/              # Brain connectivity, neuroimaging
│   │   ├── neuropsychopathology/  # NP factor, crossdisorder brain signatures
│   │   └── prefrontal-cortex-development/ # PFC maturation, executive function
│   ├── relationships/            # Interpersonal relationships, communication
│   ├── personal-development/     # Mindset, success, personal growth
│   ├── personality/              # Personality traits, stoicism, authenticity
│   └── trauma/                   # Trauma, PTSD, dissociative disorders
├── legal-science/
│   └── forensic-evidence/         # DNA evidence, legal frameworks
├── research-methodology/
│   ├── knowledge-management/      # Knowledge preservation, systems
│   └── reproducibility/           # Reproducibility crisis, validation
├── systems/
│   └── knowledge-systems/         # Neural Nexus, personal KBs
├── artificial-intelligence/       # AI/ML concepts
│   ├── large-language-models/    # LLMs, foundation models
│   ├── multimodal-ai/             # Text, image, audio models
│   ├── ai-safety/                # Alignment, ethics, safety
│   └── generative-ai/            # Gemini, Claude, GPT, etc.
├── computer-science/              # CS concepts
│   └── simulation/               # Particle simulations, cellular automata
└── finance/                       # Financial concepts
    └── insurance-products/        # Savings insurance, life insurance
├── laboratory/                    # Clinical laboratory science
│   ├── regulatory/                # CLIA, accreditation, compliance
│   ├── method-evaluation/         # Verification, validation, performance
│   └── testing/                   # LDTs, technology implementation
├── biology/                       # Biological sciences
│   └── metabolic-scaling/        # Kleiber's law, WBE theory, allometry

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
| `biotechnology.sequencing` | nanopore-sequencing, adaptive-sampling |
| `biotechnology.laboratory-methods` | sample-preparation, cell-line-culture |
| `biotechnology.environmental-biology` | ecology, conservation-biology, environmental-dna-analysis, environmental-monitoring |
| `psychology.forensic-psychology` | criminal-psychology-behavior-patterns |
| `psychology.media-ethics` | celebrity-privacy-media-ethics |
| `psychology.dating` | why-modern-dating-feels-like-parenting, why-smart-people-are-bad-at-dating, why-you-freeze-up-when-you-talk-to-women |
| `psychology.mental-health` | ai-therapy-is-making-you-mentally-weak, the-most-misdiagnosed-condition-in-mental-health, what-everyone-gets-wrong-about-adhd |
| `psychology.relationships` | can-men-women-be-friends_, how-your-brain-perceives-love-when-you-have-autism, i-did-everything-right-i-still-cant-find-love, why-validating-feelings-can-ruin-relationships, why-your-partner-doesnt-support-your-dreams |
| `psychology.personal-development` | how-to-actually-have-an-elite-mindset, the-impatient-man_-why-you-feel-like-a-failure, why-learning-from-failure-is-ruining-your-life |
| `psychology.personality` | nobody-cares-how-stoic-you-are |
| `psychology.trauma` | how-trauma-splits-a-soul |
| `legal-science.forensic-evidence` | dna-evidence-hong-kong-legal-system |
| `research-methodology.knowledge-management` | knowledge-preservation, dangerous-person-2-0-research-overview, dangerous-person-2-0-research-project |
| `research-methodology.reproducibility` | reproducibility-crisis |
| `systems.knowledge-systems` | neural-nexus, molecular-biology |
| `artificial-intelligence.generative-ai` | gemini |
| `computer-science.simulation.optimisation` | optimisation-techniques-small-scale-simulation |
| `finance.insurance-products` | savings-insurance |
| `laboratory.regulatory` | clia-regulations, cms, clia-waived-tests, laboratory-director, proficiency-testing, risk-assessment, regulatory-compliance, fda-approval-process, fda-ldt-oversight, accreditation/index |
| `laboratory.method-evaluation` | laboratory-verification, laboratory-validation, method-performance, method-evaluation-decision-flow, quality-control, statistical-analysis, diagnostic-accuracy, roc-analysis, calibration-verification, method-comparison, bridging-studies, reference-interval-verification, clinical-utility, bioinformatics-validation, ngs-validation, sample-requirements |
| `laboratory.testing` | laboratory-developed-tests, method-development, method-implementation, molecular-diagnostics |
| `biology.metabolic-scaling` | kleibers-law, wbe-theory, surface-law, one-billion-heartbeats-phenomenon, metabolic-scaling, scaling-laws, fractal-networks, comparative-physiology, urban-scaling, lifespan, scale-book |

### Entity Classification Reference

| Classification | Pages |
|---|---|
| `person.researcher` | penn-rainford |
| `person.legal-figure` | lam-kwok-wai-tuen-mun-rapist |
| `person.media-figure` | x-television-celebrity |
| `organization.insurance-provider` | bowtie-insurance |

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