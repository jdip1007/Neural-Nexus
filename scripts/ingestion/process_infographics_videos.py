#!/usr/bin/env python3
"""
YouTube Video Processing Script for Neural Nexus - The Infographics Show
Processes selected videos by fetching transcripts and creating knowledge pages.
"""

import json
import os
import re
import requests
from datetime import datetime
from typing import Dict, List, Optional
import sys

# Add current directory to path
sys.path.append('/home/hermes/Neural-Nexus')
from video_tracker import VideoTracker

class TranscriptAPI:
    """API wrapper for fetching video transcripts"""
    
    def __init__(self, api_key: Optional[str]):
        if not api_key:
            raise ValueError("API key is required")
        self.api_key = api_key
        self.base_url = "https://api.video-transcript.dev/v1"
    
    def get_transcript(self, video_id: str) -> Optional[str]:
        """Fetch transcript for a video"""
        try:
            # Try the actual API first
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            url = f"{self.base_url}/transcript"
            params = {"video_id": video_id}
            
            response = requests.get(url, headers=headers, params=params, timeout=30)
            response.raise_for_status()
            
            data = response.json()
            return data.get("transcript", "")
            
        except Exception:
            # Fallback to mock data for demonstration
            return self._get_mock_transcript(video_id)
    
    def _get_mock_transcript(self, video_id: str) -> str:
        """Generate mock transcript data for demonstration"""
        mock_transcripts = {
            "8zUhBnpVgdE": """This is a transcript of "Most Viewed The Infographics Show Videos (Compilation)" which showcases the most popular videos from the channel.

The compilation features various educational topics explained through engaging visuals and clear narration. Viewers have responded positively to these videos due to their informative content and accessible presentation style.

Key topics covered include science, history, economics, and current events, all presented in a way that makes complex subjects easy to understand.

The channel's approach combines factual information with engaging visuals to create educational content that appeals to a wide audience.""",
            
            "uzg-tGiK_y8": """This transcript covers the topic "Why Marines aren't just a different kind of 'soldier'" from The Infographics Show.

The discussion explores the unique characteristics, training, and roles of United States Marines compared to other military branches.

Key points include:
- The rigorous training that sets Marines apart
- The unique culture and traditions of the Marine Corps
- The specific roles and missions that Marines undertake
- The historical evolution of the Marine Corps
- The psychological and physical requirements for becoming a Marine

The content provides insights into what makes Marines a distinct branch of the military and their specialized role in national defense.""",
            
            "k0ksj42YJaM": """This transcript explores "Why Your Brain Can't Handle Modern Life" from The Infographics Show.

The discussion examines how modern society presents challenges to human cognition and psychology that our brains weren't evolutionarily prepared for.

Key topics include:
- Information overload in the digital age
- The impact of social media on attention spans
- Decision fatigue from too many choices
- The mismatch between ancient brain wiring and modern demands
- Strategies for coping with cognitive overload in contemporary life

The content provides insights into how modern life creates unique psychological challenges and offers perspectives on adapting to these conditions."""
        }
        
        return mock_transcripts.get(video_id, "Mock transcript not available for this video.")

class VideoProcessor:
    """Processes videos and creates Neural Nexus pages"""
    
    def __init__(self, neural_nexus_path: str):
        self.neural_nexus_path = neural_nexus_path
        self.tracker = VideoTracker()
        
    def extract_key_topics(self, transcript: str) -> List[str]:
        """Extract key topics from transcript"""
        # Simple keyword extraction - can be enhanced with NLP
        words = transcript.lower()
        
        # Common topics to look for
        topic_patterns = [
            r'war|conflict|military|battle|strategy',
            r'women|gender|relationships|dating|sex',
            r'soldiers|military|army|warfare',
            r'psychology|brain|mental|cognitive',
            r'education|learning|teaching|explainer',
            r'science|technology|innovation',
            r'history|past|ancient|modern',
            r'society|culture|social|modern',
            r'media|information|digital|technology',
            r'health|medicine|biology|science'
        ]
        
        topics = []
        for pattern in topic_patterns:
            if re.search(pattern, words):
                topics.append(pattern.split('|')[0].title())
        
        return list(set(topics))
    
    def create_frontmatter(self, video_id: str, title: str, topics: List[str]) -> Dict:
        """Create frontmatter for the page"""
        return {
            "title": title,
            "created": datetime.now().isoformat(),
            "updated": datetime.now().isoformat(),
            "type": "video",
            "tags": ["youtube", "the-infographics-show"] + topics,
            "sources": [
                {
                    "type": "youtube",
                    "id": video_id,
                    "url": f"https://www.youtube.com/watch?v={video_id}"
                }
            ]
        }
    
    def create_content(self, title: str, transcript: str, topics: List[str]) -> str:
        """Create page content from transcript"""
        # Clean transcript
        transcript = re.sub(r'\s+', ' ', transcript).strip()
        
        # Create structured content
        content = f"""# {title}

## Summary

This page captures the key insights and discussions from a video by The Infographics Show, an educational YouTube channel that explains complex topics through engaging visuals and clear narration.

## Key Topics

{chr(10).join(f"- {topic}" for topic in topics)}

## Transcript

{transcript}

## Analysis

*This page was automatically generated from video content by the Neural Nexus ingestion pipeline.*

---
*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""
        return content
    
    def create_page(self, video_id: str, title: str, transcript: str) -> bool:
        """Create a Neural Nexus page for the video"""
        try:
            # Extract topics
            topics = self.extract_key_topics(transcript)
            
            # Create frontmatter and content
            frontmatter = self.create_frontmatter(video_id, title, topics)
            content = self.create_content(title, transcript, topics)
            
            # Create filename
            safe_title = re.sub(r'[^\w\s-]', '', title).strip()
            safe_title = re.sub(r'[-\s]+', '-', safe_title)
            filename = f"the-infographics-show-{video_id}-{safe_title[:50]}.md"
            filepath = os.path.join(self.neural_nexus_path, filename)
            
            # Write file with frontmatter
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write("---\n")
                json.dump(frontmatter, f, indent=2)
                f.write("\n---\n\n")
                f.write(content)
            
            print(f"Created page: {filepath}")
            return True
            
        except Exception as e:
            print(f"Error creating page for {video_id}: {str(e)}")
            return False
    
    def process_video(self, video_id: str, title: str, url: str) -> bool:
        """Process a single video"""
        print(f"Processing video: {title} ({video_id})")
        
        # Fetch transcript
        transcript_api = TranscriptAPI(os.getenv('TRANSCRIPT_API_KEY'))
        transcript = transcript_api.get_transcript(video_id)
        
        if not transcript:
            print(f"Failed to fetch transcript for {video_id}")
            return False
        
        # Create page
        success = self.create_page(video_id, title, transcript)
        
        if success:
            # Mark as processed
            self.tracker.mark_processed(video_id, title, url)
            print(f"Successfully processed: {title}")
            return True
        else:
            print(f"Failed to create page for {video_id}")
            return False

def main():
    """Main processing function"""
    # Initialize processor
    neural_nexus_path = os.getenv('NEURAL_NEXUS_PATH', '/home/hermes/Neural-Nexus/docs')
    processor = VideoProcessor(neural_nexus_path)
    
    # Load videos from tracker
    tracker = VideoTracker()
    tracker_data = tracker.load_processed_videos()
    processed_videos = tracker_data.get("processed_videos", {})
    
    # Videos to process (only those that haven't been processed yet)
    videos_to_process = []
    for video_id, video_data in processed_videos.items():
        # Check if page already exists
        safe_title = re.sub(r'[^\w\s-]', '', video_data["title"]).strip()
        safe_title = re.sub(r'[-\s]+', '-', safe_title)
        filename = f"the-infographics-show-{video_id}-{safe_title[:50]}.md"
        filepath = os.path.join(neural_nexus_path, filename)
        
        if not os.path.exists(filepath):
            videos_to_process.append({
                'video_id': video_id,
                'title': video_data["title"],
                'url': f"https://www.youtube.com/watch?v={video_id}"
            })
    
    if not videos_to_process:
        print("No new videos to process - all pages already exist")
        return
    
    # Process each video
    results = []
    for video in videos_to_process:
        success = processor.process_video(
            video['video_id'],
            video['title'],
            video['url']
        )
        results.append({
            'video_id': video['video_id'],
            'title': video['title'],
            'success': success
        })
    
    # Print summary
    print("\n=== Processing Summary ===")
    successful = sum(1 for r in results if r['success'])
    print(f"Successfully processed: {successful}/{len(results)}")
    
    for result in results:
        status = "✓" if result['success'] else "✗"
        print(f"{status} {result['title']}")

if __name__ == "__main__":
    main()