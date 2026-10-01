---
title: YouTube Transcript: Class 27 Video: Feature Extraction and Machine Learning
created: 2026-10-01
updated: 2026-10-01
type: video
source_url: https://www.youtube.com/watch?v=ivvxfWR1azI-transcript
source_type: video
ingested: 2026-10-01
published: recent
duration_minutes: 20
language: en
time_sensitive: True
---


# YouTube Transcript: Class 27 Video: Feature Extraction and Machine Learning

## Video Information
- **Title**: Class 27 Video: Feature Extraction and Machine Learning
- **Video ID**: ivvxfWR1azI
- **Published**: Unknown
- **Views**: Unknown
- **Language**: en

## Transcript
00:00 

00:00 [SQUEAKING]

00:02 [RUSTLING]

00:04 [CLICKING]

00:06 

00:09 MICHAEL SCOTT
ASATO CUTHBERT: OK.

00:10 Let's get started right on time,
both to set a good precedent,

00:14 and there's quite
a bit to do today.

00:18 Oh, I will put that
back down for one

00:20 second so that those
who just got in

00:21 can see the agenda for today.

00:24 

00:28 First two things will just
be like a minute or two,

00:31 and then we'll spend the rest
of the time on what everybody

00:35 thinks is the coolest
thing in the world

00:38 these days in computation,
artificial intelligence

00:41 and machine learning.

00:42 But this is not a class in that.

00:44 We'll spend most of our
time on feature extraction,

00:48 the necessary evil
before doing great things

00:52 with artificial
intelligence and machine

00:53 learning when you're dealing
with data that's not already

00:57 numbers.

00:58 I want to do a really quick
discussion on something

01:04 on problem set 7/8.

01:06 I'm still listening
to the compositions.

01:08 Some of them are
really, really cool.

01:10 Just, they're all great,
that I've heard so far.

01:14 But some really went into it.

01:17 But there was one thing
that, among people

01:21 who attempted every
problem, ended up

01:23 being a consistent error.

01:26 Actually, two things.

01:28 One that a lot of people
missed here was in--

01:34 let's say you were in C
major, because that'll

01:36 make life easier.

01:38 I gave some chords
that were like this.

01:46 And what do we call
this in C major?

01:50 What's the sca--
in Roman numeral.

01:52 We're doing the Roman numeral
exercise for a second.

01:55 What scale degree?

01:56 STUDENT: A ii.

01:57 MICHAEL SCOTT
ASATO CUTHBERT: ii?

01:58 Good.

01:58 And what is the
quality of the chord?

02:01 STUDENT: Diminished.

02:02 MICHAEL SCOTT ASATO
CUTHBERT: Diminished, great.

02:04 So you don't have your problem
set back for two reasons.

02:07 One, there are a couple
more songs I'm listening to.

02:09 And also-- so how would
we write ii diminished?

02:13 STUDENT: Circle.

02:13 MICHAEL SCOTT ASATO CUTHBERT:
With a circle, yeah.

02:15 And then I noticed that my thing
said, or if it's vii diminished,

02:25 write this.

02:26 And I did not say, in general,
if it's diminished, write this.

02:31 So I think that some
people seem to write

02:33 specific code for making sure
that it only happened on vii.

02:39 But ii diminished
happens quite often.

02:42 How does it happen in C major?

02:45 You're borrowing from C
minor for a little bit.

02:49 So these borrowed chords,
either flat and natural.

02:55 And then you end up with
that D-F-A flat chord.

03:00 So that's where that comes
in, but I want to make sure.

03:02 I'm going to go
back because there

03:04 was an ambiguity in
the instructions,

03:06 and I want to make sure that
everybody gets the little point

03:09 back who made that,
who didn't put that in.

03:13 So that was one of the
two systematic issues,

03:16 and that came from
an ambiguity for me.

03:18 Here is the other one that came
up a lot that I want to address.

03:26 Oh, yeah.

03:27 So we just went from C major.

03:29 [PLAYS PIANO]

03:31 And we played--

03:32 [PLAYS PIANO]

03:33 --that ii diminished sound.

03:36 Then what about this sound?

03:40 [PLAYS PIANO]

03:42 

03:45 Anyone identify
that chord by ear?

03:50 Or just the-- what's that?

03:51 STUDENT: Augmented.

03:52 MICHAEL SCOTT ASATO
CUTHBERT: Augmented, great.

03:54 [PLAYS PIANO]

03:56 Good.

03:56 I was in, doing that
borrowing from minor thing.

04:03 And I left my blue pen, which
probably shows up better.

04:07 I was borrowing from minor and
I started on the third scale

04:10 degree.

04:10 And so this was not part of
your Roman numeral thing,

04:13 but it came on the
roots question.

04:16 

04:18 What is the root of that chord?

04:23 STUDENT: It could
be any of them.

04:25 MICHAEL SCOTT ASATO
CUTHBERT: No, it cannot.

04:26 Ah, we'll get to that.

04:28 That's where something happens.

04:29 Yep, exactly.

04:30 It's a great, great idea.

04:31 John?

04:32 STUDENT: E flat.

04:33 MICHAEL SCOTT ASATO
CUTHBERT: E flat.

04:34 Now, we'll get to
it in just a second.

04:38 What is the root of that chord?

04:46 

04:49 STUDENT: G.

04:50 MICHAEL SCOTT ASATO CUTHBERT: G.
And let's see if I can make one.

04:56 We'll go back to our E flat.

04:57 

05:02 What is the root of that one?

05:06 STUDENT: C flat.

05:06 MICHAEL SCOTT ASATO
CUTHBERT: C flat.

05:08 Now, why is it?

05:09 And so, just so we all
have it in our ears again--

05:13 [PLAYS PIANO]

05:15 

05:17 Three chords, three
exact same sound.

05:20 But roots, the
concept of root is

05:23 something that comes
from a triadic, sort

05:27 of a spelling-enabled thing.

05:30 So where do we find the root?

05:32 We talked about the
algorithm last time.

05:35 What do we want to find?

05:37 A bunch of stacked--

05:38 STUDENT: Thirds.

05:39 MICHAEL SCOTT ASATO
CUTHBERT: Thirds.

05:40 Good, I heard it.

05:40 So stacked thirds.

05:41 So here, we have a third,
followed by a third,

05:44 or a third and a
fifth, depending

05:45 on how you're counting.

05:46 But here, what's this interval?

05:48 STUDENT: Diminished.

05:49 STUDENT: Diminished iv.

05:49 STUDENT: Diminished iv.

05:50 MICHAEL SCOTT ASATO
CUTHBERT: Diminished iv.

05:51 Yeah, a iv of some sort.

05:52 So we have to move it up
the octave in order to get

05:58 our stacked iii's.

06:01 And here, we can move them both
up an octave in order to get

06:08 our stacked iii's.

06:09 So the diminished--

06:11 The augmented triad
is one of the places

06:14 where the concept of root has
everything to do with spelling.

06:20 There's one other very common
chord where the concept of root

06:24 has everything to
do with spelling.

06:26 You saw a big smile,
and it's not a triad.

06:31 Go ahead.

06:32 STUDENT: Diminished vii?

06:33 MICHAEL SCOTT ASATO CUTHBERT:
Diminished vii chord, yeah.

06:35 Here, I'll just keep
it in the light.

06:37 Assuming that's good.

06:38 So yeah, diminished vii chord.

06:40 Let's say we're in C minor.

06:42 We're going to start on
B. Would somebody shout

06:48 out the next note?

06:50 STUDENT: D.

06:51 MICHAEL SCOTT ASATO
CUTHBERT: D. Keep going.

06:53 STUDENT: F.

06:53 MICHAEL SCOTT ASATO
CUTHBERT: F. And then?

06:55 STUDENT: A flat.

06:56 MICHAEL SCOTT ASATO
CUTHBERT: A flat, yeah.

06:58 So vii, then we have
vii with a root on B.

07:02 But we can change this
to move it up an octave

07:07 and flip the enharmonic.

07:08 

07:12 And suddenly, we have iii, iii,
iii, and our root becomes D.

07:21 We've got a lot more
to get through today,

07:22 so I will leave it to a test
to prove to yourself that we

07:26 can keep doing this somehow, and
get all, every one of the four

07:30 notes, as a diminished--
as having its own,

07:37 that note as a root.

07:38 So each of the chord factors,
depending on how you spell.

07:41 And that's one of the
reasons, by the way,

07:43 this gets away from the
computational side, but maybe

07:45 a cool computational
compositional tool.

07:48 One of the reasons why a
diminished vii chord is often

07:51 a very useful way to
modulate to remote keys,

07:55 because you just sort of start
emphasizing a different note

07:57 as your root.

07:59 

08:02 Any questions on this,
or on other things?

08:05 We're all eager to get
to feature extraction?

08:08 On this, there should be a
notebook that says, under today,

08:16 2023-ai-template-blank.

08:21 That one.

08:22 Is it?

08:23 STUDENT: Yep, it's there.

08:23 MICHAEL SCOTT ASATO
CUTHBERT: It's there.

08:24 Good, good, good.

08:24 So feel free to download that
and put that where you are,

08:28 and run it.

08:30 It will install.

08:32 If your hard drive is
almost completely full,

08:35 it will install a learning
toolkit called Orange, which

08:40 also installs another
machine learning toolkit

08:43 called scikit-learn, and I think
they might be a little bit big.

08:46 Might be-- whatever.

08:47 So make sure to run all
first, and that will get you

08:53 in a pretty decent shape.

08:56 I'm going to get started on--

08:58 what we're talking
about today is something

09:02 called feature extraction.

09:04 And so feature extraction
is a conversion of elements,

09:08 in this case, musical elements,
into single numbers or lists,

09:14 arrays, vectors, tensors,
whatever you want to call them,

09:18 of numbers.

09:19 It is the most boring thing
I will teach in the class.

09:23 And please don't correct me
if you're like, Cuthbert,

09:25 there's plenty of other
boring things you've done.

09:27 But no, it's really one of the
most boring things in the world.

09:31 And here's a reason to hate it.

09:34 It really sucks the
lifeblood out of music.

09:37 Everything that you
love about music

09:39 is going to be converted
into a few numbers.

09:42 It is-- sucks the life out.

09:44 It is the zombie of music world.

09:47 Adam's very excited.

09:48 Yes, zombie invasion!

09:49 But there's a lot
of amazing things,

09:52 we know, happening in artificial
intelligence, machine learning,

09:56 deep learning, algorithms,
all these things.

09:58 And as far as I know, they
all have one thing in common.

10:03 And that is, they
work on collections,

10:06 big collections of numbers.

10:09 There's some ways
that you can work

10:12 with images that, effectively,
are kind of like two-

10:17 or multi-dimensional
arrays of numbers.

10:18 But basically, they're
all going to be numbers.

10:21 So when I put some music
notation on the board,

10:29 we're not going to be
able to work with that,

10:31 even an image of
it, even a JPEG,

10:32 unless we convert it to pixels
and convert it to numbers.

10:35 When you hear a
sound, [VOCALIZING]

10:38 something like
that, you're going

10:39 to have to convert that
into numbers in some ways.

10:45 So we're going to be just
working on converting things

10:49 to numbers.

10:49 So it's pretty simple, and--

10:54 but how to do it,
and what to extract,

10:58 and how to make
your extractions,

11:00 is the deep art
that takes a while.

11:04 Now, I'll get to a little
bit later some of the things

11:08 that people are
doing today, where

11:09 feature extraction is less--

11:11 or careful feature
extraction is less important.

11:14 And I'll tell you what those
things tend to have in common,

11:18 and that is, they work
on much bigger data sets

11:22 than what we have.

11:24 So we're going to
get started on this.

11:27 Yep, that's my template here.

11:29 And we're going to
start with, why not?

11:32 We always start with our
favorite Bach chorale.

11:36 What's the number?

11:37 STUDENT: 66.6.

11:38 MICHAEL SCOTT ASATO
CUTHBERT: 66.6.

11:40 Conjure up the bwv66.6.

11:46 I'm going to show
it, get it back.

11:47 

11:59 OK, great.

12:04 So we're going to do some
manual feature extraction first.

12:08 We're going to convert
this into numbers.

12:10 I'm going to extract two things
from this, number of parts

12:14 and initial number
of beats per measure.

12:18 So let's just do our--

12:22 You don't have to type
this if you don't want.

12:24 numParts equals 4.

12:25 Time signature.

12:27 Numerator equals 4.

12:29 There, I have done manual
feature extraction,

12:32 and describing the
piece as two numbers.

12:36 They seem to look like 4-4,
but I didn't ever just extract

12:40 the denominator.

12:41 That just happens to be
coincidence they're both 4.

12:43 So I don't know if we'd even
call this feature extraction.

12:47 But you can see, it's pretty--

12:49 we were not talking about
very, very much here.

12:52 So I'm going to define an
automatic feature extractor.

12:59 So we'll call it extract_meter.

13:01 And extract_meter,
you can save time

13:03 by not putting
these annotations.

13:05 It takes in some
sort of a stream.

13:07 I'm calling it score,
even though it's not.

13:11 And it returns two integers.

13:14 What do you think the two
integers are going to be,

13:18 if you're extracting the meter?

13:21 STUDENT: Numerator.

13:21 MICHAEL SCOTT ASATO CUTHBERT:
Numerator and denominator,

13:23 great.

13:23 Super.

13:24 So we can say, all the
meters in the piece

13:27 equals the score meter,
TimeSignature, recurse.

13:32 And the first one, we'll just
get the first one. first_meter,

13:38 all_meters 0.

13:43 And we'll return
first_meter's numerator

13:48 and first_meter's denominator.

13:52 I know I don't need
the parentheses,

13:53 but I just kind of
got used to that.

13:56 

13:59 So I'll let people
get caught up.

14:04 Now, by the way, how
many time signatures

14:08 does this little chorale have?

14:10 Are we going overkill by
getting the first one?

14:13 

14:17 Do you want to take a guess?

14:19 You all know it by now.

14:21 1?

14:21 

14:24 It actually has 4, the
way music 21 counts.

14:27 1, 2, 3, 4.

14:29 They're all the same.

14:30 But this is an error
I make quite a bit

14:33 often, that each of the parts
has its own time signature.

14:36 So this is something
to be careful on.

14:39 And now, we'll get
to the first sort

14:40 of ethical dilemma of feature
extraction and machine learning,

14:46 of which there will be many.

14:48 And quite a number today.

14:50 What happens if a score doesn't
have any time signatures?

14:55 Do we want this?

14:56 Will this crash, first off?

14:59 And if you think
it will crash, tell

15:01 me what the error that's
probably going to be returned.

15:06 STUDENT: List
index out of range.

15:08 MICHAEL SCOTT ASATO
CUTHBERT: List index

15:08 out of range, or index error.

15:10 Yep, that we're trying to get 0.

15:12 So we can say something
like, if not all_meters.

15:20 Now, so here's the
ethical dilemma.

15:22 I'm going to return 0
comma 0 as a special value.

15:26 That's also an integer, tuple
of two integers, that says,

15:31 I have no time
signature because I've

15:35 raised as a medieval
musicologist,

15:37 so I have Gregorian
chant lying around,

15:39 and other meterless
time signature pieces.

15:42 But the other reason
is that we sometimes,

15:46 in case of an error or
an out-of-bound value,

15:50 we return some sort of,
we call it the sentinel,

15:53 some kind of special
meaning number that says

15:57 some sort of an error happened.

15:59 Why?

16:00 Because you're going to someday
have a gigantic data set.

16:04 Maybe you're going to be
doing this up in the cloud

16:06 somewhere or something,
and you're going to have--

16:10 

16:13 you're going to be
letting it run overnight,

16:15 consuming a huge amount
of processor money.

16:18 And eventually, there's going to
be some bad data in there that's

16:21 going to crash your system.

16:23 And you want to be like, OK, I
just let this run for 47 hours,

16:28 and now I have to
start all over again.

16:30 Because, of course, I
didn't save intermediary

16:32 values, because I'm a
theoretical person, not

16:35 a practical programmer.

16:37 But always save.

16:39 Write to disk every
once in a while.

16:41 But so this type of
thing helps to save you

16:45 from a little bit of bad data.

16:47 What it also does, though, is it
can swallow up systematic errors

16:51 in your thought.

16:52 You know what I'm saying?

16:53 That you didn't realize that--

16:57 the one that I
always get is, I'm

16:59 looking at the
pitch of everything

17:01 in the piece, pitch of
everything in there.

17:03 And then I forget that these
structures called chords exist,

17:07 which don't just have a
pitch, they have multiple.

17:09 And so I could end up silently
throwing out all of my data

17:14 about chords, rather than
realizing I have a mental model

17:18 problem in there.

17:19 And this is some
of the things that

17:21 can lead to AI that
doesn't include all of us,

17:25 that programmers
forget that women exist

17:28 or that non-white people exist.

17:29 And therefore, oh, that's
data that's out of bounds.

17:32 So we'll go with a
default response,

17:35 rather than learning how to
deal with facial recognition

17:39 on things like that.

17:40 So here, it's not such a big--

17:44 I don't think that
we're going to have

17:46 a problem with systematically
discriminating against Gregorian

17:50 chant.

17:51 But it's these
kinds of issues that

17:54 lead to so many of the
other ethical issues

17:58 in artificial intelligence.

18:02 With that aside,
we've all caught up.

18:04 Let's see, did I, somebody--

18:06 and everybody just save me time
when I type something wrong.

18:10 Check it.

18:10 But let's see if that works.

18:12 Whew.

18:13 extract_meter(bach).

18:15 We have our first, our first
automatic feature extractor.

18:22 Is this topic, so far,
as boring as I promised?

18:25 STUDENT: No.

18:26 MICHAEL SCOTT ASATO CUTHBERT:
No OK, Somebody likes it.

18:28 Yeah, it's pretty good.

18:29 But let's go with
something else.

18:31 And we're going to start
with another ethical dilemma.

18:33 We're going to be working with
Ryan's Mammoth Collection.

18:38 And I think, if you
type "blooming,"

18:42 you should get something
that's not an error.

18:44 Do you?

18:45 Because you've already--
if you've run everything,

18:47 you've already run corpus,
parse, BloomingMeadowsJig.

18:54 And let's see that.

18:56 So apologies we didn't get
to the jig composition yet.

19:01 I do plan to pick
that up next week,

19:04 but I figure that there's
some other things that people

19:06 need for their final
projects, more importantly

19:09 than working with that.

19:11 So you all see
something like this,

19:15 but we're going to be back on
jigs again today for a bit.

19:18 Now, Ryan's Mammoth
Collection is

19:20 a little bit of an
ethical dilemma,

19:22 and I'm trying to replace it.

19:23 It is a collection of, I think,
something like 1.079 fiddle

19:30 tunes from the 19th century.

19:34 And that has a bunch
of jigs, hornpipes,

19:37 things that if you
take Joe Maurer's Sea

19:40 Shanties and English Folk Music
class and all those things,

19:45 you can learn more about them.

19:48 It also is a large collection
of musical experiences of 19th

19:54 century African-Americans
that has been parodied and/or

20:00 appropriated into
white minstrel shows.

20:03 So I've tried to remove
things that are offensive,

20:10 on first sight, from
the collection, titles

20:13 and things like that.

20:15 But the deeper history,
a lot of these songs,

20:19 has to do with a lot
of appropriation.

20:21 So I'm hoping to be
able to get a collection

20:24 to replace it at some point,
because it's not exactly

20:29 everything that I
want to do with it.

20:31 But anyhow, so we have-- for
going through, we have the one

20:34 jig, Blooming Meadows jig.

20:37 And I gave you just a
contrast, a reel, R-E-E-L,

20:44 and you should already have the
reel, I think, already loaded.

20:47 So you don't need to type this.

20:49 It's called the
"7th Regiment Reel."

20:51 And hopefully, I got that.

20:54 

20:58 And it looks a
little bit different.

20:59 

21:04 So what we're going
to do today is

21:06 try to build a system that
can tell the difference

21:09 between a jig and a reel.

21:11 Or a jig and--

21:13 try to fit it into the
remaining 52 minutes

21:16 between a jig and a not-jig.

21:18 The whole, all of music is
divided into jigs and not jigs.

21:23 It's great.

21:26 So we we'll be looking--

21:29 how would you define
the difference?

21:31 You can look down
at your own so I

21:33 don't have to keep
scrolling back and forth.

21:35 Just, if you're somebody
who didn't know,

21:39 hadn't encountered a reel or
a jig before, what is the--

21:45 what would you say is
an obvious difference?

21:48 Matthew?

21:49 Do you--

21:50 STUDENT: 2/4 versus 6/8?

21:51 MICHAEL SCOTT ASATO
CUTHBERT: 2/4 versus 6/8.

21:52 Good.

21:53 Another signature?

21:56 STUDENT: It's the
essential one, I think.

21:58 MICHAEL SCOTT ASATO
CUTHBERT: What's that?

21:59 STUDENT: It's the essential
one, the time signature.

22:01 MICHAEL SCOTT ASATO CUTHBERT:
The same one, time signature?

22:02 Good.

22:03 Yeah.

22:03 STUDENT: So the [INAUDIBLE]
seems more syncopated.

22:06 MICHAEL SCOTT ASATO CUTHBERT:
Which one seems more syncopated?

22:08 STUDENT: The jig.

22:08 MICHAEL SCOTT ASATO CUTHBERT:
The jig, a little bit more

22:09 syncopated?

22:10 Especially things--
there's always

22:12 things like this that are
not, technically, rhythmically

22:16 syncopated, but kind
of feel a little bit.

22:19 Mm-hmm.

22:21 Good.

22:21 Anything else?

22:23 Yeah, Marlon.

22:24 [NOTIFICATION TONE]

22:25 STUDENT: [INAUDIBLE]

22:25 MICHAEL SCOTT ASATO
CUTHBERT: What's that?

22:27 STUDENT: I said 16th
versus eighth notes.

22:28 MICHAEL SCOTT ASATO CUTHBERT:
16th versus eighth notes.

22:29 Thank you.

22:30 I'm going to put
that in, and I'm also

22:32 going to disable my, my what do
you call it, my notifications.

22:37 Supposed to happen
automatically.

22:40 OK, yeah.

22:41 16th versus eighth notes.

22:42 We're actually going to
possibly use that as something.

22:46 So we're going to try
to have a system that

22:49 can do the difference.

22:51 You should have--
if you type ryan,

22:55 you should be getting something.

22:56 I'm going to really
quickly just cut and paste

23:00 what I did to get to
ryan and explain it.

23:03 I first created
something called ryanM,

23:05 where I find everything in
Ryan's Mammoth Collection.

23:09 And then what I've
done is, here's

23:13 another cut and
paste, 1059, I think,

23:16 yep, is that I've gone
through everything in there.

23:20 And said, first off,
I only want to look

23:22 at the first 500 of them.

23:24 And then, I'm looking, without
parsing, if the name of the file

23:29 has jig in it.

23:33 If it doesn't have jig in it,
and if you're over file 100,

23:36 continue.

23:37 So why did I do all this stuff?

23:39 Just so that I can get something
that is approximately 50/50 jig,

23:44 not jig.

23:45 So we end up with about 200.

23:49 Here, we can-- we end
up with 212 pieces,

23:54 and I happen to know that
59% of them are jigs.

23:58 So that's pretty good.

24:00 These are all what we
call metadata entries,

24:03 so they haven't been parsed yet.

24:06 OK, great.

24:08 Everybody with me?

24:10 There.

24:11 Great.

24:12 I'm going to define a
helper function that is--

24:18 how many ethical dilemmas
are we doing today?

24:20 This one's ethical, but this
one's sort of a research thing

24:23 called is_jig, which
determines if something

24:29 is a jig by looking
at the file name

24:35 and lowercasing it, and seeing
if the word jig is in that.

24:40 I've done this with rags before,
ragtime, a really great piano

24:47 genre.

24:48 Scott Joplin, the
most famous person.

24:50 And a lot of rags have
"rag" in the title.

24:53 "Maple Leaf Rag," and so on.

24:56 But then, there's "The
Entertainer," [VOCALIZING]

25:00 

25:00 --which doesn't have the
word "rag" in the title.

25:03 So we're possibly having what
we call a bad ground truth.

25:11 The ground truth
is the definition

25:14 that is correct beforehand.

25:17 And so, is this song a jig?

25:20 Is this not a jig?

25:21 This is probably not the
greatest ground truth there.

25:24 The other thing that
will come up a lot

25:27 is that there is some
pieces that will be

25:31 very hard to tell if they are.

25:34 And two different,
intelligent people

25:36 could disagree on
something that's a jig.

25:38 This comes up a lot in
genre classification,

25:41 where people can't really
decide, is this country

25:45 or is this rock?

25:47 Is this funk?

25:48 Is this hip-hop?

25:50 Is this romantic?

25:52 Is this classical?

25:54 So somebody once
told me, when they

25:58 realized I came from a music
history training, musicology,

26:02 they said, the worst part
about musicologists getting

26:04 into this field is that they
give us really crappy ground

26:08 truths.

26:10 You all won't say what
the right answer is.

26:12 And that's, I hope, an
ambiguity we like as humans.

26:16 But anyhow, so we'll
have our is_jig.

26:21 We'll actually see,
is_jig(blooming).

26:26 I think that was the
one that is a jig.

26:28 And what was the other one?

26:30 A reel.

26:32 OK.

26:35 So with our garbage in, garbage
out, terrible ground truth, we--

26:41 seems to be working OK.

26:43 And I happen to know, 127 of
the things in there is jigs.

26:47 So let's get out second
feature extractor.

26:49 This one's going
to be pretty easy.

26:51 We'll just get the number
of sharps in the piece.

26:53 We started working
on jigs in G, so we

26:57 happen to know that there
are a whole bunch of them.

27:00 So maybe we'll do this.

27:01 And here, we can just do,
again, a try, return the scores

27:08 key.KeySignature,
the number of sharps.

27:12 If it's two flats, what's
it going to return?

27:15 STUDENT: Negative 2.

27:16 MICHAEL SCOTT ASATO
CUTHBERT: Negative 2, yep.

27:17 Great.

27:18 And if there's no
key signature--

27:21 this one's actually not a
terrible assumption, right?

27:23 Something without
a key signature

27:25 probably has a key signature
of no sharps or flats.

27:29 I don't know, maybe.

27:30 Maybe we should, in this
case, analyze the key

27:32 and do something like that.

27:34 But good enough for
just a little bit.

27:37 So let's see.

27:38 The blooming, hopefully
this will return 1.

27:43 Oops.

27:45 Oh, I know what I did.

27:47 This is why you should never
do something like this.

27:50 Except IndexError, we said, and
we didn't get an index error.

27:56 What did we get?

27:57 We got an AttributeError?

27:59 Yep, there is no
sharps, because I

28:01 forgot to say that we want the
first key signatures sharps.

28:05 You can also do the
dot 0 or bracket 0,

28:09 however you'd like that.

28:10 And so let me try
the get_sharps again.

28:14 Getting 1.

28:15 And what's the answer for Bach?

28:18 STUDENT: 3.

28:19 MICHAEL SCOTT ASATO
CUTHBERT: 3, good.

28:20 You can either do that by
hand or make sure [INAUDIBLE].

28:22 Great.

28:23 And we'll define one
more feature extractor

28:26 so that we can--

28:28 oops.

28:30 We're actually making
good time this--

28:33 we'll do eighth_fraction
based on the observation

28:38 that there's more eighth notes
in one piece than the other.

28:42 So we'll take in a stream.Score.

28:45 And this time, we'll
return a float.

28:47 So usually, you
can return an int,

28:50 which we call a continuous--
a discrete vari--

28:53 answer or a float, which
is a continuous variable.

28:56 So let's just do this.

28:58 We'll get the number
of notes in the piece.

28:59 Actually, you do this.

29:00 You give me-- go ahead and try
coding this for a little bit,

29:03 because we are a couple
minutes ahead of time.

29:06 How do we get the returns?

29:09 The fra-- you don't
need to put this.

29:11 Returns the fraction of notes in
a score that are eighth notes.

29:18 

29:23 OK, you can keep doing yours.

29:25 If you're stuck, I'm
going to give what I do.

29:28 Sign like--

29:29 [TYPING]

29:32 

29:46 Not the most efficient
use of iterators.

29:49 I've done two.

29:49 [TYPING]

29:52 

30:09 STUDENT: You're missing an H.

30:10 MICHAEL SCOTT ASATO
CUTHBERT: I'm--

30:11 where am I missing it?

30:12 It's somewhere in
eighths, right?

30:13 STUDENT: Yeah.

30:14 MICHAEL SCOTT ASATO
CUTHBERT: Where's--

30:15 STUDENT: So second to last.

30:16 MICHAEL SCOTT ASATO
CUTHBERT: Ah, eighth.

30:17 That's-- yep, eighths.

30:18 Thank you.

30:20 Appreciate that.

30:21 

30:30 And go ahead and run your num
eighths on Blooming, on Reel,

30:35 and on Bach.

30:36 And use your Spidey
sense to figure out

30:41 if your numbers are
pretty meaningful.

30:46 If there's anything I
can get from this class

30:50 to just use in all of your
programming things is,

30:52 always use your intuition
to see if something

30:58 like that, something
is working right.

31:04 Ooh, wow.

31:05 Look at that.

31:08 The reel is incredibly low.

31:10 Oops.

31:12 Now I have too many
eighth fracti--

31:14 I should have done it eighths
fraction, but whatever.

31:17 I'm--

31:17 

31:22 That actually feels
too low for that reel.

31:24 Only 8%.

31:25 But I guess there's
a lot of 16th notes.

31:30 OK, give me a snap if
you're ready to move on.

31:33 [SNAPPING]

31:33 OK, hearing some snaps, not all.

31:36 We'll give another
10 seconds or so.

31:38 

31:42 So so far, we have the
first one that seems really

31:48 to give, at least
in this one piece,

31:50 a big distinction among
the three types of things.

31:57 

32:01 OK, now I'm going to wade into
something that people don't

32:06 always say, is this
a feature extractor

32:08 because it returns a
number or something?

32:10 Or is, when you put
them all together,

32:12 is that the feature extractor?

32:14 I'm not sure, but
I'll use this term.

32:17 So the feature
extractor is going

32:18 to run all of our different
little feature extractors.

32:22 And in this case,
I'm going to say,

32:24 it's going to
return a tuple of--

32:27 and I'll tell you what
these are in a bit.

32:29 But here, I'll
write this out here.

32:31 A string, two ints, a
float, an int, and an int.

32:37 

32:40 And what are these going to be?

32:43 They're going to be
the file name, which

32:46 is pure metadata, just so that
we can look at things later.

32:50 They're going to be the
numerator and the denominator

32:53 of the piece using our function
we wrote, extract meter.

32:58 They're going to be--
what's the only thing we've

33:00 written that returns
a float as the answer?

33:02 STUDENT: Eighth.

33:03 MICHAEL SCOTT ASATO
CUTHBERT: What's that?

33:04 STUDENT: Proportion of eighth.

33:04 MICHAEL SCOTT ASATO CUTHBERT:
Eighth, yeah, eighth fraction,

33:05 eighth proportion, whatever
we are going to call it,

33:08 the number of sharps, and then
that last one we'll get to.

33:12 That's going to be
the ground truth.

33:16 And it's doing too
much JSON there.

33:19 Stop

33:19 Doing trailing commas.

33:21 So the file name, you get
this from a score's metadata

33:26 object, which we haven't
really talked about,

33:28 it's file path split.

33:32 I'm just going to
get the last bit

33:33 so I'm not showing my entire
directory tree to everything.

33:37 So I'll just get the last
thing after the slash.

33:40 Those of you who know
Python's path library,

33:42 you can probably do better.

33:46 The numerator and
the denominator

33:50 will extract meter
from the score.

33:56 The eighths we'll say is the
eighth fraction of the score.

34:04 Sharps feature is get sharps.

34:07 You can call them
whatever you'd like.

34:09 And then the ground truth,
is it a jig or is it not?

34:17 But it has to be a number.

34:19 So we'll say integer of is jig.

34:24 You could also say, if you like
this Python, 1 if jig, else 0.

34:32 Sometimes explicit's
a little bit nicer

34:34 to see what that's going to be.

34:36 And then we want to return
all that file name numerator,

34:40 denominator, eighths--

34:44 I should do quarters.

34:45 I can spell quarter--

34:47 feature, and ground truth.

34:50 I'll let everybody get caught
up while I debug my own system.

34:55 Whoa, some fast
typists in this class.

34:58 Feature extractor on bach.

35:01 Let me just see--

35:03 feature extractor on blooming.

35:09 OK.

35:09 

35:15 ABC file extension, yep.

35:17 STUDENT: [INAUDIBLE]

35:18 MICHAEL SCOTT ASATO
CUTHBERT: Yeah.

35:19 A lot of these are all
written as ABC files.

35:22 We didn't really cover-- no,
we didn't cover ABC files

35:24 because they're tiny bit
more complex than the easiest

35:29 to encode handwritten
things but not complex

35:33 enough as like
musicxml or something.

35:38 OK, so blooming metals
jig, it's in 6/8.

35:41 77% of its notes
are eighth notes.

35:45 It's in one sharp.

35:46 And that last one
indicates what again?

35:50 STUDENT: Jig.

35:51 MICHAEL SCOTT ASATO CUTHBERT:
Yep, so the one indicates jig,

35:54 right?

35:54 Great.

35:55 OK, so what I'm
going to do right now

36:00 is I'm just going to
run this for a second.

36:03 So how would I get everything?

36:06 So we can do metadata.

36:10 I'm just doing this so we
can see how we do this.

36:13 In the Ryan thing, piece
equals metadata_entry.parse.

36:19 And then we'll print the
feature extractor on the piece.

36:26 Let me just try to see.

36:29 Yep.

36:32 Because of the way
I did it, you'll

36:34 see that at first,
there's not too many jigs.

36:37 And then later on, there's jigs.

36:43 OK, now, if you scroll back
up to the top of your-- sorry,

36:50 I'm going to have to get my
blank template for a second.

36:54 Oops, that's way smaller.

36:56 There should be, on the
top of your template

36:59 if you downloaded it,
something called write_ryan.

37:02 And you just need
to change your path

37:06 to someplace that you're going
to be able to remember it.

37:11 So change that, unless
you've created a Cuthbert

37:14 user because it makes it
easier for you to cut and paste

37:17 my code.

37:18 You probably want
to change that.

37:20 And then you can run
this while I explain

37:23 a little bit what it is.

37:24 

37:27 Is write_ryan working for
people when you get that?

37:31 OK.

37:31 

37:34 Great.

37:35 

37:38 So I'm going to have
my own version here.

37:45 

37:55 STUDENT: [INAUDIBLE]

37:56 MICHAEL SCOTT ASATO CUTHBERT:
The write_ryan( ) command.

37:58 W-- you don't have to do any of
this, but it'll be kind of fun

38:03 because then you'll have
write_ryan and start.

38:13 

38:16 OK, I've seen more
people waiting

38:18 than typing for a little bit,
so I'll just explain what we do.

38:22 Some of these things,
if you work with files,

38:24 you probably know
them pretty well.

38:27 This is really not necessarily
the best way to do this,

38:29 but I'm going to open two files.

38:31 One of them is the
file that we're

38:33 going to use to
train our classifier,

38:37 the thing that is going to try
to learn if something is a jig

38:40 or not.

38:41 The other one is
the file we're going

38:44 to do to try to test
whether it can do it or not.

38:49 We're going to
hope that we don't

38:52 put the same data into both.

38:55 So we're going to try to put
some data in the testing,

38:58 some data in the training.

38:59 There's a number
of different ways

39:00 you can do this type of work.

39:03 Sometimes you put 90% in the
training and 10% in the testing.

39:08 Sometimes you put 50/50, which
is what we're going to do.

39:10 Some of it has to do with
how much data you have.

39:15 So what I'm going to do--

39:17 maybe it'll be easier to see--

39:18 I'm just going to separate--
.tab means everything's going

39:21 to be separated by tabs.

39:22 So I'm going to first
put a header line that

39:26 says the names of the columns.

39:28 These are just for us to read.

39:29 So we have a file name,
numerator, denominator, eighths,

39:32 sharp, and isjig.

39:34 And so we're going to
write that to the top of it

39:37 because a lot of the classifiers
that work on tab data

39:41 expect this to be
the first line.

39:43 Now, we're going to hope that
when running this system,

39:47 that it doesn't peek
at the file name.

39:49 And we'll see because obviously,
file name would give it away.

39:53 And then so the descriptions,
what kind of data is this?

39:57 The file name's a string.

39:58 Then we have
discrete, as we said

40:00 for an integer, discrete,
continuous discrete, discrete.

40:03 So we'll write that out again
to each of the two files.

40:09 And then we have
third line, which

40:13 is mostly blank for
all these things.

40:15 And the first one
just says metadata.

40:18 That is to say, don't
peek at the file name--

40:21 do not use the file name
to try to classify this--

40:24 then normal information
and then the class,

40:27 the thing that we're
trying to figure out.

40:30 And we really, really hope that
the artificial intelligence

40:34 thing does not peek at the
class when it's trying to look.

40:39 You can really quickly
create an incredible AI thing

40:42 if you would allow it to peek.

40:44 And so we'll put that out.

40:45 So that's just all headers.

40:46 And that's why I didn't want to
spend too much time writing it.

40:48 Then what are we going to do?

40:50 Same thing we were
saying before,

40:52 we're just going to get
each piece into there.

40:55 I've done enumerate for a
reason so I can keep track

40:58 of what the piece number is.

41:00 And then we can extract the
piece, all the features from it.

41:06 And then we'll just
write them out.

41:09 In this case, we're going
to write them as a string

41:11 because we can only write
strings out to a text file.

41:15 Write each of the features
out, tab separated.

41:19 Actually, we'll get
ready to write it.

41:21 We'll just put it into a string.

41:22 And then every other
one, we're going

41:25 to write to training and
test, training and test.

41:28 Probably, another
way to do it would

41:29 be to flip a coin each time and
use a random number so you can

41:33 see if things are going there.

41:35 I'm not an expert on
this type of work.

41:38 But that's how that works.

41:41 And I don't think--

41:44 Yeah, I don't think
I'm going to run it now

41:46 because I should have been
running it during this time.

41:48 You know what?

41:49 I'm just going to put train
data x and test data x

41:53 so that while it's running, I
have access to our baked one.

41:59 So actually we can look
at it, magic features.

42:04 So we switch out of Python and
look at the shell for a second--

42:12 train data-- wherever
you put your thing.

42:15 And I can see that
I've written out--

42:21 it's kind of weird that
the tabs don't show up.

42:24 You would love to have something
that would automatically

42:26 put it out.

42:26 But we have the file name,
all our headers, description

42:29 of the data, the metadata here.

42:32 And then yeah, we have all of
our information written out.

42:38 So that's pretty good.

42:40 Oh that did finish, great.

42:42 OK.

42:45 So now we've done our
feature extraction.

42:47 The feature extraction
part of the lecture

42:50 is done for a little bit.

42:53 This is a small
number of features.

42:55 But I think that
they're going to end up

42:57 being halfway decent
features because we

42:59 thought about them a bit.

43:01 And when the data is small,
you want to think more

43:04 about your features.

43:05 So you installed
something called Orange 3.

43:08 But it's a little bit weird.

43:09 It comes as capital Orange.

43:12 I just I don't know why.

43:13 I don't like things capital.

43:15 So I always import orange
as lowercase orange.

43:19 Great.

43:21 We're going to load
our training data

43:23 and our test data, so
first training data,

43:28 orange.data.table.

43:29 

43:32 A lot of these things are
going to be very similar

43:35 in a super modern
artificial intelligence

43:40 framework like
PyTorch or TensorFlow

43:45 or something like this.

43:46 Similar idea, you want to
load data in as a table.

43:51 If it's too big to load
on your all at once,

43:55 then there's special
techniques and stuff like that.

43:58 But we'll load the
training data in.

44:00 And now when we look at it, it
just looks a little bit nicer.

44:04 

44:08 Actually, where's our first--

44:11 I don't know--

44:13 45 to 50?

44:16 Does that work?

44:16 Yeah.

44:17 OK, so that might be
a little bit better

44:20 because we can see
we have our features

44:24 here two for 12% and 3 sharps.

44:28 And this one happens
to be a jig, so there.

44:34 And so the afterward
is what the class is.

44:37 Great, and we'll do the exact
same thing with the test data.

44:40 And we'll call it
variable test data.

44:42 So I'm just going
to copy and paste.

44:44 And hopefully, the
test data looks

44:46 a lot like the training data.

44:47 

44:52 STUDENT: Should we
change the file path?

44:54 MICHAEL SCOTT ASATO
CUTHBERT: Oh, yeah, yeah.

44:56 It looks a lot like
the training data

44:59 if we don't change
the file path.

45:01 You see how well it is.

45:02 OK, so now we're
going to create some,

45:08 we'll call learners,
classifiers, things

45:10 that can classify the data.

45:14 Here's the first
one and I think,

45:17 in some ways, the most important
classifier that you'll ever use.

45:21 And that is-- why did I
switch into camelcase?

45:24 OK, I guess I'm
in camelcase now--

45:26 something called
orange.classific

45:28 ation.MajorityLearner.

45:30 

45:38 And what a majority
learner is it's kind

45:43 of the control or the
placebo of your system

45:47 to make sure that you don't
get too excited by how

45:51 good your system is working.

45:53 What it does is it looks
at the training data,

45:57 which has hundreds--

45:59 what maybe the
training data has--

46:02 I don't know.

46:02 Let's say it has 51
jigs and 49 nonjigs.

46:08 And it says, I will always
say that any piece that's

46:13 ever shown to me is a jig
because then I will get over

46:16 50% right or I will
get the highest

46:18 answer of doing anything.

46:20 So if you are not beating
your majority learner,

46:24 then you're not doing
any classification.

46:26 So the majority classifier--

46:30 you all who have taken a
machine learning class,

46:33 do you get taught this or no?

46:36 Yeah.

46:37 OK, good.

46:38 Some people, this will be
totally old story and not.

46:43 So the majority learner
is just a generic thing.

46:47 And now we have a
classifier, which

46:48 is one trained on our data.

46:51 So we're going to say that the
majority classifier will now

46:56 know how to work with
this particular data.

47:01 And then we'll use another one
called k-nearest neighbors.

47:04 This was-- I don't know--
maybe 20 years ago,

47:08 the state of the art
of machine learning.

47:13 It's a little bit
out of date now.

47:15 But it does work pretty
well on small data

47:18 sets and few classifiers.

47:20 So nothing that it's
going to get you

47:23 super excited at
a top tech firm.

47:27 But it still has its uses.

47:30 So we're going to do the
same exact same thing.

47:33 Everything that I put
from majority learner,

47:36 and just put it
as KNN neighbors.

47:39 Look at the K, which
might be 4, might be 3,

47:41 might be 5, the
nearest neighbors

47:44 in a multi-dimensional vector
space to your one piece

47:49 and try to learn where
in this space it goes.

47:55 Snap if you're caught.

47:58 Snap if you're not now,
if you need a second.

48:01 OK, good.

48:05 Great.

48:05 So I'm just going to keep
track of how many correct

48:09 the majority gets in a
variable called majCorrect

48:11 and how many correct the
k-nearest neighbor gets

48:15 in a variable called knnCorrect.

48:18 And then total equals the
length of the test data, not

48:24 the training data.

48:25 So now we're going to
be working on this.

48:27 And we should have
something like this.

48:31 By the way, I lost half an hour
in preparing this lecture on,

48:38 why do I keep getting over 100%?

48:40 Always make sure to reclear
out your number correct as you

48:44 recode or something or make
sure to do it within your loop.

48:49 So good.

48:51 So we have 106 things that we're
going to be able to do now.

48:56 That was for our loop.

48:59 So we'll just do an enumeration
of each row in the test data.

49:06 So for i comma test row
in enumerate test data.

49:09 

49:13 And then the majority
learner is going

49:16 to take a guess for each one.

49:18 So majority's guessed is going
to be the majority classifier

49:22 of the test row,
which it's always

49:26 going to guess the same thing.

49:28 I guess in this
case, it's always

49:29 going to guess jig
because there's four more

49:31 jigs than there are non jigs.

49:33 And then our classifier,
k-nearest neighbor classifier,

49:38 will also take a
guess, knnClassifier.

49:43 I know somebody's
probably saying "guess"

49:45 is not the right
word, but type works.

49:48 And then we'll get the real
is the testrows.get_class.

49:55 So as you said, the
class is either 1 or 0,

50:00 something like that.

50:01 And we can do print
out something.

50:06 But print-- how about this?

50:10 We'll just say majGuess,
knnGuess, and real.

50:19 So I'll start this
running for a second.

50:22 But notice, we haven't
put in anything

50:24 on whether it got
it right or not.

50:26 But we can just look at that.

50:28 Oh, one of them guesses.

50:32 So you can see that the majority
one for every single piece

50:36 just puts out--

50:39 yep, it's always a jig,
always a jig, always a jig.

50:43 K-nearest neighbor says, I
don't think this is a jig.

50:49 And here's the correct answer--

50:50 not a jig, not a jig, not a jig.

50:52 And here, k-nearest neighbor
is learning that, ooh, this one

50:55 looks like a jig.

50:57 So I'll just modify
this a tiny bit

51:01 and say, if majGuess equals
real, then majCorrect add 1.

51:12 If knnGuess equals real,
knnCorrect equals 1.

51:22 When you're trying to
figure out how to do things,

51:24 you'll use more classifiers.

51:26 There's a lot more.

51:27 And so you probably want to
do this in some of a loop.

51:30 But great.

51:31 

51:37 Good.

51:38 

51:40 And so now we'll see how we did.

51:42 How did majority do?

51:43 

51:48 Here, I'll do this.

51:49 Majority majCorrect--
I always making

51:55 things look nice for humans.

51:56 

52:05 Why am I anal enough
to start already

52:09 putting in some of a
rounding thing to look?

52:14 Because I do feel like when
you see all those digits,

52:18 it's really, really hard
to figure out how important

52:23 the difference is.

52:24 So the majority,
this is what I happen

52:26 to know that there's
59% of them are jigs.

52:28 And so the majority
learner got 59% of them.

52:32 And then we'll do the
same thing for KNN.

52:37 Here, I can cut
and paste, right?

52:39 We all know how to do that.

52:41 What are we looking up?

52:43 Great.

52:43 

52:47 And we want to make sure
that that's knnCorrect.

52:49 

52:53 So our classifier is getting
about 87% correct at this, just

53:01 with these few little things.

53:03 Now, this is always
the exciting moment.

53:07 And then the hard part is almost
always getting it from 87 to 95.

53:12 And the next harder part
is getting it from 95 to 97

53:14 and then going up and
up and up from there.

53:18 So that's the
theoretical part aside.

53:21 I'm going to really quickly
just go through some things

53:28 that music 21 has
that just make some

53:37 of this a little bit easier.

53:40 So I know it's already
imported since I imported star.

53:44 But there's something
called features.

53:46 And what we can do is set equals
a features.DataSet classLabel

53:54 equals is_jig.

53:57 And then we'll do the same
thing with the test set.

54:00 So far, it's basically
the same type of thing.

54:05 And then I believe
if you type fes,

54:08 you should have something there.

54:10 I think I pasted this.

54:12 

54:15 These are built-in
feature extractor.

54:17 And each one of them has an ID.

54:19 And no, I don't have these
memorized, but something about--

54:23 

54:27 I can't remember what these are.

54:29 You know what?

54:30 I'm just going to cut and paste
because you already have this

54:32 and put it here.

54:35 STUDENT: You have fears?

54:37 MICHAEL SCOTT ASATO CUTHBERT:
Fears, yes, that's my hidden--

54:41 thank you very much.

54:42 Appreciate that.

54:44 And think that should work.

54:47 And so these are some features
that have already been put in.

54:52 So one of them, I don't know,
what's the range of the piece?

54:56 How far is it from the lowest
note to the highest note?

54:59 A lot of these, they're
adapted from a really, really

55:02 cool toolkit called
jSymbolic part of jMIR

55:06 by Cory Mckay up in Canada,
and just ported them over

55:12 because they're kind of neat.

55:13 And then some of them are ones
that I've written because I kind

55:17 think that they're
a little valuable

55:19 or somebody in the Music
21 team has written.

55:22 So here, we have a lot
more features here.

55:25 And what we can do is we
have our two data sets.

55:28 So we'll say the training
set addFeatureExtractors

55:34 and add all those
features extractors

55:36 and then same thing
for the test set.

55:38 

55:43 And this, as I
said, you don't need

55:44 to be typing too
much because I'm just

55:46 going to go pretty fast.

55:48 And what we'll do is I'm just
going to cut and paste this

55:53 because all we're doing
is dividing things up

55:57 into either the test
or the training set,

56:00 depending on if
it's even or odd.

56:02 And so we'll just
add the data on here

56:06 with some nice little features.

56:08 And this will just generate
all the headers for you.

56:11 Whoops, what did I do?

56:13 Testing set is what
I called it before.

56:16 Sorry, training and
testing, that makes sense.

56:18 

56:21 Did I do something wrong?

56:22 Oh I have to change it up here.

56:25 There we go.

56:26 Starting all over, hopefully,
I don't have any num correct.

56:29 Great, and that's just doing
all the feature extraction

56:33 of getting them in.

56:35 That's going to take
a little bit of time.

56:37 So we're going to
switch like they

56:39 do in the cooking shows to
the already baked version

56:43 where it's all done.

56:45 OK.

56:47 Oops.

56:48 Here we go.

56:51 Where do we go?

56:53 

56:55 Yep, so the next couple
of things that you do,

56:58 you want to process
all your training set

57:02 and write it out
just like before,

57:04 process it and write it out.

57:05 Why is it taking so much longer?

57:08 Because we gave it a
whole bunch of features.

57:10 And some of them take
a long time to do,

57:13 like ones that have to do
with variability between parts

57:17 and parallel fifths, finding if
it's a multi-part thing and so

57:22 on.

57:23 But then the next
row ends up being

57:26 the exact same type of thing.

57:28 We have a majority learner.

57:29 We're going to still
use the knnLearner

57:31 and then try to see how well
it did and keep looking.

57:39 And again, the majority
learner is still 59%.

57:42 You hope that doesn't change.

57:43 And now, using all of
these extra features,

57:47 we've gotten our number from
87% all the way up to 61%.

57:53 So sometimes, just throwing
more feature extractors

57:58 at the problem is
just going to have you

58:01 wait longer at the computer.

58:04 Sometimes, thinking really
carefully about what you already

58:09 think the data might look
like is a pretty good thing,

58:13 and especially if you're
working with a small data

58:16 set where it's not
going to be able to do

58:18 the kinds of deep
neural network learning.

58:21 You have to keep
going through enough

58:23 to really build a
model of the set.

58:26 As some people say that
look, the neural networks

58:33 are getting better and better.

58:35 And we just need to
throw more data at it.

58:39 But imagine if
you wanted to have

58:41 a program that was automatically
reading handwriting.

58:46 And you gave the program all
these papers of handwriting.

58:51 And you just gave
them an audio file

58:53 of how it drops, how it sounds
when it drops and try to do it.

58:56 You're giving it kind of
the wrong data to learn on.

58:59 And so a lot of
the extractors now,

59:03 unless you're writing your own
or unless you're using really

59:06 musically sensitive ones,
you can save the computer

59:09 a lot of time by trying to
already say, hey, let's process

59:14 this as a symbols ahead of
time or something like that.

59:18 A lot of, by the way, state
of the art of symbolic music

59:23 machine learning things are--

59:25 you all remember
the piano roll where

59:29 we put things like this to show
length and stuff like that?

59:34 Yeah, well, it's converting
the entire musical score

59:38 to a piano roll, saving
that as an image,

59:42 and then using image
classifiers and image generators

59:47 to generate pieces that
look like the piano rolls

59:50 and then translating them back.

59:51 So I'm hoping that over
the next decade or so,

59:56 we can do better and
do some things that

59:58 help these neural
nets and classifiers

60:02 work with data that's
a little bit closer

60:05 to the original numbers.

60:08 OK, I have time for
just a little fun

60:14 thing with my favorite low
feature extraction thing.

60:21 So let me just show a
couple little things.

60:25 OK.

60:26 Yeah.

60:28 First off, the importance
of thinking about data sets

60:31 and ground truths,
this is, I think,

60:34 one of the first
pieces that showed

60:37 deep learning, the kind
of for people in the

60:40 know moment like ChatGPT has
been in the last year happened.

60:45 I think it was about 10 years
ago when AlphaZero and AlphaGo

60:49 suddenly became the world's
greatest go and chess players.

60:54 And so a lot of people
think, well, this

60:56 was with generalized knowledge,
no rules being taught

60:59 except for legal move or not.

61:02 But one of the things to think
about the difference between

61:07 a lot of the things that they
were being trained on and what

61:10 you have is that AlphaZero, the
chess playing computer, played,

61:14 what was it, 700,000 games or a
million games or something like

61:18 that.

61:19 And at the end of every
single game it played,

61:23 it got perfect feedback
on how it did--

61:26 you won, you lost, you tied,
you won, you lost, you tied.

61:30 A lot of the things that we're
interested in doing with music

61:33 like music
recommendation or things

61:36 like this, predicting
what's the next great hit,

61:39 first off, we don't
have that correct data.

61:42 Maybe what's the Billboard
chart or something like that?

61:45 But for how good was this
piece, because it's going

61:48 to be different every time.

61:49 It's going to take
us three minutes

61:51 to listen to if it's
computer generating a song.

61:54 And then we're going
to give it feedback

61:56 that we might feel differently
about that piece tomorrow.

61:59 So we don't give
perfect feedback.

62:00 And it takes a long time.

62:02 So this is one of the
reasons I like working

62:05 with some of the older things.

62:07 OK, we'll go back.

62:08 Great.

62:10 I don't think I presented this.

62:12 No, I presented in other place.

62:14 So this is what we'll end
for the last 10 minutes

62:17 and talking about some of
the interesting things that

62:20 come out with features.

62:22 So how would you distinguish
choral music from Bach

62:26 from Monteverdi?

62:28 So we're doing a lot
of Bach in this class.

62:32 But we'll get a little
bit more into the ear.

62:34 Here's Bach.

62:36 [MUSIC PLAYING]

62:39 

62:40 So this is Bach.

62:41 

62:51 And so then we'll switch to one
of the other great composers

62:54 about 100 years before
Bach, Claudio Monteverdi.

63:00 And so, some of you, this might
be the first time you hear him.

63:03 [NO AUDIO]

63:06 

63:27 One second with the Back
again so we can get back.

63:30 

63:35 Great.

63:36 What's something
you heard different

63:39 between the two of them?

63:42 STUDENT: Monteverdi
was a bit more somber

63:44 with more of the minor keys.

63:45 MICHAEL SCOTT ASATO CUTHBERT:
OK, somber, more minor keys.

63:47 We could do a key detection.

63:49 Jonathan.

63:49 

63:53 STUDENT: I mean, Bach
had sounded like there

63:55 were more people singing.

63:56 But it's hard to tell.

63:58 MICHAEL SCOTT ASATO CUTHBERT:
Yeah, but it could be.

64:00 It could be more people,
fuller than good.

64:03 Yeah.

64:05 STUDENT: Bach is
more together where

64:07 Monteverdi has a lot of voices
going off doing kind of thing.

64:11 MICHAEL SCOTT ASATO
CUTHBERT: Bach more together,

64:13 homophonic maybe, Monteverdi
doing their own thing.

64:15 Good.

64:16 One last one.

64:17 

64:22 OK, that's a pretty
good place to start.

64:24 So I threw everything
in, all the kitchen

64:29 sink of feature
extractors and got

64:33 to see what a particular
algorithm did that seemed

64:41 to work pretty well.

64:43 And the first,
here's a little quiz.

64:46 It's one of the few quizzes
that elementary school students

64:49 do better than adults at.

64:51 So let's see if we
can figure this out.

64:53 7802 is 3.

64:56 1065 is 2.

64:59 If you've seen it before,
then don't answer.

65:02 998 is 4.

65:05 And 1773 is 0.

65:14 If you're new to this, 1, 2, 3,
3 circles, 1 circle, 2 circles,

65:29 1, 2, 3, 4 circles
and no circles.

65:31 So I bring that up to say that
sometimes the computer is going

65:35 to be looking at things that
are really, really far out

65:40 and trying to figure out things.

65:41 So there's all these things
that we could be looking at.

65:44 I'll bet that the proportion of
instruments that are electronic

65:49 isn't going to help with
Bach versus Monteverdi.

65:52 But one of the things I like
about a particular classifier

65:56 that is not close to
the state of the art

65:59 or to the getting
the best results.

66:01 But this tree learner can--

66:05 unlike being a black box, it can
actually show what the path--

66:09 so it's of a decision
tree, branching tree--

66:11 it took to get there.

66:13 So here's how it
can say, to begin,

66:17 if the note f sharp below
middle C is used more than 14%

66:23 of the time, the
piece is by Bach.

66:26 Otherwise, if the top number in
the time signature is 3 or less,

66:31 it is by Bach.

66:33 Otherwise-- I love this one.

66:36 If the distance between the
highest note in the soprano

66:38 and the lowest
note of the bass is

66:40 less than 2 octaves and a
minor sixth, then it's by Bach.

66:44 And then there's
three more things.

66:45 We get to the final
one, count the number

66:47 of times each note is used.

66:49 Find the note that is
used the most often

66:51 and the note that is used
the second most often.

66:53 If the second most often used
note is used less than 97%

66:56 as often as the most commonly
used note, the piece is by Bach.

67:00 Otherwise, it's by Monteverdi.

67:02 And this worked
with 99% accuracy.

67:07 What I loved about this is that
this was the first decision

67:13 to distinguish.

67:14 And I was just baffled by it
until I realized, well, OK, Bach

67:19 has more pieces in sharp
keys than Monteverdi is.

67:23 OK, that would make sense.

67:24 Monteverdi was mostly hovering
around no sharps or flats or one

67:29 flat assigned.

67:30 But then it's minor, and there's
raised leading tones and stuff

67:34 like that, so why not?

67:35 Well, the leading tone tends to
get raised in the melody, which

67:40 tends to be in a higher voice.

67:42 The middle area,
tenor, will only

67:46 appear as f sharp if the key
signature is already f sharp.

67:48 So it's a way of learning
some things like this.

67:51 And this particular one ended up
being garbage in, garbage out,

67:56 that Monteverdi doesn't
using modern time signatures.

68:00 And so the people who encoded
this chose never to use 2-4,

68:06 always put it into 4-4, because
it also weren't bar lines.

68:11 So you could decide how long.

68:12 So this ended up being
that the computer learned

68:16 not the difference between
Bach and Monteverdi

68:19 but the difference between
Bach's editor, modern editor,

68:22 and Monteverdi modern editor.

68:24 I have lost the
reference, but I have

68:27 been told about an
audio classifier that

68:32 tried to classify by genre.

68:34 And it was doing very, very
well until it turns out

68:37 that different genres of music
used different microphones

68:41 in general.

68:42 And it was picking
up the difference

68:44 between the microphones.

68:45 So if you sing country music
on a hip hop microphone,

68:49 it would classify as hip hop.

68:51 So all of these
things, we need to be

68:54 really careful about what's
going on with the potential

68:58 for classification.

69:00 And so this is where I
like this old school--

69:04 imagine this as a tree diagram
of things going left and right,

69:07 I guess if you
turn it sideways--

69:09 these old school feature
classifiers a little bit just

69:13 to check what might be happening
in the latest black box.

69:18 So you guys did a
remarkable stamina.

69:24 You got through the zombie of
music eating feature extraction.

69:29 And I hope that some people
will choose to find--

69:34 if you find this to be
helpful in doing something

69:37 in your final project, you now
have some of the tools to do it.

69:41 On Friday, we'll continue
with searching and similarity,

69:45 and will be giving the
first 15 minutes explaining

69:49 what he's doing at MIT.

69:50 He's a professor
of computer science

69:53 and what he's been doing
with music on his work.

69:57 So there'll be a start.

69:59 And then I'll continue
with some other things.

70:01 Great, thanks.

70:03 

