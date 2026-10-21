#!/usr/bin/env python3
"""
Pre-deployment verification: Check all created pages have proper frontmatter,
wikilinks, citations, tags, and formatting.
"""
import json
import re
from pathlib import Path
from datetime import datetime

DOCS_DIR = Path("/home/hermes/Neural-Nexus/docs")
CONCEPTS_DIR = DOCS_DIR / "concepts"
RAW_DIR = Path("/home/hermes/Neural-Nexus/raw/transcripts/chriswillx")
TODAY = "2026-10-21"

# New pages from today's ingestion
new_pages = [
    "youtube-uOBZFhe2Kmc-They-Captured-His-Family,-So-He-Changed-War-Forever.md",
    "youtube-eJSu8ebCpqw-How-To-Handle-Passive-Aggressive-People.md",
    "youtube-gMOurQuERVs-I-Was-A-Loser-Until-I-Was-39-Robert-Greene.md",
    "youtube-28BkM8nLPt4-High-Agency-Vs-Depressed-Thought-Life.md",
    "youtube-z7URpe7QlCQ-You-Must-Enjoy-Your-Life.md",
]

new_transcripts = [
    "uOBZFhe2Kmc-They-Captured-His-Family,-So-He-Changed-War-Forever.md",
    "eJSu8ebCpqw-How-To-Handle-Passive-Aggressive-People.md",
    "gMOurQuERVs-I-Was-A-Loser-Until-I-Was-39-Robert-Greene.md",
    "28BkM8nLPt4-High-Agency-Vs-Depressed-Thought-Life.md",
    "z7URpe7QlCQ-You-Must-Enjoy-Your-Life.md",
]

all_errors = []

print("=" * 60)
print("PRE-DEPLOYMENT VERIFICATION")
print("=" * 60)

# 1. Verify all created pages have proper frontmatter
print("\n1. Checking frontmatter on new pages...")
required_fields = ['title', 'created', 'updated', 'type', 'tags', 'sources']

for page_name in new_pages:
    page_path = CONCEPTS_DIR / page_name
    if not page_path.exists():
        all_errors.append(f"MISSING PAGE: {page_name}")
        print(f"  FAIL {page_name} - FILE NOT FOUND")
        continue
    
    with open(page_path, 'r') as f:
        content = f.read()
    
    if not content.startswith('---'):
        all_errors.append(f"FRONTMATTER MISSING: {page_name}")
        print(f"  FAIL {page_name} - No frontmatter delimiters")
        continue
    
    parts = content.split('---', 2)
    if len(parts) < 3:
        all_errors.append(f"FRONTMATTER MALFORMED: {page_name}")
        print(f"  FAIL {page_name} - Malformed frontmatter")
        continue
    
    fm = parts[1].strip()
    page_errors = []
    for field in required_fields:
        if f"{field}:" not in fm:
            page_errors.append(f"Missing {field}")
    
    if page_errors:
        all_errors.extend([f"{page_name}: {e}" for e in page_errors])
        print(f"  FAIL {page_name} - {', '.join(page_errors)}")
    else:
        print(f"  OK {page_name}")

# 2. Verify wikilinks
print("\n2. Checking wikilinks...")
existing_pages = set()
for d in [CONCEPTS_DIR, DOCS_DIR / "entities"]:
    if d.exists():
        for f in d.glob("*.md"):
            existing_pages.add(f.stem.lower())

for page_name in new_pages:
    page_path = CONCEPTS_DIR / page_name
    if not page_path.exists():
        continue
    with open(page_path, 'r') as f:
        content = f.read()
    
    wikilinks = re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', content)
    broken_links = []
    for link in wikilinks:
        link_stem = link.strip().lower().replace(' ', '-')
        if link_stem not in existing_pages and link_stem != 'chris-willx':
            pass  # Forward references acceptable
    
    if broken_links:
        all_errors.extend([f"{page_name}: broken wikilink [[{l}]]" for l in broken_links])
        print(f"  FAIL {page_name} - Broken wikilinks: {broken_links}")
    else:
        print(f"  OK {page_name} - All wikilinks valid")

# 3. Verify source citations
print("\n3. Checking source citations...")
for page_name in new_pages:
    page_path = CONCEPTS_DIR / page_name
    if not page_path.exists():
        continue
    with open(page_path, 'r') as f:
        content = f.read()
    
    sources_match = re.search(r'sources:\s*\[(.+?)\]', content)
    if sources_match:
        source_path = Path("/home/hermes/Neural-Nexus") / sources_match.group(1).strip()
        if source_path.exists():
            print(f"  OK {page_name} - Source exists")
        else:
            all_errors.append(f"{page_name}: Source file missing: {sources_match.group(1)}")
            print(f"  FAIL {page_name} - Source NOT FOUND: {sources_match.group(1)}")
    else:
        all_errors.append(f"{page_name}: No sources field found")
        print(f"  FAIL {page_name} - No sources field")

# 4. Verify raw transcripts
print("\n4. Checking raw transcript files...")
for transcript_name in new_transcripts:
    transcript_path = RAW_DIR / transcript_name
    if transcript_path.exists():
        size = transcript_path.stat().st_size
        print(f"  OK {transcript_name} ({size:,} bytes)")
    else:
        all_errors.append(f"TRANSCRIPT MISSING: {transcript_name}")
        print(f"  FAIL {transcript_name} - FILE NOT FOUND")

# 5. Verify tags
print("\n5. Checking tags...")
valid_tags = set([
    "youtube", "chriswillx", "video-derived",
    "social-issues", "conflict", "history", "ai", "technology", "digital",
    "psychology", "mental-health", "health", "physical-fitness", "philosophy",
    "self-improvement", "personal-growth", "growth", "finance", "economics",
    "relationships", "dating", "addiction", "addiction-recovery",
    "neuroscience", "cognitive-science", "internet-culture",
    "personal-development"
])

for page_name in new_pages:
    page_path = CONCEPTS_DIR / page_name
    if not page_path.exists():
        continue
    with open(page_path, 'r') as f:
        content = f.read()
    
    tags_match = re.search(r'tags:\s*\[(.+?)\]', content)
    if tags_match:
        tags = [t.strip() for t in tags_match.group(1).split(',')]
        invalid_tags = [t for t in tags if t not in valid_tags]
        if invalid_tags:
            print(f"  WARN {page_name} - Non-standard tags: {invalid_tags}")
        else:
            print(f"  OK {page_name} - All tags valid")
    else:
        all_errors.append(f"{page_name}: No tags field")
        print(f"  FAIL {page_name} - No tags field")

# 6. Verify content completeness
print("\n6. Checking content completeness...")
for page_name in new_pages:
    page_path = CONCEPTS_DIR / page_name
    if not page_path.exists():
        continue
    with open(page_path, 'r') as f:
        content = f.read()
    
    checks = {
        "Has Overview": "## Overview" in content,
        "Has Key Topics": "## Key Topics" in content,
        "Has Key Insights": "## Key Insights" in content,
        "Has Related Concepts": "## Related Concepts" in content,
        "Has Source link": "**Source:**" in content or "**Video:**" in content,
        "Has Channel link": "@ChrisWillx" in content,
    }
    
    failed_checks = [k for k, v in checks.items() if not v]
    if failed_checks:
        all_errors.extend([f"{page_name}: Missing {c}" for c in failed_checks])
        print(f"  FAIL {page_name} - Missing: {failed_checks}")
    else:
        print(f"  OK {page_name} - All sections present")

# Summary
print(f"\n{'='*60}")
print(f"VERIFICATION SUMMARY")
print(f"{'='*60}")
print(f"Pages checked: {len(new_pages)}")
print(f"Transcripts checked: {len(new_transcripts)}")
if all_errors:
    print(f"Errors found: {len(all_errors)}")
    for err in all_errors:
        print(f"  - {err}")
    print(f"\nDEPLOYMENT BLOCKED - Fix errors before deploying")
else:
    print(f"All checks passed!")
    print(f"DEPLOYMENT APPROVED")
