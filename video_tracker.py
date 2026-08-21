#!/usr/bin/env python3
"""
Video Tracker for YouTube Ingestion Pipeline
Tracks processed videos to avoid duplicate processing and implements random selection.
"""

import json
import os
import random
import re
from datetime import datetime
from typing import List, Dict, Set


class VideoTracker:
    def __init__(self, tracker_file: str = "video_tracker.json"):
        self.tracker_file = tracker_file
        self.processed_videos = self.load_processed_videos()
    
    def load_processed_videos(self) -> Dict:
        """Load processed videos from tracker file."""
        if os.path.exists(self.tracker_file):
            try:
                with open(self.tracker_file, 'r') as f:
                    data = json.load(f)
                    # Handle both list and dict formats
                    if "processed_videos" in data and isinstance(data["processed_videos"], list):
                        # Old format - convert to new dict format
                        processed_dict = {}
                        for video in data["processed_videos"]:
                            if isinstance(video, dict) and "id" in video:
                                processed_dict[video["id"]] = {
                                    "title": video.get("title", ""),
                                    "processed_date": video.get("processed_at", video.get("processed_date", "")),
                                    "status": "completed"
                                }
                        return {
                            "processed_videos": processed_dict,
                            "last_updated": data.get("last_updated"),
                            "channel_name": data.get("channel_name"),
                            "channel_id": data.get("channel_id")
                        }
                    elif "processed_videos" in data and isinstance(data["processed_videos"], dict):
                        # New format - use as is
                        return data
                    else:
                        # Fallback
                        return {"processed_videos": {}, "last_updated": None}
            except (json.JSONDecodeError, IOError):
                return {"processed_videos": {}, "last_updated": None}
        return {"processed_videos": {}, "last_updated": None}
    
    def save_processed_videos(self):
        """Save processed videos to tracker file."""
        self.processed_videos["last_updated"] = datetime.now().isoformat()
        with open(self.tracker_file, 'w') as f:
            json.dump(self.processed_videos, f, indent=2)
    
    def add_processed_video(self, video_id: str, video_title: str, video_url: str):
        """Add a video to the processed list."""
        if video_id not in self.processed_videos.get("processed_videos", {}):
            self.processed_videos["processed_videos"][video_id] = {
                "title": video_title,
                "processed_date": datetime.now().isoformat(),
                "status": "completed"
            }
            self.save_processed_videos()
            return True
        return False
    
    def is_video_processed(self, video_id: str) -> bool:
        """Check if a video has already been processed."""
        return video_id in self.processed_videos.get("processed_videos", {})
    
    def get_unprocessed_videos(self, all_videos: List[Dict]) -> List[Dict]:
        """Filter out already processed videos."""
        unprocessed = []
        for video in all_videos:
            video_id = video.get("video_id") or video.get("id")
            if video_id and not self.is_video_processed(video_id):
                unprocessed.append(video)
        return unprocessed
    
    def select_random_videos(self, unprocessed_videos: List[Dict], count: int = 3) -> List[Dict]:
        """Randomly select videos from unprocessed list."""
        if len(unprocessed_videos) <= count:
            return unprocessed_videos
        
        return random.sample(unprocessed_videos, count)
    
    def get_processed_count(self) -> int:
        """Get total number of processed videos."""
        return len(self.processed_videos["processed_videos"])
    
    def get_recent_videos(self, limit: int = 10) -> List[Dict]:
        """Get most recently processed videos."""
        # Convert dict to list for sorting
        videos_list = []
        for video_id, video_data in self.processed_videos.get("processed_videos", {}).items():
            video_data["video_id"] = video_id
            videos_list.append(video_data)
        
        sorted_videos = sorted(
            videos_list,
            key=lambda x: x.get("processed_date", ""),
            reverse=True
        )
        return sorted_videos[:limit]
    
    def get_statistics(self) -> Dict:
        """Get processing statistics."""
        processed_videos = self.processed_videos.get("processed_videos", {})
        return {
            "total_processed": len(processed_videos),
            "channel_name": self.processed_videos.get("channel_name", "Unknown"),
            "last_updated": self.processed_videos.get("last_updated", "Never")
        }


def generate_summary_report(tracker: VideoTracker, processed_videos: List[Dict], 
                          selected_videos: List[Dict]) -> str:
    """Generate a summary report of the ingestion process."""
    report = f"""
=== YouTube Ingestion Pipeline Report ===
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

=== Statistics ===
Total videos in channel: {len(processed_videos)}
Already processed: {tracker.get_processed_count()}
New videos processed: {len(selected_videos)}
Unprocessed remaining: {len(processed_videos) - tracker.get_processed_count()}

=== Processed Videos ===
"""
    
    for video in selected_videos:
        report += f"- {video['title']}\n"
        report += f"  ID: {video['id']}\n"
        report += f"  URL: {video['url']}\n"
        report += f"  Processed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    
    report += f"=== Recent Activity ===\n"
    recent = tracker.get_recent_videos(5)
    for video in recent:
        processed_time = datetime.fromisoformat(video.get("processed_at", "")).strftime('%Y-%m-%d %H:%M:%S')
        report += f"- {video['title']} ({processed_time})\n"
    
    return report


if __name__ == "__main__":
    # Example usage
    tracker = VideoTracker()
    print(f"Loaded tracker with {tracker.get_processed_count()} processed videos")