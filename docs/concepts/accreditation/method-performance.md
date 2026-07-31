---
title: Method Performance Characteristics
created: 2026-07-31
updated: 2026-07-31
type: concept
classification: laboratory.method-evaluation.quality
domain: laboratory
tags: [performance-characteristics, accuracy, precision, sensitivity, specificity, analytical-validation]
sources: [raw/laboratory/accreditation/verification-validation-toolkit-aphl.md]
confidence: high
status: active
reviewed: 2026-07-31
---

# Method Performance Characteristics

Performance characteristics are the measurable attributes that define how well a test method performs. All laboratory tests must have documented performance characteristics before patient testing begins.

## Required Characteristics (CLIA 42 CFR §493.1253)

### For FDA-Approved Tests (Verification)
All must be verified:
- Accuracy
- Precision
- Reportable Range
- Reference Interval

### For Laboratory-Developed Tests (Validation)
All must be established:
- Accuracy
- Precision
- Analytical Sensitivity
- Analytical Specificity
- Reportable Range
- Reference Interval

## 1. Accuracy (Trueness)

**Definition:** The closeness of agreement between a test result and the true value or reference method result.

**Qualitative Tests:**
- Percent agreement with reference method
- Sensitivity (true positive rate)
- Specificity (true negative rate)
- Positive Predictive Value (PPV)
- Negative Predictive Value (NPV)
- Kappa statistic (agreement beyond chance)

**Quantitative Tests:**
- Bias (difference from reference value)
- Recovery (percent of expected value)
- Correlation coefficient (r)
- Regression analysis parameters

**Acceptance Criteria:**
- Percent agreement ≥ 95%
- Sensitivity ≥ 95%
- Specificity ≥ 95%
- Kappa ≥ 0.75
- Bias within ±10%
- r ≥ 0.95

**Statistical Methods:**
- Paired t-test (normal distribution)
- Wilcoxon signed-rank test (non-parametric)
- Deming regression (both methods have error)
- Passing-Bablok regression
- Bland-Altman analysis
- Contingency tables (2×2 for qualitative)

## 2. Precision

**Definition:** The closeness of agreement between independent test results obtained under prescribed conditions.

### Types of Precision

**Repeatability (Within-Run Precision):**
- Same operator, same instrument, same reagents, same day
- Reflects random error under optimal conditions
- Minimum 20 replicates

**Reproducibility (Between-Run Precision):**
- Different operators, different days, possibly different reagents
- Reflects total random error in routine conditions
- Minimum 20 runs over 20 days

**Total Precision:**
- Combination of within-run and between-run components
- Estimated using ANOVA
- Variance components approach

**Statistical Analysis:**
```
Mean = Σx/n
Standard Deviation (SD) = √[Σ(x-mean)²/(n-1)]
Coefficient of Variation (CV) = (SD/mean) × 100%

ANOVA for Total Precision:
Within-run variance (s²_wr)
Between-run variance (s²_br)
Total variance = s²_wr + s²_br
Total CV = (√Total variance/mean) × 100%
```

**Acceptance Criteria:**
- Within-run CV ≤ 5%
- Between-run CV ≤ 7.5%
- Total CV ≤ 10%
- Based on clinical needs and manufacturer claims

## 3. Analytical Sensitivity

**Definition:** The lowest amount of analyte that can be reliably detected or measured.

### Limit of Detection (LoD)
- Lowest concentration that can be detected with 95% confidence
- Does not necessarily allow quantification
- Determined using probit analysis

**Procedure:**
1. Prepare serial dilutions near expected LoD
2. Test minimum 20 replicates at each concentration
3. Use probit regression to determine LoD (95% detection)
4. Include negative controls

**Alternative Method:**
- Test 20 replicates at candidate LoD
- ≥ 19/20 (95%) positive = acceptable LoD

### Limit of Quantitation (LoQ)
- Lowest concentration that can be quantified with acceptable precision
- CV ≤ 20% at LoQ
- Signal-to-noise ratio ≥ 10:1

**Determination:**
- Test replicates at low concentrations
- Identify concentration where CV ≤ 20%
- Confirm accuracy at LoQ

**Acceptance Criteria:**
- LoD suitable for clinical needs
- LoQ allows reliable clinical decision-making
- Signal-to-noise: ≥ 3:1 for LoD, ≥ 10:1 for LoQ

## 4. Analytical Specificity

**Definition:** The ability of a method to measure only the analyte of interest, free from interference.

### Interference Testing
**Common Interferents:**
- Hemoglobin (up to 1000 mg/dL)
- Bilirubin (up to 20 mg/dL)
- Lipids (Intralipid up to 1000 mg/dL)
- Common medications at therapeutic levels
- pH variations
- Endogenous substances (uric acid, albumin, etc.)

**Procedure:**
1. Spike samples with potential interferents
2. Test at clinical concentrations
3. Compare to baseline (no interferent)
4. Document any bias

**Acceptance:**
- Bias < 10% from baseline
- No clinically significant interference

### Cross-Reactivity Testing
**Purpose:** Identify substances that may cause false positives

**Procedure:**
1. Test structurally related compounds
2. Test at concentrations 10-100x expected maximum
3. Document any cross-reaction

**Acceptance:**
- No false positives at expected clinical concentrations
- Cross-reactivity only at supratherapeutic levels

### Carryover Testing
**Purpose:** Ensure no contamination between samples

**Procedure:**
1. Test high-concentration sample
2. Follow with negative sample
3. Repeat 5-10 times
4. Measure residual signal

**Acceptance:**
- No significant carryover
- Typically < 1% of high concentration

## 5. Reportable Range

**Definition:** The range of analyte concentrations that can be measured with acceptable accuracy and precision.

### Linearity Studies
**Procedure:**
1. Prepare 5-7 concentrations spanning expected range
2. Test in triplicate
3. Perform linear regression analysis
4. Assess linearity, lack-of-fit

**Statistical Analysis:**
```
Linear Regression: y = mx + b
Correlation coefficient: r
Coefficient of determination: r²
Lack-of-fit test (ANOVA)
Polynomial regression (if needed)
```

**Acceptance Criteria:**
- Linear relationship across range
- r ≥ 0.99 or r² ≥ 0.98
- No significant lack-of-fit (p > 0.05)
- Maximum allowable error within clinical requirements

### Range Extension
**When Required:**
- Clinical need beyond current range
- New applications requiring extended range

**Procedure:**
- Additional validation study
- Document extension protocol
- Establish acceptance criteria

## 6. Reference Interval

**Definition:** The range of test values expected for healthy individuals.

### Verification (FDA-approved tests)
**Purpose:** Confirm published interval is appropriate

**Procedure:**
- Test 20 reference individuals
- Confirm ≥ 90% within published interval
- Document any outliers

**Acceptance Criteria:**
- ≥ 18/20 (90%) within published interval
- Interval appropriate for laboratory population

### Establishment (LDTs)
**Purpose:** Create new reference interval

**Sample Requirements:**
- Minimum 120 reference individuals
- Appropriate population characteristics
- Exclude individuals with conditions affecting test

**Statistical Analysis:**
- Non-parametric: 2.5th to 97.5th percentiles
- Parametric: mean ± 2 SD (if normally distributed)
- Partitioning: if significant differences between groups

**Considerations:**
- Age-specific intervals (pediatric, geriatric)
- Sex-specific intervals (hormones, enzymes)
- Ethnicity-specific intervals (if significant differences)
- Pregnancy-specific intervals (if applicable)

**Acceptance Criteria:**
- Sufficient sample size (≥ 120)
- Appropriate reference population
- Clinically useful decision points
- Documented rationale

## 7. Additional Characteristics (for Complex Tests)

### Diagnostic Performance (for LDTs)
- Sensitivity and specificity vs clinical diagnosis
- ROC curve analysis
- Area Under Curve (AUC)
- Optimal cut-off determination
- Predictive values (considering prevalence)

### Carryover and Contamination
- High-to-low carryover
- Sample-to-sample contamination
- Environmental contamination
- Reagent contamination

### Recovery
- Percent recovery of known concentrations
- Matrix effects
- Dilution integrity

### Ruggedness/Robustness
- Effect of minor deliberate variations
- Operator variations
- Day-to-day variations
- Instrument variations

### Turnaround Time
- Pre-analytic time
- Analytic time
- Post-analytic time
- Total turnaround time

## Statistical Methods Summary

| Characteristic | Qualitative | Quantitative |
|---------------|------------|--------------|
| Accuracy | 2×2 tables, kappa, Se/Sp | Regression, bias, r |
| Precision | Percent agreement | SD, CV, ANOVA |
| Sensitivity | Probit analysis | Probit/serial dilution |
| Specificity | Interference studies | Interference studies |
| Reportable Range | Confirm manufacturer | Linearity study |
| Reference Interval | 20 samples | 120 samples |

## Common Pitfalls

### Insufficient Sample Size
- Problem: Underpowered studies
- Solution: Follow minimum requirements

### Inappropriate Statistical Methods
- Problem: Using wrong tests
- Solution: Use appropriate methods based on data

### Not Spanning Range
- Problem: Samples don't cover reportable range
- Solution: Include low, mid, high concentrations

### Wrong Reference Method
- Problem: Using suboptimal comparison
- Solution: Use gold standard or validated method

### Not Considering Clinical Needs
- Problem: Acceptance criteria too lenient
- Solution: Base on clinical requirements

## Related

- [[laboratory-verification]] — Verifying manufacturer claims
- [[laboratory-validation]] — Establishing performance for LDTs
- [[clia-regulations]] — 42 CFR §493.1253 requirements
- [[statistical-analysis]] — Statistical methods
- [[reference-interval-verification]] — Reference interval procedures
- [[diagnostic-accuracy]] — Diagnostic performance metrics
- [[roc-analysis]] — ROC curve methodology
- [[quality-control]] — Ongoing performance monitoring