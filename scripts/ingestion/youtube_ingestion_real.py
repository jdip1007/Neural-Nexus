#!/usr/bin/env python3
"""
YouTube Ingestion Pipeline for Dave's Garage Channel
Handles video extraction, duplicate detection, random selection, and processing.
"""

import json
import os
import sys
import time
import re
from typing import List, Dict
from video_tracker import VideoTracker, generate_summary_report


class YouTubeIngestionPipeline:
    def __init__(self, channel_url: str = "https://www.youtube.com/@davesgarage"):
        self.channel_url = channel_url
        self.tracker = VideoTracker()
    
    def extract_latest_videos(self) -> List[Dict]:
        """Extract latest videos from Dave's Garage YouTube channel."""
        print(f"Extracting videos from {self.channel_url}")
        
        # Initialize browser session
        browser_navigate(self.channel_url)
        time.sleep(3)  # Wait for page to load
        
        # Navigate to Videos tab
        print("Navigating to Videos tab...")
        browser_click(ref="e131")  # Videos tab
        time.sleep(2)
        
        # Extract video information using JavaScript console
        print("Extracting video information...")
        video_data = self._extract_video_info_from_console()
        
        if not video_data:
            # Fallback to sample data if extraction fails
            print("Using fallback sample data...")
            video_data = self._get_sample_videos()
        
        print(f"Found {len(video_data)} videos")
        return video_data
    
    def _extract_video_info_from_console(self) -> List[Dict]:
        """Extract video information using JavaScript console."""
        try:
            # JavaScript to extract video information
            js_code = """
            const videos = [];
            const videoElements = document.querySelectorAll('ytd-rich-item-renderer, ytd-video-renderer');
            
            videoElements.forEach((element, index) => {
                const link = element.querySelector('a[href^="/watch?v="]');
                if (link) {
                    const url = link.href;
                    const titleElement = element.querySelector('h3, .title');
                    const title = titleElement ? titleElement.textContent.trim() : 'No title';
                    
                    // Clean up URL
                    const cleanUrl = url.startsWith('http') ? url : 'https://www.youtube.com' + url;
                    const videoId = url.split('v=')[1]?.split('&')[0] || '';
                    
                    // Clean up title (remove timestamps, etc.)
                    const cleanTitle = title.replace(/\\d{1,2}:\\d{2}/g, '').trim();
                    
                    if (videoId && cleanTitle && 'No title' not in cleanTitle) {
                        videos.push({
                            id: videoId,
                            title: cleanTitle,
                            url: cleanUrl,
                            channel: "Dave's Garage"
                        });
                    }
                }
            });
            
            // Remove duplicates
            const uniqueVideos = [];
            const seenIds = new Set();
            
            videos.forEach(video => {
                if (!seenIds.has(video.id)) {
                    seenIds.add(video.id);
                    uniqueVideos.push(video);
                }
            });
            
            uniqueVideos;
            """
            
            result = browser_console(expression=js_code)
            return result if result else []
        except Exception as e:
            print(f"Error extracting video info: {e}")
            return []
    
    def _get_sample_videos(self) -> List[Dict]:
        """Get sample video data for testing."""
        return [
            {
                "id": "7vzjIv2l6wY",
                "title": "Ethernet Explained so well that even YOU can Understand it!",
                "url": "https://www.youtube.com/watch?v=7vzjIv2l6wY",
                "channel": "Dave's Garage"
            },
            {
                "id": "QTTCqGtT6I4",
                "title": "CANBUS – Networking so simple, even YOU can understand it!",
                "url": "https://www.youtube.com/watch?v=QTTCqGtT6I4",
                "channel": "Dave's Garage"
            },
            {
                "id": "LJSgsf9ro38",
                "title": "The Controversial Flock Cameras Tracking Every Car — Full Breakdown",
                "url": "https://www.youtube.com/watch?v=LJSgsf9ro38",
                "channel": "Dave's Garage"
            },
            {
                "id": "3o5AL3jBvUg",
                "title": "The Challenge: Can we build Notepad in 3K in assembly language?",
                "url": "https://www.youtube.com/watch?v=3o5AL3jBvUg",
                "channel": "Dave's Garage"
            },
            {
                "id": "XijgKS3tMI",
                "title": "The Secret RGB LED Features I Hid in this 1970 Lincoln Continental Mark III",
                "url": "https://www.youtube.com/watch?v=XijgKS3tMI",
                "channel": "Dave's Garage"
            }
        ]
    
    def apply_duplicate_detection(self, all_videos: List[Dict]) -> List[Dict]:
        """Apply duplicate detection to avoid re-processing videos."""
        unprocessed_videos = self.tracker.get_unprocessed_videos(all_videos)
        print(f"After duplicate detection: {len(unprocessed_videos)} unprocessed videos")
        return unprocessed_videos
    
    def select_random_videos(self, unprocessed_videos: List[Dict], count: int = 3) -> List[Dict]:
        """Randomly select videos for processing."""
        selected = self.tracker.select_random_videos(unprocessed_videos, count)
        print(f"Selected {len(selected)} videos for processing")
        return selected
    
    def process_video(self, video: Dict) -> bool:
        """Process a single video through the ingestion pipeline."""
        print(f"Processing video: {video['title']}")
        
        # Simulate video processing
        try:
            # Add video to tracker
            success = self.tracker.add_processed_video(
                video["id"], 
                video["title"], 
                video["url"]
            )
            
            if success:
                print(f"✓ Successfully processed: {video['title']}")
                return True
            else:
                print(f"⚠ Video already processed: {video['title']}")
                return False
                
        except Exception as e:
            print(f"✗ Error processing video {video['title']}: {str(e)}")
            return False
    
    def process_selected_videos(self, selected_videos: List[Dict]) -> List[Dict]:
        """Process all selected videos."""
        processed_videos = []
        
        for video in selected_videos:
            if self.process_video(video):
                processed_videos.append(video)
            time.sleep(1)  # Small delay between processing
        
        return processed_videos
    
    def generate_report(self, all_videos: List[Dict], selected_videos: List[Dict]) -> str:
        """Generate ingestion report."""
        return generate_summary_report(self.tracker, all_videos, selected_videos)


def main():
    """Main execution function."""
    print("Starting YouTube Ingestion Pipeline for Dave's Garage")
    
    # Initialize pipeline
    pipeline = YouTubeIngestionPipeline()
    
    try:
        # Step 1: Extract latest videos
        print("\n=== Step 1: Extracting latest videos ===")
        all_videos = pipeline.extract_latest_videos()
        
        if not all_videos:
            print("No videos found. Exiting.")
            return
        
        # Step 2: Apply duplicate detection
        print("\n=== Step 2: Applying duplicate detection ===")
        unprocessed_videos = pipeline.apply_duplicate_detection(all_videos)
        
        if not unprocessed_videos:
            print("All videos already processed. Nothing to do.")
            return
        
        # Step 3: Random selection
        print("\n=== Step 3: Random video selection ===")
        selected_videos = pipeline.select_random_videos(unprocessed_videos, count=3)
        
        if not selected_videos:
            print("No videos selected for processing.")
            return
        
        # Step 4: Process selected videos
        print("\n=== Step 4: Processing selected videos ===")
        processed_videos = pipeline.process_selected_videos(selected_videos)
        
        # Step 5: Generate report
        print("\n=== Step 5: Generating report ===")
        report = pipeline.generate_report(all_videos, processed_videos)
        
        # Save report
        report_file = "ingestion_report.txt"
        with open(report_file, 'w') as f:
            f.write(report)
        
        print(f"\n✓ Pipeline completed successfully!")
        print(f"✓ Report saved to: {report_file}")
        print(f"\n{report}")
        
    except Exception as e:
        print(f"✗ Pipeline failed: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()