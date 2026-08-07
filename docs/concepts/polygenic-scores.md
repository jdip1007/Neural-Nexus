---
title: Polygenic Scores
created: 2026-08-06
updated: 2026-08-06
type: concept
classification: research-methodology.genetics
domain: research-methodology
tags: [polygenic-risk, genetics, statistical-genetics, risk-prediction, heritability, genome-wide-association, quantitative-genetics, genetic-epidemiology, precision-medicine]
sources: [raw/articles/adhd-genetics-nature-genetics-2025.md]
confidence: high
status: active
reviewed: 2026-08-06
backlinks: []
---

# Polygenic Scores

## Overview

Polygenic scores (PGS), also known as polygenic risk scores (PRS), are statistical tools that aggregate the effects of thousands of genetic variants across the genome to predict an individual's genetic predisposition for complex traits and diseases. Unlike Mendelian disorders caused by single genes, complex traits like ADHD are influenced by hundreds or thousands of genetic variants, each with very small individual effects.

## What Are Polygenic Scores?

### Definition and Concept

A polygenic score is a single numerical value that represents the cumulative genetic risk for a particular trait or disease. It is calculated by summing the effects of multiple single nucleotide polymorphisms (SNPs) that have been associated with the trait through genome-wide association studies (GWAS).

**Mathematical Foundation:**
```
PGS = Σ(βᵢ × Gᵢ)
```
Where:
- `βᵢ` = Effect size of SNP i from GWAS
- `Gᵢ` = Genotype of SNP i (typically 0, 1, or 2 for homozygous/heterozygous reference/alternative)
- `Σ` = Sum across all included SNPs

### Key Characteristics

1. **Polygenic Nature**: Combines effects of hundreds to thousands of genetic variants
2. **Population-Specific**: Trained and validated in specific ancestral populations
3. **Continuous**: Represents a spectrum of genetic risk rather than binary outcomes
4. **Probabilistic**: Indicates increased probability, not certainty of developing the trait

## Why Polygenic Scores Are Important

### 1. Understanding Complex Trait Architecture

Polygenic scores help us understand the genetic architecture of complex traits by:
- **Quantifying Heritability**: Partitioning genetic variance explained by common variants
- **Identifying Missing Heritability**: Revealing what fraction of genetic risk remains unexplained
- **Revealing Genetic Complexity**: Showing how many variants contribute to each trait

### 2. Risk Stratification and Early Detection

**Clinical Applications:**
- **Early Intervention**: Identify high-risk individuals before symptom onset
- **Personalized Prevention**: Tailor screening and preventive measures based on genetic risk
- **Differential Diagnosis**: Help distinguish between conditions with overlapping symptoms

**Example in ADHD:**
- High polygenic scores may predict which children are most likely to develop ADHD symptoms
- Enables early behavioral interventions before full diagnostic criteria are met
- Helps identify children who may benefit from more frequent monitoring

### 3. Understanding Disease Mechanisms

Polygenic scores provide insights into:
- **Biological Pathways**: Enrichment analysis reveals which biological processes are involved
- **Developmental Timing**: When genetic effects become manifest across the lifespan
- **Gene-Environment Interactions**: How genetic risk interacts with environmental factors

## Why Polygenic Scores Are Better Than Diagnosis Alone

### 1. Earlier Detection

**Traditional Diagnosis Limitations:**
- Requires symptom manifestation (often years after genetic risk is present)
- Subjective diagnostic criteria
- Diagnostic delay due to waiting for symptom development

**Polygenic Score Advantages:**
- Can be calculated at birth (using genetic data)
- Predictive power years before clinical symptoms appear
- Objective, quantitative measure of genetic predisposition

### 2. Quantitative Risk Assessment

**Diagnosis vs. Polygenic Scores:**

| Aspect | Traditional Diagnosis | Polygenic Score |
|--------|---------------------|-----------------|
| **Timing** | After symptom onset | At any age (including birth) |
| **Nature** | Binary (yes/no diagnosis) | Continuous risk spectrum |
| **Precision** | Based on observable symptoms | Based on genetic predisposition |
| **Predictive Power** | Current status only | Future risk prediction |
| **Subjectivity** | Clinical judgment required | Objective calculation |

### 3. Personalized Medicine

**Polygenic Scores Enable:**
- **Risk-Adapted Screening**: More frequent monitoring for high-risk individuals
- **Preventive Interventions**: Early interventions for genetically susceptible individuals
- **Treatment Personalization**: Genetic information to guide treatment selection
- **Prognostic Information**: Understanding likely disease course and severity

### 4. Research Applications

**Advantages for Research:**
- **Population Stratification**: Control for genetic ancestry in association studies
- **Gene-Environment Interactions**: Study how environment modifies genetic risk
- **Subphenotype Identification**: Identify genetic subtypes within diagnostic categories
- **Endophenotype Mapping**: Link genetic risk to intermediate phenotypes

## How to Calculate Polygenic Scores

### Step 1: GWAS Discovery

**Requirements:**
- Large sample size (typically thousands to hundreds of thousands)
- Well-phenotyped population
- Adequate statistical power
- Proper quality control

**Key Considerations:**
- **Population Matching**: Training and validation populations should have similar ancestry
- **Phenotype Definition**: Clear, standardized phenotype definitions
- **Multiple Testing Correction**: Appropriate p-value thresholds (typically p < 5×10⁻⁸)

### Step 2: SNP Selection and Quality Control

**Inclusion Criteria:**
- Genome-wide significance (p < 5×10⁻⁸)
- Independent SNPs (pruned for linkage disequilibrium)
- Validated in discovery cohort

**Quality Control:**
- **Call Rate**: >95% genotype completion
- **Hardy-Weinberg Equilibrium**: p > 10⁻⁶
- **Minor Allele Frequency**: Typically >1%
- **Sample Relatedness**: Remove closely related individuals

### Step 3: Effect Size Estimation

**Statistical Methods:**
- **Linear Regression**: For continuous traits
- **Logistic Regression**: For binary traits
- **Mixed Models**: For related individuals or population structure
- **Meta-Analysis**: Combine results from multiple studies

**Effect Size Metrics:**
- **Beta Coefficients**: For continuous traits
- **Odds Ratios**: For binary traits
- **Variance Explained**: R² or proportion of variance

### Step 4: Score Calculation

**Basic Algorithm:**
```python
def calculate_polygenic_score(genotypes, effect_sizes):
    """
    Calculate polygenic score for an individual
    
    Parameters:
    genotypes: Array of genotypes (0,1,2) for each SNP
    effect_sizes: Array of effect sizes for each SNP
    
    Returns:
    polygenic_score: Sum of (genotype * effect_size) for all SNPs
    """
    return sum(genotype * effect_size for genotype, effect_size in zip(genotypes, effect_sizes))
```

**Advanced Methods:**
- **LD Pred**: Uses linkage disequilibrium information
- **PRSice**: Implements clumping and thresholding
- **LDPred**: Bayesian approach with LD information
- **SBayesR**: Hierarchical Bayesian approach

### Step 5: Validation and Calibration

**Validation Steps:**
1. **Internal Validation**: Split sample into discovery and validation sets
2. **External Validation**: Test in independent populations
3. **Cross-Validation**: Multiple iterations to ensure stability
4. **Calibration**: Ensure scores are properly scaled and interpretable

**Performance Metrics:**
- **Variance Explained**: R² for continuous traits
- **Area Under ROC Curve (AUC)**: For binary traits
- **Discriminatory Power**: Ability to distinguish cases from controls
- **Calibration**: Agreement between predicted and observed risk

### Step 6: Population-Specific Considerations

**Ancestry-Specific Issues:**
- **Transferability**: Scores trained in one population may not work in others
- **Allele Frequency Differences**: Different allele frequencies across populations
- **LD Patterns**: Different linkage disequilibrium structures
- **Environmental Factors**: Population-specific environmental influences

**Solutions:**
- **Population-Specific Training**: Train separate scores for each major ancestry group
- **Ancestry Adjustment**: Include principal components as covariates
- **Trans-ancestry Methods**: Use multi-ancestry GWAS and specialized methods

## Applications in ADHD Research

### ADHD Polygenic Score Performance

Based on the van der Laan et al. (2025) study:

| Polygenic Score Type | Variance Explained | Performance Rank | Best For |
|---------------------|-------------------|------------------|----------|
| **ADHDOVERALL** (Combined) | 0.3-3.1% | Best | General ADHD risk |
| **ADHDDIAG** (Diagnosis only) | 0.2-2.5% | Moderate | Clinical diagnosis |
| **ADHDSYMP** (Symptoms only) | 0.1-1.2% | Lowest | Symptom severity |

**Key Finding**: Combining ADHD symptoms with diagnosis data improves prediction accuracy by 2-3x.

### Clinical Utility in ADHD

**Risk Prediction:**
- **High-Risk Identification**: Top 10% of polygenic score distribution
- **Early Intervention**: Target screening and monitoring
- **Prognostic Information**: Predict likely symptom severity and course

**Treatment Implications:**
- **Pharmacogenomics**: Predict medication response based on genetic profile
- **Side Effect Risk**: Identify individuals at risk for medication side effects
- **Treatment Selection**: Guide choice of behavioral vs. pharmacological interventions

### Limitations in ADHD Context

**Technical Limitations:**
- **Small Effect Sizes**: Individual variants explain very little variance (0.1-1%)
- **Population Bias**: Primarily European ancestry limits generalizability
- **Missing Heritability**: Large portion of genetic risk not captured

**Clinical Limitations:**
- **Not Diagnostic**: Cannot diagnose ADHD on its own
- **Environmental Interactions**: Genetics is only one component
- **Developmental Dynamics**: Risk changes across development
- **Comorbidity**: Overlap with other psychiatric disorders

## Best Practices and Considerations

### Methodological Best Practices

1. **Sample Size**: Large discovery samples (>100,000) for better prediction
2. **Phenotype Quality**: Precise, well-validated phenotype definitions
3. **Population Matching**: Ensure training and validation populations match
4. **Statistical Rigor**: Proper multiple testing correction and validation
5. **Transparency**: Publicly share methods and results for reproducibility

### Ethical Considerations

**Privacy Concerns:**
- **Genetic Data Sensitivity**: Highly personal information
- **Data Security**: Robust protection of genetic information
- **Informed Consent**: Clear understanding of how data will be used

**Psychological Impact:**
- **Genetic Determinism**: Avoid implying genetics determines destiny
- **Anxiety**: Risk information may cause unnecessary worry
- **Stigma**: Potential for genetic discrimination

**Equity Issues:**
- **Health Disparities**: Ensure benefits are distributed equitably
- **Access to Testing**: Prevent exacerbation of existing health disparities
- **Ancestry Representation**: Include diverse populations in research

### Future Directions

1. **Improved Methods**: Better statistical methods for polygenic score calculation
2. **Rare Variants**: Integration of rare variant information
3. **Functional Annotation**: Incorporate biological function into scoring
4. **Multi-omics Integration**: Combine with epigenomic, transcriptomic data
5. **Dynamic Scores**: Age- and environment-specific risk prediction

## Common Misconceptions

| Myth | Reality |
|------|---------|
| **Polygenic scores can diagnose diseases** | Polygenic scores predict risk, not diagnosis |
| **Higher score always means disease will develop** | Probability, not certainty; environmental factors matter |
| **Scores are equally accurate across populations** | Population-specific training is required for accuracy |
| **Genetic risk is the only factor** | Environmental factors significantly modify genetic risk |
| **All variants in the score are causal** | Most are statistical proxies for causal variants |

## Related Concepts

- [[heritability]] - Genetic inheritance patterns in psychiatry
- [[adhd-risk-genes-effect-sizes]] - Specific genes associated with ADHD risk
- [[genome-wide-association]] - GWAS methodology and applications
- [[statistical-genetics]] - Statistical methods in genetic research
- [[precision-medicine]] - Personalized approaches to healthcare

## References

1. van der Laan, C. M. et al. (2025). Genome-wide association meta-analysis of childhood ADHD symptoms and diagnosis identifies new loci and potential effector genes. *Nature Genetics*, 57, 2427–2435. https://doi.org/10.1038/s41588-025-02295-y

2. Wray, N. R., et al. (2019). Polygenic risk scores for complex human traits: insights from large-scale GWAS. *Nature Reviews Genetics*, 20(4), 249-262. https://doi.org/10.1038/s41576-019-0094-5

3. Vassos, E., et al. (2017). Genetic linkage analysis in families with schizophrenia using polygenic risk scores. *Nature Neuroscience*, 20(2), 208-216. https://doi.org/10.1038/nn.4475

4. Dudbridge, F. (2013). Power and predictive accuracy of polygenic risk scores. *Genetic Epidemiology*, 37(5), 515-526. https://doi.org/10.1002/gepi.21708