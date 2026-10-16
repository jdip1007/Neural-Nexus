#!/usr/bin/env python3
"""Comprehensive verification of ALL changed files before deployment."""
import re
import yaml
from pathlib import Path
import subprocess

docs_root = Path('docs')
valid_domains = ['ai', 'biotech', 'finance', 'devops', 'psychology', 'general']
valid_types = ['entity', 'concept', 'idea', 'finding', 'reading', 'comparison', 'source']

issues = []
verified = 0
skipped = 0

# Get all changed/new files
result = subprocess.run(['git', 'status', '--short'], capture_output=True, text=True)
changed_files = []
for line in result.stdout.strip().split('\n'):
    if not line.strip():
        continue
    status = line[:2]
    filepath = line[3:].strip()
    if filepath.endswith('.md') and filepath.startswith('docs/'):
        changed_files.append(filepath)

print(f'Checking {len(changed_files)} changed markdown files...')

for filepath in sorted(changed_files):
    fpath = Path(filepath)
    if not fpath.exists():
        # Deleted file, skip
        skipped += 1
        continue

    content = fpath.read_text(encoding='utf-8')

    # Check frontmatter exists
    if not content.startswith('---'):
        # Some docs files might not need frontmatter (SCHEMA.md, index, etc.)
        if filepath in ['docs/SCHEMA.md', 'docs/index.md', 'docs/log.md', 'docs/index-catalog.md']:
            skipped += 1
            continue
        issues.append(f'No frontmatter: {filepath}')
        continue

    fm_end = content.find('---', 3)
    if fm_end == -1:
        issues.append(f'Unclosed frontmatter: {filepath}')
        continue

    fm_text = content[3:fm_end]

    # Parse YAML frontmatter
    try:
        fm = yaml.safe_load(fm_text)
    except Exception as e:
        issues.append(f'Invalid YAML frontmatter: {filepath} ({e})')
        continue

    if fm is None:
        issues.append(f'Empty frontmatter: {filepath}')
        continue

    # Check required frontmatter fields based on type
    if filepath.startswith('docs/entities/') or filepath.startswith('docs/readings/'):
        for field in ['title', 'created', 'updated', 'type', 'tags', 'sources']:
            if field not in fm:
                issues.append(f'Missing frontmatter field "{field}": {filepath}')

    elif filepath.startswith('docs/raw/'):
        for field in ['source_url', 'source_type']:
            if field not in fm:
                issues.append(f'Missing frontmatter field "{field}": {filepath}')

    # Verify type is valid
    if 'type' in fm and fm['type'] not in valid_types:
        issues.append(f'Invalid type "{fm["type"]}": {filepath}')

    # Verify domain if present
    if 'domain' in fm and fm['domain'] not in valid_domains:
        issues.append(f'Invalid domain "{fm["domain"]}": {filepath}')

    # Verify sources exist
    if 'sources' in fm and fm['sources']:
        for src in fm['sources']:
            src_path = docs_root / src if not src.startswith('/') else Path(src)
            if not src_path.exists():
                issues.append(f'Source path does not exist: {src} in {filepath}')

    # Check wikilinks
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
                issues.append(f'Broken wikilink [[{link}]] in {filepath}')

    # Check content is not empty
    body = content[fm_end+3:].strip()
    if len(body) < 20:
        issues.append(f'Ve ry short content ({len(body)} chars): {filepath}')

    verified += 1

print(f'\nVerified: {verified} files')
print(f'Skipped: {skipped} files')
print(f'Issues: {len(issues)}')
if issues:
    for i in issues[:30]:
        print(f'  - {i}')
    if len(issues) > 30:
        print(f'  ... and {len(issues) - 30} more')
else:
    print('ALL changed files pass verification!')
