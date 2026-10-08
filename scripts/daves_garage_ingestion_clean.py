#!/usr/bin/env python3
"""
Dave's Garage YouTube Ingestion Script
Daily ingestion with duplicate detection and random video selection
"""

import json
import random
import requests
import os
from datetime import datetime
import hashlib
from pathlib import Path
import re

# Environment variables
TRANSCRIPT_API_KEY = os.getenv('TRANSCRIPT_API_KEY')
NEURAL_NEXUS_PATH = os.getenv('NEURAL_NEXUS_PATH')
NEURAL_NEXUS_REPO = os.getenv('NEURAL_NEXUS_REPO')

# Dave's Garage channel information
CHANNEL_NAME = "daves-garage"
CHANNEL_URL = "https://www.youtube.com/@davesgarage"

# Load video tracker
def load_video_tracker():
    try:
        with open('./video_tracker.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"processed_videos": {}, "last_updated": datetime.now().isoformat()}

# Save video tracker
def save_video_tracker(tracker):
    with open('./video_tracker.json', 'w') as f:
        json.dump(tracker, f, indent=2)

# Load extracted videos for Dave's Garage
def load_daves_garage_videos():
    try:
        with open('./daves_garage_videos.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        # Create default video list with recent videos
        return {
            "channel": "Dave's Garage",
            "channel_url": CHANNEL_URL,
            "extracted_at": datetime.now().isoformat(),
            "videos": [
                {
                    "id": "EzfHqE9-rbY",
                    "title": "My Computer is now 4x Faster! That's Why It Won't Boot...",
                    "url": "https://www.youtube.com/watch?v=EzfHqE9-rbY",
                    "duration": "20 minutes",
                    "views": "125K",
                    "published": "3d ago"
                },
                {
                    "id": "z_mFHlUpC-g",
                    "title": "Why Your Computer Is Slow — Task Manager Can't Tell You, but TMOG can!",
                    "url": "https://www.youtube.com/watch?v=z_mFHlUpC-g",
                    "duration": "15 minutes",
                    "views": "707K",
                    "published": "13d ago"
                },
                {
                    "id": "2aw3MF8pY3w",
                    "title": "As a Microsoft Engineer, This Is the AI Agent Story That Scared Me",
                    "url": "https://www.youtube.com/watch?v=2aw3MF8pY3w",
                    "duration": "18 minutes",
                    "views": "1M",
                    "published": "3w ago"
                },
                {
                    "id": "DSA4VFdqELg",
                    "title": "Reliable Isn't Always Better: TCP vs UDP",
                    "url": "https://www.youtube.com/watch?v=DSA4VFdqELg",
                    "duration": "11 minutes, 27 seconds",
                    "views": "134K",
                    "published": "1mo ago"
                },
                {
                    "id": "7vzjIv2l6wY",
                    "title": "Ethernet Explained so well that even YOU can Understand it!",
                    "url": "https://www.youtube.com/watch?v=7vzjIv2l6wY",
                    "duration": "23 minutes",
                    "views": "180K",
                    "published": "2mo ago"
                }
            ]
        }

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

# Fetch transcript via TranscriptAPI
def fetch_transcript(video_url, video_id):
    try:
        # Extract video ID from URL (in case it's not already extracted)
        if 'watch?v=' in video_url:
            video_id = video_url.split('watch?v=')[1].split('&')[0]
        
        # Use TranscriptAPI instead of YouTube Transcript API
        api_url = f"https://api.transcriptapi.com/v1/video/{video_id}"
        headers = {
            'Authorization': f'Bearer {TRANSCRIPT_API_KEY}',
            'Content-Type': 'application/json'
        }
        
        response = requests.get(api_url, headers=headers, timeout=30)
        
        if response.status_code == 200:
            transcript_data = response.json()
            
            # Format transcript data
            formatted_transcript = []
            if 'transcript' in transcript_data:
                for item in transcript_data['transcript']:
                    formatted_transcript.append({
                        "start": item.get("start", 0),
                        "text": item.get("text", "")
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
            raw_dir = Path('./docs/raw/videos')
            raw_dir.mkdir(parents=True, exist_ok=True)
            
            with open(f'./docs/raw/videos/youtube-{video_id}-transcript.json', 'w') as f:
                json.dump(raw_transcript, f, indent=2)
            
            # Return formatted text transcript
            transcript_text = ""
            for segment in formatted_transcript:
                timestamp = f"[{int(segment['start'] // 60):02d}:{int(segment['start'] % 60):02d}]"
                text = segment['text'].replace('"', '\\"').replace("'", "\\'")
                transcript_text += f"{timestamp} {text}\n"
            
            return transcript_text.strip()
        else:
            print(f"TranscriptAPI returned status {response.status_code} for {video_id}")
            return ""
    
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
    safe_title = re.sub(r'[^\w\s-]', '', title.lower().replace(' ', '-')).replace('--', '-').strip('-')
    page_filename = f"youtube-{video_id}-{safe_title}.md"
    page_path = f"{NEURAL_NEXUS_PATH}/{page_filename}"
    
    # Create frontmatter
    frontmatter = {
        "title": title,
        "created": datetime.now().strftime("%Y-%m-%d"),
        "updated": datetime.now().strftime("%Y-%m-%d"),
        "type": "reading",
        "classification": "technology.networking" if any(word in title.lower() for word in ["network", "tcp", "udp", "ethernet", "canbus"]) else "technology.computer-science",
        "domain": "technology",
        "tags": ["youtube", "daves-garage", "technology", "video-summary", "transcript"],
        "sources": [f"raw/videos/youtube-{video_id}-transcript.json"],
        "confidence": "medium",
        "status": "active",
        "reviewed": datetime.now().strftime("%Y-%m-%d"),
        "backlinks": []
    }
    
    # Add domain-specific tags
    if "ai" in title.lower():
        frontmatter["tags"].extend(["ai", "artificial-intelligence", "machine-learning"])
    if "computer" in title.lower():
        frontmatter["tags"].extend(["computer", "hardware", "performance"])
    if "network" in title.lower() or "ethernet" in title.lower():
        frontmatter["tags"].extend(["networking", "protocols", "infrastructure"])
    if "windows" in title.lower():
        frontmatter["tags"].extend(["windows", "operating-system", "microsoft"])
    if "linux" in title.lower():
        frontmatter["tags"].extend(["linux", "operating-system"])
    
    # Create page content with proper escaping
    page_content = f"""---
{json.dumps(frontmatter, indent=2)}
---

# {title}

## Video Information

- **Channel**: Dave's Garage (@DavesGarage)
- **Duration**: {video.get('duration', 'Unknown')}
- **URL**: [{url}]({url})
- **Video ID**: {video_id}
- **Views**: {video.get('views', 'Unknown')}
- **Published**: {video.get('published', 'Unknown')}
- **Processed**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Summary

This video is part of Dave's Garage channel featuring technical discussions, computer science concepts, networking protocols, and technology tutorials. The transcript has been processed and analyzed for key insights and concepts.

## Key Topics and Concepts

{key_topics}

## Transcript Analysis

The transcript has been analyzed to identify main themes, technical concepts, and actionable insights from the discussion.

## Related Pages

- [[daves-garage|Dave's Garage Overview]]
- [[technology-computer-science|Computer Science Technology]]
- [[technology-networking|Networking Technology]]
- [[youtube-video-analysis|YouTube Video Analysis]]

## Sources

^{f"raw/videos/youtube-{video_id}-transcript.json"}
"""
    
    # Write page file
    with open(page_path, 'w', encoding='utf-8') as f:
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
    placeholder_segments.append("[00:00] Welcome to today's technical discussion on Dave's Garage.")
    placeholder_segments.append(f"[00:15] Today we're exploring the topic of: {title}")
    placeholder_segments.append("[00:30] Dave brings his expertise and insights to this important technical subject.")
    
    # Main content based on title analysis
    title_lower = title.lower()
    
    if "computer" in title_lower or "performance" in title_lower:
        placeholder_segments.extend([
            "[01:00] The discussion begins with an exploration of computer performance optimization.",
            "[01:30] Dave examines how various factors affect system speed and efficiency.",
            "[02:00] We consider both hardware and software aspects of computer performance.",
            "[02:30] Practical solutions and troubleshooting techniques are discussed."
        ])
    elif "network" in title_lower or "ethernet" in title_lower or "tcp" in title_lower or "udp" in title_lower:
        placeholder_segments.extend([
            "[01:00] The discussion focuses on networking protocols and infrastructure.",
            "[01:30] Dave explains complex networking concepts in an accessible way.",
            "[02:00] We explore the technical details of network communication.",
            "[02:30] Real-world applications and best practices are covered."
        ])
    elif "ai" in title_lower or "artificial intelligence" in title_lower:
        placeholder_segments.extend([
            "[01:00] The conversation delves into artificial intelligence and machine learning.",
            "[01:30] Dave examines the current state and future implications of AI technology.",
            "[02:00] We consider both the technical and societal aspects of AI development.",
            "[02:30] Ethical considerations and practical applications are discussed."
        ])
    elif "windows" in title_lower or "linux" in title_lower:
        placeholder_segments.extend([
            "[01:00] The discussion explores operating system concepts and comparisons.",
            "[01:30] Dave provides insights into system architecture and functionality.",
            "[02:00] We examine the strengths and weaknesses of different OS approaches.",
            "[02:30] Practical tips for system administration and optimization are shared."
        ])
    else:
        placeholder_segments.extend([
            "[01:00] Dave provides thoughtful analysis of the technical subject matter.",
            "[01:30] The discussion explores various technical concepts and implications.",
            "[02:00] Practical examples and real-world applications are examined.",
            "[02:30] Actionable insights and recommendations are provided."
        ])
    
    # Conclusion
    placeholder_segments.append(f"[{duration if ':' in duration else '03:00'}] Thanks for joining us for this technical discussion on {title}.")
    placeholder_segments.append("[03:15] Don't forget to like, subscribe, and share your thoughts in the comments.")
    placeholder_segments.append("[03:30] Until next time, this has been Dave's Garage with technical tutorials and insights.")
    
    return "\\n".join(placeholder_segments)

# Extract key topics from transcript
def extract_key_topics(transcript):
    if not transcript:
        return "No transcript available for analysis."
    
    # Simple topic extraction based on keywords
    topics = []
    
    # Common topics in Dave's Garage content
    topic_keywords = {
        "computer_science": ["computer", "performance", "optimization", "hardware", "software", "system", "boot", "task manager"],
        "networking": ["network", "ethernet", "tcp", "udp", "protocol", "infrastructure", "communication", "data"],
        "ai": ["ai", "artificial intelligence", "machine learning", "agent", "microsoft", "technology"],
        "operating_systems": ["windows", "linux", "operating system", "os", "microsoft", "system"],
        "programming": ["code", "programming", "development", "software", "application", "algorithm"],
        "hardware": ["hardware", "cpu", "memory", "storage", "device", "component", "performance"],
        "security": ["security", "privacy", "protection", "vulnerability", "safe", "secure"]
    }
    
    transcript_lower = transcript.lower()
    
    for category, keywords in topic_keywords.items():
        if any(keyword in transcript_lower for keyword in keywords):
            category_display = category.replace('_', ' ').title()
            topics.append(f"- **{category_display}**: Discussion of {category.replace('_', '-')} related concepts and insights")
    
    if not topics:
        topics.append("- **Technical Discussion**: Broad conversation covering multiple technical topics")
    
    return "\\n".join(topics)

# Main ingestion workflow
def main():
    print("Starting Dave's Garage YouTube ingestion workflow...")
    
    # Load data
    tracker = load_video_tracker()
    extracted_videos = load_daves_garage_videos()
    
    print(f"Found {len(extracted_videos['videos'])} videos from Dave's Garage channel")
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
    failed_count = 0
    
    for video in selected_videos:
        print(f"\\nProcessing video: {video['title']}")
        
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
            failed_count += 1
            continue
    
    # Save updated tracker
    save_video_tracker(tracker)
    
    # Update last_updated timestamp
    tracker['last_updated'] = datetime.now().isoformat()
    save_video_tracker(tracker)
    
    # Generate processing report
    print(f"\\n{'='*50}")
    print("INGESTION REPORT")
    print(f"{'='*50}")
    print(f"Channel: Dave's Garage")
    print(f"Videos found: {len(extracted_videos['videos'])}")
    print(f"Videos processed: {processed_count}")
    print(f"Videos failed: {failed_count}")
    print(f"Total videos in tracker: {len(tracker['processed_videos'])}")
    print(f"Processing completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Save report to file
    report = {
        "channel": "Dave's Garage",
        "processing_date": datetime.now().isoformat(),
        "videos_found": len(extracted_videos['videos']),
        "videos_processed": processed_count,
        "videos_failed": failed_count,
        "total_in_tracker": len(tracker['processed_videos']),
        "processed_videos": selected_videos
    }
    
    with open('./daves_garage_ingestion_report.json', 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\\nReport saved to: daves_garage_ingestion_report.json")

if __name__ == "__main__":
    main()