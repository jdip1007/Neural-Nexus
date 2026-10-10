#!/usr/bin/env python3
"""
Chris Willx Daily YouTube Ingestion Script (Modified Version)
Uses existing video data and fetches transcripts for unprocessed videos.
"""

import os
import json
import random
import time
import requests
import hashlib
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any, Optional

# Configuration
NEURAL_NEXUS_PATH = Path("/home/hermes/Neural-Nexus")
TRANSCRIPT_API_KEY = os.environ.get("TRANSCRIPT_API_KEY")
VIDEO_TRACKER_FILE = NEURAL_NEXUS_PATH / "video_tracker.json"
RAW_TRANSCRIPTS_DIR = NEURAL_NEXUS_PATH / "raw" / "transcripts" / "chriswillx"
DOCS_DIR = NEURAL_NEXUS_PATH / "docs"
INDEX_MD_FILE = DOCS_DIR / "index.md"
LOG_MD_FILE = DOCS_DIR / "log.md"

# Existing Chris Willx videos (from the JSON file)
EXISTING_VIDEOS = [
    {
        "id": "SNrw-C_RBck",
        "title": "I Have A Problem With Love On The Spectrum - Jeff Dye",
        "url": "https://www.youtube.com/watch?v=SNrw-C_RBck",
        "duration": "10:05"
    },
    {
        "id": "mSjaMyP5QjY",
        "title": "AI DEBATE: What Will the World Actually Look Like in 2040?",
        "url": "https://www.youtube.com/watch?v=mSjaMyP5QjY",
        "duration": "2:42:33"
    },
    {
        "id": "-5epM9WG95g",
        "title": "Why Do Female Teachers Sleep With Students?",
        "url": "https://www.youtube.com/watch?v=-5epM9WG95g",
        "duration": "9:39"
    },
    {
        "id": "f2p1YH0-BaI",
        "title": "Harvard Professor: I Tried Every Diet - Daniel Lieberman",
        "url": "https://www.youtube.com/watch?v=f2p1YH0-BaI",
        "duration": "2:08:14"
    },
    {
        "id": "4dIgq-efQpY",
        "title": "The Hugging Face AI Attack Should Terrify Us",
        "url": "https://www.youtube.com/watch?v=4dIgq-efQpY",
        "duration": "9:01"
    },
    {
        "id": "ka2GKBfviic",
        "title": "Hunter Biden, Matt McCusker & Duncan Trussell - Mostly Wise #2",
        "url": "https://www.youtube.com/watch?v=ka2GKBfviic",
        "duration": "3:06:06"
    },
    {
        "id": "XzIY0M612A0",
        "title": "It Wasnt My Baggie But If It Was - Hunter Biden",
        "url": "https://www.youtube.com/watch?v=XzIY0M612A0",
        "duration": "11:19"
    },
    {
        "id": "YGAjgLtJJFI",
        "title": "Blue Zone Science Is A Total Scam",
        "url": "https://www.youtube.com/watch?v=YGAjgLtJJFI",
        "duration": "10:10"
    },
    {
        "id": "gAxNYd01I6E",
        "title": "We Are At The Beginning Of A Revolution - Jimmy Carr",
        "url": "https://www.youtube.com/watch?v=gAxNYd01I6E",
        "duration": "1:58:52"
    },
    {
        "id": "_ZMYDb86DzY",
        "title": "Marriage Kills Womens Sex Drive: Heres Why",
        "url": "https://www.youtube.com/watch?v=_ZMYDb86DzY",
        "duration": "8:43"
    },
    {
        "id": "8Oj3NxSLP1U",
        "title": "Q&A: Becoming A Dad, Favourite Peptides & Red Rising",
        "url": "https://www.youtube.com/watch?v=8Oj3NxSLP1U",
        "duration": "1:46:33"
    },
    {
        "id": "XqXLijA6CcY",
        "title": "If Your Mind Is Racing, Give It Better Problems - Jimmy Carr",
        "url": "https://www.youtube.com/watch?v=XqXLijA6CcY",
        "duration": "8:51"
    }
]

def load_video_tracker() -> Dict[str, Any]:
    """Load video tracker data"""
    if VIDEO_TRACKER_FILE.exists():
        with open(VIDEO_TRACKER_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"processed_videos": {}, "video_metadata": {}, "last_updated": datetime.now().isoformat()}

def save_video_tracker(tracker: Dict[str, Any]):
    """Save video tracker data"""
    with open(VIDEO_TRACKER_FILE, 'w', encoding='utf-8') as f:
        json.dump(tracker, f, indent=2, ensure_ascii=False)

def get_processed_video_ids() -> List[str]:
    """Get list of already processed video IDs"""
    tracker = load_video_tracker()
    return list(tracker.get("processed_videos", {}).keys())

def sanitize_filename(text: str) -> str:
    """Generate safe filename from text"""
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        text = text.replace(char, '_')
    return text[:200]

def calculate_content_hash(content: str) -> str:
    """Calculate hash of content for duplicate detection"""
    return hashlib.md5(content.encode('utf-8')).hexdigest()

def fetch_transcript(video_url: str, video_id: str, title: str) -> Dict[str, Any]:
    """Fetch transcript using TranscriptAPI"""
    if not TRANSCRIPT_API_KEY:
        return {"error": "No API key configured"}
    
    try:
        response = requests.get(
            "https://transcriptapi.com/api/v2/youtube/transcript",
            params={"video_url": video_url},
            headers={"Authorization": f"Bearer {TRANSCRIPT_API_KEY}"},
            timeout=30
        )
        
        if response.status_code == 404:
            return {"error": "HTTP 404 - Video unavailable or removed", "status": "not_found"}
        elif response.status_code == 401:
            return {"error": "HTTP 401 - Invalid API key"}
        elif response.status_code == 429:
            return {"error": "HTTP 429 - Rate limit exceeded", "status": "rate_limited"}
        elif response.status_code == 200:
            data = response.json()
            return {"success": True, "data": data}
        else:
            return {"error": f"HTTP {response.status_code}"}
    
    except Exception as e:
        return {"error": str(e)}

def save_transcript(video_id: str, title: str, transcript_data: Dict[str, Any]) -> Optional[Path]:
    """Save transcript with proper frontmatter"""
    safe_title = sanitize_filename(title)
    filename = f"{safe_title}.md"
    filepath = RAW_TRANSCRIPTS_DIR / filename
    
    # Create frontmatter
    frontmatter = f"""---
source_url: https://www.youtube.com/watch?v={video_id}
ingested: {datetime.now().strftime('%Y-%m-%d')}
video_id: {video_id}
title: {title}
series: 
tags: [youtube, chriswillx, podcast]
---

# {title}

**Source:** Chris Williamson (@ChrisWillx)
**Video URL:** https://www.youtube.com/watch?v={video_id}
**Video ID:** `{video_id}`
**Transcript:** [[raw/transcripts/chriswillx/{filename}]]
**Accessed:** {datetime.now().strftime('%Y-%m-%d')}

## Transcript

"""
    
    # Format transcript content
    transcript_text = ""
    if "transcript" in transcript_data:
        for segment in transcript_data["transcript"]:
            time_str = segment.get("start", 0)
            text = segment.get("text", "")
            timestamp = f"[{int(time_str // 60):02d}:{int(time_str % 60):02d}]"
            transcript_text += f"{timestamp} {text}\n"
    
    # Save file
    content = frontmatter + transcript_text
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return filepath

def create_concept_page(video_id: str, title: str, transcript_path: Path) -> Optional[Path]:
    """Create concept page from transcript content"""
    # Read transcript file
    try:
        with open(transcript_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ Error reading transcript: {e}")
        return None
    
    # Extract main topics (simplified analysis)
    topics = extract_main_topics(content)
    
    # Create concept page filename
    safe_title = sanitize_filename(title)
    filename = f"youtube-{video_id}-{safe_title}.md"
    filepath = DOCS_DIR / "concepts" / filename
    
    # Create concept page content
    concept_content = f"""---
title: {title}
created: {datetime.now().strftime('%Y-%m-%d')}
updated: {datetime.now().strftime('%Y-%m-%d')}
type: concept
tags: [youtube, chriswillx, podcast, {', '.join(topics[:3])}]
sources: [{transcript_path.name}]
---

# {title}

## Overview

This podcast episode from Chris Williamson explores {topics[0] if topics else 'various topics'} with insights and analysis.

## Key Topics

<!-- Extract main topics from the video content -->
{chr(10).join(f"- **{topic}** - Brief description" for topic in topics[:5])}

## Key Insights

<!-- Important takeaways and revelations from the video -->

## Practical Applications

<!-- How viewers can apply these insights in their lives -->

## Related Concepts

<!-- Link to related concepts in the wiki -->
"""
    
    # Save concept page
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(concept_content)
    
    return filepath

def extract_main_topics(content: str) -> List[str]:
    """Extract main topics from transcript content (simplified)"""
    # This is a simplified approach - in production, you'd use more sophisticated NLP
    common_topics = [
        "relationships", "dating", "love", "friendship", "communication",
        "mental health", "psychology", "therapy", "self-improvement",
        "mindset", "personal development", "habits", "addiction",
        "family", "parenting", "marriage", "divorce", "breakups",
        "social anxiety", "depression", "anxiety", "trauma",
        "philosophy", "existentialism", "meaning", "purpose"
    ]
    
    found_topics = []
    content_lower = content.lower()
    
    for topic in common_topics:
        if topic in content_lower:
            found_topics.append(topic)
    
    return found_topics[:5]  # Return top 5 topics

def update_index_md(new_pages: List[Path]):
    """Update index.md with new pages"""
    if not INDEX_MD_FILE.exists():
        return
    
    # Read current index
    with open(INDEX_MD_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find YouTube section or create one
    youtube_section = "## YouTube Podcasts"
    if youtube_section not in content:
        content += f"\n\n{youtube_section}\n\n"
    
    # Add new pages
    for page_path in new_pages:
        page_name = page_path.name.replace('.md', '')
        content += f"- [[{page_name}]] - Chris Williamson podcast episode\n"
    
    # Write back
    with open(INDEX_MD_FILE, 'w', encoding='utf-8') as f:
        f.write(content)

def update_log_md(processing_stats: Dict[str, Any]):
    """Update log.md with processing statistics"""
    log_entry = f"""
## {datetime.now().strftime('%Y-%m-%d')} process | Chris Willx YouTube Videos

- **Source:** Chris Williamson YouTube Channel (@ChrisWillx)
- **Action:** Processed {processing_stats.get('processed', 0)} videos into wiki pages
- **Content:** Podcast episodes, interviews, discussions
- **Output:** Created concept pages + raw transcripts
- **Method:** TranscriptAPI integration with structured wiki pages
- **Success Rate:** {processing_stats.get('success_rate', 0)}%
- **Errors:** {processing_stats.get('errors', [])}
"""
    
    if LOG_MD_FILE.exists():
        with open(LOG_MD_FILE, 'a', encoding='utf-8') as f:
            f.write(log_entry)
    else:
        with open(LOG_MD_FILE, 'w', encoding='utf-8') as f:
            f.write(log_entry)

def run_quality_checks():
    """Run quality checks on the Neural Nexus"""
    try:
        import subprocess
        result = subprocess.run([
            "python3", "run_quality_checks.py"
        ], cwd=NEURAL_NEXUS_PATH, capture_output=True, text=True, timeout=60)
        
        if result.returncode == 0:
            print("✅ Quality checks passed")
            return True
        else:
            print(f"❌ Quality checks failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Error running quality checks: {e}")
        return False

def deploy_to_github_pages():
    """Deploy to GitHub Pages if requested"""
    try:
        import subprocess
        result = subprocess.run([
            "git", "add", "."
        ], cwd=NEURAL_NEXUS_PATH, capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"❌ Git add failed: {result.stderr}")
            return False
        
        result = subprocess.run([
            "git", "commit", "-m", f"Daily Chris Willx ingestion - {datetime.now().strftime('%Y-%m-%d')}"
        ], cwd=NEURAL_NEXUS_PATH, capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"❌ Git commit failed: {result.stderr}")
            return False
        
        result = subprocess.run([
            "git", "push"
        ], cwd=NEURAL_NEXUS_PATH, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Successfully deployed to GitHub Pages")
            return True
        else:
            print(f"❌ Git push failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Error deploying to GitHub Pages: {e}")
        return False

def main():
    """Main ingestion workflow"""
    print("🚀 Starting Chris Willx Daily YouTube Ingestion...")
    
    # Setup directories
    RAW_TRANSCRIPTS_DIR.mkdir(parents=True, exist_ok=True)
    (DOCS_DIR / "concepts").mkdir(parents=True, exist_ok=True)
    
    # Get processed video IDs
    processed_ids = get_processed_video_ids()
    print(f"📊 Already processed {len(processed_ids)} videos")
    
    # Filter unprocessed videos
    unprocessed_videos = [v for v in EXISTING_VIDEOS if v["id"] not in processed_ids]
    
    if not unprocessed_videos:
        print("❌ No unprocessed videos found")
        return
    
    print(f"📥 Found {len(unprocessed_videos)} unprocessed videos")
    
    # Randomly select up to 5 videos
    selected_videos = random.sample(unprocessed_videos, min(5, len(unprocessed_videos)))
    print(f"🎲 Selected {len(selected_videos)} videos for processing:")
    
    for video in selected_videos:
        print(f"  - {video['title']} ({video['duration']})")
    
    # Process selected videos
    processing_stats = {
        "total": len(selected_videos),
        "processed": 0,
        "failed": 0,
        "errors": [],
        "success_rate": 0
    }
    
    new_pages = []
    
    for i, video in enumerate(selected_videos, 1):
        print(f"\n[{i}/{len(selected_videos)}] Processing: {video['title']}")
        
        # Fetch transcript
        result = fetch_transcript(video["url"], video["id"], video["title"])
        
        if result.get("success"):
            transcript_data = result["data"]
            
            # Save transcript
            transcript_path = save_transcript(video["id"], video["title"], transcript_data)
            if transcript_path:
                print(f"  ✅ Saved transcript: {transcript_path.name}")
                
                # Create concept page
                concept_page = create_concept_page(video["id"], video["title"], transcript_path)
                if concept_page:
                    print(f"  ✅ Created concept page: {concept_page.name}")
                    new_pages.append(concept_page)
                    
                    # Update video tracker
                    tracker = load_video_tracker()
                    tracker["processed_videos"][video["id"]] = {
                        "title": video["title"],
                        "processed_at": datetime.now().isoformat(),
                        "page_filename": concept_page.name,
                        "content_hash": calculate_content_hash(str(transcript_data))
                    }
                    tracker["video_metadata"][video["id"]] = {
                        "id": video["id"],
                        "title": video["title"],
                        "url": video["url"],
                        "page_filename": concept_page.name,
                        "transcript_path": transcript_path.name,
                        "processed_at": datetime.now().isoformat(),
                        "status": "processed"
                    }
                    save_video_tracker(tracker)
                    
                    processing_stats["processed"] += 1
                else:
                    print(f"  ❌ Failed to create concept page")
                    processing_stats["failed"] += 1
                    processing_stats["errors"].append(f"Concept page creation failed for {video['id']}")
            else:
                print(f"  ❌ Failed to save transcript")
                processing_stats["failed"] += 1
                processing_stats["errors"].append(f"Transcript save failed for {video['id']}")
        else:
            print(f"  ❌ Failed to fetch transcript: {result.get('error')}")
            processing_stats["failed"] += 1
            processing_stats["errors"].append(f"Transcript fetch failed for {video['id']}: {result.get('error')}")
        
        # Rate limiting
        time.sleep(3)
    
    # Update index and log
    if new_pages:
        update_index_md(new_pages)
        update_log_md(processing_stats)
    
    # Calculate success rate
    processing_stats["success_rate"] = (processing_stats["processed"] / processing_stats["total"]) * 100
    
    # Run quality checks
    print("\n🔍 Running quality checks...")
    quality_check_passed = run_quality_checks()
    
    # Deploy to GitHub Pages
    if quality_check_passed:
        print("\n🚀 Deploying to GitHub Pages...")
        deploy_success = deploy_to_github_pages()
    else:
        deploy_success = False
    
    # Final report
    print(f"\n{'='*60}")
    print(f"📊 Chris Willx Daily Ingestion Report")
    print(f"{'='*60}")
    print(f"📹 Total videos available: {len(EXISTING_VIDEOS)}")
    print(f"📹 Already processed: {len(processed_ids)}")
    print(f"📹 Unprocessed videos: {len(unprocessed_videos)}")
    print(f"🎲 Videos selected: {len(selected_videos)}")
    print(f"✅ Videos processed: {processing_stats['processed']}")
    print(f"❌ Videos failed: {processing_stats['failed']}")
    print(f"📈 Success rate: {processing_stats['success_rate']:.1f}%")
    print(f"📄 New pages created: {len(new_pages)}")
    print(f"🔍 Quality checks: {'✅ Passed' if quality_check_passed else '❌ Failed'}")
    print(f"🚀 GitHub Pages: {'✅ Deployed' if deploy_success else '❌ Failed'}")
    
    if processing_stats["errors"]:
        print(f"\n📝 Errors encountered:")
        for error in processing_stats["errors"]:
            print(f"  - {error}")

if __name__ == "__main__":
    main()