---
title: YouTube Transcript: Why Your Computer Is Slow — Task Manager Can't Tell You
created: 2026-10-01
updated: 2026-10-01
type: video
source_url: https://www.youtube.com/watch?v=z_mFHlUpC-g-transcript
source_type: video
ingested: 2026-10-01
published: recent
duration_minutes: 20
language: en
time_sensitive: True
---


# YouTube Transcript: Why Your Computer Is Slow — Task Manager Can't Tell You

## Video Information
- **Title**: Why Your Computer Is Slow — Task Manager Can't Tell You
- **Video ID**: z_mFHlUpC-g
- **Published**: Unknown
- **Views**: Unknown
- **Language**: en

## Transcript
00:00 Something just happened to this

00:01 computer. The fans are spinning up. The

00:04 machine is starting to drag. And if this

00:06 were yours, you'd already be asking the

00:07 same question everybody asked when their

00:09 computer starts misbehaving. Why is it

00:11 slow? 30 years ago, I wrote the original

00:14 Windows Task Manager. This summer, I

00:17 built a brand new one. Now, the old one

00:19 was pretty good at telling you what's

00:20 happening right now, but I wanted

00:22 something that could tell me why it was

00:23 happening and even what happened 5

00:25 minutes ago when nobody was actually

00:27 looking. So, I'm not going to spend the

00:29 next 15 minutes just clicking through

00:30 tabs and showing you all the sexy new

00:32 features. I'm going to break this

00:34 computer on purpose in several different

00:36 ways, and we'll diagnose each one with

00:38 the new task manager to show you how it

00:40 works. Then, I'm going to break it one

00:42 last time, wait until the evidence has

00:44 disappeared, and then see if we can

00:45 catch the culprit after it's already

00:47 left the scene. Right now, our first

00:50 crime is still very much in progress.

00:51 And before I've even touched the mouse,

00:53 T-Mog has already given us our first

00:55 clue. CPU utilization has climbed

00:58 dramatically. Power consumption is

01:00 following it upwards and temperature is

01:02 beginning to move as well. And right

01:04 here on the same screen are the

01:05 processes most responsible for that

01:07 activity. And that's really the

01:09 fundamental idea behind T-MoG. I don't

01:11 merely want to know that my computer is

01:13 busy. I want to know precisely why.

01:18 The CPU looks like the obvious suspect.

01:20 So that's where we'll start. When most

01:23 system monitors tell you that your CPU

01:25 is at 60%, they're compressing a

01:27 remarkable amount of information into

01:29 one innocent looking number because a

01:31 modern processor might contain dozens of

01:33 logical processors. And increasingly,

01:35 those processors aren't even all of the

01:37 same kind. On a hybrid Intel processor,

01:40 just like on Apple silicone, we've got

01:42 performance cores intended to do heavy

01:44 lifting and then efficiency cores

01:45 designed to handle other work using less

01:47 power. T-mog distinguishes between them

01:50 visually, which means I can see not

01:51 merely that the processor is busy, but

01:53 where the work actually landed and

01:55 ideally what kind of work it was. From

01:57 there, we can follow the evidence back

01:59 to whoever is responsible. That's a

02:01 distinction that I kept coming back to

02:03 while writing T-mog. Measurement versus

02:05 diagnosis. A thermometer can tell you

02:07 that you have a fever, but it can't tell

02:09 you which raccoon bit you. In the same

02:11 way, the performance graphs tell us

02:13 which subsystem is under stress, but

02:15 eventually we need to connect that

02:16 condition back to whatever actually

02:18 caused it. And that's where the process

02:20 list becomes the other half of the

02:21 investigation. I didn't actually start

02:24 the summer intending to write another

02:25 task manager. One of my kids needed his

02:28 appendix out and then had complications

02:30 afterwards, requiring a second surgery

02:32 and a transfusion and so on. So, I wound

02:34 up with the better part of a week

02:35 sitting in hospital waiting rooms with

02:37 my laptop. and I'm pleased to report

02:39 that he's completely fine now. But I

02:42 finally had the time to write down 30

02:43 years worth of great ideas for Task

02:45 Manager that others and I had a little

02:47 too late for the original. And that's

02:49 how T-mog or Task Manager OG got

02:52 started. Plus, I wanted really to see

02:54 how I could update the visuals since 30

02:56 years of GPU development have enabled

02:58 some fairly compelling effects. If every

03:00 slow computer were caused by CPU

03:02 utilization, however, this would be a

03:04 wonderfully short episode and I would

03:05 have had considerably less software to

03:07 write because we're about to make this

03:08 machine feel almost exactly the same way

03:11 while barely bothering the CPU at all.

03:16 Now, watch the machine first. It's

03:18 becoming unpleasant again, but this time

03:19 the CPU isn't doing anything

03:21 particularly exciting. If all I had was

03:23 a CPU graph, I'd already be

03:25 investigating the wrong suspect.

03:28 Memory is telling us a different story.

03:31 People tend to look at something like 24

03:32 gigabytes used and assume that less

03:34 would be better. But unused memory is

03:36 not inherently virtuous. After all, you

03:39 paid for all that RAM and a modern

03:41 operating system will happily put spare

03:42 memory to good, useful work. What

03:45 matters here is that we're starting to

03:46 see real memory pressure and that the

03:48 operating system is having to work

03:49 around it. So now we've made the

03:51 computer feel almost exactly the same

03:53 way twice and produced that symptom

03:54 through two entirely different

03:56 mechanisms. The first time the processor

03:58 was doing too much work. This time the

04:01 CPU itself is largely innocent. And if

04:03 we simply sorted processes by CPU and

04:05 started killing whatever floated to the

04:07 top, we'd be treating the symptom with

04:09 approximately the diagnostic precision

04:10 of medieval medicine. Think of the

04:13 original task manager as a suitable

04:14 battlefield surgeon for the Civil War.

04:16 But in today's world, amputation is not

04:19 the right cure for every ill. T-Mog

04:21 helps you pick the right solution for

04:23 the particular problem that you're

04:24 having. The important part is that we've

04:26 narrowed the problem down from the

04:28 computer is slow to the memory subsystem

04:30 is under pressure. And only then does it

04:32 make sense to follow that evidence back

04:34 to the process responsible.

04:38 Now let's make the machine unpleasant in

04:39 a third way because this one is

04:41 particularly good at hiding from anyone

04:43 who believes that high CPU utilization

04:46 is synonymous with poor performance. The

04:48 computer is sluggish again. CPU isn't

04:51 pegged. Memory isn't in obvious

04:52 distress. But now the storage graph

04:55 certainly is. A process can spend most

04:57 of its time waiting for a disk or a

04:59 network connection or another process or

05:01 a synchronization primitive. And while

05:03 it's waiting, a CPU utilization can look

05:05 wonderfully innocent. Diagnosing every

05:08 performance problem by sorting the

05:09 processes list by CPU is therefore a bit

05:11 like investigating every crime by

05:13 questioning the tallest person in the

05:14 room. Occasionally, you'll get lucky,

05:16 but you've confused something that's

05:18 easy to notice with something that's

05:20 actually relevant.

05:23 Storage also gives us another kind of

05:25 problem because sometimes the disc isn't

05:27 slow at all. It's simply full. We've all

05:29 encountered this type of machine.

05:31 There's a terabyte of storage in it, but

05:33 the operating system reports 12 GB free

05:35 and the owner looks at you as though the

05:36 other 988 gigabytes must have been

05:39 stolen in the middle of the night. The

05:40 problem is pretty classic. You're cheap,

05:42 so you buy like a Mac with one terabyte

05:44 and pretty soon you're looking at 980

05:47 gigabytes used. And why there are only

05:49 20 gigabytes free, you have no idea. but

05:51 it's not your files as far as you can

05:53 tell and you need to sort it out and

05:54 find them. And so that's why T-Mog Pro

05:57 has the disk space wizard built in. Let

06:00 it run until it's accumulated some data

06:02 and then don't just start with a theory

06:03 about where the space went. You can

06:05 follow the big region down

06:08 and there it is. We've done essentially

06:09 the same thing we did with CPU and

06:11 memory. We start with a symptom and keep

06:13 following the evidence until the answer

06:14 appears. And if you were ever the sort

06:17 of person who could sit around and watch

06:18 the Windows disc def fragmenter for

06:20 entertainment back in the 1990s, then

06:22 first of all, you're not alone. And

06:23 second, I suspect you'll enjoy block

06:25 scanning mode rather more than a healthy

06:27 person should. And so CPU tells me who's

06:30 computing. Memory tells me where the

06:32 pressure is. Disc activity tells me

06:34 where we're waiting, and disc space

06:36 tells me where the bits actually went.

06:38 They're all different views of the same

06:39 machine. And what we're really trying to

06:41 do each time is taking a vague symptom

06:43 and turning it into evidence against the

06:45 original offender.

06:48 There's one more resource I want to look

06:50 at because laptop users tend to notice

06:52 it only when it disappears, and that's

06:53 battery life. My wife often complains

06:56 that her laptop battery doesn't last

06:58 nearly as long as it used to, and yet

06:59 the battery health meter still reports

07:01 95%. But if it's not the battery itself,

07:04 then what is it? Well, the most likely

07:06 answer is that the computer is simply

07:07 consuming more power than it used to for

07:09 some reason. There's the CPU load, and

07:12 as the computation increases, we can see

07:14 power consumption rising with it. A

07:16 moment later, the temperature begins to

07:18 follow, sure enough, and eventually the

07:19 cooling system has to respond because

07:21 all of that energy has to go somewhere.

07:23 On a laptop, every one of those watts

07:26 ultimately come out of the battery. So,

07:27 saying that a program uses a lot of CPU

07:29 is only one description of what's

07:31 happening. It's consuming power. It's

07:32 producing heat and it's potentially

07:34 making noise. And it's shortening the

07:36 battery life. And if the cooling system

07:38 can't eventually remove the heat quickly

07:40 enough, then the processor may

07:42 eventually throttle itself, which means

07:44 the machine can become slower precisely

07:46 because it's been working so hard. Once

07:49 we correlate these measurements in time,

07:51 the graph stop being separate numbers

07:53 and the machine starts to tell us a

07:54 story. Here's an example I experienced

07:57 on my own machine, a Ryzen AI 395 Plus

07:59 Pro. I would get good CPU PF unless the

08:02 GPU was busy. And I would get decent GPU

08:05 PF unless the CPU was busy. They should

08:07 largely be independent, but they were

08:09 not at all. And I couldn't figure out

08:11 why. But while watching the power meters

08:13 in T-Mobile, I noticed something

08:15 interesting. A full CPU load would could

08:17 use about 120 watts of chipset load. And

08:20 a full GPU load would pull about 130

08:22 watts. But when run together, they only

08:24 pulled 160, not 250. The machine wasn't

08:27 CPUbound or GPUbound or even thermally

08:30 throttled. It was limited on power

08:32 budget. And without the T-Mog beers, I

08:34 might never have caught that. Now,

08:36 there's just one serious flaw in

08:38 everything we've done so far. We happen

08:40 to be watching when it happened.

08:44 If you've ever been the designated

08:45 computer person for your family, you've

08:47 received some version of the call where

08:49 somebody tells you that their computer

08:51 completely froze this afternoon. But by

08:53 the time you get there, the CPU is back

08:55 at 3%, the fan is long since spun down,

08:57 and the disc is idle, and whatever

08:59 process ruined their entire afternoon is

09:01 probably sitting innocently in the

09:02 desktop tray, pretending it has never

09:04 done anything wrong in its life.

09:06 Traditional task managers are rather

09:08 like detectives who are only allowed to

09:09 investigate crimes while they're

09:11 actively taking place. And that's why I

09:14 added flight recorder to T-Mog Pro. I'm

09:17 going to create one more performance

09:18 problem, let it happen, and deliberately

09:20 wait until the computer has returned

09:22 completely to normal. And there you go.

09:24 The crime has been committed. The

09:25 suspect has already fled. And if I open

09:28 an imaginary task manager right now, I'd

09:29 be looking at a perfectly healthy

09:31 computer. But T-Mog remembers. There's

09:34 the event.

09:36 Here's where the little CPU burst

09:37 happened. Power follows it. A little

09:40 later, the temperature starts climbing.

09:41 And here's the disc activity joining in

09:43 as well. Instead of reconstructing the

09:45 event from somebody's recollection that

09:47 the fan sounded funny around lunch,

09:49 we're looking what the machine actually

09:50 reported at the time. And that to me is

09:53 the difference between merely monitoring

09:55 a computer and having a flight recorder

09:56 for it. Because I can save that trace. a

09:59 transient problem can become something

10:00 that I can send to somebody else and

10:02 have them investigate it later rather

10:05 than something I have to sit around

10:06 hoping will happen while I'm looking.

10:08 The same trace format works across T-Mog

10:11 on Windows, Mac, and Linux. So, the

10:12 evidence doesn't even have to remain

10:13 trapped on that machine that you

10:15 produced it on. And you can likely feed

10:17 the log file to your favorite AI for

10:19 diagnosis. Of course, if we're going to

10:21 diagnose computers from recorded

10:22 telemetry, we have to be able to trust

10:24 that telemetry. And that leads to a

10:26 couple of small engineering details that

10:27 I think matter more than they first

10:29 appear.

10:32 Suppose the temperature sensor

10:34 disappears temporarily. I could just

10:36 graph zero, which would make the chart

10:38 look nice and continuous. But zero is a

10:40 measurement and unavailable is not. If

10:43 the CPU temperature sensor stops

10:45 reporting, plotting 0 degrees would

10:47 imply that your processor has suddenly

10:48 been cryogenically preserved, which

10:50 would certainly solve our thermal

10:52 problems, but probably deserves some

10:53 investigation. So T-mog leaves a gap

10:56 where it doesn't actually have a

10:58 measurement. I'd rather put a hole in

10:59 the graph than lie to you with a

11:01 straight line. There's a similarly

11:03 obscure problem hiding in the process

11:05 list. Operating systems identify

11:07 processes using a process ID or a PID,

11:10 but PIDs get recycled. Think of a PID

11:12 more like a hotel room number. Bob might

11:15 be in room 412 today checking out in the

11:17 morning, but by tomorrow afternoon,

11:19 Alice is in 412. If I tell the front

11:21 desk to deliver Bob's package to whoever

11:23 just happens to be in room 412, then

11:26 Alice is about to receive a very

11:28 confusing package. So T-Mog doesn't

11:30 treat the pit alone as the permanent

11:32 identity when performing actions. It

11:34 pairs it with a process creation

11:35 identity. So the thing that we're acting

11:37 upon is still the thing we think it is.

11:40 Now, these aren't glamorous features. I

11:42 get it. But they're the kind of details

11:43 that you start caring about when you're

11:45 trying to build precision

11:46 instrumentation rather than merely a

11:48 dashboard. There's one final version of

11:50 my computer is slow that we haven't

11:52 dealt with yet because sometimes the

11:53 real question isn't what the machine is

11:55 doing. It's whether the machine is

11:57 performing as well as it should.

12:01 Slow is ultimately a comparison. Maybe

12:04 we're comparing this machine to another

12:05 computer. Or maybe we're comparing it to

12:06 when we first bought it. Or more

12:08 interestingly, we're comparing it to

12:10 itself 6 months ago. Maybe we change the

12:12 BIOS setting, replace the SSD, install a

12:15 new cooler, or discover that the heat

12:16 sink contains enough dust to be

12:17 considered a federally protected

12:19 ecosystem. What we need in that case is

12:21 a repeatable measurement, which is why

12:23 T-Mobile Pro includes its own benchmark

12:25 suite. Now, this computer is the

12:27 baseline for other computers because its

12:29 score is what's at the 100 for the T-Mog

12:32 score on the Mac side, but I'm also

12:35 video recording and streaming and doing

12:36 some other stuff. So, it should score

12:38 still in the high 90s if I fixed

12:40 everything. And when the test results

12:42 are finished, T-Mog combines the results

12:44 into a T-mog score.

12:51 Hey, hey, hey, hey, hey, hey, hey, hey,

12:58 hey, hey,

13:00 hey.

13:08 >> Now the notion that this computer feels

13:10 fast has become something that we can

13:11 actually compare. I can compare two

13:14 computers. compare the same machine

13:15 before and after a hardware change or

13:18 compare the computer that I have today

13:20 with the same computer when I knew it

13:22 was behaving properly. If the score

13:24 changes materially, that's evidence that

13:26 something has changed with it. The score

13:28 isn't intended to replace understanding

13:30 the machine. It's just another clue, and

13:32 clues are really what all of these tools

13:34 have in common. Now, it's also why I

13:36 wanted T-Mobile itself be measurable.

13:38 And there it is. T-Mog monitoring T-Mog.

13:41 Now, there's reasons it doesn't show up

13:42 by default, but I still think that every

13:44 system monitor should be willing to

13:45 submit to being system monitored because

13:48 otherwise it's rather like your

13:49 accountant refusing to show you the

13:51 invoice. However, it's CPU needs should

13:53 be modest. T-Mog uses a shared C++

13:56 measuring core and the applications

13:57 themselves are all fully native on

13:59 Windows, Mac, and Linux. There's no

14:01 browser pretending to be a task manager

14:03 because the last thing I want my task

14:04 manager discover is that my task manager

14:07 is the problem. And because I am

14:09 apparently constitutionally incapable of

14:11 designing a computer instrument that

14:13 does not eventually look as though it

14:14 belongs in NORAD circa 1983, there's

14:17 also a completely unnecessary but rather

14:19 entertaining amount of appearance

14:20 customization available. And true, none

14:23 of this will make your CPU any faster,

14:25 but neither will alloy wheels get you to

14:26 the grocery store any sooner. Some

14:28 things are simply allowed to be cool.

14:31 More importantly, you don't need to buy

14:32 anything to find out whether any of this

14:34 is useful to you. There's a free version

14:36 at t-mog.org And that's deliberately

14:38 where I would suggest you start.

14:40 Download it, point it at your own

14:41 computer, and leave it open while you do

14:42 whatever it is that you do. Start a

14:45 compile, copy a giant file, launch a

14:47 game, or open 50 browser tabs if that's

14:49 how you've chosen to live your life, and

14:51 see if it tells you something about the

14:52 machine sitting in front of you that you

14:53 did not know before. The pro version

14:56 adds the deeper diagnostic tools we've

14:58 explored today, including the flight

14:59 recorder, disc space, benchmarks, and so

15:01 on. But I'd much rather you try the free

15:03 version first and discover why you want

15:05 the rest than have me spend an episode

15:07 trying to convince you to do that today.

15:09 Oh, and by the way, we're still working

15:10 on getting our digital signature from

15:12 Microsoft Azure. So until then, you

15:14 might have to argue with Smart Screen

15:16 and Defender to convince them to let you

15:17 install it. But trust me on this one,

15:20 cuz your computer is always doing

15:21 something and for 30 years, task

15:23 managers have been pretty good at

15:24 showing you what. What I've become much

15:26 more interested in is the why. The

15:29 questions go in the comments and we pick

15:30 the best ones every Friday on Shop Talk.

15:32 If today's episode was useful, a like

15:34 and a subscribe help a lot more than you

15:36 might think. And if you like T-Mog,

15:38 please give it a share somewhere. In the

15:40 meantime, and in between time, hope to

15:42 see you next time right here in Dave's

