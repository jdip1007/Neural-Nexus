#!/usr/bin/env node
'use strict';

const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.join(__dirname, '..');
const DOCS_DIR = path.join(ROOT_DIR, 'docs');
const OUTPUT_FILE = path.join(DOCS_DIR, 'graph-data.json');

// Directories that contain wiki pages (not raw sources, not meta files)
const CONTENT_DIRS = ['concepts', 'entities', 'ideas', 'findings', 'readings', 'comparisons'];

// ── File scanning ─────────────────────────────────────────────

function getAllMarkdownFiles(dir) {
  const files = [];
  let items;
  try {
    items = fs.readdirSync(dir);
  } catch {
    return files;
  }

  for (const item of items) {
    if (item.startsWith('.') || item.startsWith('_')) continue;
    const fullPath = path.join(dir, item);
    const stat = fs.statSync(fullPath);

    if (stat.isDirectory()) {
      files.push(...getAllMarkdownFiles(fullPath));
    } else if (item.endsWith('.md') && item !== 'index.md' && item !== 'SCHEMA.md') {
      files.push(fullPath);
    }
  }
  return files;
}

// ── Frontmatter parsing ──────────────────────────────────────
// Handles: simple values, inline arrays [a, b], titles with colons

function parseFrontmatter(content) {
  const fmRegex = /^---\r?\n([\s\S]*?)\r?\n---/;
  const match = content.match(fmRegex);
  if (!match) return {};

  const fm = {};
  const lines = match[1].split('\n');

  for (const line of lines) {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith('#')) continue;

    const colonIdx = trimmed.indexOf(':');
    if (colonIdx === -1) continue;

    const key = trimmed.substring(0, colonIdx).trim();
    let value = trimmed.substring(colonIdx + 1).trim();

    // Strip surrounding quotes
    if ((value.startsWith('"') && value.endsWith('"')) ||
        (value.startsWith("'") && value.endsWith("'"))) {
      value = value.slice(1, -1);
    }

    // Parse inline array: [item1, item2, item3]
    if (value.startsWith('[') && value.endsWith(']')) {
      const inner = value.slice(1, -1).trim();
      fm[key] = inner ? inner.split(',').map(s => s.trim().replace(/^["']|["']$/g, '')) : [];
    } else {
      fm[key] = value;
    }
  }

  return fm;
}

// ── Wikilink extraction ──────────────────────────────────────

function extractWikilinks(content) {
  // Match [[target]] or [[target|display]] but not inside code blocks
  const links = [];
  const codeBlockRegex = /```[\s\S]*?```|`[^`]*`/g;
  const cleaned = content.replace(codeBlockRegex, ''); // Remove code blocks

  const wikilinkRegex = /\[\[([^\]|]+)(?:\|([^\]]+))?\]\]/g;
  let match;
  while ((match = wikilinkRegex.exec(cleaned)) !== null) {
    links.push(match[1].trim());
  }
  return links;
}

// ── Slug normalization ───────────────────────────────────────

function fileToSlug(filePath) {
  return path.relative(DOCS_DIR, filePath).replace(/\.md$/, '').replace(/\\/g, '/');
}

function normalizeWikilinkTarget(target) {
  // Remove anchors
  return target.split('#')[0].trim();
}

function resolveWikilink(target, slugToNode) {
  const clean = normalizeWikilinkTarget(target);
  if (!clean) return null;

  // 1. Exact match (e.g., "concepts/transformer-architecture")
  if (slugToNode[clean] !== undefined) return slugToNode[clean];

  // 2. Basename match (e.g., "transformer-architecture" → match "concepts/transformer-architecture")
  const basename = path.basename(clean);
  if (slugToNode[basename] !== undefined) return slugToNode[basename];

  // 3. Case-insensitive basename
  const lower = basename.toLowerCase();
  for (const [slug, id] of Object.entries(slugToNode)) {
    if (slug.toLowerCase().endsWith('/' + lower) || slug.toLowerCase() === lower) {
      return id;
    }
  }

  return null;
}

// ── Build graph ──────────────────────────────────────────────

function buildGraph() {
  const files = [];
  for (const dir of CONTENT_DIRS) {
    const dirPath = path.join(DOCS_DIR, dir);
    if (fs.existsSync(dirPath)) {
      files.push(...getAllMarkdownFiles(dirPath));
    }
  }
  // Also scan references/ and root for any wiki pages
  const refDir = path.join(DOCS_DIR, 'references');
  if (fs.existsSync(refDir)) {
    files.push(...getAllMarkdownFiles(refDir));
  }

  const nodes = [];
  const edges = [];
  const slugToId = {};

  // Create nodes
  for (const file of files) {
    const slug = fileToSlug(file);
    const content = fs.readFileSync(file, 'utf-8');
    const fm = parseFrontmatter(content);

    const id = nodes.length;
    slugToId[slug] = id;

    // Also map basename for fuzzy resolution
    const basename = path.basename(slug);
    if (slugToId[basename] === undefined) {
      slugToId[basename] = id;
    }

    nodes.push({
      id,
      slug,
      title: fm.title || slug,
      type: fm.type || 'unknown',
      domain: fm.domain || 'general',
      tags: Array.isArray(fm.tags) ? fm.tags : [],
      updated: fm.updated || '1970-01-01',
      url: '/' + slug + '/',
      inboundLinks: 0,
      outboundLinks: 0
    });
  }

  // Create edges from wikilinks
  for (const file of files) {
    const sourceSlug = fileToSlug(file);
    const content = fs.readFileSync(file, 'utf-8');
    const wikilinks = extractWikilinks(content);

    const sourceId = slugToId[sourceSlug];
    if (sourceId === undefined) continue;

    const seen = new Set(); // Avoid duplicate edges
    for (const link of wikilinks) {
      const targetId = resolveWikilink(link, slugToId);
      if (targetId !== null && targetId !== sourceId && !seen.has(targetId)) {
        seen.add(targetId);
        edges.push({ source: sourceId, target: targetId });
        nodes[sourceId].outboundLinks++;
        nodes[targetId].inboundLinks++;
      }
    }
  }

  const graphData = {
    nodes,
    edges,
    metadata: {
      totalNodes: nodes.length,
      totalEdges: edges.length,
      generatedAt: new Date().toISOString()
    }
  };

  fs.writeFileSync(OUTPUT_FILE, JSON.stringify(graphData, null, 2));

  console.log(`✓ Graph built: ${nodes.length} nodes, ${edges.length} edges`);
  console.log(`✓ Saved to: ${OUTPUT_FILE}`);

  // Report orphan pages (zero inbound + zero outbound links)
  const orphans = nodes.filter(n => n.inboundLinks === 0 && n.outboundLinks === 0);
  if (orphans.length > 0) {
    console.log(`⚠  ${orphans.length} orphan page(s):`);
    orphans.forEach(n => console.log(`   - ${n.slug}`));
  }

  return graphData;
}

buildGraph();