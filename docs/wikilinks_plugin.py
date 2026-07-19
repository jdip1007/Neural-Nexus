"""
MkDocs plugin: converts Obsidian-style [[wikilinks]] to proper Markdown links.

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
from mkdocs.plugins import BasePlugin


class WikilinksPlugin(BasePlugin):
    def on_files(self, files, config):
        """Build a lookup map of all page slugs → MkDocs source paths."""
        self._file_map = {}
        for f in files.src_paths.values():
            src_path = f.src_path
            slug = src_path.replace('.md', '')
            self._file_map[slug] = src_path
            basename = os.path.splitext(os.path.basename(src_path))[0]
            if basename not in self._file_map:
                self._file_map[basename] = src_path
            self._file_map[basename.lower()] = src_path
        return files

    def on_page_markdown(self, markdown, page, config, files):
        """Replace [[wikilinks]] with resolved Markdown links."""

        def replace_wikilink(match):
            target = match.group(1).strip()
            display = (match.group(2) or target).strip()

            if '#' in target:
                target_slug, anchor = target.split('#', 1)
                anchor = '#' + anchor
            else:
                target_slug = target
                anchor = ''

            if target_slug.startswith('http'):
                return match.group(0)

            resolved = (
                self._file_map.get(target_slug)
                or self._file_map.get(os.path.basename(target_slug))
                or self._file_map.get(target_slug.lower())
                or self._file_map.get(os.path.basename(target_slug).lower())
            )

            if resolved:
                return f'[{display}]({resolved}{anchor})'

            return match.group(0)

        pattern = r'\[\[([^\]|]+)(?:\|([^\]]+))?\]\]'
        return re.sub(pattern, replace_wikilink, markdown)