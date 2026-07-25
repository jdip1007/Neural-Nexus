---
title: Canvas Rendering
created: 2026-07-25
updated: 2026-07-25
type: concept
classification: computer-science.simulation
domain: devops
tags: [rendering, canvas, web-performance]
sources: [raw/articles/sand-game-simulation.md]
confidence: medium
status: draft
reviewed: 2026-07-25
backlinks: []
---

# Canvas Rendering

**Canvas rendering** uses the HTML5 Canvas API to draw graphics pixel-by-pixel. For high-performance simulations, `setGraphical(false)` with `putImageData` and Y-flip provides direct pixel buffer access.^[raw/articles/sand-game-simulation.md]

## In This Wiki

Used in the sand game simulation discussed in [[optimisation-techniques-small-scale-simulation]].

## Related

- [[optimisation-techniques-small-scale-simulation]] — Implementation details
- [[cellular-automata]] — Simulation model
- [[game-loop]] — Architecture pattern