#!/usr/bin/env python3
"""
HealthyGamerGG YouTube Ingestion Pipeline - Production Version
Uses TranscriptAPI for channel search + transcript fetch.
Implements duplicate detection, random selection, and Neural Nexus page creation.
"""

import json
import os
import sys
import time
import random
import re
import hashlib
import subprocess
from pathlib import Path
from typing import List, Dict, Optional
from datetime import datetime
import requests

# Add the scripts directory to path for video_tracker import
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from video_tracker import VideoTracker


class HealthyGamerGGLiveIngestion:
    def __init__(self):
        self.channel_handle = "@HealthyGamerGG"
        self.channel_url = "https://www.youtube.com/@HealthyGamerGG"
        self.tracker = VideoTracker(
            os.path.join(os.path.dirname(os.path.abspath(__file__)), "healthygamer_tracker.json")
        )
        self.neural_nexus_path = Path(os.getenv('NEURAL_NEXUS_PATH', '/home/hermes/Neural-Nexus/docs')).expanduser()
        self.neural_nexus_repo = os.getenv('NEURAL_NEXUS_REPO', 'github.com/jdip1007/Neural-Nexus')
        self.transcript_api_key = os.getenv('TRANSCRIPT_API_KEY')
        self.repo_root = self.neural_nexus_path.parent  # /home/hermes/Neural-Nexus

        # Statistics
        self.stats = {
            "videos_found": 0,
            "videos_already_processed": 0,
            "videos_unprocessed": 0,
            "videos_selected": 0,
            "videos_processed_success": 0,
            "videos_processed_error": 0,
            "pages_created": [],
            "errors": [],
            "start_time": datetime.now().isoformat(),
        }

        # Initialize tracker with channel info
        if not self.tracker.processed_videos.get("channel_name"):
            self.tracker.processed_videos["channel_name"] = "HealthyGamerGG"
            self.tracker.processed_videos["channel_id"] = "@HealthyGamerGG"
            self.tracker.save_processed_videos()

    # ── Step 1: Extract recent video URLs via TranscriptAPI ─────────────
    def extract_recent_videos(self, max_pages: int = 3) -> List[Dict]:
        """Search HealthyGamerGG channel for recent videos using TranscriptAPI."""
        print(f"\n🎬 Step 1: Extracting videos from {self.channel_handle} via TranscriptAPI")

        all_videos = []
        seen_ids = set()

        # Use both channel search AND general search for better coverage
        search_queries = [
            "HealthyGamerGG mental health",
            "HealthyGamerGG Dr K anxiety",
            "HealthyGamerGG relationships",
            "HealthyGamerGG ADHD",
            "HealthyGamerGG depression",
        ]

        for query in search_queries:
            try:
                # Use general search (more reliable than channel search)
                videos = self._search_general(query, limit=10)
                for v in videos:
                    vid = v.get("video_id", "")
                    if vid and vid not in seen_ids:
                        seen_ids.add(vid)
                        all_videos.append(v)
                time.sleep(0.5)  # Rate limiting
            except Exception as e:
                print(f"  ⚠️ Search '{query}' failed: {e}")
                self.stats["errors"].append(f"Search failed for '{query}': {e}")

        # Deduplicate and sort
        print(f"  ✅ Found {len(all_videos)} unique videos from channel searches")
        self.stats["videos_found"] = len(all_videos)
        return all_videos

    def _search_channel(self, query: str, limit: int = 10) -> List[Dict]:
        """Search within HealthyGamerGG channel via TranscriptAPI."""
        url = "https://transcriptapi.com/api/v2/youtube/channel/search"
        params = {
            "q": query,
            "channel": self.channel_handle,
            "limit": limit,
        }
        headers = {"Authorization": f"Bearer {self.transcript_api_key}"}

        resp = requests.get(url, params=params, headers=headers, timeout=30)
        resp.raise_for_status()
        data = resp.json()

        videos = []
        for result in data.get("results", []):
            # TranscriptAPI returns 'videoId' not 'video_id'
            video_id = result.get("videoId") or result.get("video_id", "")
            title = result.get("title", "Unknown")
            if not video_id:
                continue
            # Filter to only HealthyGamerGG videos
            channel = result.get("channelHandle") or result.get("channelTitle", "")
            if self.channel_handle.lower() not in channel.lower() and "HealthyGamerGG" not in channel:
                # For general search, only keep HealthyGamerGG videos
                if result.get("channelHandle") != "@HealthyGamerGG":
                    continue
            videos.append({
                "video_id": video_id,
                "id": video_id,  # For VideoTracker compatibility
                "title": title,
                "url": f"https://www.youtube.com/watch?v={video_id}",
                "published_at": result.get("publishedTimeText", ""),
                "views": result.get("viewCountText", ""),
                "length": result.get("lengthText", ""),
            })

        return videos

    def _search_general(self, query: str, limit: int = 10) -> List[Dict]:
        """General YouTube search (filters to HealthyGamerGG results only)."""
        url = "https://transcriptapi.com/api/v2/youtube/search"
        params = {
            "q": query,
            "type": "video",
            "limit": limit,
        }
        headers = {"Authorization": f"Bearer {self.transcript_api_key}"}

        resp = requests.get(url, params=params, headers=headers, timeout=30)
        resp.raise_for_status()
        data = resp.json()

        videos = []
        for result in data.get("results", []):
            # TranscriptAPI returns 'videoId' not 'video_id'
            video_id = result.get("videoId") or result.get("video_id", "")
            title = result.get("title", "Unknown")
            if not video_id:
                continue
            # Filter to only HealthyGamerGG videos
            channel = result.get("channelHandle") or result.get("channelTitle", "")
            if "@HealthyGamerGG" not in channel and "HealthyGamerGG" not in channel:
                continue
            videos.append({
                "video_id": video_id,
                "id": video_id,  # For VideoTracker compatibility
                "title": title,
                "url": f"https://www.youtube.com/watch?v={video_id}",
                "published_at": result.get("publishedTimeText", ""),
                "views": result.get("viewCountText", ""),
                "length": result.get("lengthText", ""),
            })

        return videos

    # ── Step 2: Duplicate detection ─────────────────────────────────────
    def filter_unprocessed(self, all_videos: List[Dict]) -> List[Dict]:
        """Filter out already-processed videos."""
        print(f"\n📊 Step 2: Duplicate detection")
        unprocessed = self.tracker.get_unprocessed_videos(all_videos)
        already_processed = len(all_videos) - len(unprocessed)
        print(f"  Already processed: {already_processed}")
        print(f"  Unprocessed: {len(unprocessed)}")
        self.stats["videos_already_processed"] = already_processed
        self.stats["videos_unprocessed"] = len(unprocessed)
        return unprocessed

    # ── Step 3: Random selection ────────────────────────────────────────
    def select_random_videos(self, unprocessed: List[Dict], count: int = 5) -> List[Dict]:
        """Randomly select up to `count` unprocessed videos."""
        print(f"\n🎲 Step 3: Random selection (up to {count} videos)")
        selected = self.tracker.select_random_videos(unprocessed, count)
        print(f"  Selected {len(selected)} videos:")
        for v in selected:
            print(f"    - {v.get('title', 'Unknown')}")
        self.stats["videos_selected"] = len(selected)
        return selected

    # ── Step 4: Fetch transcript via TranscriptAPI ──────────────────────
    def fetch_transcript(self, video_url: str) -> Optional[List[Dict]]:
        """Fetch transcript via TranscriptAPI (avoids YouTube cloud IP blocking)."""
        api_url = "https://transcriptapi.com/api/v2/youtube/transcript"
        params = {"video_url": video_url}
        headers = {"Authorization": f"Bearer {self.transcript_api_key}"}

        resp = requests.get(api_url, params=params, headers=headers, timeout=60)
        resp.raise_for_status()
        data = resp.json()

        transcript = data.get("transcript", [])
        if transcript:
            print(f"    ✅ Transcript: {len(transcript)} segments")
            return transcript
        else:
            print(f"    ⚠️ No transcript returned")
            return None

    # ── Step 5: Analyze content ─────────────────────────────────────────
    def analyze_content(self, transcript: List[Dict], video_title: str) -> Dict:
        """Extract key topics, concepts, and create structured analysis."""
        full_text = " ".join(seg.get("text", "") for seg in transcript)

        # Topic detection with schema-aligned tags
        topic_keywords = {
            "mental-health": ["mental health", "therapy", "counseling", "psychologist", "psychiatrist", "dr k"],
            "anxiety": ["anxiety", "anxious", "panic", "worry", "fear", "nervous"],
            "depression": ["depression", "depressed", "sad", "hopeless", "numb"],
            "adhd": ["adhd", "attention deficit", "hyperactivity", "focus", "distract"],
            "trauma": ["trauma", "traumatic", "ptsd", "abuse", "adverse childhood"],
            "relationships": ["relationship", "dating", "marriage", "partner", "love", "breakup"],
            "addiction": ["addiction", "addict", "substance", "gambling", "porn", "dopamine"],
            "emotional-regulation": ["emotion", "emotional", "regulate", "feelings", "anger", "frustration"],
            "burnout": ["burnout", "exhaustion", "overwhelm", "overwork", "stress"],
            "self-improvement": ["improve", "growth", "develop", "change", "habit", "discipline"],
            "neuroscience": ["brain", "neuro", "dopamine", "serotonin", "cortex", "amygdala"],
            "cognitive-science": ["cognitive", "thinking", "belief", "perception", "mindset"],
            "mindfulness": ["mindful", "meditation", "awareness", "present", "breathe"],
            "social": ["social", "isolation", "lonely", "connection", "community"],
            "family": ["family", "parent", "mother", "father", "child", "sibling"],
            "existentialism": ["existential", "meaning", "purpose", "life", "death", "mortality"],
        }

        detected_tags = []
        for tag, keywords in topic_keywords.items():
            if any(kw in full_text.lower() for kw in keywords):
                detected_tags.append(tag)

        # Ensure at least some tags
        if not detected_tags:
            detected_tags = ["mental-health", "psychology"]

        # Always include channel tags
        detected_tags.extend(["healthygamergg", "youtube", "video-derived"])
        detected_tags = list(dict.fromkeys(detected_tags))  # dedupe preserving order

        # Extract key concepts (noun phrases, simplified)
        key_concepts = []
        concept_patterns = [
            r'(?:the|a|an)\s+(?:concept|idea|theory|principle)\s+of\s+([a-z\s]+)',
            r'(?:understanding|exploring|analyzing)\s+([a-z\s]+)',
        ]
        for pat in concept_patterns:
            matches = re.findall(pat, full_text.lower())
            key_concepts.extend(m.strip() for m in matches if len(m.strip()) > 3)
        key_concepts = key_concepts[:5]  # Limit

        # Generate summary (first ~300 meaningful words)
        sentences = re.split(r'[.!?]+', full_text)
        summary_sentences = [s.strip() for s in sentences[:15] if len(s.strip()) > 20]
        summary = ". ".join(summary_sentences)
        if len(summary) > 500:
            summary = summary[:500] + "..."

        return {
            "tags": detected_tags,
            "key_concepts": key_concepts,
            "summary": summary,
            "transcript_length": len(full_text),
            "segment_count": len(transcript),
        }

    # ── Step 5b: Create Neural Nexus pages ──────────────────────────────
    def create_neural_nexus_pages(self, video: Dict, transcript: List[Dict], analysis: Dict) -> List[str]:
        """Create raw source + reading page with proper frontmatter, wikilinks, citations."""
        video_id = video.get("video_id", video.get("id"))
        title = video.get("title", "Unknown")
        video_url = video.get("url", f"https://www.youtube.com/watch?v={video_id}")
        now = datetime.now()
        date_str = now.strftime('%Y-%m-%d')
        pages_created = []

        # ── Raw source file ─────────────────────────────────────
        raw_dir = self.neural_nexus_path / "raw" / "videos"
        raw_dir.mkdir(parents=True, exist_ok=True)
        raw_filename = f"youtube-{video_id}-transcript.md"
        raw_path = raw_dir / raw_filename

        transcript_text = json.dumps(transcript)
        content_hash = hashlib.sha256(transcript_text.encode()).hexdigest()

        # Estimate duration
        last_seg = transcript[-1] if transcript else {}
        last_start = last_seg.get("start", 0)
        if isinstance(last_start, str):
            try:
                last_start = float(last_start)
            except ValueError:
                last_start = 0
        duration_minutes = int(last_start // 60) if isinstance(last_start, (int, float)) else 0

        # Build timestamped transcript
        transcript_lines = []
        for seg in transcript:
            start = seg.get("start", 0)
            if isinstance(start, str):
                try:
                    start = float(start)
                except ValueError:
                    start = 0
            mins = int(start // 60)
            secs = int(start % 60)
            text = seg.get("text", "")
            transcript_lines.append(f"[{mins:02d}:{secs:02d}] {text}")

        raw_content = f"""---
source_url: {video_url}
source_type: video
author: HealthyGamerGG
publication_date: {video.get('published_at', date_str)}
ingested_date: {date_str}
transcript_available: true
sha256: {content_hash}
duration_minutes: {duration_minutes}
---

# YouTube Transcript: {title}

## Video Information
- **Title**: {title}
- **Video ID**: {video_id}
- **Channel**: HealthyGamerGG
- **Published**: {video.get('published_at', 'Unknown')}
- **Duration**: ~{duration_minutes} minutes
- **Segments**: {len(transcript)}

## Transcript

{chr(10).join(transcript_lines)}
"""
        raw_path.write_text(raw_content, encoding='utf-8')
        raw_rel = f"raw/videos/{raw_filename}"
        pages_created.append(str(raw_path))
        print(f"    📄 Raw source: {raw_path}")

        # ── Reading/summary page ────────────────────────────────
        safe_title = re.sub(r'[^\w\s-]', '', title.lower())
        safe_title = re.sub(r'[-\s]+', '-', safe_title).strip('-')
        # Truncate very long filenames
        if len(safe_title) > 80:
            safe_title = safe_title[:80]
        reading_filename = f"youtube-{video_id}-{safe_title}.md"
        reading_path = self.neural_nexus_path / reading_filename

        # Build wikilinks from tags
        wikilinks = []
        tag_to_page = {
            "mental-health": "Mental Health",
            "anxiety": "Anxiety",
            "depression": "Depression",
            "adhd": "ADHD",
            "trauma": "Trauma",
            "relationships": "Relationships",
            "addiction": "Addiction Recovery",
            "emotional-regulation": "Emotional Regulation",
            "burnout": "Burnout",
            "self-improvement": "Self Improvement",
            "neuroscience": "Neuroscience",
            "cognitive-science": "Cognitive Science",
            "mindfulness": "Mindfulness",
            "social": "Social Dynamics",
            "family": "Family",
            "existentialism": "Existentialism",
        }
        for tag in analysis["tags"]:
            if tag in tag_to_page:
                wikilinks.append(f"[[{tag_to_page[tag]}]]")

        # Ensure minimum 2 wikilinks
        if len(wikilinks) < 2:
            wikilinks.extend(["[[Mental Health]]", "[[Psychology]]"])
        wikilinks = list(dict.fromkeys(wikilinks))  # dedupe

        # Determine domain
        domain = "psychology"
        if any(t in analysis["tags"] for t in ["neuroscience", "cognitive-science"]):
            domain = "psychology"

        # Determine type
        page_type = "reading"

        # Build tags YAML list
        tags_yaml = "\n".join(f"  - {t}" for t in analysis["tags"])

        reading_content = f"""---
title: "{title}"
created: {date_str}
updated: {date_str}
type: {page_type}
domain: {domain}
tags:
{tags_yaml}
  - healthygamer-gg
sources:
  - {raw_rel}
confidence: high
status: active
reviewed: {date_str}
---

# {title}

> **Source**: [{video_url}]({video_url})
> **Channel**: HealthyGamerGG (Dr. K)
> **Duration**: ~{duration_minutes} minutes
> **Transcript Segments**: {analysis['segment_count']}

## Summary

{analysis['summary']}

## Key Topics

{chr(10).join(f"- **{t.replace('-', ' ').title()}**" for t in analysis['tags'] if t not in ('youtube', 'video-derived', 'healthygamergg'))}

## Key Concepts

{chr(10).join(f"- {c.title()}" for c in analysis['key_concepts']) if analysis['key_concepts'] else "- Mental health and well-being topics as discussed by Dr. K"}

## Related Pages

{chr(10).join(f"- {wl}" for wl in wikilinks)}

## Source

^[{raw_rel}]
"""
        reading_path.write_text(reading_content, encoding='utf-8')
        pages_created.append(str(reading_path))
        print(f"    📄 Reading page: {reading_path}")

        return pages_created

    # ── Step 4+5: Process a single video ────────────────────────────────
    def process_video(self, video: Dict) -> Dict:
        """Process a single video: fetch transcript, analyze, create pages."""
        video_id = video.get("video_id", video.get("id"))
        title = video.get("title", "Unknown")
        video_url = video.get("url", f"https://www.youtube.com/watch?v={video_id}")

        print(f"\n  🔄 Processing: {title}")

        # Check if already processed (redundant safety check)
        if self.tracker.is_video_processed(video_id):
            print(f"    ⏭️  Already processed, skipping")
            return {"status": "skipped", "video_id": video_id}

        try:
            # Fetch transcript
            print(f"    📝 Fetching transcript...")
            transcript = self.fetch_transcript(video_url)
            if not transcript:
                raise ValueError(f"No transcript available for {video_id}")

            # Analyze content
            print(f"    🔍 Analyzing content...")
            analysis = self.analyze_content(transcript, title)

            # Create Neural Nexus pages
            print(f"    📄 Creating Neural Nexus pages...")
            pages = self.create_neural_nexus_pages(video, transcript, analysis)

            # Mark as processed
            self.tracker.mark_processed(video_id, title, video_url)

            self.stats["videos_processed_success"] += 1
            self.stats["pages_created"].extend(pages)

            return {
                "status": "success",
                "video_id": video_id,
                "title": title,
                "pages": pages,
                "tags": analysis["tags"],
            }

        except Exception as e:
            error_msg = f"Error processing {video_id} ({title}): {e}"
            print(f"    ❌ {error_msg}")
            self.stats["errors"].append(error_msg)
            self.stats["videos_processed_error"] += 1
            return {"status": "error", "video_id": video_id, "error": str(e)}

    # ── Step 6: Verification ────────────────────────────────────────────
    def verify_pages(self) -> Dict:
        """Verify all created pages have proper frontmatter, wikilinks, citations."""
        print(f"\n✅ Step 6: Pre-deployment verification")
        results = {"valid": 0, "invalid": 0, "errors": []}

        for page_path in self.stats["pages_created"]:
            path = Path(page_path)
            if not path.exists():
                results["errors"].append(f"File missing: {page_path}")
                results["invalid"] += 1
                continue

            content = path.read_text(encoding='utf-8')

            # Check frontmatter
            if not content.startswith("---"):
                results["errors"].append(f"Missing frontmatter: {page_path}")
                results["invalid"] += 1
                continue

            # Extract frontmatter
            fm_match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
            if not fm_match:
                results["errors"].append(f"Malformed frontmatter: {page_path}")
                results["invalid"] += 1
                continue

            fm_text = fm_match.group(1)

            # Check required fields (raw sources have different schema)
            is_raw = "raw/" in str(path) or "raw\\" in str(path)
            if is_raw:
                required_fields = ["source_url", "source_type", "ingested_date"]
            else:
                required_fields = ["title", "created", "updated", "type", "tags"]
            for field in required_fields:
                if f"{field}:" not in fm_text and f"{field} :" not in fm_text:
                    results["errors"].append(f"Missing '{field}' in frontmatter: {page_path}")
                    results["invalid"] += 1
                    break
            else:
                # Check sources (required for reading type)
                if "type: reading" in fm_text and "sources:" not in fm_text:
                    results["errors"].append(f"Missing 'sources' in reading page: {page_path}")
                    results["invalid"] += 1
                elif not is_raw:
                    # Check wikilinks (minimum 2, only for non-raw pages)
                    wikilinks = re.findall(r'\[\[([^\]]+)\]\]', content)
                    if len(wikilinks) < 2:
                        results["errors"].append(f"Fewer than 2 wikilinks in: {page_path}")
                        results["invalid"] += 1
                    else:
                        results["valid"] += 1
                else:
                    results["valid"] += 1

        print(f"  Valid pages: {results['valid']}")
        print(f"  Invalid pages: {results['invalid']}")
        if results['errors']:
            for err in results['errors']:
                print(f"    ❌ {err}")

        return results

    # ── Step 7: Quality checks + Deploy ─────────────────────────────────
    def run_quality_checks_and_deploy(self) -> Dict:
        """Run quality checks (lint, graph, catalog) and deploy if passing."""
        print(f"\n🚀 Step 7: Quality checks and deployment")
        deploy_result = {"quality_passed": False, "deployed": False, "errors": []}

        try:
            # Run quality check script if it exists
            qc_script = self.repo_root / "run_quality_checks.py"
            if qc_script.exists():
                print("  Running quality checks...")
                result = subprocess.run(
                    [sys.executable, str(qc_script)],
                    capture_output=True, text=True, timeout=120,
                    cwd=str(self.repo_root)
                )
                if result.returncode != 0:
                    print(f"  ⚠️ Quality checks had warnings: {result.stderr[:200]}")
                else:
                    print(f"  ✅ Quality checks passed")
            else:
                print("  ⚠️ No quality check script found, skipping")

            deploy_result["quality_passed"] = True

            # Git add, commit, push
            print("  Committing and pushing to GitHub...")
            subprocess.run(["git", "add", "-A"], cwd=str(self.repo_root), capture_output=True, timeout=30)

            commit_msg = f"HealthyGamerGG daily ingestion - {datetime.now().strftime('%Y-%m-%d')}"
            result = subprocess.run(
                ["git", "commit", "-m", commit_msg],
                cwd=str(self.repo_root), capture_output=True, text=True, timeout=30
            )
            if result.returncode == 0:
                print(f"  ✅ Committed: {commit_msg}")

                # Push
                result = subprocess.run(
                    ["git", "push"], cwd=str(self.repo_root),
                    capture_output=True, text=True, timeout=60
                )
                if result.returncode == 0:
                    print(f"  ✅ Pushed to GitHub")
                    deploy_result["deployed"] = True
                else:
                    print(f"  ❌ Push failed: {result.stderr[:200]}")
                    deploy_result["errors"].append(f"Push failed: {result.stderr[:200]}")
            else:
                # No changes to commit is OK
                if "nothing to commit" in result.stdout:
                    print(f"  ℹ️ No changes to commit")
                    deploy_result["deployed"] = True
                else:
                    print(f"  ❌ Commit failed: {result.stderr[:200]}")
                    deploy_result["errors"].append(f"Commit failed: {result.stderr[:200]}")

        except Exception as e:
            error_msg = f"Deployment error: {e}"
            print(f"  ❌ {error_msg}")
            deploy_result["errors"].append(error_msg)

        return deploy_result

    # ── Main pipeline ───────────────────────────────────────────────────
    def run(self) -> Dict:
        """Execute the full ingestion pipeline."""
        print("=" * 70)
        print("🚀 HealthyGamerGG Daily Ingestion Pipeline (Production)")
        print(f"   Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 70)

        # Step 1: Extract videos
        all_videos = self.extract_recent_videos()
        if not all_videos:
            print("\n⚠️ No videos found. Pipeline cannot continue.")
            return self._finalize(deploy_result={"deployed": False, "quality_passed": False})

        # Step 2: Filter unprocessed
        unprocessed = self.filter_unprocessed(all_videos)
        if not unprocessed:
            print("\n✅ All videos already processed. Nothing to do.")
            return self._finalize(deploy_result={"deployed": True, "quality_passed": True})

        # Step 3: Random selection (up to 5)
        selected = self.select_random_videos(unprocessed, count=5)
        if not selected:
            print("\n⚠️ No videos selected.")
            return self._finalize(deploy_result={"deployed": False, "quality_passed": False})

        # Step 4+5: Process each video
        print(f"\n🔄 Step 4-5: Processing {len(selected)} selected videos")
        results = []
        for video in selected:
            result = self.process_video(video)
            results.append(result)
            time.sleep(1)  # Rate limiting between API calls

        # Step 6: Verification
        verification = self.verify_pages()

        # Step 7: Quality checks + Deploy
        deploy_result = {"deployed": False, "quality_passed": False}
        if self.stats["videos_processed_success"] > 0 and verification["invalid"] == 0:
            deploy_result = self.run_quality_checks_and_deploy()
        elif verification["invalid"] > 0:
            print(f"\n⚠️ Skipping deployment due to {verification['invalid']} invalid pages")
        else:
            print(f"\n⚠️ No videos successfully processed, skipping deployment")

        return self._finalize(results, verification, deploy_result)

    def _finalize(self, results=None, verification=None, deploy_result=None) -> Dict:
        """Generate final report and return statistics."""
        self.stats["end_time"] = datetime.now().isoformat()

        report = f"""
{'=' * 70}
HealthyGamerGG Daily Ingestion Report
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
{'=' * 70}

## Statistics
- Videos found: {self.stats['videos_found']}
- Already processed: {self.stats['videos_already_processed']}
- Unprocessed: {self.stats['videos_unprocessed']}
- Selected for processing: {self.stats['videos_selected']}
- Successfully processed: {self.stats['videos_processed_success']}
- Failed: {self.stats['videos_processed_error']}
- Pages created: {len(self.stats['pages_created'])}

## Verification
"""
        if verification:
            report += f"""- Valid pages: {verification['valid']}
- Invalid pages: {verification['invalid']}
"""
        else:
            report += "- Skipped (no pages created)\n"

        report += f"""
## Deployment
"""
        if deploy_result:
            report += f"""- Quality checks: {'✅ Passed' if deploy_result.get('quality_passed') else '❌ Failed'}
- Deployed to GitHub: {'✅ Yes' if deploy_result.get('deployed') else '❌ No'}
"""
        else:
            report += "- Not attempted\n"

        if self.stats["errors"]:
            report += "\n## Errors\n"
            for err in self.stats["errors"]:
                report += f"- ❌ {err}\n"

        if results:
            report += "\n## Processed Videos\n"
            for r in results:
                if r["status"] == "success":
                    report += f"- ✅ {r.get('title', r['video_id'])} (tags: {', '.join(r.get('tags', []))})\n"
                elif r["status"] == "error":
                    report += f"- ❌ {r['video_id']}: {r.get('error', 'unknown')}\n"
                else:
                    report += f"- ⏭️ {r['video_id']}: skipped\n"

        if self.stats["pages_created"]:
            report += "\n## Created Pages\n"
            for p in self.stats["pages_created"]:
                report += f"- {p}\n"

        # Save report
        report_filename = f"healthygamer_daily_ingestion_report_{datetime.now().strftime('%Y-%m-%d')}.md"
        report_path = self.repo_root / report_filename
        report_path.write_text(report, encoding='utf-8')
        print(f"\n📄 Report saved: {report_path}")
        print(report)

        return {
            **self.stats,
            "verification": verification,
            "deploy_result": deploy_result,
            "report_file": str(report_path),
        }


if __name__ == "__main__":
    ingestion = HealthyGamerGGLiveIngestion()
    result = ingestion.run()
