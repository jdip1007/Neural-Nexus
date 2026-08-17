#!/usr/bin/env python3
"""
Daily Channel Ingestion Pipeline for The Infographics Show YouTube Channel
Handles video extraction, duplicate detection, random selection, and processing.
"""

import json
import os
import sys
import time
import random
import re
from typing import List, Dict
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from video_tracker import VideoTracker, generate_summary_report


class DailyChannelIngestion:
    def __init__(self, channel_url: str = "https://www.youtube.com/@TheInfographicsShow"):
        self.channel_url = channel_url
        self.tracker = VideoTracker()
        self.channel_name = "The Infographics Show"
    
    def extract_latest_videos(self) -> List[Dict]:
        """Extract latest videos from The Infographics Show YouTube channel."""
        print(f"Extracting videos from {self.channel_url}")
        
        # For now, let's create some sample video data for The Infographics Show
        # In a real implementation, you'd parse the actual YouTube page
        sample_videos = [
            {
                "id": "uzg-tGiK_y8",
                "title": "Why Marines aren't just a different kind of 'soldier' || The Infographics Show react",
                "url": "https://www.youtube.com/watch?v=uzg-tGiK_y8",
                "channel": "The Infographics Show"
            },
            {
                "id": "cemy5eP5Jjs",
                "title": "Most Insane The Infographics Show Videos of All Time (Compilation)",
                "url": "https://www.youtube.com/watch?v=cemy5eP5Jjs",
                "channel": "The Infographics Show"
            },
            {
                "id": "8zUhBnpVgdE",
                "title": "Most Viewed The Infographics Show Videos (Compilation)",
                "url": "https://www.youtube.com/watch?v=8zUhBnpVgdE",
                "channel": "The Infographics Show"
            },
            {
                "id": "D4nPxik59oE",
                "title": "The Horror of the Zodiac Killer || The Infographics Show",
                "url": "https://www.youtube.com/watch?v=D4nPxik59oE",
                "channel": "The Infographics Show"
            },
            {
                "id": "k0ksj42YJaM",
                "title": "Why Your Brain Can't Handle Modern Life || The Infographics Show",
                "url": "https://www.youtube.com/watch?v=k0ksj42YJaM",
                "channel": "The Infographics Show"
            }
        ]
        
        print(f"Found {len(sample_videos)} sample videos for {self.channel_name}")
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
    
    def run_daily_ingestion(self, video_count: int = 3):
        """Run the daily ingestion process."""
        print(f"Starting Daily Channel Ingestion for {self.channel_name}")
        print(f"Channel URL: {self.channel_url}")
        print("=" * 60)
        
        try:
            # Step 1: Extract latest videos
            print("\n=== Step 1: Extracting latest videos ===")
            all_videos = self.extract_latest_videos()
            
            if not all_videos:
                print("No videos found. Exiting.")
                return
            
            # Step 2: Apply duplicate detection
            print("\n=== Step 2: Applying duplicate detection ===")
            unprocessed_videos = self.apply_duplicate_detection(all_videos)
            
            if not unprocessed_videos:
                print("All videos already processed. Nothing to do.")
                return
            
            # Step 3: Random selection
            print(f"\n=== Step 3: Random video selection ===")
            selected_videos = self.select_random_videos(unprocessed_videos, count=video_count)
            
            if not selected_videos:
                print("No videos selected for processing.")
                return
            
            # Step 4: Process selected videos
            print(f"\n=== Step 4: Processing selected videos ===")
            processed_videos = self.process_selected_videos(selected_videos)
            
            # Step 5: Generate report
            print(f"\n=== Step 5: Generating report ===")
            report = self.generate_report(all_videos, processed_videos)
            
            # Save report
            report_file = "daily_ingestion_report.txt"
            with open(report_file, 'w') as f:
                f.write(report)
            
            print(f"\n✓ Daily ingestion completed successfully!")
            print(f"✓ Report saved to: {report_file}")
            print(f"\n{report}")
            
            return processed_videos
            
        except Exception as e:
            print(f"✗ Daily ingestion failed: {str(e)}")
            sys.exit(1)


def main():
    """Main execution function."""
    # Initialize daily ingestion for The Infographics Show
    ingestion = DailyChannelIngestion()
    
    # Run daily ingestion with default 3 videos
    ingestion.run_daily_ingestion(video_count=3)


if __name__ == "__main__":
    main()