---
source_url: https://www.youtube.com/watch?v=jH0BYAkPj78
source_type: video
ingested: 2026-09-15
published: 2026-09-15
duration_minutes: 18
language: en
sha256: 068626144b882a92dc19ee14727a15dc319c984496b1a6810e6c8d9f8989569d
time_sensitive: True
---

# YouTube Transcript: Microsoft's Secret 90s Weapon That Made Windows Fast

## Video Information
- **Title**: Microsoft's Secret 90s Weapon That Made Windows Fast
- **Video ID**: jH0BYAkPj78
- **Published**: Unknown
- **Views**: Unknown
- **Language**: en

## Transcript
00:00 Hey, I'm Dave. Welcome to my shop. I'm

00:03 Dave Plamer, retired operating systems

00:04 engineer from Microsoft, going back to

00:06 the MS DOS and Windows 95 days. And

00:08 today I want to tell you about one of

00:10 the strangest and most secret

00:11 optimizations that we ever used at

00:13 Microsoft. because it happened after the

00:15 compiler was done, after the linker was

00:17 done, and after the exe or DLL already

00:19 existed, and in many cases, after the

00:22 developers themselves thought the build

00:23 was finished, and then in the middle of

00:25 the night, some secret internal tool

00:27 would quietly take the binary apart,

00:29 rearrange its organs, sew it back

00:31 together, and ship something faster,

00:33 smaller, and more memory efficient than

00:34 the program that we had actually

00:36 written. And the best part is that

00:38 nobody outside of Microsoft knew it was

00:40 happening. It's been almost 30 years,

00:42 but it's time to tell you about it. The

00:44 tool was called BBT, usually expanded as

00:47 binary basic block tools, but you may

00:49 also hear it referred to by our

00:50 wonderfully appropriate internal

00:52 nickname of Lego. Public documentation

00:54 is pretty thin because this was an

00:56 internal Microsoft tool chain from an

00:58 era when a lot of the interesting build

00:59 magic lived behind the curtain. And

01:02 whether or not it's still enforceable, I

01:04 still respect the intent of my original

01:05 NDA. And so I can't and won't tell you

01:08 stuff that isn't public yet, even all

01:09 these years later. But we do have enough

01:11 public breadcrumbs to understand the

01:13 shape of it. A Microsoft research

01:15 retrospective notes that BBT optimized

01:17 the working set size. Microsoft's

01:20 current profileg guided optimization

01:21 documentation still describes basic

01:23 block optimization in very similar

01:25 terms, placing commonly executed basic

01:28 blocks into the same set of pages to

01:30 improve locality and reduce memory

01:32 overhead. And that little phrase, same

01:34 set of pages, is this whole episode

01:36 hiding in plain sight. Because if you

01:38 remember Windows NT4 or Windows 95 or

01:41 Office from that era, you remember a

01:43 world where memory was not merely some

01:44 abstract number in Task Manager. Memory

01:47 was the weather. Memory decided whether

01:49 your machine felt crisp or whether it

01:50 went off into a swap file coma, grinding

01:53 the disc like a raccoon trapped in a

01:54 coffee can. My first NTE dev machine,

01:57 believe it or not, only had 12 megabytes

01:59 of RAM. So that was a real target. 32

02:02 megs was luxurious. 64 megs was the kind

02:04 of thing you bragged about at lunch

02:05 before people stopped inviting you to

02:07 their parties. So, Microsoft had a very

02:09 practical problem. Windows was getting

02:11 bigger. Office was getting bigger. SQL

02:14 Server was getting bigger. The code was

02:15 more capable, more modular, and more

02:17 layered, but the hardware underneath was

02:19 still brutally finite. You could write

02:21 better algorithms and you could tune the

02:23 compiler and you could beg teams not to

02:25 add one more feature before RTM. But at

02:27 some point the binary itself became the

02:29 problem. Not the source code, the

02:32 binary. And that's where BBT comes in. A

02:35 normal compiler works mostly in the

02:36 world of source code. It sees functions,

02:39 loops, branches, local variables,

02:41 calling conventions, and maybe with

02:42 enough optimizations enabled, it can see

02:44 across several functions or compilation

02:46 units. Then the linker glues together

02:49 object files and libraries into the

02:50 final executable image. And that final

02:53 layout is pretty reasonable from the

02:54 perspective of the build system. Code

02:56 from this object file goes here. Code

02:58 from that object file goes there. Code

03:01 from the library goes there. Alignment

03:03 padding gets inserted. Import tables are

03:05 built. Debug records are attached. And

03:07 the whole thing becomes a valid portable

03:09 executable file. But valid is not the

03:11 same as laid out in the way that the CPU

03:13 actually wants to eat it. The CPU does

03:15 not execute your class hierarchy, does

03:17 not care about your project structure,

03:19 it does not care that the login dialogue

03:21 and the air handler and the happy path

03:23 loop all lived in the same source file

03:25 because that was a convenient way to do

03:26 it back in 1993. The CPU just sees

03:29 bytes. It fetches those bytes through

03:31 instruction cache lines. It maps pages

03:34 through the instruction TLB. It tries to

03:36 predict branches. It speculatively

03:38 charges down paths that may or may not

03:40 be right. And if the code it needs next

03:42 is somewhere else or on another cache

03:44 line or worse on another memory page

03:46 that is not resident then everything

03:48 stalls. And that is where working set

03:50 becomes the villain of this story. The

03:52 working set of a process is roughly the

03:54 set of memory pages that it needs to

03:56 keep resonant in RAM to run smoothly. If

03:58 your program has 10 megabytes of code,

04:00 but the common startup path only needs

04:02 300 kilobytes of it, then in a perfect

04:04 world, the operating system should only

04:06 need to bring in those 300 kilobytes.

04:08 But if those 300 kilobytes are sprinkled

04:10 like parmesan across 10 megabytes of

04:12 binary, then the loader and the memory

04:14 manager have to touch far more pages

04:16 than the actual executed code would

04:18 suggest. And that's the key point.

04:20 Imagine a library where there are five

04:22 books you need, but they're not sitting

04:23 together on one shelf, but rather each

04:25 chapter of each book has been shelved

04:27 randomly throughout the building. You

04:29 can still read the books. The

04:30 information is all still there, but you

04:32 spend most of your entire afternoon

04:33 walking around the stacks instead of

04:35 reading. That's bad enough if the

04:37 library is in RAM, but it's catastrophic

04:39 if every trip to the shelf means the

04:40 disc drive has to wake up and go

04:42 hunting. Now, BBT's core idea was simple

04:45 and ruthless. Use real execution data to

04:48 find the code that actually runs

04:50 together. Then move that code around so

04:52 it also lives together, not in the

04:54 source tree, but in the binary. To

04:56 understand LEGO, we need to know what a

04:58 basic block of code is. A basic block is

05:01 a straight line run of machine

05:02 instructions with one entry and one

05:04 exit. No jumps into the middle of it and

05:06 once execution starts at the top, it

05:08 continues until it hits a branch, a

05:10 return, a call boundary, or some other

05:12 control flow event. Compilers already

05:14 think in terms of basic blocks. But BBT

05:17 did something especially interesting

05:18 because it operated after linking. It

05:21 looked at the finished executable and

05:22 treated those basic blocks like little

05:24 bricks. And that's why the Lego name

05:26 came about and why it's so perfect, if

05:28 you know, completely legal because of

05:29 trademarks and so on. The compiler hands

05:32 you a completed model. BBT then says,

05:34 "Hey, that's a nice spaceship."

05:35 Unfortunately, the cockpit's on page 12,

05:37 and the engine controls are on page 47,

05:39 and the landing gear is mixed in with

05:40 the cafeteria, so I'm going to fix all

05:42 that for you. Now, the rough pipeline

05:44 went something like this. You build the

05:46 program normally, even with VS Code or

05:48 whatever you want, back then be Visual

05:49 Studio, but we use command line tools,

05:52 but with enough symbol relocation and

05:54 debug information that the tool can

05:56 understand what it's going to be looking

05:57 at. Then, BBT analyzes the binary and

06:00 identifies functions and basic blocks.

06:03 It either instruments the binary or

06:04 consumes profile information from

06:06 representative runs. Those profiles tell

06:09 it which blocks of code ran, how often

06:11 they ran, and which branches were

06:13 commonly taken. Then it rebuilds the

06:15 layout of the executable so that the hot

06:17 paths are packed together and the cold

06:19 paths are all pushed away. And the word

06:21 representative there is doing a lot of

06:22 work. If you train the optimizer by

06:25 launching Word, opening a document,

06:26 printing it, and exiting it, then Word

06:28 gets optimized for that scenario. But if

06:30 you train for running obscure mail merge

06:32 edge cases and try to do all these

06:34 coverage cases and invoke a printer

06:35 diver from another planet, then you may

06:37 have optimized for nothing or the wrong

06:39 thing entirely. Profileg guided

06:41 optimization is only as good as the

06:43 profile. It can be the software

06:44 equivalent of training for a marathon by

06:46 running to the refrigerator. Technically

06:48 exercise, but the wrong workload. But

06:51 Microsoft had something that most

06:52 companies did not. Massive test farms,

06:55 repeatable scenario tests, and enormous

06:57 incentive to shave memory use and

06:58 startup time from software used by

07:00 millions of machines. The small

07:02 improvement multiplied across Windows

07:04 and Office was not small. It was a

07:06 planetary event. Now, why did this

07:08 matter so much for NT4? NT was a serious

07:11 operating system. It had a real kernel,

07:13 a real security model, preemptive

07:14 multitasking, protected memory, Unicode

07:16 deep in its bones, and a design lineage

07:18 that owed more to serious workstation

07:20 operating systems than to MS DOS. But

07:22 all that sophistication cost memory. NT4

07:26 could run on machines that by all modern

07:28 standards just had pocket lid for RAM.

07:30 The operating system had to feel

07:31 responsive while sharing memory with

07:33 drivers, services, the shell, GDI, user

07:36 apps, file cache, networking, and

07:38 whatever enterprise software your

07:40 company inflicted on you because someone

07:41 in procurement owned a tie. The problem

07:44 was not merely how many bytes existed in

07:46 the binary. The problem was how many

07:47 pages of that binary got touched during

07:49 common operations. And that distinction

07:51 is crucial. Suppose you have a 4K page

07:54 of code. On that page are like 200 bytes

07:57 of hot startup logic and then 3,800

07:59 bytes of rare air handling. If the

08:01 startup logic runs, the whole page comes

08:03 into memory because you don't get to

08:04 just page in the useful 200 bytes. The

08:07 memory manager deals only in pages. And

08:09 so that cold air handling is now

08:11 freeloading in RAM, drinking your beer,

08:13 and contributing absolutely nothing in

08:14 return. Now multiply that by thousands

08:17 of functions. Let's look at a simple

08:19 case of a library with 20 functions. If

08:21 each function has about 200 bytes of hot

08:23 path and the rest is edge cases and air

08:25 handling, we can pack all 20 functions

08:27 into a single page of memory. Assuming

08:29 that we never take an air path, we can

08:32 run the whole binary out of one 4K page.

08:34 But as soon as we hit an air case or an

08:36 else or we have to branch out to

08:37 wherever BBT moved the code and it's

08:39 likely not going to be resident, that's

08:41 when we finally take a hit. BBT's trick

08:44 was to separate the roommates. So hot

08:46 code goes with hot code and cold code

08:48 gets moved somewhere else. Startup paths

08:50 get clustered. Common UI operations get

08:53 clustered. But rare dialogues,

08:55 assertions, fallback cases, obscure

08:57 protocol handlers, and this should never

08:59 happen unless the printer driver is

09:00 actually haunted paths get moved away

09:02 from the code that you use every day.

09:04 That means fewer code pages get touched,

09:06 fewer instruction cache misses, fewer

09:08 ITLB misses, fewer taken branches, less

09:12 paging, faster startup, better

09:13 responsiveness, and perhaps most

09:15 importantly for that era, a smaller

09:17 working set. And all of this could

09:19 happen without touching the source code.

09:21 And that's the part that I find almost

09:22 magical. As developers, we tend to think

09:24 of performance as something we do while

09:26 writing the code. So you pick better

09:28 data structures, you avoid needless

09:29 allocations, you don't put a network

09:31 call in a paint handler unless you enjoy

09:33 making users hate you. But BBT attacked

09:36 a different layer. It said even if the

09:38 code is already compiled, even if the

09:39 algorithms are already chosen, the

09:41 physical arrangement of the machine

09:43 instructions still matters a great deal

09:45 and it really does. Think about a branch

09:48 at the source level. You might write

09:49 something common like if the common case

09:51 is true, then do the normal thing

09:53 otherwise handle the error. But after

09:55 compilation, the machine code has to

09:56 choose which path falls through and

09:58 which path jumps away. The profile

10:00 guided layout can arrange the common

10:02 path so execution just continues into

10:04 the next instruction. The rare path

10:06 becomes the taken branch. That sounds

10:08 tiny, and it is until you remember that

10:10 computers are tiny things happening

10:11 billions of times per second. So you

10:14 make the common path straight and

10:15 compact, and the CPU's front end

10:17 breathes easier. Modern binary

10:19 optimizers still care exactly about

10:21 this. LLVM's Bolt, for example, is a

10:24 postlink optimizer that uses profile

10:26 information to improve already optimized

10:29 binaries, especially by improving

10:31 layout. Research on basic block

10:33 reordering describes the trade-off

10:34 between fall through branches,

10:36 instruction cache behavior, and

10:37 instruction TLB locality, which is

10:40 precisely the kind of terrain that BBT

10:41 was exploring decades earlier. So, BBT

10:44 was not magic in the sense of inventing

10:46 new instructions or violating the laws

10:47 of computation. It was magic in the

10:50 stage craft sense. The same actors, the

10:52 same lines, the same plot, but now the

10:54 scenery changes happen cleanly. The

10:56 props are where the actors need them,

10:57 and nobody's wandering backstage during

10:59 the big emotional monologue looking for

11:01 their sword. Now, the hard part, of

11:03 course, is that rewriting binaries

11:04 safely is absolutely nasty. I had no

11:07 idea just how nasty until I got some

11:09 exposure to it via my work on product

11:10 activation, which used related tools for

11:13 anti-hacking and offuscation rather than

11:15 for performance. But taking apart an x86

11:18 executable and rearranging it is no mean

11:20 feat. A finished executable is not just

11:22 a bag of instructions. It's a contract.

11:24 It contains entry points, import tables,

11:26 export tables, relocation records,

11:29 exception metadata, stack unwinding

11:31 information, debug symbols, alignment

11:33 padding, jump tables, comd folding

11:35 artifacts, and all sorts of delicate

11:37 little assumptions that are built in.

11:39 Move code around and every relative

11:41 branch might change length. A short jump

11:43 may no longer reach far enough. A jump

11:45 table might contain addresses that need

11:47 fixing up. Exception handling may need

11:49 to know where a protected region begins

11:51 and ends. Debuggers still need to make

11:53 some sense of the result. Servicing

11:55 tools and binary diff systems may care

11:57 about layout. Hot patching may care

11:59 about instruction alignment. And if you

12:01 get it wrong, you don't get a slightly

12:02 suboptimal program. You get a program

12:04 that runs perfectly until a CFO clicks

12:06 on exactly the wrong menu item during a

12:08 board meeting and then it explodes in a

12:10 place that no source level debugger can

12:12 easily explain why. And this is why the

12:15 kind of tool that it was makes sense

12:16 inside a company like Microsoft. You

12:18 need the build discipline, the symbols,

12:20 the test coverage, the performance labs,

12:22 and the institutional willingness to let

12:24 a post-link tool touch production

12:26 binaries. Most companies would look at

12:28 that risk and decide they had suddenly

12:30 developed a deep emotional attachment to

12:31 unoptimized code. But Microsoft had the

12:34 right incentives back then. Windows and

12:36 Office were large native code products

12:38 running on constrained machines, and the

12:40 winds were user visible. If you could

12:42 reduce the number of pages touched

12:43 during boot or shell startup, users felt

12:46 it. If you could make common application

12:48 paths fit into fewer memory pages,

12:50 multitasking got better. If you could

12:52 keep hot code out of the swap file, the

12:54 whole system felt less like it was

12:55 dragging a refrigerator through wet

12:56 cement. And that brings us to the most

12:58 interesting philosophical point. The

13:00 binary layout is the user interface.

13:03 That sounds weird, but it's true. The

13:05 user doesn't see basic blocks. They

13:07 don't see cache lines. They don't see

13:08 TLB entries. They see whether the start

13:10 menu opens instantly. They see whether

13:13 Word actually launches before they lose

13:14 their train of thought. They see whether

13:16 switching applications feel sharp or

13:18 soggy. The physical arrangement of code

13:20 inside of a DL can absolutely change

13:22 that experience. In the 1990s, we cared

13:25 about this because we had to. The

13:26 machine forced taste upon you. RAM was

13:29 limited. Discs were slow. Cache was

13:31 precious. A page fault was not an

13:33 invisible implementation detail. It was

13:34 a tiny little ambush. Today we have

13:37 machines with memory measured in

13:38 gigabytes and SSDs that could move data

13:40 faster than old systems could move

13:41 excuses. But the principle did not go

13:44 away. We just became rich enough to get

13:46 to ignore it for a while. Modern

13:48 software has the same problem at a

13:49 different scale. The binaries are much

13:52 larger. The services are distributed.

13:54 The frameworks are deeper. The machines

13:56 are faster, but the dependency graphs

13:57 are absurd. And we still discover over

14:00 and over again that locality matters as

14:02 it always does. So put the hot data

14:04 together. Put the hot code together.

14:05 Keep the common path small. Push rare

14:08 paths away. Don't make the CPU fetch a

14:10 haststack when it only needs the needle.

14:12 That's why tools like Bolt and Propeller

14:14 exist now. And that's why PGO still

14:16 matters. That's why compilers and

14:18 linkers spend so much effort on layout.

14:21 The hardware got faster, but the memory

14:23 hierarchy got more complicated. The

14:25 speed of light did not improve because

14:26 your build system switched to YAML. BBT

14:29 also teaches a more subtle lesson about

14:31 optimization culture. The best

14:33 optimizations are often not glamorous.

14:35 Nobody puts reduce ITLB pressure by

14:38 rearranged cold basic blocks on the

14:40 retail box. There's no marketing sticker

14:42 that says now with fewer useless

14:44 instructions per cash line. But those

14:46 are exactly the kind of things that make

14:48 software feel professional. They're

14:50 invisible when done well. And that

14:51 invisibility is the point. Now, nobody

14:54 knew that BBT was being done because

14:55 users were not supposed to know. The

14:57 machine just felt better, faster,

14:59 stronger. And that's the highest form of

15:01 systems engineering. Not a splash screen

15:03 announcing your cleverness. Not a

15:05 benchmark cherrypicked for the press

15:07 kit. Just millions or billions of

15:09 machines doing slightly less dumb work

15:11 every second of every day. Now, we

15:14 should be careful not to overstate what

15:15 we actually know here. BBT was internal

15:18 and the public record is sparse. Lego

15:20 was our whimsical internal code name

15:22 associated with the idea of taking

15:23 binaries apart into movable pieces. But

15:25 I would not pretend that there's a

15:27 polished public manual sitting on a

15:28 shelf somewhere that tells us all the

15:30 versions, the product, and every build

15:32 switch. What we can say with some public

15:34 confidence is that Microsoft had a basic

15:36 block tool aimed at optimizing working

15:38 set size for paged applications and that

15:40 his broad approach fits squarely into

15:42 the family of profileg guided postlink

15:44 binary layout optimizers. And frankly,

15:47 that's already interesting enough on its

15:48 own because it means that some of the

15:50 performance that people experienced in

15:51 those old Microsoft products did not

15:53 come only from hand tuned C or clever

15:56 assembly or compiler switches. It also

15:58 came from understanding that a program

15:59 is not merely what it computes. It is

16:01 how its computation is physically

16:03 arranged in the memory. The CPU is not a

16:06 philosopher. It does not appreciate your

16:07 abstractions. It wants the next bytes

16:10 nearby, the next branch predictable, and

16:12 the next page already mapped, and the

16:14 next cache line full of useful work for

16:15 it to do. BBT was Microsoft looking at

16:18 the final binary and saying, "We can

16:20 help with that." And maybe that's the

16:21 lesson for today. We spend a lot of time

16:23 arguing about languages, frameworks,

16:25 cloud architectures, and AI generated

16:27 code. But beneath all of that, the old

16:29 rules are still there. Locality matters.

16:32 Hot paths matter. Measurement matters.

16:34 Representative workloads matter. You

16:36 can't optimize what you can't understand

16:38 and you cannot understand what you can

16:40 never measure. BBT was not just a tool.

16:42 It was evidence of a mindset. The job

16:45 was not done when the code compiled. It

16:47 was not done when the linker emitted the

16:48 executable. It was not even done when

16:50 the program worked. The job was done

16:52 when the program worked well on the

16:53 machines that customers actually owned.

16:55 And that's a standard worth bringing

16:57 back because faster hardware should not

16:59 make us careless. It should make the

17:00 experience feel luxurious. They should

17:02 let software be safer, richer, more

17:04 capable, and still immediate. The

17:06 tragedy of modern abundance is not that

17:08 we have too much hardware, so we often

17:10 spend it without noticing. Microsoft's

17:12 BBT noticed for us. It noticed that the

17:15 hot code was living next to cold. It

17:17 noticed that the startup paths were

17:18 scattered all over. It noticed that the

17:20 memory manager paid by the page, not by

17:22 the instructions. It noticed that a

17:24 branch avoided and a cash line saved and

17:26 a page not touched could really matter.

17:28 Then it quietly rebuilt a binary like a

17:30 mechanic blueprinting an engine after it

17:32 already rolled off the assembly line.

17:34 Same car, better balance, less wasted

17:36 motion, and the user never has to know.

17:39 If you found today's episode interesting

17:40 or entertaining, remember that I'm

17:42 mostly in this for the subs and likes.

17:43 So, I'd be honored if you consider

17:45 leaving me one of each before you go

17:46 today. If you have comments or questions

17:48 about this episode, I'd love to hear

17:49 them. So, please do leave them below.

17:51 And then be sure to check out our weekly

17:53 episode of Shop Talk on Dave's Attic,

17:55 the second channel where we answer the

17:56 week's best questions. In the meantime,

17:58 and in between time, I'll see you next

18:00 time right here in Dave's garage.

18:02 >> Do it. Do it. Do it.

