---
backlinks: []
classification: computer-science.simulation
confidence: medium
created: 2026-07-25
domain: devops
reviewed: 2026-07-25
sources:
- raw/articles/sand-game-simulation.md
status: draft
tags:
- general
title: Canvas Rendering
type: concept
updated: 2026-07-25
---



# Canvas Rendering

**Canvas rendering** uses the HTML5 Canvas API to draw graphics pixel-by-pixel. For high-performance simulations, `setGraphical(false)` with `putImageData` and Y-flip provides direct pixel buffer access.^[raw/articles/sand-game-simulation.md]

## In This Wiki

Used in the sand game simulation discussed in [optimisation-techniques-small-scale-simulation](concepts/optimisation-techniques-small-scale-simulation.md).

## Related

- [optimisation-techniques-small-scale-simulation](concepts/optimisation-techniques-small-scale-simulation.md) — Implementation details
- [cellular-automata](concepts/cellular-automata.md) — Simulation model
- [game-loop](concepts/game-loop.md) — Architecture pattern

## Related Pages

- [concepts/optimisation-techniques-small-scale-simulation](concepts/optimisation-techniques-small-scale-simulation.md)
- [concepts/cellular-automata](concepts/cellular-automata.md)
- [concepts/game-loop](concepts/game-loop.md)


## See also

- [[architecture]]
- 