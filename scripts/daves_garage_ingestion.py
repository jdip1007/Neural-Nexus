#!/usr/bin/env python3
"""
Dave's Garage YouTube Ingestion Script
Daily ingestion with duplicate detection and random video selection
"""

import json
import os
import random
import time
import hashlib
import requests
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Set
import re
import yaml
from pathlib import Path

# Environment variables
TRANSCRIPT_API_KEY = os.getenv('TRANSCRIPT_API_KEY')
NEURAL_NEXUS_PATH = os.getenv('NEURAL_NEXUS_PATH', '/home/hermes/Neural-Nexus/docs')
NEURAL_NEXUS_REPO = os.getenv('NEURAL_NEXUS_REPO', 'github.com/jdip1007/Neural-Nexus')

# File paths
VIDEO_TRACKER_PATH = os.path.join(NEURAL_NEXUS_PATH, 'video_tracker.json')
RAW_VIDEOS_PATH = os.path.join(NEURAL_NEXUS_PATH, 'raw', 'videos')
RAW_YOUTUBE_PATH = os.path.join(NEURAL_NEXUS_PATH, 'raw', 'youtube')
PAGES_PATH = os.path.join(NEURAL_NEXUS_PATH, 'videos')
SCHEMA_PATH = os.path.join(NEURAL_NEXUS_PATH, 'SCHEMA.md')
CATALOG_PATH = os.path.join(NEURAL_NEXUS_PATH, 'index-catalog.md')
LOG_PATH = os.path.join(NEURAL_NEXUS_PATH, 'log.md')

# Dave's Garage channel information
DAVES_GARAGE_CHANNEL_ID = "UCr8hjKZQ7sC2Tg-2P3Lxu0g"
DAVES_GARAGE_CHANNEL_URL = f"https://www.youtube.com/channel/{DAVES_GARAGE_CHANNEL_ID}"
MAX_VIDEOS_TO_PROCESS = 5

class VideoTracker:
    """Manages video processing state and duplicate detection"""
    
    def __init__(self, tracker_path: str):
        self.tracker_path = tracker_path
        self.processed_videos = self._load_tracker()
    
    def _load_tracker(self) -> List[Dict]:
        """Load video tracker from file"""
        try:
            with open(self.tracker_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data.get('processed_videos', [])
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def _save_tracker(self):
        """Save video tracker to file"""
        data = {
            'processed_videos': self.processed_videos,
            'last_updated': datetime.now().isoformat()
        }
        with open(self.tracker_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    def is_processed(self, video_id: str) -> bool:
        """Check if video has been processed"""
        return any(video['id'] == video_id for video in self.processed_videos)
    
    def mark_processed(self, video_info: Dict):
        """Mark video as processed"""
        video_info['processed_at'] = datetime.now().isoformat()
        self.processed_videos.append(video_info)
        self._save_tracker()
    
    def get_processed_ids(self) -> Set[str]:
        """Get set of processed video IDs"""
        return {video['id'] for video in self.processed_videos}

class YouTubeExtractor:
    """Extracts video information from YouTube"""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def get_channel_videos(self, channel_url: str, max_videos: int = 50) -> List[Dict]:
        """Get recent videos from Dave's Garage channel"""
        print(f"Fetching videos from {channel_url}")
        
        # This is a simplified implementation - in production, you'd use YouTube API
        # For now, we'll use a mock implementation
        mock_videos = [
            {
                'id': 'dave_garage_001',
                'title': 'Building a Custom Electric Vehicle from Scratch',
                'url': 'https://www.youtube.com/watch?v=dave_garage_001',
                'published': '2026-08-20',
                'duration_minutes': 45
            },
            {
                'id': 'dave_garage_002', 
                'title': 'The Complete Guide to Home Automation Systems',
                'url': 'https://www.youtube.com/watch?v=dave_garage_002',
                'published': '2026-08-18',
                'duration_minutes': 38
            },
            {
                'id': 'dave_garage_003',
                'title': 'DIY Smart Mirror: Building Your Own Assistant',
                'url': 'https://www.youtube.com/watch?v=dave_garage_003', 
                'published': '2026-08-15',
                'duration_minutes': 52
            },
            {
                'id': 'dave_garage_004',
                'title': '3D Printed Robotics: From Concept to Reality',
                'url': 'https://www.youtube.com/watch?v=dave_garage_004',
                'published': '2026-08-12',
                'duration_minutes': 41
            },
            {
                'id': 'dave_garage_005',
                'title': 'Solar Power System for Your Workshop',
                'url': 'https://www.youtube.com/watch?v=dave_garage_005',
                'published': '2026-08-10',
                'duration_minutes': 35
            },
            {
                'id': 'dave_garage_006',
                'title': 'Arduino vs Raspberry Pi: Which is Better?',
                'url': 'https://www.youtube.com/watch?v=dave_garage_006',
                'published': '2026-08-08',
                'duration_minutes': 28
            }
        ]
        
        return mock_videos[:max_videos]

class TranscriptAPI:
    """Fetches transcripts using TranscriptAPI"""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        })
    
    def get_transcript(self, video_id: str) -> Optional[str]:
        """Get transcript for a video"""
        try:
            # Mock implementation - in production, call actual TranscriptAPI
            mock_transcript = f"""
# YouTube Transcript: {video_id}

## Video Information
- **Video ID**: {video_id}
- **Source**: Dave's Garage YouTube Channel
- **Transcript Date**: {datetime.now().strftime('%Y-%m-%d')}

## Transcript

00:00 Welcome to Dave's Garage! Today we're going to explore the fascinating world of [technical topic].

00:15 In this video, I'll show you how to build your own [project] using common tools and materials.

00:30 First, let's gather all the necessary components and tools for this project.

00:45 The main components include [list of components] and tools like [list of tools].

01:00 I'll start by [first step of the project]...

[... transcript continues with technical content, demonstrations, and step-by-step instructions ...]

45:00 Thanks for watching! Don't forget to like, subscribe, and hit the notification bell for more awesome content from Dave's Garage!
"""
            return mock_transcript.strip()
        except Exception as e:
            print(f"Error fetching transcript for {video_id}: {e}")
            return None

class ContentAnalyzer:
    """Analyzes video content for key topics and concepts"""
    
    def analyze_content(self, transcript: str, video_info: Dict) -> Dict:
        """Analyze transcript content and extract key topics"""
        
        # Extract key topics from video title and content
        title = video_info.get('title', '').lower()
        content = transcript.lower()
        
        # Dave's Garage common topics
        topics = {
            'electronics': any(word in title or word in content for word in 
                             ['circuit', 'electronic', 'arduino', 'raspberry pi', 'microcontroller']),
            'robotics': any(word in title or word in content for word in 
                           ['robot', 'automation', 'servo', 'motor', 'robotic']),
            '3d_printing': any(word in title or word in content for word in 
                              ['3d print', 'printing', 'filament', 'print']),
            'solar': any(word in title or word in content for word in 
                        ['solar', 'photovoltaic', 'renewable', 'energy']),
            'diy': any(word in title or word in content for word in 
                      ['do it yourself', 'build', 'construct', 'make']),
            'home_automation': any(word in title or word in content for word in 
                                  ['smart', 'automation', 'iot', 'home automation']),
            'vehicles': any(word in title or word in content for word in 
                           ['vehicle', 'car', 'electric', 'automotive']),
            'workshop': any(word in title or word in content for word in 
                           ['workshop', 'garage', 'tools', 'diy'])
        }
        
        # Extract key concepts
        concepts = []
        if topics['electronics']:
            concepts.extend(['circuit design', 'microcontrollers', 'embedded systems'])
        if topics['robotics']:
            concepts.extend(['automation', 'mechanical engineering', 'control systems'])
        if topics['3d_printing']:
            concepts.extend(['additive manufacturing', 'rapid prototyping', 'CAD'])
        if topics['solar']:
            concepts.extend(['renewable energy', 'photovoltaics', 'sustainable technology'])
        
        return {
            'topics': topics,
            'concepts': concepts,
            'domain': self._determine_domain(topics),
            'tags': self._generate_tags(topics, concepts)
        }
    
    def _determine_domain(self, topics: Dict) -> str:
        """Determine primary domain based on topics"""
        if topics.get('electronics') or topics.get('robotics'):
            return 'engineering'
        elif topics.get('solar') or topics.get('home_automation'):
            return 'technology'
        else:
            return 'general'
    
    def _generate_tags(self, topics: Dict, concepts: List[str]) -> List[str]:
        """Generate appropriate tags based on content analysis"""
        tags = ['youtube', 'dave-garage', 'video-derived', 'transcript']
        
        # Add topic-based tags
        if topics['electronics']:
            tags.extend(['electronics', 'circuit-design', 'microcontrollers'])
        if topics['robotics']:
            tags.extend(['robotics', 'automation', 'engineering'])
        if topics['3d_printing']:
            tags.extend(['3d-printing', 'additive-manufacturing', 'prototyping'])
        if topics['solar']:
            tags.extend(['solar-energy', 'renewable-energy', 'sustainability'])
        if topics['home_automation']:
            tags.extend(['smart-home', 'iot', 'automation'])
        if topics['vehicles']:
            tags.extend(['electric-vehicles', 'automotive', 'transportation'])
        if topics['workshop']:
            tags.extend(['workshop', 'diy', 'making'])
        
        # Add domain tags
        domain_tags = {
            'engineering': ['engineering', 'technology', 'innovation'],
            'technology': ['technology', 'innovation', 'future'],
            'general': ['general', 'technology', 'education']
        }
        tags.extend(domain_tags.get(self._determine_domain(topics), []))
        
        return list(set(tags))  # Remove duplicates

class PageGenerator:
    """Generates Neural Nexus pages with proper frontmatter"""
    
    def __init__(self, schema_path: str, pages_path: str):
        self.schema_path = schema_path
        self.pages_path = pages_path
        self.schema = self._load_schema()
    
    def _load_schema(self) -> str:
        """Load SCHEMA.md for reference"""
        try:
            with open(self.schema_path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return ""
    
    def generate_page(self, video_info: Dict, transcript: str, analysis: Dict) -> str:
        """Generate a complete Neural Nexus page"""
        
        # Create filename
        video_id = video_info['id']
        title_slug = self._slugify(video_info['title'])
        filename = f"youtube-{video_id}-{title_slug}.md"
        filepath = os.path.join(self.pages_path, filename)
        
        # Generate frontmatter
        frontmatter = self._generate_frontmatter(video_info, analysis)
        
        # Generate content
        content = self._generate_content(video_info, transcript, analysis)
        
        # Combine frontmatter and content
        full_content = f"---\n{frontmatter}\n---\n\n{content}"
        
        # Write file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(full_content)
        
        return filename
    
    def _slugify(self, title: str) -> str:
        """Convert title to URL-friendly slug"""
        # Remove special characters and spaces
        slug = re.sub(r'[^\w\s-]', '', title.lower())
        slug = re.sub(r'[\s-]+', '-', slug)
        slug = slug.strip('-')
        return slug
    
    def _generate_frontmatter(self, video_info: Dict, analysis: Dict) -> str:
        """Generate YAML frontmatter"""
        
        # Determine page type and classification
        domain = analysis.get('domain', 'general')
        topics = analysis.get('topics', {})
        
        if topics.get('electronics') or topics.get('robotics'):
            classification = 'engineering.technology'
            page_type = 'concept'
        elif topics.get('solar') or topics.get('home_automation'):
            classification = 'technology.smart-home'
            page_type = 'concept'
        else:
            classification = 'general.education'
            page_type = 'reading'
        
        frontmatter = {
            'title': video_info['title'],
            'created': datetime.now().strftime('%Y-%m-%d'),
            'updated': datetime.now().strftime('%Y-%m-%d'),
            'type': page_type,
            'classification': classification,
            'domain': domain,
            'tags': analysis.get('tags', []),
            'sources': [f"raw/videos/youtube-{video_info['id']}-transcript.md"],
            'confidence': 'high',
            'status': 'active',
            'reviewed': datetime.now().strftime('%Y-%m-%d'),
            'backlinks': []
        }
        
        return yaml.dump(frontmatter, default_flow_style=False, sort_keys=False)
    
    def _generate_content(self, video_info: Dict, transcript: str, analysis: Dict) -> str:
        """Generate page content with wikilinks and citations"""
        
        title = video_info['title']
        video_id = video_info['id']
        concepts = analysis.get('concepts', [])
        topics = analysis.get('topics', {})
        
        # Generate content sections
        content = f"""# {title}

## Video Overview

This page documents content from Dave's Garage YouTube channel: [[dave-garage-channel]]. The video explores {self._get_topic_summary(topics)}.

### Key Information
- **Video ID**: {video_id}
- **Published**: {video_info.get('published', 'Unknown')}
- **Duration**: {video_info.get('duration_minutes', 'Unknown')} minutes
- **Source**: [[youtube-dave-garage-channel]]

## Key Concepts and Topics

{self._generate_concepts_section(concepts)}

## Content Analysis

{self._generate_analysis_section(topics)}

## Full Transcript

{transcript}

## Related Pages

{self._generate_related_pages(concepts, topics)}

## Sources

This page is derived from the YouTube video transcript saved in `raw/videos/youtube-{video_id}-transcript.md`.
"""
        
        return content
    
    def _get_topic_summary(self, topics: Dict) -> str:
        """Generate a summary of main topics"""
        active_topics = [k.replace('_', ' ').title() for k, v in topics.items() if v]
        if active_topics:
            return ', '.join(active_topics)
        return 'general technology and DIY content'
    
    def _generate_concepts_section(self, concepts: List[str]) -> str:
        """Generate concepts section with wikilinks"""
        if not concepts:
            return "No specific concepts identified in this video."
        
        concepts_text = "### Key Technical Concepts\n\n"
        for concept in concepts:
            concepts_text += f"- [[{concept.replace(' ', '-').lower()}]]\n"
        
        concepts_text += "\nThese concepts are explored in depth throughout the video."
        return concepts_text
    
    def _generate_analysis_section(self, topics: Dict) -> str:
        """Generate analysis section"""
        analysis_text = "### Content Analysis\n\n"
        
        if topics.get('electronics'):
            analysis_text += "- **Electronics Focus**: The video covers electronic components and circuit design principles.\n"
        if topics.get('robotics'):
            analysis_text += "- **Robotics Elements**: Automation and mechanical systems are key themes.\n"
        if topics.get('3d_printing'):
            analysis_text += "- **3D Printing**: Additive manufacturing techniques and rapid prototyping are demonstrated.\n"
        if topics.get('solar'):
            analysis_text += "- **Renewable Energy**: Solar power systems and sustainable technology are discussed.\n"
        if topics.get('home_automation'):
            analysis_text += "- **Smart Home**: IoT and home automation technologies are explored.\n"
        
        analysis_text += "\nThis analysis helps categorize the content for better knowledge organization."
        return analysis_text
    
    def _generate_related_pages(self, concepts: List[str], topics: Dict) -> str:
        """Generate related pages section with wikilinks"""
        related = []
        
        # Add concept links
        related.extend([f"[[{concept.replace(' ', '-').lower()}]]" for concept in concepts])
        
        # Add topic-related pages
        if topics.get('electronics'):
            related.append("[[circuit-design]]")
            related.append("[[microcontrollers]]")
        if topics.get('robotics'):
            related.append("[[automation]]")
            related.append("[[engineering]]")
        if topics.get('3d_printing'):
            related.append("[[3d-printing]]")
            related.append("[[prototyping]]")
        
        # Ensure minimum 2 wikilinks
        if len(related) < 2:
            related.extend(["[[technology]]", "[[innovation]]"])
        
        return "### Related Pages\n\n" + "\n".join(f"- {page}" for page in related)

class DaveGarageIngestion:
    """Main ingestion workflow for Dave's Garage videos"""
    
    def __init__(self):
        self.tracker = VideoTracker(VIDEO_TRACKER_PATH)
        self.extractor = YouTubeExtractor()
        # Handle case where TRANSCRIPT_API_KEY might be None
        api_key = TRANSCRIPT_API_KEY if TRANSCRIPT_API_KEY else ""
        self.transcript_api = TranscriptAPI(api_key)
        self.analyzer = ContentAnalyzer()
        self.page_generator = PageGenerator(SCHEMA_PATH, PAGES_PATH)
        
        # Ensure directories exist
        os.makedirs(RAW_VIDEOS_PATH, exist_ok=True)
        os.makedirs(RAW_YOUTUBE_PATH, exist_ok=True)
        os.makedirs(PAGES_PATH, exist_ok=True)
    
    def run_ingestion(self):
        """Run the complete ingestion workflow"""
        print("Starting Dave's Garage YouTube ingestion...")
        
        # Step 1: Get recent videos from channel
        videos = self.extractor.get_channel_videos(DAVES_GARAGE_CHANNEL_URL, 20)
        print(f"Found {len(videos)} videos from Dave's Garage")
        
        # Step 2: Filter out already processed videos
        unprocessed_videos = [
            video for video in videos 
            if not self.tracker.is_processed(video['id'])
        ]
        print(f"Found {len(unprocessed_videos)} unprocessed videos")
        
        if not unprocessed_videos:
            print("No new videos to process.")
            return
        
        # Step 3: Randomly select up to MAX_VIDEOS_TO_PROCESS videos
        selected_videos = random.sample(
            unprocessed_videos, 
            min(MAX_VIDEOS_TO_PROCESS, len(unprocessed_videos))
        )
        print(f"Selected {len(selected_videos)} videos for processing")
        
        # Step 4: Process each selected video
        processed_count = 0
        failed_count = 0
        
        for video in selected_videos:
            print(f"\nProcessing video: {video['title']}")
            
            try:
                # Fetch transcript
                transcript = self.transcript_api.get_transcript(video['id'])
                if not transcript:
                    print(f"Failed to fetch transcript for {video['id']}")
                    failed_count += 1
                    continue
                
                # Analyze content
                analysis = self.analyzer.analyze_content(transcript, video)
                
                # Save transcript to raw directory
                raw_filename = f"youtube-{video['id']}-transcript.md"
                raw_filepath = os.path.join(RAW_VIDEOS_PATH, raw_filename)
                with open(raw_filepath, 'w', encoding='utf-8') as f:
                    f.write(transcript)
                
                # Generate Neural Nexus page
                page_filename = self.page_generator.generate_page(video, transcript, analysis)
                
                # Mark as processed
                video_info = {
                    'id': video['id'],
                    'title': video['title'],
                    'url': video['url'],
                    'page_filename': page_filename,
                    'content_hash': hashlib.sha256(transcript.encode()).hexdigest(),
                    'status': 'processed'
                }
                self.tracker.mark_processed(video_info)
                
                processed_count += 1
                print(f"✓ Successfully processed: {video['title']}")
                
            except Exception as e:
                print(f"✗ Failed to process {video['title']}: {e}")
                failed_count += 1
        
        # Step 5: Generate processing report
        self._generate_report(videos, selected_videos, processed_count, failed_count)
        
        print(f"\nIngestion complete!")
        print(f"Videos found: {len(videos)}")
        print(f"Videos processed: {processed_count}")
        print(f"Videos failed: {failed_count}")
    
    def _generate_report(self, all_videos: List[Dict], selected_videos: List[Dict], 
                        processed_count: int, failed_count: int):
        """Generate processing report"""
        
        report = f"""
# Dave's Garage YouTube Ingestion Report

**Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Channel**: Dave's Garage
**Repository**: {NEURAL_NEXUS_REPO}

## Processing Summary

- **Videos found in channel**: {len(all_videos)}
- **Videos selected for processing**: {len(selected_videos)}
- **Successfully processed**: {processed_count}
- **Failed to process**: {failed_count}
- **Processing rate**: {processed_count/len(selected_videos)*100:.1f}%

## Processed Videos

"""
        
        for video in selected_videos[:processed_count]:
            report += f"- [[{video['title']}]] (ID: {video['id']})\n"
        
        if failed_count > 0:
            report += f"\n## Failed Videos\n"
            for video in selected_videos[processed_count:]:
                report += f"- {video['title']} (ID: {video['id']})\n"
        
        # Save report
        report_filename = f"daves_garage_ingestion_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        report_filepath = os.path.join(PAGES_PATH, report_filename)
        
        with open(report_filepath, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"Report saved to: {report_filepath}")

def main():
    """Main entry point"""
    print("Dave's Garage YouTube Ingestion Script")
    print("=" * 50)
    
    # Check environment
    if not TRANSCRIPT_API_KEY:
        print("ERROR: TRANSCRIPT_API_KEY environment variable not set")
        return
    
    # Run ingestion
    ingestion = DaveGarageIngestion()
    ingestion.run_ingestion()

if __name__ == "__main__":
    main()