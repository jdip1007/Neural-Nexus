---
title: YouTube Transcript: 5.3.7 How IBM Built a Jeopardy Champion - Video 4: How Watson Works - Steps 1 and 2
created: 2026-10-01
updated: 2026-10-01
type: video
source_url: https://www.youtube.com/watch?v=_L315IjxyUM-transcript
source_type: video
ingested: 2026-10-01
published: recent
duration_minutes: 20
language: en
time_sensitive: True
---


# YouTube Transcript: 5.3.7 How IBM Built a Jeopardy Champion - Video 4: How Watson Works - Steps 1 and 2

## Video Information
- **Title**: 5.3.7 How IBM Built a Jeopardy Champion - Video 4: How Watson Works - Steps 1 and 2
- **Video ID**: _L315IjxyUM
- **Published**: Unknown
- **Views**: Unknown
- **Language**: en

## Transcript
00:04 

00:04 When Watson receives a
question, the first step

00:07 is question analysis.

00:09 One of the things Watson tries
to figure out in this step

00:13 is what the question
is looking for.

00:16 This is defined as trying
to find the Lexical Answer

00:19 Type, or LAT, of the question.

00:23 The LAT is the word or
noun in the question

00:26 that specifies the
type of answer.

00:29 You should be able to replace
the LAT with the answer

00:32 to complete the sentence.

00:34 For example, for the
question, "Mozart's last

00:38 and perhaps most
powerful symphony

00:40 shares its name with this
planet," the LAT in this case

00:44 is "this planet."

00:47 If we replace this with
the answer "Jupiter,"

00:50 it makes sense.

00:51 Mozart's last and perhaps
most powerful symphony shares

00:55 its name with Jupiter.

00:58 For the question, "Smaller
than only Greenland,

01:01 it's the world's second largest
island," the LAT is "it's."

01:05 If we replace the LAT with
the answer "New Guinea,"

01:09 it makes sense.

01:10 "Smaller than only
Greenland, New Guinea

01:13 is the world's second
largest island."

01:15 Unfortunately, the
LAT is not "island,"

01:18 which would be more descriptive,
since the sentence with "New

01:21 Guinea" in place of "island"
does not make sense.

01:25 We can see in these two examples
that sometimes the LAT is very

01:28 specific, like "this planet,"
and sometimes it's very vague,

01:33 like "it's."

01:36 If we know the LAT, we
know what to look for.

01:40 However, in an analysis
of 20,000 questions,

01:44 2,500 distinct LATs were
found, and 12% of the questions

01:49 did not even have
an explicit LAT.

01:51 They had LATs like "it's."

01:54 Furthermore, even the most
frequent 200 explicit LATs

01:58 cover less than 50%
of the questions.

02:02 So to enhance the
question analysis step,

02:05 Watson also performs
relation detection

02:08 to find relationships among
words and decomposition

02:12 to split the question
into different clues.

02:17 The second step in Watson
is hypothesis generation.

02:21 The goal of this step is to use
the question analysis of step

02:25 one to produce candidate answers
by searching the databases.

02:30 In this step several
hundred candidate answers

02:33 are generated.

02:35 For the question, "Mozart's
last and perhaps most powerful

02:38 symphony shares its
name with this planet,"

02:41 candidate answers could be
Mercury, Earth, and Jupiter.

02:46 These are generated using
various search techniques.

02:51 Then each candidate
answer plugged back

02:54 into the question
in place of the LAT

02:56 is considered a hypothesis.

02:59 For the question about
Mozart's symphony,

03:02 hypothesis one would
be the question

03:04 with "Mercury" in
place of "this planet."

03:07 Hypothesis two
would have "Jupiter"

03:09 in place of "this planet."

03:11 And hypothesis three
would have "Earth"

03:13 in place of "this planet."

03:18 If the correct answer is
not generated at this stage,

03:21 Watson has no hope of
getting the question right.

03:25 Therefore, this step
errors on the side

03:27 of generating a
lot of hypotheses

03:30 and leaves it up
to the next step

03:32 to find the correct answer.

03:34 In the next video, we'll
discuss how steps three and four

03:38 score and rank the hypotheses.

