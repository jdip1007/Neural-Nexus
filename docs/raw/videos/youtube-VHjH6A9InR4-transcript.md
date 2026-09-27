---
source_url: https://www.youtube.com/watch?v=VHjH6A9InR4
source_type: video
ingested: 2026-09-25
published: 2026-09-25
duration_minutes: 16
language: en
sha256: 5431ca7d3562358a2d856fdf453eb876bfa28e646479fb41c7c6a95131399059
time_sensitive: True
---

# YouTube Transcript: Video 6b: Representations of Ontologies: Craig Sapp’s Rosetta Stone

## Video Information
- **Title**: Video 6b: Representations of Ontologies: Craig Sapp’s Rosetta Stone
- **Video ID**: VHjH6A9InR4
- **Published**: Unknown
- **Views**: Unknown
- **Language**: en

## Transcript
00:00 [SQUEAKING]

00:02 [RUSTLING]

00:04 [CLICKING]

00:07 

00:10 MICHAEL CUTHBELT:
Hello everybody,

00:11 and welcome to our last
video, at least for a while,

00:14 on music representation.

00:15 And I want to talk about
a remarkable tool created

00:19 by a researcher at Stanford,
Craig Stewart Sapp,

00:22 that he calls the Rosetta stone.

00:26 I'm going to be skipping a few
slides from his presentation,

00:29 and I've added a few other
things, but in this module,

00:33 I will also present his entirety
of slides that he has given.

00:39 And my hat's off to Craig
Sapp for all he's done

00:43 and his generosity.

00:46 So the Rosetta Stone was a stone
discovered in, I think, 1799

00:52 and deciphered over the next--

00:56 I don't know-- 10 years or so.

00:58 That was a remarkable discovery,
because up until that point,

01:04 Egyptian hieroglyphics such
as those highlighted here

01:07 were not legible by anybody
living at that point.

01:13 But the Rosetta Stone had two
forms of Egyptian hieroglyphics

01:22 in the top two sections
and also at the bottom,

01:25 the exact same text in Greek.

01:28 And so since people knew
how to read ancient Greek,

01:31 they were able to
go through each

01:33 of the signs of
the ancient Greek

01:35 and figure out what the
signs of the hieroglyphics

01:39 and the two forms
of writing meant.

01:42 Craig Sapp's
Rosetta Stone allows

01:45 us to look at how different
digital representations of music

01:51 work by encoding the exact
same melody in, I think,

01:56 almost two dozen
different formats.

01:58 These are all the formats
that have ever been used,

02:01 but it's a good chunk of them.

02:02 So here's the melody, and it
has some interesting things.

02:07 Here it has different octaves.

02:09 It has key signature,
time signature.

02:11 It has beaming information.

02:13 The only thing it really--

02:15 well, some of the
things it doesn't

02:16 have are chords and triplets
and things like that,

02:20 but once you see how this melody
is encoded in a lot of formats,

02:24 you can figure out how
all the other things might

02:27 be encoded in those formats.

02:30 So here's an example of a code
that's not used as much today

02:34 but was once very important,
playing an easy code.

02:38 And you can see that we
have something like--

02:41 I can decipher, OK, maybe
that's a G on clef on line two,

02:45 and then we have
a flat on b 2/4.

02:50 And then we have an eighth
note with a dot on C.

02:54 And then I guess the
three means 32nd notes DC.

03:01 And there's a little
bracket around it,

03:03 and that probably means
they're beamed together.

03:05 Then we have two eighth
notes on C beamed together.

03:09 We have slash means
new measure and so on.

03:13 Throughout the
whole thing, we can

03:15 see that, oh, maybe octave
isn't encoded here or something

03:21 like that.

03:22 And we can figure
out how those go.

03:25 Here is another format.

03:26 This is primarily used
for folk songs called ABC.

03:30 And we can see that--

03:32 well, example.

03:34 Maybe that's the
title of the piece.

03:36 2/4 key is F. L means
the smallest possible.

03:42 Encoding is 16th note.

03:44 And then we see that C is
worth three of those 16th.

03:47 D is worth, I guess, 1/2.

03:50 C is 1/2.

03:51 C is worth two of those.

03:53 That's the eighth note.

03:54 C is worth two of those.

03:55 We have a bar line and so on.

03:57 And we can see that the
high C is encoded with C

04:00 with a apostrophe after it.

04:04 This is what's
called DARMS code.

04:07 It was once highly used,
but it hasn't really

04:10 been used very much recently.

04:12 And well, I don't know
how to read DARMS code,

04:16 but I think that the
numbers represent pitch.

04:20 Here we have an
eighth with a dot.

04:22 And T means 32nd, I'm
guessing, and so on.

04:27 We have some RSs, which
might mean rest 16th note.

04:31 This is GUIDO Music
Notation, which

04:34 uses backslashes to
indicate certain kinds

04:37 of musical elements.

04:39 We can see clefs keys,
meters are encoded in here.

04:43 Barlines are explicitly encoded.

04:45 And it looks like you put
a slash before a duration.

04:53 And there's some notes
that don't have durations,

04:55 but they seem to be the same
duration as before and so on.

05:00 I think it looks like
underscores our rest.

05:04 This is MuseData,
which Michael Good

05:06 said was one of the
inspirations behind MusicXML.

05:11 It's a little bit bigger
format, takes more space.

05:14 It was one of what
we used to use a lot,

05:18 these fixed position
encodings, so

05:20 that if you're writing
in a monospaced font,

05:23 every single place has
a particular meaning.

05:27 So you can look at column
eight or something like that

05:30 and see the duration.

05:31 And then, this was a major
positive step because it encodes

05:37 duration in terms of the
number of some things,

05:43 the number of 32nd notes
and also separately the look

05:48 of the duration.

05:49 And so you can still
see that in MusicXML

05:52 and formats that are
still in use today.

05:54 I really like the use of these
left and right square brackets

05:58 to indicate the start
and end of beams.

06:00 

06:03 Humdrum is a code that we have
encountered a couple of times,

06:07 and here it is.

06:08 And maybe it's
easier with humdrum

06:10 to rotate the musical examples
so we can see how things go,

06:15 maybe, maybe not.

06:16 But we can see that there's Ls
and Js that represent the starts

06:20 and ends of beams,
and different octaves

06:23 are represented by doubling
or tripling the letter.

06:29 LilyPond is actually
a set of macros

06:32 for the scheme programming
language, which

06:34 is a kind of variant on lisp.

06:37 And so you can actually write
computer code in LilyPond.

06:42 And here we have the
same representation.

06:45 You can see again
backslashes, indicating starts

06:49 of larger musical elements,
time signatures, barlines

06:54 that are explicitly encoded with
what they look like, and so on.

07:00 Melisma was an
interesting code format

07:04 that's a little bit similar to
what we might have with MIDI.

07:07 And what we're doing
here is we're encoding

07:10 only the numeric duration.

07:13 So we can say that, I
guess, 125 is a 32nd note.

07:19 And we can figure out
from there that 500

07:22 is an eighth note and so on.

07:24 And on the far right column,
we have the pitch encoded.

07:28 So we're losing here beams
and some other things.

07:33 We're actually even losing the
clef and the time signature,

07:36 but we do have an info tag that
tells us the key signature.

07:41 Allegro is a more compact
version of the same format.

07:45 It looks like we have
MIDI numbers, 72, 74, 72,

07:50 for C, D, C, and so on.

07:53 And I believe 64 is
encoding the velocity.

07:58 That is how loud each note is.

08:01 And since we haven't encoded any
dynamics here, they're all 64s.

08:05 And we have toward the end start
and end offsets of each note.

08:10 I think if we can
go through note 1,

08:12 2, 3, 4, 5, 6, 7, 8,
nine would be a rest,

08:17 and at 1, 2, 3, 4,
5, 6, 7, 8, we have--

08:24 sorry.

08:25 We're not doing start and end.

08:26 We're doing start,
offset, and duration.

08:28 And there we have a
start offset note eight

08:32 of 2.5, duration of one.

08:34 And then the next element
does not start at 3.5,

08:37 but it just starts at 3.75.

08:39 So we're not even
encoding rests.

08:41 We're saying that they are
gaps in the musical format.

08:48 Director musices is also a
lisp based format, I believe.

08:52 That's why we have all these
extra parentheses where we're

08:54 loading things into
a stack, and we

08:57 can see that we're encoding
the meter after the first note,

09:02 which is kind of interesting.

09:04 And 32nd notes are one over 32.

09:07 That's kind of nice.

09:09 The dotted eighth note
is three 16th notes long.

09:13 So we see 3/16 can be
an interesting format.

09:17 SCORE has come up at
least once in class.

09:22 It is perhaps the best, most
beautiful music editor ever.

09:29 This is how a user
might input SCORE,

09:34 and it makes it a little
bit easier to enter things.

09:36 You're putting slashes
between notes and so on,

09:39 and then it generates
an internal syntax

09:43 that specifies exactly where
on the page every note is.

09:47 And so musical
engravers really like

09:50 working with SCORE
because you can precisely

09:53 move things around.

09:54 Probably a professional
engraver would

09:56 have moved the C at the
beginning of the second measure

10:00 a little bit to the right
because it's a little bit close

10:02 to that bar line, and you might
confuse the bar line for a stem.

10:07 So SCORE is
sometimes still used,

10:10 even though it hasn't
been updated in decades.

10:14 This is MusicXML.

10:16 As we've seen from Michael
Good's presentation,

10:19 it is a much more
verbose format.

10:23 Things are displayed-- you
know-- it takes a lot more space

10:28 to do it.

10:29 But MusicXML was invented
around the year 2000.

10:32 Some of these other formats
were around since the '80s.

10:35 So there's a lot more space
on the hard drive-- well,

10:37 there are hard drives now--

10:39 to be able to store
all this information.

10:41 So here, Craig Sapp has simply
highlighted the part 1 measure

10:48 in order to see how this
would work in MusicXML.

10:52 MEI is another format.

10:54 You can't really
see things here,

10:55 but it's very
similar to MusicXML.

10:59 As we said, it's the format--

11:01 or as Michael Good said,
is a format mostly used

11:04 by professional musicologists
and almost nobody else

11:09 for encoding common
Western music notation.

11:12 I don't see it as
having advantages

11:15 over MusicXML, and in fact
has many disadvantages

11:19 because it's not
supported by many formats.

11:21 But MEI can also encode music
such as Medieval music, which

11:27 uses different
representation formats.

11:29 So it has a particular niche.

11:34 This is a standard MIDI
file represented in binary.

11:37 And it's a little bit
unfair to compare the two

11:41 because it's a binary format,
so we can't really see anything.

11:45 But look at what's
being highlighted.

11:47 Here we begin with 00 90, which
is the indication for a note

11:53 off.

11:54 So we're ending
the previous note.

11:56 If we go to the beginning of
the next line, we can see 80,

11:59 which is the beginning of a
note on, and then 4d, which--

12:04 let's see if I can still
wear my hexadecimal.

12:07 So four times 16 is 64.

12:10 Add d to that, that is--

12:13 what is that?

12:16 I don't know, 14, 13.

12:18 And so you end up
somewhere around 78 or so,

12:22 which is the representation
of the note f.

12:25 And then the 40 after
that is 64 in decimal.

12:32 And so that would
be the velocity,

12:35 how hard we're hitting.

12:36 Since velocity hasn't
been encoded in this

12:39 and there's a number
between 0 and 127,

12:42 64 seems a pretty good number.

12:44 And then, we date that the
note is turned off with the 90,

12:50 and we say it's turned off
after a certain amount of time.

12:54 So how much time has passed.

12:56 And you'll see this 51
seems to be a representation

12:59 of the length of a 16th note.

13:04 If you really want
to look at MIDI.

13:06 you want to use a translator.

13:08 There's one in music21.

13:10 There's one other places that
will translate this format

13:13 into a series of events like no
ons, no offs, pitch bends, time

13:18 deltas, which move
us forward in time.

13:21 That will allow you to
actually give this particular--

13:25 a fair shake.

13:28 You can see also this is NIFF
format, which Craig Sapp has

13:35 translated some of
the hexadecimals

13:40 into particular letters so
that we can see what they are.

13:45 Somewhere in the middle
of the page I see clef,

13:47 I see fing, fingering, I see
a font change, glissando harp.

13:51 I'm not sure that this is--

13:53 oh, these are just all the
things that could be in here.

13:56 So we haven't even gotten
to encoding the piece yet,

14:01 but basically NIFF encodes
where each shape is on the page.

14:06 It is a format used
by music scanners.

14:10 It's not used very much
anymore, but the idea

14:13 is that it's much more important
to get an exact representation

14:16 of what the page
looks like rather than

14:19 what it might encode.

14:21 The last format, which
in this presentation

14:25 collects outputs first, isn't
really a digital format at all,

14:29 but it is the
Braille music code,

14:31 which is an encoding
of music notation.

14:35 That was created by Louis
Braille at about the same time

14:39 that he created the TeX Braille.

14:41 So he was really interested
in music encoding also.

14:45 And we can see some parts of
Braille that does encode a clef,

14:50 even though it's not
really used in the reading,

14:53 because we're going to
encode specific notes.

14:56 Why encode a clef?

14:59 Because blind and
visually impaired

15:02 musicians often need to talk
to musicians who have sight.

15:06 So it's easy to say, well,
you know, it's in treble clef

15:08 and there's one flat
key signature and so on.

15:11 And so there's a time
signature and then--

15:14 that's not October 5.

15:16 It's octave five.

15:17 We set the octave, and we
see that there's a C8th.

15:20 We encode an augmentation dot
D 32nd, C 32nd, C 16th, F 16th,

15:28 and so on.

15:31 Interestingly, we can
usually get both the note

15:34 and the duration into a six dot
segment, which would represent

15:41 six bits or less than a byte.

15:43 So it's a very
efficient encoding.

15:45 That makes reading music
with your fingers very fast.

15:51 If you want to know
more about the Rosetta

15:54 Stone and these various
musical encodings,

15:56 I have also included Craig
Sapp's watch all video.

15:59 Thanks for watching.

16:01 

