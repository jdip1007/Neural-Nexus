---
title: Reliable Isn’t Always Better: TCP vs UDP - Summary
created: 2026-10-20
updated: 2026-10-20
type: reading
domain: general
classification: general.media
tags: [youtube, video-summary, transcript, DSA4VFdqELg]
sources: [raw/videos/youtube-DSA4VFdqELg-transcript.md]
published: 2026-08-27
time_sensitive: False
confidence: high
status: active
reviewed: 2026-10-20
---

# Reliable Isn’t Always Better: TCP vs UDP - Summary

## TL;DR
And at first that sounds almost a little perverse because we spent decades making TCP mature and reliable and then the n

## Key Points
- And at first that sounds almost a little perverse because we spent decades making TCP mature and reliable and then the newest generation of web shows up riding on the protocol whose reaction to our missing package is to basically shrug
- And that is why when looking at a slow TCP capture, I care far more about re-transmissions, duplicate acts, sack blocks and periods where the acknowledgement number stops advancing than I do about every little header field
- If the update for 103 disappears, but 107 arrives correctly, there's almost no reason to freeze the remote player at 100 while we dig through the network for his former because we already know something newer
- Two UDP sends of hello and world arrive as two separate messages, if they arrive at all, but two TCP sends of the same data may arrive as hello world or he and then low world and you know, all broken up
- Three duplicate acts for the same position was traditionally enough for the sender to conclude that the segment was lost rather than merely delayed and to retransmit before the normal timer expired
- Then a later segment beginning at 51,000 arrives successfully, as does maybe one at 52,000 and 53,000, but the receiver cannot advance its cumulative acknowledgement because there is still a hole

## Entities Mentioned
- [[in-wireshark]]

## Related Concepts
- [[ai]]
- [[api]]
- [[database]]
- [[networking]]
- [[tcp]]

## Source
- [Reliable Isn’t Always Better: TCP vs UDP](https://www.youtube.com/watch?v=DSA4VFdqELg)

## Related Pages
- [[daves-garage]]
