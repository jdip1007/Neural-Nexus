---
title: Laboratory Verification
created: 2026-07-31
updated: 2026-07-31
type: concept
classification: laboratory.method-evaluation.quality
domain: laboratory
tags: [verification, clia, fda-approved-tests, performance-characteristics, method-evaluation]
sources: [raw/laboratory/accreditation/verification-validation-toolkit-aphl.md]
confidence: high
status: active
reviewed: 2026-07-31
---

# Laboratory Verification

Method verification is the process by which a laboratory confirms it can reproduce the manufacturer's claimed performance specifications for an FDA-approved, FDA-cleared, or FDA-modified test method.

## When Verification is Required

Verification is required when:
- Implementing a new FDA-approved/cleared test
- Implementing a new FDA-cleared test system
- Making minor modifications to an FDA-approved test
- Changing specimen type within manufacturer's claims
- Implementing on a new instrument platform (within manufacturer's claims)

**Verification is NOT required when:**
- Developing a laboratory-developed test (LDT)
- Making significant modifications to an FDA-approved test
- Implementing a test with no manufacturer performance claims

## Verification vs Validation

| Aspect | Verification | Validation |
|--------|-------------|------------|
| **Purpose** | Reproduce manufacturer claims | Establish performance characteristics |
| **Test Type** | FDA-approved/cleared tests | Laboratory-developed tests |
| **Data Source** | Manufacturer's claims | Laboratory-generated data |
| **Sample Size** | Minimum 40 samples | Larger sample size required |
| **Scope** | Limited to manufacturer claims | Comprehensive evaluation |
| **Documentation** | Summary report | Complete validation report |

## Required Performance Characteristics

### 1. Accuracy (Trueness)
**Purpose:** Confirm agreement with reference method or manufacturer claims

**Procedure:**
- Test minimum 40 patient specimens spanning reportable range
- Compare to reference method or expected values
- Include low, mid, and high concentrations

**Acceptance Criteria:**
- Percent agreement ≥ 95% (qualitative)
- Bias within ±10% of expected value (quantitative)
- Kappa statistic ≥ 0.75 for qualitative tests

**Statistical Methods:**
- Paired t-test (if data normally distributed)
- Deming regression (both methods have error)
- Bland-Altman plot (bias assessment)
- Passing-Bablok regression

### 2. Precision
**Purpose:** Confirm method repeatability and reproducibility

**Within-Run Precision (Repeatability):**
- Test 20 replicates in single run
- Calculate mean, SD, CV
- Acceptance: CV ≤ 5% (or manufacturer's claim)

**Between-Run Precision (Reproducibility):**
- Test samples over 20 different days
- Include different operators and reagent lots
- Calculate mean, SD, CV
- Acceptance: CV ≤ 7.5% (or manufacturer's claim)

**Total Precision:**
- Combine within-run and between-run components
- Use ANOVA to estimate variance components
- Acceptance: CV ≤ 10% (or manufacturer's claim)

### 3. Analytical Sensitivity (Limit of Detection)
**Purpose:** Confirm lowest concentration that can be reliably detected

**Procedure:**
- Test serial dilutions near manufacturer's LoD
- Test minimum 20 replicates at LoD
- Use probit analysis or alternative method

**Acceptance Criteria:**
- ≥ 19/20 (95%) positive at claimed LoD
- LoD consistent with manufacturer's claim
- Signal-to-noise ratio ≥ 3:1

**Alternative Method (for quantitative):**
- Limit of Quantitation (LoQ): CV ≤ 20% at LoQ
- Signal-to-noise ratio ≥ 10:1

### 4. Analytical Specificity
**Purpose:** Confirm freedom from interference and cross-reactivity

**Interference Testing:**
- Test common interfering substances at clinical levels
- Hemolysis (free hemoglobin up to 1000 mg/dL)
- Icterus (bilirubin up to 20 mg/dL)
- Lipemia (Intralipid up to 1000 mg/dL)
- Common medications at therapeutic levels

**Cross-Reactivity Testing:**
- Test structurally similar compounds
- Test at concentrations 10x expected maximum

**Acceptance Criteria:**
- Bias < 10% from baseline
- No clinically significant interference
- No false positives from cross-reacting substances

### 5. Reportable Range
**Purpose:** Confirm manufacturer's stated reportable range

**Procedure:**
- Test samples at low, mid, and high range points
- Verify linearity across range
- Test near range limits

**Acceptance Criteria:**
- Accurate results across entire range
- Bias within ±10% at all points
- r ≥ 0.99 for quantitative tests

### 6. Reference Interval
**Purpose:** Verify published reference interval

**Procedure:**
- Test 20 reference individuals
- Confirm ≥ 90% within published interval
- Verify interval is appropriate for population

**Acceptance Criteria:**
- ≥ 18/20 (90%) within published reference interval
- Interval appropriate for laboratory population

## Verification Process

### Phase 1: Planning
1. Review manufacturer's package insert
2. Document intended use of test
3. Establish acceptance criteria
4. Determine sample requirements
5. Create verification plan
6. Obtain plan approval

### Phase 2: Sample Acquisition
1. Obtain appropriate patient specimens
2. Ensure sample representativeness
3. Maintain sample integrity
4. Document sample sources

### Phase 3: Testing
1. Train personnel on method
2. Perform testing per protocol
3. Document all results
4. Track any deviations

### Phase 4: Analysis
1. Perform statistical calculations
2. Compare results to acceptance criteria
3. Identify any outliers
4. Document conclusions

### Phase 5: Reporting
1. Prepare summary report
2. Include all data and analysis
3. Document any deviations
4. Obtain final approvals

### Phase 6: Implementation
1. Update laboratory procedures
2. Train all staff
3. Establish QC parameters
4. Begin patient testing
5. Monitor ongoing performance

## Documentation Requirements

### Verification Plan
- Test method description
- Manufacturer performance claims
- Acceptance criteria
- Sample requirements
- Testing protocol
- Statistical analysis plan
- Timeline and responsibilities

### Summary Report
- Executive summary
- Test method verified
- Results for each performance characteristic
- Statistical analysis
- Comparison to acceptance criteria
- Conclusions
- Implementation date
- Approvals

## Common Pitfalls

### Insufficient Sample Size
- Problem: Using fewer than 40 samples for accuracy studies
- Solution: Follow minimum sample requirements

### Inadequate Sample Range
- Problem: Samples don't span reportable range
- Solution: Include low, mid, and high concentrations

### Wrong Statistical Methods
- Problem: Using inappropriate statistical tests
- Solution: Use appropriate methods (paired t-test, Deming regression)

### Not Following Manufacturer's Instructions
- Problem: Deviating from specified procedures
- Solution: Strictly follow manufacturer's recommendations

### Incomplete Documentation
- Problem: Missing data or analysis
- Solution: Document all activities and results

## Related

- [laboratory-validation](concepts/accreditation/laboratory-validation.md) — For laboratory-developed tests
- [clia-regulations](concepts/accreditation/clia-regulations.md) — 42 CFR §493.1253 verification requirements
- [method-performance](concepts/accreditation/method-performance.md) — All performance characteristics
- [quality-control](concepts/quality-control.md) — Ongoing monitoring after verification
- [Laboratory Accreditation](findings/index.md) — Accreditation requirements
- [fda-approval-process](concepts/fda-approval-process.md) — FDA test approval process
- [statistical-analysis](concepts/statistical-analysis.md) — Statistical methods for verification
- [reference-interval-verification](concepts/reference-interval-verification.md) — Reference interval verification
- [calibration-verification](concepts/calibration-verification.md) — Calibration confirmation
- [method-comparison](concepts/method-comparison.md) — Accuracy assessment methods

## Related Pages

- [[laboratory-developed-tests]]
- [[reference-interval-verification]]
- [[sample-requirements]]
