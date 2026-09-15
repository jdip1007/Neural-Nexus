---
source_url: https://www.youtube.com/watch?v=OG91c7xsNMc
source_type: video
ingested: 2026-09-15
published: 2026-09-15
duration_minutes: 20
language: en
sha256: ad43ba62709387361693ab2ea27735210a4a29ba06e408be445efb01d9afe319
time_sensitive: True
---

# YouTube Transcript: The Challenge:  Can we build Notepad in 3K in assembly language?

## Video Information
- **Title**: The Challenge:  Can we build Notepad in 3K in assembly language?
- **Video ID**: OG91c7xsNMc
- **Published**: Unknown
- **Views**: Unknown
- **Language**: en

## Transcript
00:00 Are you sick of Windows getting just a

00:01 little fatter every single year? Tired

00:04 of apps that need an account, a cloud

00:05 sync, and 30 background services just

00:07 open a damn text file? Well, grab a seat

00:10 because today I'm actually doing

00:11 something about it. I'm talking about

00:13 the ultimate poster child for Windows

00:15 bloat. That redheaded stepchild of

00:17 desktop utilities, Notepad. You see,

00:20 back in the '90s at Microsoft, we had

00:22 some clear rules. Notepad was for plain

00:24 text. Wordpad was for RTF. And we were

00:26 taught how important it was to never

00:28 cross the streams. So, Notepad stayed

00:30 lean. Wordpad got the fancy fonts, the

00:33 colors, the spell check, and for all I

00:35 know, a recipe card file feature. I

00:37 don't actually know. I don't want to

00:38 know. I never used it. And I'm not

00:40 looking to add yet another editor to my

00:42 repertoire at this point. I just want to

00:44 tweak in any file without logging into a

00:46 Microsoft account, downloading a bunch

00:48 of DLS, and watching a 12-minute YouTube

00:50 tutorial on how to use the new Notepad.

00:52 I don't really want Copilot involved at

00:54 all. Now, that original notepad, it was

00:57 born exactly for this job. Small,

00:59 lightning fast, dead simple. So, today I

01:02 rebuilt it from scratch. 2.5 kilobytes.

01:05 No bloat, no telemetry, no nonsense.

01:08 Just pure old school Windows done right.

01:10 Let's dive in and see how it's done.

01:13 Notepad was created for simply editing

01:15 text. Small, lightweight, fast, easy to

01:17 load, easy to understand, no superolous

01:19 features. But something changed over

01:21 time. Maybe spellch check was the nose

01:23 of the camel. I'm not sure, but

01:25 somewhere at some time people started

01:27 adding features to Notepad and pretty

01:29 soon you wind up with Copilot addresses

01:30 a paperclipip asking if you need help

01:32 writing your document. But if Notepad

01:34 was the canary in the coal mine that

01:36 signaled our descent into mediocrity,

01:38 then what's the antidote? Well, of

01:40 course, the answer is to start by fixing

01:41 Notepad. So that's exactly what we're

01:43 going to do today. The program I'm going

01:45 to show you today opens files, saves

01:47 files, edits them, prints, searches,

01:49 replaces, wraps text, changes fonts,

01:52 tracks your line and column, gives you

01:54 line numbers, a right-click menu, and

01:55 asks politely before throwing away

01:57 unsaved work. In other words, it behaves

01:59 exactly like you might remember Notepad

02:01 Circa Windows XP, except this whole

02:04 program is 2,686

02:06 bytes, not kilobytes with a few zeros

02:08 missing. not a compressed installer and

02:10 not a bootstrapper that downloads the

02:12 real program after you look away. 2,686

02:16 bytes. The thumbnail for this episode is

02:18 almost certainly larger than the

02:20 application, which means the marketing

02:21 department has officially become the

02:23 bloatware. And today we're going to

02:24 answer the obvious question, which is

02:26 not merely how is that possible. The

02:28 more interesting question is what does

02:30 Windows already contain that lets a

02:31 program that small behave like a real

02:33 application? Because the answer is

02:35 hiding in plain sight. and it says

02:36 something surprisingly important about

02:38 native software operating systems design

02:40 and why modern applications sometimes

02:42 feel like they arrive towing a circus

02:44 caravan. A while back I did an episode

02:47 on building a tiny Windows program. Not

02:49 just the process that returns zero or

02:51 popped up a message box, but a real

02:53 graphical Windows app. That meant

02:54 dealing with the PE header, the import

02:57 table, section alignment, the old MZ

02:59 executable stub, and all the little bits

03:01 of ceremony that Windows requires that

03:03 you get right before your code even gets

03:05 a chance to say hello. This was already

03:07 a fun of rabbit hole to go down because

03:09 once you stop accepting the default

03:11 linker output as a law of physics, you

03:13 discover that a Windows executable has a

03:15 lot more negotiable real estate than you

03:17 might expect. The community naturally

03:19 saw a tiny program and decided that it

03:21 was still offensively large because it

03:22 was like 4K at the time. That led even

03:25 smaller experiments and eventually

03:26 Matthew Power took the idea in a more

03:28 interesting direction. Rather than

03:30 simply proving that a tiny Windows app

03:32 could be built, he built a tiny text

03:34 editor. The first version used the

03:35 standard Windows edit control which

03:37 already gives you a remarkable amount of

03:38 text editing functionality for free.

03:40 Then he moved it over to Richedit and

03:42 that changed the whole character of the

03:44 project. Suddenly it wasn't just a stunt

03:45 anymore. It was the beginning of

03:47 something that could actually behave

03:48 like actual software. And that's where a

03:50 dangerous thought entered the room.

03:52 Could you build something like classic

03:53 Notepad feature for feature and still

03:56 keep it under 4K? Cuz 4 kilobytes is one

03:58 of those wonderfully arbitrary limits

04:00 that becomes meaningful because

04:01 generations of programmers have used it

04:03 as a dare. The demo scene has produced

04:06 entire worlds, music, graphics,

04:08 procedural animation, and small miracles

04:10 inside 4,096 bytes. It is not a sensible

04:13 application budget. It's a programming

04:15 cage match. And cage matches teach you

04:17 something that polite software projects

04:19 never will. So the goal became simple.

04:22 Build a new notepad for Windows.

04:24 Implement all of the normal features

04:25 that people expect. You get open, save,

04:27 save as, cut, copy, paste, undo, find,

04:30 replace, word, time and date, fonts,

04:33 printing, status bars, rightclick menu,

04:35 and the unsaved changes prompt. Then get

04:37 the whole thing under 4K. And the trick,

04:39 of course, is not to write all of

04:41 Notepad. Now, this is going to sound

04:43 like cheating, but it's actually the key

04:45 lesson because Windows already contains

04:46 most of what we think of as a Windows

04:48 application. It has a Windows manager.

04:50 It has menus. We're not going to go off

04:52 and write the code to draw the menu

04:54 background and the lines on the menu and

04:55 all that. It has common dialogues. It

04:57 has clipboard handling. It has edit

04:59 controls. It already has font selection.

05:01 It has file open and save dialogues. And

05:03 it has some printing infrastructure. It

05:05 has a message pump. It has decades of

05:07 accumulated plumbing sitting there

05:09 waiting for a plumber like me to come

05:10 along and hook up the pipes and build

05:12 some kind of useful machine out of it. A

05:14 tiny native Windows program does not

05:15 bring along its own entire civilization.

05:18 It arrives with a lunchbox and a map of

05:20 the city. Somehow it seems modern

05:22 software manages to go the other way.

05:23 You just want a text box and then

05:25 somehow you've imported a runtime, a

05:27 layout engine, a renderer, dependency

05:29 tree, a telemetry client, an auto

05:31 updater, and a small portion of

05:32 Chromium. And by the time the app even

05:34 opens a blank document, it already has

05:36 the gravitational field of a minor

05:38 planet. But this project is the

05:39 opposite. It asks, "What's the smallest

05:41 amount of application specific glue that

05:43 you can write if you lean on windows as

05:45 hard as possible?" And when you do that,

05:48 the answer gets weird quickly. Is the

05:50 first thing you learn at this scale is

05:51 that strings are expensive. In a normal

05:53 program, nobody thinks twice about

05:54 adding a menu item called save as

05:56 because the text is just the text. But

05:58 in a 4K program, English becomes bloat.

06:01 Every character costs, every null

06:03 terminator costs, every command ID

06:05 costs, every bit of routing logic costs

06:08 something. The user interface is no

06:10 longer decoration. It's payload. If you

06:12 look at the ROM for an old game like

06:13 Tempest from Atari, which was written in

06:15 1979ish in 6502 assembly language, you

06:19 see tricks that prove that every bite

06:20 was sacred. Like they didn't use null

06:22 terminators at the end of strings.

06:24 Instead, they just set the high bit of

06:25 the last letter as the indicator

06:27 instead, saving one bite per string on

06:29 every string within the game. Basically,

06:32 we add features one at a time, build,

06:34 measure, and see what sacrifice the bite

06:37 gods demand to entertain that particular

06:38 feature. So, for example, adding the

06:41 file menu brought the executable to

06:42 1,375

06:44 bytes. In any normal context, that

06:46 number is microscopic. But when the

06:48 entire target is 4,96 bytes, you feel

06:51 like every addition is packing for your

06:52 vacation using only the pockets in your

06:54 genes. Then came the edit menu and that

06:57 only took it out to about 1428 bytes

06:59 because most of the edit operations are

07:00 just sending messages to the richedit

07:03 control. Cut, copy, paste, undo, delete,

07:06 select all. Windows already knows how to

07:07 do all those. The tiny editor mostly has

07:10 to connect the right menu items to the

07:11 right messages and then get out of the

07:13 way. Adding open and save as took it out

07:15 to 1517 bytes. Help took it out to 1557

07:19 bytes, which proves that help is cheap,

07:21 at least in executable form. But the

07:23 moment it started to feel like a real

07:24 application was the unsaved work prompt,

07:27 a text editor that lets you type for 20

07:29 minutes and then close the window

07:30 without any warning. That's not a text

07:32 editor. That's a data loss appliance

07:33 with a cursor. So the program needed to

07:36 know when the document was dirty,

07:37 intercept any close operations, ask the

07:40 user whether to save, discard or cancel,

07:41 and then do the right thing. Properly

07:44 tracking all that moved this out to 1622

07:46 bytes. And that is a philosophical

07:48 upgrade, not just a feature because it

07:51 means the program now understands one of

07:52 the most important contracts between

07:54 software and humans. Please don't

07:55 casually destroy my work. It's like

07:57 we're a real tool now, in fact. So time

08:00 and date came next. That's the little

08:02 Notepad feature where you press F5 and

08:03 it inserts the current time and date.

08:05 Nobody buys a computer for that feature,

08:07 but if you're chasing Notepad

08:08 compatibility one for one, somebody will

08:10 absolutely notice it when it's missing.

08:12 Querying the system clock and adding the

08:14 insertability brought the size up to

08:16 1668 bytes. Now, WordPok out to 1694.

08:20 Can't forget about WordP.

08:24 You're adding six bytes at a time here

08:26 and there, and you think, well, this is

08:27 easy. And that's when computers

08:29 traditionally punish you. The

08:31 right-click menu came next. In a text

08:33 editor, the context menu is one of those

08:34 features that users don't celebrate when

08:36 it works, but they instantly notice when

08:38 it's not there. Right click in an editor

08:40 and your fingers expect undo, cut, copy,

08:43 paste, delete, and select all. So, in it

08:45 went, and the executable reached 1779

08:48 bytes, still under 2K. And at this

08:50 point, we had a real editor with real

08:52 menus, real file operations, dirty state

08:55 handling, word wrap, time date, and a

08:57 context menu. But the dangerous features

08:59 were still waiting in the tall grass.

09:01 Fonts, find and replace, printing, and

09:03 the status bar. Now, the font picker

09:05 could have been a disaster because

09:06 writing a font dialogue from scratch is

09:08 not something you do in a 4K executable

09:10 unless you've made a serious mistake in

09:12 your life somewhere. It has to enumerate

09:14 all the fonts, show the sizes, the

09:16 styles, probably have a preview, device

09:18 context, and all the oddities that

09:20 accumulate when a graphical operating

09:21 system has been carrying compatibility

09:22 baggage since about the Jurassic period.

09:25 So, we don't write our own font picker.

09:27 We just call the one that Windows

09:28 already has. And that's the entire story

09:30 of this program. Don't implement the

09:31 world. Borrow the world. Hook up the

09:33 world. Create the plumbing. Make the

09:35 infrastructure work for you. The tiny

09:37 editor prepares the structure that

09:38 Windows expects, calls the common font

09:41 dialogue, lets the operating system

09:42 handle the UI, receives back the

09:44 results, creates or replies the font,

09:46 and goes back to minding its own

09:48 business. And the size lands in at 1910

09:50 bytes. So, we're still under 2K for a

09:53 graphical Windows text editor with

09:54 native font dialogue. Somewhere a modern

09:56 settings page just allocated more memory

09:58 than that to animate their toggle

09:59 switch. Then came find and replace which

10:02 I expected to hurt a bit. Find is not

10:04 just a menu item. It has state. It has a

10:06 search string. It has current selection.

10:08 It has find next which means the program

10:09 has to remember what you were looking

10:10 for the first time. Replace has even

10:13 more behavior and users have decades of

10:15 muscle memory telling them exactly how

10:16 it should feel. So find, find, next, and

10:19 replace push the executable up to 2,143

10:22 bytes. That was one of those numbers

10:24 where you stare at the file size for a

10:25 moment because it seems like the tools

10:27 must be lying, but they weren't. A 2Kish

10:29 program now has Real Search and Real

10:31 Replace. And then came printing.

10:33 Printing in Windows is kind of spooky.

10:35 It's one of those subsystems that feels

10:37 like you're opening a hatch in the floor

10:38 and you discover a second older

10:40 operating system living underneath.

10:41 There are printer dialogues, device

10:43 context, start dock, start page, end

10:45 doc, end page, fonts, margins, mapping

10:49 modes, and high metrics, and some code

10:51 path somewhere that still remembers a

10:52 laser jet 4 with unresolved emotional

10:54 needs.

10:56 But Notepad prints, so the tiny editor

10:58 had to print. Printing alone brought the

11:00 executable up to 2476 bytes. Now, that's

11:02 a large jump by our tiny app standards,

11:04 but still ridiculous in absolute terms.

11:06 a 2.5K executable that can display a

11:09 text editor, save a file, search text,

11:11 choose fonts, print, replace, and it's

11:13 exactly the kind of thing that makes you

11:14 question what all your other software is

11:16 doing all day. Then I added the status

11:18 bar with a line in the column. And the

11:20 funny thing is, after adding it, the

11:21 file size was still 2,476

11:24 bytes. That doesn't mean the feature

11:26 cost literally nothing. It means the

11:28 final compressed executable did not grow

11:30 from it. And that's when you learn that

11:32 at this size, you're no longer writing

11:33 mere code. you're negotiating with a

11:35 compression goblin. The tool we use

11:37 here, Crinkler, is a compression linker

11:39 famous in the 4K demo world. It doesn't

11:42 just link your program. It also squeezes

11:44 it, rearranges it, compresses it, and

11:46 generally treats your executable like a

11:47 suitcase being sat on by a fat man on a

11:49 hotel bed. And because the final metric

11:52 is actual compressed size, your

11:53 intuition can fail in hilarious ways.

11:56 Sometimes you add code and the file

11:57 doesn't grow. Sometimes you remove code

11:59 and the file gets bigger. Sometimes the

12:01 clean, elegant version that you write

12:02 because it's so much better is worse

12:04 than the ugly copypaste repeated

12:06 version. And that last part is the one

12:08 that offends me the most as a

12:09 programmer. We're taught not to repeat

12:11 ourselves. And in normal software,

12:13 that's excellent advice. Duplication is

12:15 where bugs breed. Abstraction gives you

12:17 structure. Tables and helper functions

12:19 and clean dispatch logic made code

12:21 easier to understand, easier to

12:22 maintain, and easier to extend. But in a

12:25 4K compressed executable, compression

12:27 loves repetition. If you repeat a small

12:29 code pattern several times, the

12:31 compressor may encode that repeated

12:32 pattern very efficiently. If you replace

12:34 it with a clever tabledriven system, now

12:36 you need the table, you need the

12:38 dispatcher, you need the offsets, the

12:39 indexes, the branches, and a little

12:41 machine that describes your cleverness

12:42 to the computer. Now, this is not a

12:44 general lesson for production software.

12:46 Please do not go to work tomorrow and

12:47 say that you were watching Dave's garage

12:49 and he said that copy paste is the cool

12:51 new architecture. Dave didn't say any

12:53 such thing. Dave is doing a science

12:54 experiment with a bite budget and a

12:56 sharp object. But it's a beautiful

12:58 reminder that good code is not a

13:00 universal constant. Good code serves its

13:02 constraints. If the constraint is

13:04 maintainability, then duplication loses.

13:06 If the constraint is clarity,

13:08 duplication again usually loses. But if

13:11 the constraint is the smallest

13:12 compressed executable, duplication might

13:14 win and everybody involved will feel

13:15 slightly dirty afterwards. I used to say

13:18 it was code that made me want to run

13:19 home and take a shower. And the final

13:21 result with everything in and working

13:22 was 2,686

13:24 bytes. 2,686

13:27 bytes. Under 3K, well under the 4K

13:29 target. A working Notepad like editor

13:32 with open, save, print, find, replace,

13:34 font selection, word wrap, time and

13:36 date, status bar, context menu, and

13:39 unsave change prompting. Now, the

13:41 obvious objection here is that this is

13:42 not really Notepad because Windows and

13:44 Richedit are doing the hard work. Well,

13:46 yes, exactly. That's the point. That's

13:48 how the real Notepad works, too. This is

13:50 not an episode about writing a text

13:52 layout engine from scratch. It's not

13:54 about implementing selection or

13:55 scrolling or cursor movement or IME

13:57 behavior, clipboard formats, file

13:59 dialogues, font enumeration, and printer

14:01 support by hand in 2.7K. That would be a

14:04 different episode, possibly flown from

14:05 inside a padded room because surprise,

14:07 this is actually an episode about how

14:09 small the application specific part can

14:11 be when the platform provides the

14:13 platform. And that distinction matters.

14:15 A native Windows application is not a

14:17 sealed shipping container. It is a

14:19 conversation with the operating system.

14:21 Create a window. Give me a rich edit

14:22 control. Show this menu. Open the file

14:24 dialogue. Let the user pick a font. Send

14:27 this text to the printer. Tell me when

14:28 the user clicks on this command. Windows

14:30 does all the heavy lifting and your

14:32 executable provides the intent. And the

14:34 tiny editor is small because Windows is

14:36 enormous. And for once, that enormity is

14:37 of an advantage. There is a kind of

14:39 software design lesson hiding here. We

14:41 sometimes talk about operating systems

14:43 as though they are just bootloadaders

14:44 for browsers and app frameworks. But a

14:46 mature OS is also a giant library of

14:48 already solved problems. Some of those

14:50 solve problems are old, weird, and named

14:52 like they were invented during a bar

14:53 fight over Hungarian notation, but they

14:55 work. Menus work, dialogues work,

14:58 controls work, the clipboard works,

14:59 printing mostly works, which is as close

15:01 as printing ever gets to a compliment.

15:03 Compatibility is not glamorous, but it

15:05 is powerful. The rich edit control

15:07 exists because decades of applications

15:09 needed serious text editing. Common

15:11 dialogues exist because pretty much

15:13 everybody needed open, save, print, and

15:15 font. The message pump exists because

15:17 Windows applications have been living in

15:19 that event-driven world since before

15:20 some of today's frameworks were even a

15:22 bad idea in somebody's graph paper

15:23 notebook. And because that machinery is

15:26 already installed on the machine, a tiny

15:28 executable can call into it and appear

15:29 to perform miracles. But it is not

15:31 magic. It's leverage. That is also why

15:34 the old tiny Windows program work

15:35 mattered. Real software needs

15:37 maintainability, test, diagnostics,

15:39 accessibility, localization,

15:41 security hardening, and code that future

15:43 humans could read without a hex editor

15:45 in a bottle of Tylenol. But as a

15:47 learning exercise, this is awesome. It

15:49 teaches you that every bite has weight.

15:51 It teaches you that strings are data and

15:52 data cost space. It teaches you that

15:54 abstractions have mass. It teaches you

15:57 that executable format matters. It

15:59 teaches you that the operating system is

16:00 part of your application. And it teaches

16:02 you to measure instead of guessing. And

16:04 of course, it teaches you that sometimes

16:06 the compressor has terrible taste and

16:07 rewards code that you would never admit

16:09 to writing in a design review. But most

16:11 of all, it reminds you that constraints

16:12 are not just limitations. They are the

16:14 microscope. When you have infinite

16:16 space, you can hide sloppy thinking

16:18 under another layer. But if you only

16:20 have 4,96 bytes, there is nowhere to

16:22 hide. Every menu item, every branch,

16:24 every string, every API call, every data

16:27 structure has to justify its existence.

16:29 And that kind of pressure creates

16:30 clarity or at least very compact

16:32 madness. But seriously, going through

16:34 all the code, you start to learn what

16:36 costs space. And you know, it's only a

16:38 few here and a few bites there. But when

16:39 you multiply that by thousands of

16:41 functions, you can see the type of thing

16:42 that grows into bloat if you're not

16:44 careful. And it makes old windows feel

16:46 fresh again when it's not there. Now, I

16:48 get it. Win32 is not fashionable. It's

16:50 not sleek. It has rough edges,

16:51 historical scars, and APIs whose names

16:53 sometimes appear to have been generated

16:55 by shaking scrabble tiles out of a big

16:56 filing cabinet. But it has one

16:58 magnificent property. It keeps working.

17:00 A small native program can still show up

17:02 decades later and plug into the same

17:04 operating system machinery that

17:05 countless applications have used before

17:07 it. That is the quiet superpower of

17:09 compatibility. So when I look at this

17:11 2.7K text editor, I don't just see the

17:13 stunt. I see a demonstration of what a

17:16 platform really is. A platform is not

17:18 just somewhere your code runs. A

17:20 platform is the accumulated set of

17:22 services that mean your code does not

17:23 have to solve every problem on its own.

17:25 This tiny executable says I need a text

17:28 editor surface and Windows provides one.

17:30 Says I need a file picker and Windows

17:32 provides one. It says I need to print

17:34 and Windows opens the ancient mechanical

17:35 door under the floorboards and provides

17:37 that too. And so the program is small

17:39 because it is not carrying what the

17:41 platform already has. And that is a

17:43 lesson that modern software could stand

17:45 to remember. Not every app needs to

17:47 bundle the universe. Not every utility

17:49 needs to ship with a browser engine. Not

17:51 every simple tool needs an update demon,

17:53 a telemetry pipeline, a sync service,

17:55 and a login flow before it lets you type

17:57 something into a box. Sometimes the

17:59 sharpest software is a software that

18:01 trusts the operating system, respects

18:02 the machine, and gets out of the way.

18:04 Now, will the community make this even

18:06 smaller? Almost certainly, and there's

18:08 not much room left, but somebody will

18:10 replace a reasonable instruction

18:12 sequence with something that appears to

18:13 have escaped from a crashed UFO.

18:15 Somebody will discover that adding a

18:16 feature somehow reduces the compressed

18:18 file size just to insult causality. And

18:21 somebody else will complain that it

18:22 doesn't count because Richedit does the

18:24 hard work. And that person may have a

18:25 technical point, but they're missing the

18:27 fun. The challenge is not to build a

18:29 text editor in a vacuum. The challenge

18:31 is to build the smallest useful native

18:33 Windows text editor by using Windows as

18:35 Windows. And that is not cheating. That

18:37 is the platform doing its job. So the

18:39 final number is 2,686 bytes. I mean, you

18:42 got no pad and less space than your

18:44 average website cookie. It saves, it

18:46 opens, it searches, it prints, it

18:48 replaces, it wraps, it changes fonts, it

18:50 tracks line and column. It protects your

18:52 unsaved work. And it does all of that by

18:54 standing on the shoulders of an

18:55 operating system that has been quietly

18:56 accumulating useful machinery for

18:58 decades. When I started thinking about

19:00 this project, I thought the story was

19:01 going to be, can we fit Notepad in under

19:03 4K? But the better story is this.

19:05 Windows already contains most of

19:07 Notepad. the tiny program is just the

19:09 smallest possible set of instructions

19:11 needed to ask for it in a very specific

19:13 way and that's kind of more interesting

19:15 and so it's kind of useless but in the

19:17 most educational possible way which is

19:19 one of my favorite categories of

19:20 computing. Nobody needs a 2.7K text

19:23 editor for Windows. Your SSD will

19:25 survive if your editor is even twice the

19:27 size. But pushing a ridiculous

19:29 constraint to its limit, we learned

19:31 something about software, about

19:32 platforms, about compression and

19:34 executable formats, and the difference

19:35 between implementing functionality and

19:37 orchestrating functionality that already

19:39 exists. And it gave me a chance to say

19:41 that the thumbnail is bigger than the

19:42 program itself, and I'm not mature

19:44 enough to pass that one up. If you have

19:46 comments, questions, or feedback about

19:47 this episode, please leave it in the

19:49 video comments. Every week on Friday,

19:51 Glenn and I host shop talk, where we go

19:52 through and answer all of the week's

19:54 best questions. And it's probably better

19:55 if you use a question mark on your

19:57 question instead of a period if it's a

19:58 statement because then I see it because

19:59 I'm looking for question marks. Now you

20:01 know if you found today's episode

20:02 interesting or entertaining, remember I

20:04 mostly end this for the subs and likes.

20:05 So I'd be honored if you would consider

20:07 leaving me one of each before you go

20:08 today. In the meantime, and in between

20:10 time, hope to see you next time right

20:11 here in Dave's garage.

