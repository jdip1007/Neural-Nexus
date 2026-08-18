---
title: Heritability
created: 2026-08-06
updated: 2026-08-06
type: concept
classification: research-methodology.genetics
domain: research-methodology
tags: [genetics, quantitative-genetics, family-studies, genetic-epidemiology, statistical-genetics]
sources: [raw/articles/adhd-genetics-nature-genetics-2025.md]
confidence: high
status: active
reviewed: 2026-08-06
backlinks: []
---

# Heritability

## Overview

Heritability is a fundamental concept in genetics that quantifies the proportion of phenotypic variation in a population that can be attributed to genetic variation. It is a population-level statistic, not an individual characteristic, and provides crucial insights into the genetic architecture of complex traits and diseases.

## Definition and Concept

### What is Heritability?

Heritability (h²) is defined as the proportion of total phenotypic variance in a population that is due to genetic variance:

```
h² = V_G / V_P
```

Where:
- **V_G** = Genetic variance (variance due to genetic differences)
- **V_P** = Total phenotypic variance (total observed variation)

### Key Characteristics

1. **Population-Specific**: Heritability estimates apply only to the specific population studied
2. **Time-Specific**: Can change over time as environments change
3. **Trait-Specific**: Different traits have different heritability estimates
4. **Not Fixed**: Can vary across different populations and environments

## Types of Heritability

### Narrow-Sense Heritability (h²)

**Definition**: Proportion of phenotypic variance due to additive genetic effects.

**Formula:**
```
h² = V_A / V_P
```

**What it captures:**
- Additive effects of alleles
- Predicts response to selection
- Most commonly reported in behavioral genetics

### Broad-Sense Heritability (H²)

**Definition**: Proportion of phenotypic variance due to all genetic effects.

**Formula:**
```
H² = V_G / V_P = V_A + V_D + V_I / V_P
```

**Components:**
- **V_A**: Additive genetic variance
- **V_D**: Dominance genetic variance
- **V_I**: Epistatic (interaction) genetic variance

## Methods for Estimating Heritability

### Twin Studies

**Classic Design**: Compare monozygotic (MZ) and dizygotic (DZ) twins

**Assumptions:**
- MZ twins share 100% of genes
- DZ twins share 50% of genes on average
- Twins share common environment

**Calculation:**
```
h² = 2 × (r_MZ - r_DZ)
```

**Limitations:**
- Equal environment assumption may not hold
- Twin studies may overestimate heritability
- Sample size limitations

### Family Studies

**Design**: Compare resemblance between relatives with varying degrees of relatedness

**Methods:**
- Parent-offspring regression
- Sibling correlations
- Extended family designs

**Advantages**: Larger sample sizes, more representative populations

### Adoption Studies

**Design**: Compare adopted children with biological vs. adoptive parents

**Strengths**: Separates genetic and environmental effects
**Limitations**: Selective placement, small sample sizes

### Genome-Wide Complex Trait Analysis (GCTA)

**Modern Approach**: Uses genome-wide SNP data to estimate heritability

**Method**: 
- Genome-wide complex trait analysis
- Relates SNP-based genetic relatedness to phenotypic similarity

**Advantages**: 
- No assumptions about family structure
- Can estimate SNP heritability directly
- Large sample sizes possible

## Heritability in ADHD

### ADHD Heritability Estimates

Based on current research:

| Heritability Type | Estimate | Study Type | Sample Size |
|-------------------|----------|------------|-------------|
| **Total Heritability** | 70-80% | Twin/Family Studies | Large cohorts |
| **SNP Heritability** | 11% | GCTA/GWAS | >100,000 |
| **Missing Heritability** | 59-69% | - | - |

### Interpretation of ADHD Heritability

**High Heritability**: ADHD is one of the most heritable psychiatric disorders
**Missing Heritability**: Large portion not explained by common variants
**Implications**: Strong genetic component but also significant environmental influences

## Factors Affecting Heritability Estimates

### Population Factors

1. **Genetic Diversity**: More diverse populations may show lower heritability
2. **Environmental Variation**: More uniform environments may show higher heritability
3. **Gene-Environment Correlations**: Genetic differences may lead to different environments

### Methodological Factors

1. **Measurement Error**: Poor measurement reduces estimated heritability
2. **Sample Size**: Small samples have imprecise estimates
3. **Statistical Power**: Limited power to detect small genetic effects

### Temporal Factors

1. **Changing Environments**: Environmental changes can alter heritability estimates
2. **Secular Trends**: Cultural and technological changes affect phenotypic expression

## Clinical Implications

### Risk Assessment

**High Heritability**: Strong genetic component suggests family history is important
**Moderate Heritability**: Both genetic and environmental factors play significant roles

### Treatment Planning

**Genetic Influence**: Understanding heritability helps frame treatment approaches
**Environmental Modification**: High environmental component suggests environmental interventions may be effective

### Prevention Strategies

**High-Risk Families**: Early intervention for families with strong genetic predisposition
**Population Screening**: May be more effective for highly heritable conditions

## Research Applications

### Gene Discovery

**Heritability as Guide**: High heritability suggests genetic studies are likely to be successful
**Sample Size Requirements**: Higher heritability allows detection with smaller samples

### Study Design

**Power Calculations**: Heritability estimates help determine required sample sizes
**Trait Selection**: Guides choice of traits for genetic studies

### Interpretation of Results

**Effect Size Interpretation**: Helps contextualize the magnitude of genetic effects
**Missing Heritability**: Highlights limitations of current genetic studies

## Common Misconceptions

| Myth | Reality |
|------|---------|
| **Heritability applies to individuals** | Heritability is a population-level statistic |
| **High heritability means genes determine fate** | Environmental factors still play crucial roles |
| **Heritability is fixed** | Heritability can change across populations and time |
| **Heritability explains all genetic effects** | Only captures additive genetic effects in narrow sense |
| **Twin studies provide perfect estimates** | Twin studies have important limitations and assumptions |

## Statistical Considerations

### Confidence Intervals

**Importance**: Always report confidence intervals around heritability estimates
**Interpretation**: Wide intervals indicate imprecise estimates

### Multiple Testing

**Challenge**: Many statistical tests in heritability analysis
**Solution**: Appropriate correction for multiple comparisons

### Model Assumptions

**Critical**: All heritability methods rely on specific assumptions
**Validation**: Assumptions should be tested when possible

## Future Directions

### Improved Methods

1. **Better Statistical Models**: More sophisticated methods for partitioning variance
2. **Multi-omics Integration**: Combine genomic, epigenomic, and transcriptomic data
3. **Longitudinal Studies**: Track heritability changes over time

### Better Understanding

1. **Gene-Environment Interactions**: How environment modifies genetic effects
2. **Epigenetic Mechanisms**: How environment affects gene expression
3. **Developmental Dynamics**: How heritability changes across development

## Related Concepts

- [[polygenic-scores]] - Using genetic information for risk prediction
- [[adhd-risk-genes-effect-sizes]] - Specific genetic variants associated with ADHD
- [[genetic-epidemiology]] - Study of genetic factors in populations
- [[statistical-genetics]] - Statistical methods in genetic research

## References

1. van der Laan, C. M. et al. (2025). Genome-wide association meta-analysis of childhood ADHD symptoms and diagnosis identifies new loci and potential effector genes. *Nature Genetics*, 57, 2427–2435. https://doi.org/10.1038/s41588-025-02295-y

2. Sullivan, P. F., et al. (2012). Genetic epidemiology of major depression: review and meta-analysis. *American Journal of Psychiatry*, 169(10), 1095-1111. https://doi.org/10.1176/appi.ajp.2012.11111716

3. Visscher, P. M., et al. (2014). 10 years of GWAS discovery: biology, function, and translation. *American Journal of Human Genetics*, 94(1), 8-14. https://doi.org/10.1016/j.ajhg.2013.11.012

4. Posthuma, D., & Polderman, T. J. (2013). Design and analysis of twin studies. *Neuropsychology Review*, 23(1), 107-120. https://doi.org/10.1007/s11065-012-9219-0