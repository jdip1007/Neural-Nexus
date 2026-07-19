---
title: Knowledge Preservation in the Era of Big Science and AI
created: 2026-07-18
updated: 2026-07-18
type: reading
domain: ai, biotech
tags: [knowledge-management, research, reproducibility, open-science, ai]
sources: [raw/articles/knowledge-preservation-big-science-ai-rainford-et-al-2026.md]
confidence: high
status: active
reviewed: 2026-07-18
---

# Knowledge Preservation in the Era of Big Science and AI

## Source

| Field | Value |
|-------|-------|
| Type | article |
| URL | https://doi.org/10.1038/s41467-026-72667-3 |
| Author | Penn F. Rainford et al. |
| Published | Nature Communications (2026) |
| Ingested | 2026-07-18 |

## TL;DR

Modern scientific research is losing knowledge through unpublished negative results, departing researchers带走 tacit knowledge, and fragmented preservation efforts. The research community needs alternative dissemination channels, improved documentation practices, and sustainable digital infrastructure to make science more open, efficient, and resilient.

## Key Points

1. **Knowledge crisis**: Science is losing knowledge it cannot afford to lose - negative results go unpublished, hard-won expertise walks out with departing researchers, and preservation efforts remain fragmented

2. **Scale transformation**: Laboratory automation and high-throughput methods have expanded dramatically, enabling experiments at previously unimaginable scales while generating vast heterogeneous, multi-modal datasets

3. **Publication inadequacy**: Traditional journals impose strict page limits, leading to abbreviated methodologies that omit crucial contextual information and troubleshooting insights needed for true reproducibility

4. **Researcher turnover**: High researcher turnover has become more pronounced due to competitive job markets, funding constraints, and increasing career mobility, impairing research efficiency

5. **Key challenges**: Reproduducibility crisis, inadequate documentation, storage issues, terminology confusion across disciplines, degrading research outputs over time, systematic exclusion of null results, loss of tacit knowledge through personnel turnover

6. **Existing solutions**: FAIR principles, BioFAIR, CURE principles, specialized repositories (PDB, GenBank, ENA, SynBioHub), version control systems, platforms like Addgene and Galaxy

7. **Future vision**: Need interconnected ecosystem linking experimental and computational outputs, null results, tacit expertise, and published findings into a coherent, navigable web of scientific knowledge

8. **AI role**: AI can help maintain and navigate the ecosystem by automating metadata generation, flagging broken links, surfacing relevant prior work, and reducing burden on individual researchers

## Notable Quotes

> "Science is losing knowledge it cannot afford to lose. Negative results go unpublished, hard-won expertise walks out the door with departing researchers, and preservation efforts remain fragmented. The consequences are wasted resources, duplicated effort, and missed discoveries."

> "Modern scientific research is undergoing an unprecedented transformation in the scale and nature of the data it produces, challenging traditional approaches to knowledge preservation and dissemination."

> "The computational aspects of modern research are particularly vulnerable to the loss of tacit knowledge. Understanding why certain parameter combinations produce unstable results, how to interpret ambiguous model outputs, or which computational approaches are best suited to specific types of data represents specialized knowledge that is difficult to codify but essential for effective research."

## Detailed Notes

### Key Challenges

**Reproducibility Crisis**: Current publication practices often fail to provide sufficient detail for true reproducibility, omitting procedural nuances, full parameter settings, and practical insights that determine experimental success.

**Storage and Preservation**: Long-term preservation faces challenges from failing freezers leading to denaturation and degradation of samples, evolving file formats, deprecated software dependencies, and absence of sustained funding for maintenance.

**Interdisciplinary Confusion**: Terminology differences across research communities create misunderstandings - common terms like 'in vivo', 'in vitro', and 'gene' have differing meanings across disciplines.

**Research Output Degradation**: Shared resources often degrade over time due to inadequate curation and maintenance - biological materials become mislabeled, code becomes obsolete as environments change, documentation becomes insufficient.

**Null Results Exclusion**: Systematic exclusion of findings that don't support experimental hypotheses or fail to replicate existing work, despite their recognized scientific value.

**Tacit Knowledge Loss**: When experienced researchers depart, they take subtle technical insights, methodological refinements, and practical knowledge essential to successful complex procedures.

### Existing Solutions and Frameworks

**FAIR Principles**: Ensure data are Findable, Accessible, Interoperable, and Reusable - widely accepted benchmark for evaluating how research outputs should be structured and shared.

**BioFAIR**: Adapts FAIR approach for life sciences by incorporating metadata standards, provenance tracking, and reproducibility layers.

**CURE Principles**: Focus on computational models that are Correct, Unbiased, Robust, and Explainable - highlights importance of transparency and validation.

**Specialized Repositories**: Protein Data Bank (PDB), GenBank, European Nucleotide Archive (ENA), SynBioHub - support data preservation within specific domains through internationally coordinated, community-driven curation and validation.

**Version Control Systems**: Git and platforms like GitHub and GitLab have transformed computational reproducibility by enabling code tracking, collaboration, and transparent records.

### Building Sustainable Knowledge Preservation

**Alternative Dissemination Channels**: Need moderated platforms for sharing null results and practical know-how that traditional journals exclude.

**Community-Driven Standards**: Shared standards that can evolve as technologies advance, enabling structured reuse, scalable moderation, and interpretability.

**AI-Powered Tools**: Tools that lower barriers to implementation by automating routine tasks, generating initial documentation drafts, and providing rapid quality assessments of shared resources.

**Incentive Structures**: Recognition and reward for knowledge sharing activities, building intrinsic community value where individual contributions generate collective benefits that exceed the sum of each person's effort.

## Entities Mentioned

- [Penn-Rainford](entities/penn-rainford.md) — Lead author, University of York, Department of Computer Science
- [[Thomas-Gorochowski]] — Corresponding author, University of Bristol, School of Biological Sciences
- [[Annalisa-Occhipinti]] — Teesside University, School of Computing, Engineering and Digital Technologies
- [[Bo-Wang]] — National Institute of Health, Laboratory of Pathology
- [[Susan-Stepney]] — University of York, Department of Computer Science
- [[Claudio-Angione]] — Teesside University
- [[Edda-Klipp]] — Humboldt-Universität zu Berlin, Institute of Biology, Theoretical Biophysics
- [[Claire-Grierson]] — University of Bristol, School of Biological Sciences
- [[Sarah-Harris]] — Sheffield University, School of Mathematical and Physical Sciences

## Concepts Referenced

- [[FAIR-principles]] — Findable, Accessible, Interoperable, Reusable data principles
- [[BioFAIR]] — FAIR principles adapted for life sciences with metadata standards
- [[CURE-principles]] — Correct, Unbiased, Robust, Explainable computational models
- [Reproducibility-crisis](concepts/reproducibility-crisis.md) — Crisis in scientific research where results cannot be reliably reproduced
- [[Tacit-knowledge]] — Unwritten expertise and practical know-how that's difficult to formalize
- [[Open-science]] — Movement to make scientific research and data accessible to all
- [Knowledge-preservation](concepts/knowledge-preservation.md) — Strategies for maintaining and accessing scientific knowledge over time

## My Takeaways

1. **Urgency**: The knowledge preservation crisis is immediate and requires coordinated action rather than waiting for comprehensive system overhauls

2. **AI's dual role**: AI can both help solve the knowledge preservation problem and make the problem worse - it needs careful management to ensure accuracy, prevent bias, and maintain human oversight

3. **Community value**: The open-source model offers valuable lessons in community governance, quality control, and incentive design that can be adapted for scientific knowledge preservation

4. **Cultural change**: Success depends on people - technology alone cannot solve what is fundamentally a cultural and organizational challenge

5. **Incremental progress**: The path forward will be incremental rather than revolutionary, built on pragmatic integration of existing tools and gradual adoption of new platforms

## Related Readings

- [reproducibility-crisis](concepts/reproducibility-crisis.md)
- [[open-science]]
- [[knowledge-management]]
- [[FAIR-principles]]