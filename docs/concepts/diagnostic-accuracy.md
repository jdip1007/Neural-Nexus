---
title: Diagnostic Accuracy
created: 2026-07-31
updated: 2026-07-31
type: concept
classification: laboratory.method-evaluation
domain: laboratory
tags: [diagnostic-accuracy, sensitivity, specificity, roc-analysis, statistical-analysis]
sources: []
confidence: high
status: active
reviewed: 2026-07-31
---

# Diagnostic Accuracy

## Definition

Diagnostic accuracy refers to the degree of agreement between a test's results and a reference standard (the "gold standard") for a given condition or analyte. It quantifies how correctly a laboratory or clinical test distinguishes between positive and negative cases, combining sensitivity (true positive rate) and specificity (true negative rate) into an overall measure of test performance.

## Key Points

- **Sensitivity** measures the proportion of true positives correctly identified by the test. Low sensitivity produces false negatives, which can delay diagnosis.
- **Specificity** measures the proportion of true negatives correctly identified. Low specificity produces false positives, which can lead to unnecessary follow-up testing or treatment.
- **Overall accuracy** is calculated as (TP + TN) / (TP + TN + FP + FN), though it can be misleading in datasets with class imbalance.
- **Predictive values** (PPV and NPV) depend on disease prevalence and are therefore not intrinsic properties of the test alone.
- Diagnostic accuracy is typically evaluated against a reference method during [method-performance](concepts/accreditation/method-performance.md) studies as part of [laboratory-validation](concepts/accreditation/laboratory-validation.md).
- Accuracy estimates should include confidence intervals; pooled estimates benefit from [statistical-analysis](concepts/statistical-analysis.md) such as meta-analytic techniques.

## Common Metrics

| Metric | Formula | Interpretation |
|--------|---------|----------------|
| Sensitivity | TP / (TP + FN) | Probability test is positive given disease present |
| Specificity | TN / (TN + FP) | Probability test is negative given disease absent |
| PPV | TP / (TP + FP) | Probability disease present given positive test |
| NPV | TN / (TN + FN) | Probability disease absent given negative test |
| Accuracy | (TP + TN) / Total | Overall proportion of correct results |

## Relationship to ROC Analysis

Diagnostic accuracy is often summarized visually and quantitatively through [roc-analysis](concepts/roc-analysis.md), which plots sensitivity against (1 − specificity) across all possible thresholds and yields an area under the curve (AUC) as a threshold-independent accuracy measure.

## Related

- [method-performance](concepts/accreditation/method-performance.md)
- [statistical-analysis](concepts/statistical-analysis.md)
- [laboratory-validation](concepts/accreditation/laboratory-validation.md)
- [roc-analysis](concepts/roc-analysis.md)
- [clinical-utility](concepts/clinical-utility.md)

## Related Pages

- [[concepts/roc-analysis]]
- [[concepts/statistical-analysis]]
- [[concepts/accreditation/method-performance]]
