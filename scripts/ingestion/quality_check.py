#!/usr/bin/env python3
"""
Quality check script for Neural Nexus pages
"""

import os
import json
import re
from pathlib import Path
from datetime import datetime

def check_frontmatter(file_path):
    """Check if file has proper frontmatter"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for JSON frontmatter (wrapped in ---{...}---)
        json_frontmatter_match = re.match(r'^---\s*\n(\{.*?\})\n---\s*\n', content, re.DOTALL)
        if json_frontmatter_match:
            frontmatter = json_frontmatter_match.group(1)
            try:
                frontmatter_data = json.loads(frontmatter)
                
                # Check required fields
                required_fields = ['title', 'created', 'updated', 'type']
                for field in required_fields:
                    if field not in frontmatter_data:
                        return False, f"Missing required field: {field}"
                
                # Check sources field
                if 'sources' not in frontmatter_data:
                    return False, "Missing sources field"
                
                return True, "Frontmatter is valid (JSON format)"
            except json.JSONDecodeError:
                return False, "Invalid JSON in frontmatter"
        
        # Check for YAML frontmatter (wrapped in ---...---)
        yaml_frontmatter_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if not yaml_frontmatter_match:
            return False, "Missing frontmatter"
        
        frontmatter = yaml_frontmatter_match.group(1)
        
        # Check required fields
        required_fields = ['title', 'created', 'updated', 'type']
        for field in required_fields:
            if f'{field}:' not in frontmatter:
                return False, f"Missing required field: {field}"
        
        # Check sources field
        if 'sources:' not in frontmatter:
            return False, "Missing sources field"
        
        return True, "Frontmatter is valid (YAML format)"
    
    except Exception as e:
        return False, f"Error reading file: {e}"

def check_wikilinks(file_path, all_files):
    """Check if wikilinks point to existing pages"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract wikilinks
        wikilinks = re.findall(r'\[\[(.*?)\]\]', content)
        issues = []
        
        for wikilink in wikilinks:
            found = False
            for other_file in all_files:
                other_stem = other_file.stem
                if wikilink.lower() in other_stem.lower() or wikilink.lower() in other_file.name.lower():
                    found = True
                    break
            
            if not found:
                issues.append(f"Broken wikilink: {wikilink}")
        
        return True if not issues else False, issues if issues else "Wikilinks are valid"
    
    except Exception as e:
        return False, f"Error checking wikilinks: {e}"

def check_sources(file_path):
    """Check if sources are valid URLs"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for JSON frontmatter
        json_frontmatter_match = re.match(r'^---\s*\n(\{.*?\})\n---\s*\n', content, re.DOTALL)
        if json_frontmatter_match:
            frontmatter = json_frontmatter_match.group(1)
            try:
                frontmatter_data = json.loads(frontmatter)
                
                if 'sources' not in frontmatter_data:
                    return False, "No sources found in frontmatter"
                
                sources = frontmatter_data['sources']
                if not isinstance(sources, list):
                    return False, "Sources should be a list"
                
                issues = []
                for source in sources:
                    if not isinstance(source, str) or not source.startswith(('http://', 'https://')):
                        issues.append(f"Invalid source URL: {source}")
                
                return True if not issues else False, issues if issues else "Sources are valid"
            except json.JSONDecodeError:
                return False, "Invalid JSON in frontmatter"
        
        # Check for YAML frontmatter
        yaml_frontmatter_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if not yaml_frontmatter_match:
            return False, "Missing frontmatter for sources check"
        
        frontmatter = yaml_frontmatter_match.group(1)
        
        # Extract sources (handle both JSON and YAML formats)
        sources_match = re.search(r'sources:\s*\[(.*?)\]', frontmatter, re.DOTALL)
        if not sources_match:
            # Try alternative YAML format with line breaks - be more precise
            sources_match = re.search(r'sources:\s*\n(.*?)(?=\n\S+:|\n---|\Z)', frontmatter, re.DOTALL)
            if sources_match:
                sources_str = sources_match.group(1)
                # Extract individual source lines - only lines starting with -
                sources = []
                for line in sources_str.split('\n'):
                    line = line.strip()
                    if line.startswith('-') and not line.startswith('--') and ':' not in line:
                        source = line[1:].strip().strip('"\'')
                        if source:
                            sources.append(source)
            else:
                return False, "No sources found in frontmatter"
        else:
            sources_str = sources_match.group(1)
            sources = [s.strip().strip('"\'') for s in sources_str.split(',') if s.strip()]
        
        issues = []
        for source in sources:
            # Accept both HTTP URLs and local file paths
            if not (source.startswith(('http://', 'https://')) or source.startswith('./') or source.startswith('/') or source.startswith('raw/')):
                issues.append(f"Invalid source format: {source}")
        
        return True if not issues else False, issues if issues else "Sources are valid"
    
    except Exception as e:
        return False, f"Error checking sources: {e}"

def check_tags(file_path, schema_file):
    """Check if tags exist in SCHEMA.md"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for JSON frontmatter
        json_frontmatter_match = re.match(r'^---\s*\n(\{.*?\})\n---\s*\n', content, re.DOTALL)
        if json_frontmatter_match:
            frontmatter = json_frontmatter_match.group(1)
            try:
                frontmatter_data = json.loads(frontmatter)
                
                if 'tags' not in frontmatter_data:
                    return False, "No tags found in frontmatter"
                
                tags = frontmatter_data['tags']
                if not isinstance(tags, list):
                    return False, "Tags should be a list"
                
                # Check against schema
                if os.path.exists(schema_file):
                    with open(schema_file, 'r', encoding='utf-8') as f:
                        schema_content = f.read()
                    
                    # Extract individual tags from schema sections
                    schema_tags = []
                    sections = re.split(r'##\s+', schema_content)
                    for section in sections[1:]:  # Skip the first part before first ##
                        lines = section.split('\n')
                        for line in lines:
                            line = line.strip()
                            if line and not line.startswith('#') and not line.startswith('*'):
                                # Clean up tag names
                                tag = line.replace('**', '').strip()
                                if tag:
                                    schema_tags.append(tag)
                    
                    issues = []
                    for tag in tags:
                        if tag not in schema_tags:
                            issues.append(f"Tag not in schema: {tag}")
                    
                    return True if not issues else False, issues if issues else "Tags are valid"
                else:
                    return False, "SCHEMA.md not found"
            except json.JSONDecodeError:
                return False, "Invalid JSON in frontmatter"
        
        # Check for YAML frontmatter
        yaml_frontmatter_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if not yaml_frontmatter_match:
            return False, "Missing frontmatter for tags check"
        
        frontmatter = yaml_frontmatter_match.group(1)
        
        # Extract tags (handle both JSON and YAML formats)
        tags_match = re.search(r'tags:\s*\[(.*?)\]', frontmatter, re.DOTALL)
        if not tags_match:
            # Try alternative YAML format with line breaks
            tags_match = re.search(r'tags:\s*\n(.*?)(?=\n\S:|\n---|\Z)', frontmatter, re.DOTALL)
            if tags_match:
                tags_str = tags_match.group(1)
                # Extract individual tag lines
                tags = []
                for line in tags_str.split('\n'):
                    line = line.strip()
                    if line.startswith('-') and not line.startswith('--'):
                        tag = line[1:].strip().strip('"\'')
                        if tag:
                            tags.append(tag)
            else:
                return False, "No tags found in frontmatter"
        else:
            tags_str = tags_match.group(1)
            tags = [tag.strip().strip('"\'') for tag in tags_str.split(',') if tag.strip()]
        
        # Check against schema
        if os.path.exists(schema_file):
            with open(schema_file, 'r', encoding='utf-8') as f:
                schema_content = f.read()
            
            # Extract individual tags from schema sections
            schema_tags = []
            sections = re.split(r'##\s+', schema_content)
            for section in sections[1:]:  # Skip the first part before first ##
                lines = section.split('\n')
                for line in lines:
                    line = line.strip()
                    if line and not line.startswith('#') and not line.startswith('*'):
                        # Clean up tag names
                        tag = line.replace('**', '').strip()
                        if tag:
                            schema_tags.append(tag)
                    
            issues = []
            for tag in tags:
                if tag not in schema_tags:
                    issues.append(f"Tag not in schema: {tag}")
            
            return True if not issues else False, issues if issues else "Tags are valid"
        else:
            return False, "SCHEMA.md not found"
    
    except Exception as e:
        return False, f"Error checking tags: {e}"

def main():
    """Main quality check function"""
    docs_path = "/home/hermes/Neural-Nexus/docs"
    schema_file = os.path.join(docs_path, "SCHEMA.md")
    
    print("🔍 Starting Quality Checks...")
    print("=" * 50)
    
    # Get all markdown files
    md_files = list(Path(docs_path).glob("*.md"))
    md_files = [f for f in md_files if not f.name.startswith("graph.json")]
    
    results = {
        "total_files": len(md_files),
        "frontmatter_issues": 0,
        "wikilink_issues": 0,
        "source_issues": 0,
        "tag_issues": 0,
        "valid_files": 0
    }
    
    for md_file in md_files:
        file_name = md_file.name
        print(f"\n📄 Checking: {file_name}")
        
        # Check frontmatter
        frontmatter_ok, frontmatter_msg = check_frontmatter(md_file)
        if not frontmatter_ok:
            print(f"  ❌ Frontmatter: {frontmatter_msg}")
            results["frontmatter_issues"] += 1
        else:
            print(f"  ✅ Frontmatter: {frontmatter_msg}")
        
        # Check wikilinks
        wikilink_ok, wikilink_msg = check_wikilinks(md_file, md_files)
        if not wikilink_ok:
            if isinstance(wikilink_msg, list):
                print(f"  ❌ Wikilinks: {len(wikilink_msg)} issues")
                for issue in wikilink_msg:
                    print(f"    - {issue}")
            else:
                print(f"  ❌ Wikilinks: {wikilink_msg}")
            results["wikilink_issues"] += 1
        else:
            print(f"  ✅ Wikilinks: {wikilink_msg}")
        
        # Check sources
        sources_ok, sources_msg = check_sources(md_file)
        if not sources_ok:
            if isinstance(sources_msg, list):
                print(f"  ❌ Sources: {len(sources_msg)} issues")
                for issue in sources_msg:
                    print(f"    - {issue}")
            else:
                print(f"  ❌ Sources: {sources_msg}")
            results["source_issues"] += 1
        else:
            print(f"  ✅ Sources: {sources_msg}")
        
        # Check tags
        tags_ok, tags_msg = check_tags(md_file, schema_file)
        if not tags_ok:
            if isinstance(tags_msg, list):
                print(f"  ❌ Tags: {len(tags_msg)} issues")
                for issue in tags_msg:
                    print(f"    - {issue}")
            else:
                print(f"  ❌ Tags: {tags_msg}")
            results["tag_issues"] += 1
        else:
            print(f"  ✅ Tags: {tags_msg}")
        
        # If all checks passed
        if frontmatter_ok and wikilink_ok and sources_ok and tags_ok:
            results["valid_files"] += 1
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 Quality Check Summary")
    print("=" * 50)
    print(f"Total files checked: {results['total_files']}")
    print(f"Valid files: {results['valid_files']}")
    print(f"Frontmatter issues: {results['frontmatter_issues']}")
    print(f"Wikilink issues: {results['wikilink_issues']}")
    print(f"Source issues: {results['source_issues']}")
    print(f"Tag issues: {results['tag_issues']}")
    
    if results['valid_files'] == results['total_files']:
        print("\n🎉 All files passed quality checks!")
        return True
    else:
        print(f"\n⚠️  {results['total_files'] - results['valid_files']} files have issues")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)