#!/usr/bin/env python3
"""
Preprocessor script to convert Obsidian-style [[wikilinks]] to proper Markdown links.
This can be run before mkdocs build to preprocess all markdown files.
"""

import re
import os
import sys
from pathlib import Path

def build_file_map(docs_dir):
    """Build a lookup map of all page slugs → source paths."""
    file_map = {}
    docs_path = Path(docs_dir)
    
    for md_file in docs_path.rglob("*.md"):
        src_path = str(md_file.relative_to(docs_path))
        slug = src_path.replace('.md', '')
        file_map[slug] = src_path
        basename = os.path.splitext(os.path.basename(src_path))[0]
        if basename not in file_map:
            file_map[basename] = src_path
        file_map[basename.lower()] = src_path
    
    return file_map

def process_wikilinks(markdown, file_map):
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
            file_map.get(target_slug)
            or file_map.get(os.path.basename(target_slug))
            or file_map.get(target_slug.lower())
            or file_map.get(os.path.basename(target_slug).lower())
        )

        if resolved:
            return f'[{display}]({resolved}{anchor})'

        return match.group(0)

    pattern = r'\[\[([^\]|]+)(?:\|([^\]]+))?\]\]'
    return re.sub(pattern, replace_wikilink, markdown)

def preprocess_docs(docs_dir):
    """Preprocess all markdown files in the docs directory."""
    file_map = build_file_map(docs_dir)
    docs_path = Path(docs_dir)
    
    processed_files = []
    
    for md_file in docs_path.rglob("*.md"):
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        processed_content = process_wikilinks(content, file_map)
        
        if processed_content != content:
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(processed_content)
            processed_files.append(str(md_file.relative_to(docs_path)))
    
    return processed_files

if __name__ == "__main__":
    if len(sys.argv) > 1:
        docs_dir = sys.argv[1]
    else:
        docs_dir = "docs"
    
    processed_files = preprocess_docs(docs_dir)
    
    if processed_files:
        print(f"Processed {len(processed_files)} files:")
        for file in processed_files:
            print(f"  - {file}")
    else:
        print("No files needed processing.")