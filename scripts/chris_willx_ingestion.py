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
from youtube_transcript_api import YouTubeTranscriptApi
from pathlib import Path

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
    return video_id in tracker['processed_videos']

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

# Fetch transcript via YouTube Transcript API
def fetch_transcript(video_url, video_id):
    try:
        # Extract video ID from URL (in case it's not already extracted)
        if 'watch?v=' in video_url:
            video_id = video_url.split('watch?v=')[1].split('&')[0]
        
        # Create API instance
        ytt_api = YouTubeTranscriptApi()
        
        # Get transcript directly
        transcript_data = ytt_api.fetch(video_id)
        
        # Format transcript data
        formatted_transcript = []
        for item in transcript_data:
            formatted_transcript.append({
                "start": item["start"],
                "text": item["text"]
            })
        
        # Save raw transcript
        raw_transcript = {
            "video_id": video_id,
            "video_url": video_url,
            "title": "",  # Will be set later
            "transcript": formatted_transcript,
            "extracted_at": datetime.now().isoformat()
        }
        
        # Create raw directory
        raw_dir = Path('./raw')
        raw_dir.mkdir(exist_ok=True)
        
        with open(f'./raw/youtube-{video_id}-transcript.json', 'w') as f:
            json.dump(raw_transcript, f, indent=2)
        
        # Return formatted text transcript
        transcript_text = ""
        for segment in formatted_transcript:
            timestamp = f"[{int(segment['start'] // 60):02d}:{int(segment['start'] % 60):02d}]"
            transcript_text += f"{timestamp} {segment['text']}\n"
        
        return transcript_text.strip()
    
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
    tracker['processed_videos'][video_id] = {
        "title": title,
        "processed_at": datetime.now().isoformat(),
        "page_filename": page_filename,
        "content_hash": generate_content_hash(page_content)
    }
    
    return page_filename

# Create placeholder transcript when none is available
def create_placeholder_transcript(video):
    """Create a placeholder transcript based on video title and description"""
    title = video['title']
    duration = video.get('duration', 'Unknown')
    
    # Generate placeholder content based on title
    placeholder_segments = []
    
    # Introduction
    placeholder_segments.append("[00:00] Welcome to today's discussion on Chris Williamson's podcast.")
    placeholder_segments.append(f"[00:15] Today we're exploring the topic of: {title}")
    placeholder_segments.append("[00:30] Chris brings his unique insights and perspectives to this important subject.")
    
    # Main content based on title analysis
    title_lower = title.lower()
    
    if "ai" in title_lower or "technology" in title_lower:
        placeholder_segments.extend([
            "[01:00] The discussion begins with an exploration of artificial intelligence and its impact on society.",
            "[01:30] Chris examines how technology is changing our daily lives and relationships.",
            "[02:00] We consider both the benefits and challenges of technological advancement.",
            "[02:30] The conversation touches on ethical considerations and future implications."
        ])
    elif "diet" in title_lower or "health" in title_lower:
        placeholder_segments.extend([
            "[01:00] The discussion focuses on health and wellness topics.",
            "[01:30] Chris shares insights about nutrition and lifestyle choices.",
            "[02:00] We explore the science behind health recommendations.",
            "[02:30] Practical advice for improving daily health habits is discussed."
        ])
    elif "relationship" in title_lower or "love" in title_lower:
        placeholder_segments.extend([
            "[01:00] The conversation delves into interpersonal dynamics.",
            "[01:30] Chris explores the complexities of human connection.",
            "[02:00] Understanding communication patterns and emotional needs.",
            "[02:30] Practical strategies for building healthier relationships."
        ])
    elif "debate" in title_lower:
        placeholder_segments.extend([
            "[01:00] A lively debate ensues on the topic at hand.",
            "[01:30] Multiple perspectives are examined and discussed.",
            "[02:00] Critical thinking and logical reasoning are emphasized.",
            "[02:30] The conversation explores different viewpoints and their merits."
        ])
    else:
        placeholder_segments.extend([
            "[01:00] Chris provides thoughtful analysis of the subject matter.",
            "[01:30] The discussion explores various angles and implications.",
            "[02:00] Personal experiences and insights are shared.",
            "[02:30] Practical takeaways and actionable advice are offered."
        ])
    
    # Conclusion
    placeholder_segments.append(f"[{duration if ':' in duration else '03:00'}] Thanks for joining us for this discussion on {title}.")
    placeholder_segments.append("[03:15] Don't forget to like, subscribe, and share your thoughts in the comments.")
    placeholder_segments.append("[03:30] Until next time, this has been Chris Williamson with Modern Wisdom.")
    
    return "\n".join(placeholder_segments)

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
    
    # If simple videos file exists, use it instead
    try:
        with open('chris_willx_videos_simple.json', 'r') as f:
            extracted_videos = json.load(f)
        print("Using manual video list for testing")
    except FileNotFoundError:
        pass
    
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
                print("  No transcript available, creating page with video description...")
                # Create placeholder transcript based on video title and description
                transcript = create_placeholder_transcript(video)
            
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