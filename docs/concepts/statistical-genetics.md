---
title: Statistical Genetics
created: 2026-08-06
updated: 2026-08-06
type: concept
classification: research-methodology.genetics
domain: research-methodology
tags: [statistical-genetics, genetics, quantitative-genetics, genetic-epidemiology, biostatistics, population-genetics, computational-biology]
sources: [raw/articles/adhd-genetics-nature-genetics-2025.md]
confidence: high
status: active
reviewed: 2026-08-06
backlinks: []
---

# Statistical Genetics

## Overview

Statistical genetics is the application of statistical methods to understand the genetic basis of traits and diseases. It provides the mathematical framework for analyzing genetic data, testing hypotheses about genetic effects, and making inferences about the genetic architecture of complex traits. This field bridges the gap between molecular genetics and population genetics, providing the tools necessary to interpret genetic data from modern high-throughput technologies.

## Definition and Scope

### What is Statistical Genetics?

Statistical genetics is the discipline that develops and applies statistical methods to:
- **Identify** genetic variants associated with traits
- **Quantify** the magnitude of genetic effects
- **Understand** the genetic architecture of complex traits
- **Predict** genetic risk and outcomes
- **Model** gene-environment interactions

### Core Areas

1. **Quantitative Genetics**: Study of continuous traits and their inheritance
2. **Population Genetics**: Study of genetic variation in populations
3. **Statistical Genomics**: Analysis of high-throughput genomic data
4. **Genetic Epidemiology**: Study of genetic factors in disease distribution
5. **Computational Genetics**: Development of algorithms for genetic analysis

## Fundamental Concepts

### Genetic Variation

#### Types of Genetic Variation

1. **Single Nucleotide Polymorphisms (SNPs)**:
   - Single base pair changes
   - Most common type of variation
   - Used in GWAS studies

2. **Insertions/Deletions (Indels)**:
   - Small insertions or deletions of DNA
   - Can have functional consequences

3. **Copy Number Variants (CNVs)**:
   - Larger duplications or deletations
   - Can affect gene dosage

4. **Structural Variants**:
   - Large-scale rearrangements
   - Chromosomal translocations, inversions

#### Genetic Variation Metrics

- **Minor Allele Frequency (MAF)**: Frequency of the less common allele
- **Heterozygosity**: Proportion of heterozygous individuals
- **Linkage Disequilibrium (LD)**: Non-random association of alleles at different loci

### Population Genetics Principles

#### Hardy-Weinberg Equilibrium

**Principle**: In a large, randomly mating population with no evolutionary forces, allele and genotype frequencies remain constant.

**Equation**: p² + 2pq + q² = 1

**Where**:
- p = frequency of allele A
- q = frequency of allele a
- p² = frequency of genotype AA
- 2pq = frequency of genotype Aa
- q² = frequency of genotype aa

#### Genetic Drift

**Definition**: Random change in allele frequencies due to sampling effects
**Impact**: Particularly strong in small populations
**Consequence**: Loss of genetic variation

#### Gene Flow

**Definition**: Movement of genes between populations
**Impact**: Reduces genetic differentiation
**Consequence**: Homogenizes allele frequencies

## Statistical Methods

### Association Testing

#### Single Variant Tests

**Binary Traits (Logistic Regression)**:
```
logit(P(disease)) = β₀ + β₁ × SNP + β₂ × covariates + ε
```

**Quantitative Traits (Linear Regression)**:
```
trait = β₀ + β₁ × SNP + β₂ × covariates + ε
```

**Interpretation**:
- β₁: Effect size (log-odds ratio for binary, mean difference for quantitative)
- SE(β₁): Standard error of effect size
- p-value: Statistical significance

#### Multiple Variant Tests

**Polygenic Risk Scores**:
```
PRS = Σ(βᵢ × Gᵢ)
```
Where βᵢ is the effect size and Gᵢ is the genotype for variant i

**Gene-Based Tests**:
- Aggregate effects of multiple variants within a gene
- Burden tests, SKAT, SKAT-O

### Population Structure Control

#### Principal Component Analysis (PCA)

**Purpose**: Identify and control for population stratification
**Method**: 
1. Calculate genetic relationship matrix
2. Perform eigenvalue decomposition
3. Use top principal components as covariates

#### Mixed Models

**Linear Mixed Model (LMM)**:
```
y = Xβ + Zu + ε
```
Where:
- y = phenotype vector
- X = fixed effects design matrix
- β = fixed effects coefficients
- Z = random effects design matrix
- u = random effects ~ N(0, σ²_g K)
- ε = residuals ~ N(0, σ²_e I)
- K = genetic relationship matrix

### Heritability Estimation

#### Twin Studies

**ACE Model**:
```
Variance = V_A + V_C + V_E
```
Where:
- V_A = Additive genetic variance
- V_C = Shared environmental variance
- V_E = Unique environmental variance

#### Genome-Based Methods

**GCTA (Genome-wide Complex Trait Analysis)**:
- Uses genome-wide SNP data to estimate heritability
- Relates genetic relatedness to phenotypic similarity

## Advanced Statistical Methods

### Machine Learning in Genetics

#### Regularization Methods

**Lasso (L1 Regularization)**:
```
minimize ||y - Xβ||² + λ||β||₁
```
- Performs variable selection
- Good for high-dimensional data

**Ridge (L2 Regularization)**:
```
minimize ||y - Xβ||² + λ||β||²
```
- Shrinks coefficients toward zero
- Good for multicollinearity

**Elastic Net**:
```
minimize ||y - Xβ||² + λ₁||β||₁ + λ₂||β||²
```
- Combines L1 and L2 penalties

#### Tree-Based Methods

**Random Forests**:
- Ensemble of decision trees
- Handles non-linear relationships
- Provides variable importance measures

**Gradient Boosting**:
- Sequential building of trees
- Optimizes for prediction accuracy
- Handles complex interactions

### Bayesian Methods

#### Bayesian GWAS

**Model**:
```
β ~ N(0, σ²_β)
p(y|β) ~ likelihood
p(β) ~ prior
```

**Advantages**:
- Incorporates prior knowledge
- Provides posterior probability estimates
- Better handles uncertainty

#### Bayesian Polygenic Risk Scores

**Hierarchical Models**:
- Model uncertainty in effect sizes
- Borrow strength across variants
- Provide probabilistic risk estimates

## Applications in Complex Traits

### ADHD Statistical Genetics

#### Effect Size Distribution

**Typical Effect Sizes**:
- **SNP Effects**: OR = 1.01-1.05 for common variants
- **Variance Explained**: 0.1-1% per variant
- **Total SNP Heritability**: ~11% for ADHD

#### Statistical Challenges in ADHD

1. **Phenotype Heterogeneity**:
   - Diagnostic variability
   - Subtype differences
   - Age-specific effects

2. **Missing Heritability**:
   - Rare variants not captured
   - Structural variants
   - Gene-environment interactions

3. **Population Stratification**:
   - Ancestry differences
   - Cultural factors
   - Environmental exposures

### Statistical Power Considerations

#### Sample Size Requirements

**Detection Power**:
```
n = (Z₁₋α/₂ + Z₁₋β)² × (σ²/β²)
```
Where:
- Z₁₋α/₂ = critical value for significance level
- Z₁₋β = critical value for power (1-β)
- σ² = phenotypic variance
- β = effect size

**ADHD GWAS Power**:
- **Small Effects (OR = 1.05)**: Requires >100,000 samples
- **Moderate Effects (OR = 1.1)**: Requires ~50,000 samples
- **Large Effects (OR = 1.2)**: Requires ~20,000 samples

#### Multiple Testing Burden

**Challenge**: Testing millions of variants simultaneously
**Solutions**:
- **Bonferroni Correction**: p < 5×10⁻⁸
- **False Discovery Rate**: Control expected proportion of false positives
- **Permutation Testing**: Empirical p-value calculation

## Quality Control and Data Processing

### Genotype Quality Control

#### Sample-Level QC

**Criteria**:
- **Call Rate**: >95% genotyped variants
- **Sex Check**: Concordance with reported sex
- **Relatedness**: Remove one from pairs with PI_HAT > 0.125
- **Population Outliers**: Remove based on PCA

#### Variant-Level QC

**Criteria**:
- **Call Rate**: >95% samples genotyped
- **Hardy-Weinberg**: p > 10⁻⁶ in controls
- **Minor Allele Frequency**: >1% (adjust based on study goals)
- **Missingness**: No systematic patterns

### Imputation

#### Reference Panels

**Common References**:
- **1000 Genomes Project**: Global diversity
- **Haplotype Reference Consortium**: Dense coverage
- **UK Biobank**: Large, diverse sample

#### Imputation Methods

**Statistical Methods**:
- **MaCH**: Hidden Markov model
- **IMPUTE2**: Bayesian haplotype-based
- **Minimac4**: Fast, accurate imputation

**Quality Metrics**:
- **Info Score**: Measure of imputation accuracy
- **R²**: Correlation between imputed and true genotypes

## Statistical Software and Tools

### GWAS Software

**Popular Packages**:
- **PLINK**: Standard GWAS analysis
- **GCTA**: Heritability estimation
- **SAIGE**: Scalable analysis for binary traits
- **REGENIE**: Fast, scalable GWAS

**R Packages**:
- **GWASTools**: Comprehensive GWAS analysis
- **SNPRelate**: Large-scale genetic data analysis
- **GAPIT**: Genome-wide association analysis

### Visualization Tools

**Manhattan Plots**:
- Display GWAS results
- Highlight significant associations
- Show chromosome positions

**Q-Q Plots**:
- Assess inflation of test statistics
- Check for population structure
- Evaluate multiple testing correction

## Best Practices

### Study Design

1. **Power Analysis**: Calculate required sample sizes
2. **Population Matching**: Ensure training and validation populations match
3. **Phenotype Definition**: Use clear, standardized criteria
4. **Replication**: Independent validation samples

### Statistical Analysis

1. **Multiple Testing**: Appropriate correction methods
2. **Population Structure**: Adequate control methods
3. **Confounding**: Account for known confounders
4. **Sensitivity Analysis**: Test robustness of results

### Reporting Standards

1. **FAIR Principles**: Findable, Accessible, Interoperable, Reusable
2. **Open Science**: Share data and code
3. **Pre-registration**: Register study design and analysis plans
4. **Reproducibility**: Provide detailed methods and code

## Common Statistical Issues

### Population Stratification

**Problem**: Spurious associations due to population differences
**Solutions**: PCA, mixed models, stratified analysis

### Confounding

**Problem**: Variables that affect both genotype and phenotype
**Solutions**: Include covariates, matched sampling, instrumental variables

### Multiple Testing

**Problem**: Increased false positives due to many tests
**Solutions**: Bonferroni, FDR, permutation testing

### Heterogeneity

**Problem**: Different effects across subgroups
**Solutions**: Subgroup analysis, meta-analysis, interaction tests

## Future Directions

### Methodological Advances

1. **Rare Variant Analysis**: Whole-genome sequencing, burden tests
2. **Gene-Environment Interactions**: G×E studies, epigenetics
3. **Multi-omics Integration**: Combine genomic, transcriptomic, proteomic data
4. **Machine Learning**: Deep learning, neural networks for genetic data

### Computational Challenges

1. **Big Data**: Handling massive datasets
2. **Cloud Computing**: Scalable analysis pipelines
3. **Reproducible Research**: Containerized workflows
4. **Real-time Analysis**: Stream processing of genetic data

## Related Concepts

- [[polygenic-scores]] - Statistical methods for genetic risk prediction
- [[heritability]] - Quantifying genetic contribution to traits
- [[genome-wide-association]] - GWAS methodology and applications
- [[genetic-epidemiology]] - Study of genetic factors in populations
- [[precision-medicine]] - Personalized approaches to healthcare

## References

1. van der Laan, C. M. et al. (2025). Genome-wide association meta-analysis of childhood ADHD symptoms and diagnosis identifies new loci and potential effector genes. *Nature Genetics*, 57, 2427–2435. https://doi.org/10.1038/s41588-025-02295-y

2. Visscher, P. M., et al. (2017). 10 years of GWAS discovery: biology, function, and translation. *American Journal of Human Genetics*, 94(1), 8-14. https://doi.org/10.1016/j.ajhg.2012.11.012

3. Yang, J., et al. (2010). Common SNPs explain a large proportion of the heritability for human height. *Nature Genetics*, 42(7), 565-569. https://doi.org/10.1038/ng.608

4. Balding, D. J. (2006). A tutorial on statistical methods for population association studies. *Nature Reviews Genetics*, 7(10), 781-791. https://doi.org/10.1038/nrg1964