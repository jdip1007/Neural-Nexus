#!/usr/bin/env node
'use strict';

const fs = require('fs');
const path = require('path');
const {
  DOCS_DIR, getAllPages, parseFrontmatter, extractWikilinks, fileToSlug
} = require('./lib');

const OUTPUT_FILE = path.join(DOCS_DIR, 'graph-data.json');

// ── Wikilink resolution ──────────────────────────────────────
// 3-tier: exact slug → basename → case-insensitive basename.
// Handles basename collisions by returning first match (logged).

function buildSlugIndex(pages) {
  const slugToId = {};
  const basenameToId = {};
  const collisions = [];

  for (let i = 0; i < pages.length; i++) {
    const slug = pages[i].slug;
    slugToId[slug] = i;

    const basename = pages[i].basename;
    if (basenameToId[basename] !== undefined) {
      collisions.push({ basename, first: pages[basenameToId[basename]].relPath, second: pages[i].relPath });
    } else {
      basenameToId[basename] = i;
    }
  }

  return { slugToId, basenameToId, collisions };
}

function resolveWikilink(target, slugToId, basenameToId) {
  const clean = target.split('#')[0].trim();
  if (!clean) return null;

  // 1. Exact slug
  if (slugToId[clean] !== undefined) return slugToId[clean];

  // 2. Basename
  const basename = path.basename(clean);
  if (basenameToId[basename] !== undefined) return basenameToId[basename];

  // 3. Case-insensitive basename
  const lower = basename.toLowerCase();
  for (const [slug, id] of Object.entries(slugToId)) {
    if (slug.toLowerCase().endsWith('/' + lower) || slug.toLowerCase() === lower) return id;
  }

  return null;
}

// ── Build graph ──────────────────────────────────────────────

function buildGraph() {
  const pages = getAllPages();
  const { slugToId, basenameToId, collisions } = buildSlugIndex(pages);

  if (collisions.length > 0) {
    console.log(`⚠  ${collisions.length} basename collision(s) detected:`);
    for (const c of collisions) {
      console.log(`   "${c.basename}" — "${c.first}" vs "${c.second}" (first wins)`);
    }
  }

  const nodes = pages.map((page, i) => {
    const content = fs.readFileSync(page.path, 'utf-8');
    const fm = parseFrontmatter(content) || {};
    return {
      id: i,
      slug: page.slug,
      title: fm.title || page.basename,
      type: fm.type || 'unknown',
      classification: fm.classification || null,
      domain: fm.domain || 'general',
      tags: Array.isArray(fm.tags) ? fm.tags : [],
      updated: fm.updated || '1970-01-01',
      url: '/' + page.slug + '/',
      inboundLinks: 0,
      outboundLinks: 0
    };
  });

  const edges = [];
  for (const page of pages) {
    const content = fs.readFileSync(page.path, 'utf-8');
    const wikilinks = extractWikilinks(content);
    const sourceId = slugToId[page.slug];
    if (sourceId === undefined) continue;

    const seen = new Set(); // Deduplicate edges
    for (const link of wikilinks) {
      const targetId = resolveWikilink(link, slugToId, basenameToId);
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

  const orphans = nodes.filter(n => n.inboundLinks === 0 && n.outboundLinks === 0);
  if (orphans.length > 0) {
    console.log(`⚠  ${orphans.length} orphan page(s):`);
    orphans.forEach(n => console.log(`   - ${n.slug}`));
  }
}

buildGraph();
