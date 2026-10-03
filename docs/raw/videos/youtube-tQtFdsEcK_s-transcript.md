---
source_url: https://www.youtube.com/watch?v=tQtFdsEcK_s
source_type: video
ingested: 2026-10-02
published: 2026-10-02
duration_minutes: 22
language: en
sha256: 8cfbfda4434d735d647e675ee13ea39ccf715c919249ba096a5420f0366c376b
time_sensitive: True
---

# YouTube Transcript: E01: What is the FASTEST Computer Language?  45 Languages Tested!

## Video Information
- **Title**: E01: What is the FASTEST Computer Language?  45 Languages Tested!
- **Video ID**: tQtFdsEcK_s
- **Published**: Unknown
- **Views**: Unknown
- **Language**: en

## Transcript
00:00 What's the Fastest computer language in the
world?

00:03 Find out in Dave's Garage where today it's
time for the latest round of the biggest software

00:07 drag racing extravaganza yet.

00:09 We're pitting 42 different computer languages
against one another in a no holds barred Battle

00:13 Royale of prime number generating madness
with no quarter given and none asked.

00:18 Who's the fastest and who's the slowest and
where does YOUR favorite language rank relative

00:22 to the big dogs like C, Rust, and Assembly
language?

00:26 It's an episode so compelling that if you're
not watching you better be dead or in jail.

00:30 And if you're in jail, break out!

00:34 [Intro]
Hey, I'm Dave, welcome to my shop!

00:41 I'm Dave Plummer, a retired operating systems
engineer going back to the MS-DOS and Win95

00:46 days, and today's going to be a lot of fun.

00:48 A few months back I had what started out,
I think, as a pretty cool idea: take a standard

00:53 prime sieve and then write it in C, Python,
and C# to see how the performance compared

00:58 and what code written in the different languages
actually looks like and how the languages

01:02 differ.

01:03 You should absolutely check out that first
episode for the detailed comparison, but after

01:06 I posted it, something blew up.

01:08 [Boom]
No, not, not like that.

01:11 I mean it blew up on GitHub, and in a good
way.

01:13 I uploaded my code in those three languages
and soon enough, something amazing had happened.

01:18 People started porting my code to other languages.

01:20 They improved on my implementations and added
many new ones.

01:24 And now, from Ada to Zig, we have over 100
implementations in some 45 different programming

01:30 languages, and as we go, we're going take
a brief look at every one of them.

01:34 You'll get to see the same algorithm implemented
in each language so that I can show you the

01:38 basics the language syntax, data declarations,
structure, and simple I/O.

01:42 It'll be a quick tour where you learn just
enough about each language to be dangerous

01:45 and perhaps entertaining at cocktail parties.

01:47 That in and of itself is amazing, but it wouldn't
be that useful unless there was some way to

01:51 keep track of all these implementations and
even find out how they performed relative

01:55 to one another.

01:57 Being new to GitHub collaboration, not to
mention busy with writing code and speeches

02:00 and making these videos, I realized there
was no way I was going to be able to do a

02:04 good job of it, so I turned to you guys, the
viewers, for help, hoping someone knowledgeable

02:07 in the way of forks and branches would step
forward and volunteer.

02:10 I didn't have to wait long, as right away
a fellow named Rolf in the Netherlands offered

02:14 to take over.

02:15 I handed him the keys to the kingdom and hoped
for the best, and I was not disappointed.

02:20 Pretty soon the amount of work grew and Tudor
from Romania joined the effort along with

02:23 Rutger, who is also of the Netherlands.

02:25 Together they've not only whipped the project
into shape, organized and made sense of it,

02:29 but even contributed new implementations.

02:31 I'm indebted to everyone in the community
who pitched in, but it just wouldn't have

02:33 been possible without the hard work of these
three guys especially.

02:35 You can imagine that with all of these languages
this could quickly turn into a giant mess.

02:39 It's hard enough to get a single project to
compile and work on everyone's machine everywhere,

02:43 but now we're talking about a build process
that uses potentially 40+ different languages!

02:47 I don't know about you, but I sure don't have
Cobol or Fortran compilers ready to go on

02:51 my machine, let alone V or Zig.

02:53 The other problem is testing them all.

02:55 You'd have to run up to 100 different implementations
in those 40 languages and collect results

03:00 data and then somehow put it all together
into a useful report of some sort.

03:04 I'm very happy to say that everything is completely
automated so that a single make command automatically

03:08 not only builds and benchmarks all 40+ languages
but it also collects the statistics and tabulates

03:14 a comparison report at the end . You can literally
enlist in the GitHub project and type 'make'

03:19 and given some time, you'll get a full report
of the performance of every language on your

03:23 personal machine.

03:25 Thanks to the magic of Docker and the Primes
team, there are 40+ complete development environments

03:29 set up and ready to go.

03:30 That's some high-level stuff!

03:32 If you think you can make a prime sieve faster
and have been looking for an open source project

03:36 to dip your toe into, check out the video
description for a link to the repository.

03:40 If you've never worked on an open source project
before, this could be a great place to start,

03:44 and we'd be more than happy to have you as
a contributor.

03:47 I do ask that the primary focus being improving
and optimizing the implementations already

03:51 in the tree before simply adding new ones.

03:53 For me, there are two very cool and valuable
aspects to this software showdown.

03:57 The first is that we get objective speed comparisons
between the languages.

04:01 If you've wondered how C++ compares to C#,
or how Python compares to Ruby, even Pascal

04:06 to Ada, we've now got the hard facts, at least
when it comes to high-speed memory and bit

04:10 manipulation.

04:11 I was particularly looking forward to the
Rust results to see how memory protection

04:14 impacted code like this relative to a raw
C implementation.

04:17 So, which languages are represented?

04:19 Well, as just a partial list we have ARM and
x86 assembly, Ada, Basic, C, C++, C#, D, Dart,

04:28 Delphi, F#, Fortran, Go, Haskel, Java, Julia,
Lisp, PHP, Pascal, Perl, Python, Ruby, Rust,

04:37 Scala, Swift, TypeScript, V, and Zig.

04:40 There are actually quite a few more, and in
many cases, we have multiple solutions in

04:44 each language.

04:45 That's how we wind up with more than 100 variations
in total.

04:49 We also have single threaded and multithreaded
solutions.

04:52 In each case the goal is always the same:
solve for all the prime numbers up to one

04:56 million.

04:57 Do that as many times in five seconds as possible,
and then report the average number of passes

05:02 per second.

05:03 That number - prime sieve passes per second,
becomes the language's performance score in

05:07 the drag race.

05:09 It's worth noting that the language itself
is in fact the primary factor in the results.

05:13 For example, Python, being an interpreted
language, is going to be necessarily slower

05:17 than C or Rust.

05:19 But that doesn't mean it's going to be slow.

05:21 After all, it's still running dozens or even
hundreds of passes per second, and that alone

05:25 is impressive.

05:26 But the languages that compile right to fully
optimized binary executables can measure their

05:30 results in thousands of passes per second,
so there's really no competition between them

05:35 if raw performance is the goal.

05:37 What you can do more fairly is to compare
results within language types - BASIC vs Python,

05:42 for example, or C vs Rust, or C# vs Java.

05:46 And that's exactly what we'll be doing: popping
a small handful of languages off the stack

05:50 in each episode that are related to one another
so we can compare and contrast them.

05:54 And it just makes a lot more sense to compare
Bash to Powershell than to, let's say, Rust.

05:58 Back in college one of my very favorite classes
was Computer Science 405 with Dr. Yang.

06:03 Disguised formally as a languages class, for
me it was really an excuse to play with a

06:07 wide array of different languages all within
a single semester.

06:11 From Ada to LISP to Prolog and more, Dr. Yang
introduced each language to us in his inimitable

06:15 style and then assigned a programming task
in it so that we were forced to become at

06:19 least somewhat proficient with each language.

06:20 Since then, I've spent a lifetime in operating
systems, but it's been entirely in assembly

06:25 language, C, and C++.

06:27 While I'm also recreationally fluent in C#
and dabble in some Python, that's about it.

06:32 As a result, the opportunity to tour more
than 40 different languages was simply too

06:36 good to pass up.

06:37 It would be like CS405 all over again but
turned up to 11, then on steroids.

06:42 Like the CS405 Turbo Plus 3D Max Professional
edition.

06:46 While I was genuinely curious about the results
of which language in each category would be

06:51 fastest, I was even more excited about seeing
the code for my sieve implementation ported

06:55 to all these different, and sometimes exotic,
languages.

06:58 Seeing the same algorithm ported to any new
language should be way more instructive than

07:02 if I didn't even know what the code was trying
to accomplish.

07:06 And my goal is to share whatever I can learn
about each language along the way with you.

07:10 To that end, then, we're going to break the
languages into groups and then run the benchmarks

07:13 between them.

07:15 Then we'll go through the code and see how
it's done in each language, and I'll point

07:18 out the interesting differences and things
that stand out to me about each.

07:21 Think of it as a little sampler of up to 40
languages, many of which I'd wager that you'd

07:25 otherwise hear of but never get to see.

07:27 Now you'll know just enough about each of
them to be dangerous and to appear clever

07:28 at cocktail parties.

07:29 It's worth noting that I'm just an old C programmer.

07:30 I'm not an academic, and I'm certainly not
someone like Dr. Yang who can offer you intelligent

07:35 comparative analysis between languages.

07:54 But I can show you how to do things like allocate
a packed bit array and a dictionary and run

07:58 a loop in each language, and even seemingly
mundane things like if/then/else control and

08:02 how to output your results to the console
can be worthwhile knowledge.

08:05 So, grab a helmet and a cup of coffee and
hang on as I take a look at the first group

08:14 of languages: Pascal, Delphi, and Ada.

08:20 Delphi and Ada are both based on Pascal, and
we'll see how they're similar, how they differ,

08:25 and which is fastest once we benchmark their
implementations later in this episode.

08:28 And before you even think about bailing because
you don't use those languages, remember that's

08:29 half the point: getting to see how the stuff
you never touch works!

08:30 Fortunately for us, the process has been completed
automated by the Github Primes team.

08:33 You simply enlist in the project, cd into
the folder, and run make.

08:37 From there it's all automatic.

08:39 All 100 or so implementations will be built
and executed and the results tabulated into

08:43 a report automatically.

08:45 The first run can be slow, as each language
comes with its own Docker container that represents

08:49 the build environment for that language.

08:52 But that's the genius of how they've set it
up, because it means you don't have to install

08:55 50 different compilers; you simply need a
working docker implementation and a few basic

08:59 tools like Git.

09:01 Let's start our tour with the Pascal implementation.

09:04 Pascal is an elegant procedural language that
lends itself to good programming practices

09:08 such as data structures and structured programming.

09:10 It was invented by Niklaus Wirth.

09:12 Americans will often call him Nicholas Worth,
and so he's been known to joke that Americans

09:16 call him by value whereas Europeans call him
by name.

09:18 Well, if you've got a better Pascal joke,
I'd love to hear it, so please leave it in

09:23 the comments!

09:24 Pascal was largely intended as an educational
language, but good compilers and tools back

09:28 in the 90s made it popular among computer
enthusiasts and even a few professional developers.

09:33 Most notable among these was Borland's TurboPascal,
which was written largely in assembly language

09:37 by Anders Hejlsberg [Haylsberg].

09:39 In the "small world" department, Anders later
went on to design C#, and is currently the

09:43 lead architect of that language at Microsoft.

09:44 [Pascal Code]
Let's dive right into the Pascal to get things

09:49 started.

09:50 The first thing we see is that Pascal supports
classes, and there is a PrimeSieve class with

09:54 the three main members that we've come to
expect: RunSieve, CountPrimes, and ValidateResults.

10:00 As you might expect, RunSieve does the prime
number calculations.

10:04 CountPrimes determines how many primes were
found, and ValidateResults compares the results

10:08 to known values to make sure it's all working
properly.

10:11 In case you've never seen Pascal before, one
thing that will look different right up front

10:14 is the assignment operator.

10:16 Where C uses a single equal sign for assignment
and a double equal sign for equality, Pascal

10:22 uses the single equal sign for equality testing
and then adds the colon-equal operator for

10:26 assignment.

10:27 Whenever you see the colon-equals operator,
something is being assigned to something else.

10:31 When you the equals sign by itself, something
is being tested for equality.

10:32 The one concern I have right away with the
Pascal version is that it's using a 32-bit

10:36 integer for the index into the map of primes.

10:39 That means it's limited to 32-bit values.

10:42 My initial implementation supported 64 bits,
so while this isn't a problem for the benchmark

10:46 testing as it only runs up to one million,
it is a broader limitation that you should

10:50 be aware of.

10:51 My original Sieve can handle up to 100 billion,
but this implementation can't go past about

10:55 4 billion.

10:56 As always, our prime sieve needs to keep a
bitmap of which numbers are prime or not.

11:01 Thus, if we're testing up to one million,
the program keeps a million bits in a row

11:05 to indicate which numbers are or are not prime.

11:08 That array of bits is named the NotPrimeArray
in this case.

11:11 The declaration of the PackedBoolArray is
interesting - it turns out that Pascal natively

11:15 supports packed arrays.

11:17 Normally, if you had an array of 8-bit or
even 1-bit values, they are stored in words

11:22 for faster memory access.

11:24 That does improve performance but wastes a
great deal of memory space.

11:28 A packed array squeezes all the data together
efficiently into an array of raw bits within

11:32 bytes.

11:33 It's slower to access but much more efficient
on space.

11:36 In some languages, like classic C, we would
need to do this work ourselves, but apparently,

11:43 Pascal does it for us.

11:45 The RunSieve function will return that packed
bit array to us for results and validation.

11:50 RunSieve itself has three main variables - the
factor by which we are stepping through the

11:54 array to eliminate primes, the number we use
to step through the array while marking off

11:58 those non-primes, and the square root of the
sieve size, which is the upper bound we need

12:03 to work up to.

12:04 As you can see, Pascal is very readable.

12:07 The loops are obvious, and it uses BEGIN and
END tags, rather than punctuation or indentation,

12:11 to delineate them.

12:13 Looking at the CountPrimes function there
are couple of interesting things to note.

12:16 You can see that the return type of a function,
in this case an Integer, follows the function

12:21 name in the declaration, and that variables
are given their own declaration section above

12:25 the code block.

12:27 Taking a quick look at the For loop, we can
see the use of the LOW and HIGH operators.

12:31 In Pascal you have the option of defining
the range of your array, by which I mean where

12:36 the array indices start and end.

12:38 Whereas in C arrays always start at index
0 and go up from there, in Pascal they can

12:43 start anywhere, even at a negative index.

12:45 Let's say you had an array of printable characters.

12:48 If you made the index into the array be the
ASCII code of the character, you could start

12:52 the array at 32, the first printable character,
and extend it up to 126, the last printable

12:57 character.

12:58 Any references to characters outside this
range could be caught by the compiler or at

13:03 runtime.

13:04 The Low and High operators tell you, the programmer,
where any given array starts and ends.

13:08 The ValidateResults function returns a simple
true/false value to indicate whether or not

13:13 the results can be confirmed.

13:15 The program contains a dictionary map of how
many primes can be found up to one hundred,

13:19 one thousand, one million, and so on.

13:21 If you results match the known values, the
function returns true.

13:25 Based on the way this is written, it appears
that Pascal doesn't support static declarations

13:29 of dictionaries.

13:30 Instead, an empty dictionary is created dynamically
and each of the value pairs is added programmatically

13:36 one by one.

13:37 Finally, let's look at where the Pascal version
prints its results.

13:41 There appear to be two functions of interest,
Write and WriteLine, which differ by whether

13:45 or not they automatically add a newline to
the output or not.

13:48 We can also see how the DurationTickCount
variable's output is formatted: in Pascal,

13:52 you can provide the total field width, which
is given as 4 in this case, and the decimal

13:56 part width, which is specified here as 2.

13:59 Whereas languages like C# and Java use bytecodes
or an intermediate language, the Pascal code

14:04 will compile and link down to a native binary.

14:06 Moving on now to Delphi, I should explain
that Delphi is technically a development environment,

14:11 not a language per se.

14:13 The underlying language is perhaps most accurately
described as Object Pascal.

14:17 The first versions of Delphi actually evolved
from Borland's Turbo Pascal, but it was decided

14:22 that the object-oriented extensions that had
been added to the Pascal language up to that

14:25 point in time were not ideal, so they effectively
started fresh and derived the language more

14:30 from Apple's Object Pascal.

14:32 Still, if I called it Object Pascal, I'd have
to explain that I really meant Delphi, so

14:37 we'll just call it Delphi for simplicity.

14:39 The Delphi code looks quite different, and
there are two reasons.

14:42 The first is that the object handling is different
in Delphi than in classic Pascal, and the

14:46 other is that each was written by a different
author in their own style.

14:49 In my original implementations I tried to
keep them as similar as possible between languages,

14:53 but in a few cases the authors took greater
style liberties.

14:57 If we can still learn from looking at the
code, though, that's the main thing.

15:00 Let's start with some simple things, the prime
counting and validation.

15:04 We can see that CountPrimes and ValidateResults
are both defined as member functions.

15:09 The former returns an integer, the latter
a Boolean.

15:12 Otherwise, the functions are quite straightforward.

15:15 The main loop is also similar to what we saw
with Pascal.

15:18 One thing that stands out is that the time
math here shows that Delphi contains the notion

15:22 of a timespan, and that durations can be converted
to units like total seconds.

15:26 This is likely more a function of the compiler
library, but it's quite reminiscent of the

15:30 .NET framework.

15:33 Rather than checking for null, which in C
is synonymous with meaning "no pointer value

15:37 assigned", Delphi has an explicit operator
called assigned to let you know if a pointer

15:42 has been set or not.

15:44 While I'd venture to say that in C, using
i++ or even i=i+1 has always felt quite natural.

15:50 In Delphi, however, you have increment and
decrement operators.

15:53 They accept an optional "how much to increment"
value and otherwise assume one if it is not

15:57 provided.

15:59 At the bottom of the PrintResults function
we can see the use of a Format function that

16:02 appears to provide C-style printf formatting
for strings and variables.

16:06 While I imagine the Pascal mechanism of total
and decimal field width's still works in Delphi,

16:11 you might prefer the expressiveness of this
printf mechanism.

16:14 The RunSieve function again shows the use
of the increment operator, but this time with

16:18 a variable increment amount.

16:21 Pulling back in scope for a moment to look
at the class declaration itself, we can see

16:24 that at least in this case, all data is private
to the class, but there are both public and

16:29 private functions.

16:31 Delphi appears to support virtual functions
as well, at least judging by the presence

16:34 of the override keyword.

16:36 The bit array is declared as an array of the
type ByteBool.

16:40 That means each bit is actually taking up
a full byte, rather than a single bit.

16:43 There are also wordbool and longbool types,
but they just waste even more space.

16:48 Because the Delphi version uses 8 bits per
prime, in my mind, it's not authentic to the

16:53 original, and so its score cannot be counted.

16:56 Add in the further complication of it needing
a commercial license for the environment,

17:00 of which we have only one, and you can see
why we generally omit its performance numbers

17:03 from our test matrix.

17:05 Since Delphi is just Object Pascal, Delphi's
performance is very similar to that of Pascal

17:10 itself when not doing object oriented programming.

17:14 We finally turn our attention to Ada, which
you won't be surprised to find out is another

17:17 declarative and imperative language just like
its progenitor, Pascal.

17:21 Ada has built-in language support for interface
contracts, extremely strong typing, explicit

17:27 concurrency, tasks, synchronous message passing,
protected objects, and non-determinism.

17:33 Ada is very popular with the military, and
if you're going to write the software for

17:36 a nuclear ICBM, odds are you'll be doing it
in Ada.

17:40 Perhaps one of the reasons is that Ada is
particularly adept at catching things at compile

17:44 time, rather than runtime.

17:45 Because after all, runtime is a terrible time
to find bugs in your ICBM code.a

17:50 I've long had a fascination with Ada, but
have never really more than dabbled with it.

17:54 What time I spent with the language convinced
me that by and large, if your code compiles

17:58 in Ada, it's got a very good chance of working.

18:00 Ada can catch things like invalid parameters,
range violations, invalid references, mismatched

18:05 types all at compilation time.

18:08 Because concurrency support is actually built
into the language, the compiler can even recognize

18:12 certain potential deadlock situations.

18:14 Dipping our toes into the code by starting
with CountPrimes, we see that the code is

18:18 written to use a 64-bit quantity, a long long.

18:22 The loop and if-then syntax are unremarkable,
and for most intents and purposes, this stuff

18:26 could be Pascal.

18:28 The output is similarly straightforward.

18:29 We can see that there are two ways of sending
output to the console: Put and Putline, the

18:34 latter of which adds the newline.

18:35 One novelty is that the string representation
of a numeric variable is obtained by looking

18:39 at its image attribute.

18:41 Before the apostrophe is the type and the
instance, if needed, is passed in parenthesis.

18:45 Finally, we look at Ada's RunSieve implementation,
which to me reads clearly enough.

18:50 It's perhaps reassuring that, at least at
the level of a prime sieve, the language looks

18:54 quite natural.

18:55 It's only when you start devling into topics
like concurrency that the language really

18:58 starts to get complicated, and we don't need
that for our single instance sieve implementation.

19:02 Well, we've had our quick peek at the implementations,
and that means it's time to race them.

19:07 As noted, Delphi will be represented by Pascal,
so it's a heads-up Ada vs Pascal showdown.

19:14 Before we do any racing, though, it's likely
a good time to let you in on the number one

19:17 rule of software drag racing club.

19:19 And that is that if you don't like the results
your favorite language is getting, you don't

19:23 whine online, you improve the code.

19:25 You get out your editor and head on over to
the github and you hack away until your code

19:29 is faster than my code.

19:31 And, while the individual races will be determined
by the state of the code as it is today, the

19:36 official winner will be determined by the
grande finale episode with the code as it

19:40 sits then.

19:42 That way you can improve anything you're not
happy with and achieve redemption for Powershell,

19:46 or whatever it is you're really, really passionate
about.

19:48 With that out of the way, let's hit the track.

19:51 Primes to one million, as many times as possible
for five seconds, head to head: Ada vs Pascal.

20:03 Ooh, that's gotta hurt for the Ada guys.

20:17 Especially because I thought Ada was now compiled
with GCC which I thought might give it a leg

20:21 up over whatever older tech the Pascal is
probably based on.

20:26 The languages are similar enough at this level
of coding that odds are this one comes down

20:30 to algorithm implementation, so if you're
an Ada fan and aficionado, you know what to

20:34 do.

20:35 And heck, if you're a Pascal guru, it could
be faster as well, I bet!

20:38 To put these results in some larger perspective,
the world record score recorded on that machine

20:43 on that day was 7301 per second.

20:47 The lowest score turned in by any language
that day was one pass every 294 seconds.

20:52 Clearly that's a huge range of results, and
part of what's going to make this tour so

20:55 interesting as we keep revealing languages.

20:58 For now, both Ada and Pascal can be found
on the top half of the bottom half of our

21:02 leaderboard.

21:04 We're just scratching the surface with these
first languages.

21:06 We've yet to even talk about scripting languages,
shell languages, functional languages, notationals,

21:11 and many more types.

21:12 We'll race and explore the highest performance
languages such as Rust, assembly, and C while

21:17 also looking at the exotics like F#, oddities
like LISP and Prolog, and even some comical

21:21 ones like the powershell vs bash showdown.

21:24 But unless you take the time to subscribe
to the channel and turn the bell on, you might

21:28 never know about them.

21:30 Which makes right now a really, really good
time to do it.

21:33 Because later means no.

21:35 If you enjoyed this episode, please find that
like button in the toolbar and Smash it real

21:39 good, or whatever the kids are doing these
days.

21:41 I don't even know anymore.

21:42 But I can count, and if lots of people like
and subscribe, it makes both me and the algorithm

21:46 happy.

21:47 So, click on it just to prove to yourself
it really does turn blue.

21:50 Thanks for joining me out here in the shop!

22:05 In the meantime, and in between time, I hope
to see you next time, right here in Dave's

22:26 Garage!

