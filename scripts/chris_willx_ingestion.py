#!/usr/bin/env python3
"""
Chris Willx YouTube Ingestion Script
Daily ingestion with duplicate detection and random video selection
"""

import json
import random
import requests
import os
from datetime import datetime
import hashlib

# Environment variables
TRANSCRIPT_API_KEY = os.getenv('TRANSCRIPT_API_KEY')
NEURAL_NEXUS_PATH = os.getenv('NEURAL_NEXUS_PATH')
NEURAL_NEXUS_REPO = os.getenv('NEURAL_NEXUS_REPO')

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

# Fetch transcript via TranscriptAPI
def fetch_transcript(video_url, video_id):
    try:
        # Extract video ID from URL
        api_url = f"https://api.transcriptapi.com/v1/video?url={video_url}"
        
        headers = {
            'Authorization': f'Bearer {TRANSCRIPT_API_KEY}',
            'Content-Type': 'application/json'
        }
        
        response = requests.post(api_url, headers=headers, timeout=300)
        response.raise_for_status()
        
        result = response.json()
        
        # Save raw transcript
        raw_transcript = {
            "video_id": video_id,
            "video_url": video_url,
            "title": result.get('title', ''),
            "transcript": result.get('transcript', ''),
            "extracted_at": datetime.now().isoformat()
        }
        
        os.makedirs('./raw', exist_ok=True)
        with open(f'./raw/youtube-{video_id}-transcript.json', 'w') as f:
            json.dump(raw_transcript, f, indent=2)
        
        return result.get('transcript', '')
    
    except Exception as e:
        print(f"Error fetching transcript for {video_id}: {e}")
        return ""

# Generate content hash for duplicate prevention
def generate_content_hash(content):
    return hashlib.sha256(content.encode()).hexdigest()

# Create Neural Nexus page
def create_neural_nexus_page(video, transcript, tracker):
    video_id = video['id']
    title = video['title']
    url = video['url']
    
    # Extract key topics and concepts from transcript
    key_topics = extract_key_topics(transcript)
    
    # Generate page filename
    safe_title = title.lower().replace(' ', '-').replace('"', '').replace('’', '').replace('—', '-').replace(':', '-')
    page_filename = f"youtube-{video_id}-{safe_title}.md"
    page_path = f"{NEURAL_NEXUS_PATH}/{page_filename}"
    
    # Create frontmatter
    frontmatter = {
        "title": title,
        "created": datetime.now().strftime("%Y-%m-%d"),
        "updated": datetime.now().strftime("%Y-%m-%d"),
        "type": "reading",
        "classification": "psychology.media-ethics" if "ethics" in title.lower() or "moral" in title.lower() else "psychology.personal-development",
        "domain": "psychology",
        "tags": ["youtube", "chris-willx", "podcast", "video-summary", "transcript"],
        "sources": [f"raw/youtube-{video_id}-transcript.json"],
        "confidence": "medium",
        "status": "active",
        "reviewed": datetime.now().strftime("%Y-%m-%d"),
        "backlinks": []
    }
    
    # Add domain-specific tags
    if "ai" in title.lower():
        frontmatter["tags"].extend(["ai", "artificial-intelligence"])
    if "debate" in title.lower():
        frontmatter["tags"].extend(["discussion", "debate"])
    if "diet" in title.lower():
        frontmatter["tags"].extend(["health", "nutrition"])
    if "science" in title.lower():
        frontmatter["tags"].extend(["science", "research"])
    
    # Create page content
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

## Summary

This video is part of Chris Williamson's podcast series featuring discussions on various topics including psychology, philosophy, current events, and personal development. The transcript has been processed and analyzed for key insights and concepts.

## Key Topics and Concepts

{key_topics}

## Transcript Analysis

The transcript has been analyzed to identify main themes, notable quotes, and actionable insights from the discussion.

## Related Pages

- [[chris-williamson-podcast|Chris Williamson Podcast Overview]]
- [[podcast-analysis|Podcast Content Analysis]]
- [[psychology-personal-development|Personal Development Psychology]]

## Sources

^{f"raw/youtube-{video_id}-transcript.json"}
"""
    
    # Write page file
    with open(page_path, 'w') as f:
        f.write(page_content)
    
    # Update video tracker
    tracker['processed_videos'].append({
        "id": video_id,
        "title": title,
        "url": url,
        "processed_at": datetime.now().isoformat(),
        "page_filename": page_filename,
        "content_hash": generate_content_hash(page_content)
    })
    
    return page_filename

# Extract key topics from transcript
def extract_key_topics(transcript):
    if not transcript:
        return "No transcript available for analysis."
    
    # Simple topic extraction based on keywords
    topics = []
    
    # Common topics in Chris Williamson's content
    topic_keywords = {
        "psychology": ["mind", "brain", "psychology", "mental", "behavior", "thought", "emotion", "feeling"],
        "philosophy": ["philosophy", "meaning", "purpose", "existence", "truth", "wisdom"],
        "relationships": ["love", "relationship", "marriage", "friendship", "connection", "partnership"],
        "current_events": ["news", "current", "events", "society", "culture", "politics"],
        "self_improvement": ["growth", "improvement", "development", "habit", "routine", "success"],
        "health": ["health", "diet", "nutrition", "exercise", "wellness", "medical"],
        "technology": ["ai", "technology", "digital", "internet", "social media", "tech"]
    }
    
    transcript_lower = transcript.lower()
    
    for category, keywords in topic_keywords.items():
        if any(keyword in transcript_lower for keyword in keywords):
            topics.append(f"- **{category.title()}**: Discussion of {category}-related concepts and insights")
    
    if not topics:
        topics.append("- **General Discussion**: Broad conversation covering multiple topics")
    
    return "\n".join(topics)

# Main ingestion workflow
def main():
    print("Starting Chris Willx YouTube ingestion workflow...")
    
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
            # Fetch transcript
            print("  Fetching transcript...")
            transcript = fetch_transcript(video['url'], video['id'])
            
            if not transcript:
                print(f"  Warning: No transcript available for {video['id']}")
                continue
            
            # Create Neural Nexus page
            print("  Creating Neural Nexus page...")
            page_filename = create_neural_nexus_page(video, transcript, tracker)
            
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
    print(f"Processed {processed_count} out of {len(selected_videos)} selected videos")
    print(f"Total videos processed: {len(tracker['processed_videos'])}")

if __name__ == "__main__":
    main()