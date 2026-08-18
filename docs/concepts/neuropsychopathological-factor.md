---
title: Neuropsychopathological Factor
created: 2025-01-21
updated: 2026-07-31
type: concept
classification: psychology.neuroscience.neuropsychopathology
domain: psychology
tags: [neuropsychopathology, psychiatric-comorbidity, brain-connectivity, longitudinal-study, prefrontal-cortex, executive-function, genetics, mental-health, research]
sources: [raw/articles/shared-neural-basis-psychiatric-comorbidity.md]
confidence: high
status: active
reviewed: 2026-07-31
backlinks: []
---

# Neuropsychopathological (NP) Factor

The **neuropsychopathological (NP) factor** is a reproducible neural signature that underlies both externalizing and internalizing psychiatric symptoms. Identified by Xie et al. (2023) in *Nature Medicine*, it represents a unified, genetically determined, delayed development of the prefrontal cortex leading to poor executive function and increased vulnerability for multiple mental disorders.^[raw/articles/shared-neural-basis-psychiatric-comorbidity.md]

## Definition

The NP factor is a crossdisorder brain signature derived from multitask fMRI connectomes. It captures shared functional connectivity (FC) edges that predict both externalizing symptoms (ASD, ADHD, ODD, CD) and internalizing symptoms (GAD, depression, ED, SP). Unlike the behavioral **p factor** (which simply sums symptom correlations), the NP factor is grounded in specific neural circuits and cognitive processes.

## Core Mechanism

The NP factor operates through three interconnected networks:

| Network | Role | Key Finding |
|---------|------|-------------|
| **Sensorimotor (SMF)** | Sensorimotor integration, action planning, cognitive control | Weaker intra-network FC → higher symptoms |
| **Salience (SAL)** | Detecting relevant stimuli, switching between DMN and executive networks | Weaker intra-network FC → higher symptoms |
| **Frontoparietal (FPN)** | Working memory, decision-making, cognitive control | Weaker intra-network FC → higher symptoms |

**Key regions**: ventral precuneus (vPCun), medial prefrontal cortex (mPFC), inferior frontal gyrus (IFG) — these serve as hub nodes with high centrality.

**Mechanism**: Reduced connectivity within SMF/SAL/FPN networks (positive edges) reflects delayed maturation of prefrontal circuits during adolescence. Enhanced connectivity between these networks and other regions (negative edges) is protective.

## Why It Matters

1. **Bridges the internalizing–externalizing divide**: Traditional psychiatry treats these as separate dimensions. The NP factor shows they share a common neural substrate.

2. **Mechanistic link from genes to behavior**: The chain is: genetic risk (ADHD/depression PRS) → neurodevelopmental SNPs → delayed prefrontal maturation → weaker SMF/SAL/FPN connectivity → poor executive function → psychiatric symptoms.

3. **Critical developmental window**: NP factor scores decrease with age (normalization), but higher scores at age 14 predict slower symptom reduction — adolescence is the window for intervention.

4. **Transdiagnostic biomarker**: Generalizes across development (ages 10–29), imaging modalities (task + resting-state), and clinical populations (ADHD-200, STRATIFY/ESTRA).

## Current State

### Reliability and Reproducibility

- Test-retest reliability: ICC = 0.94 (excellent)
- Longitudinal stability: Age 14 → Age 19 correlation r = 0.57
- Validated in 5 independent cohorts (IMAGEN, ABCD, HCP, ADHD-200, STRATIFY/ESTRA), total N = 4,891

### Prediction Accuracy

| Context | Externalizing | Internalizing |
|---------|--------------|---------------|
| IMAGEN age 14 (task) | r = 0.30 | r = 0.24 |
| IMAGEN age 19 (task) | r = 0.24 | r = 0.19 |
| IMAGEN age 14 (resting) | r = 0.22 | r = 0.18 |
| ABCD ages 10-11 | r = 0.15–0.35 | r = 0.15–0.35 |
| ADHD-200 clinical | r = 0.28 (ADHD) | — |
| STRATIFY/ESTRA clinical | r = 0.19–0.26 | r = 0.19–0.26 |

### Genetic Underpinnings

- Associated with ADHD PRS (r = -0.10, P = 0.002) and depression PRS (r = -0.09, P = 0.004)
- Gene ontology enrichment: neuronal differentiation, axon guidance, synapse formation (P < 0.001)
- No enrichment for immune or metabolic pathways — specificity to neurodevelopmental processes

### Neurobehavioral Profile

Specific to **executive function** deficits only:
- IQ: r = -0.18 (P < 0.001)
- Working memory: r = -0.15 (P < 0.001)
- Risk adjustment: r = -0.12 (P < 0.001)
- Not associated with processing speed or memory consolidation (non-executive domains)

## Comparison with the p Factor

| Aspect | p Factor | NP Factor |
|--------|----------|-----------|
| Level | Behavioral (symptom sums) | Neural (FC edges) |
| Scope | Positive correlations only | Both positive and negative edges |
| Mechanism | Statistical abstraction | Specific brain circuits |
| Cognitive link | Unspecified | Executive function deficits |
| Genetic link | Broad | ADHD/depression PRS + neurodevelopmental SNPs |
| Modality | Usually task-free | Multitask fMRI (SST, MID, EFT) |

## Open Questions

1. **Population diversity**: IMAGEN is primarily European ancestry — does the NP factor generalize to other populations?
2. **Environmental factors**: Current model is genetic-only. How do stress, trauma, and social environment interact with the NP factor?
3. **Intervention targets**: Can executive function training during adolescence normalize NP factor connectivity?
4. **Clinical utility**: Can NP factor scores be used for early screening and personalized intervention?
5. **Longitudinal prediction**: Does the NP factor at age 10 predict symptom onset at age 14?

## Common Misconceptions

| Myth | Reality |
|------|---------|
| The NP factor is just the p factor in the brain | NP factor is circuit-specific (SMF/SAL/FPN), not a statistical abstraction |
| It means all mental disorders are the same | It identifies shared neural vulnerability; disorders still have distinct features |
| Weaker connectivity always means worse outcomes | Negative edges (stronger between-network FC) are protective |
| The NP factor applies to all psychiatric disorders | Only tested for 8 symptoms (4 externalizing, 4 internalizing); not yet tested for psychosis, bipolar, etc. |

## Related Concepts

- [psychiatric-comorbidity](concepts/psychiatric-comorbidity.md) — The phenomenon the NP factor explains
-  — The cognitive domain linked to the NP factor
- [prefrontal-cortex-development](concepts/prefrontal-cortex-development.md) — The developmental process underlying the NP factor
-  — The FC measure used to construct the NP factor
-  — The behavioral p factor (predecessor concept)
- [mental-health](concepts/mental-health.md) — Hub page for mental health concepts
- [psychology](concepts/psychology.md) — Parent domain

## Related Entities

-  — Primary cohort (N = 1,750)
-  — Clinical validation sample
-  — ADHD clinical validation

## Related Pages

- [[mental-health]]
- [[executive-function]]
- [[psychology]]
