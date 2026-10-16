#!/usr/bin/env python3
"""Fix raw transcript frontmatter for Infographics Show videos."""
from pathlib import Path

video_ids = ['zeVq8Pt2JCc', 'ZV6pUX8kJwg', '8M8U9Tj15bI', 'bD8ta7nsA8A', 'p5KvyYwaj4s']

for vid in video_ids:
    fpath = Path(f'docs/raw/videos/youtube-{vid}-transcript.md')
    content = fpath.read_text(encoding='utf-8')
    
    # Find the first --- ... --- block
    first_end = content.find('---', 3)
    fm_text = content[3:first_end]
    
    # Parse the frontmatter manually
    fm_lines = fm_text.strip().split('\n')
    fm_dict = {}
    for line in fm_lines:
        if ':' in line:
            key, val = line.split(':', 1)
            fm_dict[key.strip()] = val.strip()
    
    # Find the second --- block (metadata block)
    second_block_start = first_end + 3
    second_end = content.find('---', second_block_start)
    if second_end != -1:
        second_block = content[second_block_start:second_end].strip()
        for line in second_block.split('\n'):
            if ':' in line:
                key, val = line.split(':', 1)
                fm_dict[key.strip()] = val.strip()
        
        # Quote title
        title = fm_dict.get('title', '')
        ts = fm_dict.get('time_sensitive', 'false')
        if ts == 'True':
            ts = 'true'
        
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
        
        # Get the body content (after second ---)
        body = content[second_end + 3:]
        
        new_content = new_fm + body
        fpath.write_text(new_content, encoding='utf-8')
        print(f'Fixed: {fpath}')
    else:
        print(f'No second --- block found in {fpath}, skipping')

print('Done fixing raw transcript files')
