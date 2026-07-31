---
title: Method Evaluation Decision Flow
created: 2026-07-31
updated: 2026-07-31
type: concept
classification: laboratory.method-evaluation.workflow
domain: laboratory
tags: [decision-flow, verification-vs-validation, method-evaluation, clia-requirements]
sources: [raw/laboratory/accreditation/verification-validation-toolkit-aphl.md]
confidence: high
status: active
reviewed: 2026-07-31
---

# Method Evaluation Decision Flow

Systematic approach for determining whether verification or validation is required when implementing a new laboratory test method.

## Primary Decision Tree

```
START
  │
  ▼
Is the test FDA-approved, FDA-cleared, or FDA-modified?
  │
  ├── YES ──→ Is it being used exactly as described in manufacturer's instructions?
  │              │
  │              ├── YES ──→ VERIFICATION required
  │              │              (Reproduce manufacturer claims)
  │              │
  │              └── NO ──→ Have there been significant modifications?
  │                          │
  │                          ├── YES ──→ VALIDATION required
  │                          │              (Establish new performance)
  │                          │
  │                          └── NO ──→ VERIFICATION required
  │                                      (Minor changes only)
  │
  └── NO ──→ Is it a laboratory-developed test (LDT)?
              │
              ├── YES ──→ VALIDATION required
              │              (Establish performance characteristics)
              │
              └── NO ──→ Investigate test source
                          (May still require validation)
```

## Detailed Decision Criteria

### 1. Test Source Identification

**FDA-Approved Tests:**
- Received 510(k) clearance
- Received PMA approval
- Listed on FDA database
- Manufacturer provides performance claims

**FDA-Cleared Tests:**
- Substantially equivalent to predicate device
- Received 510(k) clearance
- Manufacturer provides performance claims

**FDA-Modified Tests:**
- FDA-approved test modified by laboratory
- Minor modifications within scope
- Some performance claims available

**Laboratory-Developed Tests (LDTs):**
- Designed and developed in laboratory
- No manufacturer performance claims
- Novel methodology or application
- Not listed on FDA database

### 2. Modification Assessment

**Minor Modifications (Verification Required):**
- Change in specimen collection tube
- Change in specimen volume (within acceptable range)
- Change in storage time (within stability limits)
- Minor software update (no algorithm change)
- Change in reporting format only
- Change in specimen type within manufacturer claims

**Significant Modifications (Validation Required):**
- Change in specimen type outside manufacturer claims
- Change in analytical principle
- Modification to critical reagents
- Significant software algorithm change
- Change in instrument platform
- Extension of reportable range beyond claims
- Combination of multiple tests into new test
- Change in clinical interpretation criteria

### 3. Special Considerations

**Companion Diagnostics:**
- May require validation even if FDA-approved
- Therapeutic implications require careful assessment

**High-Complexity Tests:**
- Often require more thorough evaluation
- May need additional validation studies

**Novel Biomarkers:**
- Even if using FDA-approved platform, may require validation

**Multiplex Panels:**
- Individual components may be FDA-approved
- Panel as whole may require validation
- Depends on panel composition and claims

## Verification Requirements

### When Required
- Implementing new FDA-approved/cleared test
- Implementing new FDA-cleared test system
- Making minor modifications within manufacturer claims
- Changing specimen type within manufacturer claims

### Performance Characteristics to Verify
- Accuracy (bias)
- Precision (repeatability, reproducibility)
- Reportable range
- Reference interval

### Sample Requirements
- Accuracy: minimum 40 samples spanning range
- Precision: minimum 20 replicates
- Reference interval: minimum 20 reference individuals

### Acceptance Criteria
- Use manufacturer's claimed performance
- Verify laboratory can reproduce claims
- Document comparison to claims

## Validation Requirements

### When Required
- Developing laboratory-developed test (LDT)
- Making significant modifications to FDA-approved test
- Implementing test without manufacturer claims
- Changing specimen type outside manufacturer claims
- Modifying test algorithm or interpretation
- Combining multiple test systems into new test

### Performance Characteristics to Establish
- Accuracy (bias)
- Precision (repeatability, reproducibility)
- Analytical sensitivity (LoD, LoQ)
- Analytical specificity (interference, cross-reactivity)
- Reportable range (linearity)
- Reference interval (establishment)
- Clinical performance (if applicable)

### Sample Requirements
- Accuracy: minimum 100-200 samples
- Precision: minimum 20-30 replicates, multiple runs
- LoD: minimum 20 replicates at multiple concentrations
- Reference interval: minimum 120 reference individuals

### Acceptance Criteria
- Based on clinical requirements
- Established during validation
- Documented justification

## Documentation Requirements

### Verification Documentation
1. **Verification Plan**
   - Test method description
   - Manufacturer performance claims
   - Acceptance criteria
   - Sample requirements
   - Testing protocol
   - Statistical analysis plan

2. **Summary Report**
   - Executive summary
   - Results for each characteristic
   - Statistical analysis
   - Comparison to claims
   - Conclusions
   - Approvals

### Validation Documentation
1. **Validation Protocol**
   - Introduction and rationale
   - Method description
   - Performance characteristics
   - Acceptance criteria
   - Sample requirements
   - Testing protocols
   - Statistical methods

2. **Validation Report**
   - Executive summary
   - Background and rationale
   - Methods and protocols
   - Detailed results
   - Statistical analysis
   - Discussion
   - Conclusions
   - Approvals

## Common Decision Points

### Scenario 1: New FDA-Approved Test
**Decision:** Verification required
**Rationale:** FDA-approved test, used per manufacturer instructions
**Requirements:** Verify accuracy, precision, reportable range, reference interval

### Scenario 2: Modified FDA-Approved Test (Minor)
**Decision:** Verification required
**Rationale:** Minor modification within manufacturer claims
**Requirements:** Verify all performance characteristics

### Scenario 3: Modified FDA-Approved Test (Significant)
**Decision:** Validation required
**Rationale:** Significant modification outside manufacturer claims
**Requirements:** Establish all performance characteristics

### Scenario 4: Laboratory-Developed Test
**Decision:** Validation required
**Rationale:** No manufacturer performance claims
**Requirements:** Establish all performance characteristics

### Scenario 5: New Specimen Type (Within Claims)
**Decision:** Verification required
**Rationale:** Specimen type included in manufacturer claims
**Requirements:** Verify performance with new specimen type

### Scenario 6: New Specimen Type (Outside Claims)
**Decision:** Validation required
**Rationale:** Specimen type not included in manufacturer claims
**Requirements:** Establish all performance characteristics

### Scenario 7: Software Update (Minor)
**Decision:** Limited verification required
**Rationale:** Minor update, no algorithm change
**Requirements:** Verify with 20 samples

### Scenario 8: Software Update (Major)
**Decision:** Re-verification or re-validation required
**Rationale:** Major update, algorithm change
**Requirements:** Assess impact, may need full re-validation

## Related

- [[laboratory-verification]] — Verification process details
- [[laboratory-validation]] — Validation process details
- [[clia-regulations]] — 42 CFR §493.1253 requirements
- [[method-performance]] — Performance characteristics
- [[laboratory-developed-tests]] — LDT evaluation
- [[bridging-studies]] — Evaluating modifications
- [[change-control]] — Managing test changes
- [[method-implementation]] — Implementation process
- [[regulatory-compliance]] — Ensuring compliance