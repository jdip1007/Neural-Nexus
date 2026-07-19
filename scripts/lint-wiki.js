#!/usr/bin/env node
'use strict';

const fs = require('fs');
const path = require('path');
const {
  DOCS_DIR, getAllPages, parseFrontmatter, extractWikilinks,
  getUniqueWikilinkTargets, extractProse, loadTagsFromSchema, escapeRegex
} = require('./lib');

const REQUIRED_FM_FIELDS = ['title', 'created', 'updated', 'type', 'domain', 'tags'];
const TYPES_REQUIRING_SOURCES = ['reading', 'finding', 'concept', 'entity', 'comparison'];
const TYPES_REQUIRING_CLASSIFICATION = ['concept', 'entity'];
const REVIEW_STALE_DAYS = 180; // Pages not reviewed in 6 months flagged for re-check

const errors = [];
const warnings = [];
const info = [];

// ── Check functions ──────────────────────────────────────────

function checkFrontmatter(files, validTags) {
  for (const file of files) {
    const content = fs.readFileSync(file.path, 'utf-8');
    const fm = parseFrontmatter(content);

    if (!fm) {
      errors.push(`Missing frontmatter: ${file.relPath}`);
      continue;
    }

    for (const field of REQUIRED_FM_FIELDS) {
      if (fm[field] === undefined) {
        warnings.push(`Missing field '${field}': ${file.relPath}`);
      }
    }

    // Tags must be in taxonomy (only if we loaded tags successfully)
    if (validTags.size > 0 && Array.isArray(fm.tags)) {
      for (const tag of fm.tags) {
        if (!validTags.has(tag)) {
          warnings.push(`Tag '${tag}' not in SCHEMA.md taxonomy: ${file.relPath}`);
        }
      }
    }

    // Classification required for concepts and entities
    if (TYPES_REQUIRING_CLASSIFICATION.includes(fm.type)) {
      if (!fm.classification) {
        warnings.push(`Missing 'classification' field for ${fm.type} page: ${file.relPath}`);
      } else {
        const parts = fm.classification.split('.');
        if (parts.length < 2) {
          warnings.push(`Classification '${fm.classification}' needs at least 2 levels (category.subcategory): ${file.relPath}`);
        }
      }
    }
  }
}

function checkCitations(files) {
  for (const file of files) {
    const content = fs.readFileSync(file.path, 'utf-8');
    const fm = parseFrontmatter(content);
    if (!fm) continue;

    const fmSources = (Array.isArray(fm.sources) ? fm.sources : []).filter(s => s && s.trim());
    const inlineRegex = /\^\[([^\]]+)\]/g;
    const inlineCitations = [];
    let match;
    while ((match = inlineRegex.exec(content)) !== null) {
      inlineCitations.push(match[1].trim());
    }

    const hasCitations = fmSources.length > 0 || inlineCitations.length > 0;

    // Type-specific rules
    if (fm.type === 'reading' || fm.type === 'finding') {
      if (!hasCitations) {
        errors.push(`${fm.type} page has no sources cited: ${file.relPath}`);
      }
    } else if (TYPES_REQUIRING_SOURCES.includes(fm.type)) {
      if (!hasCitations) {
        warnings.push(`No sources cited for ${fm.type} page: ${file.relPath}`);
      }
    }

    // Orphan citations — inline markers pointing to non-existent files
    for (const citation of inlineCitations) {
      const fullPath = path.join(DOCS_DIR, citation.replace(/^\.\//, ''));
      if (!fs.existsSync(fullPath)) {
        warnings.push(`Inline citation points to missing file: ^[${citation}] in ${file.relPath}`);
      }
    }

    // Frontmatter sources must exist
    for (const src of fmSources) {
      const fullPath = path.join(DOCS_DIR, src.replace(/^\.\//, ''));
      if (!fs.existsSync(fullPath)) {
        warnings.push(`Frontmatter source file missing: ${src} in ${file.relPath}`);
      }
    }

    // Uncaptured external URLs
    const proseContent = content.replace(/```[\s\S]*?```/g, '');
    const urlRegex = /https?:\/\/[^\s)]+/g;
    let urlMatch;
    const urls = [];
    while ((urlMatch = urlRegex.exec(proseContent)) !== null) {
      const url = urlMatch[0];
      if (url.includes('github.com') && url.includes('Neural-Nexus')) continue;
      if (url.includes('jdip1007.github.io')) continue;
      urls.push(url);
    }
    if (urls.length > 0 && fm.type !== 'idea' && !hasCitations) {
      info.push(`Page references ${urls.length} external URL(s) but has no raw sources — consider capturing to raw/: ${file.relPath}`);
    }
  }
}

function checkBrokenWikilinks(files) {
  const allSlugs = new Set();
  const allBasenames = new Set();
  for (const file of files) {
    allSlugs.add(file.slug);
    allBasenames.add(file.basename);
  }

  for (const file of files) {
    const content = fs.readFileSync(file.path, 'utf-8');
    const links = extractWikilinks(content);
    for (const link of links) {
      const target = link.split('#')[0].trim();
      if (!target) continue;
      const basename = path.basename(target);
      if (!allSlugs.has(target) && !allBasenames.has(basename)) {
        warnings.push(`Broken wikilink [[${link}]] in: ${file.relPath}`);
      }
    }
  }
}

function checkOrphans(files) {
  const inbound = {};
  const outbound = {};
  for (const file of files) {
    inbound[file.slug] = 0;
    outbound[file.slug] = 0;
  }

  const allBasenames = new Set(files.map(f => f.basename));

  for (const file of files) {
    const content = fs.readFileSync(file.path, 'utf-8');
    const targets = getUniqueWikilinkTargets(content);
    for (const target of targets) {
      const basename = path.basename(target);
      if (allBasenames.has(basename)) {
        outbound[file.slug]++;
        inbound[basename]++;
      }
    }
  }

  for (const file of files) {
    if (inbound[file.basename] === 0 && outbound[file.slug] === 0) {
      info.push(`Orphan page (no inbound/outbound links): ${file.relPath}`);
    }
  }
}

function checkPageSize(files) {
  for (const file of files) {
    const content = fs.readFileSync(file.path, 'utf-8');
    const lines = content.split('\n').length;
    if (lines > 200) {
      info.push(`Large page (${lines} lines, consider splitting): ${file.relPath}`);
    }
  }
}

function checkStaleContent(files) {
  const now = new Date();
  const staleThreshold = new Date(now.getTime() - 90 * 24 * 60 * 60 * 1000);

  for (const file of files) {
    const content = fs.readFileSync(file.path, 'utf-8');
    const fm = parseFrontmatter(content);
    if (!fm || !fm.updated) continue;
    const updated = new Date(fm.updated);
    if (updated < staleThreshold) {
      info.push(`Stale content (updated ${fm.updated}): ${file.relPath}`);
    }
  }
}

function checkMinLinks(files) {
  for (const file of files) {
    const content = fs.readFileSync(file.path, 'utf-8');
    const uniqueTargets = getUniqueWikilinkTargets(content);
    if (uniqueTargets.size < 2) {
      warnings.push(`Fewer than 2 unique wikilink targets (${uniqueTargets.size}): ${file.relPath}`);
    }
  }
}

// ── Truth/validity review tracking ───────────────────────────
// Pages have a `reviewed` frontmatter field (ISO date).
// Lint flags pages that haven't been reviewed in REVIEW_STALE_DAYS.

function checkReviewStatus(files) {
  const now = new Date();
  const reviewStale = new Date(now.getTime() - REVIEW_STALE_DAYS * 24 * 60 * 60 * 1000);

  for (const file of files) {
    const content = fs.readFileSync(file.path, 'utf-8');
    const fm = parseFrontmatter(content);
    if (!fm) continue;

    // Never reviewed
    if (!fm.reviewed) {
      if (fm.status !== 'draft') {
        warnings.push(`Never reviewed (add 'reviewed: YYYY-MM-DD' after checking): ${file.relPath}`);
      }
      continue;
    }

    // Review is stale
    const reviewedDate = new Date(fm.reviewed);
    if (reviewedDate < reviewStale) {
      info.push(`Review stale (last reviewed ${fm.reviewed}, >${REVIEW_STALE_DAYS} days): ${file.relPath}`);
    }

    // Reviewed before last update — content changed since review
    if (fm.updated && reviewedDate < new Date(fm.updated)) {
      warnings.push(`Content updated after last review (updated: ${fm.updated}, reviewed: ${fm.reviewed}): ${file.relPath}`);
    }
  }
}

// ── Missing link discovery ───────────────────────────────────
// Finds pages that should be connected but aren't.
// 3 strategies: text mention, shared source, tag overlap.
// Pre-filters by domain for performance.

function checkMissingLinks(files) {
  if (files.length < 2) return [];

  const pageIndex = files.map(file => {
    const content = fs.readFileSync(file.path, 'utf-8');
    const fm = parseFrontmatter(content) || {};
    const existingLinks = getUniqueWikilinkTargets(content);
    return {
      ...file,
      title: fm.title || file.basename,
      domain: fm.domain || 'general',
      classification: fm.classification || null,
      tags: Array.isArray(fm.tags) ? fm.tags : [],
      sources: Array.isArray(fm.sources) ? fm.sources : [],
      prose: extractProse(content),
      existingLinks
    };
  });

  // Group by domain for pre-filtering text mentions
  const byDomain = {};
  for (const p of pageIndex) {
    const d = p.domain || 'general';
    if (!byDomain[d]) byDomain[d] = [];
    byDomain[d].push(p);
  }

  const suggestions = [];

  // Strategy 1: Text mentions (same domain only — cross-domain is usually noise)
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
            detail: `mentions "${targetPage.title}" in prose`
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
              detail: `mentions "${slugAsPhrase}" in prose`
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
          detail: `both cite ${shared[0]}`
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
            detail: `same domain (${domain}), shared tags: ${sharedTags.join(', ')}`
          });
        }
      }
    }
  }

  // Strategy 4: Classification overlap (same classification branch, no link)
  const classifiedPages = pageIndex.filter(p => p.classification);
  const byClassBranch = {};
  for (const p of classifiedPages) {
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
        const alreadySuggested = suggestions.some(s =>
          (s.source === a.relPath && s.target === b.relPath) ||
          (s.source === b.relPath && s.target === a.relPath)
        );
        if (alreadySuggested) continue;
        suggestions.push({
          type: 'classification-overlap',
          source: a.relPath,
          target: b.relPath,
          detail: `same classification branch (${branch})`
        });
      }
    }
  }

  return suggestions;
}

// ── Run ──────────────────────────────────────────────────────

function lint() {
  console.log('Running Neural Nexus lint...\n');

  const files = getAllPages();
  const validTags = loadTagsFromSchema();
  console.log(`Scanning ${files.length} pages...`);
  console.log(`Loaded ${validTags.size} valid tags from SCHEMA.md\n`);

  checkFrontmatter(files, validTags);
  checkCitations(files);
  checkBrokenWikilinks(files);
  checkOrphans(files);
  checkPageSize(files);
  checkStaleContent(files);
  checkMinLinks(files);
  checkReviewStatus(files);

  const linkSuggestions = checkMissingLinks(files);

  // Report
  if (errors.length > 0) {
    console.log(`❌ ERRORS (${errors.length}):`);
    errors.forEach(e => console.log(`   ${e}`));
    console.log();
  }

  if (warnings.length > 0) {
    console.log(`⚠  WARNINGS (${warnings.length}):`);
    warnings.forEach(w => console.log(`   ${w}`));
    console.log();
  }

  if (info.length > 0) {
    console.log(`ℹ  INFO (${info.length}):`);
    info.forEach(i => console.log(`   ${i}`));
    console.log();
  }

  if (linkSuggestions.length > 0) {
    console.log(`💡 MISSING LINKS (${linkSuggestions.length}):`);
    const byType = {};
    for (const s of linkSuggestions) {
      byType[s.type] = (byType[s.type] || 0) + 1;
    }
    for (const [type, count] of Object.entries(byType)) {
      console.log(`   ${type}: ${count}`);
    }
    console.log(`   Run \`node scripts/suggest-links.js\` for full report.`);
    console.log();
  }

  if (errors.length === 0 && warnings.length === 0 && info.length === 0 && linkSuggestions.length === 0) {
    console.log('✓ All checks passed. No issues found.');
  }

  const total = errors.length + warnings.length + info.length + linkSuggestions.length;
  console.log(`\nTotal: ${errors.length} errors, ${warnings.length} warnings, ${info.length} info, ${linkSuggestions.length} link suggestions`);

  process.exit(errors.length > 0 ? 1 : 0);
}

lint();
