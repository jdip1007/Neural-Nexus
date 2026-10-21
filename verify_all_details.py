#!/usr/bin/env python3
"""
Comprehensive verification of all changed/new markdown files before deployment.
Checks: frontmatter, wikilinks, source citations, tags taxonomy, content format.
"""

import os
import re
import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime

NEURAL_NEXUS_PATH = Path(os.getenv('NEURAL_NEXUS_PATH', '~/Neural-Nexus/docs')).expanduser()
REPO_ROOT = NEURAL_NEXUS_PATH.parent
SCHEMA_PATH = REPO_ROOT / 'docs' / 'SCHEMA.md'

issues = []
warnings = []
verified = []

def load_schema_tags():
    """Load tag taxonomy from SCHEMA.md."""
    tags = set()
    if not SCHEMA_PATH.exists():
        warnings.append("SCHEMA.md not found - skipping tag taxonomy check")
        return tags
    
    content = SCHEMA_PATH.read_text()
    # Look for tag taxonomy sections - try different patterns
    # Pattern 1: tags: [tag1, tag2, ...]
    tag_lists = re.findall(r'tags:\s*\[([^\]]+)\]', content)
    for tl in tag_lists:
        for tag in tl.split(','):
            tags.add(tag.strip().strip('"').strip("'"))
    
    # Pattern 2: - tagname (indented list under tags:)
    tag_items = re.findall(r'^\s+-\s+(\S+)', content, re.MULTILINE)
    for tag in tag_items:
        tags.add(tag.strip())
    
    # Also extract domain values
    domain_vals = re.findall(r'domain:\s*(\S+)', content)
    for d in domain_vals:
        tags.add(d.strip())
    
    return tags

def check_frontmatter(file_path, content, file_type):
    """Check frontmatter has all required fields."""
    if not content.startswith('---'):
        issues.append(f"❌ Missing frontmatter: {file_path}")
        return None
    
    end = content.find('---', 3)
    if end == -1:
        issues.append(f"❌ Invalid frontmatter (no closing ---): {file_path}")
        return None
    
    frontmatter = content[3:end]
    
    # Required fields based on type
    if file_type in ('entity', 'reading', 'finding', 'concept'):
        required = ['title', 'created', 'updated', 'type', 'tags', 'sources']
    elif file_type == 'raw':
        required = ['title', 'created', 'updated', 'type', 'tags']
    else:
        required = ['title', 'created', 'updated', 'type', 'tags']
    
    for field in required:
        if field not in frontmatter:
            issues.append(f"❌ Missing frontmatter field '{field}': {file_path}")
    
    # Validate date format
    for date_field in ['created', 'updated']:
        match = re.search(rf'{date_field}:\s*(\S+)', frontmatter)
        if match:
            date_val = match.group(1)
            try:
                datetime.strptime(date_val, '%Y-%m-%d')
            except ValueError:
                issues.append(f"❌ Invalid date format for {date_field} '{date_val}': {file_path}")
    
    # Validate type field
    type_match = re.search(r'type:\s*(\S+)', frontmatter)
    if type_match:
        type_val = type_match.group(1)
        valid_types = ['concept', 'entity', 'finding', 'reading', 'idea', 'comparison', 'raw', 'video']
        if type_val not in valid_types:
            warnings.append(f"⚠️ Unusual type '{type_val}': {file_path}")
    
    return frontmatter

def check_wikilinks(file_path, content):
    """Check all wikilinks point to existing pages."""
    wikilinks = re.findall(r'\[\[([^\]]+)\]\]', content)
    broken = []
    for link in wikilinks:
        link_name = link.split('|')[0].strip()
        # Check possible paths
        possible_paths = [
            REPO_ROOT / 'docs' / f'{link_name}.md',
            REPO_ROOT / 'docs' / 'concepts' / f'{link_name}.md',
            REPO_ROOT / 'docs' / 'entities' / f'{link_name}.md',
            REPO_ROOT / 'docs' / 'readings' / f'{link_name}.md',
            REPO_ROOT / 'docs' / 'findings' / f'{link_name}.md',
        ]
        
        if any(p.exists() for p in possible_paths):
            continue
        
        # Case-insensitive fallback
        found = False
        for subdir in ['concepts', 'entities', 'readings', 'findings', 'raw']:
            target_dir = REPO_ROOT / 'docs' / subdir
            if target_dir.exists():
                for f in target_dir.glob('*.md'):
                    if f.stem.lower() == link_name.lower():
                        found = True
                        break
            if found:
                break
        
        if not found:
            broken.append(link_name)
    
    if broken:
        for b in broken:
            issues.append(f"❌ Broken wikilink [[{b}]]: {file_path}")

def check_source_citations(file_path, content):
    """Check source citations point to existing files."""
    # Only for entity/reading/finding/concept pages
    if not content.startswith('---'):
        return
    
    end = content.find('---', 3)
    if end == -1:
        return
    
    frontmatter = content[3:end]
    
    # Check sources: [raw/videos/file.md, ...]
    sources_match = re.search(r'sources:\s*\[(.+?)\]', frontmatter)
    if sources_match:
        for source in sources_match.group(1).split(','):
            source = source.strip()
            source_path = REPO_ROOT / 'docs' / source
            if not source_path.exists():
                issues.append(f"❌ Broken source citation '{source}': {file_path}")
    
    # For raw files, check source_url field
    if '/raw/' in str(file_path):
        remaining = content[end + 3:]
        for field in ['source_url', 'source_type']:
            if field not in remaining:
                issues.append(f"❌ Missing field '{field}' in raw source: {file_path}")

def check_tags_taxonomy(file_path, content, valid_tags):
    """Check tags exist in SCHEMA.md taxonomy."""
    if not content.startswith('---'):
        return
    
    end = content.find('---', 3)
    if end == -1:
        return
    
    frontmatter = content[3:end]
    tags_match = re.search(r'tags:\s*\[([^\]]+)\]', frontmatter)
    if tags_match and valid_tags:
        for tag in tags_match.group(1).split(','):
            tag = tag.strip().strip('"').strip("'")
            # Skip very common/dynamic tags that may not be in schema
            skip_tags = {'youtube', 'video-summary', 'transcript'}
            if tag in skip_tags:
                continue
            if valid_tags and tag not in valid_tags:
                # Not a hard failure - just a warning
                warnings.append(f"⚠️ Tag '{tag}' not in SCHEMA.md taxonomy: {file_path}")

def check_content_format(file_path, content):
    """Check content is properly formatted and not empty."""
    # Check file is not just frontmatter
    if content.startswith('---'):
        end = content.find('---', 3)
        if end != -1:
            body = content[end + 3:].strip()
            if not body:
                issues.append(f"❌ Empty body content: {file_path}")
            elif len(body) < 20:
                warnings.append(f"⚠️ Very short body content ({len(body)} chars): {file_path}")
    
    # Check for proper markdown headers
    if not re.search(r'^#\s+', content, re.MULTILINE):
        warnings.append(f"⚠️ No top-level header (# ) found: {file_path}")

def main():
    os.chdir(REPO_ROOT)
    
    print("=" * 60)
    print("COMPREHENSIVE PRE-DEPLOYMENT VERIFICATION")
    print("=" * 60)
    print()
    
    # Load tag taxonomy
    print("📋 Loading SCHEMA.md tag taxonomy...")
    valid_tags = load_schema_tags()
    if valid_tags:
        print(f"   ✓ Loaded {len(valid_tags)} valid tags from SCHEMA.md")
    else:
        print("   ⚠️ No tags loaded from SCHEMA.md")
    print()
    
    # Get all changed markdown files
    result = subprocess.run(
        ['git', 'status', '--porcelain'],
        capture_output=True, text=True, timeout=30
    )
    
    changed_files = []
    for line in result.stdout.split('\n'):
        if not line.strip():
            continue
        parts = line.strip().split(maxsplit=1)
        if len(parts) == 2 and parts[1].endswith('.md'):
            changed_files.append(parts[1])
    
    print(f"📄 Found {len(changed_files)} changed/new markdown files")
    print()
    
    # Categorize files
    entity_files = [f for f in changed_files if '/entities/' in f]
    reading_files = [f for f in changed_files if '/readings/' in f]
    raw_files = [f for f in changed_files if '/raw/' in f]
    other_files = [f for f in changed_files if f not in entity_files + reading_files + raw_files]
    
    print(f"   Entities: {len(entity_files)}")
    print(f"   Readings: {len(reading_files)}")
    print(f"   Raw sources: {len(raw_files)}")
    print(f"   Other: {len(other_files)}")
    print()
    
    # Verify each file
    for file_path in changed_files:
        full_path = Path(file_path)
        if not full_path.exists():
            issues.append(f"❌ File not found: {file_path}")
            continue
        
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Determine type
        if '/entities/' in file_path:
            file_type = 'entity'
        elif '/readings/' in file_path:
            file_type = 'reading'
        elif '/raw/' in file_path:
            file_type = 'raw'
        elif '/findings/' in file_path:
            file_type = 'finding'
        elif '/concepts/' in file_path:
            file_type = 'concept'
        else:
            file_type = 'other'
        
        # Run all checks
        check_frontmatter(file_path, content, file_type)
        check_wikilinks(file_path, content)
        check_source_citations(file_path, content)
        check_tags_taxonomy(file_path, content, valid_tags)
        check_content_format(file_path, content)
        
        verified.append(file_path)
    
    # Summary
    print("=" * 60)
    print("VERIFICATION RESULTS")
    print("=" * 60)
    print()
    print(f"✅ Files verified: {len(verified)}")
    print()
    
    if issues:
        print(f"❌ CRITICAL ISSUES ({len(issues)}):")
        for issue in issues:
            print(f"   {issue}")
        print()
    
    if warnings:
        print(f"⚠️ WARNINGS ({len(warnings)}):")
        for warning in warnings:
            print(f"   {warning}")
        print()
    
    if not issues and not warnings:
        print("✅ ALL CHECKS PASSED - Ready for deployment!")
    elif not issues:
        print("✅ No critical issues - Warnings only, safe to deploy")
    else:
        print("❌ CRITICAL ISSUES FOUND - DO NOT DEPLOY until fixed")
    
    print()
    return len(issues) == 0

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
