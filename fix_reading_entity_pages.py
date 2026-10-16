#!/usr/bin/env python3
"""Fix reading and entity pages for Infographics Show videos."""
import re
from pathlib import Path
import yaml

video_ids = ['zeVq8Pt2JCc', 'ZV6pUX8kJwg', '8M8U9Tj15bI', 'bD8ta7nsA8A', 'p5KvyYwaj4s']

fixed_count = 0
error_count = 0

for vid in video_ids:
    # Fix reading pages
    reading_path = Path(f'docs/readings/youtube-{vid}-summary.md')
    if reading_path.exists():
        content = reading_path.read_text(encoding='utf-8')
        # Fix Python-style boolean
        content = content.replace('time_sensitive: True', 'time_sensitive: true')
        content = content.replace('time_sensitive: False', 'time_sensitive: false')
        reading_path.write_text(content, encoding='utf-8')
        fixed_count += 1

    # Fix entity pages
    for entity_file in Path('docs/entities').glob(f'youtube-{vid}-*.md'):
        content = entity_file.read_text(encoding='utf-8')
        content = content.replace('time_sensitive: True', 'time_sensitive: true')
        content = content.replace('time_sensitive: False', 'time_sensitive: false')
        entity_file.write_text(content, encoding='utf-8')
        fixed_count += 1

print(f'Fixed {fixed_count} reading/entity files')
