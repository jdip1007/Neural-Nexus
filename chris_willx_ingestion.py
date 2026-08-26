#!/usr/bin/env python3
"""
Chris Willx YouTube Neural Nexus Ingestion Script
Daily ingestion with duplicate detection and random video selection
"""

import json
import requests
import random
import time
from datetime import datetime
import hashlib
import os
import re
from urllib.parse import urlparse, parse_qs
import yaml
from video_tracker import VideoTracker


class ChrisWillxIngestion:
    def __init__(self):
        self.video_tracker_path = "./video_tracker.json"
        self.raw_transcripts_path = "./raw/transcripts"
        self.docs_path = "./docs"
        self.transcript_api_key = os.getenv("TRANSCRIPT_API_KEY")
        self.neural_nexus_path = os.getenv("NEURAL_NEXUS_PATH", "/home/hermes/Neural-Nexus/docs")
        self.neural_nexus_repo = os.getenv("NEURAL_NEXUS_REPO", "github.com/jdip1007/Neural-Nexus")
        
        # Load real videos from extracted data
        try:
            with open('real_channel_videos.json', 'r') as f:
                self.channel_videos = json.load(f)
        except FileNotFoundError:
            # Fallback to dummy videos if real ones not available
            self.channel_videos = [
                {
                    "title": "25 Years Later: \"We Were Wrong About The War\"",
                    "url": "https://www.youtube.com/watch?v=dummy1",
                    "duration": "10 minutes, 29 seconds",
                    "views": "21K",
                    "video_id": "dummy1"
                },
                {
                    "title": "Ex-Gang Member: Why Violence Is Safer Than Vulnerability - Johnny Chang",
                    "url": "https://www.youtube.com/watch?v=dummy2",
                    "duration": "2 hours",
                    "views": "79K",
                    "video_id": "dummy2"
                },
                {
                    "title": "\"81% Of Women Said Yes. Only 58% Of Men Did.\"",
                    "url": "https://www.youtube.com/watch?v=dummy3",
                    "duration": "10 minutes, 9 seconds",
                    "views": "75K",
                    "video_id": "dummy3"
                },
                {
                    "title": "Jocko Willink, Matt McCusker & Jeff Dye - Mostly Wise #3",
                    "url": "https://www.youtube.com/watch?v=dummy4",
                    "duration": "2 hours, 33 minutes",
                    "views": "211K",
                    "video_id": "dummy4"
                },
                {
                    "title": "\"After 3 Days... I Start To Feel Amazing\" - Dr David Sinclair",
                    "url": "https://www.youtube.com/watch?v=dummy5",
                    "duration": "8 minutes, 26 seconds",
                    "views": "36K",
                    "video_id": "dummy5"
                },
                {
                    "title": "\"I Have A Problem With Love On The Spectrum\" - Jeff Dye",
                    "url": "https://www.youtube.com/watch?v=dummy6",
                    "duration": "10 minutes, 5 seconds",
                    "views": "62K",
                    "video_id": "dummy6"
                },
                {
                    "title": "\"Age Reversal Is Coming.\" Everything You Need To Know - Dr David Sinclair",
                    "url": "https://www.youtube.com/watch?v=dummy7",
                    "duration": "2 hours, 5 minutes",
                    "views": "67K",
                    "video_id": "dummy7"
                },
                {
                    "title": "Why Violence Is Safer Than Vulnerability - Johnny Chang",
                    "url": "https://www.youtube.com/watch?v=dummy8",
                    "duration": "2 hours",
                    "views": "152K",
                    "video_id": "dummy8"
                }
            ]
        
        # Initialize video tracker
        self.tracker = VideoTracker(self.video_tracker_path)
        
        # Ensure directories exist
        os.makedirs(self.raw_transcripts_path, exist_ok=True)
        os.makedirs(self.docs_path, exist_ok=True)
    
    def extract_video_id(self, url):
        """Extract video ID from YouTube URL"""
        parsed_url = urlparse(url)
        
        # Handle standard YouTube URLs with query parameters
        if parsed_url.netloc == 'www.youtube.com' and parsed_url.path == '/watch':
            video_id = parse_qs(parsed_url.query).get('v', [None])[0]
            if video_id:
                return video_id
        
        # Handle shortened URLs like https://youtu.be/video_id
        elif parsed_url.netloc == 'youtu.be':
            # The video ID is the path component
            video_id = parsed_url.path.lstrip('/')
            if video_id:
                return video_id
        
        # Handle other YouTube URL formats
        elif 'youtube.com' in parsed_url.netloc:
            # Try to extract from path if it's in format /video_id or /embed/video_id
            path_parts = parsed_url.path.split('/')
            if len(path_parts) >= 2 and path_parts[1]:
                # Check if it's a direct video ID or embed format
                if path_parts[0] == '' and len(path_parts[1]) == 11:  # Direct video ID
                    return path_parts[1]
                elif path_parts[0] == 'embed' and len(path_parts[1]) == 11:  # Embed format
                    return path_parts[1]
        
        return None
    
    def get_transcript_from_api(self, video_id):
        """Fetch transcript using TranscriptAPI"""
        if not self.transcript_api_key:
            raise Exception("TRANSCRIPT_API_KEY environment variable not set")
        
        # Simulate transcript API call
        # In real implementation, this would call the actual TranscriptAPI
        return {
            "video_id": video_id,
            "title": self.get_video_title(video_id),
            "text": self.generate_mock_transcript(video_id),
            "timestamp": datetime.now().isoformat()
        }
    
    def get_video_title(self, video_id):
        """Get video title from channel videos list"""
        for video in self.channel_videos:
            if video_id in video["url"]:
                return video["title"]
        return f"Video {video_id}"
    
    def generate_mock_transcript(self, video_id):
        """Generate mock transcript for demonstration"""
        topics = {
            "dummy1": ["war", "history", "reflection", "lessons"],
            "dummy2": ["violence", "vulnerability", "gangs", "psychology"],
            "dummy3": ["relationships", "dating", "gender", "statistics"],
            "dummy4": ["leadership", "military", "wisdom", "interview"],
            "dummy5": ["health", "diet", "aging", "science"],
            "dummy6": ["relationships", "spectrum", "autism", "dating"],
            "dummy7": ["AI", "technology", "future", "debate"],
            "dummy8": ["ethics", "education", "teachers", "students"],
            "dummy9": ["diet", "health", "harvard", "nutrition"]
        }
        
        video_topics = topics.get(video_id, ["general", "discussion"])
        return f"This is a mock transcript for video {video_id}. Topics covered include: {', '.join(video_topics)}. This is a simulated transcript for demonstration purposes. In a real implementation, this would contain the actual transcript text from the video."
    
    def analyze_content(self, transcript_text):
        """Analyze transcript content for key topics and concepts"""
        # Simple keyword-based analysis
        topics = []
        
        # Common topics in Chris Willx content
        topic_keywords = {
            "psychology": ["mind", "brain", "behavior", "mental", "psychological"],
            "relationships": ["love", "dating", "partnership", "marriage", "connection"],
            "philosophy": ["meaning", "purpose", "existence", "truth", "wisdom"],
            "health": ["diet", "exercise", "nutrition", "wellness", "medicine"],
            "technology": ["AI", "tech", "digital", "innovation", "future"],
            "society": ["culture", "social", "community", "politics", "ethics"],
            "personal growth": ["growth", "development", "improvement", "self", "awareness"]
        }
        
        text_lower = transcript_text.lower()
        
        for topic, keywords in topic_keywords.items():
            if any(keyword in text_lower for keyword in keywords):
                topics.append(topic)
        
        return topics if topics else ["general", "discussion"]
    
    def create_frontmatter(self, video_data, topics):
        """Create frontmatter for the Neural Nexus page"""
        return {
            "title": video_data["title"],
            "created": datetime.now().isoformat(),
            "updated": datetime.now().isoformat(),
            "type": "video",
            "tags": ["youtube", "chris-willx"] + topics,
            "sources": [video_data["url"]],
            "duration": video_data.get("duration", "Unknown"),
            "views": video_data.get("views", "Unknown"),
            "video_id": self.extract_video_id(video_data["url"])
        }
    
    def create_wikilinks(self, topics):
        """Create wikilinks for related topics"""
        wikilinks = []
        for topic in topics:
            # Create simple wikilink format
            wikilinks.append(f"[[{topic}]]")
        return wikilinks
    
    def create_citations(self, video_data):
        """Create proper citations for the video"""
        return f"""
## Sources

- **Video**: [{video_data['title']}]({video_data['url']})
- **Channel**: Chris Willx (@ChrisWillx)
- **Published**: {datetime.now().strftime('%Y-%m-%d')}
- **Duration**: {video_data.get('duration', 'Unknown')}
- **Views**: {video_data.get('views', 'Unknown')}
"""
    
    def create_neural_nexus_page(self, video_data, transcript_data, topics):
        """Create a Neural Nexus page with proper formatting"""
        # Create filename
        video_id = self.extract_video_id(video_data["url"])
        safe_title = re.sub(r'[^\w\s-]', '', video_data["title"]).strip()
        safe_title = re.sub(r'[-\s]+', '-', safe_title)
        filename = f"youtube-{video_id}-{safe_title[:50]}.md"
        filepath = os.path.join(self.docs_path, filename)
        
        # Create frontmatter
        frontmatter = self.create_frontmatter(video_data, topics)
        
        # Create content
        wikilinks = self.create_wikilinks(topics)
        citations = self.create_citations(video_data)
        
        content = f"""# {video_data['title']}

{', '.join(wikilinks)}

## Transcript

{transcript_data['text']}

## Analysis

This video explores key topics related to {', '.join(topics)}. The content provides insights into {', '.join(topics)} and their implications for modern society.

## Key Takeaways

- Analysis of {', '.join(topics)}
- Discussion of {', '.join(topics)}
- Insights into {', '.join(topics)}

{citations}
"""
        
        # Write file
        with open(filepath, 'w', encoding='utf-8') as f:
            # Write YAML frontmatter
            f.write("---\n")
            yaml.dump(frontmatter, f, default_flow_style=False)
            f.write("---\n\n")
            # Write content
            f.write(content)
        
        return filepath
    
    def process_video(self, video_data):
        """Process a single video"""
        video_id = self.extract_video_id(video_data["url"])
        
        print(f"Processing: {video_data['title']}")
        
        # Check if already processed
        if video_id and self.tracker.is_video_processed(video_id):
            print(f"  → Already processed, skipping...")
            return None
        
        try:
            # Fetch transcript
            print(f"  → Fetching transcript for {video_id}...")
            transcript_data = self.get_transcript_from_api(video_id)
            
            # Analyze content
            print(f"  → Analyzing content...")
            topics = self.analyze_content(transcript_data["text"])
            print(f"  → Topics identified: {topics}")
            
            # Create Neural Nexus page
            print(f"  → Creating Neural Nexus page...")
            page_path = self.create_neural_nexus_page(video_data, transcript_data, topics)
            
            # Mark as processed
            if video_id:
                self.tracker.add_processed_video(video_id, video_data["title"], video_data["url"])
            
            print(f"  → Successfully processed: {page_path}")
            return page_path
            
        except Exception as e:
            print(f"  → ERROR: {str(e)}")
            return None
    
    def run_daily_ingestion(self):
        """Run the daily ingestion workflow"""
        print("=== Chris Willx YouTube Daily Ingestion ===")
        print(f"Starting at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Get unprocessed videos
        unprocessed_videos = self.tracker.get_unprocessed_videos(self.channel_videos)
        print(f"Total videos in channel: {len(self.channel_videos)}")
        print(f"Already processed: {self.tracker.get_processed_count()}")
        print(f"Unprocessed videos: {len(unprocessed_videos)}")
        
        if not unprocessed_videos:
            print("No new videos to process.")
            return
        
        # Randomly select up to 5 videos
        selected_videos = self.tracker.select_random_videos(unprocessed_videos, 5)
        print(f"Selected {len(selected_videos)} videos for processing:")
        
        for i, video in enumerate(selected_videos, 1):
            print(f"{i}. {video['title']}")
        
        # Process selected videos
        success_count = 0
        failure_count = 0
        processed_paths = []
        
        for video in selected_videos:
            result = self.process_video(video)
            if result:
                success_count += 1
                processed_paths.append(result)
            else:
                failure_count += 1
            
            # Add small delay to avoid rate limiting
            time.sleep(1)
        
        # Generate report
        self.generate_report(success_count, failure_count, processed_paths)
        
        print(f"\n=== Ingestion Complete ===")
        print(f"Successfully processed: {success_count}")
        print(f"Failed to process: {failure_count}")
        print(f"Success rate: {success_count/(success_count+failure_count)*100:.1f}%")
    
    def generate_report(self, success_count, failure_count, processed_paths):
        """Generate processing report"""
        report = f"""
# Chris Willx YouTube Ingestion Report

**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Summary
- **Total videos processed**: {success_count + failure_count}
- **Successfully processed**: {success_count}
- **Failed to process**: {failure_count}
- **Success rate**: {success_count/(success_count+failure_count)*100:.1f}%

## Processed Videos
"""
        
        for path in processed_paths:
            filename = os.path.basename(path)
            report += f"- {filename}\n"
        
        report += f"""
## Statistics
- **Channel**: Chris Willx (@ChrisWillx)
- **Total channel videos**: {len(self.channel_videos)}
- **Already processed**: {self.tracker.get_processed_count()}
- **Unprocessed remaining**: {len(self.channel_videos) - self.tracker.get_processed_count()}

## Recent Activity
"""
        
        recent_videos = self.tracker.get_recent_videos(5)
        for video in recent_videos:
            report += f"- {video.get('title', 'Unknown')}\n"
        
        # Save report
        report_path = os.path.join(self.docs_path, "chris_willx_ingestion_report.md")
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"Report saved to: {report_path}")


def main():
    """Main function to run the ingestion"""
    ingestion = ChrisWillxIngestion()
    ingestion.run_daily_ingestion()


if __name__ == "__main__":
    main()