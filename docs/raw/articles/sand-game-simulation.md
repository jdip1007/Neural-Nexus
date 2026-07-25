---
source_url: https://github.com/jdip1007/Projects
source_type: file
ingested: 2026-07-23
sha256: stub
---

# Sand Game Simulation Source

Raw source file for the optimisation techniques concept page. Content based on the sand game implementation at jdip1007/Projects repository.

Key technical details:
- Single-grid architecture with updated[] flag
- Sand sinks through liquid vertically only (50% buoyancy prob, no diagonal diffusion)
- Liquid same-type swap
- Diffusion: water↔acid 90% 8-neighbor inlined
- Dynamic grid resize 150-1000 (bottom-center anchored)
- GPU: setGraphical(false) + putImageData Y-flip
