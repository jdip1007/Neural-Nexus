# Neural Nexus

Personal knowledge base powered by LLM Wiki + Obsidian, hosted on GitHub Pages.

## Features
- 6 content types: concepts, entities, ideas, findings, readings, comparisons
- Multi-domain: AI/ML, biotech, finance, psychology, devops, personal
- Interactive D3.js knowledge graph
- Obsidian-style [[wikilinks]] (server-side rendered)
- Full-text search
- Dark/light mode
- Citation enforcement (readings/findings must cite sources)
- Review tracking (periodic truth/validity checks)
- Active link discovery (finds missing connections)
- GitHub Actions CI/CD (lint → build → deploy)
- Hermes Agent automation

## Quick Start
```bash
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
node scripts/build-graph.js
mkdocs serve
```

Visit http://127.0.0.1:8000

## Structure
See [docs/SCHEMA.md](docs/SCHEMA.md) for conventions.
See [docs/references/setup-guide.md](docs/references/setup-guide.md) for complete setup instructions.

## Scripts
| Script | Purpose |
|--------|---------|
| `scripts/lib.js` | Shared utilities (imported by all scripts) |
| `scripts/build-graph.js` | Build D3.js graph data |
| `scripts/generate-catalog.js` | Generate page catalog |
| `scripts/lint-wiki.js` | Health check + citation enforcement + link discovery |
| `scripts/suggest-links.js` | Standalone link discovery report |

All scripts use zero npm dependencies — only Node.js built-in modules.

## License
MIT
