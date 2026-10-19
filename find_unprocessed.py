#!/usr/bin/env python3
"""Find unprocessed Dave's Garage videos."""
import json

with open('/home/hermes/Neural-Nexus/video_tracker.json', 'r') as f:
    tracker = json.load(f)
processed = set(tracker.get('processed_videos', {}).keys())

# Videos from channel (from yt-dlp)
all_videos = [
    ("KC31K-CUC5Y", "I Tested AI Cloning... and It's Way Worse Than You Think!", "20:51", 628000),
    ("EzfHqE9-rbY", "My Computer is now 4x Faster! That's Why It Won't Boot...", "20:49", 149000),
    ("z_mFHlUpC-g", "Why Your Computer Is Slow - Task Manager Can't Tell You, but TMOG can!", "15:46", 821000),
    ("2aw3MF8pY3w", "As a Microsoft Engineer, This Is the AI Agent Story That Scared Me", "18:44", 1100000),
    ("DSA4VFdqELg", "Reliable Isn't Always Better: TCP vs UDP", "11:27", 137000),
    ("7vzjIv2l6wY", "Ethernet Explained so well that even YOU can Understand it!", "23:27", 185000),
    ("QTTCqGtT6I4", "CANBUS - Networking so simple, even YOU can understand it!", "23:07", 574000),
    ("LJSgsf9ro38", "The Controversial Flock Cameras Tracking Every Car - Full Breakdown", "22:50", 269000),
    ("OG91c7xsNMc", "The Challenge: Can we build Notepad in 3K in assembly language?", "20:15", 338000),
    ("hRhBuHJ-j_o", "The Secret RGB LED Features I Hid in this 1970 Lincoln Continental Mark III", "22:21", 42000),
    ("jH0BYAkPj78", "Microsoft's Secret 90s Weapon That Made Windows Fast", "18:08", 139000),
    ("SR8ESCmUYLY", "Hidden Code: How Slot Machines Actually Work - The Computer Inside", "18:24", 520000),
    ("XAzUoizwnXM", "fopen is Magic! - Find Out What You've Been Missing All These Years!", "16:28", 136000),
    ("kLcpCqLwNU8", "Autism Works - Neurodiversity in the Workplace", "22:12", 84000),
    ("vEAjtOI-Oaw", "1980s: Learning To Code Back in the 80s!", "16:02", 159000),
    ("kdnN0kk7MS0", "printf is Actually a Secret Virtual Machine - And a Giant Security Hole!", "16:54", 135000),
    ("mYBxnojY-JA", "Malloc is NOT Magic: Let's Build it to Learn What's Inside!", "16:30", 328000),
    ("I14yjt00Fl8", "Yellow Key: BitLocker has been Broken! Don't lose your laptop!", "2:19", 115000),
    ("UQ4pSVS_mN0", "The Morse Code Hack That Made an AI Agent Spend $200,000", "16:14", 256000),
    ("VYTF4KIF2z0", "Why I Deleted printf() from Windows COM in 1994!", "16:29", 231000),
    ("UXd8MfTJQVg", "What do CPUs do when there's nothing to do?", "12:42", 189000),
    ("j8DygtESGeE", "Making a 1990s Phone Work Again! Hacking, Firmware, and What's Inside!", "23:24", 168000),
    ("qSNTtA7gXOA", "Inside a Massive 1980s Hard Drive: 14 Inches of Fury!", "14:05", 67000),
    ("vELETrEp27k", "The AI Model TOO POWERFUL to be Released to the Public...", "12:29", 205000),
    ("HiHMQN3kQlQ", "Task Manager is LYING About Your CPU Usage (Here's the Truth)", "18:44", 91000),
    ("y7thb-SC09g", "Wargames Movie Magic: Where it Cheats - IMSAI & WOPR!", "16:46", 71000),
    ("NebvccLHutQ", "Terminator: The Story of the 6502 Code You See Onscreen", "13:26", 177000),
    ("OUE3FSIk46g", "EXPOSED: The Dirty Little Secret of AI (On a 1979 PDP-11)", "22:24", 447000),
    ("OyN4LGyPwxc", "Why the Original Task Manager Was Under 80K and Insanely Fast - By Its Creator", "14:26", 210000),
    ("t992ul_IKtc", "Why your NEW computer is SLOWER than your OLD computer! By a Retired Microsoft Engineer.", "16:53", 536000),
]

unprocessed = [(vid, title, dur, views) for vid, title, dur, views in all_videos if vid not in processed]
print(f"Found {len(all_videos)} videos from channel")
print(f"Already processed: {len(all_videos) - len(unprocessed)}")
print(f"Unprocessed: {len(unprocessed)}")
print()
for vid, title, dur, views in unprocessed:
    print(f"  {vid} | {title} | {dur} | {views}")
