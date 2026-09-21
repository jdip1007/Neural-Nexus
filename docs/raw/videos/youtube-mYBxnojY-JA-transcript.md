---
source_url: https://www.youtube.com/watch?v=mYBxnojY-JA
source_type: video
ingested: 2026-09-19
published: 2026-09-19
duration_minutes: 16
language: en
sha256: 3fd351c6fc97dbfc4fd724468f5ee6aa6f52bcc7ca81a49efb3ec4d68bee47c4
time_sensitive: True
---

# YouTube Transcript: Malloc is NOT Magic: Let's Build it to Learn What's Inside!

## Video Information
- **Title**: Malloc is NOT Magic: Let's Build it to Learn What's Inside!
- **Video ID**: mYBxnojY-JA
- **Published**: Unknown
- **Views**: Unknown
- **Language**: en

## Transcript
00:00 Every program that you've ever written

00:01 or used depends on Malik whether you've

00:03 called it directly or not. C uses it,

00:05 C++ uses it for new. Python, JavaScript,

00:09 Java, C, Go, Rust, browsers, games,

00:12 databases, web servers, device drivers,

00:14 and probably even the little demon that

00:16 updates your Sonic Air toothbrush all

00:17 have some version of the same problem.

00:20 At runtime, they need memory, but they

00:22 don't know exactly how much ahead of

00:23 time. And then somebody has to give them

00:25 a pointer. And that someone is not a

00:27 magical little wizard. Nomalik looks

00:30 magical because the interface is almost

00:31 offensively simple. You say, "I need 37

00:34 bytes." And it hands you back an

00:35 address. That's it. No ceremony, no

00:37 explanation, just a pointer to what

00:39 looks like fresh empty space. But behind

00:41 that pointer is one of the most

00:42 important pieces of plumbing in the

00:44 entire software world, a memory

00:45 allocator. Today, we're going to build

00:47 the simplest one possible, but not just

00:49 in theory, not as a computer science

00:51 bedtime story. We're going to start with

00:53 the dumbest allocator you can imagine,

00:55 the kind you could write on a napkin

00:56 while waiting for your fries. And then

00:58 we're going to watch it fail in all the

00:59 real ways that real allocators have

01:01 spent the last 40 years trying not to

01:03 fail. Because while Malik isn't magic,

01:06 implementing it is a bit like running a

01:07 parking garage where every car is a

01:09 different size, nobody parks in order,

01:11 and half the drivers leave their keys in

01:13 somebody else's glove box. The problem

01:14 that Malik solves is simple to state and

01:17 surprisingly hard to solve. Well, your

01:18 program needs chunks of memory of

01:20 different sizes at different times. One

01:22 routine wants 24 bytes for a little

01:24 structure. Another wants 4 megabytes for

01:26 an image. A parser wants thousands of

01:28 tiny nodes. A web server requests big

01:30 buffers, but they only last a few

01:32 milliseconds. The operating system can

01:34 give a process memory, but it usually

01:36 does so in big chunks called pages. And

01:38 on modern systems, that's commonly 4K

01:40 pages, though larger page sizes are also

01:42 available. The OS is very good at

01:45 mapping pages of virtual address space

01:47 into your process, but it's not

01:49 interested in being called every time

01:50 you need 19 bytes for a string. That

01:52 would be like driving to Home Depot

01:53 every time you needed another nail. So,

01:56 Malak sits in between your program and

01:57 the operating system. It asks the OS for

02:00 big regions of memory and then it carves

02:01 those regions up into smaller pieces for

02:03 your code. On Unix like systems,

02:06 historically that meant break and sreak

02:08 to extend the program break and the

02:10 modern allocators also use end mapap for

02:12 larger mappings. On Windows, the C

02:14 runtime malik ultimately gets memory

02:16 from the Windows heap and virtual memory

02:18 machinery. The exact details differ, but

02:20 the shape of the problem is the same

02:21 everywhere. get big memory from the OS,

02:24 hand out little memory to the programs,

02:25 and somehow keep track of the mess. So,

02:28 let's start with the entire heap just

02:29 being a big empty array. That's one

02:31 megabyte of fake heap. And our first

02:33 allocator is almost insultingly small.

02:36 And there it is. That's a real allocator

02:38 in the same way that a tarp over a

02:40 shopping cart is technically a camper.

02:42 You ask for memory, it gives you the

02:43 current pointer, and then it moves the

02:44 pointer forward. And that's called a

02:46 bump allocator because allocation is

02:48 just bumping a pointer. And the first

02:50 time you see it, there's usually this

02:51 wonderful little moment where you think,

02:53 "Wait, really? That's it?" Yeah. In the

02:56 simplest case, that really is it. And

02:57 it's fast. Absurdly fast. It doesn't

03:00 search a list. It doesn't lock a mutex.

03:01 It doesn't split up blocks. It doesn't

03:03 maintain a tree. It doesn't ask the

03:05 operating system. It just returns an

03:06 address that increments a pointer. On a

03:08 modern CPU, that's barely more than a

03:10 shrug. This kind of allocator is not

03:13 just a toy, either. Bump allocation

03:14 shows up in real systems all the time

03:16 when the lifetime of the memory is

03:18 simple and well understood. Compilers

03:20 use arena allocators while parsing. Web

03:23 servers may allocate per request memory

03:24 for an arena and then throw the whole

03:26 arena away when the request completes.

03:29 Embedded systems use fixed pools where

03:31 allocation has to be deterministic. Some

03:33 operating system kernels use region

03:35 style allocations during boot because

03:36 early in boot there may not even be a

03:38 full heat manager yet. So our little

03:40 allocator is not stupid because it's

03:42 simple. It's stupid because it has no

03:44 answers to what happens next. First, it

03:46 has no bounce check. Ask it for two

03:48 megabytes from a 1 megabyte heap and it

03:50 will happily hand you a pointer into

03:51 tomorrow morning. That's better because

03:53 it now fails instead of just wandering

03:55 into the neighbor's yard wearing only a

03:56 bathrobe. But it still has a subtle

03:58 problem. Alignment. When Malo returns

04:01 memory, it has to be suitably aligned

04:02 for the kind of object you're going to

04:04 store there. If you allocate a double or

04:06 a pointer or a SIMD type, the CPU may

04:08 expect the address to be aligned to 8,

04:10 16, or even more bytes. On the x86,

04:13 unaligned access usually works, but can

04:15 be slower. On other architectures, it

04:17 can just fault outright. So, a real

04:19 allocator round sizes up to an alignment

04:21 boundary. And believe it or not, that

04:22 was actually the very first question I

04:24 was asked my first interview on my first

04:26 morning at Microsoft in my loop. Write a

04:28 function that returns the next highest

04:29 multiple of 16. So, I even know how to

04:31 do it. If we align to 16 bytes, asking

04:34 for 37 actually consumes 48. That extra

04:37 11 bytes is internal fragmentation,

04:39 which is a polite way of saying the

04:40 allocator took a little bite out of your

04:42 sandwich to keep the hardware happy. But

04:44 the biggest problem is that our

04:45 allocator cannot free anything. We can

04:47 add a function called free, of course.

04:49 And congratulations, we have just

04:51 reinvented the memory leak officially.

04:53 And that may sound useless, but even

04:54 this noop free has legitimate uses when

04:56 the allocator's lifetime in the arena is

04:58 that of the whole arena. If you allocate

05:01 a bunch of stuff while processing a file

05:02 and then you throw away the entire arena

05:04 in one go, you never need to free the

05:06 individual objects, that can be both

05:08 faster and safer because there's no

05:10 dangling half reused heap full of little

05:12 landmines to unwind. But general purpose

05:14 Malach cannot get away with that. In

05:16 normal programs, objects are born and

05:18 die in no particular order. So now Malik

05:20 allocates memory and free needs to give

05:23 it back. And this is where the elegant

05:24 little bump allocator is going to fail

05:26 hard. The allocator has to remember

05:28 which parts of the heap are used and

05:29 which parts are free. But where does it

05:31 store that information? Well, the answer

05:33 is usually right next to or in the

05:35 memory it gives you. A simple little

05:37 block might look like this. A structure

05:39 with a pointer and then the number of

05:41 bytes and then a pointer to the next

05:43 block. And that header is going to live

05:44 immediately before the pointer that

05:46 Malik returns. So when you ask for 100

05:48 bytes, the allocator actually reserves

05:50 enough space for your header plus 100

05:52 bytes, maybe rounded up for alignment.

05:54 It returns a pointer to pass the header.

05:56 To you, it looks like just pure usable

05:58 memory, but to the allocator, there's a

06:00 little tag staple to the front saying

06:01 how big the block is, whether it's free,

06:03 and where the next block lives. And this

06:05 is one of Malak's great little

06:07 illusions. The pointer you get looks

06:08 like the beginning of the allocation,

06:10 but it usually isn't actually the

06:12 beginning of the block because there's

06:13 metadata hiding just before it, like a

06:15 luggage tag that you're not supposed to

06:16 notice. Now, free becomes possible. When

06:19 you call free on a pointer, the

06:21 allocator subtracts the size of the

06:23 header from P, finds the block metadata,

06:25 and then marks it free. That also

06:27 explains why passing a bad pointer to

06:29 free is so catastrophic. If you pass a

06:31 pointer that didn't really come from

06:33 Malik, the allocator walks backwards

06:34 from it, then tries to interpret

06:36 whatever random bites happen to be there

06:37 as a block header. And if there's one

06:39 thing the colonel guys taught me is you

06:41 don't want to go swimming after somebody

06:42 has peed in the pool. And if you free

06:44 the same pointer twice, the allocator

06:46 may put the same block back into the

06:48 free list twice. Later, two different

06:50 calls to Malo may return the same memory

06:52 to two different parts of your program,

06:53 and now you've got two owners of the

06:55 same house, both redecorating the

06:56 kitchen at the same time. Good luck

06:58 debugging that one. That's called heap

07:00 corruption, and it's one of the reasons

07:01 that C and C++ give you both incredible

07:04 power and an incredible ability to ruin

07:06 your weekend. But now, our allocator has

07:08 a free list. When Malik needs memory, it

07:10 scans a list looking for a free block

07:12 big enough to satisfy it. That's called

07:14 first fit if it takes the first suitable

07:16 block. There's also best fit which tries

07:18 to use the smallest block that works.

07:20 And there are lots of variations, but

07:22 every strategy is making trade-offs. So

07:25 suppose our heap looks like this. Used,

07:27 free, used, free, and then used. So you

07:29 have memory free, plenty of it maybe,

07:31 but now you ask for a block larger than

07:32 any individual free gap. You might have

07:35 500k free in total, but if it's

07:37 scattered in 50 little individual

07:38 blocks, you cannot satisfy a 200k

07:41 allocation. It's the memory allocator

07:43 version of having enough floor space in

07:44 the garage for your motorcycle, except

07:46 it's distributed across 400 places

07:47 between paint cans, Christmas

07:49 decorations, and whatever that weird

07:50 cable was for. The allocator can fight

07:53 fragmentation by splitting and coalesing

07:55 blocks. Splitting means if you have a

07:57 free 1,000 byt block and somebody asks

07:59 for 100 bytes, you don't give them the

08:01 whole 1,000 bytes. you split it into a

08:03 100 block bite and a 900 block bite.

08:05 Coalescing is the opposite and it means

08:07 that when a block is freed, you check

08:08 whether the neighboring blocks are also

08:10 free on each side. And if so, you merge

08:12 them back into one larger block. That

08:14 sounds straightforward until you ask how

08:16 the allocator knows who the neighbors

08:18 are. So, you can keep blocks in address

08:20 order. You can store a footer at the end

08:22 of the block, sometimes called a

08:23 boundary tag, so you can walk backwards

08:25 as well as forwards. You can maintain

08:27 separate lists for free blocks. You can

08:29 use bins organized by size class. Every

08:32 little improvement adds metadata,

08:33 complexity, and another opportunity to

08:35 get things wrong. And this is why real

08:37 Malak implementations are not five lines

08:39 long. The fiveline version works right

08:41 up until the time when reality touches

08:43 it. Real allocators usually don't keep

08:45 one giant free list. That would be too

08:47 slow. If every Malach had to scan

08:49 thousands of blocks to find just one

08:51 that fits, your program would spend most

08:52 of its life doing tiny real estate

08:54 transactions. Instead, allocators divide

08:57 memory into size classes. So, tiny

08:59 allocations go into one set of bins,

09:01 medium allocations go into another, and

09:03 large allocations may bypass the normal

09:05 heap entirely and request dedicated

09:07 virtual memory mappings from the

09:08 operating system directly. That is

09:10 because allocation patterns are not

09:11 random. Programs tend to allocate a lot

09:14 of objects of the same size. Strings,

09:16 nodes, buffers, hasht entries, message

09:18 objects, gooey controls, packets. So if

09:21 you know that a request is for 64 bytes,

09:23 you can often satisfy it from a bin of

09:25 64 byt chunks without searching the

09:27 entire heap. This is also the idea

09:28 behind slab allocators and object pools.

09:31 If you allocate the same kind of thing

09:33 over and over, prepare a tray of exactly

09:35 the kind of thing and stop making the

09:36 allocator guess. Then come threads. In

09:39 the old days, a program might be mostly

09:41 single threaded and Malik could get away

09:42 with some relatively simple locking. But

09:44 modern software has thread pools, async

09:47 runtimes, background workers, render

09:48 threads, audio threads, telemetry

09:50 threads, and 17 things named helper that

09:53 appear in task manager while appearing

09:54 to do absolutely nothing helpful. If

09:56 every thread has to grab one global heap

09:58 lock for every allocation, then Malik

10:00 effectively becomes like a traffic light

10:02 in the middle of a freeway interchange.

10:04 So modern allocators often use per

10:06 thread caches or multiple arenas. A

10:09 thread can allocate small objects from

10:10 its local cache without contending with

10:12 every other thread in the process.

10:14 That's much faster, but it introduces

10:16 new trade-offs. Memory can become

10:18 stranded in one thread's cache while

10:20 another thread really needs it. More

10:22 arenas can reduce lock content, but

10:24 increase the total memory footprint.

10:26 Once again, every solution drags a

10:28 little wagon of new problems behind it.

10:30 And then there's security. For many

10:31 years, heap metadata was a favorite

10:33 target for exploitation. If an attacker

10:35 could overflow a buffer and overwrite

10:37 the allocator's bookkeeping, they might

10:38 be able to trick free into writing

10:40 attacker controlled values to attacker

10:43 controlled locations. And that's the

10:45 sort of bug that turns oops, I just

10:46 copied too many bytes into oops, now

10:48 somebody else owns your process. Modern

10:51 allocators defend themselves with

10:52 cookies, encoded pointers, guard pages,

10:55 delayed reuse, quarantines, heap

10:57 consistency checks, randomized layouts,

10:59 and debug modes that fill free memory

11:01 with recognizable patterns. Tools like

11:03 address sanitizer can catch use after

11:06 free and out of bounds rights by

11:07 surrounding allocations with poisoned

11:09 regions. Back in the NT days, we had a

11:11 special debug allocator that would put

11:13 hardware guard pages before and after

11:15 every allocation. It was a ton of

11:17 overhead to run that build, but it shook

11:19 a lot of bugs loose. These tools are

11:21 wonderful, but they work because they

11:22 make the memory allocator more

11:24 suspicious, and suspicion has a cost.

11:26 And that cost is why your release

11:28 allocator and your debug allocator may

11:30 behave very differently. The debug heap

11:33 allocator is like a building inspector

11:34 who checks every nail, every joint, and

11:36 everything. The release heap allocator

11:38 is trying to get the subdivision built

11:39 before lunch. There's another

11:41 misconception worth killing too, and

11:42 that is that free does not necessarily

11:44 give memory back to the operating system

11:46 right away. Often it just returns the

11:48 block to the allocator so it can be

11:50 reused by your process. So your process

11:52 memory usage may not go down in task

11:55 manner just because you freed a bunch of

11:56 objects. the allocator may hold on to

11:59 that memory because it expects that

12:00 you'll need it again and giving it back

12:02 to the OS to only ask for it 10

12:03 milliseconds later would be silly. So

12:06 large allocations are also more likely

12:07 to be returned because they may have

12:09 their own page mappings. But small

12:11 allocations usually stay in the heap's

12:13 private economy. That's why memory

12:15 behavior can be surprising. You allocate

12:17 a million small objects, free them all,

12:19 but your process still looks fat. It may

12:21 not be leaking. It may simply have a

12:23 heap that is now well stocked with

12:24 reusable objects. On Windows, the heap

12:27 manager has evolved through decades of

12:29 exactly these problems. The low

12:31 fragmentation heap was introduced to

12:33 improve behavior for common allocation

12:35 patterns by grouping allocations into

12:37 buckets and reducing the kind of

12:38 fragmentation that made older heaps look

12:40 like Swiss cheese after a few bad hours.

12:43 Other platforms have allocators like J

12:45 Malak, TC Malak, Mi Malik, and Harden

12:47 Malaks. Each tuned for different

12:49 balances of speed, footprint,

12:51 scalability, and security. And that's

12:53 the point. There is no one perfect

12:55 Malako. There are only trade-offs. If

12:57 you optimize for raw speed, you may use

12:59 more memory. If you optimize for low

13:01 memory footprint, you may spend more CPU

13:03 cycles searching and coalescing. If you

13:05 optimize for thread scalability, you may

13:07 duplicate caches and arenas. If you

13:09 optimize for security, you may add

13:11 checks and randomness that cost you time

13:13 and space. If you optimize for

13:14 deterministic timing, as in embedded

13:16 real-time systems, you may avoid general

13:19 purpose malic entirely in hot paths

13:21 because unpredictable allocation latency

13:23 is unacceptable to you. And that all

13:25 leads to a practical takeaway, which is

13:26 that the fastest Malo call is the one

13:28 you do not make. Now, I don't mean you

13:30 should never allocate memory. That's

13:31 silly. I mean, allocation patterns

13:33 matter. If you allocate inside a hot

13:35 loop without thinking about it, you may

13:37 be pouring sand into the gears of your

13:38 machinery. If a vector or dynamic array

13:41 keeps growing one element at a time,

13:43 reserve the capacity ahead of time when

13:45 you can. If you allocate millions of

13:47 tiny objects with the same lifetime, use

13:49 an arena for them and free them all

13:50 together. If you allocate the same

13:52 fixedsiz object repeatedly, consider a

13:54 pool. If you were passing strings around

13:56 and copying them three times because the

13:58 abstraction diagram looked better that

14:00 way, maybe the machine is trying to tell

14:01 you something. And profile before you

14:04 get religious about it. Malik is often

14:06 not the bottleneck. Modern allocators

14:08 are actually very good. But when

14:10 allocation is the bottleneck, it can be

14:12 spectacularly bad because it's not just

14:14 the allocator cost. It's the cache

14:16 misses, the fragmentation, it's memory

14:18 bandwidth, it's lock contention, it's

14:20 TLB pressure, it's destructors and

14:22 constructors and zeroing and page faults

14:24 and all the invisible machinery that

14:26 wakes up because you asked for another

14:28 tiny object in the wrong place. The real

14:30 lesson is not that Malik is bad. Malach

14:32 is one of the great enabling hacks in

14:34 software history. It lets static

14:35 programs adapt dynamically at runtime.

14:37 It lets data structures grow. It lets

14:39 code handle the world as it is instead

14:41 of the world the programmer guessed

14:42 about at compile time. But Malo is not

14:45 magic. It starts as a pointer into a big

14:47 empty array. Then you add bounce checks,

14:49 then alignment, then headers, then free

14:51 lists, then splitting, then coalescing,

14:52 and then bins, then larger allocation

14:54 paths, then locks, then thread caches,

14:57 then arenas, then security hardening,

14:59 and then debug modes, and then tools to

15:00 help you find all the ways that you've

15:02 been using it wrong. And by the time

15:04 you're done, Malik has become a tiny

15:05 little operating system inside your

15:07 process, managing a private city of

15:09 blocks and pages and alleys and

15:10 abandoned warehouses. Most of the time

15:12 it works so well that you never think

15:14 about it. Which is exactly the kind of

15:16 engineering we tend to undervalue. The

15:18 engineering that disappears when it's

15:19 done right. So the next time you write

15:21 Malak 128 and get back a pointer,

15:23 remember what just happened. A little

15:25 bookkeeper found a place in your

15:26 process's private universe, made sure it

15:28 was aligned, recorded its size, hid an

15:30 ID tag in front of it, maybe split up a

15:33 larger block, maybe pulled a thread from

15:34 the thread cache, maybe asked the OS for

15:37 new pages, and then handed you an

15:38 address with the quiet confidence of a

15:40 parent who knows that you're absolutely

15:41 going to write past the end of it

15:42 someday anyway. And when you call free,

15:44 it will take that memory back, mark it

15:45 as available, maybe merge it with its

15:47 neighbors, maybe hold it for reuse,

15:49 maybe return it to the OS, and then sit

15:51 there quietly hoping you don't touch

15:52 that pointer again. So, Malik isn't

15:55 magic. It's bookkeeping. Plus 40 years

15:57 of people fixing all the ways that the

15:58 bookkeeping can go wrong. If you found

16:01 today's episode interesting or

16:02 entertaining, remember I'm mostly in

16:03 this for the subs and likes. So, I'd be

16:05 honored if you consider leaving me one

16:06 of each before you go today. And if you

16:08 have a good question, please post it in

16:09 the comments with a question mark. We

16:11 answer all the best ones every Friday on

16:13 Shop Talk. And I'll put a link to one

16:14 episode here so you can check it out. Go

16:16 over there and give it a subscription as

16:17 well if you like it. Thanks. And in the

16:20 meantime, and in between time, I'll see

16:21 you next time right here in Dave's

16:23 Garage.

16:24 >> Do it. Do it. Do it.

