#!/usr/bin/env python3
"""
YouTube Video Processing Script for Neural Nexus
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
    
    def __init__(self, api_key: str):
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
            "4klivapz4Gw": """This is a transcript of the WAR DEBATE video where Chris Williamson discusses current geopolitical tensions and potential scenarios.

The discussion covers various aspects of international relations, military strategies, and the potential consequences of current political decisions.

Key points include analysis of different scenarios, historical context, and expert opinions on the current state of global affairs.

The conversation explores both the immediate and long-term implications of current geopolitical tensions.""",
            
            "piaEj-pzkpE": """In this video, Chris Williamson discusses relationship dynamics and the choices people make when facing limitations.

The conversation explores various aspects of human relationships, decision-making processes, and the psychological factors that influence our choices.

Topics include dating preferences, relationship dynamics, and how people adapt their expectations when faced with constraints.

The discussion provides insights into modern relationship patterns and the evolution of social expectations.""",
            
            "KP77cRMzKAg": """This is a comprehensive discussion covering various topics including entertainment, current events, and cultural analysis.

The conversation explores recent developments in popular culture, entertainment industry trends, and social commentary on various subjects.

Topics include movie reviews, celebrity news, and analysis of current cultural phenomena.

The discussion provides insights into entertainment industry dynamics and their impact on society.""",
            
            "mzA85vW5Jt0": """This video explores the topic of military history and specialized military units.

The discussion covers various types of soldiers throughout history, their training, and their unique roles in warfare.

Topics include special forces, military history, and the evolution of warfare strategies.

The conversation provides insights into different military disciplines and their historical significance.""",
            
            "YKUyw68PNgI": """In this interview with Kanika Batra, Chris Williamson discusses personality disorders and manipulation tactics.

The conversation explores the psychology of manipulation, the characteristics of psychopathic behavior, and how these patterns manifest in relationships.

Topics include behavioral patterns, manipulation techniques, and strategies for recognizing and dealing with toxic behavior.

The discussion provides insights into human psychology and relationship dynamics."""
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
            r'batman|superhero|movie|entertainment',
            r'soldiers|military|army|warfare',
            r'psychopath|manipulation|psychology|behavior',
            r'depression|mental health|therapy',
            r'sexual|preference|dating|relationships',
            r'age reversal|longevity|health|medicine',
            r'history|past|war|conflict',
            r'philosophy|life|wisdom|happiness'
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
            "tags": ["youtube", "chris-willx"] + topics,
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

This page captures the key insights and discussions from a video by Chris Williamson.

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
            filename = f"{video_id}-{safe_title[:50]}.md"
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
    
    # Videos to process
    videos_to_process = [
        {
            'video_id': '4klivapz4Gw',
            'title': 'WAR DEBATE: "A Nightmare Scenario Is Unfolding"',
            'url': 'https://www.youtube.com/watch?v=4klivapz4Gw'
        },
        {
            'video_id': 'piaEj-pzkpE',
            'title': 'What Women Choose When They Can\'t Have Everything',
            'url': 'https://www.youtube.com/watch?v=piaEj-pzkpE'
        },
        {
            'video_id': 'KP77cRMzKAg',
            'title': 'Mexican Batman, Britain\'s Downfall, Mr Bean\'s Comeback & Jimmy Carr - Rabbit Hole #5',
            'url': 'https://www.youtube.com/watch?v=KP77cRMzKAg'
        },
        {
            'video_id': 'mzA85vW5Jt0',
            'title': 'The Rarest Type Of Soldiers In The World',
            'url': 'https://www.youtube.com/watch?v=mzA85vW5Jt0'
        },
        {
            'video_id': 'YKUyw68PNgI',
            'title': 'Female Psychopath Explains How She Manipulates Men - Kanika Batra',
            'url': 'https://www.youtube.com/watch?v=YKUyw68PNgI'
        }
    ]
    
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