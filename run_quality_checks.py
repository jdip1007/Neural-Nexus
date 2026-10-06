#!/usr/bin/env python3
import json
import os
import glob
from datetime import datetime

def update_catalog():
    """Update the catalog.json with all pages"""
    catalog_file = '/home/hermes/Neural-Nexus/docs/catalog.json'
    
    # Find all markdown files in docs directory
    docs_path = '/home/hermes/Neural-Nexus/docs'
    md_files = glob.glob(os.path.join(docs_path, '*.md'))
    
    catalog = {}
    
    for md_file in md_files:
        try:
            # Extract filename without extension
            filename = os.path.basename(md_file)
            name = os.path.splitext(filename)[0]
            
            # Read frontmatter if it exists
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract frontmatter
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    frontmatter = parts[1].strip()
                    try:
                        fm_data = json.loads(frontmatter)
                        catalog[name] = {
                            'title': fm_data.get('title', name),
                            'file': md_file,
                            'type': fm_data.get('type', 'page'),
                            'tags': fm_data.get('tags', []),
                            'created': fm_data.get('created'),
                            'updated': fm_data.get('updated'),
                            'sources': fm_data.get('sources', [])
                        }
                        continue
                    except json.JSONDecodeError:
                        pass
            
            # If no frontmatter, create basic entry
            catalog[name] = {
                'title': name,
                'file': md_file,
                'type': 'page',
                'tags': [],
                'created': datetime.now().isoformat(),
                'updated': datetime.now().isoformat()
            }
            
        except Exception as e:
            print(f"Error processing {md_file}: {e}")
    
    # Save catalog
    with open(catalog_file, 'w') as f:
        json.dump(catalog, f, indent=2)
    
    return catalog

def build_graph():
    """Build the graph.json file"""
    catalog_file = '/home/hermes/Neural-Nexus/docs/catalog.json'
    graph_file = '/home/hermes/Neural-Nexus/docs/graph.json'
    
    # Load catalog
    with open(catalog_file, 'r') as f:
        catalog = json.load(f)
    
    # Build graph nodes
    nodes = []
    links = []
    
    for page_id, page_data in catalog.items():
        node = {
            'id': page_id,
            'title': page_data['title'],
            'file': page_data['file'],
            'tags': page_data['tags'],
            'type': page_data['type']
        }
        nodes.append(node)
        
        # Create links based on shared tags
        for other_id, other_data in catalog.items():
            if page_id != other_id:
                shared_tags = set(page_data['tags']) & set(other_data['tags'])
                if shared_tags:
                    links.append({
                        'source': page_id,
                        'target': other_id,
                        'weight': len(shared_tags),
                        'tags': list(shared_tags)
                    })
    
    # Build graph
    graph = {
        'nodes': nodes,
        'links': links,
        'generated': datetime.now().isoformat()
    }
    
    # Save graph
    with open(graph_file, 'w') as f:
        json.dump(graph, f, indent=2)
    
    return graph

def run_quality_checks():
    """Run basic quality checks on the created pages"""
    issues = []
    
    # Check for proper frontmatter
    docs_path = '/home/hermes/Neural-Nexus/docs'
    youtube_files = glob.glob(os.path.join(docs_path, 'youtube-*.md'))
    
    for md_file in youtube_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check for frontmatter
            if not content.startswith('---'):
                issues.append(f"{md_file}: Missing frontmatter")
                continue
            
            # Check for required fields
            parts = content.split('---', 2)
            if len(parts) >= 3:
                frontmatter = parts[1].strip()
                try:
                    fm_data = json.loads(frontmatter)
                    required_fields = ['title', 'type', 'tags', 'sources']
                    for field in required_fields:
                        if field not in fm_data:
                            issues.append(f"{md_file}: Missing required field '{field}'")
                except json.JSONDecodeError:
                    issues.append(f"{md_file}: Invalid frontmatter JSON")
            
            # Check for transcript section
            if '```transcript' not in content:
                issues.append(f"{md_file}: Missing transcript section")
                
        except Exception as e:
            issues.append(f"{md_file}: Error reading file - {e}")
    
    return issues

def main():
    print("Running quality checks and building catalog...")
    
    # Run quality checks
    issues = run_quality_checks()
    if issues:
        print("Quality check issues found:")
        for issue in issues:
            print(f"  - {issue}")
    else:
        print("✓ Quality checks passed")
    
    # Update catalog
    print("Updating catalog...")
    catalog = update_catalog()
    print(f"✓ Catalog updated with {len(catalog)} pages")
    
    # Build graph
    print("Building graph...")
    graph = build_graph()
    print(f"✓ Graph built with {len(graph['nodes'])} nodes and {len(graph['links'])} links")
    
    print("\nQuality check summary:")
    print(f"- Pages processed: {len(catalog)}")
    print(f"- Issues found: {len(issues)}")
    print(f"- Graph nodes: {len(graph['nodes'])}")
    print(f"- Graph links: {len(graph['links'])}")
    
    return len(issues) == 0

if __name__ == '__main__':
    success = main()
    exit(0 if success else 1)