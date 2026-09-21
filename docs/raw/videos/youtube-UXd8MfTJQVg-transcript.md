---
source_url: https://www.youtube.com/watch?v=UXd8MfTJQVg
source_type: video
ingested: 2026-09-19
published: 2026-09-19
duration_minutes: 12
language: en
sha256: 4fa98cac7fe2b595ef1626cb376627c44302f84c2fbdf4bae90361859e946eb5
time_sensitive: True
---

# YouTube Transcript: What do CPUs do when there's nothing to do?

## Video Information
- **Title**: What do CPUs do when there's nothing to do?
- **Video ID**: UXd8MfTJQVg
- **Published**: Unknown
- **Views**: Unknown
- **Language**: en

## Transcript
00:00 What does a CPU do when there's nothing

00:02 to do and how does it do it? Open Task

00:05 Manager on a quiet Windows machine and

00:06 you may see something that looks

00:07 absolutely backwards. The system idle

00:10 process sitting there using 90 95 even

00:13 99% of your CPU. And if you've never

00:16 seen it before, your natural reaction

00:18 might be, well, there's the problem.

00:19 It's this idle thing hogging the whole

00:21 machine. But the system idle process is

00:24 not stealing your CPU. It's the

00:26 accounting record for the CPU that

00:28 nobody wanted. It's the empty lane on

00:30 the freeway at 3 in the morning. It's

00:32 not traffic. It's the absence of

00:33 traffic. And yet, that simple little

00:35 number opens a door to one of the most

00:37 important parts of any operating system.

00:39 What does a CPU do when there's nothing

00:41 to do? Because a processor can't just

00:44 wander off and get a coffee. At every

00:46 instant, every logical processor in your

00:48 machine has to be in some defined state.

00:51 It's either running a thread that has

00:53 work to do, handling an interrupt,

00:55 executing kernel code, or sitting in

00:57 some kind of idle path waiting for the

00:59 next event. The system idle process is

01:02 Windows giving a name and a counter to

01:03 that last category. I actually did it

01:06 recently in my night driver code, an

01:07 ESP32 project that runs all these LEDs.

01:10 I had two cores, so I created two idle

01:12 tasks, one for each core, both scheduled

01:14 at the absolute lowest priority. Their

01:17 job was simply to run when nothing else

01:19 could. In my case, I just burned time in

01:22 a busy weight, kept track of how much

01:23 time they wasted, and that made the idle

01:25 measurement easy. Anytime those lower

01:28 priority tasks got scheduled, it meant

01:30 that there was no real task time needed.

01:32 And that's a great model for

01:34 understanding the idea. But it's also

01:36 exactly the wrong model for a modern

01:38 Windows PC. Because on a small embedded

01:40 system, especially one running at a

01:42 fixed clock speed, the idle task that

01:44 spins in a loop may be good enough. It's

01:46 wasteful, but the waste is visible and

01:48 predictable. If your idle task ran 80%

01:51 of the time, then roughly 80% of the CPU

01:53 was unused. Older PCs like the one I

01:56 wrote the original task manager on were

01:58 closer to that world. CPUs often ran at

02:00 a constant speed, so CPU usage was

02:03 mostly a time measurement that felt like

02:05 a work measurement. If the machine said

02:07 it was 50% busy, you could imagine that

02:09 half of the available compute budget had

02:11 been consumed. Modern CPUs laugh at that

02:14 simplification. Today, a processor is

02:16 not like a fixed speed crankshaft or

02:18 flywheel. It's a power managed beast. It

02:21 can run one moment at 5 GHz, the next

02:23 one at 1 ghahertz, and then put a core

02:25 into a shallow nap, then a deeper sleep,

02:27 then wake up on an interrupt and turbo

02:29 again before you have a chance at all of

02:32 catching that on a graph. So, if you see

02:34 50% CPU today, that might mean that the

02:36 CPU spent half the time doing work at

02:38 high speed and the other half resting at

02:40 low power. Or it might mean that all

02:42 cores were lightly loaded, or one core

02:44 was pegged while the others were asleep,

02:47 or a hybrid CPU was juggling work

02:49 between performance cores and efficiency

02:50 cores. And so that percentage is not the

02:53 whole truth. It's kind of a cartoon

02:54 version of the truth. Windows does not

02:57 schedule programs. It schedules threads.

02:59 Every processor you think of as an app

03:01 is really a container for one or more

03:03 threads. And those threads are what the

03:05 scheduleuler actually chooses between.

03:07 If a thread is ready to run, it goes

03:09 into a ready queue. Theuler looks at

03:12 priorities, processor affinity, recent

03:14 history, fairness, power policy, and a

03:16 pile of other details, and then chooses

03:18 what should run next on each logical

03:20 processor. But sometimes there is no

03:23 thread ready to run on a given

03:24 processor. And not no important thread

03:27 and not no foreground app. What we mean

03:29 is that there's no runnable thread

03:31 available at all. Everything is waiting

03:33 for disk or waiting for a network packet

03:35 or waiting on a timer or waiting for a

03:37 lock or waiting for the user or it's

03:38 simply finished. And at that point,

03:40 theuler still needs to answer the

03:42 question, well, what thread runs now?

03:44 And the answer is the idle thread. So

03:46 each logical processor has an idle

03:48 thread. The system idle process is the

03:51 object that Windows uses to account for

03:53 these this group of idle threads. It's

03:55 not a normal application. You can't

03:57 close it to reclaim performance. You

03:59 can't uninstall your idleness. It's the

04:02 bottom of the scheduleuler's world, the

04:03 safe place the CPU lands when there is

04:06 nothing else useful to execute. This is

04:08 cleaner than making nothing a special

04:10 case because kernels hate special cases

04:12 because special cases grow teeth

04:14 eventually. It's much better to say that

04:15 every processor is always running some

04:18 thread and that sometimes that thread is

04:19 the idle thread. But the idle thread on

04:21 a modern PC does not sit there in a

04:23 tight loop saying, "Are we there yet?" a

04:24 billion times a second. That would be

04:26 insane. It would keep the processor

04:28 awake. it would burn power, generate

04:30 heat, and murder your battery for the

04:32 privilege of accomplishing absolutely

04:33 nothing. So instead, the idle path

04:36 becomes an opportunity to save power.

04:38 The simplest old school version of this

04:40 on the x86 is the old halt instruction.

04:43 Halt just tells the processor to stop

04:45 executing instructions until something

04:47 happens, typically an interrupt. That

04:49 alone is a giant improvement over a busy

04:51 loop because the core is no longer

04:53 fetching, decoding, and executing

04:55 useless instructions. But modern idle

04:57 goes much deeper. CPUs have performance

05:00 states and idle states. Performance

05:02 states, often called Pates, control

05:04 things like the frequency and the

05:06 voltage and what's going on with the

05:08 processor while it's active. Idle

05:10 states, or Cates, describe how deeply

05:12 parts of the processor can go to sleep

05:14 when there is no work to do. So, a

05:17 shallow idle state is quick to leave and

05:19 quick to enter, but saves less power. A

05:21 deeper idle state saves more power but

05:24 costs more time and energy to enter and

05:25 exit. So Windows has to make a judgment.

05:28 If the next timer is going to fire in

05:30 100 micros secondsonds, then diving into

05:32 a deep sleep state would be pointless.

05:34 And by the time you get settled in, it's

05:36 already time to wake up again. But if

05:37 the machine can stay quiet for 20

05:39 milliseconds, now the math changes. The

05:41 CPU can shut down more internal

05:43 machinery, reduce power, and come back

05:45 when the next interrupt rings its

05:46 doorbell. And that means the idle thread

05:48 is no longer just a trash can for spare

05:50 cycles. It's now part of the power

05:52 management strategy. And that strategy

05:54 only works if your software cooperates.

05:57 So if a program has nothing to do, it

05:59 should block. It should wait on an

06:01 event, a socket, a timer, a file

06:03 handler, or some other kind of

06:05 synchronization object. Because when it

06:07 does that, Windows removes the thread

06:09 from the ready Q. Theuler no longer

06:11 considers it runnable. And that opens

06:13 the door for the idle thread to run and

06:15 the processor can then potentially

06:16 sleep. But if a program busy waits, it

06:19 lies to theuler. It says, "I'm ready and

06:21 I have work to do." Even if all it's

06:23 doing is spinning in a loop, checking

06:25 whether something important changed, it

06:27 still looks and is runnable. So the CPU

06:29 keeps running it, maybe at low priority,

06:32 maybe plately yielding to real work, but

06:34 preventing idle nonetheless. And that

06:36 distinction matters more now than it did

06:38 in the old fixed speed world. A low

06:40 priority background task that burns CPU

06:43 may not make your foreground app slow,

06:45 but it can stop the processor from

06:46 entering deeper idle states. So the

06:49 machine feels fine, but the fan runs,

06:51 the laptop gets warm, the battery

06:53 disappears. You look at task manager and

06:55 nothing looks dramatic because the crime

06:57 is not performance. The crime is

06:59 preventing rest. And that's why idle on

07:02 a modern machine is not merely the

07:03 absence of work. It's a carefully

07:05 engineered state the system tries to

07:07 reach and preserve. It's also why CPU

07:10 usage is easier to misunderstand than

07:12 ever. When Task Manager says a system

07:14 idle process is at 95%, that usually

07:16 means the CPU is mostly unused, which is

07:19 good. It does not mean that the idle

07:20 processes is consuming 95% of your

07:23 system. It means that 95% of the sampled

07:25 processor time had no better work to do.

07:28 The idle process is not the pig of the

07:30 trough. It's just the leftover food,

07:33 which kind of makes it the pig of the

07:34 trough. So, forget that analogy. But

07:37 conversely, if the system idle process

07:39 is low, something is using the CPU. That

07:42 something might be an app or a service

07:43 or a driver, interrupt handling,

07:45 antivirus, indexing, compression, or a

07:48 browser tab that's decided to become a

07:50 space heater, or perhaps some background

07:52 service doing what background services

07:53 do best, which is making you wonder why

07:55 they exist. But even then, the aggregate

07:57 number can mislead you. Suppose you have

08:00 an eight logical processor machine, and

08:02 one old singlethreaded program pins one

08:04 logical processor at 100%. Overall CPU

08:07 usage may only show 12 or 13%. The

08:10 system as a whole is mostly idle, but

08:12 the program that you care about is

08:13 completely bottlenecked. From the

08:15 machine's point of view, there is plenty

08:17 of CPU left. From your point of view,

08:19 the app is stuck in molasses. But both

08:21 things are true. And that's why averages

08:23 are where the truth goes to wear a fake

08:25 mustache. And the reverse is also true.

08:27 A machine can show moderate CPU usage

08:30 and still feel terrible because the CPU

08:31 is not the bottleneck. It might be

08:33 waiting on disc. It might be paging

08:35 because memory is tight or it might be

08:37 stalled on network calls. It might be

08:39 thermally throttled. It might be

08:41 drowning in interrupts from a bad driver

08:43 or it might be stuck behind a lock held

08:44 by another thread that is itself waiting

08:46 for something else. Computers are very

08:49 good at arranging circular blame. The

08:51 system idle process helps you eliminate

08:53 at least one suspect. So if idle is

08:55 high, the CPU probably is not your main

08:57 problem. Not always, but usually. If

09:00 idle is low, then something is keeping

09:01 the processors busy and then you go

09:03 hunting. There's one more wrinkle, and

09:05 it's a big one. Timers. Modern operating

09:08 systems try hard to batch work. If 10

09:10 different programs each wake up once per

09:12 second at slightly different times, the

09:14 CPU may never get a decent nap. It's

09:17 wake, work, sleep, wake, work, sleep

09:19 over and over. So, Windows tries to

09:21 coales timers where it can, aligning

09:23 wakeups so that the machine handles a

09:25 burst of activity and then returns back

09:26 to idle. It's one of these clever

09:28 optimizations that users rarely ever

09:30 notice, but they will absolutely notice

09:32 it when it doesn't work. a badly behaved

09:34 app that wakes the CPU all the time and

09:36 can destroy battery life while barely

09:38 appearing in the performance charts.

09:40 It's like somebody walking into your

09:42 bedroom every 30 seconds to ask you if

09:43 you're asleep yet. So, the best idle

09:45 time is not just unused time, it's

09:47 uninterrupted unused time. And that's

09:50 also why operating systems have become

09:52 more aggressive about background work.

09:54 They defer it, they batch it, they run

09:56 it on a laptop when it's plugged in.

09:58 They avoid waking sleeping cores if one

10:00 active core can handle the work. They

10:02 may park cores entirely on hybrid

10:05 systems. They may prefer efficiency

10:06 cores for background tasks and reserve

10:08 performance cores for foreground

10:10 responsiveness. And the goal is not to

10:12 simply make the CPU graph look better.

10:14 The goal is to get useful work done

10:16 quickly and then get out of the way.

10:18 This is sometimes called the race to

10:19 idle. It sounds counterintuitive, but it

10:21 can be more efficient to run fast for a

10:23 short burst and then sleep deeply than

10:25 to run slowly for a long time while

10:28 never quite getting idle. Your CPU may

10:30 sprint to finish a task and then drop

10:32 into a low power state. And that spike

10:34 is not necessarily waste. It may be the

10:37 most efficient path back to doing

10:38 nothing. And doing nothing done properly

10:40 is one of the hardest jobs on the

10:42 machine. So the systemal process exists

10:44 for three main reasons. It gives theuler

10:47 a real thread to run when nothing else

10:49 is ready. Gives Windows and tools like

10:51 task manager a clean way to account for

10:53 unused processor time. And it provides

10:55 the entry point into the processor idle

10:57 behavior that lets modern systems save

10:59 power, reduce heat, and stay responsive.

11:02 That's the journey from the simple

11:04 embedded idle task to the modern Windows

11:06 idle process. That's the journey from

11:08 the simple embedded idle task to the

11:10 modern Windows idle process. The

11:12 embedded system just says run this

11:14 lowest priority loop so we can measure

11:15 what's left. The modern Windows version

11:17 says there's no work here. So, let's

11:19 account for that fact, predict how long

11:20 the silence might last, and then put as

11:23 much silicon to sleep as we safely can.

11:25 And that's why the old mental model is

11:27 useful but incomplete. On a fixed speed

11:30 system, idle time is wasted time. On a

11:33 modern system, idle time is an asset.

11:35 It's where battery life comes from. It's

11:37 where thermal headroom comes from. It's

11:39 what lets your CPU turbo when you

11:41 actually need it to because it wasn't

11:42 wasting heat 5 seconds earlier doing

11:44 nothing badly. The system idle process

11:46 is not your enemy. It's Windows saying

11:48 good news. The machine has spare

11:50 capacity. And on a modern computer,

11:52 spare capacity is not just unused

11:54 performance. It's potential silence,

11:56 potential battery life, potential

11:58 coolness, and potential speed later when

12:00 you need it. So the next time you see

12:02 the system idle at 98%, don't panic.

12:04 It's not a runaway process. It's not

12:06 malware. It's not Windows eating itself.

12:08 It's just a sound of your CPU waiting

12:10 politely for something worth doing. And

12:12 in a world where so much software seems

12:14 determined to burn every available cycle

12:15 just to animate the settings page, a

12:17 processor that knows how to do nothing

12:19 for a bit is a beautiful thing. If you

12:21 found today's episode interesting or

12:23 entertaining, remember that I'm mostly

12:24 in this for the subs and likes. So, I

12:26 would be honored if you would consider

12:27 leaving me one of each before you go

12:29 today. And if you're already subscribed,

12:31 thank you. In the meantime, and in

12:33 between time, I'll see you next time

12:34 right here in Dave's Garage.

12:37 >> Do it. Do it. Do it.

