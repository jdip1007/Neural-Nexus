---
title: Brain Blood Volume
created: 2026-07-29
updated: 2026-07-29
type: concept
classification: biotechnology.neuroscience.brain-energy-dynamics
domain: biotech
tags: [cerebral-blood-flow, brain-metabolism, neurovascular-coupling]
sources: [raw/articles/energy-paradox-rem-sleep-2026.md]
confidence: high
status: active
reviewed: 2026-07-29
---

# Brain Blood Volume (BBV)

## Definition

Brain blood volume (BBV) refers to the total volume of blood within the cerebral vasculature at any given time. Changes in BBV reflect vascular dilation or constriction, which regulate the delivery of oxygen and glucose to brain tissue. BBV is a key component of [neurovascular-coupling](concepts/neurovascular-coupling.md) and cerebral hemodynamics.

## Measurement

### Wide-Field Fluorescence Imaging
- In the Takahashi et al. (2026) study, BBV was measured using wide-field fluorescence imaging through the intact skull of head-fixed mice
- **Direct measurement**: Albumin-mScarlet (blood plasma marker) — fluorescence increases with BBV
- **Indirect proxy**: Direct YFP (dYFP) signal from Thy1-ATeam mice — fluorescence decreases with BBV (blood vessels appear as dark shadows in dYFP images)
- The dYFP and mScarlet signals are strongly anticorrelated (r = −0.947 across all vigilance states), confirming dYFP as a reliable inverse proxy for BBV

### Validation
| State | dYFP vs mScarlet correlation |
|---|---|
| NREM | r = −0.901 |
| REM | r = −0.957 |
| WAKE | r = −0.734 |
| All combined | r = −0.947 |

## State-Dependent BBV Dynamics

### NREM Sleep
- BBV fluctuates in sync with theta-band (6–9 Hz) ECoG activity
- Theta-band power precedes BBV changes by ~4–5 seconds
- Fast anterior-to-posterior vascular waves propagate across the cortex
- BBV fluctuations are relatively localized

### REM Sleep
- BBV increases dramatically (pronounced hyperemia)
- BBV increase originates in the **posterior cortex** (occipital) and slowly propagates anteriorly
- BBV fluctuations become synchronized over broader cortical areas
- The posterior origin may relate to the visual nature of dreams

### Transition NREM → REM
- A large, slow decrease in dYFP signal (increase in BBV) occurs across all cortical regions
- This global signal fluctuation marks the onset of the REM-specific vascular pattern

## Spatiotemporal Propagation

- **Lagged cross-correlation analysis** reveals temporal delays between BBV changes in different cortical regions
- During NREM: faster propagation (~4–5 s), anterior-to-posterior direction
- During REM: slower propagation, posterior-to-anterior direction
- The different propagation patterns suggest distinct regulatory mechanisms for vascular control across brain states

## Clinical Relevance

- BBV changes are the basis of the fMRI BOLD signal
- Understanding state-dependent BBV dynamics improves interpretation of sleep neuroimaging studies
- Abnormal BBV regulation is associated with stroke, migraine, and neurodegenerative diseases

## Related

- [neurovascular-coupling](concepts/neurovascular-coupling.md) — How neuronal activity drives BBV changes
- [rem-sleep-energy-paradox](concepts/rem-sleep-energy-paradox.md) — The paradoxical relationship between increased BBV and decreased neuronal ATP during REM
- [brain-energy-metabolism](concepts/brain-energy-metabolism.md) — The metabolic context for BBV regulation
- [energy-paradox-rem-sleep-2026](raw/articles/energy-paradox-rem-sleep-2026.md) — Source reading

## Related Pages

- [[rem-sleep]]
- [[nrem-sleep]]
