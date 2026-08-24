#!/usr/bin/env python3
"""
Graph build script for Neural Nexus
"""

import os
import json
import re
from datetime import datetime
from pathlib import Path

def build_graph(docs_path):
    """Build graph of pages and their relationships"""
    graph = {
        "nodes": [],
        "edges": [],
        "metadata": {
            "generated": datetime.now().isoformat(),
            "total_nodes": 0,
            "total_edges": 0
        }
    }
    
    # Scan all markdown files
    md_files = list(Path(docs_path).glob("*.md"))
    
    for md_file in md_files:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract frontmatter
        frontmatter_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if frontmatter_match:
            frontmatter = frontmatter_match.group(1)
            # Simple YAML parsing for this example
            title_match = re.search(r'title:\s*(.*)', frontmatter)
            tags_match = re.search(r'tags:\s*\[(.*?)\]', frontmatter, re.DOTALL)
            
            title = title_match.group(1).strip() if title_match else md_file.stem
            tags = tags_match.group(1).split(',') if tags_match else []
            tags = [tag.strip().strip('\'"') for tag in tags if tag.strip()]
            
            # Add node
            node_id = md_file.stem
            graph["nodes"].append({
                "id": node_id,
                "title": title,
                "file": str(md_file),
                "tags": tags,
                "type": "page"
            })
            
            # Extract wikilinks
            wikilinks = re.findall(r'\[\[(.*?)\]\]', content)
            for wikilink in wikilinks:
                # Find target file
                target_file = None
                for other_md in md_files:
                    other_stem = other_md.stem
                    if wikilink.lower() in other_stem.lower() or wikilink.lower() in other_md.name.lower():
                        target_file = other_md.stem
                        break
                
                if target_file and target_file != node_id:
                    graph["edges"].append({
                        "source": node_id,
                        "target": target_file,
                        "type": "wikilink"
                    })
    
    # Update metadata
    graph["metadata"]["total_nodes"] = len(graph["nodes"])
    graph["metadata"]["total_edges"] = len(graph["edges"])
    
    # Save graph
    graph_file = os.path.join(docs_path, "graph.json")
    with open(graph_file, 'w', encoding='utf-8') as f:
        json.dump(graph, f, indent=2)
    
    return graph

if __name__ == "__main__":
    docs_path = "/home/hermes/Neural-Nexus/docs"
    graph = build_graph(docs_path)
    print(f"Graph built with {graph['metadata']['total_nodes']} nodes and {graph['metadata']['total_edges']} edges")
    print(f"Graph saved to: {os.path.join(docs_path, 'graph.json')}")
    print("Graph preview:")
    for node in graph["nodes"][:3]:  # Show first 3 nodes
        print(f"  - {node['title']} ({node['id']})")
    for edge in graph["edges"][:3]:  # Show first 3 edges
        print(f"  - {edge['source']} -> {edge['target']} ({edge['type']})")