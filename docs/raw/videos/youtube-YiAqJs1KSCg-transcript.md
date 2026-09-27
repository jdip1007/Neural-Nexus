---
source_url: https://www.youtube.com/watch?v=YiAqJs1KSCg
source_type: video
ingested: 2026-09-25
published: 2026-09-25
duration_minutes: 11
language: en
sha256: c570d6f839dd4572515ff503f45699c57f0657e435f52d172779ec84e1912747
time_sensitive: True
---

# YouTube Transcript: Video 9b: Introduction to MusicXML

## Video Information
- **Title**: Video 9b: Introduction to MusicXML
- **Video ID**: YiAqJs1KSCg
- **Published**: Unknown
- **Views**: Unknown
- **Language**: en

## Transcript
00:00 [SQUEAKING]

00:02 [RUSTLING]

00:04 [CLICKING]

00:07 

00:10 MICHAEL SCOTT ASATO CUTHBERT:
Hello, computational

00:12 musicologist and
music theorists.

00:14 While you're working on your
own representation formats,

00:17 I want to introduce one
representation format, indeed,

00:21 the most commonly
used representation

00:24 format for common Western
music notation scores.

00:27 And that is MusicXML created
by Michael Good around the year

00:31 2000.

00:34 Looking over at the
MusicXML website,

00:37 we can see their
version of Hello World!

00:39 As you know, in
programming traditions,

00:42 it's become traditional
to print out

00:44 the word Hello,
World to show how

00:48 a programming language works.

00:49 In music notation, it's
become common, instead,

00:53 to show how note middle
C would be represented,

00:58 whole note or
something like that.

01:00 And here's the example of that
middle C whole note in MusicXML

01:05 One of the things you
can see in MusicXML,

01:08 just like any XML
or HTML, we have

01:11 these things called tags which
are enclosed in angle brackets.

01:15 Then we have a
content for the tag,

01:18 and then the tag is closed
with those same angle brackets

01:22 with a slash in front.

01:24 Tags can enclose other tags.

01:27 So the score part encloses
a tag called part-name,

01:31 and then it's closed later.

01:33 And tags can also have
attributes, id equals P1.

01:37 And we'll look at those
in just a little bit.

01:41 Let's scroll down to the note.

01:43 So all of that is to set up what
we might normally do for a note.

01:48 So a note is a tag called note.

01:51 Within it, there's
a tag called pitch.

01:53 Within that, there's
a tag called step.

01:56 And the step has
a single letter.

01:59 This is very similar to music21.

02:02 In fact, I borrowed
these concepts from here,

02:06 so that the accidental
would be encoded elsewhere.

02:10 Then the octave is encoded
as a single number,

02:13 then the pitch is closed.

02:15 After that, we have
a duration tag.

02:18 And we'll get back
to that in a second.

02:20 But it's duration 4.

02:22 And then there's
something called

02:23 a type, which is different.

02:26 And it says whole, so it
says that this note's type is

02:29 a whole note.

02:31 We have the duration and
the type encoded separately,

02:36 because the type explains
to notation software

02:40 how to represent this note,
what it should look like.

02:44 And the duration, instead,
tells it how long it is.

02:51 So you could, in theory,
put a duration of any number

02:56 and a type of any
number, and you

02:58 could make things
that looked very

03:00 different from how they sounded
or how they were represented.

03:03 In practice, most
notation software

03:05 reads one or the other of these,
so that's kind of too bad.

03:09 The duration 4 does not, like
in music21 represent necessarily

03:14 four quarter notes.

03:16 What it does is it refers
back to the last tag

03:20 within an attributes
tag called divisions.

03:23 And this says how many
parts should a quarter

03:28 note be divided up into.

03:30 So in this case, because the
only note is a whole note,

03:34 we can just divide up the
quarter note into one part,

03:37 not divide it at
all, and then say

03:39 a whole note has four of these.

03:42 But if we were going to
later have an eighth note,

03:46 then this would have
to be at least 2,

03:48 because the quarter note can
be divided into two parts.

03:51 If we might have 16th notes, it
would need to be 4 because it

03:55 can be divided into four parts.

03:57 And if we were going to have
16th notes and triplets also,

04:02 then it would need to be 12
because you can divide it

04:06 into 12 different ways.

04:08 In practice, these
divisions usually end up

04:12 being much higher numbers.

04:15 Some people use 16, 3, 8,
4, which is a power of 2.

04:19 I like using a high power
of 2 multiplied by 3,

04:23 multiplied by 5,
multiplied by 7,

04:25 so I can exactly represent
triplets, quintuplets,

04:30 septuplets, things like that.

04:32 But you can change this
division with each,

04:35 I think, at least each measure,
so that you can make sure

04:38 that whatever you're going to
be representing will be there.

04:42 We can also see that
there's a key signature,

04:44 and that's marked in the
number of fifths from C.

04:50 So remember your
circle of fifths.

04:52 If you want a key signature
of D major of two sharps,

04:56 that would be 2.

04:57 If you want B major,
that should be 5.

05:01 If you want F major, well,
we're going the other way,

05:04 so that's going to
be negative 1, so we

05:06 can represent keys that way.

05:08 Time, you can
probably figure out.

05:09 Beats and beat type are 4/4.

05:12 Could be called numerator
and denominator.

05:14 But it is one of these
things about MusicXML

05:18 that the format likes to
show the musical meaning,

05:26 not just how it's
going to be laid out.

05:28 We have the clef.

05:30 Instead of saying
it's treble clef,

05:31 we say that it is
a G clef on line 2.

05:36 And so here is some of
the basics of MusicXML

05:41 You can go to musicxml.com
and read more about this.

05:45 We're going to look at a few
other components of MusicXML

05:49 before going on.

05:50 But you're not necessarily need
to learn everything about it.

05:56 So if we're looking
at how MusicXML works,

05:59 we're going to look at a
slightly more complex example

06:02 than just a single quarter note.

06:04 We have a vocal part
and then a piano part

06:08 represented on two staves.

06:11 Here, we're using
a divisions that's

06:13 a higher number than 1, negative
3 for the key signature,

06:20 and then we can
explicitly encode

06:22 that it's actually in minor So.

06:23 We're not in E-flat major.

06:24 We're in C minor, right?

06:26 

06:29 There's transposition.

06:31 But we don't need to
know that for this.

06:33 The pitch element, the note
element, I'm sorry to say,

06:37 sorry, can also have ties
on it and can have lyrics.

06:44 We can say that this is an end
of a syllable that ends "meil."

06:48 And we end in extension.

06:50 This is another thing you
can do in XML-based formats.

06:53 If you want to open a tag
and immediately close it,

06:56 you can just put a slash
at the end, instead.

06:58 

07:01 We'll look at tied notes, even
though it's just a little thing.

07:06 And that is that there
are two different parts

07:10 in a tied note in MusicXML
and for a number of things

07:14 in MusicXML.

07:15 There is the tie element
which represents conceptually,

07:21 is this note tie.

07:22 And then there is the
tied, with a D element.

07:26 And that says, how do we
draw the tie on the page.

07:30 So you can draw a tie
without having a note

07:33 that sounds tied or is
conceived of as tied.

07:36 Or you can have sounds conceived
of as tied but not drawn.

07:42 And this shows up
in other places,

07:44 namely in accidentals because
you can imagine a B-flat,

07:50 you conceive of it as
a B-flat, but you also

07:53 put a flat sign in front of it.

07:54 The next B in that same measure,
you conceive of it is B-flat,

07:59 but you don't put a flat
sign in front of it.

08:01 So there's a distinction between
how we represent a note on paper

08:07 and how we conceive of it.

08:09 And this is very
important, also.

08:11 We can look over here at chords
and see that a cord is simply--

08:17 here's a 3-note chord.

08:18 We start with a note.

08:19 It's a C in octave
4, And then we

08:24 have the next note
has this empty chord

08:27 tag that says it's part of a
chord of the previous note.

08:30 So in MusicXML, if
you want to know

08:32 whether something
is a chord, you

08:35 won't know it from
the first node.

08:36 You'll only know it
from the second note on.

08:38 Here's an example
where we have E-flat

08:41 altered by negative 1 semitones,
and then the next note G.

08:51 Here's a little example of
multi-part music, and especially

08:56 this part where we have
two different voices

09:01 in the same measure.

09:03 So we have two chords that
can be represented as just

09:06 a single set of note elements.

09:10 And then we have a chord
here and a chord here,

09:12 but in between, we have
this separate voice

09:15 with separate stem
directions and so on.

09:18 One of the things
that MusicXML does,

09:21 is that when you get
to a certain point,

09:23 you're reading through
all of your durations.

09:25 They're all considered
to be in a row.

09:27 You get to maybe the
end of the measure,

09:29 and you can back up a
certain number of divisions,

09:34 and then you can
go forward again.

09:36 In this case, you would
probably just back up 8.

09:40 But a lot of notation
software seems

09:42 to only use backup to go to
the beginning of the measure.

09:45 And then if you need
to skip forward,

09:46 you use a forward again.

09:49 And it is also customary,
though not strictly required,

09:53 I don't believe, but
almost a lot of notation,

09:57 things that read MusicXML, we
call them consumers of MusicXML.

10:01 A lot of them might
have a problem

10:03 or might crash if you don't
include what's customary, again,

10:07 then you end at the
end of the measure

10:09 by going forward
until the very end.

10:13 There's all kinds of
other things on repeats,

10:16 on sound suggestions, and so on.

10:17 But one of the
things you can see

10:19 is that, compared to
some of the thoughts

10:21 we had on compact
representations,

10:24 MusicXML is very verbose.

10:27 It takes up a lot of
space on the screen.

10:30 It takes up a good
amount of space on disk,

10:33 though not nearly as much as
this video would ever take.

10:37 So there is a compressed
format, and they call it MXL.

10:41 We call .XML or .musicxml, the
file extension for standard

10:45 MusicXML format, and .MXL
if it's just gzipped.

10:51 And right now, we're
working on ways

10:53 so that a gzip archive can
include the score, maybe

10:56 a compressed score, a
transposed score, and also all

11:00 of the parts.

11:00 So new things are still
coming out with MusicXML.

11:04 And we will turn to
learning more about MusicXML

11:08 from the creator.

11:11 

