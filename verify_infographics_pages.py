#!/usr/bin/env python3
"""Verify newly created Infographics Show pages."""
import re
import yaml
from pathlib import Path

new_ids = ['zeVq8Pt2JCc', 'ZV6pUX8kJwg', '8M8U9Tj15bI', 'bD8ta7nsA8A', 'p5KvyYwaj4s']
docs_root = Path('docs')

valid_domains = ['ai', 'biotech', 'finance', 'devops', 'psychology', 'general']
valid_types = ['entity', 'concept', 'idea', 'finding', 'reading', 'comparison', 'source']

issues = []
verified = 0

# Find all new files
new_files = []
for vid in new_ids:
    for subdir in ['entities', 'readings', 'raw/videos']:
        pattern = f'{subdir}/youtube-{vid}-*.md'
        for f in docs_root.glob(pattern):
            new_files.append(f)

for vid in new_ids:
    f = docs_root / 'raw' / 'videos' / f'youtube-{vid}-transcript.md'
    if f.exists():
        new_files.append(f)

for fpath in sorted(set(new_files)):
    content = fpath.read_text(encoding='utf-8')

    # 1. Check frontmatter exists
    if not content.startswith('---'):
        issues.append(f'No frontmatter: {fpath}')
        continue

    fm_end = content.find('---', 3)
    if fm_end == -1:
        issues.append(f'Unclosed frontmatter: {fpath}')
        continue

    fm_text = content[3:fm_end]

    # Parse YAML frontmatter
    try:
        fm = yaml.safe_load(fm_text)
    except Exception as e:
        issues.append(f'Invalid YAML frontmatter: {fpath} ({e})')
        continue

    rel = str(fpath)

    # 2. Check required frontmatter fields based on type
    if rel.startswith('docs/entities/') or rel.startswith('docs/readings/'):
        for field in ['title', 'created', 'updated', 'type', 'tags', 'sources']:
            if field not in fm:
                issues.append(f'Missing frontmatter field "{field}": {fpath}')

    elif rel.startswith('docs/raw/'):
        for field in ['source_url', 'source_type']:
            if field not in fm:
                issues.append(f'Missing frontmatter field "{field}": {fpath}')
        if 'title' not in fm:
            issues.append(f'Missing title in raw source: {fpath}')

    # 3. Verify type is valid
    if 'type' in fm and fm['type'] not in valid_types:
        issues.append(f'Invalid type "{fm["type"]}": {fpath}')

    # 4. Verify domain if present
    if 'domain' in fm and fm['domain'] not in valid_domains:
        issues.append(f'Invalid domain "{fm["domain"]}": {fpath}')

    # 5. Verify sources exist (for readings and entities)
    if 'sources' in fm and fm['sources']:
        for src in fm['sources']:
            src_path = docs_root / src if not src.startswith('/') else Path(src)
            if not src_path.exists():
                issues.append(f'Source path does not exist: {src} in {fpath}')

    # 6. Check wikilinks
    wikilink_pattern = re.compile(r'\[\[([^\]|]+?)(?:\|[^\]]+?)?\]\]')
    wikilinks = wikilink_pattern.findall(content)
    for link in wikilinks:
        possible = [
            docs_root / f'{link}.md',
            docs_root / 'concepts' / f'{link}.md',
            docs_root / 'entities' / f'{link}.md',
            docs_root / 'readings' / f'{link}.md',
            docs_root / 'findings' / f'{link}.md',
        ]
        if not any(p.exists() for p in possible):
            found = False
            for subdir in ['concepts', 'entities', 'readings', 'findings']:
                d = docs_root / subdir
                if d.exists():
                    for f in d.glob('*.md'):
                        if f.stem.lower() == link.lower():
                            found = True
                            break
                if found:
                    break
            if not found:
                issues.append(f'Broken wikilink [[{link}]] in {fpath}')

    # 7. Check content is not empty (beyond frontmatter)
    body = content[fm_end+3:].strip()
    if len(body) < 50:
        issues.append(f'Ve ry short content ({len(body)} chars): {fpath}')

    verified += 1

print(f'Ve rified {verified} new Infographics Show pages')
print(f'Found {len(issues)} issues')
if issues:
    for i in issues[:30]:
        print(f'  - {i}')
    if len(issues) > 30:
        print(f'  ... and {len(issues) - 30} more')
else:
    print('All pages pass verification!')
