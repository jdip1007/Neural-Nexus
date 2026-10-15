#!/usr/bin/env python3
"""
Fix frontmatter in raw transcript files to match expected format.
"""

import os
import re
from pathlib import Path
from datetime import datetime

def fix_raw_transcript_frontmatter(file_path):
    """Fix frontmatter in a raw transcript file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if it already has the correct frontmatter
        if content.startswith('---\n') and 'title:' in content and 'sources:' in content:
            print(f"✓ {file_path} already has correct frontmatter")
            return True
        
        # Extract video ID from filename
        filename = os.path.basename(file_path)
        video_id = filename.replace('youtube-', '').replace('-transcript.md', '')
        
        # Extract title from content
        title_match = re.search(r'# YouTube Transcript: (.+)', content)
        if not title_match:
            print(f"❌ Could not extract title from {file_path}")
            return False
        
        title = title_match.group(1)
        
        # Create new frontmatter
        new_frontmatter = f"""---
title: {title}
created: {datetime.now().strftime('%Y-%m-%d')}
updated: {datetime.now().strftime('%Y-%m-%d')}
type: raw
domain: ai
classification: general.media
tags: [youtube, transcript, {video_id}]
sources: [{file_path.relative_to(Path('docs'))}]
published: {datetime.now().strftime('%Y-%m-%d')}
time_sensitive: False
confidence: medium
status: active
reviewed: {datetime.now().strftime('%Y-%m-%d')}
---

"""
        
        # Replace old frontmatter with new one
        frontmatter_end = content.find('---', 3)
        if frontmatter_end == -1:
            print(f"❌ Could not find frontmatter end in {file_path}")
            return False
        
        new_content = new_frontmatter + content[frontmatter_end + 3:]
        
        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✓ Fixed frontmatter in {file_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error fixing {file_path}: {e}")
        return False

def main():
    """Main function to fix all raw transcript files."""
    docs_path = Path('docs')
    raw_videos_path = docs_path / 'raw' / 'videos'
    
    if not raw_videos_path.exists():
        print(f"❌ Directory not found: {raw_videos_path}")
        return
    
    # Find all raw transcript files
    transcript_files = list(raw_videos_path.glob('youtube-*-transcript.md'))
    
    if not transcript_files:
        print("❌ No raw transcript files found")
        return
    
    print(f"Found {len(transcript_files)} raw transcript files to fix")
    
    fixed_count = 0
    for file_path in transcript_files:
        if fix_raw_transcript_frontmatter(file_path):
            fixed_count += 1
    
    print(f"\n✓ Fixed {fixed_count}/{len(transcript_files)} files")

if __name__ == "__main__":
    main()