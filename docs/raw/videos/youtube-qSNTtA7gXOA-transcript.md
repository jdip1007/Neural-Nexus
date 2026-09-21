---
source_url: https://www.youtube.com/watch?v=qSNTtA7gXOA
source_type: video
ingested: 2026-09-19
published: 2026-09-19
duration_minutes: 14
language: en
sha256: 2fb5a77f9618fd4eeae0f6021e79200ec6d3d477e1754bf0a45c085ed48c9076
time_sensitive: True
---

# YouTube Transcript: Inside a Massive 1980s Hard Drive: 14 Inches of Fury!

## Video Information
- **Title**: Inside a Massive 1980s Hard Drive: 14 Inches of Fury!
- **Video ID**: qSNTtA7gXOA
- **Published**: Unknown
- **Views**: Unknown
- **Language**: en

## Transcript
00:00 All right, I've got my PDP1 1144

00:02 basically up and running the way I want

00:03 it. Except it's all blown apart with

00:05 cables running everywhere. But before I

00:07 put it all back together, I thought I'd

00:08 show you what goes inside so you can see

00:10 what actually happens inside one of

00:12 these machines. But in order for you to

00:14 be able to hear me, we probably need to

00:15 turn this machine off. So we'll turn it

00:17 off and have a look inside.

00:21 Now, this is your main CPU case. This is

00:23 where all of the data processing and the

00:25 basic cards plug in at your main bus.

00:27 Can't really see down in there very

00:29 well, but there are actually slots which

00:31 are six tabs long and back two are

00:35 unibus front four are ABCD or is it

00:38 CDEF? I can never remember. We'll pull

00:41 one out here so we can have a look at

00:43 it. This is the math board. I want to be

00:44 very careful with it because they are

00:46 rare

00:47 especially in working condition.

00:54 So, here's the mathematics board or FPU

00:57 if you prefer. As you can see, it has a

01:00 ton of AMD 2901 bit slice. In fact, it

01:04 probably has 16, I would guess, 48. Yep,

01:06 16 of them. 16 bits. So, it actually

01:09 cascades bits from one chip to the next.

01:11 And it's just uh the same kind of binary

01:13 addition of mathematics that you learned

01:15 back in first year computer science.

01:17 Plus a whole bunch of TTL logic to drive

01:19 it that you would have learned in first

01:20 year electronics many years ago. But

01:22 even I don't know today.

01:31 When it comes time, you push these two

01:32 tabs down and it will seat the card down

01:34 into the bus. Let's have a look at uh

01:37 the cash board. What else have we got

01:40 here?

01:41 You got data path.

01:43 Each board does, you know, a function of

01:45 the CPU. This is just the cache board of

01:47 the CPU. It's, I believe, a 64k cache.

01:52 You can see it's just got a ton of

01:53 static RAM on it.

01:55 And it's got bypass switches to turn off

01:58 cache if you want to test it without

01:59 cache. And it is in fact about 30 to 40%

02:02 slower with the cache bypass. So, this

02:04 is a nice feature to have. I think it's

02:05 standard in the 44, but something you

02:07 don't want to run without.

02:13 Next, we have the Unibus interface board

02:15 here. And then we have 4 megabytes of

02:17 RAM. These would have been brutally

02:19 expensive in the 80s, if you could even

02:21 get them in the 80s. I'm not sure. This

02:22 is the maximum amount of RAM that can be

02:24 configured into a PDP11.

02:27 And we'll pull out one megabyte and have

02:29 a look.

02:31 Now, that is a lot of chips. And getting

02:34 four of these where every chip and every

02:35 parody chip and everything else works

02:37 perfectly is not an easy task. But I

02:39 managed to get four of them. So that's

02:41 how I managed to assemble 4 megabytes of

02:43 RAM. Each one will have a base address

02:45 and a CSR response address. You get to

02:48 set those on the pins. I'm not sure what

02:50 these big gold packages are, but I'm

02:51 sure they're important. These look like

02:53 static RAM, almost like it has its own

02:56 cache in front of it. I'm not certain.

02:57 Moving

03:05 right along. Next on the bus, we have an

03:07 Amux SCSI controller. You can see this

03:09 is a standard 50 pin SCSI connector

03:11 coming out. And I currently have it

03:12 connected to a Zulu SCSI board which has

03:15 an SD card in it which has a 32 GB SD

03:17 card which contains images of the

03:19 diagnostics of BSD of RT11 and RSX11. so

03:23 I can boot into any of the four or five

03:25 major operating systems as well as

03:27 diagnostics. Then when I get the machine

03:29 finally settled, I pull the uh modern

03:32 electronics entirely out and let it run

03:34 on its own. But during the debugging

03:35 process, it's much easier to boot and

03:37 repair images than it is to say boot and

03:40 repair a giant R81 that we'll look at

03:42 next.

03:45 Next up in the stack is a Unibus card,

03:48 which is called the Unibone. The

03:49 Unibone. I'm going to pull it out

03:51 because he's just that interesting.

03:58 Now, the Unibone has an actual Beagle

04:00 Bone Linux computer on it and it

04:01 interfaces with the bus through these

04:03 bus transceiver chips. So, it allows you

04:05 to run code on Linux that talks to the

04:07 PTB11 bus through these transceivers.

04:10 And uh out of the box, it comes with

04:13 emulation for a number of devices like

04:14 serial and storage and so on. And then a

04:18 couple months ago, I wrote a network

04:20 adapter emulator. So I have a network

04:22 adapter that runs pretty much entirely

04:24 on

04:27 it acts like a real network card, which

04:28 I actually have now, but uh at the time

04:31 I did not. So I wrote a virtual one.

04:32 Then I found a physical one and now both

04:34 work. So I can talk to myself. We have a

04:38 40 and a 50 pin cable here. Connect

04:40 these two boards together. These two

04:42 boards form a disc controller. So, this

04:44 is a UDA50 unibus SDI disc controller.

04:49 Each disc is then connected by four

04:51 pairs of differential signaling cables,

04:52 which are little coax cables if I'm not

04:54 mistaken. Kind of similar to the way

04:56 SATA is wired, but a different

04:58 frequency. So, you can't cheat and use

04:59 SATA cable, or so I am told.

05:03 Next up, after this controller, we have

05:05 another two board set. This is a DEUNA

05:08 network adapter, and this is a 10

05:10 megabit adapter.

05:12 The adapter cable actually comes out

05:14 here. So I'll pull the transceiver up.

05:20 So the cards connection runs to a 15 pin

05:23 which plugs into a transceiver which

05:24 plugs into RJ45 converts it then. So

05:27 this is on my local LAN and it's also on

05:29 the internet when it's running. So this

05:31 1983ish computer with 1983ish

05:34 network adapter runs live on the

05:36 network.

05:40 Last up, we have the TS11 tape

05:41 controller. That's for the big uh it's

05:44 for this guy,

05:46 the big tape controller, but he's not

05:48 hooked up yet because I'm still working

05:49 on the tape controller.

05:55 Down in here, you can see there's some

05:57 little tiny cards and those are just

05:58 jumping the grant from one slot to the

06:00 next. So, when a board wants to do DMA,

06:02 the CPU will send a signal out saying,

06:04 "Hey, does anybody want to do DMA?" And

06:06 the first board that cares intercepts

06:08 that signal and doesn't pass it along

06:10 does its DMA and that's how you get away

06:12 with bus mastering basically. Uh but

06:15 that means that signal has to be

06:16 propagated slot to slot rather than a

06:18 bus fashion and it is. But if you have a

06:20 card not in a slot, somebody has to pass

06:23 that signal along. So, it's either wired

06:25 on the back plane, which I'll get you a

06:27 shot of in a second, or you drop in a

06:30 small adapter card,

06:34 which looks a lot like this, cuz this is

06:36 one of them, flip chip.

06:39 And all it does is bridge some of these

06:41 important signals that have to be passed

06:42 along from slot to slot when there's no

06:45 other card in. When there's a full card

06:47 in, if that card is responsibly made, it

06:48 will pass them along. And finally, we

06:51 have a bigger grant that passes uh NPG

06:54 and some other signals. I'm not exactly

06:56 sure what the difference is, but if you

06:57 look, there is a second set of signals

06:59 being propagated here. Here's the ones

07:02 we saw in the little card. But over

07:04 here, we also passed this, which I

07:06 believe is the MPG grant line from

07:07 looking at it, but that's a guess.

07:17 Now, before we power these up, because

07:18 they get kind of loud, we'll have a look

07:20 inside. This is an RX02 floppy drive.

07:27 Good chunk of it is power supply. And

07:30 here you have logic

07:32 and disc control.

07:35 Top board, which lifts up here, would be

07:36 the logic interface back to the PDP. And

07:38 then the second board would actually

07:40 control the two Scheugart SA 800 drives.

07:43 I imagine they're SA800s or 801's.

07:51 and they are front loaders.

08:00 One thing that's odd about 8 in

08:01 floppies, you have to put the right

08:03 protect tab on to write to them. Unlike

08:05 five and a quarter inch floppies where

08:07 you put a tab on to protect them, on

08:09 these they come, you can't write to them

08:10 until you put a tab on them. A little

08:12 extra fail safe, I guess.

08:17 This is the RA81. I'll show you the

08:19 inside guts once we fold the boards back

08:21 up. But for now,

08:23 we can see that it's got three massive

08:25 circuit boards. The signal from the

08:26 PDP11 comes into this board here. There

08:28 are two ports. So, you can actually

08:30 connect this to two computers.

08:32 How they arbitrate is up or arbiter

08:35 arbitrate. Yeah, how they arbitrate that

08:37 connection is up to them. But uh the

08:39 drive is capable of talking to the two

08:41 different Here's the rest of the drive

08:44 control and power logic. And there's a

08:46 8085 CPUs thrown around in this thing.

08:48 I'm not sure what they're doing with

08:49 them, but there's a couple of them. So,

08:51 let's fold this up

08:56 carefully.

09:11 Now I need a screwdriver of some

09:13 description.

09:16 Smash.

09:18 And somewhere in here you push.

09:22 O.

09:24 Now there's the drive mechanism

09:26 and the drive electronics. A couple

09:28 power transistors. This thing is 14 in

09:30 across, I believe, and it spins at 3500

09:32 RPM. And it's going to be freakishly

09:33 loud when we fire it up. Unfortunately,

09:36 the gas struts that are holding up this

09:37 massive lid are about 40 years expired,

09:40 so it's heavy. And I'm going to put it

09:41 down now. Look at the size of that

09:43 motor, though, back there. It's like the

09:44 size of a Chevy starter motor on a big

09:46 block Chevy.

09:50 All right. Below that, we have RA60

09:51 drives. We have three of those. These

09:53 are 200 megabytes a piece, and they take

09:55 removable cartridges that I can't

09:57 currently load or unload because I got

09:59 the RA81 sitting on top. Oh, actually, I

10:01 can, but I have to power one up. Okay,

10:04 I'll see if I can get them powered up.

10:05 We'll open one later. For now, let's

10:08 start powering up the system.

10:12 Turn the key. That will fire on a remote

10:14 sense switch at the big power center

10:16 that will then fire on the bottom three

10:18 drives powers. But I'll have to turn on

10:19 the R81 by itself. There we go. Nice and

10:22 tidy. Now I should be able to fire up

10:24 the front panel.

10:29 And away she goes.

10:32 All

10:43 right, let's power up the second one. I

10:44 have to move a cable.

10:50 Let's go back and see what we can see.

10:52 Well, first here's a deck writer. Not

10:54 currently set up in the current system

10:56 yet. I have to configure it under BSD.

10:58 As you can see, I was printing and I

11:00 printed a giant X. Not a bad font for

11:03 the 80s, eh? Welcome to my nightmare.

11:08 This is where the cables go.

11:33 I think we have to wait until stop goes

11:35 out.

11:44 Push the button.

11:46 Put the lid.

11:54 And my disc pack is in the other drive.

11:57 But this is what the disc holder looks

11:59 like. This is where the drive actually

12:00 sits. There's a platter stack of six

12:02 platter sits in here

12:05 like so.

12:09 And then when you lift them out, you're

12:11 left with the drives behind.

12:16 if I had one. But I don't have any spare

12:18 RA60 media anymore. Ever. Actually,

12:26 let's power up the old RA81.

12:34 Oh, I got to hit the breaker. One more.

12:36 One moment, please.

12:51 All right, to power up the RA81, we flip

12:53 on the breaker first.

13:00 That's primarily fans you're hearing

13:02 now.

13:03 We'll give it a moment. Don't want to

13:05 stress the motor. We'll fire off run.

13:18 And we dropped the breaker.

13:20 Well, that's never good. Let's go find

13:22 out why. Well, I wish I had a cool story

13:25 for you, but the reality is you just

13:26 can't power up the drive when the

13:28 computer's already on because there's a

13:29 base load from the computer. And that

13:31 base load plus the motor start load is

13:33 too much for the power center. So, you

13:35 have to power on the drive first and

13:37 then the computer. Unfortunately, when I

13:39 did that, the PDP11 did not power on or

13:41 boot. So, something about me taking

13:44 cards out, putting them back has blown

13:47 up the system, and now I must fix it.

13:49 And so, I'm going to go do that now, and

13:52 then I'll uh be back at some point with

13:54 another video. So, if you found kind of

13:55 the PDP11 adventure interesting or

13:57 informative, make sure you give it a sub

13:59 and uh a like, and I will see you next

14:01 time right here in Dave's Garage.

