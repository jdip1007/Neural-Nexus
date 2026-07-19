"""
MkDocs hook: converts Obsidian-style [[wikilinks]] to proper Markdown links.

Supports:
  [[page-name]]           → [page-name](resolved/path.md)
  [[page-name|display]]   → [display](resolved/path.md)
  [[page-name#header]]    → [page-name#header](resolved/path.md#header)

Resolution:
  1. Exact slug match (full relative path without .md)
  2. Basename match (filename without extension)
  3. Case-insensitive basename match
  4. If unresolved, leaves [[link]] as-is (lint will flag it)
"""

import re
import os

# Global file map: slug → src_path
_file_map = {}


def on_files(files, config):
    """Build a lookup map of all page slugs → MkDocs source paths."""
    global _file_map
    _file_map = {}
    for f in files.src_paths.values():
        src_path = f.src_path
        # Map: full slug (e.g., "concepts/transformer-architecture")
        slug = src_path.replace('.md', '')
        _file_map[slug] = src_path
        # Map: basename only (e.g., "transformer-architecture")
        basename = os.path.splitext(os.path.basename(src_path))[0]
        if basename not in _file_map:
            _file_map[basename] = src_path
        # Map: lowercase basename for case-insensitive matching
        _file_map[basename.lower()] = src_path
    return files


def on_page_markdown(markdown, page, config, files):
    """Replace [[wikilinks]] with resolved Markdown links."""

    def replace_wikilink(match):
        target = match.group(1).strip()
        display = (match.group(2) or target).strip()

        # Split anchor
        if '#' in target:
            target_slug, anchor = target.split('#', 1)
            anchor = '#' + anchor
        else:
            target_slug = target
            anchor = ''

        # Skip external links
        if target_slug.startswith('http'):
            return match.group(0)

        # Resolve: try exact, then basename, then lowercase
        resolved = (
            _file_map.get(target_slug)
            or _file_map.get(os.path.basename(target_slug))
            or _file_map.get(target_slug.lower())
            or _file_map.get(os.path.basename(target_slug).lower())
        )

        if resolved:
            # Calculate relative path from current page to target
            return f'[{display}]({resolved}{anchor})'

        # Unresolved — leave as-is, lint will catch it
        return match.group(0)

    pattern = r'\[\[([^\]|]+)(?:\|([^\]]+))?\]\]'
    return re.sub(pattern, replace_wikilink, markdown)