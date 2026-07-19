#!/usr/bin/env node
'use strict';

const fs = require('fs');
const path = require('path');
const {
  getAllPages, parseFrontmatter, getUniqueWikilinkTargets,
  extractProse, escapeRegex
} = require('./lib');

// ── Link suggestion engine ───────────────────────────────────
// Uses same logic as lint-wiki.js checkMissingLinks but outputs
// a full formatted report. See lib.js for shared utilities.

function suggestLinks() {
  const files = getAllPages();
  if (files.length === 0) {
    console.log('No pages found.');
    return;
  }

  const pageIndex = files.map(file => {
    const content = fs.readFileSync(file.path, 'utf-8');
    const fm = parseFrontmatter(content) || {};
    return {
      ...file,
      title: fm.title || file.basename,
      domain: fm.domain || 'general',
      classification: fm.classification || null,
      tags: Array.isArray(fm.tags) ? fm.tags : [],
      sources: Array.isArray(fm.sources) ? fm.sources : [],
      prose: extractProse(content),
      existingLinks: getUniqueWikilinkTargets(content)
    };
  });

  // Group by domain for pre-filtering
  const byDomain = {};
  for (const p of pageIndex) {
    const d = p.domain || 'general';
    if (!byDomain[d]) byDomain[d] = [];
    byDomain[d].push(p);
  }

  const suggestions = [];

  // Strategy 1: Text mentions (same domain only)
  for (const domain of Object.keys(byDomain)) {
    const domainPages = byDomain[domain];
    for (const sourcePage of domainPages) {
      for (const targetPage of domainPages) {
        if (sourcePage.slug === targetPage.slug) continue;
        if (sourcePage.existingLinks.has(targetPage.basename)) continue;

        const targetTitle = targetPage.title.toLowerCase();
        if (targetTitle.length < 4) continue;

        const titleRegex = new RegExp(`\\b${escapeRegex(targetTitle)}\\b`, 'i');
        if (titleRegex.test(sourcePage.prose)) {
          suggestions.push({
            type: 'text-mention',
            source: sourcePage.relPath,
            target: targetPage.relPath,
            suggestion: `Add [[${targetPage.basename}]] to "${sourcePage.relPath}" — mentions "${targetPage.title}" in prose`
          });
          continue;
        }

        const slugAsPhrase = targetPage.basename.toLowerCase().replace(/-/g, ' ');
        if (slugAsPhrase.length >= 4) {
          const slugRegex = new RegExp(`\\b${escapeRegex(slugAsPhrase)}\\b`, 'i');
          if (slugRegex.test(sourcePage.prose)) {
            suggestions.push({
              type: 'text-mention',
              source: sourcePage.relPath,
              target: targetPage.relPath,
              suggestion: `Add [[${targetPage.basename}]] to "${sourcePage.relPath}" — mentions "${slugAsPhrase}" in prose`
            });
          }
        }
      }
    }
  }

  // Strategy 2: Shared sources
  for (let i = 0; i < pageIndex.length; i++) {
    for (let j = i + 1; j < pageIndex.length; j++) {
      const a = pageIndex[i];
      const b = pageIndex[j];
      if (a.existingLinks.has(b.basename) || b.existingLinks.has(a.basename)) continue;
      const shared = a.sources.filter(s => b.sources.includes(s));
      if (shared.length > 0) {
        suggestions.push({
          type: 'shared-source',
          source: a.relPath,
          target: b.relPath,
          suggestion: `Link "${a.relPath}" ↔ "${b.relPath}" — both cite ${shared[0]}`
        });
      }
    }
  }

  // Strategy 3: Tag overlap (same domain + 2+ shared tags)
  for (const domain of Object.keys(byDomain)) {
    if (domain === 'general') continue;
    const domainPages = byDomain[domain];
    for (let i = 0; i < domainPages.length; i++) {
      for (let j = i + 1; j < domainPages.length; j++) {
        const a = domainPages[i];
        const b = domainPages[j];
        if (a.existingLinks.has(b.basename) || b.existingLinks.has(a.basename)) continue;
        const sharedTags = a.tags.filter(t => b.tags.includes(t));
        if (sharedTags.length >= 2) {
          suggestions.push({
            type: 'tag-overlap',
            source: a.relPath,
            target: b.relPath,
            suggestion: `Link "${a.relPath}" ↔ "${b.relPath}" — same domain (${domain}), shared tags: ${sharedTags.join(', ')}`
          });
        }
      }
    }
  }

  // Strategy 4: Classification overlap (same classification branch, no link)
  const classifiedPages = pageIndex.filter(p => p.classification);
  const byClassBranch = {};
  for (const p of classifiedPages) {
    // Group by first two levels of classification (e.g., "biotechnology.molecular-biology")
    const parts = p.classification.split('.');
    const branch = parts.length >= 2 ? parts.slice(0, 2).join('.') : parts[0];
    if (!byClassBranch[branch]) byClassBranch[branch] = [];
    byClassBranch[branch].push(p);
  }
  for (const branch of Object.keys(byClassBranch)) {
    const branchPages = byClassBranch[branch];
    if (branchPages.length < 2) continue;
    for (let i = 0; i < branchPages.length; i++) {
      for (let j = i + 1; j < branchPages.length; j++) {
        const a = branchPages[i];
        const b = branchPages[j];
        if (a.existingLinks.has(b.basename) || b.existingLinks.has(a.basename)) continue;
        // Skip if already suggested by tag-overlap
        const alreadySuggested = suggestions.some(s =>
          (s.source === a.relPath && s.target === b.relPath) ||
          (s.source === b.relPath && s.target === a.relPath)
        );
        if (alreadySuggested) continue;
        suggestions.push({
          type: 'classification-overlap',
          source: a.relPath,
          target: b.relPath,
          suggestion: `Link "${a.relPath}" ↔ "${b.relPath}" — same classification branch (${branch})`
        });
      }
    }
  }

  // Report
  if (suggestions.length === 0) {
    console.log('✓ No missing links found. All connections are already in place.');
  } else {
    const byType = {};
    for (const s of suggestions) {
      if (!byType[s.type]) byType[s.type] = [];
      byType[s.type].push(s);
    }

    const labels = {
      'text-mention': 'Text Mentions (page mentions another page\'s title in prose)',
      'shared-source': 'Shared Sources (pages cite the same raw source)',
      'tag-overlap': 'Tag Overlap (same domain + 2+ shared tags, no link)',
      'classification-overlap': 'Classification Overlap (same classification branch, no link)'
    };

    console.log(`Found ${suggestions.length} potential missing link(s):\n`);

    for (const [type, label] of Object.entries(labels)) {
      if (!byType[type]) continue;
      console.log(`── ${label} (${byType[type].length}) ──\n`);
      for (const s of byType[type]) {
        console.log(`  ${s.suggestion}`);
      }
      console.log();
    }

    console.log(`Total: ${suggestions.length} suggestions`);
    console.log('\nTo add links: edit the source page and add [[target-page]] at the appropriate location.');
    console.log('Then run: node scripts/build-graph.js && node scripts/generate-catalog.js');
  }

  process.exit(0);
}

suggestLinks();
