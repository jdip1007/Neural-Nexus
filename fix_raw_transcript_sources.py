#!/usr/bin/env python3
"""
Fix sources field in raw transcript files to remove self-references.
"""

import os
import re
from pathlib import Path

def fix_raw_transcript_sources(file_path):
    """Fix sources field in a raw transcript file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract video ID from filename
        filename = os.path.basename(file_path)
        video_id = filename.replace('youtube-', '').replace('-transcript.md', '')
        
        # Fix sources field - remove self-reference and add the video URL
        new_sources_field = f'sources: ["https://www.youtube.com/watch?v={video_id}"]'
        
        # Replace sources field
        sources_pattern = r'sources:\s*\[([^\]]+)\]'
        new_content = re.sub(sources_pattern, new_sources_field, content)
        
        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✓ Fixed sources in {file_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error fixing {file_path}: {e}")
        return False

def main():
    """Main function to fix sources in all raw transcript files."""
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
        if fix_raw_transcript_sources(file_path):
            fixed_count += 1
    
    print(f"\n✓ Fixed sources in {fixed_count}/{len(transcript_files)} files")

if __name__ == "__main__":
    main()