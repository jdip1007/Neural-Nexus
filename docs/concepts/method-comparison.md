---
title: Method Comparison
created: 2026-07-31
updated: 2026-07-31
type: concept
classification: laboratory.method-evaluation
domain: laboratory
tags: [method-comparison, accuracy, bias, statistical-analysis, method-evaluation]
sources: []
confidence: high
status: active
reviewed: 2026-07-31
---

# Method Comparison

## Definition

Method comparison is the experimental and statistical evaluation of two analytical methods — typically a new or candidate method against an established comparative (reference) method — to determine whether they produce equivalent results across a clinically relevant range. It is a core component of [[method-performance]] evaluation during [[laboratory-verification]] of new instruments, reagents, or modified assays.

## Key Points

- **Study design:** Sample size and concentration distribution should span the medical decision range; CLSI EP09 recommends ≥40 patient specimens analyzed by both methods.
- **Bias estimation:** Average bias between methods is assessed via regression (ordinary least squares, Deming, or Passing-Bablok depending on error structure).
- **Agreement visualization:** Bland-Altman (difference) plots complement regression by showing bias and limits of agreement as a function of concentration.
- **Acceptability criteria:** Clinical, not purely statistical, criteria determine whether observed bias is acceptable (e.g., based on biological variation or total allowable error).
- **Statistical rigor:** Appropriate [[statistical-analysis]] accounts for measurement error in both methods, heteroscedasticity, and potential non-linearity.
- **Correlation is insufficient:** A high correlation coefficient does not prove agreement; regression and difference analysis are required.

## Common Regression Approaches

| Method | Use Case |
|--------|----------|
| Ordinary least squares | Comparative method has negligible error |
| Deming regression | Both methods have random error |
| Passing-Bablok | Robust to outliers and non-constant error |

## Related

- [[statistical-analysis]]
- [[method-performance]]
- [[laboratory-verification]]
- [[calibration-verification]]
