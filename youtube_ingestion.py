#!/usr/bin/env python3
"""
YouTube Ingestion Pipeline for Dave's Garage Channel
Handles video extraction, duplicate detection, random selection, and processing.
"""

import json
import os
import sys
import time
from typing import List, Dict
from video_tracker import VideoTracker, generate_summary_report


class YouTubeIngestionPipeline:
    def __init__(self, channel_url: str = "https://www.youtube.com/@davesgarage"):
        self.channel_url = channel_url
        self.tracker = VideoTracker()
    
    def extract_latest_videos(self) -> List[Dict]:
        """Extract latest videos from Dave's Garage YouTube channel."""
        print(f"Extracting videos from {self.channel_url}")
        
        # For now, let's create some sample video data for testing
        # In a real implementation, you'd parse the actual YouTube page
        sample_videos = [
            {
                "id": "dQw4w9WgXcQ",
                "title": "Building a Workshop from Scratch - Ep 1",
                "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                "channel": "Dave's Garage"
            },
            {
                "id": "2Z4m4n5R6tU",
                "title": "Tool Restoration Project - Old Power Tools",
                "url": "https://www.youtube.com/watch?v=2Z4m4n5R6tU",
                "channel": "Dave's Garage"
            },
            {
                "id": "7Y8s9T0uVwX",
                "title": "Workshop Tour and Organization Tips",
                "url": "https://www.youtube.com/watch?v=7Y8s9T0uVwX",
                "channel": "Dave's Garage"
            },
            {
                "id": "3A4b5C6dE7f",
                "title": "Building a Custom Workbench",
                "url": "https://www.youtube.com/watch?v=3A4b5C6dE7f",
                "channel": "Dave's Garage"
            },
            {
                "id": "8G9h0I1jK2l",
                "title": "Tool Review: Latest Power Tools",
                "url": "https://www.youtube.com/watch?v=8G9h0I1jK2l",
                "channel": "Dave's Garage"
            }
        ]
        
        print(f"Found {len(sample_videos)} sample videos")
        return sample_videos
    
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