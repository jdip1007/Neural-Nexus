#!/usr/bin/env python3
"""Second pass: add wikilinks to remaining orphan pages using tag-overlap and shared-source suggestions."""

import subprocess
import re
import os
from collections import defaultdict

DOCS_DIR = os.path.expanduser("~/Neural-Nexus/docs")
REPO_DIR = os.path.expanduser("~/Neural-Nexus")

result = subprocess.run(
    ["node", "scripts/suggest-links.js"],
    capture_output=True, text=True, cwd=REPO_DIR
)

pattern = re.compile(r'Add \[\[([^\]]+)\]\] to "([^"]+)"')

# Parse ALL suggestions (text, shared, tag, classification)
all_suggestions = defaultdict(list)  # page -> [(target, section), ...]
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
    if m and current_section:
        target = m.group(1).strip()
        page = m.group(2).strip()
        all_suggestions[page].append((target, current_section))

# Priority: text > shared > tag > classification
priority = {'text': 0, 'shared': 1, 'tag': 2, 'classification': 3}

modified = 0
for page_path, suggestions in sorted(all_suggestions.items()):
    full_path = os.path.join(DOCS_DIR, page_path)
    if not os.path.exists(full_path):
        continue
    
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Skip if already has Related Pages section
    if '## Related Pages' in content:
        continue
    
    # Sort by priority, deduplicate targets
    seen = set()
    prioritized = []
    for target, section in sorted(suggestions, key=lambda x: priority.get(x[1], 99)):
        if target not in seen:
            seen.add(target)
            prioritized.append(target)
        if len(prioritized) >= 5:
            break
    
    if len(prioritized) < 2:
        continue
    
    links = '\n'.join(f'- [[{t}]]' for t in prioritized)
    section = f"\n\n## Related Pages\n\n{links}\n"
    
    content = content.rstrip() + section
    
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    modified += 1

print(f"Second pass: modified {modified} additional pages")
