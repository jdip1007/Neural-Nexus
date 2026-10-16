#!/usr/bin/env python3
"""Fix all raw video transcripts that are missing source_url/source_type or have invalid types."""
from pathlib import Path
import re

raw_dir = Path('docs/raw/videos')
fixed = 0

for f in sorted(raw_dir.glob('youtube-*-transcript.md')):
    content = f.read_text(encoding='utf-8')
    
    if not content.startswith('---'):
        continue
    
    fm_end = content.find('---', 3)
    if fm_end == -1:
        continue
    
    fm_text = content[3:fm_end]
    
    needs_fix = False
    fm_dict = {}
    for line in fm_text.strip().split('\n'):
        if ':' in line:
            key, val = line.split(':', 1)
            key = key.strip()
            val = val.strip()
            fm_dict[key] = val
    
    # Check for issues
    if 'source_url' not in fm_dict:
        needs_fix = True
    if 'source_type' not in fm_dict:
        needs_fix = True
    if fm_dict.get('type') == 'raw':
        needs_fix = True
    
    if not needs_fix:
        continue
    
    # Extract video ID from filename
    vid_match = re.search(r'youtube-([^-]+)-transcript', f.name)
    if not vid_match:
        continue
    vid = vid_match.group(1)
    
    # Fix frontmatter
    new_lines = []
    for line in fm_text.strip().split('\n'):
        if line.startswith('type: raw'):
            new_lines.append('type: source')
        else:
            new_lines.append(line)
    
    new_fm = '\n'.join(new_lines)
    
    # Add source_url and source_type if missing
    if 'source_url' not in fm_dict:
        source_url = f'https://www.youtube.com/watch?v={vid}'
        new_fm += f'\nsource_url: {source_url}'
    if 'source_type' not in fm_dict:
        new_fm += '\nsource_type: video'
    
    new_content = '---\n' + new_fm + content[fm_end:]
    f.write_text(new_content, encoding='utf-8')
    fixed += 1

print(f'Fixed {fixed} raw video transcript files')
