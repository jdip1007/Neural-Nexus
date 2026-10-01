---
title: YouTube Transcript: Video 9a: Music Information Retrieval (MIR): Sound to Score and Music Theory
created: 2026-10-01
updated: 2026-10-01
type: video
source_url: https://www.youtube.com/watch?v=gHT4d3Ep_M0-transcript
source_type: video
ingested: 2026-10-01
published: recent
duration_minutes: 20
language: en
time_sensitive: True
---


# YouTube Transcript: Video 9a: Music Information Retrieval (MIR): Sound to Score and Music Theory

## Video Information
- **Title**: Video 9a: Music Information Retrieval (MIR): Sound to Score and Music Theory
- **Video ID**: gHT4d3Ep_M0
- **Published**: Unknown
- **Views**: Unknown
- **Language**: en

## Transcript
00:00 [SQUEAKING]

00:01 [RUSTLING]

00:03 [CLICKING]

00:06 

00:11 MICHAEL SCOTT ASATO CUTHBERT:
Hello, computational music

00:13 theorists.

00:14 Here's a short video on what
some of the problems in MIR,

00:19 or Music Information Retrieval,
are and how they can be

00:23 connected to music
theory and musicology,

00:26 which is the main topic
of this class, 21m.383.

00:31 These slides owe a lot to Avi
Pfeffer, professor at Harvard,

00:36 who inspired them
with his lectures.

00:40 The main question that
we'll be working on

00:42 is, how do we move from sound
that's made in the real world

00:49 to a score that's printed out
or displayed on the screen?

00:53 What kinds of
technologies are needed,

00:56 and what kinds of problems need
to be solved in order to do this

00:59 really well?

01:00 Well, first, when we sing
or play an instrument,

01:03 we're making actual sound
waves in the real world,

01:06 so we need to solve
the problem of how

01:08 to most accurately transform
sound into a signal.

01:13 And this involves microphones
and other devices,

01:16 and it's kind of a pure
engineering problem

01:19 that we're not going to be
focusing on in this class.

01:22 But it's very complex
and very valuable,

01:25 and we offer some courses
in the music department

01:27 that will help you
do this better.

01:30 But once we've got the
sound from the real world

01:34 into an electrical
signal, we're working

01:38 in the time domain,
as we call it,

01:41 and that is the amplitude of
sound at a single moment--

01:46 forward, backwards,
positive, or negative.

01:48 And we usually record in
something close to CD quality

01:54 or 44,000 times per second.

01:56 We're measuring the amplitude
as a 16-bit signed integer.

02:00 And so the sound, at this
point, looks something like this

02:05 if this was, I don't
know, an attack

02:08 of an instrument
that's decaying,

02:09 maybe a piano or
something of that sort.

02:14 The problem here is, how do we
convert from the time domain

02:18 to frequency, to being able to
say, OK, all these impulses add

02:24 up to a particular frequency?

02:27 How do we decode
it from the signal

02:31 and understand that,
hey, in this sound,

02:33 there's two principal
frequencies that

02:36 are being heard?

02:38 And to do this, we use
Fourier transforms,

02:41 and the fast Fourier
transform algorithm

02:44 is something that is very
good to know in order

02:48 to work in this field.

02:49 So now we have
frequencies, and we

02:51 want to translate them to
pitch and pitch connections.

02:57 And that's not just
thinking about,

03:00 what is A, 440
hertz or something,

03:02 but which of those
frequencies that pop up are

03:05 prolonged to make
a particular pitch?

03:08 Because even while I'm speaking,
there are particular frequencies

03:12 that are popping up, but they
don't necessarily make pitches.

03:15 The attack on a flute
isn't necessarily the pitch

03:21 that we want.

03:21 So which ones are
connected for this?

03:24 And once we have these
particular frequency pitch

03:26 connections, we want to move
from there to pitch notes.

03:32 As we saw with
the piano example,

03:35 there were two
frequencies there.

03:36 Does that mean
two pitches, or is

03:38 one of them a
reverberation in the room?

03:41 Or if you're listening
to another instrument,

03:44 maybe you hear seven pitches.

03:46 Six of them are higher
and much quieter,

03:49 and you might think, oh,
that's the overtone series

03:52 of that instrument.

03:53 And so going from pitch
connections to pitch notes

03:56 involves an
estimation of timbre.

03:59 What is the timbre
of the instrument?

04:01 What is the overtone
series that one expects

04:04 and who we remove them.

04:06 And from there, do we end up
still with multiple pitches

04:08 in a chord?

04:11 Now that we know
the musical pitches

04:15 that we're interested
in, we want

04:16 to go from there
to understanding

04:20 the duration of these pitches
and the tempo of the piece.

04:24 And so there are
particular algorithms

04:26 that we can use to
estimate the duration.

04:29 I mean, one thing is you just
look at milliseconds and things

04:32 and then say, OK,
well, that's going

04:34 to be the most common note.

04:35 We'll call it a
quarter note and so on.

04:38 And from there, we can
estimate the tempo.

04:41 Or we can do it
in the other way.

04:44 We can take all
these pitches and try

04:47 to estimate a tempo based
on, what are the recurring

04:51 onsets that seem to be beats?

04:54 And from there, go and figure
out the duration-- quarter note,

04:58 half note, three beats
long, something like that

05:01 for each of the notes.

05:03 So which direction
do MIR people go?

05:08 It turns out that we usually
create a sort of feedback loop.

05:12 So we try to do both at once,
and estimations of tempo

05:16 lead to durations, which then
can be rejected or accepted,

05:20 and estimations of the duration
lead to estimations of tempo.

05:25 And so the technologies
involved are

05:27 beat tracking and
self-similarity detection

05:30 and others.

05:32 From the pitches, the
duration, and the tempo,

05:36 we can create what we call the
full notes or just the notes.

05:42 That is something from a
pitch and a duration combined.

05:47 From all these
full notes, we can

05:50 construct what we
call a virtual score,

05:53 and that is the
score as represented

05:56 purely as collections of
notes and other events.

06:01 We might be estimating,
at this point, crescendos

06:04 and decrescendos,
and maybe we're

06:06 hearing certain
notes are slurred,

06:07 and we're keeping these all
as objects inside memory.

06:12 And so this involves
the technology

06:14 of music representation,
which we will be getting

06:17 to very soon in this class.

06:18 And so how might we
represent a score, maybe as

06:22 a set of parts with measures
and notes in between?

06:24 

06:27 From the virtual score,
we need to figure out, OK,

06:32 how is this going to look on
the page or on the screen?

06:35 And so we perform
layout estimation,

06:39 and we create a laid-out
score where it's not just

06:42 notes inside of an array
or a list or something

06:45 like that but actual
positions on a page.

06:50 And this involves
some technologies

06:52 that we'll be getting
to in the class.

06:54 Here's an example of very
poor layout estimation.

06:58 

07:01 From the laid-out
score, we choose

07:05 what the glyphs that
would be appropriate are

07:07 and where are they going
to be placed on the page?

07:11 A sample of some of
the things that might

07:13 be involved in doing that.

07:17 And then once we have
the laid-out score,

07:19 the glyph selection,
and placement,

07:21 we move to pixel
rendering, individual

07:25 dots no longer connected to
any semantic meaning but just,

07:28 is this x, y coordinate going
to be black, white, or something

07:33 in between or something else?

07:36 And from there, we have
particular technologies

07:40 that we're going to
need, such as screen

07:42 drawing, old-school cathode
ray tubes, LED display, things

07:47 like that, or how to actually
make a printer distribute ink

07:51 on a page.

07:51 And these, again, are
engineering problems

07:53 that are beyond the scope
of this class but still

07:56 very, very important.

07:58 So let's look, again, a
summary of what we have here.

08:01 We move from the time
domain to frequency,

08:04 frequency to pitch connections.

08:06 We estimate the duration and
the tempo, creating full notes.

08:10 Create a virtual score
or logical score.

08:13 Some people separate
these two out.

08:15 Then we try to make the
layout and to the output.

08:19 At each of these
points in the process,

08:24 we can involve music
theory or musicology,

08:28 and we can learn aspects about
music theory or musicology

08:32 from the data that we're
getting at this point.

08:35 So, for instance, the
duration/tempo level,

08:39 we can start to ask, well,
what are the most commonly

08:41 used rhythms in this piece?

08:43 And from there, hey, let's
create a backing drum track

08:46 to accompany the soloist
because we figured out

08:50 what kinds of durations,
what kinds of rhythms

08:53 connect to this with
a database, so on.

08:56 Or at the frequency to
pitch connections level,

09:02 we can now understand,
based on which

09:04 overtones were removed, what
instruments were being used?

09:07 Are they playing in
their natural ranges?

09:09 And from there,
we might estimate

09:11 the year of this recording
based on particular sounds

09:15 and sound artifacts or
the year of the piece

09:18 based on instruments
that are used and so on.

09:21 So these are places where
music theory and musicology can

09:25 get data from this MIR process.

09:30 But there's another side that's
been much less talked about

09:33 and it's a place
of great potential

09:35 that I think people
in this class

09:37 will be able to
contribute to, and that

09:39 is going from music
theory or musicology

09:42 back and using
things that we know

09:46 about theory or history
of music or music studies

09:49 to enhance the quality
of the algorithms being

09:53 used in these places.

09:54 For instance, at the
pitch connection level,

09:57 we can say, well, let's
look at the metadata,

10:00 and it suggests that this
is a piece by Mozart.

10:03 He died in 1791.

10:04 So let's look at
those instruments.

10:06 Now, the frequency, overtone
estimation was saying, OK,

10:12 the most likely instrument
is electric guitar.

10:14 This is very likely wrong.

10:16 I mean, I don't know.

10:17 Maybe it's a modern arrangement,
but it's pretty likely wrong.

10:21 Why don't you try this overtone
profile of a fortepiano,

10:24 an early piano instead?

10:26 And wow, you find out, OK,
that was the second-best score

10:30 but probably the best one
when taking into account

10:33 the metadata on the piece.

10:34 

10:37 Or we can use music
theory and musicology

10:41 at the
frequency-detection level.

10:43 So we might say,
hey, all of the notes

10:44 you've been detecting around
this note have been in E major.

10:47 And then you hear an A sharp,
and that's a little fishy.

10:53 Oh, hey, there's
a runner-up note

10:55 of A natural that
was 95% as likely.

11:00 From a music-theory standpoint,
I think that, more likely,

11:05 we've detected the wrong note.

11:07 So these are ways that
music theory and musicology

11:10 can enhance this process.

11:13 Most exciting at all, though,
is when parts of the process

11:18 feed into music theory
and musicology algorithms

11:23 and are enhanced by it.

11:24 So we say, oh, hey,
given these frequencies,

11:26 pitches, durations, we get
the style of the piece,

11:30 and we suggest that
it's from the swing era.

11:34 And then we can help later
parts of the process by saying,

11:41 if the style of the piece
is from the swing era,

11:43 when you do your virtual
score, your logical score,

11:45 probably all those triplets,
those "yum, ba bum, ba bum,

11:49 ba bum" should be written down
and represented as eighth notes.

11:53 That's what,
conceptually, they are.

11:55 

11:57 But we can not
just move forward.

12:00 We can, at the
virtual score level,

12:02 maybe it's beginning
to lay out the score,

12:05 and they're putting
everything nicely into 3/4.

12:08 And the musicology or
music-theory algorithm says,

12:12 well, these rhythms are
highly unusual for 3/4 time.

12:17 Let's go back and rerun some
of the previous steps with that

12:21 notion that that was highly
improbable and try to make

12:25 the score again so we can
move backwards in time,

12:28 redo a particular part
of the process, rerun it,

12:32 and then maybe come up
with a different result.

12:36 We'll put this in 6/8.

12:38 So here are some of the ways
that music theory and musicology

12:41 can feed back into the MIR
sound-to-score process.

12:47 Next time, sometime
soon, I hope to say

12:50 how we can go the
opposite direction, how

12:53 we can take a score and
automatically perform it.

12:56 And even though
we're going to be

12:58 going in the opposite
direction, it

12:59 turns out that there's a totally
different set of problems

13:02 that we have to solve.

13:04 

