/**
 * Shared utilities for Neural Nexus scripts.
 * All scripts require this: `const { ... } = require('./lib');`
 *
 * Single source of truth for: file scanning, frontmatter parsing,
 * wikilink extraction, prose extraction, tag loading from SCHEMA.md.
 */

const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.join(__dirname, '..');
const DOCS_DIR = path.join(ROOT_DIR, 'docs');

// All directories that contain wiki pages (content + references)
const CONTENT_DIRS = ['concepts', 'entities', 'ideas', 'findings', 'readings', 'comparisons', 'references'];

// ── File scanning ─────────────────────────────────────────────

function getAllMarkdownFiles(dir) {
  const files = [];
  let items;
  try { items = fs.readdirSync(dir); } catch { return files; }

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

/**
 * Get all wiki page files across all content directories.
 * Returns array of { path, relPath, slug, dir, basename }
 */
function getAllPages() {
  const files = [];
  for (const dir of CONTENT_DIRS) {
    const dirPath = path.join(DOCS_DIR, dir);
    if (!fs.existsSync(dirPath)) continue;
    const found = getAllMarkdownFiles(dirPath);
    for (const f of found) {
      const basename = path.basename(f, '.md');
      files.push({
        path: f,
        relPath: path.relative(DOCS_DIR, f),
        slug: path.relative(DOCS_DIR, f).replace(/\.md$/, '').replace(/\\/g, '/'),
        basename,
        dir
      });
    }
  }
  return files;
}

// ── Frontmatter parsing ──────────────────────────────────────
// Handles: simple values, inline arrays [a, b], quoted values,
// titles with colons, multi-line arrays (basic).

function parseFrontmatter(content) {
  const fmRegex = /^---\r?\n([\s\S]*?)\r?\n---/;
  const match = content.match(fmRegex);
  if (!match) return null;

  const fm = {};
  const lines = match[1].split('\n');
  let currentKey = null;
  let inArray = false;

  for (const line of lines) {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith('#')) continue;

    // Continuation of multi-line array
    if (inArray && (trimmed.startsWith('- ') || trimmed.startsWith('-\t'))) {
      const val = trimmed.replace(/^-\s*/, '').trim().replace(/^["']|["']$/g, '');
      if (currentKey && Array.isArray(fm[currentKey])) {
        fm[currentKey].push(val);
      }
      continue;
    }

    // End of multi-line array
    if (inArray && !trimmed.startsWith('-')) {
      inArray = false;
    }

    const colonIdx = trimmed.indexOf(':');
    if (colonIdx === -1) continue;

    const key = trimmed.substring(0, colonIdx).trim();
    let value = trimmed.substring(colonIdx + 1).trim();

    // Strip surrounding quotes
    if ((value.startsWith('"') && value.endsWith('"')) ||
        (value.startsWith("'") && value.endsWith("'"))) {
      value = value.slice(1, -1);
    }

    // Inline array: [item1, item2, item3]
    if (value.startsWith('[') && value.endsWith(']')) {
      const inner = value.slice(1, -1).trim();
      fm[key] = inner ? inner.split(',').map(s => s.trim().replace(/^["']|["']$/g, '')) : [];
    }
    // Start of multi-line array (empty bracket or no value)
    else if (value === '[]' || value === '') {
      fm[key] = [];
      if (value === '[]') { /* inline empty array, done */ }
      else { inArray = true; currentKey = key; }
    }
    // Multi-line array starting with [ but not closing
    else if (value.startsWith('[') && !value.endsWith(']')) {
      fm[key] = [];
      inArray = true;
      currentKey = key;
      const partial = value.slice(1).trim();
      if (partial) {
        fm[key].push(partial.replace(/^["']|["']$/g, ''));
      }
    }
    else {
      fm[key] = value;
    }
  }

  return fm;
}

// ── Wikilink extraction ──────────────────────────────────────

function extractWikilinks(content) {
  const links = [];
  const codeBlockRegex = /```[\s\S]*?```|`[^`]*`/g;
  const cleaned = content.replace(codeBlockRegex, '');
  const regex = /\[\[([^\]|]+)(?:\|([^\]]+))?\]\]/g;
  let match;
  while ((match = regex.exec(cleaned)) !== null) {
    links.push(match[1].trim());
  }
  return links;
}

/**
 * Get unique wikilink targets (strips anchors, deduplicates).
 */
function getUniqueWikilinkTargets(content) {
  const links = extractWikilinks(content);
  const targets = new Set();
  for (const link of links) {
    targets.add(link.split('#')[0].trim());
  }
  return targets;
}

// ── Prose extraction (for link discovery) ────────────────────

function extractProse(content) {
  content = content.replace(/^---\r?\n[\s\S]*?\r?\n---/, '');
  content = content.replace(/```[\s\S]*?```/g, ' ');
  content = content.replace(/`[^`]*`/g, ' ');
  content = content.replace(/\[\[([^\]|]+)\|([^\]]+)\]\]/g, '$2');
  content = content.replace(/\[\[([^\]]+)\]\]/g, '$1');
  content = content.replace(/\[([^\]]*)\]\([^)]*\)/g, '$1');
  content = content.replace(/[*_~#>|]/g, ' ');
  return content.toLowerCase();
}

// ── Tag taxonomy loader (from SCHEMA.md) ─────────────────────

let _cachedTags = null;

function loadTagsFromSchema() {
  if (_cachedTags) return _cachedTags;

  const schemaPath = path.join(DOCS_DIR, 'SCHEMA.md');
  let content;
  try {
    content = fs.readFileSync(schemaPath, 'utf-8');
  } catch {
    _cachedTags = new Set();
    return _cachedTags;
  }

  const tags = new Set();
  let inTaxonomy = false;
  for (const line of content.split('\n')) {
    if (line.startsWith('## Tag Taxonomy')) { inTaxonomy = true; continue; }
    if (inTaxonomy && line.startsWith('## ') && !line.includes('Taxonomy')) { inTaxonomy = false; continue; }
    if (inTaxonomy && line.trim().startsWith('-') && !line.trim().startsWith('- **')) {
      const items = line.trim().slice(1).trim();
      for (const item of items.split(',')) {
        const tag = item.trim().replace(/`/g, '');
        if (tag && tag.length < 40 && !tag.startsWith('**')) {
          tags.add(tag);
        }
      }
    }
  }

  _cachedTags = tags;
  return tags;
}

// ── Slug helpers ─────────────────────────────────────────────

function fileToSlug(filePath) {
  return path.relative(DOCS_DIR, filePath).replace(/\.md$/, '').replace(/\\/g, '/');
}

function escapeRegex(str) {
  return str.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

module.exports = {
  ROOT_DIR,
  DOCS_DIR,
  CONTENT_DIRS,
  getAllMarkdownFiles,
  getAllPages,
  parseFrontmatter,
  extractWikilinks,
  getUniqueWikilinkTargets,
  extractProse,
  loadTagsFromSchema,
  fileToSlug,
  escapeRegex
};
