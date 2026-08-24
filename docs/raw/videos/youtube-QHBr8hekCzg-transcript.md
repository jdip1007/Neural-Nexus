---
source_url: https://www.youtube.com/watch?v=QHBr8hekCzg
source_type: video
ingested: 2026-08-24
published: 2026-08-24
duration_minutes: 13
language: en
sha256: 6f4e2bff4e919bb47629ba2d74f4686cef5917a8d5401487e722336fc06b75e6
time_sensitive: True
---

# YouTube Transcript: NVIDIA's $249 Secret Weapon for Edge AI - Jetson Orin Nano Super: Driveway Monitor

## Video Information
- **Title**: NVIDIA's $249 Secret Weapon for Edge AI - Jetson Orin Nano Super: Driveway Monitor
- **Video ID**: QHBr8hekCzg
- **Published**: Unknown
- **Views**: Unknown
- **Language**: en

## Transcript
00:00 hey I'm Dave welcome to my shop we're

00:02 going to be living on the edge literally

00:04 today with a brand new Jetson Ora Nano a

00:06 single board CPU a six arm cores and

00:09 1024 Cuda cores it's a pint-sized

00:12 Powerhouse that is quite unlike the

00:13 desktops or raspberry pies that you

00:15 might be more familiar with this episode

00:17 is sponsored by Nvidia a rare occurrence

00:19 for my channel but fret not Nvidia has

00:21 no editorial control here they just

00:24 FedEx me the Orin Nano developer kit to

00:25 Tinker with ahead of its release so

00:27 let's dive in and see what came in the

00:29 Box

00:30 all right let's have a look at what the

00:32 FED X-Man brought today open up the box

00:35 take out a bag of air not very exciting

00:37 but next to it we've got an or Nano

00:40 notice the SD card that was taped to the

00:42 back of the box I did not I had to fetch

00:45 that from the garbage later but for now

00:47 let's open it up and see what's inside

00:49 Kudos tovid on the packaging it's

00:51 actually pretty nice for a developer kit

00:53 you get a little pamphlet here that

00:55 tells you next to nothing you get a

00:56 charger which I will set aside and of

00:58 course you get the or a nano itself next

01:02 I'll pull the power cable out and that's

01:03 everything that's involved here let's

01:05 boot it up now when you think of Nvidia

01:08 chances are your mind jumps straight to

01:09 their gpus whether that's for gaming

01:11 machine learning or crunching numbers on

01:13 the world's most powerful supercomputer

01:15 clusters but what's a Jetson well Jetson

01:18 is nvidia's answer to Edge Ai and that's

01:20 all about bringing computational muscle

01:22 closer to where the action is actually

01:24 happening be it in robots drones cameras

01:26 or as we'll see today in my driveway

01:28 when you need your AI to be local and

01:30 you can't stop a big desktop to it Edge

01:32 Computing like the Orin Nano is the

01:34 solution the Jetson Orin Nano fits into

01:36 a particular but an interesting Niche it

01:39 looks a little bit like a Raspberry Pi

01:40 on steroids a compact form factor but

01:43 with far greater performance under the

01:44 hood and that's not hyperbole it boasts

01:47 the GPU with 1024 Nvidia Cuda cores

01:50 making it an ideal playground for AI

01:52 experiments don't get me wrong this

01:54 isn't going to replace your desktop for

01:56 high performance gaming or anything like

01:57 that but for the price it's an

01:59 incredible little platform to explore

02:01 what AI can do without selling your soul

02:03 or your GPU budget and I'm pleased to

02:05 report that they've slashed the price

02:07 down to $2.49 which is pretty impressive

02:09 for a machine with as I said 1,24 Cuda

02:11 cores 8 GB of RAM and six arm cores I'll

02:14 confess that my first adventures with

02:16 the Orin Nano were anything but cutting

02:18 Aji they had actually included a

02:20 bootable micro SD card with the Orin but

02:22 I didn't see it taped to the side of the

02:24 box and that means I went through the

02:26 whole mundane process of downloading the

02:28 SD card image from nvidia's website

02:30 fidgeting with the tiniest micro SD card

02:32 slot that I've ever seen and eventually

02:34 booting into auntu Linux if there's a

02:36 golden rule of developer boards this

02:38 your patience is tested long before your

02:40 programming skills over are I spent far

02:43 too long poking around and prodding at

02:44 the MicroSD Port but once that hurdle

02:47 was cleared it was smooth sailing

02:49 fortunately it's not something you have

02:50 to do very often so otherwise it might

02:52 be a concern one thing I should mention

02:54 I added a 1 tbte Samsung 970 Evo SSD to

02:58 give the oron Nano a bit of breathing

02:59 room room now during the initial Ubuntu

03:01 setup it defaulted to installing the

03:03 operating system on the micro SD card

03:05 instead of the SSD not ideal after some

03:08 tinkering I cloned the system from the

03:09 SD card onto the SSD using Linux command

03:12 line tools like DD EF CK and resized to

03:16 FS to make everything fit and with that

03:18 the system was now booting off the SSD

03:20 and the performance was definitely night

03:21 and day in terms of disc it's worth the

03:23 effort if you're planning to do anything

03:24 intensive with it I even repeated the

03:26 setup to confirm that I wasn't given a

03:28 choice of install Drive which I still

03:29 find odd now what makes the oron Nano

03:32 particularly intriguing is its support

03:33 for nvidia's AI ecosystem including

03:35 tensor RT Cuda and a host of pre-trained

03:38 models that makes it a solid candidate

03:40 for AI enthusiasts like me who might not

03:42 be ready to train their own GPT model

03:44 from scratch but still want to dabble in

03:46 the technology that powers things like

03:47 Tesla's self-driving cars or Amazon's

03:50 new Alexa with that in mind I decided to

03:53 put the or n to work on a simple yet

03:55 practical AI application a driveway

03:57 monitor and this isn't your

03:58 run-of-the-mill beam detect

04:00 now this is a custom python script that

04:01 uses a YOLO V8 object detection model to

04:04 identify Vehicles entering and leaving

04:06 my driveway the goal to teach the Jetson

04:09 not just to detect motion but to

04:11 understand what it's seeing and to

04:12 notify me accordingly the script is

04:14 where the magic happens at its core it

04:16 uses the ultral litic YOLO Library

04:18 running directly on the GPU to analyze

04:21 video frames from my security camera

04:22 feed in real time YOLO or you only look

04:26 once is an object detection model that

04:28 true to its name analyze izes an entire

04:30 frame in a single pass making it

04:32 extremely fast and speed does matter

04:34 when you're dealing with live video

04:35 streams so let's break the script down

04:38 the script initializes the YOLO model

04:40 and configures it to run on the oron

04:41 Nano's GPU this isn't just about speed

04:44 it's about maximizing this Hardware's

04:46 potential and here's the kicker YOLO

04:48 comes pre-trained on a massive data set

04:50 so right out of the box it already knows

04:52 how to recognize cars trucks buses and

04:54 more my job was to narrow its focus to

04:56 vehicles and tweak confidence thresholds

04:58 to avoid any false positives after all I

05:01 don't want it mistaking my dog for a

05:02 Corvette the script also includes a

05:04 rudimentary tracking system to keep tabs

05:06 on individual vehicles I calculate the

05:09 overlap between deducted bounding boxes

05:11 to decide whether an object is new or

05:13 just the same car moving around that way

05:15 it doesn't show vehicle arriving every

05:17 time somebody nudges their car forward a

05:18 few inches and here's the fun part the

05:20 system doesn't just detect the vehicles

05:22 it notifies me over the intercom using

05:24 text to speech modules if a car pulls up

05:27 it announces vehicle arriving if it

05:29 leaves I vehicle leaving might seem like

05:31 a gimmick but it's been surprisingly

05:32 effective out here in the shop the key

05:34 is keeping the announcements infrequent

05:36 enough that they don't turn into

05:37 background noise in the final setup the

05:40 script processes video frames at a few

05:42 frames per second on the Orin but that's

05:43 fast enough for my purposes and the oron

05:46 Nano barely breaks a sweat doing it the

05:48 tracking system also assigns unique IDs

05:50 to vehicles and keeps a history of their

05:52 movements over time I could extend this

05:54 to include more advanced analytics say

05:56 recognizing specific cars or who might

05:58 be driving them or alerting when an

06:00 unknowing vehicle arrives the oron

06:02 Nano's architecture makes it possible to

06:04 handle all of this in real time it

06:06 offloads the heavy lifting like the

06:07 neural network inference to its caor

06:09 freeing up the CPU for other tasks it's

06:12 this seamless interplay between the

06:14 hardware and the software that sets the

06:15 Jetson apart from say a Raspberry Pi or

06:17 similar boards and because it's from

06:19 Nvidia it works with Cuda and working

06:21 with Cuda is almost a prerequisite for

06:23 doing AI these days now let's pivot to a

06:26 completely different AI use case for the

06:28 oron Nano butning large language models

06:30 locally with llama and the Llama 3.2

06:32 model if you've ever been fascinated by

06:35 how chat GPT like systems generate human

06:37 like responses you're going to love this

06:39 experiment the idea is just to see how

06:41 well the Orin Nano can handle processing

06:43 a massively large model locally no Cloud

06:46 involved and then compare its

06:47 performance to something like an M2 Mac

06:49 Pro Ultra to give the Orin a better shot

06:52 we're going to up its power to the nmax

06:54 setting doing so it required that I

06:56 update the firmware from the Nvidia site

06:58 which I did and then the machine came

06:59 back up with the new nmax power setting

07:01 which I selected for maximum performance

07:03 now before we look at setting up AMA on

07:05 the Orin Nano let's take a quick look at

07:07 running it on the pi 4 first I used my

07:10 best pi4 an 8 gbyte model so it would

07:12 have the memory needed to even have a

07:14 chance at running the model and when I

07:16 ran it I found myself ambivalent in the

07:18 literal sense of the word because I was

07:20 of two minds about it first it was

07:21 incredibly impressive to me that a

07:23 Raspberry Pi can run a large language

07:25 model at all it's like when a dog plays

07:27 a piano it's not how well they do it

07:28 it's that they do do it at all and like

07:31 the dog playing the piano the pie does

07:33 it but not very well it runs at a speed

07:35 of about a to in a second so it's far

07:37 too slow to do anything responsive or

07:39 truly useful I'd say you're certainly

07:41 not going to have any kind of useful

07:43 back and forth conversation with it so

07:45 let's see if the oron Nano with the

07:46 cacor fares any better the first step in

07:49 this experiment was to install olama the

07:51 local platform for running llama models

07:54 olama simplifies the process of using

07:56 large language models on your local

07:57 Machine by providing a streamlined frame

07:59 workor for downloading and running these

08:00 models efficiently to install olama I

08:03 ran the script provided on the ama.com

08:05 homepage next I downloaded the Llama 3.2

08:08 model this model is one of the most

08:10 advanced open source large language

08:11 models available known for its high

08:13 accuracy and capability to generate

08:15 detailed coherent responses using ama's

08:19 CLI downloading the model was as

08:21 straightforward as AMA pull llama 3.2

08:24 and with the model installed I was ready

08:26 to test its performance on the auron

08:27 Nano to measure through put I used ama's

08:30 verbose mode this mode provides detailed

08:33 insights into the model's operations

08:35 like the metrics such as the tokens

08:36 generated per second GPU use and latency

08:39 per token these statistics help paint a

08:41 clearer picture of how the hardware

08:42 handles the Intensive AI workloads

08:44 offering valuable data points for

08:46 optimization and performance tuning the

08:48 specific tests involved asking llama 3.2

08:51 to generate a 500-word story based on a

08:53 simple prompt tell me a story about

08:55 robots that learn to paint the Orin Nano

08:58 tackled this task admirably particularly

09:00 given the challenge of running a model

09:01 as large and complex as llama 3.2

09:04 processing a large language model

09:06 locally requires not only substantial

09:08 computational power but also efficient

09:09 resource allocation the oron Nano's

09:12 Reliance on its CA cores and six arm CPU

09:14 cores demonstrated its optimized

09:16 architecture for AI workloads using all

09:18 six arm cores for CPU side operations

09:20 and offloading as much as possible to

09:22 its Cuda cores the system managed to

09:24 generate around 21 tokens per second

09:27 while this might not sound blazing fast

09:29 as compared to cloud gpus or the

09:31 high-end desktops it's important to

09:32 remember that this is a 15w device and

09:35 it's at least an order of magnitude

09:37 faster than the pi and then some the

09:39 verbose output showed steady token

09:41 generation with the GPU utilization

09:43 hovering around 60% the story itself was

09:46 rich and detailed and while the

09:47 processing time was longer than you'd

09:49 experience on a high-end workstation the

09:51 Orin Nano proved as more than capable of

09:53 running Cutting Edge language models in

09:56 the end those 20 tokens per second are

09:57 easily fast enough to make it responsive

09:59 enough for fluid text to speech

10:01 answering questions or using the model

10:03 to solve problems in real time for

10:05 comparison I ran the same test on an M2

10:08 Mac Pro Ultra and it's a fairly maxed

10:11 out machine as well with the maximum

10:12 number of GPU cores I think it's 76 in

10:15 the Mac world and as expected the Mac Go

10:17 perform the oron Nano by a factor of

10:19 about five generating tokens at an

10:21 impressive of 113 tokens per second this

10:24 performance is largely due to the m2's

10:26 unified memory architecture and highly

10:27 efficient neural engine both of which

10:29 which are optimized for handling AI

10:31 tasks the significant difference in

10:33 token generation speeds highlights the

10:34 disparity and computational power

10:36 between the two systems but also

10:37 underscores the efficiency of the Orin

10:39 Nano given its limitations however

10:42 what's fascinating is how close the Orin

10:43 Nano comes given its size and power

10:45 constraints the Mac Pro represents the

10:48 Pinnacle of Apple's desktop processing

10:49 power with its custom silicon optimized

10:51 for AI tasks it also cost more than

10:54 $10,000 the oron Nano on the other hand

10:57 is a $249 developer board designed for

10:59 Edge Computing despite this it holds its

11:01 own in a way that's nothing short of

11:03 remarkable now if you need even more

11:05 performance out of the system we can go

11:06 to a more compact version of llama 3.2

11:09 with only a billion parameters doing so

11:12 more than triple the speed to an

11:14 impressive 34 tokens per second a very

11:16 fast generation rate so why would you

11:19 use an Ora Nano instead of a more

11:20 powerful system well the answer lies in

11:22 its Niche Edge Computing applications

11:25 often prioritize low power consumption

11:27 compact form factors and low local

11:29 processing capabilities the oron Nano

11:31 can run AI models like llama 3.2 in

11:34 environments where a full-fledged

11:35 desktop or server isn't feasible think

11:37 of robots iot devices drones and that

11:40 sort of thing imagine embedding a

11:42 language model in a drone for natural

11:44 language processing as it's flying

11:46 allowing it to interact seamlessly with

11:47 the operators or other devices in real

11:49 time and so the Jets or Nano continues

11:52 to impress with its versatility and raw

11:53 performance for its size particularly

11:55 when compared to other Edge Computing

11:57 Solutions like a Raspberry Pi or the

11:59 Coral TPU its ability to seamlessly

12:01 integrate with nvidia's AI ecosystem

12:03 coupled with its low power consumption

12:05 and robust Hardware makes it an

12:07 exceptional choice for developers and

12:08 researchers looking to push the

12:09 boundaries of an AI budget the device

12:11 strikes a compelling balance between

12:13 cost performance and functionality I

12:15 think solidifying its place in the edge

12:17 AI landscape from driveway monitoring to

12:19 running large language models this

12:21 pint-sized AI Powerhouse proves that you

12:23 don't need a data center to do serious

12:25 AI work while the M2 Mac Ultra Pro May

12:28 dominate in Ross speed the oron Nano's

12:30 ability to run models like llama 3.2

12:32 locally and efficiently highlights just

12:34 how far Edge Computing has come if you

12:36 found today's little Nano adventure to

12:38 be any combination of informative or

12:40 entertaining remember that I'm mostly

12:42 eating this for the subs and likes so

12:43 I'd be honored if you consider

12:44 subscribing to my channel and leaving a

12:46 like on the video before you go today

12:48 and if you're already subscribed thank

12:49 you please consider turning on the

12:51 notifications Bell check out the free

12:53 sample of my book on Amazon Link in the

12:55 video description it's everything I know

12:57 now about living your best life on the

12:58 spectrum that I wish I'd know one long

13:00 ago thanks for joining me out here in

13:01 the shop today if you've got a moment

13:03 check out Dave's attic my second Channel

13:05 where Glenn and I do a podcast every

13:07 Friday and there are in about 12 back

13:09 episodes now that you can check out Link

13:10 in the video description in the meantime

13:13 and in between time I see you next time

13:15 right here in Dave's Garage subscribe

