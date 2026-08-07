#!/usr/bin/env python3
"""Auto-add wikilinks to orphan pages based on suggest-links.js output.
Adds a '## Related Pages' section at the end of each page with relevant [[wikilinks]].
Focuses on text-mention suggestions (most reliable), then shared-source, tag-overlap."""

import subprocess
import re
import os
from collections import defaultdict

DOCS_DIR = os.path.expanduser("~/Neural-Nexus/docs")
REPO_DIR = os.path.expanduser("~/Neural-Nexus")

# Run suggest-links.js and capture output
result = subprocess.run(
    ["node", "scripts/suggest-links.js"],
    capture_output=True, text=True, cwd=REPO_DIR
)

# Parse suggestions: "  Add [[target]] to \"path\" — reason"
pattern = re.compile(r'Add \[\[([^\]]+)\]\] to "([^"]+)"')
suggestions = defaultdict(set)  # page -> set of targets

for line in result.stdout.split('\n'):
    m = pattern.search(line)
    if m:
        target = m.group(1).strip()
        page = m.group(2).strip()
        suggestions[page].add(target)

# Also parse text-mention suggestions specifically (higher priority)
text_mentions = defaultdict(set)
current_section = None
for line in result.stdout.split('\n'):
    if 'Text Mentions' in line:
        current_section = 'text'
    elif 'Shared Source' in line:
        current_section = 'shared'
    elif 'Tag Overlap' in line:
        current_section = 'tag'
    elif 'Classification Overlap' in line:
        current_section = 'classification'
    
    m = pattern.search(line)
    if m and current_section == 'text':
        target = m.group(1).strip()
        page = m.group(2).strip()
        text_mentions[page].add(target)

print(f"Total pages with suggestions: {len(suggestions)}")
print(f"Pages with text-mention suggestions: {len(text_mentions)}")

# Process each page
modified = 0
for page_path, targets in sorted(suggestions.items()):
    full_path = os.path.join(DOCS_DIR, page_path)
    if not os.path.exists(full_path):
        continue
    
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Skip if already has a Related Pages section
    if '## Related Pages' in content:
        continue
    
    # Prioritize text-mention targets, then add others up to 5
    text_targets = text_mentions.get(page_path, set())
    other_targets = targets - text_targets
    
    # Take up to 3 text-mention targets, then fill with others up to 5 total
    prioritized = list(text_targets)[:3]
    for t in sorted(other_targets):
        if len(prioritized) >= 5:
            break
        if t not in prioritized:
            prioritized.append(t)
    
    if len(prioritized) < 2:
        continue  # Need at least 2 for lint requirement
    
    # Build the related pages section
    links = '\n'.join(f'- [[{t}]]' for t in prioritized)
    section = f"\n\n## Related Pages\n\n{links}\n"
    
    # Append to end of file
    content = content.rstrip() + section
    
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    modified += 1

print(f"Modified {modified} pages with Related Pages sections")
