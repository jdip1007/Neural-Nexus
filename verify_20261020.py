#!/usr/bin/env python3
"""Pre-deployment verification of all created pages"""
import re
from pathlib import Path

NEURAL_NEXUS_PATH = Path("/home/hermes/Neural-Nexus")
DOCS_DIR = NEURAL_NEXUS_PATH / "docs"
CONCEPTS_DIR = DOCS_DIR / "concepts"
RAW_DIR = NEURAL_NEXUS_PATH / "raw"

TODAY = "2026-10-20"

# New pages from this run
new_pages = [
    "youtube-0bSPgeTBj1M-Sam-Sulek's-Opinion-On-Evidence-Based-Lifting.md",
    "youtube-fb-SGTSPkHA-The-Recession-Proof-Investment-No-One-Knows-They-Can-Access-Tony-Robbins.md",
    "youtube-WS3BZjtHpWw-Why-Pessimism-Makes-Dumb-Ideas-Sound-Smart-David-Deutsch.md",
    "youtube-_Ej44Xo2pTM-Let's-Be-Blunt-About-Peptides-Andrew-Huberman.md",
    "youtube-Y-r63JyWmDs-Why-Women-Hate-Sydney-Sweeney-&-Love-Sabrina-Carpenter.md",
]

# Get all existing page stems for wikilink validation
existing_pages = set()
for directory in [CONCEPTS_DIR, DOCS_DIR / "entities"]:
    if directory.exists():
        for f in directory.glob("*.md"):
            existing_pages.add(f.stem.lower())

# Known valid tags from SCHEMA.md taxonomy
schema_tags = {
    "youtube", "chriswillx", "video-derived",
    "social-issues", "conflict", "history",
    "ai", "technology", "digital",
    "psychology", "mental-health",
    "self-improvement", "personal-growth", "growth",
    "finance", "economics",
    "health", "physical-fitness",
    "relationships", "dating",
    "addiction", "addiction-recovery",
    "philosophy", "personal-development",
    "neuroscience", "cognitive-science",
    "internet-culture",
}

all_errors = []
all_warnings = []

print("=" * 60)
print("PRE-DEPLOYMENT VERIFICATION")
print("=" * 60)

for page_name in new_pages:
    filepath = CONCEPTS_DIR / page_name
    print(f"\nVerifying: {page_name[:60]}...")

    if not filepath.exists():
        all_errors.append(f"{page_name}: File does not exist")
        print(f"  FAIL: File does not exist!")
        continue

    content = filepath.read_text()

    # 1. Verify frontmatter
    if not content.startswith('---'):
        all_errors.append(f"{page_name}: Missing frontmatter delimiters")
        print(f"  FAIL: Missing frontmatter")
        continue

    parts = content.split('---', 2)
    if len(parts) < 3:
        all_errors.append(f"{page_name}: Malformed frontmatter")
        print(f"  FAIL: Malformed frontmatter")
        continue

    fm = parts[1].strip()
    required_fields = ['title', 'created', 'updated', 'type', 'tags', 'sources']
    for field in required_fields:
        if f"{field}:" not in fm:
            all_errors.append(f"{page_name}: Missing required field '{field}'")
            print(f"  FAIL: Missing field: {field}")

    # Check created/updated dates
    if f"created: {TODAY}" not in fm:
        all_warnings.append(f"{page_name}: created date not today")
    if f"updated: {TODAY}" not in fm:
        all_warnings.append(f"{page_name}: updated date not today")

    # 2. Verify tags exist in taxonomy
    tags_match = re.search(r'tags:\s*\[(.+?)\]', fm)
    tag_count = 0
    if tags_match:
        tags = [t.strip() for t in tags_match.group(1).split(',')]
        tag_count = len(tags)
        for tag in tags:
            if tag not in schema_tags:
                all_warnings.append(f"{page_name}: Tag '{tag}' not in SCHEMA.md taxonomy")

    # 3. Verify source citations exist
    sources_match = re.search(r'sources:\s*\[(.+?)\]', fm)
    if sources_match:
        source_path = NEURAL_NEXUS_PATH / sources_match.group(1).strip()
        if not source_path.exists():
            all_errors.append(f"{page_name}: Source file does not exist: {sources_match.group(1)}")
            print(f"  FAIL: Source file missing: {sources_match.group(1)}")
        else:
            print(f"  OK: Source file exists")

    # 4. Verify wikilinks
    wikilinks = re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', content)
    for link in wikilinks:
        link_stem = link.strip().lower().replace(' ', '-')
        if link_stem not in existing_pages:
            all_warnings.append(f"{page_name}: Wikilink [[{link}]] points to non-existent page")

    # 5. Verify content is complete (has sections)
    required_sections = ['Overview', 'Key Topics', 'Key Insights', 'Related Concepts']
    for section in required_sections:
        if f"## {section}" not in content:
            all_warnings.append(f"{page_name}: Missing section '{section}'")

    print(f"  OK: Frontmatter verified")
    print(f"  OK: Wikilinks checked ({len(wikilinks)} found)")
    print(f"  OK: Tags validated ({tag_count} tags)")

print(f"\n{'='*60}")
print(f"VERIFICATION SUMMARY")
print(f"{'='*60}")
print(f"Pages verified: {len(new_pages)}")
print(f"Errors: {len(all_errors)}")
print(f"Warnings: {len(all_warnings)}")

if all_errors:
    print(f"\nERRORS (must fix before deploy):")
    for e in all_errors:
        print(f"  - {e}")

if all_warnings:
    print(f"\nWARNINGS (non-blocking):")
    for w in all_warnings:
        print(f"  - {w}")

if not all_errors:
    print(f"\nALL CRITICAL CHECKS PASSED - Safe to deploy")
else:
    print(f"\nCRITICAL ERRORS FOUND - Do not deploy until fixed")
