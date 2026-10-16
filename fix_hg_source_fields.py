#!/usr/bin/env python3
"""Fix remaining healthygamergg raw transcript files missing source_url/source_type."""
from pathlib import Path
import re

hg_dir = Path('docs/raw/transcripts/healthygamergg')
fixed = 0

# Map filenames to video IDs (from existing video_id in frontmatter or from filename)
for f in sorted(hg_dir.glob('*.md')):
    content = f.read_text(encoding='utf-8')
    
    if not content.startswith('---'):
        continue
    
    fm_end = content.find('---', 3)
    if fm_end == -1:
        continue
    
    fm_text = content[3:fm_end]
    
    # Check if source_url is already present
    if 'source_url:' in fm_text:
        continue
    
    # Extract video_id if present
    vid_match = re.search(r'video_id:\s*(\S+)', fm_text)
    if vid_match:
        vid = vid_match.group(1)
        source_url = f'https://www.youtube.com/watch?v={vid}'
    else:
        # Skip files without video_id
        continue
    
    # Add source_url and source_type after the last frontmatter field
    new_fm = fm_text.rstrip() + f'\nsource_url: {source_url}\nsource_type: video'
    new_content = '---' + new_fm + content[fm_end:]
    f.write_text(new_content, encoding='utf-8')
    fixed += 1
    print(f'Fixed: {f.name}')

print(f'\nFixed {fixed} healthygamergg files')
