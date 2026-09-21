---
source_url: https://www.youtube.com/watch?v=VYTF4KIF2z0
source_type: video
ingested: 2026-09-19
published: 2026-09-19
duration_minutes: 16
language: en
sha256: 11ab45707cd929cdce3dd25170af749960e72bef6a14aba91896df2ebaf58b28
time_sensitive: True
---

# YouTube Transcript: Why I Deleted printf() from Windows COM in 1994!

## Video Information
- **Title**: Why I Deleted printf() from Windows COM in 1994!
- **Video ID**: VYTF4KIF2z0
- **Published**: Unknown
- **Views**: Unknown
- **Language**: en

## Transcript
00:00 Have I ever told you about the time that

00:01 I made a core Windows routine about a

00:03 hundred times faster and Microsoft

00:05 somehow forgot to rename the campus

00:06 after me? Yeah, me neither. Because what

00:09 actually happened was I checked in the

00:10 code. Somebody in the code review said

00:12 something spiritually equivalent to

00:14 cool, nice one. And then everybody went

00:16 back to work, which is I later learned

00:18 exactly how it should be. But I was a

00:21 kid and when you're young, every clever

00:22 optimization feels like you've just

00:24 split the atom in your dorm room. Now,

00:26 the routine in question did something

00:27 almost offensively simple. It took an

00:29 iid, which is a comm interface

00:31 identifier, and converted it into the

00:33 familiar string form of a grid. You've

00:36 almost certainly seen these things

00:37 before. Curly braces, eight hex digits,

00:40 a hyphen, four hex digits, another

00:41 hyphen, and so on. If it looks like a

00:43 license plate designed by a mainframe,

00:45 the registry is full of them. And if you

00:47 use regedit, you'll see a lot of them

00:48 there. And your first instinct might be

00:50 to ask, Dave, why would anybody care?

00:53 How often do you really convert a grid

00:54 to a string? And that is exactly the

00:56 trap because in comm IIIDs are not

00:59 decorative. They are the fingerprints of

01:01 the entire object model. Comm is

01:03 basically a civilization built out of

01:05 tiny contracts and every one of those

01:07 contracts is identified by unique 128

01:10 bit number that says this interface is

01:12 this interface and not some interface

01:14 that merely looks pretty similar if you

01:15 squint. Query interface is built around

01:17 it. Marshalling depends on it. Proxy and

01:20 stub lookup depend on it. Registry

01:22 lookup depends on it. Debugging depends

01:24 on it. logging depends on it. So if COM

01:26 is a plumbing system, IIDs are stamped

01:29 part numbers on every valve, elbow, and

01:31 every adapter in the building. IIDs are

01:33 randomly generated and incorporate a

01:35 hash of your MAC address. And at 128

01:38 bits, they're functionally unique and

01:39 will never collide. Mathematically, it's

01:42 possible, but not likely to happen

01:44 before the proton decay of the universe.

01:46 And during my first months in the comm

01:48 team, I was trying to understand all of

01:49 this by doing what any sane new hire

01:51 would do back in those days when dropped

01:53 into a codebase of ancient machinery,

01:55 undocumented assumptions, and C++

01:57 written by people who clearly slept

01:59 under their desks a lot. So I single

02:01 stepped through it. I would sit there in

02:02 the debugger and ask innocent little

02:04 questions like, "What does co-initialize

02:06 ex?"

02:07 And then three hours later, I'd be 12

02:09 layers deep in apartment initialization,

02:11 TLS state, activation, plumbing, RPC

02:14 setup, and internal helper functions

02:15 with names that sounded like they've

02:17 been assigned by a committee after a

02:18 very long lunch. I even bought the book

02:21 inside Olay 2, which may be a very fine

02:23 book, but I'll admit something slightly

02:25 embarrassing. I was literally on the OA

02:27 comm team, and I don't think I truly

02:29 understood comm well until Don Box's

02:31 book came out a couple of years later.

02:33 And that's not a dig at anybody. Comm

02:35 was one of those technologies that

02:36 looked simple from orbit and then once

02:38 you got close, you realized the surface

02:40 was covered in trapped doors, rotating

02:42 knives, and small handwritten notes that

02:43 said things like, "We do this for 16-bit

02:45 compatibility." So, I learned the hard

02:47 way. I just followed the code. And the

02:50 more I followed it, the more I noticed

02:51 that everything eventually seemed to

02:52 turn into an IID, out of an IID, or into

02:55 a search for an IID. It's like being a

02:57 detective in a movie where every suspect

02:59 has the same last name for some reason.

03:01 Eventually, I found the function that

03:03 converted an iid to text. And as I

03:05 remember it, it was using the functional

03:07 equivalent of print f. Something like

03:09 take data 1, data 2, data 3, and the

03:11 eight bytes of data 4. Feed them through

03:13 a format string with percent 08x,

03:16 percent 04x, percent 02x, and so on. And

03:19 to be clear, that works. It's clean.

03:21 It's obvious. And it produces the right

03:23 answer. It's also a bit like using a

03:25 Swiss watch to hammer in a thumbtack.

03:27 Print f is magnificent because it's

03:29 general. It can format strings,

03:31 integers, floatingoint numbers, widths,

03:33 precision, padding, flags, signs,

03:36 alternate forms, left justification,

03:38 maybe localal sensitive details

03:40 depending on the implementation, and all

03:42 sorts of other things. It has to parse

03:44 the format string. It has to walk the

03:46 variable arguments, which means the

03:47 compiler can't type check it in the

03:49 normal way. It has to decide what

03:51 conversion you meant, how wide it should

03:52 be, how many characters to emit, and

03:54 where they should go. It's really a tiny

03:57 interpreter hiding in your C runtime.

03:59 And that's fantastic when you need a

04:01 tiny interpreter. But an iID string is

04:03 not a general formatting problem. It's a

04:05 16 byt to 32 hex digit problem with four

04:08 hyphens in fixed locations and maybe

04:10 braces depending on the convention.

04:12 There's no mystery. There's no

04:13 formatting language. There are no user

04:15 choices. There's not even any arithmetic

04:17 more complicated than take the high

04:18 nibble and end the low nibble. And you

04:20 already know that a bite is eight bits.

04:22 But some people have made it to

04:23 adulthood without actually noticing that

04:25 a single hex digit represents exactly

04:27 four bits. And that's why a bite is two

04:29 hex digits. One for the upper four bits

04:32 called a nibble and one for the lower

04:33 nibble. If you can learn to read

04:35 four-bit binary, you can actually

04:36 convert binary to 32-bit hex on the fly.

04:38 And it's a fun trick at certain cocktail

04:40 parties. Either way, the point is that

04:43 every bite becomes exactly two hex

04:45 characters. You take the top four bits

04:47 and you use them as an index into the

04:48 string zero through f. Write that

04:51 character. Then take the bottom four

04:52 bits and do the same thing. Do that 16

04:55 times and you have 32 hex digits. Put

04:57 the hyphens in at the correct places and

04:59 you've made a fully valid grid string.

05:01 And that's it. That's the whole magic

05:03 trick. But there's one little wrinkle

05:04 and it's the kind of wrinkle that

05:05 separates the I wrote some fast code

05:07 from the I wrote some fast code that

05:09 also works. A grid in memory is not

05:12 stored exactly the way it appears on the

05:13 screen. Unfortunately, at least not in

05:16 the little Indian machine like the x86

05:18 systems that we were mostly using. A

05:20 grid in memory is not stored exactly the

05:22 way it appears on the screen. at least

05:23 not on a little Indian machine like the

05:25 x86 systems that we were using. The grid

05:28 structure has a 32-bit data 1 field, two

05:31 16- bit fields called data 2 and data 3,

05:33 and then an 8bit data 4 array. When you

05:36 print data 1 as an integer, print f

05:38 naturally emits the number in canonical

05:40 human readable order. But if you simply

05:42 walk the bytes in memory from beginning

05:43 to end, data 1 would come out bite

05:45 reversed. Same with data 2 and data 3.

05:48 But data 4 is already bite by bite. So

05:51 the fast version can't just say dear

05:52 pointer please walk 16 bytes and tell me

05:54 what you see. That would produce a valid

05:57 looking lie which is the most dangerous

05:59 kind of lie in systems code. It has to

06:01 walk the bites in the right canonical

06:03 order on x86. That means rating the

06:06 bites in the order 3 2 1 0 for data 1

06:08 and then 54 for data 2 then 76 for data

06:12 3 and then 8 through 15 for data 4. And

06:15 once you have that order table the

06:17 conversion is brutally simple. Read a

06:19 bite, emit two hex characters, check

06:21 whether you've reached one of the hyphen

06:22 positions, and then keep going. Now,

06:25 somewhere out there, I can already hear

06:26 a viewer cracking their knuckles in the

06:28 comment section. Dave, this is premature

06:30 optimization. The root of all evil. Just

06:31 use the library. The compiler is smarter

06:33 than you. And besides, standard format

06:35 exists now. And congratulations. You've

06:37 made a good modern point from the

06:39 comfort of a machine that has more L1

06:41 cache than my dev box at the time had

06:43 for RAM. But this was not some random

06:45 dialog box code that ran once when the

06:47 user clicked about. This was comm. This

06:49 was core plumbing. This was code that

06:51 you might hit while initializing,

06:52 activating, registering, marshalling,

06:54 debugging, tracing, and generally trying

06:56 to make distributed objects behave like

06:58 local ones, which is already a polite

07:00 fiction requiring a lot of machinery.

07:02 Hot paths have a way of hiding inside

07:04 boring helper routines. And helper

07:06 routines are dangerous precisely because

07:08 everyone assumes they're too small to

07:09 matter. That's how performance dies. not

07:12 usually in one glorious bonfire, but by

07:14 a thousand tiny paper cuts, each one

07:16 defended by somebody saying, "Well,

07:17 surely this can't be the problem." And

07:19 so, one evening, I dialed in over Raz,

07:22 because this was the era when working

07:24 remotely meant that your modem made the

07:25 scream of an angry robot and then

07:27 connected you to the office at a speed

07:29 that today would make a smartwatch file

07:31 a workplace grievance. So, I was at home

07:33 connected over a phone line by modem,

07:35 rewriting a little iid string conversion

07:37 function because I was convinced that it

07:39 had been wasteful. And yes, a smarter

07:41 man might have instrumented it first. A

07:43 more disciplined engineer might have

07:44 written a benchmark, gathered traces,

07:46 measured call counts, and then presented

07:47 a tidy little table showing before and

07:49 after timings across representative

07:51 workloads. I did not do that. I just

07:54 looked at the print version, looked at

07:55 what the function was actually needing

07:57 to do, and thought, well, that can't

07:59 possibly be a fast way to do it. And

08:01 fortunately, in this case, youthful

08:02 arrogance and basic computer science

08:04 happened to be pointing in the same

08:05 direction. Now, the replacement code was

08:08 a basically a little nibble walker. It

08:10 treated the iid as bytes, but walked

08:12 them in the right order. For each bite,

08:14 it indexed into a static hex table

08:16 twice. Once for the upper nibble and

08:17 once for the lower nibble. It wrote the

08:19 characters directly into the output

08:20 buffer. And after the output index

08:22 reached the magic positions, it inserted

08:24 a hyphen. The hyphen part always

08:26 bothered me a little, though. The

08:28 canonical grid format has groups of

08:30 eight, four, four, four, and 12 hex

08:33 digits. So, the hyphens go after

08:34 character positions 8, 13, 18, and 23.

08:38 If you're counting the hyphens as

08:40 they're inserted. Well, my code did the

08:42 obvious thing that after writing each

08:44 pair of hex digits, it checks whether

08:45 the output index is one of those

08:47 positions. And if it is, it writes a

08:48 hyphen. And I never really love that. I

08:50 felt like there had to be a better way,

08:52 some elegant little branchless trick,

08:54 some mathematically satisfying answer

08:56 where the hyphens emerge naturally from

08:58 the topology of the grid like crystals

09:00 forming in a super saturated solution.

09:02 But at some point you have to remember

09:04 that you're not designing a cathedral.

09:05 You're converting an IID to a string. So

09:07 I shipped the obvious way. If you can

09:10 think of a faster way to do it, let me

09:11 know in the comments. Now thinking out

09:13 loud, if I were to do it today, I might

09:15 do it a little differently. I might

09:17 start with a template string full of

09:18 zeros and hyphens and then fill in only

09:20 the hex positions. Or I might use a

09:22 small table to output offsets. Or I

09:24 might unroll the whole thing because for

09:25 something this fixed, the most readable

09:27 code can sometimes be the one that

09:29 admits there is no real loop-shaped

09:31 problem here. But back then, the loop

09:33 was compact, correct, and much faster

09:35 than invoking the formatting machinery.

09:37 And when I say faster, I mean the

09:38 difference between hiring a moving

09:39 company and picking up the pencil by

09:41 yourself. Print f has to parse. My code

09:44 did not. Print f has to interpret a

09:46 miniature formatting language. And of

09:47 course, my code did not. Print f has to

09:50 handle all the cases, and my code had to

09:51 handle exactly one case. Print f

09:54 converts integers to text using general

09:56 purpose routines, but my code did two

09:58 table lookups per bite. And so Print F

10:00 is like a universal multi-tool, but my

10:02 version was more of a precision vera

10:04 screwdriver made for only one type of

10:06 screw. And that is the essence of good

10:08 optimization. Not making the general

10:10 case slightly more clever, but noticing

10:12 when the general case is using the wrong

10:14 tool entirely. Now, was it really 100

10:16 times faster? That's the number I

10:18 remember, but memory is sort of a

10:20 compression algorithm with a sense of

10:21 nostalgia. The exact factor is less

10:24 important than the shape of the result

10:25 because it wasn't 5% faster. It was not

10:28 the compiler did a little better with

10:29 the inlining case. It was a whole

10:31 different category of work. When you

10:33 replace a general formatter with fixed

10:35 stores and table lookups, you don't need

10:37 a PhD to predict the direction of

10:39 travel. But there's an important lesson

10:41 hiding in that because it's very easy to

10:42 take the wrong lesson from this story.

10:44 The lesson is not rewrite every print f

10:46 in your program by hand. Please don't.

10:48 That way lies madness, bugs, and a

10:50 future coworker quietly cursing your

10:52 name while trying to localize an error

10:53 message into finish. The lesson is that

10:56 generality has a cost and sometimes we

10:59 pay the cost in places where we don't

11:00 need the generality. Most of the time

11:03 that's fine. Most code is not hot. Most

11:05 code should be boring, obvious, and

11:07 maintained by somebody who has had a

11:08 reasonable amount of sleep. But when you

11:10 in a foundational layer and the

11:12 operation is fixed, tiny, and repeated

11:14 endlessly, it's worth asking whether the

11:17 fancy machinery is doing useful work or

11:18 merely wearing a little top hat while

11:20 wasting your cycles. Comm was full of

11:23 these lessons. It was a technology built

11:25 at the boundary between elegance and

11:27 punishment. On paper, query interface is

11:29 a beautiful idea. An object exposes

11:32 interfaces. A caller asks for an

11:33 interface by a unique ID. If the object

11:36 supports it, it returns a pointer. If

11:38 not, it returns an air. It's clean,

11:40 binary, language neutral, and insanely

11:42 powerful. In practice, that little dance

11:45 happens all over the place. It happens

11:46 across components, across process

11:48 boundaries, across departments, across

11:51 marshalling layers, and through code

11:52 paths where performance matters because

11:54 the user is waiting for an application

11:56 to start or a document to open or an

11:58 automation call to return before Excel

12:00 starts looking like it's gone out for

12:02 cigarettes. And every time you cross one

12:04 of those boundaries, the system has to

12:06 know what interface you mean. The IID is

12:08 that name tag. It is the passport. It's

12:10 the secret handshake. converting it to a

12:12 string might seem like administrative

12:14 trivia, but systems are made of

12:15 administrative trivia. That's where the

12:17 dragons live. There was also the small

12:19 worry in the back of my mind about

12:20 internationalization. Whenever you touch

12:22 string formatting inside of a platform

12:24 product, there's a tiny voice that asks

12:26 or should ask, "Am I accidentally

12:28 assuming something about language,

12:30 local, character set, or reading order,

12:32 and that's a good voice, and you should

12:34 listen to it." That voice prevents you

12:35 from shipping software that works

12:36 perfectly in a Redmond and then bursts

12:38 into flames somewhere else in the world.

12:40 But in this case, I don't think there

12:41 was a hidden international version of

12:43 awid string waiting to ambush me. Awid's

12:46 canonical representation is not pros.

12:48 It's not a sentence. It's not even

12:50 really a number being displayed for a

12:51 human in the normal cultural sense. It's

12:54 a protocol-shaped identifier made of asy

12:56 hex digits and fixed punctuation. If

12:58 IIDs are backwards in Arabic, as I used

13:00 to joke, then the printf version wasn't

13:02 accounting for that either. And nobody

13:04 really wants a globally unique

13:06 identifier that changes shape depending

13:08 on the user's local. Naturally, the code

13:10 went through rigorous review. And this

13:12 is where 20something me expected, if not

13:14 a parade, than at least some recognition

13:16 that I had found a hot little

13:17 inefficiency in the bowels of comm and

13:19 replaced it with something much leaner.

13:21 Perhaps a small statue, maybe just a

13:23 plaque. Here in this windowless office,

13:25 a young man saved millions of cycles and

13:27 briefly became insufferable. Instead,

13:29 the reaction was roughly, "Cool, nice

13:31 one." At the time, that felt

13:33 underwhelming. Later, I came to

13:35 understand that this was actually high

13:36 praise. In systems teams, especially

13:38 good ones, the highest compliment is

13:40 often that nobody has to talk about your

13:42 code very much. It just does the thing.

13:44 It's understandable. It does not create

13:46 a maintenance disaster. Doesn't require

13:48 a meeting. It just makes the product

13:50 better and disappears into the machine.

13:52 And that's the part young engineers

13:54 sometimes miss. The best systems work

13:56 often has no theatrical payoff. Nobody

13:58 sees the milliseconds you saved or the

14:00 allocation you avoided or the helper

14:02 function that no longer drags a

14:04 formatting engine into a hot path. users

14:07 just see the machine getting slightly

14:08 faster, smoother, and less irritating.

14:10 And they call that quality without

14:11 really knowing why. That invisible

14:13 quality is the whole game. It's also why

14:16 I'm skeptical when people talk about

14:17 performance like it's something you

14:19 sprinkle on at the end. Performance is

14:21 not paprika. You don't build a cathedral

14:23 load of wet cardboard and then make it

14:25 right in version two. Performance is the

14:27 habit of noticing. It's looking at code

14:29 that works perfectly and still asking,

14:31 "Why is this code doing so much?" It's

14:33 knowing when a library call is exactly

14:35 right and when it's hiding a bulldozer

14:36 behind the doororknob. And yes, you can

14:38 absolutely overdo it. There is a version

14:40 of this story, I suppose, where I spend

14:42 three days making IIID to string faster,

14:44 introduce a bite order bug, break half

14:46 the registry tooling, and become a

14:48 cautionary tale told to interns on

14:50 orientation day. Correctness comes

14:52 first. Readability matters. You don't

14:54 hand optimize code just because it makes

14:56 you feel like you're wearing a cape. But

14:58 sometimes the right optimization makes

14:59 the code more honest. The print that

15:01 version said this is a formatting

15:03 problem. But the nibble version said no

15:05 it's not. This is a fixed encoding

15:07 problem. And once you see the operation

15:09 clearly, the code almost writes itself.

15:11 And there's the other lesson. Don't just

15:13 read architecture documents.

15:14 Architecture documents tell you what the

15:16 system wishes it was. Debuggers tell you

15:19 what it actually is. Single step the

15:21 boring paths. Follow initialization.

15:23 Watch what happens before the first

15:25 window appears. That's how you learn the

15:27 real shape of a codebase. That's how I

15:29 started understanding Kong. Not by being

15:31 brilliant and not by already knowing

15:32 everything. I was there, yes, but mostly

15:35 I was there being confused in close

15:36 proximity to the source code, which is

15:38 still one of the best ways to learn

15:40 anything complicated. And every once in

15:42 a while, while wandering around with a

15:43 debugger and a modem connection, you

15:45 might find a little function doing way

15:46 too much work. You replace a general

15:48 purpose machine with a tiny

15:50 purpose-built one, save a pile of cycles

15:51 and get a cool good one. And 30 years

15:54 later realize that that was probably the

15:56 perfect ending because the machine got a

15:58 little better and that was the job. If

16:00 you've got comments or questions, leave

16:01 them with a question mark. We go

16:03 through, parse them all out, and answer

16:05 the best ones every Friday on Shop Talk.

16:07 I'll leave a link here so you can check

16:08 out an episode. Head on over there and

16:10 subscribe so we can get our little

16:11 cheesy plaque. It's the only plaque I'm

16:13 getting. If you found today's episode

16:15 interesting or entertaining, remember

16:17 that I'm mostly in this for the subs and

16:18 likes. So, I'd be honored if you would

16:20 consider leaving me one of each before

16:21 you go today. And if you're already

16:22 subscribed, thank you. In the meantime,

16:25 and in between time, I hope to see you

16:26 next time right here in Dave's Garage.

