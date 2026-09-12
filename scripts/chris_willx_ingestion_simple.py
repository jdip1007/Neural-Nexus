#!/usr/bin/env python3
"""
Chris Willx YouTube Ingestion Script - Simplified Version
Creates placeholder pages when transcripts are not available
"""

import json
import random
import os
from datetime import datetime
import hashlib

# Environment variables
NEURAL_NEXUS_PATH = os.getenv('NEURAL_NEXUS_PATH')

# Load video tracker
def load_video_tracker():
    try:
        with open('./video_tracker.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"processed_videos": [], "last_updated": datetime.now().isoformat()}

# Save video tracker
def save_video_tracker(tracker):
    with open('./video_tracker.json', 'w') as f:
        json.dump(tracker, f, indent=2)

# Load extracted videos
def load_extracted_videos():
    try:
        with open('./chris_willx_videos.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"videos": [], "channel": "ChrisWillx", "extracted_at": datetime.now().isoformat()}

# Check if video already processed
def is_video_processed(video_id, tracker):
    return any(video['id'] == video_id for video in tracker['processed_videos'])

# Get unprocessed videos
def get_unprocessed_videos(extracted_videos, tracker):
    unprocessed = []
    for video in extracted_videos['videos']:
        if not is_video_processed(video['id'], tracker):
            unprocessed.append(video)
    return unprocessed

# Randomly select videos
def select_random_videos(unprocessed_videos, max_count=5):
    if len(unprocessed_videos) <= max_count:
        return unprocessed_videos
    return random.sample(unprocessed_videos, max_count)

# Generate content hash for duplicate prevention
def generate_content_hash(content):
    return hashlib.sha256(content.encode()).hexdigest()

# Create Neural Nexus page without transcript
def create_neural_nexus_page(video, tracker):
    video_id = video['id']
    title = video['title']
    url = video['url']
    
    # Generate page filename
    safe_title = title.lower().replace(' ', '-').replace('"', '').replace("'", '').replace('---', '-').replace(':', '-')
    page_filename = f"youtube-{video_id}-{safe_title}.md"
    page_path = f"{NEURAL_NEXUS_PATH}/{page_filename}"
    
    # Create frontmatter
    frontmatter = {
        "title": title,
        "created": datetime.now().strftime("%Y-%m-%d"),
        "updated": datetime.now().strftime("%Y-%m-%d"),
        "type": "reading",
        "classification": get_classification(title),
        "domain": "psychology",
        "tags": ["youtube", "chris-willx", "podcast", "video-summary"],
        "sources": [f"raw/youtube-{video_id}-placeholder.json"],
        "confidence": "low",
        "status": "active",
        "reviewed": datetime.now().strftime("%Y-%m-%d"),
        "backlinks": []
    }
    
    # Add domain-specific tags
    if "ai" in title.lower() or "technology" in title.lower():
        frontmatter["tags"].extend(["ai", "artificial-intelligence", "technology"])
    if "debate" in title.lower():
        frontmatter["tags"].extend(["discussion", "debate"])
    elif "diet" in title.lower():
        frontmatter["tags"].extend(["health", "nutrition", "science"])
    elif "science" in title.lower():
        frontmatter["tags"].extend(["science", "research"])
    elif "attack" in title.lower() or "terrify" in title.lower():
        frontmatter["tags"].extend(["security", "technology", "ai-safety"])
    elif "revolution" in title.lower():
        frontmatter["tags"].extend(["philosophy", "current-events"])
    elif "mind" in title.lower() or "racing" in title.lower():
        frontmatter["tags"].extend(["psychology", "mental-health", "self-improvement"])
    elif "marriage" in title.lower() or "sex" in title.lower():
        frontmatter["tags"].extend(["relationships", "psychology"])
    elif "hunter biden" in title.lower():
        frontmatter["tags"].extend(["current-events", "politics", "media"])
        frontmatter["classification"] = "psychology.media-ethics"
    
    # Create placeholder content
    page_content = f"""---
{json.dumps(frontmatter, indent=2)}
---

# {title}

## Video Information

- **Channel**: Chris Williamson (@ChrisWillx)
- **Duration**: {video.get('duration', 'Unknown')}
- **URL**: [{url}]({url})
- **Video ID**: {video_id}
- **Processed**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
- **Status**: Placeholder - Transcript not available

## Overview

This video is part of Chris Williamson's podcast series. Due to transcript API limitations, this page serves as a placeholder with basic video information and categorization.

## Content Analysis

*Note: Full transcript analysis requires transcript access. This page will be updated when transcripts become available.*

## Key Topics (Based on Title)

Based on the video title, this discussion likely covers:

{get_topic_analysis(title)}

## Related Pages

- [[chris-williamson-podcast|Chris Williamson Podcast Overview]]
- [[podcast-analysis|Podcast Content Analysis]]
- {get_related_pages(title)}

## Sources

^{f"raw/youtube-{video_id}-placeholder.json"}
"""
    
    # Write page file
    with open(page_path, 'w') as f:
        f.write(page_content)
    
    # Create placeholder raw file
    placeholder_content = {
        "video_id": video_id,
        "video_url": url,
        "title": title,
        "status": "placeholder",
        "reason": "Transcript API not accessible",
        "created_at": datetime.now().isoformat(),
        "page_filename": page_filename
    }
    
    os.makedirs('./raw', exist_ok=True)
    with open(f'./raw/youtube-{video_id}-placeholder.json', 'w') as f:
        json.dump(placeholder_content, f, indent=2)
    
    # Update video tracker
    tracker['processed_videos'].append({
        "id": video_id,
        "title": title,
        "url": url,
        "processed_at": datetime.now().isoformat(),
        "page_filename": page_filename,
        "content_hash": generate_content_hash(page_content),
        "status": "placeholder"
    })
    
    return page_filename

# Get classification based on title
def get_classification(title):
    title_lower = title.lower()
    
    if "ai" in title_lower or "technology" in title_lower:
        return "psychology.media-ethics"
    elif "diet" in title_lower or "health" in title_lower:
        return "psychology.mental-health"
    elif "science" in title_lower:
        return "psychology.mental-health"
    elif "marriage" in title_lower or "sex" in title_lower:
        return "psychology.relationships"
    elif "hunter biden" in title_lower:
        return "psychology.media-ethics"
    elif "mind" in title_lower or "racing" in title_lower:
        return "psychology.personal-development"
    elif "revolution" in title_lower:
        return "psychology.personal-development"
    else:
        return "psychology.personal-development"

# Get topic analysis based on title
def get_topic_analysis(title):
    title_lower = title.lower()
    topics = []
    
    if "ai" in title_lower or "technology" in title_lower:
        topics.extend([
            "- **Artificial Intelligence**: Discussion about AI development and implications",
            "- **Technology**: Analysis of current technological trends and future predictions",
            "- **Debate**: Multiple perspectives on AI's role in society"
        ])
    elif "diet" in title_lower or "health" in title_lower:
        topics.extend([
            "- **Nutrition**: Scientific analysis of dietary approaches",
            "- **Health**: Medical perspectives on diet and wellness",
            "- **Research**: Harvard professor's findings and expertise"
        ])
    elif "science" in title_lower:
        topics.extend([
            "- **Research**: Scientific methodology and findings",
            "- **Analysis**: Critical examination of scientific claims",
            "- **Blue Zones**: Investigation of longevity research"
        ])
    elif "marriage" in title_lower or "sex" in title_lower:
        topics.extend([
            "- **Relationships**: Dynamic between marriage and intimacy",
            "- **Psychology**: Behavioral patterns in long-term relationships",
            "- **Gender Studies**: Different perspectives on relationship dynamics"
        ])
    elif "hunter biden" in title_lower:
        topics.extend([
            "- **Current Events**: Political and media coverage",
            "- **Ethics**: Media responsibility and public figures",
            "- **Legal**: Legal proceedings and public scrutiny"
        ])
    elif "mind" in title_lower or "racing" in title_lower:
        topics.extend([
            "- **Mental Health**: Managing anxious thoughts",
            "- **Self-Help**: Practical strategies for mental well-being",
            "- **Comedy**: Jimmy Carr's perspective on modern life"
        ])
    elif "revolution" in title_lower:
        topics.extend([
            "- **Current Events**: Analysis of societal changes",
            "- **Philosophy**: Discussion about revolution and progress",
            "- **Comedy**: Jimmy Carr's comedic take on modern times"
        ])
    elif "attack" in title_lower or "terrify" in title_lower:
        topics.extend([
            "- **Security**: AI safety and security concerns",
            "- **Technology**: Hugging Face and AI platforms",
            "- **Risk Assessment**: Potential threats and mitigation"
        ])
    else:
        topics.extend([
            "- **General Discussion**: Broad conversation covering multiple topics",
            "- **Podcast Format**: Typical Chris Williamson interview style",
            "- **Guest Analysis**: Featured guest's expertise and perspective"
        ])
    
    return "\n".join(topics)

# Get related pages
def get_related_pages(title):
    title_lower = title.lower()
    
    if "ai" in title_lower or "technology" in title_lower:
        return "[[ai-safety|AI Safety]]\n[[technology-ethics|Technology Ethics]]"
    elif "diet" in title_lower or "health" in title_lower:
        return "[[health-psychology|Health Psychology]]\n[[nutrition-science|Nutrition Science]]"
    elif "science" in title_lower:
        return "[[scientific-method|Scientific Method]]\n[[research-methodology|Research Methodology]]"
    elif "marriage" in title_lower or "sex" in title_lower:
        return "[[relationship-dynamics|Relationship Dynamics]]\n[[gender-psychology|Gender Psychology]]"
    elif "hunter biden" in title_lower:
        return "[[media-ethics|Media Ethics]]\n[[public-figures|Public Figures]]"
    elif "mind" in title_lower or "racing" in title_lower:
        return "[[anxiety-management|Anxiety Management]]\n[[mental-wellness|Mental Wellness]]"
    elif "revolution" in title_lower:
        return "[[social-change|Social Change]]\n[[philosophy-of-progress|Philosophy of Progress]]"
    else:
        return "[[podcast-content-analysis|Podcast Content Analysis]]\n[[interview-techniques|Interview Techniques]]"

# Main ingestion workflow
def main():
    print("Starting Chris Willx YouTube ingestion workflow (simplified)...")
    
    # Load data
    tracker = load_video_tracker()
    extracted_videos = load_extracted_videos()
    
    print(f"Found {len(extracted_videos['videos'])} videos from Chris Willx channel")
    print(f"Already processed {len(tracker['processed_videos'])} videos")
    
    # Get unprocessed videos
    unprocessed_videos = get_unprocessed_videos(extracted_videos, tracker)
    print(f"Found {len(unprocessed_videos)} unprocessed videos")
    
    if not unprocessed_videos:
        print("No new videos to process. All videos have been processed.")
        return
    
    # Randomly select videos
    selected_videos = select_random_videos(unprocessed_videos, max_count=5)
    print(f"Selected {len(selected_videos)} videos for processing:")
    
    for video in selected_videos:
        duration = video.get('duration', 'Unknown')
        print(f"  - {video['title']} ({duration})")
    
    # Process each selected video
    processed_count = 0
    for video in selected_videos:
        print(f"\nProcessing video: {video['title']}")
        
        try:
            # Create Neural Nexus page (placeholder)
            print("  Creating placeholder Neural Nexus page...")
            page_filename = create_neural_nexus_page(video, tracker)
            
            print(f"  ✓ Successfully created page: {page_filename}")
            processed_count += 1
            
        except Exception as e:
            print(f"  ✗ Error processing video {video['id']}: {e}")
            continue
    
    # Save updated tracker
    save_video_tracker(tracker)
    
    # Update last_updated timestamp
    tracker['last_updated'] = datetime.now().isoformat()
    save_video_tracker(tracker)
    
    print(f"\nIngestion complete!")
    print(f"Created {processed_count} placeholder pages out of {len(selected_videos)} selected videos")
    print(f"Total videos processed: {len(tracker['processed_videos'])}")
    print(f"Note: These are placeholder pages due to transcript API limitations")

if __name__ == "__main__":
    main()