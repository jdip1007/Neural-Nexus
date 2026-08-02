# Neural Nexus Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: create, ingest, update, query, lint, deploy, archive, review, links

## [2026-08-02] ingest | Prion Disease (Chubbyemu Video)

- **Source:** Chubbyemu YouTube video "My friend got prion disease. We watched her forget who we are." (August 1, 2026)
- **Action:** Ingested video, created 4 wiki pages
- **Files created:**
  - `raw/videos/prion-disease-colleague-story.md` (raw source, 3,936 chars)
  - `readings/prion-disease-colleague-story.md` (reading summary, 6,512 chars)
  - `concepts/prion-disease.md` (comprehensive concept page, 11,208 chars)
  - `entities/katherine-johns.md` (medical reviewer entity, 2,326 chars)
- **Graph update:** 186 nodes, 1223 edges (increased from 183 nodes, 1204 edges)
- **Catalog update:** 187 pages across 7 sections
- **Tags used:** neurodegeneration, prion-disease, creutzfeldt-jakob-disease, kuru, infectious-proteins, brain-disease, protein-folding, neurodegenerative-disease, medical-case, medical-youtube-channel, medical-reviewer, hematology, medical-education
- **Note:** Full transcript unavailable due to YouTube bot protection; created pages based on video title, description, and extensive references

## [2026-08-01] ingest | eMAG vs MagNA PURE 96 vs easyMAG Respiratory Virus Extraction Comparison

- **Source:** Hindiyeh M, Mor O, Pando R, et al. (2019). Comparison of the new fully automated extraction platform eMAG to the MagNA PURE 96 and the well-established easyMAG for detection of common human respiratory viruses. PLoS ONE 14(2): e0211079. DOI: 10.1371/journal.pone.0211079
- **Action:** Ingested paper, created 7 wiki pages
- **Files created:**
  - `raw/laboratory/validation/emag-magana-easymag-respiratory-virus-extraction-comparison.md` (raw source, 21,630 chars)
  - `readings/emag-magana-easymag-respiratory-virus-extraction-comparison-2019.md` (reading summary, 12,065 chars)
  - `concepts/nucleic-acid-extraction-platforms.md` (concept page, 7,013 chars)
  - `entities/michel-mandelboim.md` (person/researcher, 5,449 chars)
  - `entities/musa-hindiyeh.md` (person/researcher, 3,153 chars)
  - `entities/orna-mor.md` (person/researcher, 2,723 chars)
  - `entities/biomerieux.md` (organization, 5,471 chars)
  - `entities/roche.md` (organization, 5,505 chars)
  - `comparisons/emag-vs-magana-pure-96-vs-easymag.md` (comparison, 11,321 chars)
- **SCHEMA.md update:** Added 10 new tags to taxonomy: nucleic-acid-extraction, respiratory-viruses, qpcr, influenza, rsv, hmpv, adenovirus, laboratory-platform-comparison, clinical-validation, analytical-sensitivity, limit-of-detection
- **Study scope:** 262 archived respiratory samples, 6 viruses (influenza A/B/H1N1pdm, RSV, hMPV, parainfluenza-3, adenovirus)
- **Key findings:** All platforms demonstrated comparable performance (>97% sensitivity, >98% specificity). Kappa >0.973 inter-platform agreement. LOD differences within one dilution factor (clinically negligible)
- **Tags used:** validation, nucleic-acid-extraction, respiratory-viruses, qpcr, influenza, rsv, hmpv, adenovirus, laboratory-platform-comparison, performance-characteristics, clinical-validation, analytical-sensitivity, limit-of-detection, molecular-biology, laboratory-technique

## [2026-07-31] audit+fix | Full wiki audit, fix, and deploy

- Audit: 130 nodes, 942 edges, 201 warnings, 94 broken wikilinks, 60 missing tags
- Fixed: Added 60+ tags to SCHEMA.md taxonomy
- Fixed: Moved raw/laboratory/ → docs/raw/laboratory/
- Fixed: Source paths in reading page (removed absolute paths)
- Fixed: Stale reviewed dates (7 pages updated to 2026-07-31)
- Created: 25+ hub/entity pages to resolve broken wikilinks
- Created: quality-control, metabolic-scaling, scaling-laws, fractal-networks, comparative-physiology
- Created: james-brown, van-savage, peter-sheridan-dodds, steven-strogatz (entities)
- Created: proficiency-testing, risk-assessment, statistical-analysis, cms, laboratory-director
- Created: clia-waived-tests, sample-requirements, scale-book, diagnostic-accuracy, roc-analysis
- Created: calibration-verification, method-comparison, bridging-studies, fda-ldt-oversight
- Created: method-development, clinical-utility, executive-function, lifespan
- Created: bioinformatics-validation, ngs-validation, molecular-diagnostics, urban-scaling
- Created: change-control, method-implementation, regulatory-compliance, fda-approval-process
- Created: reference-interval-verification
- Updated: Classification tree in SCHEMA.md (laboratory + biology branches)
- Updated: Classification reference table (4 new categories)

## [2026-07-31] ingest | One Billion Heartbeats (Veritasium Video)

- **Source:** Veritasium YouTube video "Why does every mammal get 1 billion heartbeats in their life?" (July 25, 2026)
- **Action:** Ingested video, created 10 wiki pages
- **Files created:**
  - `raw/videos/one-billion-heartbeats-veritasium.md` (raw source, 5,627 chars)
  - `readings/one-billion-heartbeats-veritasium.md` (comprehensive reading summary, 8,121 chars)
  - `concepts/kleibers-law.md` (3/4 power metabolic scaling, 8,914 chars)
  - `concepts/wbe-theory.md` (West-Brown-Enquist fractal network theory, 9,926 chars)
  - `concepts/one-billion-heartbeats-phenomenon.md` (constant heartbeat product, 8,109 chars)
  - `concepts/surface-law.md` (historical 2/3 power theory, 7,487 chars)
  - `entities/max-kleiber.md` (discoverer of Kleiber's Law, 6,534 chars)
  - `entities/geoffrey-west.md` (WBE theory co-developer, 8,550 chars)
  - `entities/brian-enquist.md` (WBE theory co-developer, 5,132 chars)
  - `entities/veritasium.md` (science YouTube channel, 5,542 chars)
  - `entities/derek-muller.md` (Veritasium creator, 6,565 chars)
- **Graph update:** 123 nodes, 917 edges (increased from previous state)
- **Catalog update:** 123 pages across 7 sections
- **Tags used:** metabolic-scaling, kleibers-law, scaling-laws, fractal-networks, lifespan, heart-rate, biology, mathematics, wbe-theory, surface-law, comparative-physiology, theoretical-biology, allometry, historical-biology, superseded-theory, theoretical-physics, complex-systems, fractal-geometry, urban-scaling, ecological-scaling, biological-networks, science-communication, youtube-channel, educational-content, youtube-educator, science-education, snatoms, agricultural-science, historical-biologist, media-figure
- **Note:** Full transcript unavailable due to YouTube bot protection; created pages based on video description, chapters, and expert credits

## [2026-07-30] ingest | AI's Impact on Science (Nature 2026)

- **Source:** Hao, Q., Xu, F., Li, Y., & Evans, J. (2026). "Artificial intelligence tools expand scientists' impact but contract science's focus." *Nature*, 649, 1237-1244. DOI: 10.1038/s41586-025-09922-y.
- **Action:** Ingested paper, created 6 wiki pages
- **Files created:**
  - `raw/articles/ai-impacts-science-nature-2026.md` (raw source, 77,991 chars)
  - `readings/ai-impacts-science-nature-2026.md` (reading summary with metrics)
  - `entities/qianyue-hao.md` (person/researcher)
  - `entities/fengli-xu.md` (person/researcher)
  - `entities/yong-li.md` (person/researcher)
  - `entities/james-evans.md` (person/researcher)
  - `findings/ai-individual-gains-collective-loss.md` (key finding)
- **Note:** First PDF (doc_ec779b330804_file.pdf) was empty (0 chars) — skipped
- **Tags used:** ai, research, researcher, scientific-method, open-science, reproducibility, knowledge-management, analysis, computer-science