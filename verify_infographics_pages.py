#!/usr/bin/env python3
"""
Comprehensive verification script for The Infographics Show pages.
Checks all quality requirements before deployment.
"""

import json
import os
import re
import yaml
from datetime import datetime
import frontmatter

def load_schema():
    """Load SCHEMA.md taxonomy"""
    schema_path = "docs/SCHEMA.md"
    if not os.path.exists(schema_path):
        print("❌ SCHEMA.md not found")
        return {}
    
    with open(schema_path, 'r') as f:
        content = f.read()
    
    # Extract tags from SCHEMA.md
    tags = set()
    # Look for tag sections in the schema
    tag_pattern = r'##\s*Tags?\s*\n(.*?)(?=##|\Z)'
    matches = re.findall(tag_pattern, content, re.DOTALL)
    
    for match in matches:
        # Extract individual tags
        tag_lines = re.findall(r'-\s*`([^`]+)`', match)
        tags.update(tag_lines)
    
    return tags

def check_frontmatter(page_path):
    """Check if page has proper frontmatter"""
    try:
        with open(page_path, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
        
        required_fields = ['title', 'created', 'updated', 'type', 'sources']
        missing_fields = []
        
        for field in required_fields:
            if field not in post.metadata:
                missing_fields.append(field)
        
        # Check tags
        tags = post.metadata.get('tags', [])
        if not tags or not isinstance(tags, list):
            missing_fields.append('tags')
        
        return {
            'valid': len(missing_fields) == 0,
            'missing_fields': missing_fields,
            'title': post.metadata.get('title', ''),
            'type': post.metadata.get('type', ''),
            'tags': tags,
            'sources': post.metadata.get('sources', [])
        }
    except Exception as e:
        return {'valid': False, 'error': str(e)}

def check_wikilinks(page_path):
    """Check if all wikilinks are valid"""
    try:
        with open(page_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all wikilinks
        wikilinks = re.findall(r'\[\[([^\]]+)\]\]', content)
        
        invalid_links = []
        for link in wikilinks:
            # Check if link points to existing file
            possible_paths = [
                f"docs/{link}.md",
                f"docs/{link.replace(' ', '-')}.md",
                f"docs/concepts/{link}.md",
                f"docs/entities/{link}.md",
                f"docs/readings/{link}.md"
            ]
            
            link_exists = any(os.path.exists(path) for path in possible_paths)
            if not link_exists:
                invalid_links.append(link)
        
        return {
            'valid': len(invalid_links) == 0,
            'invalid_links': invalid_links,
            'total_links': len(wikilinks)
        }
    except Exception as e:
        return {'valid': False, 'error': str(e)}

def check_source_citations(page_path):
    """Check if source citations are correct and files exist"""
    try:
        with open(page_path, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
        
        sources = post.metadata.get('sources', [])
        missing_sources = []
        
        for source in sources:
            source_path = f"docs/{source}"
            if not os.path.exists(source_path):
                missing_sources.append(source)
        
        return {
            'valid': len(missing_sources) == 0,
            'missing_sources': missing_sources,
            'total_sources': len(sources)
        }
    except Exception as e:
        return {'valid': False, 'error': str(e)}

def check_content_format(page_path):
    """Check if content is properly formatted"""
    try:
        with open(page_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        issues = []
        
        # Check for proper heading structure
        if not content.startswith('# '):
            issues.append("Missing main heading")
        
        # Check for empty sections
        sections = re.findall(r'^#+\s+(.*)$', content, re.MULTILINE)
        empty_sections = []
        for i, section in enumerate(sections):
            if i < len(sections) - 1:
                next_section_pos = content.find(f"{'#' * (i + 1)} {sections[i + 1]}", content.find(f"#{i + 1} {section}"))
                section_content = content[content.find(f"#{i + 1} {section}") + len(f"#{i + 1} {section}"):next_section_pos].strip()
                if not section_content:
                    empty_sections.append(section)
        
        if empty_sections:
            issues.append(f"Empty sections: {empty_sections}")
        
        return {
            'valid': len(issues) == 0,
            'issues': issues,
            'sections': len(sections)
        }
    except Exception as e:
        return {'valid': False, 'error': str(e)}

def main():
    print("🔍 Starting comprehensive verification of The Infographics Show pages...")
    
    # Load schema
    schema_tags = load_schema()
    print(f"📋 Loaded {len(schema_tags)} tags from SCHEMA.md")
    
    # Find all The Infographics Show pages
    infographics_pages = []
    docs_dir = "docs"
    
    # Search in different directories
    search_dirs = ["docs/youtube", "docs/readings", "docs/entities"]
    
    for search_dir in search_dirs:
        if os.path.exists(search_dir):
            for root, dirs, files in os.walk(search_dir):
                for file in files:
                    if file.endswith('.md') and ('infographics' in file.lower() or 'k0ksj42YJaM' in file or 'uzg-tGiK_y8' in file or 'cemy5eP5Jjs' in file or '8zUhBnpVgdE' in file or 'D4nPxik59oE' in file):
                        page_path = os.path.join(root, file)
                        infographics_pages.append(page_path)
    
    print(f"📄 Found {len(infographics_pages)} The Infographics Show pages")
    
    if not infographics_pages:
        print("❌ No The Infographics Show pages found")
        return
    
    # Verify each page
    results = []
    for page_path in infographics_pages:
        print(f"\n📝 Verifying: {page_path}")
        
        # Check frontmatter
        frontmatter_result = check_frontmatter(page_path)
        
        # Check wikilinks
        wikilinks_result = check_wikilinks(page_path)
        
        # Check source citations
        sources_result = check_source_citations(page_path)
        
        # Check content format
        content_result = check_content_format(page_path)
        
        # Check tags against schema
        tags_valid = True
        invalid_tags = []
        if frontmatter_result.get('tags'):
            for tag in frontmatter_result['tags']:
                if tag not in schema_tags:
                    invalid_tags.append(tag)
                    tags_valid = False
        
        page_result = {
            'path': page_path,
            'frontmatter_valid': frontmatter_result['valid'],
            'wikilinks_valid': wikilinks_result['valid'],
            'sources_valid': sources_result['valid'],
            'content_valid': content_result['valid'],
            'tags_valid': tags_valid,
            'title': frontmatter_result.get('title', ''),
            'issues': []
        }
        
        if not frontmatter_result['valid']:
            page_result['issues'].append(f"Missing frontmatter fields: {frontmatter_result['missing_fields']}")
        
        if not wikilinks_result['valid']:
            page_result['issues'].append(f"Invalid wikilinks: {wikilinks_result['invalid_links']}")
        
        if not sources_result['valid']:
            page_result['issues'].append(f"Missing sources: {sources_result['missing_sources']}")
        
        if not content_result['valid']:
            page_result['issues'].append(f"Content issues: {content_result['issues']}")
        
        if not tags_valid:
            page_result['issues'].append(f"Invalid tags: {invalid_tags}")
        
        results.append(page_result)
    
    # Generate report
    print("\n" + "="*60)
    print("📊 VERIFICATION REPORT")
    print("="*60)
    
    total_pages = len(results)
    valid_pages = sum(1 for r in results if all([r['frontmatter_valid'], r['wikilinks_valid'], r['sources_valid'], r['content_valid'], r['tags_valid']]))
    
    print(f"📄 Total pages: {total_pages}")
    print(f"✅ Valid pages: {valid_pages}")
    print(f"❌ Invalid pages: {total_pages - valid_pages}")
    
    if total_pages > 0:
        success_rate = (valid_pages / total_pages) * 100
        print(f"📈 Success rate: {success_rate:.1f}%")
    
    # Show issues
    if total_pages - valid_pages > 0:
        print("\n🔴 ISSUES FOUND:")
        print("-" * 40)
        for result in results:
            if not all([result['frontmatter_valid'], result['wikilinks_valid'], result['sources_valid'], result['content_valid'], result['tags_valid']]):
                print(f"\n❌ {result['path']}")
                print(f"   Title: {result['title']}")
                for issue in result['issues']:
                    print(f"   - {issue}")
    
    # Deployment recommendation
    print("\n" + "="*60)
    if valid_pages == total_pages:
        print("🚀 DEPLOYMENT READY: All pages meet quality standards!")
        print("✅ All frontmatter is correct")
        print("✅ All wikilinks are valid")
        print("✅ All source citations are correct")
        print("✅ All content is properly formatted")
        print("✅ All tags are in the schema")
    else:
        print("⚠️  DEPLOYMENT BLOCKED: Issues found that need to be resolved")
        print("   Please fix the issues above before deploying")
    
    print("="*60)

if __name__ == "__main__":
    main()