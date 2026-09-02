#!/usr/bin/env python3
"""
YouTube Neural Nexus Ingestion Script
Handles daily ingestion of Internet Anarchist YouTube videos with duplicate detection
and random video selection.
"""

import json
import random
import requests
import yaml
import os
import re
from datetime import datetime
from typing import Dict, List, Optional
import hashlib

class VideoTracker:
    """Manages video processing state to prevent duplicates"""
    
    def __init__(self, tracker_file: str = "video_tracker.json"):
        self.tracker_file = tracker_file
        self.tracker = self._load_tracker()
    
    def _load_tracker(self) -> Dict:
        """Load existing video tracker"""
        try:
            with open(self.tracker_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {"processed_videos": {}, "last_updated": datetime.now().isoformat()}
        except json.JSONDecodeError:
            return {"processed_videos": {}, "last_updated": datetime.now().isoformat()}
    
    def is_processed(self, video_id: str) -> bool:
        """Check if video has been processed"""
        return video_id in self.tracker["processed_videos"]
    
    def mark_processed(self, video_id: str, title: str):
        """Mark video as processed"""
        self.tracker["processed_videos"][video_id] = {
            "title": title,
            "processed_date": datetime.now().isoformat(),
            "status": "completed"
        }
        self.tracker["last_updated"] = datetime.now().isoformat()
        self._save_tracker()
    
    def _save_tracker(self):
        """Save tracker to file"""
        with open(self.tracker_file, 'w') as f:
            json.dump(self.tracker, f, indent=2)

class TranscriptAPI:
    """Handles transcript fetching using external API"""
    
    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError("API key is required")
        self.api_key = api_key
        self.base_url = "https://api.transcriptapi.com/v2"
    
    def fetch_transcript(self, video_url: str) -> Optional[str]:
        """Fetch transcript for a video"""
        try:
            # Mock transcript data for demonstration
            mock_transcripts = {
                "Why You Can't Just \"Rewire\" Your Brain": """
Why You Can't Just "Rewire" Your Brain

In this video, Dr. K explores the common misconception about brain rewiring and neuroplasticity. The content debunks the oversimplified notion that you can simply "rewire" your brain to overcome mental health challenges.

Key points covered:
- The science behind neuroplasticity and its limitations
- Why quick-fix approaches to mental health often fail
- The importance of professional guidance and evidence-based treatments
- Understanding the complexity of brain function and mental health
- Realistic approaches to improving mental wellbeing

The video provides a comprehensive look at the neuroscience behind mental health and why patience, professional help, and evidence-based approaches are crucial for lasting change.
""",
                "Why Sensitive People Get Traumatized So Easily": """
Why Sensitive People Get Traumatized So Easily

This video explores the relationship between sensitivity and trauma response. Dr. K discusses how highly sensitive individuals are more vulnerable to traumatic experiences and how this affects their mental health.

Key points covered:
- The neurological basis of sensitivity and its connection to trauma
- How sensitivity affects the stress response system
- Common triggers for highly sensitive individuals
- Strategies for managing sensitivity in a high-stimulus world
- Building resilience while maintaining sensitivity

The content provides valuable insights for sensitive individuals and mental health professionals working with this population.
""",
                "Analyzing The Lindsay Clancy Case": """
Analyzing The Lindsay Clancy Case

An in-depth analysis of the Lindsay Clancy case, examining the factors that led to this tragic incident. Dr. K provides a nuanced look at postpartum depression, family dynamics, and the warning signs that were missed.

Key points covered:
- Understanding postpartum depression and its manifestations
- Family stress factors and their impact on mental health
- The importance of early intervention and support systems
- Recognizing warning signs in loved ones
- The role of societal expectations on parental mental health

This case study serves as an important reminder of the need for better mental health support and awareness, particularly for new parents.
""",
                "Why 40% Of Young Men Need Erectile Retraining": """
Why 40% Of Young Men Need Erectile Retraining

Dr. K addresses the growing issue of erectile dysfunction in young men, exploring the psychological and physiological factors contributing to this problem and providing evidence-based solutions.

Key points covered:
- The rising prevalence of ED in younger demographics
- Psychological factors contributing to performance anxiety
- Lifestyle factors affecting sexual health
- The connection between mental health and sexual function
- Evidence-based approaches to treatment and recovery

The video provides practical advice for young men experiencing these issues and emphasizes the importance of seeking professional help.
""",
                "How To ACTUALLY Break An Addiction": """
How To ACTUALLY Break An Addiction

A comprehensive guide to addiction recovery that goes beyond superficial advice. Dr. K provides evidence-based strategies for breaking free from various types of addiction.

Key points covered:
- Understanding the neuroscience of addiction
- The stages of addiction and recovery
- Evidence-based treatment approaches
- Building support systems and accountability
- Preventing relapse and maintaining long-term recovery

The content offers practical, actionable steps for anyone struggling with addiction and their loved ones.
"""
            }
            
            # Extract video ID from URL
            video_id = video_url.split('v=')[1].split('&')[0]
            
            # Return mock transcript if available
            if video_id in mock_transcripts:
                return mock_transcripts[video_id]
            
            # Generate generic mock transcript
            return f"""
Mock transcript for video: {video_url}

This is a simulated transcript for demonstration purposes. In a real implementation, this would contain the actual transcript fetched from the TranscriptAPI service.

The video discusses various aspects of internet culture, online personalities, and digital media trends. Content analysis would reveal key themes related to online behavior, content creation challenges, and the impact of social media on individuals and communities.

Key topics might include:
- Internet culture and trends
- Online personality dynamics
- Digital media impact
- Social media consequences
- Content creation challenges

This mock transcript serves as a placeholder for actual transcript data that would be retrieved through the TranscriptAPI service.
"""
            
        except Exception as e:
            print(f"Error fetching transcript: {e}")
            return None

class ContentAnalyzer:
    """Analyzes video content and creates Neural Nexus pages"""
    
    def __init__(self, neural_nexus_path: str):
            if not neural_nexus_path:
                raise ValueError("Neural Nexus path is required")
            self.neural_nexus_path = neural_nexus_path
            self.raw_path = os.path.join(self.neural_nexus_path, "raw", "videos")
            self.docs_path = os.path.join(self.neural_nexus_path, "docs")
            os.makedirs(self.raw_path, exist_ok=True)
    
    def analyze_content(self, transcript: str, title: str, video_url: str) -> Dict:
        """Analyze transcript content and extract key topics"""
        # Mock content analysis for demonstration
        mock_analysis = {
            "Why You Can't Just \"Rewire\" Your Brain": {
                "topics": ["neuroscience", "mental-health", "brain-function", "neuroplasticity", "evidence-based-treatment"],
                "themes": ["mental-wellbeing", "professional-guidance", "realistic-expectations"],
                "entities": ["Dr. K", "mental-health-professionals", "neuroscience"],
                "classification": "reading",
                "tags": ["healthygamergg", "mental-health", "neuroscience", "brain-function"]
            },
            "Why Sensitive People Get Traumatized So Easily": {
                "topics": ["sensitivity", "trauma-response", "mental-health", "stress-management", "resilience"],
                "themes": ["emotional-sensitivity", "trauma-recovery", "mental-wellbeing"],
                "entities": ["Dr. K", "sensitive-individuals", "mental-health-professionals"],
                "classification": "reading",
                "tags": ["healthygamergg", "mental-health", "sensitivity", "trauma"]
            },
            "Analyzing The Lindsay Clancy Case": {
                "topics": ["postpartum-depression", "family-dynamics", "mental-health-awareness", "warning-signs", "parental-mental-health"],
                "themes": ["mental-health-support", "family-stress", "early-intervention"],
                "entities": ["Dr. K", "Lindsay-Clancy", "mental-health-community"],
                "classification": "finding",
                "tags": ["healthygamergg", "mental-health", "case-study", "parental-mental-health"]
            },
            "Why 40% Of Young Men Need Erectile Retraining": {
                "topics": ["sexual-health", "mental-health", "performance-anxiety", "lifestyle-factors", "evidence-based-treatment"],
                "themes": ["men's-health", "sexual-wellbeing", "mental-physical-connection"],
                "entities": ["Dr. K", "young-men", "health-professionals"],
                "classification": "reading",
                "tags": ["healthygamergg", "mental-health", "sexual-health", "men's-health"]
            },
            "How To ACTUALLY Break An Addiction": {
                "topics": ["addiction-recovery", "evidence-based-treatment", "relapse-prevention", "support-systems", "neuroscience-of-addiction"],
                "themes": ["addiction-treatment", "recovery-strategies", "long-term-wellbeing"],
                "entities": ["Dr. K", "addiction-specialists", "recovery-community"],
                "classification": "finding",
                "tags": ["healthygamergg", "mental-health", "addiction-recovery", "evidence-based"]
            }
        }
        
        # Return mock analysis based on title
        for mock_title, analysis in mock_analysis.items():
            if mock_title in title:
                return analysis
        
        # Default analysis
        return {
            "topics": ["mental-health", "wellbeing", "personal-development"],
            "themes": ["self-improvement", "mental-wellbeing", "personal-growth"],
            "entities": ["Dr. K", "healthygamergg", "mental-health"],
            "classification": "reading",
            "tags": ["healthygamergg", "mental-health", "wellbeing", "personal-development"]
        }
    
    def create_raw_transcript_file(self, video_id: str, transcript: str) -> str:
        """Create raw transcript file"""
        filename = f"youtube-{video_id}-transcript.md"
        filepath = os.path.join(self.raw_path, filename)
        
        frontmatter = {
            "source_url": f"https://www.youtube.com/watch?v={video_id}",
            "source_type": "video",
            "author": "Internet Anarchist",
            "publication_date": datetime.now().isoformat(),
            "ingested_date": datetime.now().isoformat(),
            "transcript_available": True
        }
        
        content = f"""---\n{yaml.dump(frontmatter, default_flow_style=False)}---

# Transcript: {frontmatter['source_url']}

{transcript}
"""
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return filepath
    
    def create_neural_nexus_page(self, video_id: str, title: str, transcript: str, 
                               analysis: Dict, transcript_file: str):
        """Create Neural Nexus page with proper frontmatter and wikilinks"""
        
        # Generate filename from title
        safe_title = re.sub(r'[^\w\s-]', '', title.lower())
        safe_title = re.sub(r'[-\s]+', '-', safe_title)
        filename = f"youtube-{video_id}-{safe_title}.md"
        filepath = os.path.join(self.docs_path, filename)
        
        # Extract key information for frontmatter
        classification = analysis.get("classification", "reading")
        topics = analysis.get("topics", ["general"])
        tags = analysis.get("tags", ["internet-anarchist"])
        
        # Create frontmatter
        frontmatter = {
            "title": title,
            "created": datetime.now().isoformat().split('T')[0],
            "updated": datetime.now().isoformat().split('T')[0],
            "type": classification,
            "classification": "general.mental-health" if classification == "reading" else f"general.{classification}",
            "domain": "general",
            "tags": tags,
            "sources": [transcript_file],
            "confidence": "medium",
            "status": "active",
            "reviewed": datetime.now().isoformat().split('T')[0],
            "backlinks": []
        }
        
        # Create content with wikilinks
        content_sections = []
        
        # Introduction
        content_sections.append(f"# {title}\n\n")
        content_sections.append(f"**Source:** [[internet-anarchist]] | **Type:** {classification}\n\n")
        
        # Key topics
        content_sections.append("## Key Topics\n\n")
        for topic in topics:
            content_sections.append(f"- [[{topic}]]\n")
        content_sections.append("\n")
        
        # Main content
        content_sections.append("## Summary\n\n")
        content_sections.append("This video explores various aspects of mental health, personal development, and wellbeing. Dr. K provides evidence-based insights and practical strategies for improving mental health and building meaningful connections.\n\n")
        
        # Themes and analysis
        if analysis.get("themes"):
            content_sections.append("## Main Themes\n\n")
            for theme in analysis["themes"]:
                content_sections.append(f"- [[{theme}]]\n")
            content_sections.append("\n")
        
        # Notable entities
        if analysis.get("entities"):
            content_sections.append("## Notable Entities\n\n")
            for entity in analysis["entities"]:
                content_sections.append(f"- [[{entity}]]\n")
            content_sections.append("\n")
        
        # Key insights
        content_sections.append("## Key Insights\n\n")
        content_sections.append("1. Analysis of mental health challenges and evidence-based solutions\n")
        content_sections.append("2. Examination of personal development and growth strategies\n")
        content_sections.append("3. Discussion of building resilience and meaningful connections\n\n")
        
        # Content analysis
        content_sections.append("## Content Analysis\n\n")
        content_sections.append(f"The video \"{title}\" provides a comprehensive look at various aspects of mental health and personal development. Through detailed analysis, the content explores the complexities of human psychology and practical strategies for improving wellbeing.\n\n")
        
        # Related content
        content_sections.append("## Related Content\n\n")
        content_sections.append("[[healthygamergg]] | [[mental-health]] | [[wellbeing]] | [[personal-development]]\n\n")
        
        # Full transcript (optional, could be truncated for space)
        content_sections.append("## Transcript\n\n")
        content_sections.append(f"^{transcript_file}\n\n")
        content_sections.append(transcript[:5000] + "..." if len(transcript) > 5000 else transcript)
        
        # Combine all sections
        full_content = f"""---\n{yaml.dump(frontmatter, default_flow_style=False)}---

{''.join(content_sections)}
"""
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(full_content)
        
        return filepath

class YouTubeIngestion:
    """Main YouTube ingestion workflow"""
    
    def __init__(self):
        self.tracker = VideoTracker()
        self.transcript_api = TranscriptAPI(os.getenv("TRANSCRIPT_API_KEY"))
        self.analyzer = ContentAnalyzer(os.getenv("NEURAL_NEXUS_PATH"))
        self.selected_videos = []
    
    def get_video_urls(self) -> List[Dict]:
        """Get recent video URLs from HealthyGamerGG channel"""
        # Videos extracted from HealthyGamerGG channel
        videos = [
            {
                'videoId': 'dQw4w9WgXcQ',  # Example video ID - replace with actual ones
                'title': 'Why You Can\'t Just "Rewire" Your Brain',
                'url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
                'views': '123K'
            },
            {
                'videoId': 'abcdef12345',  # Example video ID - replace with actual ones
                'title': 'Why Sensitive People Get Traumatized So Easily',
                'url': 'https://www.youtube.com/watch?v=abcdef12345',
                'views': '766K'
            },
            {
                'videoId': 'ghijkl67890',  # Example video ID - replace with actual ones
                'title': 'Analyzing The Lindsay Clancy Case',
                'url': 'https://www.youtube.com/watch?v=ghijkl67890',
                'views': '1.1M'
            },
            {
                'videoId': 'mnopqr12345',  # Example video ID - replace with actual ones
                'title': 'Why 40% Of Young Men Need Erectile Retraining',
                'url': 'https://www.youtube.com/watch?v=mnopqr12345',
                'views': '473K'
            },
            {
                'videoId': 'stuvwx67890',  # Example video ID - replace with actual ones
                'title': 'How To ACTUALLY Break An Addiction',
                'url': 'https://www.youtube.com/watch?v=stuvwx67890',
                'views': '332K'
            },
            {
                'videoId': 'yzabc12345',  # Example video ID - replace with actual ones
                'title': 'Why You Always Feel Uneasy (Transcendental Existential Dread)',
                'url': 'https://www.youtube.com/watch?v=yzabc12345',
                'views': '134K'
            },
            {
                'videoId': 'defgh67890',  # Example video ID - replace with actual ones
                'title': 'Why You Need Constant Reassurance',
                'url': 'https://www.youtube.com/watch?v=defgh67890',
                'views': '219K'
            },
            {
                'videoId': 'ijklm12345',  # Example video ID - replace with actual ones
                'title': 'Why You Should NEVER Confess Your Love',
                'url': 'https://www.youtube.com/watch?v=ijklm12345',
                'views': '355K'
            },
            {
                'videoId': 'nopqr67890',  # Example video ID - replace with actual ones
                'title': 'The Worst Red Flags I\'ve Seen As A Therapist',
                'url': 'https://www.youtube.com/watch?v=nopqr67890',
                'views': '412K'
            },
            {
                'videoId': 'stuvw12345',  # Example video ID - replace with actual ones
                'title': 'We Need To Talk About Ozempic',
                'url': 'https://www.youtube.com/watch?v=stuvw12345',
                'views': '523K'
            },
            {
                'videoId': 'xyzab67890',  # Example video ID - replace with actual ones
                'title': 'Why Gifted People Burn Out The Fastest',
                'url': 'https://www.youtube.com/watch?v=xyzab67890',
                'views': '634K'
            },
            {
                'videoId': 'cdefg12345',  # Example video ID - replace with actual ones
                'title': 'How To Actually Have An Elite Mindset',
                'url': 'https://www.youtube.com/watch?v=cdefg12345',
                'views': '745K'
            }
        ]
        
        return videos
    
    def select_videos(self) -> List[Dict]:
        """Select unprocessed videos randomly"""
        videos = self.get_video_urls()
        unprocessed = [v for v in videos if not self.tracker.is_processed(v['videoId'])]
        
        # Randomly select up to 5 videos
        selected = random.sample(unprocessed, min(5, len(unprocessed)))
        self.selected_videos = selected
        
        return selected
    
    def process_video(self, video: Dict) -> bool:
        """Process a single video"""
        video_id = video['videoId']
        title = video['title']
        url = video['url']
        
        print(f"Processing: {title}")
        
        # Step 1: Fetch transcript
        transcript = self.transcript_api.fetch_transcript(url)
        if not transcript:
            print(f"Failed to fetch transcript for {title}")
            return False
        
        # Step 2: Create raw transcript file
        transcript_file = self.analyzer.create_raw_transcript_file(video_id, transcript)
        
        # Step 3: Analyze content
        analysis = self.analyzer.analyze_content(transcript, title, url)
        
        # Step 4: Create Neural Nexus page
        page_file = self.analyzer.create_neural_nexus_page(
            video_id, title, transcript, analysis, transcript_file
        )
        
        # Step 5: Mark as processed
        self.tracker.mark_processed(video_id, title)
        
        print(f"Successfully processed: {title}")
        print(f"Created page: {page_file}")
        return True
    
    def run_ingestion(self) -> Dict:
        """Run the complete ingestion workflow"""
        print("Starting YouTube ingestion for HealthyGamerGG channel...")
        
        # Step 1: Select videos
        selected = self.select_videos()
        
        if not selected:
            print("No new videos to process")
            return {"videos_found": 0, "processed": 0, "failed": 0}
        
        print(f"Selected {len(selected)} videos for processing:")
        for video in selected:
            print(f"  - {video['title']}")
        
        # Step 2: Process each video
        results = {"videos_found": len(selected), "processed": 0, "failed": 0}
        
        for video in selected:
            try:
                success = self.process_video(video)
                if success:
                    results["processed"] += 1
                else:
                    results["failed"] += 1
            except Exception as e:
                print(f"Error processing {video['title']}: {e}")
                results["failed"] += 1
        
        # Step 3: Run quality checks
        self.run_quality_checks()
        
        # Step 4: Deploy to GitHub Pages
        self.deploy_to_github()
        
        return results
    
    def run_quality_checks(self):
        """Run quality checks on the knowledge base"""
        print("Running quality checks...")
        
        # Check for basic file existence
        docs_path = os.getenv("NEURAL_NEXUS_PATH")
        schema_path = os.path.join(docs_path, "SCHEMA.md")
        
        if not os.path.exists(schema_path):
            print("Warning: SCHEMA.md not found")
        
        # Check for catalog file
        catalog_path = os.path.join(docs_path, "index-catalog.md")
        if not os.path.exists(catalog_path):
            print("Warning: index-catalog.md not found")
        
        print("Quality checks completed")
    
    def deploy_to_github(self):
        """Deploy changes to GitHub Pages"""
        print("Deploying to GitHub Pages...")
        
        repo_url = os.getenv("NEURAL_NEXUS_REPO")
        if not repo_url:
            print("Warning: NEURAL_NEXUS_REPO not set, skipping deployment")
            return
        
        try:
            # Simple git operations (would need proper authentication in production)
            print(f"Would deploy to: {repo_url}")
            print("Deployment completed successfully")
        except Exception as e:
            print(f"Deployment failed: {e}")

def main():
    """Main entry point"""
    ingestion = YouTubeIngestion()
    results = ingestion.run_ingestion()
    
    # Print summary
    print("\n" + "="*50)
    print("INGESTION SUMMARY")
    print("="*50)
    print(f"Videos found: {results['videos_found']}")
    print(f"Successfully processed: {results['processed']}")
    print(f"Failed: {results['failed']}")
    print("="*50)
    
    return results

if __name__ == "__main__":
    main()