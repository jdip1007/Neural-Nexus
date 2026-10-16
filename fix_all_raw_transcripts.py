#!/usr/bin/env python3
"""Fix all raw video transcripts with unquoted title fields and other YAML issues."""
import re
from pathlib import Path

docs_root = Path('docs')
raw_videos = docs_root / 'raw' / 'videos'

fixed_count = 0
error_count = 0

for fpath in sorted(raw_videos.glob('youtube-*-transcript.md')):
    content = fpath.read_text(encoding='utf-8')
    
    if not content.startswith('---'):
        continue
    
    first_end = content.find('---', 3)
    if first_end == -1:
        continue
    
    fm_text = content[3:first_end]
    
    # Check if there's a second --- block
    second_block_start = first_end + 3
    second_end = content.find('---', second_block_start)
    
    if second_end == -1:
        # No second block - just fix title quoting and boolean
        fm_dict = {}
        for line in fm_text.strip().split('\n'):
            if ':' in line:
                key, val = line.split(':', 1)
                fm_dict[key.strip()] = val.strip()
        
        title = fm_dict.get('title', '')
        if not (title.startswith('"') and title.endswith('"')):
            # Need to quote and rebuild
            ts = fm_dict.get('time_sensitive', 'false')
            if ts == 'True':
                ts = 'true'
            
            new_fm_lines = ['---']
            for line in fm_text.strip().split('\n'):
                if line.startswith('title:'):
                    new_fm_lines.append(f'title: "{title}"')
                elif line.startswith('time_sensitive:'):
                    new_fm_lines.append(f'time_sensitive: {ts}')
                else:
                    new_fm_lines.append(line)
            new_fm_lines.append('---')
            
            new_fm = '\n'.join(new_fm_lines)
            body = content[first_end + 3:]
            new_content = new_fm + body
            fpath.write_text(new_content, encoding='utf-8')
            fixed_count += 1
            print(f'Fixed (no second block): {fpath.name}')
        continue
    
    # Has second block - merge into one frontmatter block
    second_block = content[second_block_start:second_end].strip()
    
    fm_dict = {}
    for line in fm_text.strip().split('\n'):
        if ':' in line:
            key, val = line.split(':', 1)
            fm_dict[key.strip()] = val.strip()
    
    for line in second_block.split('\n'):
        if ':' in line:
            key, val = line.split(':', 1)
            fm_dict[key.strip()] = val.strip()
    
    title = fm_dict.get('title', '')
    ts = fm_dict.get('time_sensitive', 'false')
    if ts == 'True':
        ts = 'true'
    
    # Check if already fixed (quoted title with source_url in frontmatter)
    if title.startswith('"') and 'source_url' in fm_dict:
        continue
    
    new_fm = f"""---
title: "{title}"
created: {fm_dict.get('created', '')}
updated: {fm_dict.get('updated', '')}
type: {fm_dict.get('type', 'source')}
domain: {fm_dict.get('domain', 'ai')}
classification: {fm_dict.get('classification', 'general.media')}
tags: [{fm_dict.get('tags', '').strip('[]')}]
sources: {fm_dict.get('sources', '[]')}
published: {fm_dict.get('published', '')}
time_sensitive: {ts}
source_url: {fm_dict.get('source_url', '')}
source_type: {fm_dict.get('source_type', 'video')}
ingested: {fm_dict.get('ingested', '')}
duration_minutes: {fm_dict.get('duration_minutes', '0')}
language: {fm_dict.get('language', 'en')}
sha256: {fm_dict.get('sha256', '')}
---"""
    
    body = content[second_end + 3:]
    new_content = new_fm + body
    fpath.write_text(new_content, encoding='utf-8')
    fixed_count += 1
    print(f'Fixed: {fpath.name}')

print(f'\nFixed {fixed_count} raw video transcript files')
