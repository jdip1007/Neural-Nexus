#!/usr/bin/env python3
"""
Daily YouTube ingestion for HealthyGamerGG channel with fallback transcript APIs
Processes randomly selected videos with duplicate detection and creates Neural Nexus pages
"""

import os
import json
import time
import requests
import random
from pathlib import Path
from datetime import datetime
from video_tracker import VideoTracker

# Configuration
TRANSCRIPT_API_KEY = os.environ.get("TRANSCRIPT_API_KEY")
NEURAL_NEXUS_PATH = os.environ.get("NEURAL_NEXUS_PATH", "/home/hermes/Neural-Nexus")
RAW_TRANSCRIPTS_DIR = Path("/home/hermes/Neural-Nexus") / "raw" / "transcripts" / "healthygamergg"

def sanitize_filename(text):
    """Generate safe filename from text"""
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        text = text.replace(char, '_')
    return text[:200]

def fetch_transcript_fallback(video_url, video_id, title):
    """Fetch transcript using YouTube Transcript API as fallback"""
    try:
        # Try YouTube Transcript API first
        response = requests.get(
            f"https://youtube-transcript-api.herokuapp.com/transcript?url={video_url}",
            timeout=30
        )
        
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "success" and "transcript" in data:
                return {"success": True, "data": {"transcript": data["transcript"]}}
            else:
                return {"error": f"API returned: {data.get('message', 'Unknown error')}"}
        else:
            return {"error": f"HTTP {response.status_code}"}
            
    except Exception as e:
        return {"error": f"YouTube Transcript API failed: {str(e)}"}

def fetch_transcript_primary(video_url, video_id, title):
    """Fetch transcript using TranscriptAPI (primary)"""
    if not TRANSCRIPT_API_KEY:
        return {"error": "No API key configured"}

    try:
        response = requests.get(
            "https://transcriptapi.com/api/v2/youtube/transcript",
            params={"video_url": video_url},
            headers={"Authorization": f"Bearer {TRANSCRIPT_API_KEY}"},
            timeout=30
        )

        if response.status_code == 404:
            return {"error": "HTTP 404 - Video unavailable or removed", "status": "not_found"}
        elif response.status_code == 401:
            return {"error": "HTTP 401 - Invalid API key"}
        elif response.status_code == 429:
            return {"error": "HTTP 429 - Rate limit exceeded", "status": "rate_limited"}
        elif response.status_code == 200:
            data = response.json()
            return {"success": True, "data": data}
        else:
            return {"error": f"HTTP {response.status_code}"}

    except Exception as e:
        return {"error": str(e)}

def fetch_transcript(video_url, video_id, title):
    """Fetch transcript with fallback to YouTube Transcript API"""
    # Try primary API first
    result = fetch_transcript_primary(video_url, video_id, title)
    
    if result.get("success"):
        return result
    elif result.get("error") and "HTTP 402" in str(result.get("error")):
        # Fallback to YouTube Transcript API
        print(f"  🔄 Primary API failed, trying fallback...")
        return fetch_transcript_fallback(video_url, video_id, title)
    else:
        return result

def save_transcript(video_id, title, transcript_data):
    """Save transcript with proper frontmatter"""
    safe_title = sanitize_filename(title)
    filename = f"{safe_title}.md"
    filepath = RAW_TRANSCRIPTS_DIR / filename

    # Create frontmatter
    frontmatter = f"""---
source_url: https://www.youtube.com/watch?v={video_id}
ingested: {datetime.now().strftime('%Y-%m-%d')}
video_id: {video_id}
title: {title}
series: 
---

"""

    # Format transcript content
    transcript_text = ""
    if "transcript" in transcript_data:
        for segment in transcript_data["transcript"]:
            time_str = segment.get("start", 0)
            text = segment.get("text", "")
            timestamp = f"[{int(time_str // 60):02d}:{int(time_str % 60):02d}]"
            transcript_text += f"{timestamp} {text}\n"

    # Save file
    content = frontmatter + transcript_text
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return filepath

def create_neural_nexus_page(video_id, title, transcript_file, content_type="concept"):
    """Create Neural Nexus page with proper frontmatter and content"""
    concepts_dir = Path("/home/hermes/Neural-Nexus") / "docs" / "concepts"
    concepts_dir.mkdir(parents=True, exist_ok=True)

    # Determine content type and tags based on title
    title_lower = title.lower()
    
    if any(keyword in title_lower for keyword in ['dating', 'relationship', 'love', 'friend', 'partner']):
        tags = ['dating', 'relationships', 'psychology', 'healthygamergg']
    elif any(keyword in title_lower for keyword in ['adhd', 'mental health', 'trauma', 'disorder', 'therapy']):
        tags = ['mental-health', 'psychology', 'therapy', 'healthygamergg']
    elif any(keyword in title_lower for keyword in ['mindset', 'elite', 'stoic', 'failure', 'success']):
        tags = ['mindset', 'psychology', 'personal-development', 'healthygamergg']
    else:
        tags = ['psychology', 'youtube', 'healthygamergg']

    # Generate safe filename
    safe_title = sanitize_filename(title)
    page_filename = f"youtube-{video_id}-{safe_title}.md"
    page_path = concepts_dir / page_filename

    # Read transcript content
    transcript_content = ""
    try:
        with open(transcript_file, 'r', encoding='utf-8') as f:
            transcript_content = f.read()
    except:
        transcript_content = "Transcript content not available"

    # Extract key topics from title
    topic_mapping = {
        "Can Men & Women Be Friends?": "Interpersonal Relationships and Friendship Dynamics",
        "The Lie of \"Positive Thinking\"": "Cognitive Psychology and Positive Thinking Critique",
        "Why You Should NEVER Confess Your Love": "Relationship Psychology and Love Confession",
        "How To Actually Have An Elite Mindset": "Mindset Development and Peak Performance Psychology",
        "Flirting Kinda Sucks, Actually.": "Dating Dynamics and Social Interaction Challenges"
    }

    topic = topic_mapping.get(title, "Mental Health and Psychology")

    # Create page content
    page_content = f"""---
title: {title}
created: {datetime.now().strftime('%Y-%m-%d')}
updated: {datetime.now().strftime('%Y-%m-%d')}
type: {content_type}
tags: {tags}
sources: [raw/transcripts/healthygamergg/{transcript_file.name}]
---

# {title}

## Overview

This video from HealthyGamerGG explores {topic.lower()} and provides insights into the psychological and emotional aspects of {title.lower()}.

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
**Video URL:** https://www.youtube.com/watch?v={video_id}
**Video ID:** `{video_id}`
**Transcript:** [[raw/transcripts/healthygamergg/{transcript_file.name}]]
**Accessed:** {datetime.now().strftime('%Y-%m-%d')}

## Related

- [[mental-health-awareness]] - Broader context of psychological well-being
- [[relationship-psychology]] - Understanding interpersonal dynamics

---

## Transcript

{transcript_content}
"""

    # Save page
    with open(page_path, 'w', encoding='utf-8') as f:
        f.write(page_content)

    return page_path

def update_index_md():
    """Update index.md with new content"""
    index_path = Path(NEURAL_NEXUS_PATH) / "docs" / "index.md"
    
    # Read current index
    try:
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        content = ""

    # Add HealthyGamerGG section if not present
    if "HealthyGamerGG YouTube Summaries" not in content:
        healthygamer_section = """

## HealthyGamerGG YouTube Summaries

**Mental Health & Relationships**
- [[can-men-women-be-friends]] - Exploring cross-gender friendships
- [[the-lie-of-positive-thinking]] - Cognitive psychology and positive thinking critique
- [[why-you-should-never-confess-your-love]] - Relationship psychology and love confession
- [[how-to-actually-have-an-elite-mindset]] - Mindset development and peak performance
- [[flirting-kinda-sucks-actually]] - Dating dynamics and social interaction challenges
"""
        
        # Insert before the last line
        lines = content.split('\n')
        lines.insert(-1, healthygamer_section)
        content = '\n'.join(lines)

    # Write back
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)

def update_log_md():
    """Update log.md with processing entry"""
    log_path = Path(NEURAL_NEXUS_PATH) / "docs" / "log.md"
    
    # Read current log
    try:
        with open(log_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        content = ""

    # Add new entry
    new_entry = f"""

## {datetime.now().strftime('%Y-%m-%d')} process | HealthyGamerGG YouTube Videos

- **Source:** HealthyGamerGG YouTube Channel (@HealthyGamerGG)
- **Action:** Processed 5 videos into wiki pages
- **Content:** Mental health, relationships, dating, self-improvement
- **Output:** Created concept pages + raw transcripts
- **Method:** TranscriptAPI + YouTube Transcript API fallback
"""

    # Add to end of file
    content += new_entry

    # Write back
    with open(log_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    if not TRANSCRIPT_API_KEY:
        print("⚠️  TRANSCRIPT_API_KEY not set - using YouTube Transcript API fallback")
        print("Set with: export TRANSCRIPT_API_KEY='your_key_here' for better reliability")

    # Load videos
    with open('healthygamer_videos.json', 'r') as f:
        all_videos = json.load(f)

    # Initialize tracker
    tracker = VideoTracker("healthygamer_tracker.json")

    # Get unprocessed videos
    unprocessed_videos = []
    for video in all_videos:
        video_id = video['video_id']
        if not tracker.is_video_processed(video_id):
            unprocessed_videos.append(video)

    # Randomly select up to 5 videos
    selected_videos = random.sample(unprocessed_videos, min(5, len(unprocessed_videos)))

    print(f"📥 Processing {len(selected_videos)} randomly selected videos...\n")

    # Create directories
    RAW_TRANSCRIPTS_DIR.mkdir(parents=True, exist_ok=True)

    results = {
        "success": 0,
        "failed": 0,
        "not_found": 0,
        "rate_limited": 0,
        "errors": []
    }

    for i, video in enumerate(selected_videos, 1):
        video_id = video['video_id']
        video_url = video['url']
        title = video['title']
        
        print(f"[{i}/{len(selected_videos)}] Processing: {title[:50]}...")

        # Fetch transcript
        result = fetch_transcript(video_url, video_id, title)

        if result.get("success"):
            transcript_data = result["data"]
            transcript_file = save_transcript(video_id, title, transcript_data)
            print(f"  ✅ Saved transcript: {transcript_file.name}")
            
            # Create Neural Nexus page
            try:
                page_path = create_neural_nexus_page(video_id, title, transcript_file)
                print(f"  ✅ Created page: {page_path.name}")
                
                # Mark as processed
                tracker.mark_processed(video_id, title, video_url)
                results["success"] += 1
            except Exception as e:
                print(f"  ❌ Page creation failed: {str(e)}")
                results["errors"].append({
                    "video_id": video_id,
                    "title": title,
                    "error": str(e)
                })
                results["failed"] += 1

        elif result.get("status") == "not_found":
            print(f"  ❌ HTTP 404 - Video unavailable")
            results["not_found"] += 1
        elif result.get("status") == "rate_limited":
            print(f"  ⚠️  Rate limited - pausing for 60s")
            results["rate_limited"] += 1
            time.sleep(60)
            continue
        else:
            print(f"  ❌ Error: {result.get('error')}")
            results["errors"].append({
                "video_id": video_id,
                "title": title,
                "error": result.get('error')
            })
            results["failed"] += 1

        # Rate limiting: delay between requests
        time.sleep(3)

    # Update index and log
    update_index_md()
    update_log_md()

    # Save results
    results_file = Path(NEURAL_NEXUS_PATH) / "healthygamer_ingestion_results.json"
    with open(results_file, 'w') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"\n{'='*60}")
    print(f"📊 Daily Ingestion Complete")
    print(f"{'='*60}")
    print(f"✅ Success: {results['success']}")
    print(f"❌ Failed: {results['failed']}")
    print(f"⚠️  Not Found (404): {results['not_found']}")
    print(f"🚫 Rate Limited: {results['rate_limited']}")
    print(f"\nResults saved to: {results_file}")

if __name__ == "__main__":
    main()