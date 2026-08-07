#!/usr/bin/env python3
"""Third pass: add wikilinks to remaining orphan pages.
For pages with <2 suggestions, find pages with same classification or same domain+shared tags."""

import subprocess
import re
import os
import json
from collections import defaultdict

DOCS_DIR = os.path.expanduser("~/Neural-Nexus/docs")
REPO_DIR = os.path.expanduser("~/Neural-Nexus")

# Load graph data for node info
with open(os.path.join(DOCS_DIR, 'graph-data.json'), 'r') as f:
    graph = json.load(f)

# Build slug → node info map
nodes_by_slug = {}
for node in graph['nodes']:
    nodes_by_slug[node['slug']] = node

# Get remaining orphans from lint
lint_result = subprocess.run(
    ["node", "scripts/lint-wiki.js"],
    capture_output=True, text=True, cwd=REPO_DIR
)

orphan_pages = []
for line in lint_result.stdout.split('\n'):
    m = re.search(r'Fewer than 2 unique wikilink targets \(0\): (.+)', line)
    if m:
        orphan_pages.append(m.group(1).strip())
    m = re.search(r'Fewer than 2 unique wikilink targets \(1\): (.+)', line)
    if m:
        orphan_pages.append(m.group(1).strip())

print(f"Remaining orphan pages: {len(orphan_pages)}")

# For each orphan, find related pages by classification prefix or shared tags
modified = 0
for orphan_slug in orphan_pages:
    # Normalize slug (remove .md extension if present)
    orphan_slug_clean = orphan_slug.replace('.md', '')
    
    orphan_node = nodes_by_slug.get(orphan_slug_clean)
    if not orphan_node:
        # Try with concepts/ prefix
        for s, n in nodes_by_slug.items():
            if s == orphan_slug_clean or n.get('slug') == orphan_slug_clean:
                orphan_node = n
                break
    
    if not orphan_node:
        continue
    
    orphan_path = os.path.join(DOCS_DIR, orphan_slug)
    if not os.path.exists(orphan_path):
        continue
    
    with open(orphan_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '## Related Pages' in content:
        continue
    
    orphan_tags = set(orphan_node.get('tags', []))
    orphan_class = orphan_node.get('classification', '') or ''
    orphan_domain = orphan_node.get('domain', 'general')
    
    # Score candidates by shared tags + classification prefix
    candidates = []
    for node in graph['nodes']:
        if node['slug'] == orphan_slug_clean:
            continue
        
        node_tags = set(node.get('tags', []))
        node_class = node.get('classification', '') or ''
        
        shared_tags = len(orphan_tags & node_tags)
        class_prefix_match = (
            orphan_class and node_class and 
            orphan_class.split('.')[0] == node_class.split('.')[0]
        )
        same_domain = orphan_domain == node.get('domain', 'general')
        
        score = shared_tags * 2 + (3 if class_prefix_match else 0) + (1 if same_domain else 0)
        
        if score >= 3:
            candidates.append((score, node['slug']))
    
    # Sort by score, take top 3
    candidates.sort(key=lambda x: -x[0])
    targets = [c[1] for c in candidates[:3]]
    
    if len(targets) < 2:
        # Fallback: any 2 pages with same domain
        for node in graph['nodes']:
            if node['slug'] == orphan_slug_clean:
                continue
            if node.get('domain', 'general') == orphan_domain:
                targets.append(node['slug'])
            if len(targets) >= 3:
                break
    
    if len(targets) < 2:
        continue
    
    # Use basename for wikilinks
    links = '\n'.join(f'- [[{t}]]' for t in targets[:3])
    section = f"\n\n## Related Pages\n\n{links}\n"
    
    content = content.rstrip() + section
    
    with open(orphan_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    modified += 1

print(f"Third pass: modified {modified} additional pages")
