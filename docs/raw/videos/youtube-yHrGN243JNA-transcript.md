---
source_url: https://www.youtube.com/watch?v=yHrGN243JNA
source_type: video
ingested: 2026-08-24
published: 2026-08-24
duration_minutes: 13
language: en
sha256: eec7422259751db8bd5dc84abc1f5cf75e481473a60584aa5aaea8aee0a01824
time_sensitive: True
---

# YouTube Transcript: Desktop AI Compared - From 2GB to 1024GB, Deepseek R1, Gemma3, and More!

## Video Information
- **Title**: Desktop AI Compared - From 2GB to 1024GB, Deepseek R1, Gemma3, and More!
- **Video ID**: yHrGN243JNA
- **Published**: Unknown
- **Views**: Unknown
- **Language**: en

## Transcript
00:00 Hey, I'm Dave. Welcome to my shop.

00:02 Today, we're going to look at running a

00:04 large range of AI models entirely at

00:06 home, right on your own desktop. But

00:08 once you leave the cloud behind, you

00:10 become entirely dependent on your own

00:12 hardware. And it's sometimes hard to

00:13 know how much is enough. And that's the

00:15 question we're going to answer today. At

00:17 each of the price points, we'll increase

00:19 the amount of AI memory available at

00:20 each step, starting with only 2 GB until

00:23 we test out systems with 512 GB of

00:25 memory and even a full terabyte of RAM.

00:28 And at each step along the way, I'll

00:29 show you what's possible with it and how

00:31 fast it is or isn't. Now, there's a

00:33 persistent myth out there that you need

00:35 gobs of RAM to do anything with AI. But

00:37 I'm going to start out by showing you

00:38 that this is not always the case. It's

00:40 much smarter and more effective to let

00:42 your actual needs drive your hardware

00:44 spec. So, instead of buying a GPU and

00:47 then finding out later what it's

00:48 possible to do with it, let's just dive

00:50 right in and see what we can do at the

00:51 various memory sizes. Down at the

00:54 smallest end of the spectrum, you'll

00:55 find devices intended for edge

00:57 computing, like the Jetson Orura Nano

00:59 that I reviewed a few months back. It's

01:01 a tiny board about the size of a

01:02 Raspberry Pi, but it features a complete

01:04 CUDA capable Nvidia GPU backed with 2 GB

01:08 of RAM. That's the same amount of RAM

01:10 you'd find in a GeForce 710 card that

01:12 you can grab today on Amazon for 54

01:14 bucks and run Kudo on that. So either

01:17 way, it's a pretty small investment.

01:19 Now, 2 GB of RAM may not sound like a

01:21 lot, and it isn't by most measures. But

01:23 if the model you're trying to run fits

01:25 into the available memory, that's 90% of

01:27 the battle. And for simpler tasks, the

01:29 models can actually be quite small. For

01:31 example, the DeepQ model that I used in

01:33 my Tempest Arcade AI project, watch the

01:36 channel for that one coming soon, has

01:37 just under 100,000 total parameters, and

01:40 so it could run in only a few hundred K

01:42 of memory. That means it fits and runs

01:44 easily even on the 2 GB Nano. I've also

01:47 used the Nano for AI vision tasks such

01:48 as using the YOLO library to do license

01:51 plate recognition on my security

01:52 cameras. Not only did the model fit

01:54 nicely into the memory, but performance

01:56 was completely acceptable for the task

01:58 that I was performing as it could still

02:00 process several frames per second of

02:02 visual inference. And that's the key.

02:04 You want the most affordable piece of

02:05 hardware that has both the capacity to

02:07 hold the models that you're interested

02:09 in combined with the performance needed

02:11 to run them at a rate that you can live

02:12 with. In the Tempest case, I could at

02:14 least in theory do all of my training on

02:16 the Orin Nano, but it runs about 10

02:18 times slower at least than the RTX 6000

02:20 ADA cards in the Thread Ripper, a setup

02:22 that we'll check out soon enough. So, in

02:25 my case, while the Orin Nano had the

02:26 capacity, it lacked the required

02:28 performance. And in each of our cases,

02:30 I'll show you what each increasingly

02:31 large system has the capacity for, show

02:34 it to you in action, and then you can

02:35 decide on the price point that meets

02:37 your needs. Because when it comes to AI,

02:39 speed costs money, kid. how fast you

02:41 want to go. To run and test each of

02:43 these models, we'll be using Olama, an

02:45 application that allows you to run AI

02:47 models entirely locally. We'll start by

02:50 going to ola.com and then clicking on

02:52 the install link for our operating

02:53 system. Once the installation has

02:55 completed, it will add itself to the

02:57 command line, launch the server in the

02:58 background, and we'll be able to run our

03:00 AI. To do so, we have to next download a

03:03 model. And the Alama site has a rich

03:05 repository of models to select from, as

03:07 well as some surprisingly fast download

03:09 speeds. We simply head to olama.com.

03:12 Select a model that will fit into our

03:13 hardware and download it. With only 2 GB

03:16 of RAM to get started with, we'll need

03:17 to start with one of the smallest

03:19 models. And it looks like the Gemma 3

03:21 model with 1 billion parameters is about

03:23 815 MGB in size. So, it should work

03:26 nicely for our purposes. To actually

03:28 install the model, I simply type ola

03:30 pull and then the name of the model

03:32 including its size after the colon. So,

03:34 I'm specific. And so my complete command

03:36 line is Olama pull Gemma 3 col 1B.

03:40 Depending on your internet connection

03:42 will take anywhere from a few seconds to

03:43 a couple of minutes to download the

03:45 model. And once it does, you can run it

03:47 with the command line Olama run gemma 3

03:50 col 1B. I like to add the verbose flag

03:52 to my command line to get a sense of the

03:54 raw performance when evaluating a model.

03:56 And so I'll do that here as well today.

03:58 Now, I'm not going to be overly

04:00 concerned with the actual text quality

04:01 of the model output as there are dozens

04:03 of models to select from and the one you

04:05 pick will be chosen first by what fits

04:07 in memory and second by the capabilities

04:09 of the model. But those will vary wildly

04:11 and there's no simple score I can give

04:13 you for each and nobody agrees on what

04:15 those scores should be or how to test

04:16 them. Plus, the models are constantly

04:18 changing and evolving. So, my

04:19 recommendation is to keep an eye open on

04:21 the Lama site for the popularity

04:23 leaderboard. Odds are the model you want

04:25 for general use will be among the more

04:27 popular. Once O Lama has loaded and

04:30 initialized your model, you're ready to

04:31 go. And speaking of ready to go, my

04:33 subscriber count is poised to crack 1

04:35 million. As you likely know, I'm mostly

04:37 in this for the subs and likes. So, with

04:39 just a few more subs, I'll be a

04:41 millionaire. Either way, I'd be honored

04:43 if you'd take a moment to subscribe to

04:44 the channel and help me push over that

04:46 hump. Back to our model. Let's just ask

04:48 it to tell us a story. That will give us

04:50 some sense of how verbose the model is

04:52 and what rate it can generate tokens as

04:54 long as you remember to specify the

04:56 verbose flag. Now, as with all cases

04:58 here, I'll first let you see the model

04:59 generating tokens at its actual speed on

05:02 the very hardware that we're testing on.

05:03 And then I'll speed up the footage to

05:05 let it complete so that we can get to

05:07 the end without waiting around on a

05:08 geological time scale for some of the

05:10 more demanding models to finish. And

05:12 when Gemma 31B cranks out our answer, we

05:14 can see that it did so at a rate of

05:16 almost 30 tokens per second, which is

05:18 pretty darn fast and certainly fast

05:20 enough to be useful as long as the 1

05:21 billion model can do the work you need.

05:24 If I showed this to you 5 years ago on

05:25 50 bucks worth of hardware, it would

05:27 have blown your mind. So, at least keep

05:28 that in perspective. And next, let's

05:30 upgrade that perspective a little bit by

05:32 moving up in RAM capacity. I'm going to

05:34 jump up to the 8 gigabyte level as

05:36 that's a very common capacity level in

05:38 consumer GPUs, something many of you

05:39 already have on hand for other purposes.

05:42 To do so, I'm going to turn to the Tesla

05:44 P40 card in our 45 Sto because, as

05:47 you'll learn soon enough in a

05:48 forthcoming episode, as long as you're

05:49 subscribed, of course, we recently

05:51 upgraded the Storinator Q30 to an epic

05:53 CPU with a terabyte of conventional RAM.

05:56 And that's not even considering its 420

05:58 tab of disc storage. The P40 was a

06:01 mid-level server GPU that fit in a

06:03 single slot, and it doesn't even have

06:04 any HDMI outputs, so it's strictly for

06:07 server use. That does make it handy for

06:09 AI workloads, and it features 8 GB of

06:11 video RAM and has CUDA support. Now, the

06:14 model I wanted to try was the same Gemma

06:16 3, but this time in a 12 billion

06:17 parameter variant. It was listed as

06:19 requiring 8.1 GB of GPU space, so I

06:22 wasn't actually sure if it would

06:23 technically fit in 8 GB or not, so the

06:26 only way to find out was to try. And the

06:28 P40 brought a mix of good news, bad

06:30 news. The good news is that it was able

06:32 to squeeze the model into memory and it

06:34 ran. The bad news is that it ran really

06:36 slow. The P40 just doesn't have the

06:38 chops to run this model at what I would

06:39 call live speeds. I want the model to

06:42 produce text at least as fast as I can

06:44 read or otherwise you wind up waiting on

06:46 it. And the P40 could barely muster two

06:48 tokens per second. That started to worry

06:50 me as the models we're going to try

06:51 today are only going to get larger and

06:53 larger. Once we move to GPUs with more

06:55 memory, the models will be more

06:57 complicated. And will the processing

06:58 horsepower keep up with the storage

07:00 capacity? Well, again, there's only one

07:02 way to find out, and that's to bust out

07:04 the Thread Ripper. You see, Dell had

07:05 graciously loan me a really nice

07:07 workstation for a while. So nice, in

07:09 fact, that it had the top-of-the-line 96

07:11 core Thread Ripper and not one, but two

07:13 RTX 608 GPUs, each sporting 48 GB of GPU

07:17 memory for a total combined 96 GB of GPU

07:21 memory. But at some point it had to go

07:22 back and it did so early this year. Then

07:25 I started working on the Tempest AI

07:26 project which we'll feature in upcoming

07:28 episodes and I needed something with

07:30 more inference horsepower. I mentioned

07:32 this to Dell and they sent the machine

07:34 back to me. So I let it take a break

07:36 from doing Tempest training large enough

07:37 to do some large language model work.

07:40 Even though this machine technically has

07:41 96 GB of GPU memory, you're not going to

07:44 be able to just naively load a 96 GB

07:46 monolithic model. That's because memory

07:49 is spread across those two GPUs and by

07:51 default will only be able to use a

07:53 single unit. Now, you could split the

07:55 model into layers perhaps and run each

07:57 layer on a different GPU, but that's a

07:59 lot of work and we want to fairly

08:01 compare how things work out of the box.

08:02 And so, for that reason, we're

08:04 constrained to using a single GPU only.

08:07 Now, depending on who you ask, the RTX

08:09 680 units are somewhere between the 4090

08:11 and the 5090 in performance, probably

08:14 closer to the 4090. Its main claim to

08:16 fame in the AI world, however, is the

08:18 much larger memory capacity than you'd

08:19 find on either of those consumer GPUs.

08:22 And so I went looking for the biggest

08:23 model I could fit into 48 gigabytes. And

08:25 I found it in the Deepseek R170 billion

08:28 parameter variant. Weighing in at 43 GB,

08:31 it's a substantial download. Now, I'm

08:34 fortunate to be on 5 GB fiber, so it

08:36 goes pretty quickly, which is a

08:37 testament to the bandwidth that the Lama

08:39 model hosting must have. It's like steam

08:41 in its ability to saturate your download

08:43 pipe. Once a download is complete, it

08:46 will run through an MD5 hash check to

08:47 make sure the model is intact and

08:49 unmodified, and then it will launch. The

08:52 first load takes some time, especially

08:53 on these larger models. After all,

08:56 loading 40 GB from a fast SSD is still

08:58 going to take 10 seconds or so, no

09:00 matter what, so a bit of waiting is

09:01 going to be inevitable. Once the models

09:04 loaded, however, I was very pleasantly

09:06 surprised by the performance. It

09:08 produced results at what I'd call a fast

09:09 reading pace, about 20 tokens per

09:11 second. That's enough to keep me busy as

09:13 it's producing its answer and it's fast

09:15 enough to be hooked up to something like

09:16 Visual Studio for local AI assisted

09:19 development. Now, stepping up to the

09:20 next level at 128 GB meant that unless

09:23 somebody's going to loan me an Nvidia

09:25 B200, we're going to have to leave

09:26 dedicated GPUs behind and move up to

09:28 unified memory of the kind that you'd

09:30 find in a modern Apple machine or a

09:32 Windows Ryzen desktop with integrated

09:34 graphics. And since I'm fortunate to

09:36 have a 120 GB M2 Mac Pro on hand as my

09:39 main machine, it made perfect sense to

09:41 run that same model DeepS R170B on the

09:45 Mac to compare to how it tests on the

09:46 Nvidia. And so that's precisely what I

09:49 did. Downloading, installing the model

09:51 is the same, of course. And then I just

09:52 asked the model the same prompt, tell me

09:54 a story. And as soon as I did, I was

09:56 greeted with an experience very similar

09:58 to what I'd seen on the Nvidia RTX 6000.

10:01 The text was flowing at a comfortable

10:03 reading rate, though perhaps not quite

10:04 as fast as the prior test. I wasn't sure

10:06 yet. But when I saw the numbers, they

10:08 fell into line with my expectations, 12

10:10 tokens per second. It's still fast

10:13 enough for live use and production

10:14 coding, but slower than what we saw with

10:16 the Nvidia GPUs. But to go even larger,

10:19 we'd need bigger hardware. Hardware I

10:21 don't own. Hardware that nobody has

10:23 offered to loan me or would have been in

10:24 this episode. But then I got a

10:26 serendipitous email from a fellow named

10:28 Riff. He said that he was a developer

10:30 who works in fintech and a Google

10:32 developer expert and that he had access

10:33 to a 512 GB Mac M4. He was willing to

10:37 let me use the machine remotely and so

10:39 we set up Tailscale and soon enough I

10:41 was able to use Apple screen sharing to

10:43 connect directly to the desktop on the

10:45 other side of the world. Now I figured

10:47 Riff is a Google evangelist so he'd

10:49 probably like it if I started with a

10:50 Google model. So I picked the largest of

10:52 the Gemma 3 models coming in at 27

10:54 billion parameters. At 17 GB, that makes

10:57 it too large to run on all but the

10:59 largest consumer GPUs, but it should run

11:01 easily on the max unified memory

11:03 architecture. So, I gave it a quick

11:05 download and test using the same prompt

11:07 as always. And I'd say that the 27

11:09 billion parameter Gemma 3 on the Mac is

11:11 about the sweet spot as it's a very

11:13 capable model and was able to generate

11:16 more than 23 tokens per second, more

11:18 than enough for live desktop use. It's

11:20 also rather unique in that it supports a

11:22 massive context window of up to 128,000

11:25 tokens. So, our tell me a story prompt

11:28 certainly doesn't even scratch the

11:29 surface, but you could upload a huge

11:31 amount of rag context with your query.

11:34 But we were on a big Mac for one primary

11:36 reason, to run the largest model we

11:38 could find. And for the last several

11:39 months, that has remained Deepseek R1's

11:42 original, coming in at 671 billion

11:44 parameters and requiring a whopping 404

11:48 GB of GPU accessible memory just to load

11:50 it. But on paper, we had the hardware

11:52 for it, so I spun it up and gave it a

11:54 shot. Now, as a little side quest, the

11:56 45 Sto has a full terabyte of RAM, or

12:00 1,024 GB. It's not GPU accessible

12:03 memory, but you can run a Lama on just

12:05 the CPU if the model won't fit into GPU

12:08 memory. So, I figured I'd give that a

12:09 try as well. And I was able to load the

12:12 massive model with ease, but its

12:13 performance was uh wanting. It was about

12:16 three tokens per second, sometimes two,

12:18 and this is on the epic CPU. Too slow to

12:21 do anything live with. But now, we could

12:23 bring the GPU to the table. And doing so

12:25 brought us firmly into the realm of

12:26 things like a dog playing the piano.

12:28 Something that it's impressive that it

12:29 can do it all, regardless of how well it

12:31 actually does it. And while it's

12:33 impressive that the 512 GB Mac M4 can

12:36 run the model at all, it can still only

12:38 do so at about six tokens per second.

12:40 Now granted, that's more than twice as

12:42 fast as the good CPU, but I was hoping

12:44 for a little more. But it looks like

12:46 live performance with the largest of the

12:48 models require hardware akin to that

12:50 B200 or the forthcoming DGX station.

12:52 Neither of which I have, but you never

12:54 know, maybe one day. If you enjoyed

12:56 today's look at the very large language

12:58 models, please consider subscribing to

13:00 the channel for more like it. And if you

13:01 could drop a like on the video to make

13:03 the algorithm happy, I'd appreciate it.

13:05 I'm always eager to hear your comments

13:06 and questions, and every Friday on

13:08 Dave's Attic, we go through the best of

13:09 them on Shop Talk. I'll put a link in

13:11 the video description for you and

13:13 encourage you to check it out. Thanks

13:14 for joining me out here in the shop

13:16 today. In the meantime, and in between

13:17 time, I hope to see you next time right

13:19 here in Dave's Garage. Do it, Lyn. Do

13:22 it. Do it.

