---
title: YouTube Transcript: Video 7a: Unlocking Duration and Note Objects in music21
created: 2026-10-01
updated: 2026-10-01
type: video
source_url: https://www.youtube.com/watch?v=nr0RErrOPKk-transcript
source_type: video
ingested: 2026-10-01
published: recent
duration_minutes: 20
language: en
time_sensitive: True
---


# YouTube Transcript: Video 7a: Unlocking Duration and Note Objects in music21

## Video Information
- **Title**: Video 7a: Unlocking Duration and Note Objects in music21
- **Video ID**: nr0RErrOPKk
- **Published**: Unknown
- **Views**: Unknown
- **Language**: en

## Transcript
00:00 [SQUEAKING]

00:02 [RUSTLING]

00:04 [CLICKING]

00:07 

00:08 MICHAEL SCOTT ASATO
CUTHBERT: This

00:09 is a short video following up
on the unlocking of pitches,

00:14 where we will unlock duration
and note objects in music21.

00:19 Go ahead and start up
your Jupyter Notebook,

00:22 and let's get programming.

00:26 Start with durations.

00:28 So go ahead and from
music21 import duration.

00:32 And that thing we've just
imported-- duration--

00:37 put a thumbs up
if it's an object.

00:40 Put a thumbs down if
you think it's a module

00:44 OK.

00:45 So in this case, it is a module.

00:49 If you didn't get
it right no worries,

00:51 because there is no way you can
actually tell just from that,

00:55 except for by convention.

00:56 Python, by convention, we
write our modules in lowercase.

00:59 We can see that it's a
module by checking its type.

01:03 Yay, good.

01:04 Phew.

01:04 It'd be terrible if I didn't.

01:05 Within the module, there
is usually an object

01:10 with the same name as it.

01:12 I hit tab and I get, oh,
there is a Duration object.

01:15 So we'll create
one, assign it to d.

01:18 And I'm going to create
a duration of 3.0.

01:23 What I want you to do
is open up the chat,

01:25 and don't yet hit enter on
it-- but if you could put what

01:30 you think 3.0 might represent.

01:33 

01:40 Yep.

01:40 So we have a lot
of beats going on.

01:44 Some-- I like qualification
with some standard of how long

01:48 a beat is.

01:49 And we also have dotted
half and things like that.

01:52 Nobody seems to like our
favorite thing, milliseconds.

01:56 Maybe if I had purposely
made my thing 3,000,

02:02 then people would
have thought that.

02:04 But it is a flow.

02:05 It could be seconds
or something.

02:07 In this case, we'll
figure it out.

02:09 Well, OK, that doesn't
tell us much of anything.

02:13 And what we can do is, we
can get the full name of this

02:18 and see it is a dotted half,
so it could be beats still.

02:25 I'll just go ahead
and say, in music 21,

02:28 I made the decision to
have the number represent

02:32 the number of quarter notes.

02:35 Over time, I have sometimes
regretted that decision.

02:38 But they had to be something.

02:40 And one of the reasons I
decided not to go with beats

02:45 is that the length--

02:49 the representation of a
note, in terms of beats,

02:52 is dependent on
something external.

02:54 And that is the time
signature, right?

02:57 So 2/2 has a different
type of beat from 6/8,

03:04 which has a different
type of beat from 4/4.

03:06 So that's one of the
reasons going with this.

03:10 So every Duration
object has a full name.

03:14 It also has a type--

03:16 half-- and it has dots.

03:20 It's great.

03:22 It also has something
called quarterLength,

03:25 which in this case is
the number of quarters.

03:29 And that's not so bad.

03:30 But that's something you
already knew how to do.

03:33 But maybe we can create a
duration in a different way.

03:38 We'll say type='whole'
and dots=4.

03:43 And suddenly, the
quarter length of this

03:48 is a little bit
harder to compute.

03:50 Anybody know off the
top of their head?

03:54 Right, you're all
too shy to say 7.75.

03:57 OK, good.

03:58 Well, I don't know that number.

04:00 OK, so here are some of
the things that we can do.

04:06 Can we create a triplet?

04:09 Let's try that.

04:11 

04:16 1/3 of a note-- so what
kind of a triplet is that?

04:19 Somebody shout it out.

04:22 AUDIENCE: An eighth
note triplet?

04:24 MICHAEL SCOTT ASATO
CUTHBERT: Let's see.

04:25 Type-- yay, eighth note triplet.

04:28 So we can create triplets.

04:30 Notice-- we'll go
back to d here.

04:34 Notice that some durations
are expressed in floats.

04:38 Some are expressed in
rational fractions.

04:41 And that tells
you whether or not

04:44 you're going to safely
be able to add them up

04:46 and get an exact number.

04:48 Anything that's a multiple
of a power of 2 in binary

04:52 will be exactly representable.

04:54 Anything that
isn't will be here.

04:56 So great.

04:56 So trip, its type is eighth.

05:01 So that doesn't tell
me anything about it.

05:02 Its dots, I hope, are 0.

05:05 There's no dots there.

05:06 Great.

05:07 So there is something
called tuplets,

05:12 which a tuplet is a type of--

05:15 like, a quadruplet,
a quintuplet.

05:17 Triplet is the one we most know.

05:19 Great.

05:20 What I want you to do is, take
a second and put in the chat,

05:23 what kind of object was just
returned from dot tuplets?

05:29 OK, we have a couple
different answers.

05:33 But most people
say it's a tuple--

05:36 a tuple of tuplets, which--

05:39 try not to say that
too many times fast.

05:41 And you know it's
a tuple because it

05:44 has this comma at the end.

05:46 So it's an immutable--
a list of it.

05:50 And that means you can have
more than one template.

05:53 So you might have a triplet
within a triplet and so on.

05:56 So those are some
things we can do.

06:01 So we can get at that
darn tuplet object.

06:03 I'm just trying to pull
it out, pull it out.

06:06 Oh, right.

06:07 It's not a graphical
environment.

06:09 So we'll get the first one.

06:11 We'll call it t.

06:14 And we'll see that the tuplet
itself is also a complex object.

06:20 We can dir it.

06:22 And we can see it has certain
things like, tupletMultiplier,

06:26 which I happen to
know is a method.

06:30 And so we can see that when you
throw this tuplet onto a note,

06:34 that note becomes
2/3 of its previous.

06:37 Here are just some of
the things you can do.

06:39 You will learn this in
the music 21 user's guide

06:46 2 and 3, which we'll
get to in a bit.

06:49 Some of the things you
might see are duration--

06:54 that, obviously, 4 is a whole.

06:59 For people who
like these things,

07:01 8 is a double whole note,
also called a breve,

07:06 which means short, because
there used to be longer notes.

07:10 And they're still somewhere.

07:11 And that's the
longest possible note,

07:14 which no longer exists, except
that somebody used a double,

07:18 the longest possible note.

07:19 But then at a certain
point, you can't do it.

07:22 Similarly, on the small
side, you can go--

07:25 

07:27 oops-- and let's get
the type of that.

07:31 Notice that the type of an
eighth note is E-I-G-H-T-H.

07:36 The type of a 16th note--

07:40 I misspelled 16th
too many times.

07:42 So I decided we'd go from here.

07:47 I don't think I know my
fractions below that,

07:50 so we'll just keep
going like that.

07:52 You can go down pretty far.

07:54 Let's skip a bit--

07:55 oops-- we're at 16.

07:58 And you can go down
to 1024th notes.

08:04 Theoretically,
notes go on forever.

08:05 But music21 at a
certain point says, this

08:12 isn't representation music.

08:15 Great.

08:16 I want to do one
more little exercise.

08:19 And this is a trick question.

08:21 So just put your
head what you think.

08:24 I'm going to sing
something to you,

08:26 and you tell me how
many notes I sang.

08:29 [SINGS NOTE]

08:33 Yes, I sang a eighth note tied
to a 32nd note because it was

08:38 slightly longer than half
of a beat in my head.

08:41 So how do we deal
with things like that?

08:43 Well, let's make it a whole
note tied to a quarter note.

08:45 Let's say the duration was fast.

08:46 So I'll call that an odd thing.

08:48 And by the way, thank
everybody for saying 1 and not

08:52 saying 7 because Cuthbert
warbles too much.

08:56 But let's take that eighth
note tied to a 32nd note.

09:02 What is that?

09:03 0.125.

09:07 So we can see that
you can create things.

09:10 And this says it's complex.

09:11 It is a duration
that has multiple--

09:15 what I call components, which
there's an eighth and an eighth

09:21 and a 32nd that
are put together.

09:23 And so what we mean by
the length of a note

09:29 and where a note splits
will depend on the context

09:32 that we want to use it.

09:34 So if we're thinking
about, hey, he just

09:38 sang that note in a sound
context, in a recording context,

09:41 obviously, that's one note.

09:43 There's no other way around it.

09:47 But if we're thinking about
it in a notation context

09:49 and you're writing
something that

09:51 has to draw notes
on a page, you're

09:54 going to want to say that,
well, that's actually two notes.

09:59 Because there's no way to
represent the duration that we

10:02 heard with just one note.

10:05 So some of the
things we're going

10:06 to be working on
in this class is,

10:08 how do we move from one
representation to another

10:11 so that we're always using the
representation that is most

10:16 appropriate for the situation?

10:18 And so we'll spend a lot of
time in this class working

10:22 on translations among
representations.

10:26 Remember, you can always
take the directory

10:32 of music21 or any
Python object to get

10:36 some more things about it.

10:38 But also, in Jupyter, you
can put in question mark

10:43 afterwards and get some docs
or look at the docs online.

10:47 So now you have
unlocked pitches,

10:49 and you have unlocked durations.

10:52 Let's move on to the last
thing that we want that we're

10:57 going to unlock today.

10:59 And those are notes.

11:03 So there are a
million ways we could

11:07 have called something a note.

11:10 We could say, a note is
the same thing as a pitch.

11:14 Some people say that.

11:15 But here's how I have chosen,
with my advisors and stuff,

11:22 how to represent a note.

11:23 A note takes in a string,
just like a pitch,

11:28 just like you saw
in the pitch video.

11:31 And it's called a note.

11:33 It doesn't print the
octave, for some reason.

11:37 And it has a name,
just like a pitch does.

11:42 But also, all those things
are in a stored pitch object.

11:47 So a note has a pitch object.

11:51 And so you can change that--

11:53 n.pitch.octave = 4.

11:54 

11:59 And see all that.

12:01 But a note also has a duration.

12:05 And so in this
case, the default,

12:07 all notes start off with a
duration of one quarter note.

12:11 I don't know why I'm
privileging quarter notes,

12:13 but somehow, I have.

12:15 We can change the
quarter length of that--

12:19 3.5.

12:21 And then, well,
it has a fullName.

12:24 So we can look at this--

12:26 'B-flat in octave 4
Double Dotted Half Note'.

12:29 OK, so that's all there.

12:32 Hopefully this is working.

12:33 One cool thing that
you can do that you

12:35 can't do with a
pitch or duration,

12:37 really, is, you can show a note.

12:39 It's weird that the first
time, it always takes longer.

12:41 And then it's later,
so here we go.

12:44 We have a particular note.

12:46 It figures out some
kind of context for it.

12:49 Has a couple other
things we can do--

12:51 we can change the
notehead to be an x.

12:55 We can change the
note to be no red.

12:59 I'm slightly colorblind, so I
can't really see the difference.

13:03 But you can tell
me if that works.

13:08 Yep.

13:08 And we can also make
it into a complex note.

13:15 So I think we
learned 6.25 couldn't

13:19 be represented normally.

13:20 But we can see that
music21 will figure out

13:25 how many notes are necessary
to represent it on the staff.

13:31 There's other
miscellaneous things.

13:34 You can give it a
lyric and so on.

13:38 So again, everything
there is in the--

13:42 during it.

13:44 And you'll see there's
a lot of stuff.

13:47 And we're going to get
through a good chunk

13:50 of learning these things later.

13:52 No, you will not be
ever quizzed on, OK,

13:56 what does purgeOrphans
mean on a note?

13:59 It's not that kind of class.

14:01 But I want you to feel free--

14:05 play around with this.

14:06 Play with anything except,
just like with pitch,

14:09 anything that begins
with transpose

14:12 is off limits,
only because it'll

14:17 make the problem set where we do
a lot of things with intervals

14:22 a lot less fun.

14:23 Because you're not using it.

14:25 Anyhow, this is the end of
the unlocking for topic 1.

14:32 

