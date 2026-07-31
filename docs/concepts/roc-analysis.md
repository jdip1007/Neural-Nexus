---
title: ROC Analysis
created: 2026-07-31
updated: 2026-07-31
type: concept
classification: laboratory.method-evaluation
domain: laboratory
tags: [roc-analysis, diagnostic-accuracy, statistical-analysis, sensitivity, specificity]
sources: []
confidence: high
status: active
reviewed: 2026-07-31
---

# ROC Analysis

## Definition

Receiver Operating Characteristic (ROC) analysis is a statistical method for evaluating the ability of a continuous test to discriminate between two classes (e.g., disease vs. healthy). It plots sensitivity (true positive rate) against 1 − specificity (false positive rate) across all possible decision thresholds, producing a curve that characterizes the trade-off between sensitivity and specificity independent of prevalence.

## Key Points

- The **Area Under the Curve (AUC)** is the primary summary statistic. An AUC of 0.5 indicates no discrimination; 1.0 indicates perfect discrimination. AUC ≥ 0.9 is generally considered excellent.
- ROC analysis is threshold-independent, making it well suited to [[diagnostic-accuracy]] evaluation when the optimal cutoff is not yet established.
- The **Youden index** (J = sensitivity + specificity − 1) identifies the threshold maximizing overall correct classification.
- Confidence intervals for AUC are typically computed via the DeLong method or bootstrap resampling, requiring rigorous [[statistical-analysis]].
- Comparing two tests on the same population requires paired ROC analysis (e.g., DeLong's test) rather than independent comparison of AUCs.
- ROC analysis complements, but does not replace, [[method-performance]] evaluation of bias, imprecision, and analytical validity.

## Interpretation Guide

| AUC Range | Discrimination |
|-----------|----------------|
| 0.5 | No discrimination (chance) |
| 0.7–0.8 | Acceptable |
| 0.8–0.9 | Good |
| 0.9–1.0 | Excellent |

## Related

- [[diagnostic-accuracy]]
- [[method-performance]]
- [[statistical-analysis]]
- [[clinical-utility]]
