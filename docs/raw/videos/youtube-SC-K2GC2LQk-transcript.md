---
title: YouTube Transcript: Class 28 Video: Feature Extraction and Machine Learning (II)
created: 2026-10-01
updated: 2026-10-01
type: video
source_url: https://www.youtube.com/watch?v=SC-K2GC2LQk-transcript
source_type: video
ingested: 2026-10-01
published: recent
duration_minutes: 20
language: en
time_sensitive: True
---


# YouTube Transcript: Class 28 Video: Feature Extraction and Machine Learning (II)

## Video Information
- **Title**: Class 28 Video: Feature Extraction and Machine Learning (II)
- **Video ID**: SC-K2GC2LQk
- **Published**: Unknown
- **Views**: Unknown
- **Language**: en

## Transcript
00:00 [SQUEAKING]

00:01 [RUSTLING]

00:03 [CLICKING]

00:07 

00:09 KIKI GUTIERREZ: My name is Kiki.

00:11 I'm visiting a
scholar here at MIT.

00:13 I'm actually an
assistant professor

00:14 at Polytechnical
University of Madrid.

00:18 My background is
actually on engineering.

00:21 I am aerospace engineer.

00:23 I did my PhD on numerical
methods, but after my postdoc,

00:28 I decided to start doing things
that really fascinates me,

00:30 and that's how I end up doing
something related with music.

00:33 So I'm relatively
new in this field.

00:36 Today I'm going to show you
an algorithm that I came up

00:39 for pattern detection
in music, which

00:42 is what I've been working on
for the last year and a half,

00:45 more or less.

00:46 So as running example,
I'm going to use

00:50 the most listened song of the
history, which is Baby Shark.

00:57 So I don't know
if I can play it.

01:02 At least, it's the most listened
song of the history of YouTube.

01:07 [MUSIC PLAYING]

01:07 Baby shark doo doo
doo doo doo doo.

01:10 Baby Shark doo doo
doo doo doo doo.

01:12 Baby Shark doo doo
doo doo doo doo.

01:14 Baby shark.

01:15 Mommy shark doo doo doo doo doo.

01:18 Mommy shark doo doo doo doo.

01:20 Mommy shark doo doo doo doo.

01:22 Mommy shark--

01:23 OK, is pretty much
like that of the song.

01:26 This is the melody.

01:28 So what's the problem of
pattern detection in music?

01:32 We would like to have a
tool, an automated tool that

01:36 helps us to identify over
the score or over a corpus

01:40 the important musical
ideas there, you know.

01:43 So I'm highlighting
here some fragments,

01:46 how I look first at the
blue fragment over there.

01:49 There are three fragments,
three occurrences of them.

01:53 All of them are
exactly the same.

01:54 They have the same notes
with the same pitches

01:57 and same durations.

01:59 The only difference
is that they occur

02:00 at different moments of the
score, but it seems logical.

02:04 It seems reasonable to group
them as the same musical idea

02:07 and say that they
represent the same pattern.

02:13 We can call them--

02:15 we can put them a
label, blue pattern.

02:18 For the green one,
it's a little trickier

02:20 because the occurrence number
2 and the occurrence number 3

02:24 are exactly the same.

02:26 Probably makes sense
to group them together.

02:28 Occurrence number 1
has different durations

02:31 for the notes and the
occurrence number 4

02:34 is even trickier because they
just start with the rest that--

02:40 it's three notes
also and the lyrics.

02:43 But it's pretty different.

02:46 So that's one of the main
difficulties of the problem

02:49 of pattern mining in music.

02:51 That even though objects that
we want to group together--

02:55 because in our mind represent
the same musical idea--

02:59 over the table, they might
look pretty different.

03:02 And there are two
mechanisms involved here.

03:05 The first one is something
that we have already

03:07 studied, transformations.

03:09 So if we have a
music fragment, if we

03:12 apply a mathematical
transformation over the notes

03:16 there, we obtain other fragments
that under some circumstances,

03:20 our mind will process
them as equivalent.

03:23 And how to deal with
this computationally

03:28 from the point of view of
pattern mining algorithms?

03:31 My approach was to use
the concept of viewpoint.

03:34 I'm going to show you an
example of what is this about,

03:37 but for the moment,
it's enough to know

03:40 that it has a double task.

03:43 On the first hand,
it directly takes

03:46 into account these
transformations.

03:48 You will see it in a minute.

03:49 And probably more important, it
simplifies the representation,

03:53 because one of the constants in
this course, in these classes,

03:57 is that music is
something complex.

04:00 It has complex,
logical structures

04:04 among the elements of the score.

04:06 And if we find a way to
simplify that representation,

04:10 would be helpful from the
computational point of view.

04:13 So the viewpoint representation
is pretty simple.

04:17 It's just I'm
going to substitute

04:19 a complex tune like this one by
a single sequence of symbols.

04:26 So actually, here I'm showing
three viewpoints representation.

04:30 The pitch viewpoint, it's the
sequence of these symbols 83,

04:34 83, 83, 85.

04:35 It's the midi Note.

04:37 Then we have the duration
and the onset time.

04:41 I'm going to
highlight a fragment.

04:44 So you can see the different
viewpoints representations

04:46 for that fragment.

04:47 And it's nice that the
idea of constructing

04:50 the score by overlapping
layers of information.

04:54 That's the idea.

04:55 Formerly, a viewpoint
is a mapping

04:58 between the current event, the
current time slice, and all

05:03 the former ones into symbol,
usually an integer or float

05:08 but could be others.

05:10 Those that are
derived at viewpoints.

05:13 And perhaps for your own
particular music application,

05:17 you need to develop your own
viewpoint representation.

05:21 And here is clearly highlighted
how the transformations

05:25 could be directly taken into
account by using this technique.

05:28 For instance, if you apply
the octave transformation

05:32 to that pattern
there, that fragment,

05:35 you obtain that one over there,
which by the interval viewpoint

05:42 representation, we
have the same symbol.

05:45 So for sure, any
pattern mining algorithm

05:48 that is trying to
find this sequence

05:52 will see that that
one is the same.

05:54 Is that enough to deal with
the concept of dissimilarity

05:58 in music?

05:59 Unfortunately, no.

06:00 So have a look at these two
occurrences of the green pattern

06:04 of Baby Shark.

06:05 There is no viewpoint
representation

06:08 that can take us from
one to the other.

06:11 So someone said
at some point, OK,

06:13 it would be nice to
have a kind of measure,

06:16 a mathematical tool that help
us to evaluate how different two

06:19 fragments are.

06:21 Like the aim here is that,
OK, if I use that matrix

06:27 with this guy and this guy,
I would expect a lower value

06:31 than the one that
I would obtain when

06:34 taking this guy and this guy.

06:35 Because they are more far.

06:39 They represent further ideas.

06:42 So in computer science, they
use what is called the distance

06:46 functions.

06:46 This in a general scenario is
that you can give to a function

06:52 two objects, two random objects,
for instance, me, myself,

06:55 and this computer,
and it returns

06:58 a non-negative real
number, evaluating

07:01 the degree of dissimilarity
between the two objects.

07:05 In the context of
sequences, because we

07:07 are using viewpoint
representation,

07:09 so now this fragment
will be a sequence.

07:12 For instance.

07:13 Let's think that I'm using
the duration viewpoint.

07:16 So in the literature, we have
plenty of distance functions.

07:22 This was a very trending topic
in music information retrieval

07:26 15 years ago, more or less.

07:28 There were many
studies and papers

07:32 trying to figure out which was
the best distance function,

07:36 depending on the style.

07:39 The Levenshtein distance
function, perhaps, it's

07:42 not the most advanced
one, but this

07:43 is one of the simplest one and
probably the most used one.

07:46 And it accounts for the number
of substitutions, deletions,

07:50 or insertions to go from
one sequence to the other.

07:54 So to go from the sequence 0.5,
0.5, 0.5 to the sequence 0.5,

08:01 0.52, we just need a
single substitution.

08:05 So the Levenshtein distance
function between the fragment

08:08 2 and fragment 4 is 1.

08:11 Probably the Levenshtein
distance function between this

08:13 guy and this guy it's--

08:14 I don't know-- two
or three, at least.

08:17 So cool.

08:18 Now we have all the
ingredients needed

08:21 to understand the inputs
and outputs of my algorithm.

08:26 We have a corpus or
a piece of music.

08:29 We have also the
viewpoint representation

08:31 that the user wants to choose.

08:33 And some parameters
at the input.

08:36 The minimum support is the
minimum number of repetitions

08:39 that we require to a pattern
to be considered frequent

08:43 and to be included
in the result list.

08:45 These two guys, the minimum
length and maximum length,

08:48 are the parameters to control
the lengths of the patterns

08:50 that we want to mine
and some parameters

08:53 to control the degree
of dissimilarity

08:56 from the former slide.

08:57 And the result is just like
the list of frequent patterns

09:02 together with the position.

09:04 This is an example with the
piece of the former slide.

09:08 Now I'm selecting the interval
viewpoint and those parameters

09:13 over there.

09:14 And this is an example of the
output that we might obtain.

09:18 So we have a yellow pattern
that has four occurrences

09:23 and have a look that
each of these fragments

09:26 are at most distance one
from any of the rest,

09:33 taking the Levenshtein
distance function.

09:35 And we might have,
for instance, also

09:38 this guy, the purple
pattern, and this green one,

09:42 which is of length 4.

09:43 So in a real case,
the pattern structure

09:47 might be complex, as
you see, because you

09:49 have nested patterns.

09:50 You have many overlappings.

09:52 I won't go into
the details of how

09:54 I implemented the algorithm,
just a brief overview.

09:57 I divided in four steps.

10:00 The one is the creation
of an initial database.

10:03 A vertical database
is called sometimes,

10:05 where I just take a sliding
window of minimum length,

10:10 the minimum length
selected by the user,

10:12 and I just create a
database of all the patterns

10:16 together with their
positions within the score.

10:18 Then in the next step,
I compare every pattern

10:23 against all the rest, trying
to see if they satisfies

10:27 the distance constraint.

10:29 And in that case, I
group them together

10:32 into what I call metric
patterns, which are like groups

10:37 of fragments of music.

10:38 At this stage,
it's safe to delete

10:41 the entries that doesn't reach
the minimum support constraint.

10:44 They don't have
enough occurrences

10:46 to be considered frequent.

10:48 And finally, as here, I
still have patterns of length

10:53 equal to the minimum
length, and we actually

10:55 want longer patterns.

10:57 So the last stitch is
overlapping different patterns

11:00 to form longer ones.

11:03 And to finish this I'm going
to show you some results.

11:06 This is the last slide.

11:08 I'm actually already using this.

11:10 I started collaborating
with these research groups

11:13 like seven months ago.

11:15 This is a research group from
another university of Madrid.

11:22 They got a good amount of
money of the European Union

11:26 to study the Italian operas.

11:28 They have a huge database with
many features for each piece.

11:34 And in particular, they are
interested in the motion

11:37 that the piece evokes.

11:39 So here, we are trying
to find some correlations

11:43 between the emotions and
the pattern structure

11:46 of the different pieces.

11:48 These two other products
are pretty similar.

11:51 The number 2 is on a corpus of
folk music from a very concrete

11:58 region of Europe,
around the Pyrenees,

12:01 and the second one is the
database of jazz solos.

12:07 So here we are building
classifiers, similar to what

12:10 we did in the last class.

12:13 Here I'm showing the number
of patterns per style

12:17 for the different
styles in this corpus,

12:21 but perhaps here, we can see
a cool thing of the algorithm.

12:25 That it returns also the
position of the patterns,

12:28 not only the fact that a
piece contains the pattern.

12:31 So here, I'm plotting--

12:33 it's called coverage,
this variable,

12:35 but it's actually like
the probability function

12:39 of encountering a
pattern within a solo.

12:42 So I normalize the length
of all the solos by style,

12:47 and the thin line is the
average for the solos.

12:50 We can see, for instance, that
the concentration of patterns

12:55 tends to be at the beginning
and not in the end.

12:57 This is intuitive because
the improvisers usually

13:02 start their solos in
a more organized way,

13:05 taking thematic material
from the original melody,

13:08 and then they start to
do more crazy stuff.

13:11 Then, I'm also trying
to build up a pattern

13:14 dictionary in an Irish corpus.

13:18 These are the five
most frequent patterns

13:21 in the subset of minor rules in
the corpus that I'm working on.

13:25 So I don't know
for a performance

13:27 that is interested in
playing this music.

13:29 Perhaps, the take away
of this is, OK, you

13:32 might want to start
studying these patterns

13:35 because they appear quite
often in the corpus.

13:39 So better to first master them.

13:42 For the future with
Michael, we want

13:46 to study how the
algorithm performs

13:49 in a nice corpus of
early music that he has,

13:52 and also, we want to analyze
some solos of Charlie Parker,

13:55 who was one of the most
mathematical improvisers

13:59 of the history.

14:00 And also for the
close future, I would

14:02 like to see if this tool can
be helpful for plagiarism

14:06 detection.

14:06 I suspect that two pieces
that are very similar

14:12 are also some similarities
in their pattern structure.

14:16 And that's all.

14:17 Thank you very much guys.

14:19 Any questions.

14:20 [APPLAUSE]

14:23 

14:24 MICHAEL CUTHBERT:
By the way, just

14:26 so you get a sense
for your final things,

14:27 that was 12 minutes.

14:29 So a tiny bit longer than
what you have as a maximum.

14:32 

14:37 KIKI GUTIERREZ: Cool.

14:39 If any of you are interested
in a particular thing

14:41 of the algorithm,
just drop me an email,

14:43 and we can talk about it.

14:46 Thank you.

14:47 MICHAEL CUTHBERT:
So what I want to do

14:48 is I want to immediately
start by putting

14:51 some of these thoughts to work.

14:54 So get with a
partner next to you.

15:00 You can do that.

15:00 Over here, we need
a group of three.

15:02 Or unless you want
to participate

15:03 with a friend or jump over
there or jump over with Jordan,

15:09 if you do.

15:10 And here are six melodies.

15:14 I'm going to play
each one of them.

15:18 I'm going to play A
bunch of times also.

15:20 So I'll tell you which one I'm
playing, and you're going to--

15:23 and you can talk during this or
wait till just after playing.

15:27 You're going to
tell me which melody

15:33 is most or least similar to A.

15:37 [PLAYING INSTRUMENT]

15:43 OK.

15:46 And this is B. And I
want you to say why.

15:51 [PLAYING INSTRUMENT]

15:54 

15:59 This is C.

16:02 [PLAYING INSTRUMENT]

16:06 

16:09 And I'm going to
play A one more time

16:11 to get it back into our heads.

16:13 [PLAYING INSTRUMENT]

16:16 

16:19 And now D--

16:23 Oh, and by the way,
this isn't a right--

16:24 isn't a right answer one.

16:26 [PLAYING INSTRUMENT]

16:29 

16:32 Great.

16:35 Now E.

16:36 [PLAYING INSTRUMENT]

16:39 

16:44 And now A one more time before
doing F. So this is A again.

16:49 [PLAYING INSTRUMENT]

16:53 

16:56 And now F.

17:03 [PLAYING INSTRUMENT]

17:04 Oops, that's F and
E simultaneously,

17:06 which is very different.

17:07 Now F.

17:09 [PLAYING INSTRUMENT]

17:12 

17:16 Great.

17:17 Talk amongst yourself.

17:18 I want a ranking
from your group,

17:21 so somebody write it down.

17:22 

17:27 And I want to know why.

17:29 

17:33 OK, let's bring it
all back together.

17:34 

17:37 Let's bring it
all back together.

17:40 So look looking at
your list, and we'll

17:45 count like normal human beings.

17:47 Whichever one is the
top in your list is one.

17:50 Whichever one
second, two, stuff.

17:52 And we'll vote by fingers first
off for the general ranking.

17:58 So if you hold up the
number of fingers that--

18:02 if it's closest, it's
pulled up one finger.

18:05 If not, two-- whatever.

18:07 And full palm means I
have no idea what that is.

18:11 OK, B. Oh, B's doing pretty well
A lot of twos, a couple of ones.

18:22 C. OK, well, a little
bit more variety.

18:27 Hold them up so that
other people can see also.

18:29 Look around the room.

18:29 It's not just for me.

18:30 Great.

18:30 Great.

18:31 D. Oh, OK, we got a variety
who don't know, whatever.

18:38 Great.

18:39 E. Oh, still see
some poems or things.

18:45 Great.

18:45 And F. OK.

18:50 Oh, we have one four.

18:52 Good, good.

18:54 What do you-- you put it down.

18:55 What do you guys--
those who put F as four,

18:58 what do you put as five?

18:59 AUDIENCE: D.

18:59 MICHAEL CUTHBERT: B.

19:00 AUDIENCE: D.

19:00 MICHAEL CUTHBERT:
D. OK, D. Good.

19:02 Good.

19:03 Great.

19:05 Somebody who had C above
B justify your answer.

19:13 Who had C above B?

19:14 There were a couple people.

19:15 Yeah, go ahead.

19:16 Jake first.

19:18 Yeah, groups.

19:20 AUDIENCE: C was basically just a
transposition, whereas B like--

19:23 B changed a lot of
the rhythms a bit.

19:26 B, I think, fits the exact
pitches a little better, but--

19:31 or aside from a couple places
where it has some accidentals,

19:34 but it changes the
rhythm quite a bit.

19:37 Whereas C is just
a transposition.

19:39 So for relative
pitch essentially.

19:41 We waited transposition
equivalence more.

19:43 MICHAEL CUTHBERT: OK, good.

19:44 Good.

19:44 I'm already hearing words
that I'm liking stuff.

19:47 Great.

19:47 Somebody who had it the other
way around justify your answer.

19:50 Who had it the other way around?

19:53 Who had-- a bunch of people
had B above C. Yeah, John.

19:58 AUDIENCE: I'm looking for
the sound feel that A had.

20:03 Because a lot of the comments
are probably similar to A and B.

20:07 That's why we put it a
bit higher relative to C.

20:09 And when you take transposition
into account, only part of C's

20:13 becoming transpose,
so it doesn't even

20:15 feel like it's like
a full transposition.

20:17 MICHAEL CUTHBERT: Great.

20:18 Only part of it's transpose.

20:19 Yeah, yeah, it kind of
gets back on for a bit

20:22 and then comes back off.

20:24 Great.

20:26 Who had D-- who had D one two?

20:30 Anybody?

20:31 I can't remember.

20:33 Why do you have one or two?

20:36 AUDIENCE: Because it
basically has this--

20:38 so it has all of the same
notes in the right positions--

20:42 or basically--

20:45 yeah, all you have to
do is remove notes,

20:47 and then you get the
same thing, and--

20:49 I think with a few exceptions.

20:51 But that never happened
in any of them.

20:52 MICHAEL CUTHBERT: Great.

20:53 Who had D very low?

20:57 Yeah, go ahead, Tony.

20:58 AUDIENCE: Like before--

20:59 MICHAEL CUTHBERT: Sorry, Tony.

21:01 Can you speak louder?

21:02 AUDIENCE: Before, like a
rhythm, I guess, the same.

21:06 MICHAEL CUTHBERT: OK, great.

21:07 

21:12 Did anybody have E above four?

21:18 OK.

21:19 AUDIENCE: We have D at three.

21:21 And we put it there because
the pattern was very similar,

21:26 if not identical,
even though the melody

21:27 wasn't all that close.

21:29 So we figured that probably
counted for something.

21:31 MICHAEL CUTHBERT: So when
you say pattern, what's--

21:33 AUDIENCE: It's like the rhythm.

21:33 MICHAEL CUTHBERT: The rhythm.

21:34 The rhythmic pattern,
it's about the same.

21:36 Good.

21:37 AUDIENCE: That's an
inversion, right?

21:39 MICHAEL CUTHBERT:
Is it an inversion?

21:41 No.

21:41 No.

21:43 Would I do that?

21:45 AUDIENCE: The inversion.

21:47 MICHAEL CUTHBERT: By the way,
I can't remember where melody--

21:49 I think melody A comes from
a Huron book and then gives--

21:54 there's some search book, and
I should have my notes better,

21:58 and I'll try to make sure
it gets annotated later.

22:01 That had three other melodies.

22:02 I tried this in the past,
and it was so obvious

22:05 that everybody had the
exact same ranking.

22:06 I had to agree with them.

22:07 But I think this is better
for making some arguments.

22:10 Good.

22:11 Who had F anything but--

22:14 actually, somebody
who gave F five?

22:16 Jonathan, why would you--
did you give F five?

22:19 AUDIENCE: Yeah.

22:19 MICHAEL CUTHBERT: Why
did you give it five?

22:21 AUDIENCE: I mean, it didn't have
any noticeable similarities.

22:26 Like at first, it seemed
closer to E in terms of-- it

22:30 might have been inversion
but then not really.

22:33 The rhythm is also completely
different-- or not completely,

22:36 but it's fairly different.

22:38 MICHAEL CUTHBERT: Great.

22:39 So I'm just going to
point, and we'll get some--

22:44 

22:47 just what your ranking is.

22:49 So say them from--

22:50 Matthew, what was yours?

22:52 AUDIENCE: Alphabetical order.

22:54 MICHAEL CUTHBERT:
B, C, D, E, F--

22:55 OK, good.

22:58 AUDIENCE: B, C, D, E, F.

22:59 MICHAEL CUTHBERT: B, C, D, E, F.

23:01 AUDIENCE: [INAUDIBLE]

23:02 MICHAEL CUTHBERT: B,
C, E, D, F. Great.

23:05 Great.

23:07 Vincent?

23:09 AUDIENCE: C, B, D--

23:10 MICHAEL CUTHBERT:
C, B, D-- good.

23:12 And anything it
feels like you're not

23:14 being represented on there?

23:16 Hannah, what's your group have?

23:18 AUDIENCE: I think we
put C, B, D, E, F.

23:22 MICHAEL CUTHBERT: C, B,
D, E, F-- great, super.

23:24 Now what I want
you to do-- we're

23:26 not going to get through
all of the exercises today,

23:29 but I think this is the
most important part.

23:31 What I want you to do is
think about what ways--

23:35 

23:38 I'll give you a
little bit of things--

23:39 what are some ways you can
make sure that your computer

23:42 system that is going to
classify things by similarity

23:46 follows your intuition
of what is similar,

23:49 and not somebody else's
intuition for what is similar?

23:54 So that's going to be the main
theme for the rest of this.

23:57 So we are intelligent people.

23:59 We are intelligent musicians.

24:01 We make these
choices, and yet we

24:04 are making differences on how
far and how similar they are.

24:09 So, in fact, I'm going
to blank the screen

24:11 and say the one takeaway
from today's lecture, I hope,

24:16 and from all these
things, is that there

24:19 is no right answer for the
similarity between two melodies,

24:25 between the similarity
between two pieces.

24:28 There may be wrong answers.

24:30 I will not deny that,
that if somebody

24:33 said that F was closer to, I
don't know, than the same thing

24:37 with one note
changed or something,

24:39 I would think that that might be
wrong, that your program might

24:43 be malfunctioning.

24:44 But there isn't a right answer.

24:45 And a lot of it--

24:47 what's different
between good answers

24:50 are what we think
of as important

24:53 when thinking similarity.

24:55 There is a yearly competition--

24:57 I think it's been
suspended since COVID,

24:59 so I don't know
if it's restarted,

25:01 but for the algorithm
that can classify songs

25:06 as the most similar.

25:07 And here is a place
where I would say,

25:09 what are your ground truths?

25:11 How do we trust that you
have gotten it right?

25:14 And are we just trying having
to recreate the views--

25:20 I won't say biases, but
the views of the people

25:22 who organize the conference and
what's that going to do for us?

25:28 So I want you to
start thinking that.

25:32 And I will tell you
what F is beforehand.

25:36 F is one that a lot of
computers' programs--

25:40 in fact, what I went aha
during one of these algorithms,

25:46 they could--

25:47 F is 1 that a number
of algorithms,

25:50 especially older ones, will
classify as the most similar.

25:54 Because what is F?

25:57 Unlike any of the other
lines, F has every single note

26:03 and every single rhythm,
if I did it right.

26:06 I was doing in my head.

26:07 Every single note and every
single rhythm from A--

26:10 just order didn't matter.

26:13 A is the counterset function,
the unordered version, the P--

26:20 yeah, the permutation does
not matter version of F.

26:25 Or F is the permutation does
not matter version of A.

26:28 Did I get it right?

26:30 AUDIENCE: It looks right.

26:31 AUDIENCE: It looks right.

26:32 

26:34 MICHAEL CUTHBERT: So
we're going to go quickly

26:37 through some things I
think you've probably

26:39 seen before, some ways
of measuring distance.

26:42 You all learned this at some
point, the Euclidean distance

26:47 between two points.

26:48 Take the square
root of the x terms.

26:51 Take the square
root of the y term.

26:53 Add, what, difference squared
plus difference squared

26:57 square root.

26:59 Square root of x squared
plus difference between x

27:02 and difference between y.

27:03 

27:06 So anyone seen this thing, where
the distance between these two

27:11 points, 3 comma 2
and 7 comma 8, is 10.

27:17 Taxicab distance--
Manhattan distance,

27:21 we'll go with taxicabs
since not all of us

27:23 have been to a Manhattan and had
the joys of taking a taxi there.

27:27 And so why this--

27:29 here, the distance was 10.

27:32 Here, it's approximately--
that's not a negative sign.

27:34 That's an approximate sign--

27:36 approximately 7.2.

27:39 Why is the distance
greater here?

27:42 Somebody who's done this
triangle inequality.

27:46 Talk English to me for a second.

27:50 Talk like you're talking
to your cab driver

27:54 who you're explaining to this--

27:55 cab drivers are really smart.

27:57 Talk, but who may not have
heard the final inequality.

28:00 What is represented
by the term Manhattan

28:03 distance or taxicab distance?

28:07 What's the notion-- intuition?

28:13 Yeah?

28:14 AUDIENCE: Go along the axes.

28:15 MICHAEL CUTHBERT: Go along
the axes or that go along--

28:19 let's get more literal.

28:21 One of the things that
we don't do so well

28:23 is step back into
the real world.

28:24 What is the distance traveled?

28:26 What constrains the taxicab
from not hitting distance of 7.2

28:33 but instead of 10?

28:34 Yeah?

28:34 AUDIENCE: You get straight
up and down to the side.

28:37 MICHAEL CUTHBERT: You
can only go straight

28:38 up and down to the side.

28:39 You can only go on-- let's
go even further back.

28:41 What, in Manhattan, if you
don't want to get arrested,

28:44 you can only drive on?

28:45 AUDIENCE: Streets.

28:46 MICHAEL CUTHBERT: Streets.

28:47 And the streets
in Manhattan go--

28:49 AUDIENCE: Orthogonal.

28:50 MICHAEL CUTHBERT: Yeah,
they're orthogonal.

28:51 There are these little lines.

28:53 So you are constrained
in where you can go.

28:56 So if there are constraints
on your distance,

28:59 and the most common one is you
can go up, down, left, or right.

29:05 You can't always do that
in Manhattan but because

29:08 of one ways.

29:08 But let's assume that we
have certain constraints.

29:11 You can be brought down.

29:12 Good.

29:13 I wanted to make sure
that we all have that,

29:15 and so that we can
start thinking about--

29:18 

29:21 first off, that what
operations are allowed

29:23 determines the distance metric.

29:25 What operations are
allowed determines

29:28 how far the distance are.

29:29 What are some operations
we do in music?

29:32 

29:36 That's a question.

29:37 What operations do we
allow and not allow?

29:40 Adam?

29:40 AUDIENCE: We could look
at many different models.

29:42 MICHAEL CUTHBERT: We can look at
midi difference between notes.

29:45 So therefore, we can take notes
and bring them higher and lower.

29:50 We can raise and lower notes.

29:52 What are other things we can do?

29:54 

29:58 What are some things you've
ever done with a piece

30:00 to make it a little bit
different or interesting?

30:04 Yeah?

30:05 AUDIENCE: You can
subdivide or combine notes.

30:08 MICHAEL CUTHBERT: You can
subdivide or combine notes.

30:11 Maybe you can, maybe you can't.

30:12 But yeah, quite often you can.

30:13 This is a context where you can.

30:16 Yeah, other--

30:17 AUDIENCE: --durations.

30:18 MICHAEL CUTHBERT: You can
change durations-- great, super.

30:22 How about this?

30:24 Which of these two chords
are closer to the first one?

30:29 The first one is going
to be C major versus--

30:36 

30:43 another little
similarity problem.

30:46 The second one was G major.

30:50 Sorry, the first
one was G major.

30:53 The second one, I went from
C major to C augmented.

30:58 Great, C augmented triad.

30:59 So those are two things.

31:02 Which one?

31:02 Who votes that from going from
C major to G major is closer?

31:08 Who votes that C major and
C augmented are closer?

31:12 Two people.

31:12 OK, great.

31:13 So a lot of it has to do
with your thought about--

31:18 well, on the augmented,
you're only changing one note,

31:21 and you're only changing by a
half step, the minimum distance

31:25 in our Manhattanized musical
world of midi and piano

31:30 keyboards.

31:31 That is, their minimum
distance is one half step--

31:34 not for all music in the world.

31:36 Great.

31:36 C major to G major--

31:38 you're also just moving one.

31:40 If you think of
something this way,

31:41 you're moving one
distance in what space?

31:45 AUDIENCE: [INAUDIBLE]

31:46 MICHAEL CUTHBERT:
Oh, what's that word?

31:48 AUDIENCE: Circle of fifths.

31:48 MICHAEL CUTHBERT: It's
circle of fifths space.

31:50 C and G are about
as close as you

31:53 can get without
being the identity,

31:55 C and F probably the other
way, although, I don't know,

31:57 maybe it's a one way
circle of fifths.

31:59 You only go around one
direction or another.

32:02 Great.

32:04 Based on the time,
I'm not going to go

32:06 through all these other
measurements of distance

32:09 that people can do.

32:10 Who has heard of
earthmover distance?

32:12 That is the amount
of work that it

32:14 takes to move one mound of
things over to another place.

32:20 And sometimes, you're
optimizing depending

32:23 on how much it costs
to move distance

32:26 and how much it costs
to move material.

32:29 You can end up with
different results.

32:31 

32:35 This was one of
the charts I think

32:36 I showed early in the
semester is here's

32:39 one place where
earthmover distance might

32:41 be a good use of
things of distances.

32:46 And then Levenshtein
or edit distance

32:49 is what was mentioned in--

32:51 do you use it in your work?

32:53 Yep, so that's where
you're talking about,

32:56 so the idea of how to change
the word Hyundai into Honda,

33:02 and no international East Asian
politics please for a second.

33:08 And you can think of every
time, OK, H and H are the same.

33:13 So it has a cost of 0.

33:15 Or we can delete the H and start
an O, and we have a cost of 1.

33:19 But we can find the
pattern of as we

33:22 change, we're going to
insert a Y after the H.

33:25 We're going to
substitute a U for an O.

33:28 This should be
symmetrical the other way

33:30 around-- different operations.

33:32 N is the same, so that's good.

33:34 D is the same, so it
doesn't cost anything.

33:36 So our cost function goes here.

33:38 And so we're trying to find
the minimum cost from going

33:41 from one end to another.

33:43 We don't have time to go through
all of the algorithms for this.

33:47 But Levenshtein
distance, edit distance,

33:50 has a lot of good
qualities that makes

33:53 it useful for a lot of
musical similarity tasks.

33:58 Just so that you can
say your professor

34:00 at least put the algorithm
up on the hand for a second.

34:04 But more importantly,
I think a lot of times

34:07 is thinking about the
particular costs of things

34:10 in a musical space,
in a musical world.

34:13 So for instance,
is deleting what--

34:18 we're trying to think about
two pieces, two melodies.

34:23 One of them deletes
the first note.

34:26 What would you call
the cost on that?

34:28 Well, maybe 1.

34:30 But then, if it doesn't make
up the total rhythm later,

34:36 and everything from here
on is going to be off,

34:38 and it's one line within
an orchestral piece,

34:41 that might be a higher
cost, maybe some--

34:46 and the classic debate
is whether changing

34:49 a note is that the same
or changing a letter

34:53 in something like this?

34:55 Is this the same?

34:56 Does this cost 1
or does this cost--

34:59 well, one way you can change
a letter is you delete it,

35:02 and then you add a new
letter back with a cost of 2.

35:06 And these are things
that come up quite a bit

35:09 in similarity search.

35:11 And just really want to say that
it comes up a lot in music--

35:15 don't borrow your distance
metric from somebody else.

35:19 Different ones might be used
for different situations.

35:21 So the distance
between dog and gato--

35:25 well, we can substitute d for g.

35:29 I don't know, or maybe
we add other things.

35:31 But I'm going to assert
that, in some situations,

35:34 the distance might be
2 between dog and gato.

35:38 What we do is we use the
substitute closely related

35:42 pet function for cost of 1.

35:44 So dog becomes cat, and then
translate English to Spanish

35:48 might cost 1.

35:50 And if you think about
large language learning

35:53 models and things,
you might want

35:55 to have functions like this.

35:57 And, in fact, this is not a
digital humanities text class.

36:02 But if it were and we
were doing computation,

36:04 we'd definitely be talking about
an algorithm called word2vec,

36:08 which was one of the earlier
successful algorithms

36:11 for trying to predict what words
are similar to other words, what

36:16 words are synonyms, so you can
create a kind of cost function

36:21 that is for this word is a
synonym for this one that

36:24 has been substituted
that is lower than this--

36:29 then this sentence is
different from this one

36:31 because it's using a
completely different concept.

36:34 

36:37 I'll skip that.

36:39 So when we're thinking
about these distances

36:44 and these weird things
like substitute dog for cat

36:49 on low-cost substitute
cat for gato

36:51 at low cost, what's the term
that we spent a lot of time,

36:57 maybe even too much
time for-- it felt

36:59 like at the time-- talking about
earlier in this semester, that

37:02 helps to think about things
that are not the same,

37:06 but might be closely
related to each other?

37:08 

37:13 AUDIENCE: Equivalence.

37:14 MICHAEL CUTHBERT: Equivalence,
or equivalence classes, yes.

37:16 So one of the things
you might want to do

37:18 is define what equivalence
classes it could be.

37:21 I mean, I think last--

37:23 other times, I've given the
exact same melody up an octave,

37:27 and everybody
immediately said, oh,

37:29 that is basically
the same thing.

37:31 So everybody was
very quickly putting

37:33 in an oh, equivalence
class things.

37:36 So I wanted to make
sure that we had that.

37:41 And so once you have
these distances,

37:44 we tend to go through-- and this
is if you're in a biology class,

37:48 you'll spend a lot of
computational biology,

37:50 a lot of time on this--
sequence alignment,

37:53 a kind of distance
metric where you're

37:55 trying to find the minimum
distance between two things

37:58 that you believe might represent
the same type of thing.

38:03 Or you might say it's
innocent until proven guilty.

38:06 We'll first try to see if they
can be changed into another

38:10 thing at a low cost and then
discard once we realize the cost

38:15 cannot be minimized.

38:17 I will say that algorithms that
can be short circuited, that you

38:21 can prove at a certain
point you can't

38:24 do better than this cost will
speed up a lot of your run times

38:31 because once--

38:32 you might say that
there's no way

38:36 that this could be better than
20% or it could be-- yeah,

38:44 there's no way that this could
possibly be better than 90%

38:47 similar to this.

38:48 So I'm going to stop looking
at the rest of the piece

38:51 or whatever your cut off.

38:54 So one of the classic things
for sequence alignment

38:58 is trying to find--

38:59 this is Google's data
set they released

39:02 at the height of Britney
Spears popularity of all

39:06 the number of searches
that they believed

39:09 were trying to find the top
left one, Britney Spears--

39:14 actually really,
really impressed

39:16 that the number of correct
spellings of a hard name

39:20 to spell outweighs the rest.

39:22 Anyhow, that's
all we're talking.

39:23 And the people who are
really, really good

39:27 at this-- and any time
I'm trying to figure out

39:30 a similarity sequence
alignment or a similarity task

39:34 that I don't know is to
look at the people who

39:37 are trying to align
base pairs in biology

39:42 or trying to align genes because
they have many, many options.

39:52 So I'm just going
to keep pounding

39:55 this term in as many
different ways I can do.

39:58 All the things that
we're just working with--

40:00 Hyundai, Honda, Britney Spears,
genes, those are all strings.

40:06 But we work on notes and clefs
and things like notes and stuff,

40:10 but things like that.

40:11 So how do we get them in?

40:13 So this is great to get this
from two different people,

40:16 same thing-- we use
things called hashes,

40:19 which are very similar to
the concept of viewpoints

40:23 to the rescue, so that--

40:25 try to convert things--

40:28 hash and note.

40:29 We might say that here are
equivalence classes all notes

40:33 that are names with octave.

40:34 And so we might hash a stream by
just joining all the hash notes

40:39 for all the notes in there.

40:42 You will find, in Music 21,
if you're working on it,

40:46 there's a bunch of
tools for this already.

40:48 They're in
music21.search, a module

40:51 that we have not
talked about now

40:52 and we will not
talk about again.

40:54 But if you're doing
a lot of searching,

40:56 it's probably worth reading
the module reference for it.

41:01 I think that there
might be a user's guide,

41:03 but I can't remember
if I finished it

41:05 or if it just trails
off after a few words.

41:08 So we might take a string,
convert it to a stream--

41:13 that's hard to say very fast--

41:15 and translate it.

41:17 And we might have
some of hash function

41:20 that tries to make everything
into an ASCII character.

41:27 Though there's no
reason that everything

41:30 needs to be turned into a
string like nameWithOctave.

41:34 In a lot of ways, strings
are just arrays of ints.

41:41 

41:43 We're talking about that A--

41:53 no, lowercase a is generally
represented internally

41:59 as anyone-- remember number?

42:01 AUDIENCE: 97.

42:01 MICHAEL CUTHBERT: What's that?

42:03 97 or 96, I can't remember.

42:05 96?

42:06 Yep, and capital
A-- is that one 60--

42:08 AUDIENCE: 65.

42:09 MICHAEL CUTHBERT: 65.

42:10 OK, so some people
some people know these.

42:12 I used to have them
all top of the head.

42:13 So all the letters
you're doing have

42:16 a particular representation.

42:17 And back in the bad, bad days
of the '60s and '70s, different

42:22 computers would have different
representations for this,

42:24 and then we all agreed on the
same representation for letters.

42:28 And then we remembered that
there are other things in the--

42:33 other characters in the world.

42:36 That looks too much
like an A. How do I

42:38 do a jin or something, or an
alpha, beta, things like that.

42:43 And then, for a while,
we had a big problem

42:45 that they weren't all
converging to the same thing.

42:47 Anyhow, digression aside,
maybe we'll get to the point

42:51 where we can start converting
things besides midi numbers

42:54 and notes into something
more standardized

42:58 because, right now, the
midi numbers is basically

43:00 the only standardized
notes, which is probably

43:03 why midi keeps being used for a
lot of computational projects.

43:10 So the hard part is
always finding out

43:14 what numbers we should
use to represent a note.

43:18 

43:21 So if we're going to
convert nameWithOctave

43:24 and we want to make
a string, and then

43:26 we want to make it
a number, and then

43:27 we want to have a
whole bunch of numbers,

43:30 what have we just recently
seen that looks like a tool

43:35 to take a score or
a part or something

43:39 and works like a
hash or a viewpoint

43:42 that tries to convert it
to a bunch of numbers?

43:44 

43:53 Not asking you to think too
far back, but farther back

43:58 than today.

43:58 

44:02 Yeah?

44:02 AUDIENCE: I'm getting a
feature representation.

44:04 MICHAEL CUTHBERT:
Yeah, extracting

44:05 features, getting a
feature representation.

44:07 Yeah, so feature
extraction and this kind

44:10 of viewpoint searching go
hand-in-hand with each other.

44:15 So if it's partially why once
you finish up a search function,

44:20 you're just going to
want to probably try

44:22 to see if AI or machine
learning can do it

44:25 better because you have
everything ready to go for it.

44:27 But sometimes what we extract
is different from others.

44:32 I want to give a little bit
of a caution that back then--

44:39 of course, you had
to do a little final,

44:41 a final project called the UAP--

44:43 and we thought that
making these viewpoints,

44:45 making a hashing system for
Music 21 for comparisons

44:50 would be a nice senior project.

44:52 And then we both
realized that, no,

44:56 it's a lot bigger than we
thought and a lot more complex

44:59 than we thought, and so
it needed to be an M. Eng.

45:02 Emily Zhang was great at
creating this and great,

45:04 oh, we did a really
great M. Eng project.

45:06 And then we realized,
no, this really

45:10 needs to be a PhD project.

45:12 We did not continue on--

45:15 there are so many difficult
parts of hash algorithms

45:19 because you want to
think about things like--

45:23 yeah, we'll not get to it--

45:27 going all the way
back to the beginning,

45:32 how can we create a
viewpoint or something

45:36 that allows D not to be totally,
totally different for anybody

45:42 who didn't put D as the last
of all possible results?

45:48 What kinds of hashes--

45:51 what kinds of numbers would we
need to represent a piece on

45:54 to make D not the worst
and really make sure

46:02 that F isn't the best?

46:05 So that's going to be our
last 5-6 minutes of class.

46:07 I want you to talk with 5
minutes of y'all talking with

46:11 each other, and 5 minutes of
y'all talk and talking to me.

46:14 So what kinds of
feature extraction,

46:18 what kind of hash function,
what kind of viewpoints?

46:20 These are all slightly
different concepts,

46:22 but they're all
in the same area.

46:23 What kinds of
equivalence classes

46:25 will you need in order
to make this happen?

46:31 Go ahead.

46:34 OK, I hear words continuing
but less frequently.

46:38 Let's talk about what
are some of the ways

46:41 that people thought to create
a strategy that doesn't

46:45 make D and F about the same?

46:48 

46:52 Yeah, go ahead.

46:53 AUDIENCE: You could look at
the sequence of local maxima

46:55 and minima.

46:56 MICHAEL CUTHBERT: Local
maxima and minima.

46:58 OK, I think I know what
you're talking about,

47:00 but let's give you
a little example.

47:02 Let's talk about
A. What do you--

47:04 AUDIENCE: So you
could maybe argue

47:06 that the C is the
local minima, and then

47:08 the F is higher than both of its
neighbors, so it's a maximum.

47:11 And then a D is a minimum,
the E's a maximum,

47:14 and then the D and C after that
are not really anything until

47:18 you hit the A on the 16th note.

47:21 MICHAEL CUTHBERT: Cool.

47:22 So yeah, we're just
looking at every time

47:24 the direction changes
of the pitches.

47:26 Great.

47:27 And compare that-- so beginning
A has G, F, D, E. Here,

47:32 we have D, F, G--

47:35 a tiny bit different, D,
F, but then going down to--

47:39 a little bit different,
but it's at least

47:41 giving some numbers we have.

47:45 Always the question is,
does your current streak

47:48 end when you hit a rest or not?

47:51 And maybe it depends on how
long the rest is, so good.

47:54 Other strategies?

47:56 Adam?

47:57 AUDIENCE: I would look at
where offsets are the same

47:58 and then check that their
notes are the same or not.

48:01 MICHAEL CUTHBERT: Great.

48:02 So we're going to look at
offsets that are the same

48:04 and see if notes
are the same or not.

48:07 That works really well.

48:08 And what I'd love to do, if
this were, what do you call it,

48:12 the generalized
adversarial problem

48:15 set, the gain problem
set, where one team

48:17 has to solve the problem.

48:18 The other team has
to keep giving them

48:20 things that break that.

48:21 I think it was a great idea.

48:23 And I think it would
work in general.

48:25 But I could generate something
where all I insert is

48:32 let's insert a 64th rest at
the beginning and then put all

48:36 random notes.

48:37 And you're going
to end up with--

48:39 and then maybe we'll put one
note that's the same at the end.

48:42 And you could end up with 100%
of the notes on the same offset

48:47 are the same.

48:50 I think we would really
work in the real world,

48:53 but we might want to always
think about something like that,

48:57 too.

48:58 Great idea.

48:58 John?

48:59 Then two people.

49:00 AUDIENCE: [INAUDIBLE] so first--

49:02 MICHAEL CUTHBERT: You can say--

49:04 AUDIENCE: --builds
up on what Adam said

49:06 AUDIENCE: But first, you
take a look at the notes

49:09 and do a set, kind of like
crossover between a set of D's

49:14 and aces and then ASes.

49:16 So both of those would still
show up relatively high.

49:19 And then compare
the offsets, which

49:22 would obviously take
up a bit, but still

49:24 keep D relatively high.

49:26 MICHAEL CUTHBERT: Super.

49:27 When we're talking about
offsets, are we talking about--

49:30 what kind of offsets?

49:33 AUDIENCE: We're in the--

49:34 I guess within the two
measures that the notes being--

49:37 MICHAEL CUTHBERT: Great.

49:37 Where in the two measures?

49:38 Where in the measure?

49:40 We sometimes want to do global
offset from the beginning

49:43 of the measure.

49:44 But then you can't identify
similar phrases or, all it takes

49:49 is put a repeat, put the first
four measures, repeat it once,

49:53 and suddenly the whole rest
of the piece is different.

49:55 So yeah, that's great.

49:57 AUDIENCE: If you
just start at time

50:02 equals 0 and go all the
way through the piece,

50:04 like anytime the two pieces
have the same pitch, you score--

50:08 so the alpha that they
both have on beat two

50:10 would be like a
quarter point because--

50:13 MICHAEL CUTHBERT: The F that
they both have on beat two

50:16 would be a quarter
point because--

50:17 AUDIENCE: Their duration
is only for that 16th note.

50:20 MICHAEL CUTHBERT: Got you.

50:21 So we look at shared duration.

50:23 Great.

50:24 I like that a lot.

50:25 Did anybody try to come
up with a equivalent?

50:28 Yeah?

50:29 The contour ends up being a
kind of a new equivalence class

50:32 that we hadn't talked about,
which kind of works out

50:34 in thinking that everything
that doesn't change directions

50:38 is a kind of passing tone, even
though not in the proper music

50:43 theory term, and
so can be ignored.

50:48 By the way, the one
I use quite often

50:50 is I'm just going to look
on downbeats or on beats

50:54 and ignore everything else,
and that works pretty well

50:57 for a lot of things.

51:01 

