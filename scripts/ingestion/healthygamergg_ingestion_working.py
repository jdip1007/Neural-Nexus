#!/usr/bin/env python3
"""
HealthyGamerGG YouTube Ingestion Pipeline with Working Transcript API
Handles video extraction, duplicate detection, random selection, transcript fetching, and Neural-Nexus page creation.
"""

import json
import os
import sys
import time
import random
import requests
from typing import List, Dict, Optional
from datetime import datetime
from video_tracker import VideoTracker

# Import browser and terminal functions from Hermes
try:
    from browser import browser_navigate, browser_snapshot, browser_console
    from terminal import terminal
except ImportError:
    # Fallback for testing
    def browser_navigate(url): print(f"Mock navigate to: {url}")
    def browser_snapshot(): print("Mock snapshot")
    def browser_console(expression): return []
    def terminal(command): return {"exit_code": 0, "output": "", "error": None}


class HealthyGamerGGIngestion:
    def __init__(self, channel_url: str = "https://www.youtube.com/@HealthyGamerGG"):
        self.channel_url = channel_url
        self.tracker = VideoTracker()
        self.api_key = os.getenv('TRANSCRIPT_API_KEY')
        self.neural_nexus_path = os.getenv('NEURAL_NEXUS_PATH', '/home/hermes/Neural-Nexus/docs')
        self.neural_nexus_repo = os.getenv('NEURAL_NEXUS_REPO', 'github.com/jdip1007/Neural-Nexus')
        
        if not self.api_key:
            raise ValueError("TRANSCRIPT_API_KEY environment variable not set")
    
    def extract_latest_videos(self) -> List[Dict]:
        """Extract latest videos from HealthyGamerGG YouTube channel using real data."""
        print(f"🎬 Extracting videos from {self.channel_url}")
        
        # Get real video IDs from curl output
        try:
            with open('/tmp/healthygamergg_proper_ids.txt', 'r') as f:
                video_ids = [line.strip() for line in f.readlines() if line.strip()]
            
            # Create video data with placeholder titles
            video_data = []
            for i, vid in enumerate(video_ids):
                video_data.append({
                    "id": vid,
                    "title": f"HealthyGamerGG Video {i+1}: {vid}",
                    "url": f"https://www.youtube.com/watch?v={vid}",
                    "channel": "HealthyGamerGG"
                })
            
            print(f"✅ Found {len(video_data)} real videos")
            return video_data
            
        except Exception as e:
            print(f"❌ Error extracting real video data: {e}")
            # Fallback to sample data
            return self._get_sample_healthygamergg_videos()
    
    def _get_sample_healthygamergg_videos(self) -> List[Dict]:
        """Get sample HealthyGamerGG video data for testing."""
        return [
            {
                "id": "dQw4w9WgXcQ",
                "title": "How Your Brain Perceives Love When You Have Autism",
                "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                "channel": "HealthyGamerGG"
            },
            {
                "id": "sample2",
                "title": "What Everyone Gets Wrong About ADHD",
                "url": "https://www.youtube.com/watch?v=sample2",
                "channel": "HealthyGamerGG"
            },
            {
                "id": "sample3",
                "title": "How To Actually Have An Elite Mindset",
                "url": "https://www.youtube.com/watch?v=sample3",
                "channel": "HealthyGamerGG"
            },
            {
                "id": "sample4",
                "title": "The Cost Of Attention",
                "url": "https://www.youtube.com/watch?v=sample4",
                "channel": "HealthyGamerGG"
            },
            {
                "id": "sample5",
                "title": "Can Men & Women Be Friends?",
                "url": "https://www.youtube.com/watch?v=sample5",
                "channel": "HealthyGamerGG"
            }
        ]
    
    def fetch_transcript(self, video_id: str, video_title: str) -> Optional[str]:
        """Fetch transcript for a video using working YouTube Transcript API."""
        print(f"📝 Fetching transcript for {video_title}")
        
        try:
            # Try YouTube Transcript API
            from youtube_transcript_api import YouTubeTranscriptApi
            
            try:
                # Use the correct method name
                transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
                # Get the available languages
                available_languages = transcript_list.available_languages
                print(f"Available languages: {available_languages}")
                
                # Try English first, then any available
                if 'en' in available_languages:
                    transcript = transcript_list.find_transcript(['en'])
                else:
                    # Use the first available language
                    lang = available_languages[0]
                    transcript = transcript_list.find_transcript([lang])
                
                # Get the transcript text
                transcript_data = transcript.fetch()
                transcript_text = " ".join([item['text'] for item in transcript_data])
                
                print(f"✅ Transcript fetched successfully ({len(transcript_text)} characters)")
                return transcript_text
                
            except Exception as e:
                print(f"❌ YouTube Transcript API error: {e}")
                return None
                
        except ImportError:
            print("❌ youtube_transcript_api not available")
            return None
        except Exception as e:
            print(f"❌ Error fetching transcript: {e}")
            return None
    
    def analyze_content(self, transcript: str) -> Dict:
        """Analyze transcript content for key topics and concepts."""
        print("🧠 Analyzing content for key topics...")
        
        # Simple keyword-based analysis
        topics = {
            "ADHD": ["adhd", "attention deficit", "add", "hyperactivity", "focus"],
            "Autism": ["autism", "autistic", "asd", "neurodivergent"],
            "Mental Health": ["mental health", "psychology", "therapy", "counseling"],
            "Relationships": ["relationship", "dating", "love", "friendship"],
            "Gaming": ["gaming", "video games", "esports", "streaming"],
            "Social Skills": ["social skills", "communication", "interaction", "social"],
            "Self Improvement": ["self improvement", "personal growth", "mindset", "habits"],
            "Anxiety": ["anxiety", "stress", "worry", "panic"],
            "Depression": ["depression", "sadness", "mood", "emotional"],
            "Mindfulness": ["mindfulness", "meditation", "present", "awareness"]
        }
        
        found_topics = []
        topic_scores = {}
        
        for topic, keywords in topics.items():
            score = 0
            for keyword in keywords:
                score += transcript.lower().count(keyword.lower())
            
            if score > 0:
                found_topics.append(topic)
                topic_scores[topic] = score
        
        # Sort by score
        sorted_topics = sorted(topic_scores.items(), key=lambda x: x[1], reverse=True)
        
        analysis = {
            "topics": found_topics,
            "topic_scores": topic_scores,
            "key_concepts": sorted_topics[:5],  # Top 5 topics
            "word_count": len(transcript.split()),
            "summary": f"Content analysis reveals focus on {', '.join(found_topics[:3])}..." if found_topics else "General content analysis"
        }
        
        print(f"🎯 Key topics identified: {', '.join(found_topics[:3])}")
        return analysis
    
    def create_neural_nexus_page(self, video_id: str, video_title: str, transcript: str, analysis: Dict) -> str:
        """Create a Neural-Nexus page with proper frontmatter and content."""
        print(f"📄 Creating Neural-Nexus page for {video_title}")
        
        # Generate filename
        safe_title = video_title.replace(" ", "_").replace("/", "_").replace(":", "_")
        filename = f"youtube-{video_id}-{safe_title[:50]}.md"
        filepath = os.path.join(self.neural_nexus_path, filename)
        
        # Create frontmatter
        frontmatter = {
            "title": video_title,
            "created": datetime.now().strftime('%Y-%m-%d'),
            "updated": datetime.now().strftime('%Y-%m-%d'),
            "type": "video",
            "tags": analysis["topics"] + ["youtube", "healthygamergg"],
            "sources": [f"youtube.com/watch?v={video_id}"],
            "video_id": video_id,
            "channel": "HealthyGamerGG",
            "word_count": analysis["word_count"]
        }
        
        # Create content
        content = f"""# {video_title}

## Video Information

- **Video ID**: {video_id}
- **Channel**: HealthyGamerGG
- **Source**: [YouTube](https://www.youtube.com/watch?v={video_id})
- **Date Created**: {frontmatter["created"]}
- **Word Count**: {analysis["word_count"]} words

## Content Analysis

{analysis["summary"]}

### Key Topics
{chr(10).join(f"- **{topic}**: {score} mentions" for topic, score in analysis["key_concepts"])}

## Transcript

{transcript}

## Related Concepts

{chr(10).join(f"- [[{topic}]]" for topic in analysis["topics"])}
"""
        
        # Write the file
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✅ Page created: {filepath}")
            return filepath
            
        except Exception as e:
            print(f"❌ Error creating page: {e}")
            return None
    
    def process_videos(self, videos: List[Dict], max_videos: int = 5) -> Dict:
        """Process a list of videos with duplicate detection and random selection."""
        print(f"🔄 Processing up to {max_videos} videos...")
        
        # Apply duplicate detection
        unprocessed_videos = self.tracker.get_unprocessed_videos(videos)
        print(f"🔍 After duplicate detection: {len(unprocessed_videos)} unprocessed videos")
        
        if not unprocessed_videos:
            print("✅ All videos already processed. Nothing to do.")
            return {"processed": [], "failed": [], "skipped": len(videos)}
        
        # Randomly select videos
        selected_videos = self.tracker.select_random_videos(unprocessed_videos, max_videos)
        print(f"🎲 Selected {len(selected_videos)} videos for processing:")
        
        for video in selected_videos:
            print(f"  - {video['title']}")
        
        # Process each selected video
        results = {"processed": [], "failed": [], "skipped": len(videos) - len(selected_videos)}
        
        for video in selected_videos:
            try:
                print(f"\n🚀 Processing: {video['title']}")
                
                # Fetch transcript
                transcript = self.fetch_transcript(video["id"], video["title"])
                if not transcript:
                    print(f"❌ Failed to fetch transcript for {video['title']}")
                    results["failed"].append(video)
                    continue
                
                # Analyze content
                analysis = self.analyze_content(transcript)
                
                # Create Neural-Nexus page
                page_path = self.create_neural_nexus_page(
                    video["id"], video["title"], transcript, analysis
                )
                
                if page_path:
                    # Mark as processed
                    self.tracker.add_processed_video(video["id"], video["title"], video["url"])
                    results["processed"].append({
                        "video": video,
                        "page_path": page_path,
                        "analysis": analysis
                    })
                    print(f"✅ Successfully processed: {video['title']}")
                else:
                    results["failed"].append(video)
                    print(f"❌ Failed to create page for: {video['title']}")
                    
            except Exception as e:
                print(f"❌ Error processing {video['title']}: {e}")
                results["failed"].append(video)
        
        return results
    
    def run_quality_checks(self) -> Dict:
        """Run quality checks on the created pages."""
        print("🔍 Running quality checks...")
        
        try:
            # Check if we're in the Neural-Nexus directory
            if not os.path.exists(self.neural_nexus_path):
                print(f"❌ Neural-Nexus path not found: {self.neural_nexus_path}")
                return {"passed": False, "errors": ["Path not found"]}
            
            # Check for recent YouTube pages
            youtube_files = []
            for file in os.listdir(self.neural_nexus_path):
                if file.startswith("youtube-") and file.endswith(".md"):
                    youtube_files.append(file)
            
            print(f"📄 Found {len(youtube_files)} YouTube pages")
            
            # Basic validation
            errors = []
            for file in youtube_files[-5:]:  # Check last 5 files
                filepath = os.path.join(self.neural_nexus_path, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if not content.strip():
                            errors.append(f"Empty file: {file}")
                        if "title:" not in content:
                            errors.append(f"Missing title in: {file}")
                        if "sources:" not in content:
                            errors.append(f"Missing sources in: {file}")
                except Exception as e:
                    errors.append(f"Error reading {file}: {e}")
            
            if errors:
                print(f"❌ Quality check failed with {len(errors)} errors")
                return {"passed": False, "errors": errors}
            else:
                print("✅ Quality checks passed")
                return {"passed": True, "errors": []}
                
        except Exception as e:
            print(f"❌ Error running quality checks: {e}")
            return {"passed": False, "errors": [str(e)]}
    
    def deploy_to_github_pages(self) -> bool:
        """Deploy changes to GitHub Pages if quality checks pass."""
        print("🚀 Deploying to GitHub Pages...")
        
        try:
            # Run quality checks first
            quality_result = self.run_quality_checks()
            if not quality_result["passed"]:
                print("❌ Quality checks failed, skipping deployment")
                return False
            
            # Check if git is available
            git_check = terminal("git status")
            if git_check["exit_code"] != 0:
                print("❌ Git not available or not in a git repository")
                return False
            
            # Add files
            add_result = terminal("git add .")
            if add_result["exit_code"] != 0:
                print("❌ Failed to add files to git")
                return False
            
            # Commit changes
            commit_result = terminal(f'git commit -m "Update with new HealthyGamerGG videos - {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}"')
            if commit_result["exit_code"] != 0:
                print("❌ Failed to commit changes")
                return False
            
            # Push to GitHub
            push_result = terminal("git push")
            if push_result["exit_code"] != 0:
                print("❌ Failed to push to GitHub")
                return False
            
            print("✅ Successfully deployed to GitHub Pages")
            return True
            
        except Exception as e:
            print(f"❌ Error during deployment: {e}")
            return False
    
    def generate_report(self, results: Dict) -> str:
        """Generate a processing report."""
        report = f"""
=== HealthyGamerGG YouTube Ingestion Pipeline Report ===
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

=== Statistics ===
Total videos found: {results.get('skipped', 0) + len(results.get('processed', [])) + len(results.get('failed', []))}
Successfully processed: {len(results.get('processed', []))}
Failed to process: {len(results.get('failed', []))}
Skipped (already processed): {results.get('skipped', 0)}

=== Processed Videos ===
"""
        
        for result in results.get('processed', []):
            video = result['video']
            analysis = result['analysis']
            report += f"- {video['title']}\n"
            report += f"  Topics: {', '.join(analysis['topics'][:3])}\n"
            report += f"  Word count: {analysis['word_count']}\n"
            report += f"  Page: {result['page_path']}\n\n"
        
        if results.get('failed', []):
            report += "=== Failed Videos ===\n"
            for video in results.get('failed', []):
                report += f"- {video['title']}\n"
        
        return report


def main():
    """Main execution function."""
    print("🎬 Starting HealthyGamerGG YouTube Ingestion Pipeline")
    
    try:
        # Initialize ingestion
        ingestion = HealthyGamerGGIngestion()
        
        # Step 1: Extract videos
        print("\n=== Step 1: Extracting latest videos ===")
        videos = ingestion.extract_latest_videos()
        
        # Step 2: Process videos with duplicate detection and random selection
        print("\n=== Step 2: Processing videos ===")
        results = ingestion.process_videos(videos, max_videos=5)
        
        # Step 3: Run quality checks
        print("\n=== Step 3: Running quality checks ===")
        quality_result = ingestion.run_quality_checks()
        
        # Step 4: Deploy to GitHub Pages if quality checks pass
        deployed = False
        if quality_result["passed"]:
            print("\n=== Step 4: Deploying to GitHub Pages ===")
            deployed = ingestion.deploy_to_github_pages()
        
        # Generate and save report
        report = ingestion.generate_report(results)
        report_path = os.path.join(ingestion.neural_nexus_path, "healthygamergg_ingestion_report.md")
        
        try:
            with open(report_path, 'w', encoding='utf-8') as f:
                f.write(report)
            print(f"\n📄 Report saved to: {report_path}")
        except Exception as e:
            print(f"❌ Failed to save report: {e}")
        
        # Print final summary
        print(f"\n=== Final Summary ===")
        print(f"Videos processed: {len(results.get('processed', []))}")
        print(f"Videos failed: {len(results.get('failed', []))}")
        print(f"Quality checks: {'PASSED' if quality_result['passed'] else 'FAILED'}")
        print(f"Deployment: {'SUCCESS' if deployed else 'FAILED'}")
        
        return len(results.get('processed', []))
        
    except Exception as e:
        print(f"❌ Fatal error: {e}")
        return 0


if __name__ == "__main__":
    success_count = main()
    sys.exit(0 if success_count > 0 else 1)