# Knowledge Graph

> Interactive visualization of your knowledge network

## About

- **Nodes**: Knowledge pages, colored by domain
- **Edges**: Wikilinks between pages
- **Size**: Proportional to connection count
- **Click** a node to navigate to that page
- **Scroll** to zoom, **drag** to pan

<div id="knowledge-graph"></div>

<div class="graph-legend">
  <span style="color: #4ecdc4;">AI/ML</span>
  <span style="color: #51cf66;">Biotech</span>
  <span style="color: #ffd43b;">Finance</span>
  <span style="color: #cc5de8;">Psychology</span>
  <span style="color: #ff922b;">DevOps</span>
  <span style="color: #868e96;">General</span>
</div>

## Statistics

| Metric | Value |
|--------|-------|
| Total Nodes | Loading... |
| Total Edges | Loading... |
| Orphan Pages | Loading... |

## Rebuild

Graph data is auto-generated on every push via GitHub Actions. To rebuild locally:

```bash
node scripts/build-graph.js
```
