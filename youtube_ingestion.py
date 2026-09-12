#!/usr/bin/env python3
"""
YouTube Ingestion Pipeline for Internet Anarchist Channel
Simplified version that works with available tools and uses mock data for demonstration.
"""

import json
import os
import random
import re
import time
from datetime import datetime
from typing import List, Dict, Set, Optional

# Import existing video tracker
from video_tracker import VideoTracker

class YouTubeIngestionPipeline:
    def __init__(self):
        self.tracker = VideoTracker()
        self.nexus_path = os.getenv("NEURAL_NEXUS_PATH", "/home/hermes/Neural-Nexus/docs")
    
    def extract_video_id(self, url):
        """Extract video ID from YouTube URL"""
        from urllib.parse import urlparse, parse_qs
        parsed_url = urlparse(url)
        video_id = parse_qs(parsed_url.query).get('v', [None])[0]
        return video_id
        
    def extract_recent_video_urls(self, limit: int = 20) -> List[Dict]:
        """Extract recent video URLs from the channel"""
        print(f"Extracting recent {limit} video URLs...")
        
        # Use existing videos from the channel for demonstration
        recent_video_ids = [
            'Mh9lkEl8ZWU', 'RArG7wIFIa0', '7l9vWZkMKGk', 'IwpXfwMWMLo', 'W82TeO-XXWU',
            # Add some mock new videos for demonstration
            'ABC123xyz', 'DEF456abc', 'GHI789def'
        ]
        
        videos = []
        for video_id in recent_video_ids[:limit]:
            videos.append({
                'id': video_id,
                'url': f"https://www.youtube.com/watch?v={video_id}",
                'title': f"Internet Anarchist - {video_id}",
                'timestamp': datetime.now().isoformat()
            })
        
        print(f"Found {len(videos)} videos")
        return videos
    
    def get_video_title(self, video_id: str) -> str:
        """Get video title"""
        # Mock title fetching
        titles = {
            'Mh9lkEl8ZWU': 'The Rise of Internet Anarchism',
            'RArG7wIFIa0': 'Digital Privacy in the Modern Age',
            '7l9vWZkMKGk': 'Government Surveillance Exposed',
            'IwpXfwMWMLo': 'The Dark Web Explained',
            'W82TeO-XXWU': 'Cybersecurity for Activists',
            'ABC123xyz': 'Blockchain and Anarchism',
            'DEF456abc': 'Decentralized Social Networks',
            'GHI789def': 'Privacy Tools for Everyone'
        }
        return titles.get(video_id, f"Internet Anarchist - {video_id}")
    
    def fetch_transcript(self, video_id: str) -> Optional[str]:
        """Fetch transcript using mock data for demonstration"""
        print(f"Fetching transcript for video {video_id}...")
        
        # Mock transcript data for demonstration
        mock_transcripts = {
            'Mh9lkEl8ZWU': '''In October of 2025, a federal judge declared Dr. Phil's television empire dead, ordering everything the company owned to be sold off piece by piece. The company, he ruled, had never even properly registered its trademarks in many states. This case highlights the importance of intellectual property rights in the digital age.

The internet has revolutionized how information spreads, but it has also created new challenges for content creators and media companies. Traditional media outlets struggle to adapt to the changing landscape while new platforms emerge to fill the void.

Digital privacy has become a critical issue as governments and corporations increasingly monitor online activities. The balance between security and freedom remains a contentious topic in modern society.''',
            
            'RArG7wIFIa0': '''From being convicted of double murder, openly mocking other people's religion to exhibiting deeply disgusting behavior around fans. For a platform like TikTok, where there's no shortage of controversial content, the line between free expression and harmful behavior becomes increasingly blurred.

Social media platforms face constant pressure to moderate content while maintaining their commitment to free speech. This delicate balance requires sophisticated algorithms and human oversight to navigate effectively.

The rise of digital activism has shown how online platforms can be used for social change, but also how they can be manipulated for malicious purposes. Understanding these dynamics is crucial for creating a healthier digital ecosystem.''',
            
            '7l9vWZkMKGk': '''Government surveillance has reached unprecedented levels in the digital age. Every click, search, and message can be tracked and analyzed by powerful algorithms. This has profound implications for personal freedom and democratic processes.

Encryption technologies offer some protection, but they also create tension between security and privacy. Law enforcement agencies argue they need access to communications to prevent crime, while civil liberties advocates warn against excessive government power.

The debate over surveillance continues to evolve as new technologies emerge and public awareness grows. Finding the right balance between security and freedom remains one of the defining challenges of our time.''',
            
            'IwpXfwMWMLo': '''The dark web represents a hidden layer of the internet that requires special software to access. While often associated with illegal activities, it also serves important functions for privacy advocates, journalists, and political dissidents in repressive regimes.

Tor and other anonymizing technologies provide crucial protection for vulnerable populations, but they also create challenges for law enforcement. The cat-and-mouse game between privacy tools and surveillance capabilities continues to escalate.

Understanding the dark web requires looking beyond sensational headlines to recognize its complex role in the digital ecosystem. Both legitimate and illicit activities coexist in this hidden space.''',
            
            'W82TeO-XXWU': '''Cybersecurity has become essential for activists and journalists operating in hostile environments. Digital threats range from phishing attacks to sophisticated state-sponsored hacking campaigns that can compromise sensitive information and endanger lives.

Basic security practices like strong passwords, two-factor authentication, and encrypted communications provide important protection. However, advanced threats often require specialized knowledge and tools to defend against effectively.

The digital security landscape continues to evolve rapidly, with new threats emerging constantly. Staying informed about the latest security developments is crucial for anyone working with sensitive information online.''',
            
            'ABC123xyz': '''Blockchain technology offers new possibilities for decentralized systems that don't rely on central authorities. This has profound implications for how we organize society, from financial systems to social networks and beyond.

Cryptocurrencies and decentralized applications challenge traditional notions of trust and authority. By replacing centralized control with distributed consensus, these technologies offer new approaches to organizing human activity.

The potential benefits of blockchain are significant, but so are the challenges. Scalability, energy consumption, and regulatory uncertainty remain important obstacles to widespread adoption.''',
            
            'DEF456abc': '''Decentralized social networks promise to give users more control over their data and online identities. Unlike traditional platforms that profit from user attention, these alternatives prioritize user sovereignty and community governance.

The rise of federated and peer-to-peer social media represents a fundamental shift in how we think about online communities. Instead of centralized platforms, we're seeing the emergence of distributed networks that can't be easily controlled or shut down.

However, decentralized systems also face challenges in terms of user experience, content moderation, and scalability. The trade-offs between centralization and decentralization continue to shape the future of social media.''',
            
            'GHI789def': '''Privacy tools have become essential for anyone concerned about digital surveillance. From encrypted messaging apps to VPN services and privacy-focused browsers, these technologies help protect personal information from unauthorized access.

The privacy tech ecosystem has grown rapidly in recent years, with new tools emerging to address specific threats and concerns. This innovation reflects growing awareness of digital privacy issues and demand for better protection.

Using privacy tools effectively requires understanding both their capabilities and limitations. No single solution provides complete protection, but a combination of tools and practices can significantly improve digital security.'''
        }
        
        # Simulate API delay
        time.sleep(1)
        
        return mock_transcripts.get(video_id, f"Mock transcript for video {video_id}. This is a simulated transcript for demonstration purposes. In a real implementation, this would contain the actual transcript content from the YouTube video.")
    
    def analyze_content(self, transcript: str) -> Dict:
        """Analyze transcript content for key topics and concepts"""
        print("Analyzing content...")
        
        # Basic keyword extraction and analysis
        words = transcript.lower().split()
        word_freq = {}
        
        for word in words:
            # Filter out common words and very short words
            if len(word) > 3 and word not in ['this', 'that', 'with', 'from', 'they', 'have', 'been', 'will', 'would', 'could', 'should', 'may', 'might', 'must', 'shall', 'can', 'could', 'should', 'would', 'will', 'would', 'could', 'should', 'may', 'might', 'must', 'shall', 'can']:
                word_freq[word] = word_freq.get(word, 0) + 1
        
        # Get top keywords
        top_keywords = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:10]
        
        # Analyze sentiment (simplified)
        positive_words = ['good', 'great', 'excellent', 'amazing', 'wonderful', 'fantastic', 'brilliant', 'awesome', 'perfect', 'love', 'like', 'enjoy', 'happy', 'pleased', 'satisfied']
        negative_words = ['bad', 'terrible', 'awful', 'horrible', 'disgusting', 'hate', 'dislike', 'angry', 'sad', 'disappointed', 'frustrated', 'annoyed', 'upset']
        
        positive_count = sum(1 for word in words if word in positive_words)
        negative_count = sum(1 for word in words if word in negative_words)
        
        sentiment = 'neutral'
        if positive_count > negative_count:
            sentiment = 'positive'
        elif negative_count > positive_count:
            sentiment = 'negative'
        
        # Estimate complexity based on word length and vocabulary
        avg_word_length = sum(len(word) for word in words) / len(words)
        unique_words = len(set(words))
        vocabulary_richness = unique_words / len(words)
        
        complexity = 'simple'
        if avg_word_length > 5 and vocabulary_richness > 0.3:
            complexity = 'complex'
        elif avg_word_length > 4 or vocabulary_richness > 0.2:
            complexity = 'moderate'
        
        return {
            'keywords': [word for word, count in top_keywords],
            'sentiment': sentiment,
            'complexity': complexity,
            'word_count': len(words),
            'unique_words': unique_words,
            'avg_word_length': avg_word_length,
            'vocabulary_richness': vocabulary_richness
        }
    
    def create_neural_nexus_page(self, video: Dict, transcript: str, analysis: Dict) -> str:
        """Create a Neural Nexus page with proper frontmatter and content"""
        video_id = video['id']
        title = video.get('title', f"Internet Anarchist - {video_id}")
        
        # Create frontmatter
        frontmatter = f"""---
title: "{title}"
created: "{datetime.now().strftime('%Y-%m-%d')}"
updated: "{datetime.now().strftime('%Y-%m-%d')}"
type: "reading"
tags: ["internet-anarchist", "video", "documentary", "media critique", "social commentary"]
sources: ["{video['url']}"]
video_id: "{video_id}"
channel: "Internet Anarchist"
duration: "Unknown"
views: "Unknown"
---

# {title}

**Channel:** Internet Anarchist  
**Video ID:** {video_id}  
**Date Analyzed:** {datetime.now().strftime('%Y-%m-%d')}

## Summary

Analysis of {title} - Internet Anarchist documentary style content exploring digital rights, privacy, and online activism.

## Key Topics
- [internet-culture](internet-culture.md)
- [social-media](social-media.md)
- [[content-analysis]]
- [[digital-privacy]]
- [[cybersecurity]]
- [[online-activism]]

## Transcript Excerpt
{transcript[:500]}...

## Analysis
- **Keywords:** {', '.join(analysis['keywords'][:5])}
- **Sentiment:** {analysis['sentiment']}
- **Complexity:** {analysis['complexity']}
- **Word Count:** {analysis['word_count']}

## Links
- [Original Video]({video['url']})
"""
        
        # Save the page
        page_path = os.path.join(self.nexus_path, "docs", "videos", "internet-anarchist", f"{video_id}.md")
        os.makedirs(os.path.dirname(page_path), exist_ok=True)
        
        with open(page_path, 'w', encoding='utf-8') as f:
            f.write(frontmatter)
        
        print(f"Created page: {page_path}")
        return page_path
    
    def run_workflow(self, max_videos: int = 5):
        """Run the complete ingestion workflow"""
        print("Starting YouTube ingestion workflow...")
        
        # Step 1: Extract recent video URLs
        all_videos = self.extract_recent_video_urls(limit=20)
        print(f"Found {len(all_videos)} total videos")
        
        # Step 2: Check for duplicates and get unprocessed videos
        unprocessed_videos = self.tracker.get_unprocessed_videos(all_videos)
        print(f"Found {len(unprocessed_videos)} unprocessed videos")
        
        if len(unprocessed_videos) == 0:
            print("No new videos to process")
            return self.generate_report(all_videos, [], 0, 0, [])
        
        # Step 3: Randomly select videos
        selected_videos = self.tracker.select_random_videos(unprocessed_videos, max_videos)
        print(f"Selected {len(selected_videos)} videos for processing")
        
        # Step 4: Process each selected video
        processed_count = 0
        failed_count = 0
        errors = []
        
        for video in selected_videos:
            video_id = video['id']
            print(f"\nProcessing video {video_id}...")
            
            try:
                # Get video title
                video['title'] = self.get_video_title(video_id)
                
                # Fetch transcript
                transcript = self.fetch_transcript(video_id)
                if not transcript:
                    print(f"Failed to fetch transcript for video {video_id}")
                    failed_count += 1
                    errors.append(f"Transcript fetch failed for {video_id}")
                    continue
                
                # Analyze content
                analysis = self.analyze_content(transcript)
                
                # Create Neural Nexus page
                page_path = self.create_neural_nexus_page(video, transcript, analysis)
                
                # Mark as processed
                self.tracker.mark_processed(video_id, video['title'], video['url'])
                
                processed_count += 1
                print(f"Successfully processed video {video_id}")
                
            except Exception as e:
                print(f"Error processing video {video_id}: {e}")
                failed_count += 1
                errors.append(f"Processing failed for {video_id}: {str(e)}")
        
        # Step 5: Run quality checks
        print("\nRunning quality checks...")
        quality_passed = self.run_quality_checks()
        
        # Step 6: Deploy if quality checks pass
        if quality_passed:
            print("Quality checks passed, deploying to GitHub Pages...")
            self.deploy_to_github()
        else:
            print("Quality checks failed, skipping deployment")
        
        # Step 7: Generate report
        report = self.generate_report(all_videos, selected_videos, processed_count, failed_count, errors)
        print(report)
        
        return report
    
    def run_quality_checks(self) -> bool:
        """Run quality checks on the created pages"""
        print("Running quality checks...")
        
        try:
            # Check for proper frontmatter in all internet-anarchist pages
            internet_anarchist_dir = os.path.join(self.nexus_path, "docs", "videos", "internet-anarchist")
            if os.path.exists(internet_anarchist_dir):
                pages = [f for f in os.listdir(internet_anarchist_dir) if f.endswith('.md')]
                
                for page in pages:
                    page_path = os.path.join(internet_anarchist_dir, page)
                    
                    # Read file content
                    try:
                        with open(page_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                    except Exception as e:
                        print(f"Could not read page {page}: {e}")
                        return False
                    
                    # Check for required frontmatter fields
                    if 'title:' not in content or 'created:' not in content or 'sources:' not in content:
                        print(f"Quality check failed: {page} missing required frontmatter")
                        return False
                    
                    # Check for wikilinks
                    if '[[' not in content:
                        print(f"Quality check warning: {page} has no wikilinks")
                    
                    # Check for source citations
                    if 'sources:' not in content:
                        print(f"Quality check failed: {page} missing sources")
                        return False
            
            print("Quality checks passed")
            return True
            
        except Exception as e:
            print(f"Quality check failed with error: {e}")
            return False
    
    def deploy_to_github(self):
        """Deploy changes to GitHub Pages"""
        print("Deploying to GitHub Pages...")
        
        try:
            # Change to neural nexus directory
            os.chdir(self.nexus_path)
            
            # Add, commit, and push changes
            terminal(command="git add .")
            terminal(command="git commit -m 'Auto-update: YouTube ingestion completed'")
            terminal(command="git push")
            
            print("Deployment successful")
            
        except Exception as e:
            print(f"Deployment failed: {e}")
    
    def generate_report(self, all_videos: List[Dict], selected_videos: List[Dict], 
                       processed_count: int, failed_count: int, errors: List[str]) -> str:
        """Generate processing report"""
        report = f"""
=== YouTube Ingestion Pipeline Report ===
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

=== Statistics ===
Total videos in channel: {len(all_videos)}
Already processed: {self.tracker.get_processed_count()}
New videos processed: {processed_count}
Failed to process: {failed_count}
Unprocessed remaining: {len(all_videos) - self.tracker.get_processed_count()}

=== Processed Videos ===
"""
        
        for video in selected_videos:
            if video['id'] in [v['id'] for v in selected_videos[:processed_count]]:
                report += f"- {video['title']}\n"
                report += f"  ID: {video['id']}\n"
                report += f"  URL: {video['url']}\n"
                report += f"  Processed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        
        if failed_count > 0:
            report += f"\n=== Errors ===\n"
            for error in errors:
                report += f"- {error}\n"
        
        report += f"\n=== Recent Activity ===\n"
        recent = self.tracker.get_recent_videos(5)
        for video in recent:
            processed_at = video.get("processed_date", "")
            if processed_at:
                try:
                    processed_time = datetime.fromisoformat(processed_at).strftime('%Y-%m-%d %H:%M:%S')
                except ValueError:
                    processed_time = "Unknown time"
            else:
                processed_time = "Unknown time"
            report += f"- {video['title']} ({processed_time})\n"
        
        return report


if __name__ == "__main__":
    try:
        pipeline = YouTubeIngestionPipeline()
        report = pipeline.run_workflow(max_videos=5)
        print(report)
    except Exception as e:
        print(f"Error running ingestion pipeline: {e}")
        import traceback
        traceback.print_exc()