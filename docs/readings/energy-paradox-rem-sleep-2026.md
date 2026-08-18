---
title: "Energy Paradox in REM Sleep: Balancing Supply and Consumption in Brain Metabolism"
created: 2026-07-29
updated: 2026-07-29
type: reading
domain: biotech
tags: [sleep, brain-metabolism, REM-sleep, neurovascular-coupling, ATP, pyruvate, energy-dynamics]
sources: [raw/articles/energy-paradox-rem-sleep-2026.md]
confidence: high
status: active
reviewed: 2026-07-29
---

# Energy Paradox in REM Sleep: Balancing Supply and Consumption in Brain Metabolism

**Authors:** Yusuke Takahashi, Yoko Ikoma & Ko Matsui (Tohoku University, Japan)

**Journal:** Communications Biology (2026) 9:979

**DOI:** [10.1038/s42003-026-10646-6](https://doi.org/10.1038/s42003-026-10646-6)

## TL;DR

During REM sleep, brain blood volume increases dramatically, astrocytic pyruvate rises, but neuronal ATP paradoxically declines sharply — revealing distinct energy-allocation strategies across brain states. During NREM sleep, theta-band ECoG activity predicts subsequent blood volume changes with ~4-5 s delay, suggesting a homeostatic neurovascular coupling mechanism.

## Key Points

### 1. Theta-Band ECoG Predicts Blood Volume Changes in NREM
- During NREM sleep, theta-band (6–9 Hz) ECoG power fluctuations precede brain blood volume (BBV) changes by ~4–5 seconds
- An optimized finite-impulse-response brain-blood-volume response function (FIR-BRF) captures this neurovascular coupling
- The FIR-BRF peaks at 4–5 s, matching the observed cross-correlation lag
- This suggests a homeostatic mechanism dynamically adjusting energy delivery to match neuronal demands

### 2. State-Dependent Reorganization of Metabolic Dynamics
- **NREM**: BBV fluctuations are relatively localized, with anterior-to-posterior vascular waves
- **REM**: BBV becomes synchronized over broader cortical areas, with a pronounced increase originating in the posterior cortex
- BBV propagates slowly across the brain during REM, unlike the faster anterior-to-posterior waves in NREM

### 3. The REM Energy Paradox
- REM sleep shows a pronounced increase in BBV (blood supply ↑)
- Astrocytic pyruvate levels are elevated (metabolic substrate ↑)
- **Paradoxically, neuronal ATP levels decline sharply** (energy state ↓)
- This decoupling suggests that during REM, energy is consumed faster than it can be supplied to neurons, or that astrocyte-neuron energy transfer is disrupted

### 4. Astrocyte-Neuron Energy Relationship
- During NREM, astrocytic pyruvate and neuronal ATP are relatively stable
- During REM, the astrocyte-neuron energy relationship becomes partially reciprocal
- Astrocytes may consume more pyruvate for their own oxidative metabolism during REM, reducing metabolite availability for neuronal transfer
- The [astrocyte-neuron-lactate-shuttle](concepts/astrocyte-neuron-lactate-shuttle.md) (ANLS) may be less efficient during REM

### 5. Vascular Wave Propagation
- NREM: Fast anterior-to-posterior vascular waves (~4–5 s propagation)
- REM: Slow posterior-to-anterior wave originating in occipital cortex
- The REM-specific posterior origin may relate to the visual nature of dreams

### 6. Spatiotemporal Motifs
- NMF (Non-negative Matrix Factorization) analysis identified 15 recurring spatiotemporal motifs of blood volume fluctuations
- Motifs were grouped into 10 categories based on spatial features
- REM-specific motifs showed posterior-dominant patterns, while NREM motifs were more anterior

### 7. Pharmacological Validation
- Vasodilation induced by acetazolamide confirmed that BBV increase alone does not decrease neuronal ATP
- The ATP decline during REM is therefore not simply a consequence of increased blood flow, but reflects a genuine metabolic shift

## Key Methods

- **Wide-field fluorescence imaging** through intact skull in head-fixed mice
- **Thy1-ATeam mice** for FRET-based neuronal ATP sensing
- **PYRS sensor** for astrocytic pyruvate measurement
- **Albumin-mScarlet** for blood plasma labeling
- **dYFP signal** as inverse proxy for BBV (validated: r = −0.947 across all states)
- **Difference method** (dYFP − fYFP for PYRS; fYFP − dYFP for ATeam) for artifact correction
- **FIR-BRF** for modeling neurovascular coupling
- **Hierarchical clustering** and **lagged cross-correlation** for spatiotemporal analysis
- **NMF** for spatiotemporal motif extraction

## Entities & Concepts Mentioned

- [ko-matsui](entities/ko-matsui.md) — Senior/corresponding author
- [yusuke-takahashi](entities/yusuke-takahashi.md) — First author
- [yoko-ikoma](entities/yoko-ikoma.md) — Co-author
- [tohoku-university](entities/tohoku-university.md) — Affiliated institution
- [rem-sleep-energy-paradox](concepts/rem-sleep-energy-paradox.md) — Core concept
- [neurovascular-coupling](concepts/neurovascular-coupling.md) — Brain-blood volume relationship
- [astrocyte-neuron-lactate-shuttle](concepts/astrocyte-neuron-lactate-shuttle.md) — ANLS mechanism
- [brain-blood-volume](concepts/brain-blood-volume.md) — BBV measurement
- [brain-energy-metabolism](concepts/brain-energy-metabolism.md) — Energy dynamics in the brain
- [theta-band-activity](concepts/theta-band-activity.md) — 6–9 Hz oscillations
- [nrem-sleep](concepts/nrem-sleep.md) — Non-REM sleep state
- [rem-sleep](concepts/rem-sleep.md) — REM sleep state

## Takeaways

1. Brain energy dynamics are **state-dependent** — the same vascular increase has different metabolic consequences in NREM vs REM
2. The REM energy paradox (high supply, low neuronal ATP) challenges the assumption that increased blood flow always means increased neuronal energy availability
3. Theta-band activity during NREM serves as a **predictive signal** for vascular changes, suggesting a feedforward neurovascular coupling mechanism
4. Astrocytes and neurons may have a **partially reciprocal energy relationship** during REM, with astrocytes consuming more pyruvate at the expense of neuronal ATP supply
5. These findings have implications for understanding sleep disorders, memory consolidation, and the brain's energy efficiency compared to artificial computing systems

## Quotes

> "REM sleep was marked by a pronounced increase in BBV, originating in the posterior cortex and slowly propagating across the brain. This was accompanied by elevated astrocytic pyruvate; paradoxically, however, neuronal ATP levels declined sharply."

> "Theta-band ECoG activity during NREM sleep reliably predicts subsequent BBV fluctuations, suggesting a homeostatic mechanism that dynamically adjusts energy delivery to match ongoing neuronal demands."

> "The delicate balance between energy consumption and supply breaks down during the transition to REM sleep."

## Related Pages

- [[rem-sleep]]
- [[nrem-sleep]]
- [[ko-matsui]]
