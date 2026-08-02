---
title: Laboratory Validation
created: 2026-07-31
updated: 2026-07-31
type: concept
classification: laboratory.method-evaluation.quality
domain: laboratory
tags: [validation, laboratory-developed-tests, ldt, performance-characteristics, method-development]
sources: [raw/laboratory/accreditation/verification-validation-toolkit-aphl.md]
confidence: high
status: active
reviewed: 2026-07-31
---

# Laboratory Validation

Method validation is the process by which a laboratory establishes and documents the performance characteristics of a laboratory-developed test (LDT) or a test that has been significantly modified beyond manufacturer claims.

## When Validation is Required

Validation is required when:
- Developing a new laboratory-developed test (LDT)
- Making significant modifications to an FDA-approved test
- Using a test without manufacturer performance claims
- Combining multiple test systems into a new test
- Adapting a test for a new specimen type (outside manufacturer claims)
- Modifying test algorithm or interpretation criteria

**Examples requiring validation:**
- Modifying an FDA-approved molecular assay for new targets
- Developing an in-house multiplex PCR panel
- Creating a new mass spectrometry application
- Modifying specimen collection procedures
- Changing test methodology significantly

## Validation vs Verification

| Aspect | Verification | Validation |
|--------|-------------|------------|
| **Purpose** | Reproduce manufacturer claims | Establish performance characteristics |
| **Test Type** | FDA-approved/cleared tests | Laboratory-developed tests (LDTs) |
| **Data Source** | Manufacturer's claims | Laboratory-generated data |
| **Sample Size** | Minimum 40 samples | Larger sample size (often 100+) |
| **Scope** | Limited to manufacturer claims | Comprehensive evaluation |
| **Complexity** | Moderate | High |
| **Documentation** | Summary report | Complete validation report with protocol |
| **Regulatory** | 42 CFR §493.1253(b) | 42 CFR §493.1253(c) |

## Required Performance Characteristics

### 1. Accuracy (Trueness)
**Purpose:** Establish agreement with reference method or truth

**Procedure:**
- Test minimum 100-200 patient specimens spanning reportable range
- Compare to reference method or gold standard
- Include low, mid, and high concentrations
- For定性 tests, include positive, negative, and equivocal samples

**Statistical Analysis:**
- Paired t-test or non-parametric equivalent
- Deming regression
- Bland-Altman analysis
- Passing-Bablok regression
- Sensitivity, specificity, PPV, NPV (for qualitative)

**Acceptance Criteria:**
- Sensitivity ≥ 95% (qualitative)
- Specificity ≥ 95% (qualitative)
- Kappa ≥ 0.75 (qualitative)
- Bias within ±10% (quantitative)
- r ≥ 0.95 (quantitative)

### 2. Precision
**Purpose:** Determine method repeatability and reproducibility

**Within-Run Precision (Repeatability):**
- Test 20-30 replicates in single run
- Test multiple concentration levels
- Calculate mean, SD, CV

**Between-Run Precision (Reproducibility):**
- Test samples over 20-30 different days
- Include different operators, instruments, reagent lots
- Test 2-3 replicates per run
- Calculate mean, SD, CV

**Total Precision:**
- Use ANOVA to estimate variance components
- Combine within-run and between-run variance
- Calculate total CV

**Acceptance Criteria:**
- Within-run CV ≤ 5%
- Between-run CV ≤ 7.5%
- Total CV ≤ 10%
- Based on clinical needs for test

### 3. Analytical Sensitivity
**Purpose:** Determine lowest concentration that can be reliably detected (LoD) or quantified (LoQ)

**Limit of Detection (LoD):**
- Prepare serial dilutions near expected detection limit
- Test minimum 20 replicates at each concentration
- Use probit analysis to determine LoD (95% detection probability)
- Include negative controls

**Limit of Quantitation (LoQ):**
- Determine lowest concentration with acceptable precision
- Test replicates at low concentrations
- Identify concentration where CV ≤ 20%
- Confirm accuracy at LoQ

**Acceptance Criteria:**
- LoD suitable for clinical application
- LoQ allows reliable quantification
- Signal-to-noise ratio: ≥ 3:1 for LoD, ≥ 10:1 for LoQ

### 4. Analytical Specificity
**Purpose:** Establish freedom from interference and cross-reactivity

**Interference Testing:**
- Test 20-30 potentially interfering substances
- Test at clinically relevant concentrations
- Include:
  - Hemoglobin (up to 1000 mg/dL)
  - Bilirubin (up to 20 mg/dL)
  - Lipids (Intralipid up to 1000 mg/dL)
  - Common medications at therapeutic and toxic levels
  - Endogenous substances

**Cross-Reactivity Testing:**
- Test structurally related compounds
- Test at concentrations 10-100x expected maximum
- Include common cross-reacting substances

**Carryover Testing:**
- Test high-concentration sample followed by negative sample
- Repeat with multiple high-negative pairs
- Measure any residual signal

**Acceptance Criteria:**
- Bias < 10% from baseline
- No false positives from cross-reactivity
- No clinically significant interference
- No significant carryover

### 5. Reportable Range
**Purpose:** Establish valid measurement range

**Linearity Study:**
- Prepare samples at 5-7 concentrations spanning expected range
- Test in triplicate
- Perform linear regression analysis
- Assess linearity, lack-of-fit, polynomial terms

**Acceptance Criteria:**
- Linear relationship across range
- r ≥ 0.99 or r² ≥ 0.98
- No significant deviation from linearity
- Maximum allowable error within clinical requirements

**Extension Studies:**
- If needed, extend range with additional validation
- Document extension process

### 6. Reference Interval
**Purpose:** Establish expected results in healthy population

**Establishment Requirements:**
- Test minimum 120 reference individuals
- Use appropriate reference population
- Consider age, sex, ethnicity factors
- Exclude individuals with conditions affecting test

**Statistical Analysis:**
- Non-parametric method (2.5th-97.5th percentile)
- Parametric method (if data normally distributed)
- Partitioning if significant differences between groups

**Acceptance Criteria:**
- Appropriate for intended population
- Clinically useful decision points
- Supported by adequate sample size

### 7. Clinical Performance (if applicable)
**Purpose:** Establish clinical utility and performance

**Diagnostic Sensitivity and Specificity:**
- Compare to clinical diagnosis
- Test well-characterized patient samples
- Calculate sensitivity and specificity

**ROC Analysis:**
- Receiver Operating Characteristic curve
- Determine optimal cut-off values
- Calculate area under curve (AUC)

**Predictive Values:**
- Positive and negative predictive values
- Consider disease prevalence

**Acceptance Criteria:**
- Adequate sensitivity and specificity for intended use
- AUC ≥ 0.8 for good diagnostic performance
- Predictive values suitable for clinical population

## Validation Protocol

### 1. Introduction
- Purpose and scope of validation
- Test method description
- Intended clinical use
- Rationale for LDT development

### 2. Method Development
- Description of development process
- Reagents and materials
- Equipment and instrumentation
- Software and algorithms
- Critical reagents and controls

### 3. Performance Characteristics
- Detailed protocols for each characteristic
- Acceptance criteria
- Sample requirements
- Statistical analysis methods

### 4. Resources
- Personnel and qualifications
- Equipment specifications
- Reagent sources
- Timeline

### 5. Documentation
- Data collection forms
- Report templates
- QC requirements
- Ongoing monitoring plan

### 6. Regulatory Considerations
- CLIA requirements
- State regulations
- Payer requirements
- Other applicable regulations

## Validation Report

### 1. Executive Summary
- Test method validated
- Overall conclusion
- Implementation recommendation

### 2. Background
- Test method description
- Rationale for development
- Clinical need

### 3. Methods
- Validation protocols
- Sample descriptions
- Testing procedures
- Statistical analysis

### 4. Results
- Detailed results for each performance characteristic
- Statistical analysis
- Comparison to acceptance criteria
- Graphs and tables

### 5. Discussion
- Interpretation of results
- Any deviations from protocol
- Limitations
- Clinical relevance

### 6. Conclusions
- Overall assessment
- Recommendations for implementation
- Ongoing monitoring requirements

### 7. Appendices
- Raw data
- Statistical calculations
- Protocol deviations
- Approvals

## Special Considerations for LDTs

### Regulatory Landscape
- FDA oversight of LDTs evolving
- CLIA requires validation
- State regulations may apply
- Payer requirements for coverage

### Documentation Requirements
- Comprehensive method documentation
- Validation protocol and report
- Ongoing performance monitoring
- Change control procedures

### Quality Management
- Robust QC program
- Proficiency testing (if available)
- Ongoing verification
- Regular review

### Revalidation Requirements
- Significant changes to method
- New software versions
- New reagent lots
- Equipment changes
- Clinical need changes

## Common Pitfalls

### Insufficient Validation
- Problem: Inadequate sample size or scope
- Solution: Follow comprehensive validation guidelines

### Inappropriate Reference Method
- Problem: Using suboptimal comparison method
- Solution: Use gold standard or well-validated method

### Poor Statistical Analysis
- Problem: Using incorrect statistical methods
- Solution: Use appropriate statistical techniques

### Inadequate Documentation
- Problem: Missing or incomplete documentation
- Solution: Maintain comprehensive records

### Not Establishing Ongoing Monitoring
- Problem: No ongoing verification after implementation
- Solution: Establish ongoing QC and monitoring program

## Related

- [laboratory-verification](concepts/accreditation/laboratory-verification.md) — For FDA-approved tests
- [clia-regulations](concepts/accreditation/clia-regulations.md) — 42 CFR §493.1253 validation requirements
- [method-performance](concepts/accreditation/method-performance.md) — All performance characteristics
- [laboratory-developed-tests](concepts/accreditation/laboratory-developed-tests.md) — LDT overview
- [quality-control](concepts/quality-control.md) — Ongoing monitoring
- [fda-ldt-oversight](concepts/fda-ldt-oversight.md) — FDA LDT policy
- [bioinformatics-validation](concepts/bioinformatics-validation.md) — Validation of bioinformatics pipelines
- [ngs-validation](concepts/ngs-validation.md) — NGS-specific validation requirements
- [clinical-utility](concepts/clinical-utility.md) — Establishing clinical performance
- [method-development](concepts/method-development.md) — LDT development process