---
title: YouTube Transcript: Class 8 Video: Hierarchies (II): Streams and Recursions
created: 2026-10-01
updated: 2026-10-01
type: video
source_url: https://www.youtube.com/watch?v=F-KsvLCM-Ns-transcript
source_type: video
ingested: 2026-10-01
published: recent
duration_minutes: 20
language: en
time_sensitive: True
---


# YouTube Transcript: Class 8 Video: Hierarchies (II): Streams and Recursions

## Video Information
- **Title**: Class 8 Video: Hierarchies (II): Streams and Recursions
- **Video ID**: F-KsvLCM-Ns
- **Published**: Unknown
- **Views**: Unknown
- **Language**: en

## Transcript
00:00 

00:00 [SQUEAKING]

00:02 [RUSTLING]

00:04 [CLICKING]

00:05 

00:13 MICHAEL CUTHBERT: I'm going
to switch over to the Jupyter

00:16 Notebook to talk a
review of last class,

00:20 and then going forward.

00:21 So what are some of the
things we unlocked last class?

00:25 So Music21 objects
that we can use.

00:29 Shout them out.

00:32 What's that?

00:33 Stream.

00:33 Good.

00:34 AUDIENCE: Pitch.

00:34 AUDIENCE: Corpus.

00:35 MICHAEL CUTHBERT:
Pitch, corpus, I heard.

00:37 Anything else?

00:38 AUDIENCE: Duration?

00:39 MICHAEL CUTHBERT: Duration.

00:40 And pitch from duration
lets you do what?

00:43 AUDIENCE: Note.

00:44 MICHAEL CUTHBERT: Note, good.

00:44 We remember that.

00:45 And there's one other one
I just want to remind you.

00:48 We're not going to
use it very much.

00:49 It's called converter.

00:50 Let me make this a
little bit bigger.

00:52 Oh, that's nice for me, too.

00:54 And sorry.

00:57 Great.

01:00 Because converter does the
same thing as corpus, but loads

01:03 any file on your hard drive
or anywhere on the web.

01:07 But since I don't know
what's on your hard drive,

01:11 we're not going to
use it that much.

01:13 Great.

01:15 And what's something
we did last class?

01:18 What's the problem?

01:19 So let's all load
that Bach piece.

01:23 Anyone remember
what I should type?

01:25 AUDIENCE: Corpus.

01:26 MICHAEL CUTHBERT: Corpus dot--

01:27 AUDIENCE: Parse.

01:28 MICHAEL CUTHBERT: Parse.

01:29 Good.

01:29 And I said it was Bach BWV 66.6.

01:35 The only thing you
actually need is

01:36 whatever is necessary
to distinguish it

01:38 from anything else.

01:41 So you'll sometimes
see I'm going

01:43 to be taking a shortcut there.

01:44 Good.

01:45 And how many things
were in Bach?

01:48 Do you remember?

01:49 Estimate.

01:49 Six.

01:50 Oh, good.

01:50 We have the exact number.

01:52 Yep.

01:52 Why?

01:55 Where are the notes?

01:58 We have a score object, I'm
pretty sure, just to recall.

02:03 Yep.

02:05 We have score object.

02:06 And then what's inside
of it, the main thing,

02:09 four of the six things?

02:11 AUDIENCE: Parts.

02:12 MICHAEL CUTHBERT: Parts, good.

02:13 And then inside
the part, Hannah,

02:15 did you-- you had your
hand up for the last one.

02:17 I'll get you in.

02:18 What's inside of a part?

02:19 AUDIENCE: The measure?

02:20 MICHAEL CUTHBERT:
Measure objects.

02:21 Good.

02:22 And what's inside
the measure objects?

02:25 AUDIENCE: Notes?

02:26 MICHAEL CUTHBERT: Notes, and
other things, but primarily.

02:28 So we have this hierarchy,
this nested hierarchy.

02:31 Score, parts, measure, notes.

02:36 There may sometimes even be
another level of hierarchy.

02:40 For instance, in
scores like this

02:44 where you have two different
voices on the same part, there--

02:50 what do you call it?

02:51 There may be a voice
object inside of a measure.

02:54 And if you have a whole
collection of scores,

02:56 we call it something
begins with an O-P.

03:00 AUDIENCE: Opus.

03:00 MICHAEL CUTHBERT: Opus, yeah.

03:01 So you can have something
that's bigger than a score.

03:04 You can have opuses,
opera, technically,

03:06 an opus that has
scores inside it.

03:09 And then you can put
opuses inside opuses,

03:11 because I didn't want
to make anything bigger.

03:12 Yeah, go ahead, Misha.

03:13 AUDIENCE: Can we close the door?

03:14 MICHAEL CUTHBERT:
Oh yeah, sure, sure.

03:15 Can you close the door for
somebody who can get there?

03:17 Thanks.

03:20 Thank you, I appreciate it.

03:23 Great.

03:24 So how did we get down to the--

03:29 how did we get down to
the notes last time?

03:32 We did something like
four thing in score.

03:36 You don't have to type.

03:37 This as all review.

03:38 In Bach if thing, in if--

03:44 we remember that isinstance is
the Python way of figuring out

03:48 same thing in score
is a stream dot part.

03:53 We can also just say
stream dot stream.

03:55 If it's some of a stream, then
for thing in part in thing

04:01 in score.

04:04 I don't want to waste
too much time on this.

04:06 I can do this.

04:09 If instance thing in part.

04:12 Somebody tell me if I type
something wrong on this,

04:14 because I'll probably do it.

04:16 And there's no tricks on this.

04:19 For thing in-- what is it?

04:25 Measure in thing in part,
print thing in measure.

04:34 Hopefully, that works.

04:35 Yep.

04:36 So that lets us get
down to the lowest

04:39 level of what's happening here.

04:44 We have a whole bunch of notes.

04:46 What are we doing?

04:47 

04:50 You'll remember the two
representations, the box

04:53 representation or the
salami slice, time wise.

04:58 What are we doing?

04:59 Are we going through all
the parts here first,

05:02 or are we going through
one part and then another?

05:06 Hint.

05:06 You can always look
back at your score.

05:08 You know the piece and
you have the notes.

05:10 

05:18 Go ahead.

05:18 And when you have it, just
look up and then shout it out.

05:23 AUDIENCE: Part by part.

05:24 MICHAEL CUTHBERT: We're
going part by part.

05:26 The soprano C-sharp,
B, A, B, C-sharp.

05:31 Fermata.

05:33 It's nice to see that
fermatas are not in here,

05:36 so they must be someplace else.

05:38 E, C-sharp.

05:39 Yeah, so we're going part
by part in this case.

05:42 Great.

05:45 And we also saw last class
that we could do something.

05:48 If we knew exactly
where something

05:50 was, we could say Bach 2,
which I happen to remember,

05:55 there's a metadata
soprano then alto.

05:58 So that would be two.

05:59 I don't know.

06:00 Let's choose a random measure,
and we can make a list out

06:04 of this.

06:05 I can't remember if--

06:06 I think I demonstrated that.

06:07 And get what is in here.

06:10 And we'll keep seeing that
these random other things keep

06:14 popping up here, like
system layouts and so on.

06:20 So we'll need a better
way to get to notes.

06:26 Questions?

06:27 This is review, so
I went pretty fast.

06:29 But the important thing
is, if I'm reviewing it,

06:32 it's probably important that
we have good understanding

06:34 before we move on.

06:36 Yeah, Jake.

06:37 AUDIENCE: You had us
recurse on the first day?

06:39 Are we going to use that?

06:39 MICHAEL CUTHBERT: So we're going
to get to that in just a second.

06:42 Yep.

06:42 Good.

06:43 Yeah.

06:44 AUDIENCE: Close that.

06:45 MICHAEL CUTHBERT: Sure.

06:46 Great, great.

06:49 There we go.

06:49 Sorry that the blackout
blind over there

06:51 doesn't seem to be working.

06:53 

06:58 If you email me
after class, I'll

06:59 remember to put in a
facilities request.

07:01 Or if you email me right now
in class, you'll hear a ding.

07:04 Then I'll put in a
facilities request,

07:05 because that's going to get
annoying after daylight savings

07:09 time starts for this class.

07:11 Good.

07:12 

07:15 Any other things that we
want before from the review

07:20 last time?

07:21 Yeah.

07:21 I showed a whole bunch of
things on the first class

07:23 that are not done yet, but
we'll be getting to them sooner.

07:29 So assume everything
on the first class,

07:31 I think I said at the end,
was then immediately relocked.

07:34 But as far as this recurse
thing, we're going to get to it

07:38 and unlock it in
just a few seconds.

07:42 Great.

07:43 

07:46 So any stream can be converted
to a list by doing it,

07:51 so we can get the list
of everything that's

07:53 in the top level
score for Bach here.

07:57 And then we can,
yeah, do other things.

08:03 There are some differences
between a stream and a list

08:06 that are pretty important.

08:07 So when I say a list,
array in other languages,

08:11 what are some of the
things you can do?

08:13 It's a mutable container.

08:15 So what some things
you can do to it?

08:18 Yeah.

08:18 AUDIENCE: You can add to it.

08:19 MICHAEL CUTHBERT:
You can add to it.

08:20 Great.

08:21 Other things?

08:23 You usually can add.

08:24 AUDIENCE: You can pop things.

08:25 MICHAEL CUTHBERT: You
can pop things off of it.

08:26 Great.

08:27 You can remove things out of it.

08:29 What are some other
things that lists do?

08:31 Yeah, go ahead.

08:32 AUDIENCE: You can change
things at certain indices.

08:34 MICHAEL CUTHBERT: You can change
things at certain indices.

08:35 Yeah, you can replace
one thing with another.

08:38 Good.

08:38 Any other things we can do?

08:42 Yeah, Jason.

08:42 AUDIENCE: Find the length?

08:43 MICHAEL CUTHBERT: You
can find the length.

08:44 Great.

08:45 You can find the length,
and you can append to it

08:47 and change the length,
all those things.

08:49 One other thing beginning
with IT that you can do.

08:54 Yeah, John.

08:54 AUDIENCE: Iterate on it.

08:55 MICHAEL CUTHBERT:
You can iterate it.

08:56 You can put it into a
for loop and get things.

08:58 Great, great.

09:00 There's one more over here.

09:02 AUDIENCE: Splicing?

09:03 MICHAEL CUTHBERT:
Splicing, yeah.

09:04 You can get little
parts of it, too.

09:06 So in this way a stream
really does work like a list.

09:14 We can get out, get
rid of that metadata.

09:17 We can get rid of
other things here.

09:20 If I had been
smarter 20 years ago,

09:23 it probably would inherit
from list, but it does not.

09:26 But it has a lot of
things that are list-like.

09:30 But there's some things
that you can also

09:32 do that are a little different.

09:35 Actually, what was
that over here?

09:38 We went up to Bach 2, 4.

09:42 Let's get that out here.

09:44 I think that should
be measure three.

09:49 Let's see.

09:50 And m equals this, and
we'll see what m is.

09:54 Yep, measure three.

09:56 Great.

09:56 So measure three
of the second thing

09:59 up here, so the third
thing, because we're

10:01 doing 2, 0 index 0, 1, 2,
measure three of the alto part.

10:07 Here is something
that I don't think,

10:09 for all the amazing things
MIT CS training does,

10:13 I don't think it
does very, very well.

10:15 I think that this says measure
three of the alto part.

10:19 And here's the contents of it.

10:20 Let's just go through
and make sure.

10:22 Remember, pickups
are measure what?

10:24 AUDIENCE: Zero.

10:25 MICHAEL CUTHBERT: Zero.

10:26 So let's make sure that this
is actually measure three.

10:28 

10:32 Is that right?

10:33 Do we get the right measure?

10:34 

10:39 The next problem set,
the one that we're

10:41 going to be talking
about at the end of class

10:43 today, it's probably
the least time

10:47 consuming of any of the ones
you've had so far, so good.

10:52 I figure every third one, you
need a little bit of a break.

10:54 So we'll go down on that.

10:56 I will tell you in
advance where people

10:59 lose points on this problem set,
is that they write the code,

11:04 the code works, and
then they go on,

11:05 and there's a little
programming error somewhere

11:07 that could have easily been
fixed by looking at the score

11:11 during show and checking
that your answer was actually

11:15 what it should be.

11:17 So just to have that
there, and that's now,

11:22 my feeling is everybody
can get an A plus.

11:25 We can all get
perfects on everything.

11:27 I don't need to play
gotcha games for [LAUGH].

11:32 Now there's nothing to mark off.

11:34 So good.

11:35 So make sure that you're
always doing that,

11:37 and make sure to do these
column sanity checks,

11:40 that you're getting
out from your data

11:41 what you should be getting in.

11:44 OK, so these are some
things that are similar.

11:47 One of the things, though, in--

11:51 so we have this
measure, object n.

11:54 We'll look.

11:54 

11:57 Shape of your
brackets does matter.

12:00 You have something here.

12:01 Now, if this was just a
normal list, m dot insert 2,

12:09 we're going to
put it position 2.

12:11 Let's put a note dot note.

12:12 Let's do one that
we can immediately

12:14 recognize, A double flat 4.

12:18 We can create an object in here.

12:20 Actually, we'll be smart.

12:22 We'll call that n and
define it before n equals,

12:27 so that we can
reference it again.

12:29 Sorry, I'll try not to get
this at the very bottom

12:32 of the screen.

12:33 Great.

12:33 

12:44 So what should have happened
if this were a normal list?

12:51 Where would you have expected
to see that double flat,

12:56 A double flat?

12:59 Adam.

12:59 AUDIENCE: After the G-sharp.

13:00 MICHAEL CUTHBERT:
After the G-sharp.

13:02 

13:04 Everybody agree?

13:05 Sometimes everybody agrees when
the professor's like, yeah, does

13:09 it go after two or does it--

13:10 I can't remember, but yeah,
I'm pretty sure that's right.

13:13 So it should be
somewhere over here.

13:17 Why is it here?

13:18 Let's go back to that
alto part, measure 2,

13:23 and see it's coming
after the C-sharp.

13:27 Does the C-sharp have
a fermata on it or not?

13:30 I just want to make sure
we're all on the same place.

13:32 

13:39 Yeah, John's nodding his
head and John's almost always

13:42 right on these
things, so good, good.

13:46 And yeah, so we have
it on the last "ya"

13:49 of that word that I'm not going
to say during Lent, right?

13:53 And good.

13:54 So it's come in
right after there,

13:56 and yet we said we
should put it at 2.

14:01 What might be happening here?

14:05 Yeah, John.

14:06 AUDIENCE: It's being put at
the second beat, 12, 0 index.

14:10 MICHAEL CUTHBERT: The
second beat, yeah,

14:14 with the beginning being 0.

14:16 Now, I told you that's very,
very close to the right answer.

14:19 So great, great.

14:20 I said at the
beginning there was

14:22 a reason why I didn't like to
use beat as a fundamental unit.

14:26 What was that?

14:27 

14:30 Or because of things
like 5/8 where the--

14:35 fast 5/8, 1, 1 and 2, and a 1
and 2 and a, where beats can

14:41 change their duration
even within a measure.

14:44 So what's something equivalent?

14:48 What would durations
measured in?

14:51 I'm going to call
on Misha next, but I

14:52 want to make sure that
we have-- yeah, Misha.

14:54 AUDIENCE: Yeah, I
think it was just said.

14:55 I think you said you used
quarter notes, I assume.

14:57 MICHAEL CUTHBERT: Yeah,
so quarter length.

14:59 So in this case, it's
exactly the same as beat.

15:01 So this correct
answer in this case,

15:04 because we're in four quarters.

15:06 But so we've put it in--

15:09 what do we have?

15:10 Eighth, eighth.

15:11 So that's all
within 0, 0.5, 1, 2.

15:18 But there might
be a problem here.

15:21 Why is it after the C-sharp?

15:26 Well, let's do this.

15:27 We remember some
of our iteration

15:30 for, I'll still, say thing in
m, even though they're mostly

15:33 notes.

15:34 Print thing and things.

15:38 New term that we haven't
seen, it's offset.

15:42 So the offset, just
like the duration

15:45 is measured in quarter
lengths, the offset

15:48 from the beginning of
the current container

15:51 is measured in quarter lengths.

15:53 So we have here.

15:55 And we can actually now have
two notes at the same time.

15:59 So you can have multiple
things at the same position.

16:03 That makes it a
little bit harder

16:05 to remove by offset
that you want to have,

16:10 because unlike in an
array where there can only

16:13 be one thing at a
particular index, here

16:16 you can have multiple
things at the same index.

16:20 This is a simplification.

16:22 We'll see in a little bit
that notes and everything else

16:25 can have an infinite number
of offsets simultaneously.

16:29 But this is good
enough to start here.

16:33 Yeah, go ahead.

16:35 AUDIENCE: So if you do
show, it doesn't put them

16:37 in the same place.

16:38 MICHAEL CUTHBERT: If you
put it in show, it doesn't.

16:40 Right, because not,
that's a great thing.

16:43 You're going to find it is easy
to create things that are valid

16:47 musical concepts that cannot
be shown by any of our music

16:56 representation software,
our MuseScores, or Finales,

16:59 or whatever like that.

17:01 Why?

17:01 Because if you have a
part, do you have two--

17:06 This is an ontological question.

17:08 Do you have two notes that sound
at the same time in one part?

17:12 

17:15 Or do you have
something else that

17:18 happens when you have two
notes at the same time?

17:23 What other representation
might be for two notes,

17:26 for two things that
sound at the same time?

17:29 I won't say notes.

17:30 

17:33 Nobody?

17:35 AUDIENCE: Different parts?

17:36 MICHAEL CUTHBERT:
You would have--

17:38 A, you could have it in
two different parts, which

17:40 is what we've normally seen.

17:41 Or yep.

17:41 AUDIENCE: You can have a
split, like one person going

17:44 up and down.

17:45 MICHAEL CUTHBERT: Yeah,
you can have a split.

17:47 Yeah, a split.

17:48 We call those voices in this.

17:50 So you have two
voices at that thing.

17:51 What's the other thing,
another fundamental part

17:56 of our ontologies?

17:57 [PIANO CHORD]

17:58 AUDIENCE: Chord?

17:58 MICHAEL CUTHBERT: Chord.

17:59 So in this case,
your software wants

18:03 me to have created a chord
object, which is not yet

18:05 unlocked for us
out of these two.

18:07 So it just does whatever
it wants with it.

18:11 Great question.

18:12 Super.

18:13 So keep playing with the limits.

18:15 We're a little
bit behind in time

18:17 because we're really
asking great questions.

18:20 So I'm going to hold
off a little bit on some

18:23 until we can get a little
bit further into some things.

18:29 So yeah, question.

18:33 Go ahead.

18:34 AUDIENCE: How do you remove?

18:35 MICHAEL CUTHBERT:
How do you remove?

18:37 Well, you'll be able to-- you
can either remove the thing,

18:41 and it will find it, Or you can
remove something at an offset.

18:45 And fortunately, all
of these other things

18:49 will be-- all
these other options

18:52 will be revealed to
you in the reading

18:57 before next time
we meet together,

19:00 which is the user's
guide chapter on streams.

19:03 So I think that remove
is mentioned in there.

19:06 It can be a little bit more
complicated, as I said,

19:08 so I want to hold that
off for just a little bit.

19:15 Let me do another little
thing for a second,

19:19 and we'll jump to some ways
that we can make our life easier

19:24 by not doing for
thing and thing,

19:26 than for next thing and
thing, next thing in fixing

19:28 the previous thing.

19:30 Obviously, we're going
to have some other ideas.

19:35 So this is one notion, one way
a score might be represented

19:40 in Music21 with two parts.

19:43 And so within the score in this,
its score's length is how much?

19:50 Just shout it out.

19:51 AUDIENCE: Two.

19:51 AUDIENCE: Two.

19:52 MICHAEL CUTHBERT: Two or?

19:54 AUDIENCE: Three.

19:54 MICHAEL CUTHBERT: Three,
because we have this metadata.

19:56 And so I've put underneath
is the offset of everything.

19:59 Both parts start at the
beginning of the score.

20:03 So they have offset 0.

20:05 Within part one, there
are two, I'm calling,

20:08 measures measure 1a, measure 2a.

20:13 Their offsets are at 0
and 4, which makes sense

20:17 because somewhere in here,
there's a 4/4 time signature.

20:22 

20:26 Notice, though, that when
we're looking at measure two,

20:29 measure two's offset is 4, but
we start again with offset 0.

20:34 So if you want to know how many
quarter notes into the piece

20:39 quarter note 9 happens, you'd
have to add 2 plus 4 plus 0.

20:47 Fortunately, adding 0
is easy, so you get, ah,

20:50 it's 6 quarter notes
into the piece.

20:52 So this is one, the
representation that's happening.

20:57 Now, when you iterate over the
score for all size-- use el,

21:01 element--

21:02 thing, things comes
off the tongue better,

21:05 but el is quicker to type.

21:07 And when you do this, you'll
see that-- we've already

21:12 seen you get the metadata,
you get part one,

21:16 and then you get part
two, and that's all.

21:20 So you get the three
things that are there.

21:24 The more powerful way
to do this is something

21:26 called recurse, the
recurse method on here.

21:31 And what this does is it
goes through the first thing,

21:35 and then if there's anything
inside the metadata,

21:38 which there isn't-- it's not a
container-- it would go into it.

21:41 Then part one is
a container class.

21:44 All containers are
called streams,

21:46 but the general term in
computational music theory

21:49 is the container.

21:51 And then within this container,
we have another container,

21:55 and it will go through these
things that are not containers.

21:58 Sometimes these are called
leaves, the leaf node,

22:02 like in a graph, the thing
that has no descendants on it.

22:05 And then it will go
through the second one.

22:07 Then it jumps back to part
two and goes through each one,

22:12 and tells you that.

22:13 So that's going to
make life a lot easier.

22:16 Let's recurse through.

22:18 

22:21 Can I move over here?

22:23 Let's recurse through Bach.

22:26 For el in Bach dot
recurse, print.

22:31 Let's do el and el's offset.

22:33 

22:38 Oops.

22:38 And now I have to get
my scrolling back.

22:41 Here we go.

22:44 So now, we're seeing
there's the metadata.

22:46 There's the soprano part.

22:48 If we were writing a program,
we could keep track of what part

22:53 we're in at a certain point, and
every time we see a new part,

22:55 do something.

22:56 And then we see, oh,
we're at measures zero.

22:59 Here we go.

22:59 Here's all the different things
to measure one, measure two.

23:04 And if I scroll far enough,
eventually, we should see--

23:09 here we go-- part alto.

23:13 So that's pretty good.

23:17 All this information
about what's

23:19 its offset and things,
this can be done,

23:22 also gotten in a way
that just prints.

23:25 It's not useful for parsing.

23:27 I would not say parse this.

23:28 But if you do Bach dot show
text, and it just gives you,

23:35 basically, the same information
as that routine, but nicely

23:40 formatted.

23:43 So I'll give a second where the
current offset is given first,

23:49 and then the next thing also
puts everything like this.

23:56 Questions on this part?

24:00 Now your computer
science question.

24:03 Recurse is what type
of graph search?

24:08 Don't shout it out yet.

24:10 We'll let everyone think.

24:11 There are a number of ways
of searching through a graph

24:15 or iterating through a graph.

24:17 What kind would we call this?

24:21 I'll give you a hint.

24:22 The second word
is usually first.

24:26 That wasn't much of a hint.

24:28 So raise your hand if you're
confident that the answer

24:32 to this now, and go like
this if you're not confident

24:38 that you know the answer.

24:39 Great.

24:40 Could you talk with
the person next to you,

24:42 and especially if you
have a couple people who

24:45 aren't so confident,
and share your answer

24:47 and see if you're
in the same boat?

24:50 

24:53 Who is now a little bit
less-- is still unconfident?

24:57 Who didn't come to an
agreement on your thing?

25:00 You guys are still
in disagreement.

25:03 No, you're in agreement.

25:04 Good, good.

25:06 So let's all shout it out.

25:09 The kind of search is a--

25:11 AUDIENCE: Depth.

25:12 MICHAEL CUTHBERT: First
search, a depth first search.

25:14 Good.

25:15 So we're always going to
be following the leftmost--

25:19 I should do this in different
colors so it's easier to see.

25:23 The leftmost node that
we haven't yet seen,

25:28 and doing something with that,
and then going back up, here,

25:32 going back up, down.

25:34 Does that seem to fit other
people's computer science

25:38 things?

25:39 I have neither a
concentration minor, major,

25:42 or PhD in computer science.

25:44 So please, if I get
something wrong,

25:46 you all shout to me because
you've done more of that

25:48 than I have.

25:50 Great.

25:51 So we have depth first search.

25:52 What are some of the things
anybody knows from other things

25:55 that depth first
searches are good for?

25:58 And what are some of the things
that they're not good at?

26:01 So good for anybody
who wants to say.

26:04 

26:08 Don't worry.

26:09 It's a safe space.

26:13 AUDIENCE: Shortest path problem?

26:14 MICHAEL CUTHBERT:
Shortest path problem.

26:16 Good.

26:17 Shortest path problem.

26:18 Anybody, do you want to explain?

26:19 Or anybody else want to explain
what that is for those who

26:22 haven't?

26:22 

26:25 Shortest path between two
nodes, how to get there.

26:28 You might not want to do.

26:29 Something else it
might be good for?

26:31 

26:35 Yeah.

26:36 AUDIENCE: It's just when
you're in a scenario where

26:38 you think you want to look
over every possible object.

26:41 MICHAEL CUTHBERT: Great.

26:42 In a scenario where you want to
look at every possible object.

26:46 Now, there's other
search methods

26:48 that also have that property,
but this one has that property.

26:54 So it's already a lot better
than for thing and thing

26:57 than thing and thing,
thing and thing.

26:58 You know that you're going
to get to every point.

27:01 What's something that it
might not be good for,

27:04 or that another
search method might

27:06 be a better way of doing it?

27:08 

27:12 Yeah.

27:13 AUDIENCE: In the case of breadth
first search versus depth

27:15 first search, if
something's close by,

27:18 there's not a lot of it.

27:19 Or the tree is super deep.

27:23 But the answer is super close.

27:25 MICHAEL CUTHBERT: Yep.

27:26 AUDIENCE: Depth first search
will search through every one.

27:28 Or to go to the
depths of the tree.

27:30 MICHAEL CUTHBERT: The tree.

27:30 AUDIENCE: Just to check
in the first couple.

27:32 MICHAEL CUTHBERT: Great.

27:33 Super, super.

27:33 And we should say
what we're comparing.

27:36 There's lots and
lots of searches,

27:37 but the two key ones, we
have depth first search,

27:41 and it's compared to what?

27:42 AUDIENCE: Breadth.

27:43 MICHAEL CUTHBERT:
Breadth first search.

27:45 Yep, the breakfast
search as I always say.

27:46 Breadth first search.

27:48 So that one, what
are we going to do

27:51 if we want to breadth
first search in here?

27:53 What are we going to see first?

27:56 What's the first node
we're going to visit?

27:58 AUDIENCE: SC.

27:59 MICHAEL CUTHBERT: SC, the score.

28:00 Good.

28:01 So, so far, it's exactly the
same as the depth first search.

28:03 Second node we're going
to see in this side?

28:05 AUDIENCE: Part one.

28:06 MICHAEL CUTHBERT:
Part one, good.

28:08 Third node?

28:08 AUDIENCE: Part two.

28:09 MICHAEL CUTHBERT: Part two.

28:10 So we're already different.

28:11 Next node?

28:12 [INTERPOSING VOICES]

28:13 MICHAEL CUTHBERT: Was one.

28:14 Yep.

28:14 AUDIENCE: For one, isn't
BFS better for shortest path

28:17 searching, rather than DFS?

28:20 AUDIENCE: It depends on
how you're doing your path.

28:22 If you're looking for
distance one minus path,

28:24 and you want to find the
first one that gets you there,

28:27 that's better.

28:27 But you're doing positive
length distances in DFS.

28:31 

28:34 MICHAEL CUTHBERT: I'm trying
to remember the exact what

28:36 I remember, which one of these.

28:38 AUDIENCE: A star
would be even better.

28:40 MICHAEL CUTHBERT: Yeah, so we'll
get to these particular types

28:42 of searches later.

28:43 Controversy in the
class, I'll try

28:45 to remember exactly which one.

28:47 Do we have a--

28:48 but yeah, I'll trust that we'll
solve that because we're not

28:52 going to be doing shortest
path yet in this class.

28:57 But we'll see that there's
certain advantages to one

29:00 versus the other.

29:01 The other thing, so what's a
musical thing that we want to--

29:05 how about this?

29:07 Do all parts start with
the same key signature?

29:14 Breadth first or depth first?

29:17 Which one is going to be
fastest to get you your answer?

29:20 [INTERPOSING VOICES]

29:21 MICHAEL CUTHBERT: I
heard depth and breadth.

29:23 Who's on depth?

29:25 Who's on breadth?

29:26 Yep.

29:27 OK, good.

29:28 So we're going to want to
have both types of searches

29:30 available.

29:32 So recurse will
give you always a--

29:37 what do you call it--
the depth first search.

29:42 There's another one that
we're going to have.

29:45 And you're going to see
it's the flatten operation.

29:49 And you're going
to see it sometimes

29:50 in my old slides I haven't
figured out how to update,

29:54 dot flat.

29:55 But it used to be a property.

29:58 That is to say, you didn't
need the calls called flat.

30:02 Now it's a method
called flatten, I think.

30:05 There were two reasons for this.

30:06 One, if anybody has a new--

30:09 uses an IDE, like
VS Code or PyCharm,

30:13 or something like that, which
I highly encourage you to do--

30:16 it's nothing elite to
use VIM anymore in life--

30:21 then a lot of those will now
go through and call and check

30:26 every one of the properties
at a certain point

30:28 so it can repeat for you.

30:29 And flat ended up being for a
very, very large score, very

30:35 space and time sensitive.

30:37 And so once I
upgraded to a thing,

30:39 I realized, OK, that can't
work anymore, that flat.

30:43 So we had to do this.

30:44 I also wanted to make
it a few more letters

30:47 so that people would stop
calling flat instead of recurse,

30:51 just because it
was less to type.

30:52 So now they're much
more equal, flatten.

30:56 And what flatten
does is it gives you

30:59 the option of doing
everything first

31:03 that's at the same
offset of everything.

31:06 So we start with--

31:08 I think I have an
animation on this--

31:10 the metadata, again.

31:13 Let me get one clef,
next clef, both the time

31:19 signatures, everything
that's at the same point.

31:22 When you have a half
note here, we'll

31:24 get both quarter notes before
getting to the other thing.

31:28 The other thing that flatten
does that's different

31:32 is you'll see the offsets are
now, because it's flattened,

31:37 they're now all relative
to the start of the score.

31:44 So because of this, they're
implemented in different ways.

31:49 Recurse the breadth
first search just has

31:53 a little pointer that's going
around, figuring out where I am,

31:57 figuring out how to go back up
to the next hierarchy level,

32:00 and walk around, and do this.

32:02 So it's very, very fast and
not very memory intensive.

32:06 The flatten, on the
other hand, in order

32:10 to compute where
everything should be

32:12 and which one is actually
coming next into this hierarchy,

32:15 and for historical
reasons, flatten

32:18 will take that same
score and put it

32:21 all into a new score object,
a new thing, but with--

32:28 it also removes all
the parts and stuff.

32:31 Flatten, there are
no parts or anything.

32:33 There's just the things, just
the leaf nodes at the end.

32:36 So you'll get the clef, the
other clef, the time signature,

32:40 the other time signature, and so
on, all in a new stream object.

32:47 And this is the
first time when I

32:50 was saying that a note
might have more than one

32:53 offset, because
this is the same.

32:57 Oops.

32:58 This quarter note here is the
same as that quarter note there.

33:02 So dot offset will be
changing as this happens.

33:06 

33:09 This is something that
will occasionally bite you,

33:12 but usually not.

33:14 Which offset does it tell
we need to put dot offset?

33:18 It tells you whatever the
offset is in the last stream

33:22 that you iterated over
that has that object in it.

33:28 So we call that the active site.

33:31 

33:34 So it tells you the
offset in its active site.

33:38 

33:40 You will find that
it's often you're

33:44 looking at something in
a flattened stream that

33:48 should say flattened up there.

33:50 And you want to know something
about, oh, Professor Cuthbert

33:54 said, get me all of the
notes between offset 5 and 7,

33:59 and tell me what
measure they're in.

34:02 Shoot.

34:03 We've gotten all things 5 and 7
from the beginning of the score.

34:08 The problem is we've
lost all the measure

34:10 information over here.

34:11 So there is a property on
all streams, dot derivation,

34:15 dot origin, which
will take you back

34:18 to the original, the
place where it came from,

34:21 so the pre flattened stream.

34:22 And that's something you're
going to be working with a lot.

34:26 This is an ontological
choice I've

34:28 made on how things are related,
how flattened versions of scores

34:33 have a derivation to the
origin of the original score.

34:38 Now I'll take
questions on anything.

34:42 It's pretty confusing.

34:43 It's a lot to jump in.

34:44 Yeah, Adam.

34:45 AUDIENCE: Last time, what was
BOEHME in the German anthem

34:48 encoding?

34:49 MICHAEL CUTHBERT: What was what?

34:50 AUDIENCE: At the very, very
top, I said it was the composer.

34:52 MICHAEL CUTHBERT: Oh, Bohem.

34:54 OK, so we're jumping
quite a bit back.

34:56 It's the location of Bohemian,
originally, a Bohemian song.

35:00 

35:04 That was a pop quiz to
see what I remembered.

35:07 Great.

35:07 

35:10 Any other questions on this
material specifically, and then

35:15 on anything?

35:16 

35:23 OK, well, let's start by having
a little bit of programming

35:31 exercise time.

35:33 We have this Bach
chorale BWV 66.6.

35:40 Are there more?

35:41 Yep, go ahead.

35:42 AUDIENCE: So does flatten
mutate the object?

35:44 MICHAEL CUTHBERT:
So flatten mutates--

35:47 yes, it mutates something
on every object called

35:52 sites that keeps track
of where things are,

35:55 but it does not change a thing.

35:58 There were some
choices that, now

36:00 that Music21 is 20
years old almost,

36:03 there are some things that I
would have done differently.

36:06 And I think it's probably
time for somebody who's

36:09 younger and more
ambitious and wants

36:12 to do something for the next 20
years to come up with things,

36:16 because I did not listen to
our great software engineering

36:19 Professor Peter Jackson's
warnings against mutability

36:24 in objects as well
as I should have.

36:26 And now, I'm trying to
make more things immutable.

36:29 But you will find
that a lot of things

36:31 will, by default, not
mutate, but then can.

36:35 And objects can be mutated.

36:36 So that's a great question.

36:37 Everyone knows mutable
versus immutable objects.

36:40 You can change, you can not.

36:42 Lists are--

36:43 AUDIENCE: Mutable.

36:44 MICHAEL CUTHBERT: What is the
equivalent of a list in Python

36:46 that is immutable?

36:47 AUDIENCE: Tuple.

36:48 MICHAEL CUTHBERT: Tuple, good.

36:49 You all say tuple.

36:50 Here I always learned
it as tuple, but tuple.

36:52 Great.

36:53 Super.

36:55 So any other questions before
I go on to my question for you

36:59 about Bach?

37:02 OK, here is the question
for you to answer.

37:09 And let's do this
in groups of two,

37:10 because it's much more
fun to be talking to.

37:13 Does Bach use more
ascending notes

37:19 or descending notes, descending
notes, or about the same?

37:28 You might think the piece
doesn't start off, Hallelujah,

37:32 and end all [DEEP MUMBLING],
and it doesn't go the opposite,

37:36 so it must be about the
same maybe, but we'll see.

37:39 So talk.

37:42 Everyone know who they're
going to be paired up with?

37:45 See pairs.

37:46 It's easier if you're
sitting on think, sit paired.

37:49 Great.

37:50 So start talking about
how are you going to do

37:53 this and what which type of--

37:56 AUDIENCE: I think I
have a quick question.

37:57 Why does flattening show?

38:00 MICHAEL CUTHBERT: Flatten?

38:01 Why does flatten show?

38:03 [INTERPOSING VOICES]

38:05 MICHAEL CUTHBERT:
Because it's able to--

38:08 ah, because recurse
is not a stream.

38:12 Yeah, so I should
say, recurse just

38:14 gives you an
iterator around that.

38:16 You could do recurse
thing, and then there's

38:20 a dot stream that
you can put onto it,

38:22 and that'll give you a stream.

38:24 But it's just going to give you
the same thing you started with,

38:26 because yeah.

38:27 [INTERPOSING VOICES]

38:29 MICHAEL CUTHBERT: No, no, no.

38:30 Then do it then.

38:31 Yeah, thank you.

38:32 Thank you.

38:32 Always say, we're
going to talk first

38:34 about how to do it then
implement, but talk.

38:37 [INTERPOSING VOICES]

38:38 MICHAEL CUTHBERT: It's in class.

38:40 I don't care however
you'd like to do it.

38:42 But always start talking
then implementing.

38:45 

38:48 OK I'm hearing the
discussion start

38:51 dying down and
hearing some clicks.

38:53 You can keep talking, but
just an informal poll.

38:56 Which groups are
on team flatten?

39:03 We got one, two, three.

39:05 Good, good.

39:06 Which groups are on team
recurse, is the best way?

39:09 Good, good, good.

39:10 And which groups are in team
for thing, and thing, and thing,

39:13 and thing, and thing?

39:16 No, just there was a
smile with that one.

39:18 So keep going.

39:20 There's ways to
keep working on it.

39:23 I think you'll find there's one
that's better than the other.

39:26 But we'll figure out
which one that is.

39:29 [INTERPOSING VOICES]

39:31 

39:34 MICHAEL CUTHBERT: And if
you're lucky to be sitting

39:36 next to a group that's
on the different team,

39:39 maybe talk across
groups and figure out.

39:41 We'll dialogue across
religions and political views.

39:46 [INTERPOSING VOICES]

39:49 MICHAEL CUTHBERT: I'm going
to interrupt for one second

39:51 to say something
that I've heard.

39:54 Just a second.

39:56 Yeah, just one second.

39:57 Can I interrupt for one second
to say something I have heard

40:00 from two different groups?

40:01 Matthew.

40:03 Introduced for two
different groups.

40:05 I have heard this,
something like, oh,

40:07 but think of the memory.

40:08 We're going to have to keep a
reference to the previous note.

40:11 What is to keep a reference
to the previous note?

40:14 What is the big O
memory consideration

40:17 that we're thinking about?

40:20 AUDIENCE: 1?

40:20 AUDIENCE: 1?

40:21 MICHAEL CUTHBERT: 1.

40:22 Do we care about?

40:23 0 of 1 memory?

40:25 AUDIENCE: No.

40:26 MICHAEL CUTHBERT: No, we do not.

40:27 Good.

40:28 Keep going with that.

40:29 Just wanted to make
sure that we had

40:31 that we don't care about 0
of 1 operations very often.

40:34 Occasionally.

40:35 AUDIENCE: Is it just this piece?

40:37 MICHAEL CUTHBERT:
Just this piece.

40:38 Oh.

40:39 It was just this.

40:40 I just heard, is it just
this piece or all of Bach?

40:45 Just this piece is
what I'm asking for,

40:48 but you could do for
chorale in corpus dot--

40:58 [INTERPOSING VOICES]

41:01 

41:08 MICHAEL CUTHBERT: So you, Derek
and Vincent, if you wanted to,

41:14 there is a for loop
you can do above it.

41:16 And since we've unlocked
corpus, that will give you all.

41:20 Looking good.

41:21 Looking good.

41:22 So if anybody's finished
and has gotten a thing,

41:26 oh, a couple questions
once you have that.

41:29 They're not exactly the same.

41:31 I'll say that.

41:31 And what are some features in
the chorale that explain that?

41:35 The other thing you could do is
do this for all 360 chorales.

41:43 [INTERPOSING VOICES]

41:46 

41:49 MICHAEL CUTHBERT: That's
a lowercase C in chorales.

41:52 [INTERPOSING VOICES]

41:55 

41:59 MICHAEL CUTHBERT: Corpus
dot corrals dot Iterator.

42:02 Just before we go, who
is still on team flatten?

42:12 You used flatten a little bit?

42:13 OK.

42:14 And actually, it will say,
who used flatten anywhere

42:17 in the score?

42:18 And who used recurse
anywhere in their score?

42:22 OK.

42:22 I'm curious, how did flatten
work for getting this?

42:29 AUDIENCE: We had to say
change or first times flatten,

42:31 and it's the same for ascending.

42:33 And then for descending,
we're off by 2.

42:35 MICHAEL CUTHBERT: Interesting.

42:36 I'll be curious to
see how that happened.

42:40 Great.

42:41 So I think we're
wrapping up a bit.

42:44 You can keep working, obviously.

42:47 What is it?

42:47 Item 9 on your thing,
sound to score,

42:50 it's one of my favorite things
to teach in class because it's

42:53 really, really fun.

42:54 But I have made a video so we
can save some time outside.

42:58 And that, I'll add that.

43:00 That's about a 10
minute to watch.

43:03 Trying to make it quite a
bit easier on this weekend.

43:07 Try to make it a
little bit lighter,

43:08 so it's just some
interesting added things

43:12 that are happening there.

43:13 And for the first
time, I'm going

43:16 to really recommend that you
read the Music21 user's guide

43:21 chapters.

43:22 There's an optional one,
Chapter 26 at the end.

43:25 You don't need to read it
because it's a little bit

43:27 complex.

43:27 But if you do read it
and get through it,

43:29 there are some
tips in there that

43:31 can make some aspects
of the problem set

43:34 3 a little bit easier.

43:37 So any other questions
on what we did?

43:41 One last thing.

43:42 One last thing on this.

43:44 I always recommend
and I really, really

43:47 recommend a readable code.

43:49 Write readable code.

43:50 Write code so that you
can do this collaboration

43:53 and give it to your friends.

43:55 Write things like that.

43:56 But one year a while
back, the class

44:01 did decide to go code golfing
on this particular thing

44:05 to see who could write the
shortest code to do all this.

44:11 

44:14 Oops, sorry.

44:14 AUDIENCE: Why did they
do that to the eyes?

44:16 MICHAEL CUTHBERT:
Because back then,

44:17 we were using Piazza for
a discussion board, which

44:20 used a proportional font.

44:21 So using eyes made it-- also,
it makes it a little bit more

44:25 inscrutable.

44:26 So never write code like this.

44:28 But I do believe that
that works if you want it.

44:32 And your prof won, but see
if you can beat that one.

44:37 Thanks, everybody.

44:38 [LAUGH]

44:40 

