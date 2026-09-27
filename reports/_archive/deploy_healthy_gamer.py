#!/usr/bin/env python3
"""
Final deployment script for HealthyGamerGG ingestion
"""

import os
import sys
import subprocess
import json
from pathlib import Path
from datetime import datetime

def run_quality_checks(neural_nexus_path):
    """Run quality checks on the Neural Nexus site."""
    try:
        os.chdir(neural_nexus_path.parent)
        
        print("🔍 Running quality checks...")
        
        # Check markdown syntax
        result = subprocess.run(
            ['python', '-m', 'markdown', 'docs/', '--version'],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode != 0:
            print(f"Markdown check warning: {result.stderr}")
        
        # Build knowledge graph
        result = subprocess.run(
            ['mkdocs', 'build'],
            capture_output=True,
            text=True,
            timeout=120
        )
        
        if result.returncode != 0:
            print(f"Knowledge graph build failed: {result.stderr}")
            return False
        
        print("✓ Quality checks passed")
        return True
    
    except Exception as e:
        print(f"Error during quality checks: {e}")
        return False

def deploy_to_github_pages(neural_nexus_path):
    """Deploy changes to GitHub Pages."""
    try:
        os.chdir(neural_nexus_path.parent)
        
        print("🚀 Deploying to GitHub Pages...")
        
        # Add changes
        result = subprocess.run(
            ['git', 'add', 'docs/'],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        # Commit changes
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        commit_message = f"Daily HealthyGamerGG ingestion - {timestamp}"
        
        result = subprocess.run(
            ['git', 'commit', '-m', commit_message],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode != 0:
            print(f"Commit warning: {result.stderr}")
        
        # Push to repository
        result = subprocess.run(
            ['git', 'push'],
            capture_output=True,
            text=True,
            timeout=60
        )
        
        if result.returncode != 0:
            print(f"Push failed: {result.stderr}")
            return False
        
        print("✓ Successfully deployed to GitHub Pages")
        return True
    
    except Exception as e:
        print(f"Error during deployment: {e}")
        return False

def main():
    """Main deployment function."""
    neural_nexus_path = Path(os.getenv('NEURAL_NEXUS_PATH', '~/Neural-Nexus/docs')).expanduser()
    
    # Read the latest ingestion report
    report_files = list(Path('docs').glob("healthygamer_ingestion_report_*.json"))
    if not report_files:
        print("❌ No ingestion report found")
        return False
    
    latest_report = max(report_files, key=os.path.getctime)
    print(f"📊 Using report: {latest_report}")
    
    with open(latest_report, 'r') as f:
        report = json.load(f)
    
    print(f"📈 Processing statistics:")
    print(f"  - Videos found: {report['total_videos_found']}")
    print(f"  - Videos processed: {report['videos_processed']}")
    print(f"  - Videos failed: {report['videos_failed']}")
    print(f"  - Selected videos: {report['selected_videos']}")
    
    if report['videos_processed'] > 0:
        print("🔍 Running quality checks...")
        if run_quality_checks(neural_nexus_path):
            print("✅ Quality checks passed")
            
            print("🚀 Deploying to GitHub Pages...")
            if deploy_to_github_pages(neural_nexus_path):
                print("✅ Deployment successful")
                return True
            else:
                print("❌ Deployment failed")
                return False
        else:
            print("❌ Quality checks failed, skipping deployment")
            return False
    else:
        print("❌ No videos successfully processed, skipping deployment")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)