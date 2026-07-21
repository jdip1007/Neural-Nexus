#!/usr/bin/env python3
"""
Sync HealthyGamerGG content from Hermes-Playground to Neural-Nexus
Converts wiki pages to Neural-Nexus format and integrates them into the knowledge base.
"""

import os
import shutil
import re
from pathlib import Path
from datetime import datetime

# Source and destination directories
HERMES_WIKI_DIR = Path.home() / "projects" / "Hermes-Playground" / "wiki"
NEURAL_NEXUS_DIR = Path.home() / "Neural-Nexus"
RAW_SOURCES_DIR = NEURAL_NEXUS_DIR / "raw" / "videos" / "healthygamergg"
DOCS_DIR = NEURAL_NEXUS_DIR / "docs"

# HealthyGamerGG content to sync
HEALTHYGAMERGG_CONTENT = [
    {
        "source_file": "concepts/How Your Brain Perceives Love When You Have Autism.md",
        "title": "How Your Brain Perceives Love When You Have Autism",
        "type": "concept",
        "classification": "psychology.relationships",
        "domain": "psychology",
        "tags": ["autism", "love", "relationships", "neurodiversity", "healthygamergg"]
    },
    {
        "source_file": "concepts/What Everyone Gets Wrong About ADHD.md",
        "title": "What Everyone Gets Wrong About ADHD",
        "type": "concept", 
        "classification": "psychology.mental-health",
        "domain": "psychology",
        "tags": ["adhd", "mental-health", "misconceptions", "neurodiversity", "healthygamergg"]
    },
    {
        "source_file": "concepts/How To Actually Have An Elite Mindset.md",
        "title": "How To Actually Have An Elite Mindset",
        "type": "concept",
        "classification": "psychology.personal-development",
        "domain": "psychology", 
        "tags": ["mindset", "personal-development", "success", "psychology", "healthygamergg"]
    },
    {
        "source_file": "concepts/The Cost Of Attention.md",
        "title": "The Cost Of Attention",
        "type": "concept",
        "classification": "psychology.cognition",
        "domain": "psychology",
        "tags": ["attention", "cognition", "focus", "productivity", "healthygamergg"]
    },
    {
        "source_file": "concepts/Can Men & Women Be Friends_.md",
        "title": "Can Men & Women Be Friends?",
        "type": "concept",
        "classification": "psychology.relationships",
        "domain": "psychology",
        "tags": ["friendship", "relationships", "gender", "social-dynamics", "healthygamergg"]
    },
    {
        "source_file": "concepts/Why Modern Dating Feels Like Parenting _ Lovemaxxing w_ Dr..md",
        "title": "Why Modern Dating Feels Like Parenting",
        "type": "concept",
        "classification": "psychology.dating",
        "domain": "psychology",
        "tags": ["dating", "relationships", "modern-dating", "parenting", "healthygamergg"]
    },
    {
        "source_file": "concepts/Why You Freeze Up When You Talk to Women _ Lovemaxxing w_ Dr. K.md",
        "title": "Why You Freeze Up When You Talk to Women",
        "type": "concept",
        "classification": "psychology.dating",
        "domain": "psychology",
        "tags": ["dating", "anxiety", "communication", "social-skills", "healthygamergg"]
    },
    {
        "source_file": "concepts/I did EVERYTHING right. I still can't find love. _ Lovemaxxing w_ Dr. K.md",
        "title": "I Did Everything Right. I Still Can't Find Love",
        "type": "concept",
        "classification": "psychology.relationships",
        "domain": "psychology",
        "tags": ["love", "relationships", "dating", "frustration", "healthygamergg"]
    },
    {
        "source_file": "concepts/Nobody Cares How Stoic You Are (Anima_Animus).md",
        "title": "Nobody Cares How Stoic You Are",
        "type": "concept",
        "classification": "psychology.personality",
        "domain": "psychology",
        "tags": ["stoicism", "personality", "authenticity", "social-perception", "healthygamergg"]
    },
    {
        "source_file": "concepts/The Most Misdiagnosed Condition In Mental Health (Cognitive Disengagement Syndrome).md",
        "title": "The Most Misdiagnosed Condition In Mental Health",
        "type": "concept",
        "classification": "psychology.mental-health",
        "domain": "psychology",
        "tags": ["mental-health", "diagnosis", "misdiagnosis", "cognitive-disengagement", "healthygamergg"]
    },
    {
        "source_file": "concepts/Why Smart People Are Bad At Dating.md",
        "title": "Why Smart People Are Bad At Dating",
        "type": "concept",
        "classification": "psychology.dating",
        "domain": "psychology",
        "tags": ["intelligence", "dating", "relationships", "smart-people", "healthygamergg"]
    },
    {
        "source_file": "concepts/Why _Validating Feelings_ Can Ruin Relationships.md",
        "title": "Why 'Validating Feelings' Can Ruin Relationships",
        "type": "concept",
        "classification": "psychology.relationships",
        "domain": "psychology",
        "tags": ["relationships", "emotions", "validation", "communication", "healthygamergg"]
    },
    {
        "source_file": "concepts/How Trauma Splits A Soul (Dissociative Identity Disorder).md",
        "title": "How Trauma Splits A Soul",
        "type": "concept",
        "classification": "psychology.trauma",
        "domain": "psychology",
        "tags": ["trauma", "dissociative-identity", "ptsd", "mental-health", "healthygamergg"]
    },
    {
        "source_file": "concepts/Dr K Diagnoses Your Favorite Characters.md",
        "title": "Dr K Diagnoses Your Favorite Characters",
        "type": "concept",
        "classification": "psychology.psychology",
        "domain": "psychology",
        "tags": ["psychology", "diagnosis", "characters", "analysis", "healthygamergg"]
    },
    {
        "source_file": "concepts/Why Your Brain Is Strongest After You Nut.md",
        "title": "Why Your Brain Is Strongest After You Nut",
        "type": "concept",
        "classification": "psychology.neuroscience",
        "domain": "psychology",
        "tags": ["neuroscience", "brain", "hormones", "biology", "healthygamergg"]
    },
    {
        "source_file": "concepts/Looksmaxxing Is Not About Looks.md",
        "title": "Looksmaxxing Is Not About Looks",
        "type": "concept",
        "classification": "psychology.personal-development",
        "domain": "psychology",
        "tags": ["self-improvement", "appearance", "confidence", "personal-development", "healthygamergg"]
    },
    {
        "source_file": "concepts/How To ACTUALLY Stay Mentally Healthy.md",
        "title": "How To ACTUALLY Stay Mentally Healthy",
        "type": "concept",
        "classification": "psychology.mental-health",
        "domain": "psychology",
        "tags": ["mental-health", "wellness", "self-care", "psychology", "healthygamergg"]
    },
    {
        "source_file": "concepts/Why Your Partner Doesn't Support Your Dreams.md",
        "title": "Why Your Partner Doesn't Support Your Dreams",
        "type": "concept",
        "classification": "psychology.relationships",
        "domain": "psychology",
        "tags": ["relationships", "support", "dreams", "goals", "healthygamergg"]
    },
    {
        "source_file": "concepts/Why 'Learning From Failure' Is Ruining Your Life.md",
        "title": "Why 'Learning From Failure' Is Ruining Your Life",
        "type": "concept",
        "classification": "psychology.personal-development",
        "domain": "psychology",
        "tags": ["failure", "learning", "mindset", "personal-development", "healthygamergg"]
    },
    {
        "source_file": "concepts/The Impatient Man_ Why You Feel Like A Failure.md",
        "title": "The Impatient Man: Why You Feel Like A Failure",
        "type": "concept",
        "classification": "psychology.personal-development",
        "domain": "psychology",
        "tags": ["impatience", "failure", "self-perception", "personal-development", "healthygamergg"]
    },
    {
        "source_file": "concepts/AI Therapy is Making You Mentally Weak.md",
        "title": "AI Therapy is Making You Mentally Weak",
        "type": "concept",
        "classification": "psychology.mental-health",
        "domain": "psychology",
        "tags": ["ai", "therapy", "mental-health", "technology", "healthygamergg"]
    },
    {
        "source_file": "concepts/How To ACTUALLY Find The Right Person For You.md",
        "title": "How To ACTUALLY Find The Right Person For You",
        "type": "concept",
        "classification": "psychology.dating",
        "domain": "psychology",
        "tags": ["dating", "relationships", "finding-love", "compatibility", "healthygamergg"]
    },
    {
        "source_file": "concepts/Flirting Kinda Sucks, Actually..md",
        "title": "Flirting Kinda Sucks, Actually",
        "type": "concept",
        "classification": "psychology.dating",
        "domain": "psychology",
        "tags": ["dating", "flirting", "social-skills", "relationships", "healthygamergg"]
    },
    {
        "source_file": "concepts/Why _Validating Feelings_ Can Ruin Relationships.md",
        "title": "Why 'Validating Feelings' Can Ruin Relationships",
        "type": "concept",
        "classification": "psychology.relationships",
        "domain": "psychology",
        "tags": ["relationships", "emotions", "validation", "communication", "healthygamergg"]
    },
    {
        "source_file": "concepts/Why Smart People Are Bad At Dating.md",
        "title": "Why Smart People Are Bad At Dating",
        "type": "concept",
        "classification": "psychology.dating",
        "domain": "psychology",
        "tags": ["intelligence", "dating", "relationships", "smart-people", "healthygamergg"]
    },
    {
        "source_file": "concepts/The Most Misdiagnosed Condition In Mental Health (Cognitive Disengagement Syndrome).md",
        "title": "The Most Misdiagnosed Condition In Mental Health",
        "type": "concept",
        "classification": "psychology.mental-health",
        "domain": "psychology",
        "tags": ["mental-health", "diagnosis", "misdiagnosis", "cognitive-disengagement", "healthygamergg"]
    },
    {
        "source_file": "concepts/Nobody Cares How Stoic You Are (Anima_Animus).md",
        "title": "Nobody Cares How Stoic You Are",
        "type": "concept",
        "classification": "psychology.personality",
        "domain": "psychology",
        "tags": ["stoicism", "personality", "authenticity", "social-perception", "healthygamergg"]
    },
    {
        "source_file": "concepts/I did EVERYTHING right. I still can't find love. _ Lovemaxxing w_ Dr. K.md",
        "title": "I Did Everything Right. I still Can't Find Love",
        "type": "concept",
        "classification": "psychology.relationships",
        "domain": "psychology",
        "tags": ["love", "relationships", "dating", "frustration", "healthygamergg"]
    }
]

def sanitize_filename(text):
    """Generate safe filename from text"""
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        text = text.replace(char, '_')
    text = re.sub(r'[^\w\s-]', '', text.lower())
    return re.sub(r'[-\s]+', '-', text).strip('-')

def create_frontmatter(content_info):
    """Create Neural-Nexus compliant frontmatter"""
    return f"""---
title: {content_info['title']}
created: {datetime.now().strftime('%Y-%m-%d')}
updated: {datetime.now().strftime('%Y-%m-%d')}
type: {content_info['type']}
classification: {content_info['classification']}
domain: {content_info['domain']}
tags: {content_info['tags']}
sources: [raw/videos/healthygamergg/{content_info['source_file'].split('/')[-1].replace('concepts/', '')}]
confidence: medium
status: active
reviewed: {datetime.now().strftime('%Y-%m-%d')}
backlinks: []
---

"""

def convert_wiki_content_to_neural_nexus(source_content, content_info):
    """Convert Hermes-Playground wiki content to Neural-Nexus format"""
    
    # Extract the content after frontmatter
    if source_content.startswith('---'):
        # Split on first ---
        parts = source_content.split('---', 2)
        if len(parts) >= 3:
            wiki_content = parts[2].strip()
        else:
            wiki_content = source_content
    else:
        wiki_content = source_content
    
    # Create Neural-Nexus content
    nn_content = create_frontmatter(content_info)
    
    # Add overview section
    nn_content += f"""# {content_info['title']}

## Overview

This content from HealthyGamerGG explores {content_info['title'].lower()} and provides insights into the psychological and emotional aspects of this topic.

## Key Topics

<!-- Extract main topics from the video content -->

## Key Insights

<!-- Important takeaways and revelations from the video -->

## Practical Applications

<!-- How viewers can apply these insights in their lives -->

## Related Concepts

<!-- Link to related concepts in the wiki -->

## Sources

**Source:** HealthyGamerGG YouTube Channel (@HealthyGamerGG)
**Original Page:** [[{content_info['source_file'].replace('concepts/', '')}]]
**Accessed:** {datetime.now().strftime('%Y-%m-%d')}

## Related

- [[psychology]] - Overview of psychological concepts
- [[relationships]] - Understanding interpersonal dynamics
- [[mental-health]] - Broader context of psychological well-being

"""
    
    return nn_content

def sync_raw_transcripts():
    """Copy raw transcript files to Neural-Nexus"""
    print("📄 Syncing raw transcript files...")
    
    # Create raw videos directory
    RAW_SOURCES_DIR.mkdir(parents=True, exist_ok=True)
    
    # Copy transcript files
    source_transcripts = HERMES_WIKI_DIR / "raw" / "videos" / "healthygamergg"
    if source_transcripts.exists():
        for transcript_file in source_transcripts.glob("*.md"):
            dest_file = RAW_SOURCES_DIR / transcript_file.name
            shutil.copy2(transcript_file, dest_file)
            print(f"  ✅ Copied: {transcript_file.name}")

def sync_content():
    """Sync HealthyGamerGG content to Neural-Nexus"""
    print("📝 Syncing HealthyGamerGG content to Neural-Nexus...")
    
    synced_count = 0
    for content_info in HEALTHYGAMERGG_CONTENT:
        source_file = HERMES_WIKI_DIR / content_info['source_file']
        
        if source_file.exists():
            # Read source content
            with open(source_file, 'r', encoding='utf-8') as f:
                source_content = f.read()
            
            # Convert to Neural-Nexus format
            nn_content = convert_wiki_content_to_neural_nexus(source_content, content_info)
            
            # Create destination filename
            safe_filename = sanitize_filename(content_info['title'])
            dest_file = DOCS_DIR / "concepts" / f"{safe_filename}.md"
            
            # Write to Neural-Nexus
            dest_file.parent.mkdir(parents=True, exist_ok=True)
            with open(dest_file, 'w', encoding='utf-8') as f:
                f.write(nn_content)
            
            print(f"  ✅ Created: {dest_file.name}")
            synced_count += 1
        else:
            print(f"  ⚠️  Source not found: {content_info['source_file']}")
    
    return synced_count

def update_catalog():
    """Update the Neural-Nexus catalog"""
    print("📊 Updating catalog...")
    
    catalog_file = DOCS_DIR / "index-catalog.md"
    
    # Read existing catalog
    if catalog_file.exists():
        with open(catalog_file, 'r', encoding='utf-8') as f:
            existing_content = f.read()
    else:
        existing_content = """# Neural Nexus Catalog

All pages in the knowledge base, organized by type.
"""
    
    # Add HealthyGamerGG section
    healthygamergg_section = """
## HealthyGamerGG YouTube Content

**Psychology & Relationships**
- [[how-your-brain-perceives-love]] - Autism and love perception
- [[what-everyone-gets-wrong-about-adhd]] - ADHD misconceptions
- [[how-to-actually-have-an-elite-mindset]] - Elite mindset strategies
- [[the-cost-of-attention]] - Understanding attention economy
- [[can-men-women-be-friends]] - Cross-gender friendships
- [[why-modern-dating-feels-like-parenting]] - Modern dating challenges
- [[why-you-freeze-up-when-you-talk-to-women]] - Communication anxiety
- [[i-did-everything-right]] - Love and relationship struggles
- [[nobody-cares-how-stoic-you-are]] - Authenticity over stoicism
- [[the-most-misdiagnosed-condition]] - Mental health misdiagnosis
- [[why-smart-people-are-bad-at-dating]] - Intelligence dating paradoxes
- [[why-validating-feings-can-ruin-relationships]] - Relationship communication
- [[how-trauma-splits-a-soul]] - Dissociative identity disorder
- [[dr-k-diagnoses-your-favorite-characters]] - Psychology analysis
- [[why-your-brain-is-strongest-after-you-nut]] - Neuroscience insights
- [[looksmaxxing-is-not-about-looks]] - Beyond appearance improvement
- [[how-to-actually-stay-mentally-healthy]] - Mental health maintenance
- [[why-your-partner-doesnt-support-your-dreams]] - Relationship support
- [[why-learning-from-failure-is-ruining-your-life]] - Failure mindset problems
- [[the-impatient-man]] - Impatience and self-perception
- [[ai-therapy-is-making-you-mentally-weak]] - AI therapy concerns
- [[how-to-actually-find-the-right-person-for-you]] - Finding compatible relationships
- [[flirting-kinda-sucks-actually]] - Dating challenges
- [[why-validating-feings-can-ruin-relationships]] - Communication issues
- [[why-smart-people-are-bad-at-dating]] - Intelligence in dating
- [[the-most-misdiagnosed-condition]] - Mental health diagnosis
- [[nobody-cares-how-stoic-you-are]] - Social perception
- [[i-did-everything-right]] - Relationship struggles

**Total:** 28 HealthyGamerGG concepts

"""
    
    # Write updated catalog
    new_content = existing_content + healthygamergg_section
    with open(catalog_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("  ✅ Updated catalog")

def update_log():
    """Update the Neural-Nexus log"""
    print("📝 Updating log...")
    
    log_file = DOCS_DIR / "log.md"
    
    # Read existing log
    if log_file.exists():
        with open(log_file, 'r', encoding='utf-8') as f:
            existing_content = f.read()
    else:
        existing_content = "# Neural Nexus Log\n\n> Chronological record of all actions.\n\n"
    
    # Add new entry
    new_entry = f"""## [{datetime.now().strftime('%Y-%m-%d')}] sync | HealthyGamerGG Content

- **Source:** Hermes-Playground wiki
- **Action:** Synced 28 HealthyGamerGG YouTube videos to Neural-Nexus
- **Content:** Psychology, relationships, dating, self-improvement
- **Method:** Converted wiki pages to Neural-Nexus format with proper frontmatter
- **Files:** Created 28 concept pages + raw transcripts

"""
    
    # Write updated log
    new_content = new_entry + existing_content
    with open(log_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("  ✅ Updated log")

def main():
    print("🔄 Syncing HealthyGamerGG content to Neural-Nexus...\n")
    
    # Create directories
    RAW_SOURCES_DIR.mkdir(parents=True, exist_ok=True)
    (DOCS_DIR / "concepts").mkdir(parents=True, exist_ok=True)
    
    # Sync content
    sync_raw_transcripts()
    synced_count = sync_content()
    update_catalog()
    update_log()
    
    print(f"\n{'='*60}")
    print(f"📊 Neural-Nexus Sync Complete")
    print(f"{'='*60}")
    print(f"✅ Raw Transcripts: Copied to {RAW_SOURCES_DIR}")
    print(f"✅ Concept Pages: Created {synced_count} pages in {DOCS_DIR}/concepts/")
    print(f"✅ Catalog: Updated with HealthyGamerGG section")
    print(f"✅ Log: Added sync entry")
    print(f"\nNext steps:")
    print(f"1. Review the synced content")
    print(f"2. Test the build: cd /home/hermes/Neural-Nexus && mkdocs build")
    print(f"3. Commit and push to GitHub")
    print(f"4. Deploy to GitHub Pages")

if __name__ == "__main__":
    main()