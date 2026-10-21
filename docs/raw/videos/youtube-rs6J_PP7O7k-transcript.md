---
title: YouTube Transcript: Commodore 64 Chip Designer Interview: Albert Charpentier
created: 2026-10-21
updated: 2026-10-21
type: source
domain: ai
classification: general.media
tags: [youtube, transcript, rs6J_PP7O7k]
sources: []
published: 2026-10-21
time_sensitive: True
---
source_url: https://www.youtube.com/watch?v=rs6J_PP7O7k
source_type: video
ingested: 2026-10-21
duration_minutes: 63
language: en
sha256: d5f80c5e3eafc8a2b270cd35aac0a0f33c804ab1382ee8352379ebd2e4aa765d
---

# YouTube Transcript: Commodore 64 Chip Designer Interview: Albert Charpentier

## Video Information
- **Title**: Commodore 64 Chip Designer Interview: Albert Charpentier
- **Video ID**: rs6J_PP7O7k
- **Published**: Unknown
- **Views**: Unknown
- **Language**: en

## Transcript
00:00 [Music]

00:07 hey i'm dave welcome to my shop i'm dave

00:10 plummer a retired operating systems

00:12 engineer from microsoft going back to

00:14 the ms-dos and windows 95 days and today

00:17 in dave's garage i'm honored to have

00:19 albert charpentier designer of the major

00:21 chips in both the vic-20 and the

00:23 commodore 64 as the first guest in the

00:25 dave's garage interview series

00:28 albert was at mos in the mid-70s even

00:30 before was acquired by commodore once

00:33 commodore had acquired mos he went on to

00:35 design the chips that lent their

00:36 personality to the vic-20 and the

00:38 commerce 64.

00:40 now his success can be measured not only

00:41 on the tens of millions of units sold

00:43 but also in the affinity that many

00:45 owners still have for the commodore 64

00:47 and the vic-20 some 40 years later

00:50 albert thanks so much for joining me

00:52 today why not take us back to the

00:54 beginning and tell us how you came to be

00:55 at mos in the first place okay um i'm

00:58 going to give you a little background

01:00 for me

01:00 point um

01:03 when i was seven years old i would get

01:05 up early in the morning sometimes and

01:06 you'd see the test pattern on the screen

01:09 and

01:10 as a little kid like going how did that

01:12 get there

01:13 i mean here's this box sitting in your

01:15 room and had the we had the uh what do

01:17 you call it the rabbit ears right

01:20 back then

01:21 and a test pattern there and i was just

01:23 fascinated how did that get there what

01:25 what happened how did that work

01:27 so

01:29 that was my impetus for becoming an

01:31 electrical engineer

01:32 so

01:33 now fast forward 20 you know i guess

01:36 almost 20 years later

01:37 and

01:38 i'm still fascinated by video and video

01:41 games and um i wanted to design a video

01:45 chip

01:46 so i

01:48 made a presentation to uh the folks at

01:52 mos at that time and um

01:55 then um

01:57 they said i said i can do a video game

01:59 and i outlined what i wanted to do

02:01 and

02:02 commodore commodore mos was a small

02:04 company back then and and it was very um

02:07 there's a lot of freedom okay people

02:10 you could make a proposal if it made

02:12 sense it was sort of like i call it

02:14 pseudo business plan but from a

02:16 technology perspective

02:17 um

02:19 but back then in the late 70s was

02:21 everybody was doing all kinds of things

02:23 and all different kinds of companies but

02:24 i had the freedom there was some freedom

02:26 there of of innovation so they said sure

02:29 go do it

02:30 and um

02:32 but

02:33 they said well before you let you go do

02:35 a chip

02:36 why don't you do a pc board that will

02:38 actually prove you know what you're

02:40 doing

02:42 so i designed a pcb that literally was

02:45 about 15 inches on a side

02:47 all out of ttl

02:49 that mimicked what i wanted to do in a

02:52 subset of what i wanted to do on a video

02:55 chip right

02:57 and so i got that working

02:59 and it took me about three months or so

03:01 as i recall and four months and

03:05 i was able to put a picture on the

03:07 screen

03:08 and it

03:09 to show that

03:10 i actually knew what i was talking about

03:12 right

03:14 and

03:16 so once i did that then i said okay go

03:18 design a chip

03:20 and

03:21 the background for a background for that

03:23 is there was a um

03:26 a product called the

03:28 video typewriter i believe it was called

03:30 um

03:32 don lancaster yeah tv typewriter

03:36 right exactly don lancaster's book

03:38 correct so i that was

03:40 one of my

03:42 uh references that i used to look at how

03:45 to do the vic 1.

03:47 and if you

03:48 remember that the tv typewriter had its

03:50 character space built into raw

03:53 and it was you couldn't change it so but

03:56 it allowed you to put up alphanumeric

03:58 characters on the screen and have

04:00 essentially a typewriter tv typewriter

04:04 that you could then essentially turn

04:05 into a

04:06 a monitor if you will okay for typing

04:09 whatever

04:11 but

04:12 not particularly useful if you want to

04:14 do a really cool video game right

04:18 i had the aha moment at one point to say

04:20 well gee what if we made the rom ram

04:24 and what if the processor could change

04:26 that information in the ram

04:28 on the fly

04:30 so that it would then share the memory

04:32 with the video

04:34 so that you could be able to then change

04:36 the background whatever change the

04:37 screen to whatever you wanted

04:39 so

04:40 that was the idea and then the next

04:43 piece was to create dma

04:45 okay so the

04:47 video chip and the uh processor would

04:50 have equal access

04:52 to the ram when they needed it okay so

04:57 as luck had it the 6502 microprocessor

05:02 was a essentially uh would run at one

05:05 megahertz i designed the vic-1 chip to

05:07 run approximately one megahertz and

05:11 we would share the memory

05:13 so that on one for for 500 nanoseconds

05:16 the video chip hadn't had the ram

05:19 and for the other 500 the microprocessor

05:22 had the ram okay so because the ram was

05:24 able to run at twice the speed

05:27 of

05:28 either the video or the or the cpu

05:31 then everything worked well

05:33 okay and that was

05:35 that was really the the key moment in

05:38 that case and uh i used static ram in

05:41 the vic-1

05:42 uh that turned into a vic-20 eventually

05:45 um

05:46 for that design so that was

05:49 rational there nowadays there is dual

05:51 ported ram where two people can read and

05:52 write from the rom or from the ram chip

05:54 at the same time effectively in the chip

05:56 arbitrates but with static ram you can't

05:58 do that you have to manually

06:00 enable who has access to it is that

06:02 right

06:03 correct well and that was the idea here

06:04 is that i simply

06:06 forced a situation where

06:08 on phase one the cpu had its space

06:13 okay and on phase two the video chip and

06:15 then back to phase one back to phase two

06:18 so it was constantly just a 100

06:21 50 50 interleave whereas in in rams

06:24 today and in modern architecture you

06:27 have weight states and and

06:29 be able to arbitrate between who gets

06:31 the memory more easily and elegantly

06:33 than we had back then right but

06:35 concept no difference in the concept i

06:37 actually did have a situation in the vic

06:39 2 where i had to hold off the processor

06:43 as in normal dma today in order to get

06:46 enough access for the video chip but we

06:48 can talk about that later

06:50 so it's good probably a good time to

06:51 jump into the 6502 since as we're tying

06:53 that in and that really came about from

06:56 the 6800 chip over at motorola and then

06:58 chuck petal wanted to do a cost reduced

07:01 version and they wouldn't let them as i

07:02 understand it

07:03 that is correct yes um

07:06 the 6800 was was designed by chuck

07:09 paddle and uh wool mathis and bill

07:12 mentioned

07:13 it was about eight guys that were

07:15 involved in it there and they wanted to

07:17 go to the next level

07:19 and uh chuck

07:21 envisioned the cpu

07:23 as a

07:24 i call it an industrial controller kind

07:27 of a product all right for doing um

07:30 controls for printers and there was he

07:32 felt that there were volume

07:34 opportunities there that really that was

07:37 the niche that he was aiming at but in

07:39 order to hit that he had to get a lower

07:40 price point he wanted to be able to get

07:42 it out there faster motorola really

07:44 didn't want to look at that they think

07:47 there was no there was no price pressure

07:49 by anybody to do that so they said now

07:51 why why should we do that

07:53 so chuck petal approached

07:56 the president of commodore of mos

07:58 technology at the time in

08:00 1975 i believe it was 75

08:04 yeah about 75 and um

08:07 the

08:08 uh he proposed that they do this new

08:11 processor and mos

08:13 they agreed that okay they they hired on

08:16 the team to go ahead and do it

08:18 okay

08:19 and um it was

08:21 it was a great team of guys i mean

08:23 unfortunately mos technology had a

08:25 pretty good process at the time we were

08:27 building a lot of calculator tips we

08:28 knew how to do that and we had an end

08:31 channel process that was relatively new

08:34 but again the fundamentals of the fab

08:36 were pretty good

08:37 so

08:38 the team put it together and they called

08:40 6500

08:42 and chuck petal put the

08:45 architecture together right basically he

08:47 was really the guy who he formulated the

08:50 instruction set will mathis did the

08:52 architecture bill mentioned all the uh

08:55 uh the hardware design analysis and

08:57 design but

08:59 mos had the

09:00 the infrastructure to allow them to do

09:02 that

09:04 you know so then the thing came out and

09:06 uh they agreed to sell it for 20 bucks a

09:09 copy which was you know a re you know

09:11 that

09:12 right unheard of it was they were

09:14 selling for 80 000

09:16 so going to 20 just created such an

09:20 environment that everybody started using

09:22 the thing you know and actually actually

09:24 the 6502 is which pat was what is what

09:26 powered the atari 2600 obviously the

09:29 apple product

09:31 um it was even in the uh nintendo right

09:36 yeah i don't know how many millions it's

09:37 got to be over 100 million for sure well

09:40 certainly it was i mean the commodore 64

09:42 alone sold 30 million units right apple

09:45 and so i mean it's it's got to be in the

09:47 hundreds of millions i mean it's still

09:49 in use today now you can buy them at

09:51 eight megahertz i believe and or maybe

09:52 16 i'm not sure but yeah

09:54 exactly now their first wrap of it was

09:56 actually the 6501 and it was a little

09:58 too compatible because it was pin

10:00 compatible or instruction compatible

10:01 with the

10:03 not 6800s set compatible okay

10:06 okay and uh motorola didn't like that i

10:08 could imagine especially at 20 bucks

10:11 right exactly they were very unhappy now

10:14 there really wasn't back because

10:16 processors even though

10:18 they were microprocessors and done in

10:20 semiconductors

10:22 cpus have been around for a while it

10:24 wasn't like there was a lot you could

10:25 patent

10:27 in

10:28 a cpu so there wasn't a lot of patent

10:30 protection you could get for a basic cpu

10:32 at the time i mean you might you could

10:34 copyright your instruction set right but

10:37 taking instruction and doing something

10:39 with it

10:40 pretty much been done

10:42 so

10:43 it wasn't you really couldn't but throw

10:44 motorola threatened to sue so they

10:46 changed the pin out

10:48 and they wouldn't let them call the the

10:50 6501 and so that's where the name 6502

10:54 came from

10:55 to get around and pacify motorola right

11:00 funny world

11:02 now the kim one that they put together

11:03 to sort of as a proof of concept or an

11:05 engineering sample board for the 6502

11:08 was actually not done by chuck peddle it

11:09 came out of the calculator group if i'm

11:11 not mistaken yeah there was a group

11:13 there that that i mean

11:16 it was clear that to the calculator

11:18 group that the world was changing the

11:20 calculators were not going to be a

11:22 future

11:23 like a career opportunity

11:25 so

11:26 um

11:27 they saw the opportunity with this and

11:29 and uh there's a couple of guys there

11:31 john may in particular one of the prime

11:33 movers he then said okay we'll go ahead

11:36 and we can take this and we can turn

11:38 this into a a reference design if you

11:41 will to show people how to use 6502 and

11:44 to give them something to play with

11:47 and um

11:48 it was here from the calculator group

11:50 and you'll notice it had a calculator

11:52 keypad on there that's true

11:54 one thing i also was wondering about is

11:56 uh

11:57 it's very similar to the architecture of

11:59 the pet because the two ici chips and

12:02 the cpu and the layout of similar memory

12:03 is even kind of it was i mean yeah it

12:05 wasn't just the calculator group there

12:07 was a lot of synergy there okay between

12:09 okay communication between the group and

12:11 there's no question that chuck and and

12:14 will and so forth interface with the

12:15 calculator guys the calculator guys knew

12:18 what they wanted to do like i know that

12:20 they designed the um

12:22 uh the the the uh storage the cassette

12:25 storage

12:26 thing that uh you know the tape recorder

12:28 stores it was on the chem one

12:30 uh i know that the i think john may did

12:32 that forget who did that in the group

12:33 there i can't remember who did that but

12:36 at any rate um yeah there was synergy

12:38 there uh and architecturally but then

12:42 the the

12:43 the calculator guys drove it to a final

12:46 product

12:47 okay

12:48 um and that was right at the time and

12:51 that the mos got into financial

12:53 difficulty because um

12:56 uh

12:57 there was uh

12:58 you know they they brought in the guys

13:00 from motorola and trying to roll this

13:02 thing out so there was quite a bit of

13:04 cash that was moved out and then in the

13:06 late in the mid 70s there was a

13:08 recession so things got a little tight

13:11 and um

13:12 that's when uh the original investors in

13:15 mos technology were alan bradley the old

13:18 resistor company okay and they basically

13:21 didn't want to put any more money into

13:23 mos technology and um

13:25 that's when commodore came in and and

13:28 bought them

13:29 so they were probably happy to sell

13:30 almost at that point it sounds like well

13:32 it was it was um bittersweet okay

13:35 somebody you know it was great that the

13:36 company was gonna survive

13:38 but

13:39 um it was not what most of the folks who

13:42 were there in that when it started up in

13:44 69

13:45 expected as an outcome right literally i

13:48 would say that almost

13:52 it was only

13:54 almost everybody left within a year who

13:56 was the original partner

13:58 fabrication guys did not leave but all

14:01 the all the calculator engineering guys

14:03 did

14:04 okay

14:05 um except for one guy and um

14:08 i was sitting there i'm literally like

14:10 you know three years out of school now

14:12 and going

14:13 gee what does this mean for me

14:15 right

14:16 or should i stay

14:18 and ultimately i made the decision to

14:20 stay because of the fact i said wow

14:22 you know there's nobody here

14:24 and and i can help grow this place back

14:26 up again okay

14:28 and so that's where

14:31 i had i was in the rom designs but and

14:34 literally during that transition is when

14:36 i

14:36 uh

14:37 made that proposal to do

14:40 the uh the vic one ship

14:42 okay so during all that chaos and people

14:45 were looking for okay what do we do next

14:47 so there was a you know a meeting of all

14:49 the different things that allowed me

14:51 that that opportunity to do that

14:53 now when you're doing chip design in

14:55 those days it's pre-cad so you're

14:57 actually laying things out with a

14:58 template at the level of the flip-flop

15:00 basically

15:01 um

15:02 how big is the thing that you're

15:03 actually building on the table and how

15:05 big is the table and

15:07 it's let me see if i have i think i may

15:10 have

15:12 and i'm going to show you a couple

15:13 things that i used here

15:15 yeah here you go

15:16 you see that yeah

15:18 that is that is the actual logic

15:21 template that i use to design

15:23 the uh the chips that i did

15:26 okay

15:27 and you would you would literally have

15:29 a d size c or d size sheet of vellum

15:33 paper with you know the plastic

15:36 graft paper basically because it was

15:38 more durable than regular paper so it's

15:40 like a

15:41 they called it vellum but it was more

15:43 plastic

15:45 parchment if you will okay it's very

15:47 durable and you would draw that by hand

15:50 and you might have 30 or 40 pages of

15:53 schematics

15:55 okay

15:56 and then you would take the same thing

15:59 and they came in rolls

16:01 and you would roll out and you would do

16:02 a timing diagram by hand okay

16:05 and they might go for feet

16:09 now robs and rams are a lot simpler i

16:11 mean there's there's an address

16:13 you access a cell and you put it out you

16:15 could do that on a few pages it wasn't

16:17 that difficult but when you started

16:18 talking about something like a

16:20 microprocessor or a video chip

16:23 now there was a whole lot of things to

16:25 keep track of

16:26 and it really came down to

16:30 how

16:31 you could manage all the different

16:33 pieces and you tried to keep the cell

16:35 structures

16:36 um

16:38 very

16:39 standardized okay like flip flops you

16:42 had a flip-flop cell and you had a um

16:45 a nand gate in the nor gate cells and so

16:49 depending on how fast you needed to move

16:52 you'd have a type 1 a type 2 a type 3

16:55 and they were just multiples of the

16:57 standard so when you looked at something

16:59 you wouldn't be taking out a ruler to

17:01 measure every transistor each time

17:04 if you weren't careful you would have to

17:06 so once you did the schematic with this

17:08 then you'd have a layout designer where

17:10 you architect your your blocks and then

17:12 the layout designer would actually turn

17:15 the the

17:16 this the schematic into cells and then

17:19 put the cells together

17:21 and then

17:22 this whole thing was done on uh a big

17:24 plotter essentially so that you would

17:27 lay out a piece of paper on a a giant

17:30 platter which was

17:31 really just the flatbed plotter

17:34 and then it would just

17:35 draw them out or draw out all the cells

17:38 that were interconnected by it so we did

17:40 have a little bit of computerization and

17:43 the fact that you were able to digitize

17:45 a cell you were able to put cells

17:47 together

17:48 but there was no

17:50 uh

17:52 checking of did was the schematic right

17:54 there right no nations

17:56 um

17:57 [Music]

17:58 there was no

18:00 drc's

18:01 it was all done by hand okay and that's

18:04 why the number number of components the

18:06 number of transistors

18:08 not only to the process in that handle i

18:10 mean you only had some your geometries

18:12 are so much bigger than but

18:15 physically you couldn't without the

18:16 computer assist you couldn't do things

18:18 much more complicated it was it was so

18:20 hard now when you're doing a ram or a

18:23 rom like the atari rom that's 64k you're

18:25 not laying out 500 and 12 000 flip flops

18:27 by hand so how is that

18:30 you did have the cad capability of step

18:32 and repeat okay

18:34 lay out the one cell and you could step

18:36 it in the x and y directions okay so

18:40 it would essentially you'd give it a

18:42 command to do that so there was we had

18:44 an ibm 360 computer that and some and

18:47 some deck stuff that were essentially

18:51 our

18:53 our cad system it's the nikoi cat is

18:55 pretty weak though i mean it allows you

18:57 to put some things together on the

18:59 screen after you drew them because you

19:01 draw them up and digitize them and then

19:02 that digitized cell you could then step

19:04 and repeat

19:05 and it would have interconnect tabs on

19:08 it similar to any any other i'll call it

19:12 uh chip if you will okay or like a ttl

19:15 pack so you had these connection points

19:16 that go to schematic

19:18 do they have spice in those days yet

19:20 yes we had spice and that was your only

19:23 real methodology for doing any

19:25 simulation with spikes so

19:27 uh you could do a few hundred

19:29 transistors if that and maybe a hundred

19:32 not even a few hundred so there was no

19:33 simulation of the entire chip that i'm

19:36 guessing hathway

19:39 okay but no so you had to actually

19:43 draw up your logic and then go through

19:45 it and then okay this this signal should

19:47 go here and you draw that on a big

19:49 timing diagram i mean the one for the

19:51 vic-20 honestly was about 12 feet long

19:55 because you had to get the timing for

19:56 the vertical sink the horizontal sink

20:00 all of the fetches that had to happen so

20:03 that happened over that

20:05 long video time frame so you had to make

20:07 sure you had all that right

20:09 so what were your major constraints that

20:10 you had to face when you did the vic-1

20:12 obviously the character resolution is

20:14 very low on it what caused that to be so

20:16 low

20:17 well a number of things speed is the

20:19 main one i mean the fact is is that back

20:21 then

20:22 i mean going at

20:24 a couple of megahertz was

20:26 pushing i mean the stuff didn't go that

20:28 fast that that okay and power

20:32 this was done with mmos so you're

20:34 essentially your your your load was a

20:36 resistor

20:38 so

20:38 it it

20:40 every time you had a device that turned

20:42 off you were you were stuck in dc power

20:44 okay for zero so you can only fit so

20:48 much power into that piece of silicon so

20:52 you are not only fighting the speed

20:54 uh but power as well and then the

20:57 geometries so there was

20:59 those three things were always playing

21:01 together as to what the limits of what

21:03 you could accomplish would be

21:05 yeah i guess my graphics card today has

21:07 a tdp of about 320 watts that's probably

21:09 a lot more than you

21:11 yes exactly right you can deal with back

21:14 then so we were trying to stay into the

21:16 you know 120 mil you know 200 milliwatt

21:19 well maybe a little more than that

21:21 probably

21:22 400 milliwatts or something like that it

21:24 was pretty low i mean it said you were

21:26 bumping up against those those

21:28 constraints yeah that's an enormous

21:30 contrast in power consumption

21:32 oh yeah yeah the other one always

21:34 surprises me is there's a single board

21:36 reduction of the 6502 down to discrete

21:39 chips and leds and it's cool to look at

21:41 but it's about a foot square and

21:43 apparently if you scaled the current mac

21:45 ultra's chip out to that scale it would

21:47 be two acres in size or 2.3

21:49 which is

21:50 another amazing perspective to look at

21:52 oh it is just think about

21:55 how computer technology essentially

21:58 we've i was back then way i was always

22:01 thinking about the fact we're designing

22:02 computers to help us design computers

22:04 right

22:05 because you needed the assist to be able

22:08 to get to the next level of complexity

22:10 that that would allow us to do the

22:12 things we wanted to do

22:14 yeah it really only feels to me like the

22:15 last five years we got past the point of

22:17 making tools to make better tools now

22:19 you can actually use them to be creative

22:21 i think you're right i think that the

22:23 tool sets are now so good that you can

22:26 do an awful lot and um

22:30 it it happens so that that the creative

22:33 part has

22:34 made the grudge work a little bit less

22:36 problematic and so you can't

22:39 right

22:40 i agree yeah now if i understand

22:42 correctly you were big into the notion

22:44 or into gaming but you never run up a

22:46 game company why not go to bali or atari

22:48 or williams or one of those oh well um

22:52 interesting okay i'll tell you some of

22:54 the background when what why i left

22:57 commodore and what was going on there at

22:59 the time so um

23:01 after that the commodore 64 was

23:03 introduced i actually made a

23:06 presentation to jack tramiel and the

23:09 team there that said i wanted to do a

23:11 commodore 80.

23:12 now the commodore 80 was going to be an

23:14 80 character version

23:16 of the commodore 64.

23:18 okay so you get 80 you know 80 by 40 a

23:20 true real

23:22 month

23:23 or high res not high res for the time

23:27 and it would be built in and you

23:29 couldn't buy it a commercially screened

23:31 like that so you had to have a built-in

23:32 monitor

23:34 and i wanted to put in a disk drive

23:36 what does that sound like

23:38 gee it's a mac right

23:41 so i made that presentation that i

23:43 wanted to do this and do the next

23:45 generation video chip and and and so

23:48 forth and um

23:50 the

23:51 jack tramiel

23:53 was

23:54 i still remember the statement he said

23:55 to me he said well

23:57 he said you know

23:59 a computer's just a big

24:03 right calculator

24:05 and you need a word processor

24:07 and um

24:09 a couple other things he said in there

24:10 he said

24:11 and and once you have that what do you

24:13 need

24:15 and he said um we're gonna do the plus

24:18 four which eventually became the ted uh

24:22 at commodore because but once he said

24:23 that this was um

24:25 may of 82. i i made i was said i'm

24:28 getting out of here

24:30 and it was the first time i've been told

24:32 no

24:32 right

24:34 that i couldn't do what i wanted to do

24:36 and um

24:37 i just decided it was time to leave so

24:40 um again

24:42 what i realized even though i love video

24:44 games and i played them a lot and still

24:45 do

24:46 um

24:47 the

24:48 i recognize that that a computer is

24:51 still the fundamental place you want to

24:53 be because it gives you productivity and

24:55 by the way i can play good games so

24:57 there's an intersection there that makes

24:59 sense so when i left commodore i started

25:02 a company called in sonic which was an

25:04 audio technology company

25:07 and um but originally before we did that

25:10 i i wanted to do the commodore 80. so

25:14 four of us left from commodore and the

25:16 business plan was to do the commodore 80

25:19 based around the uh intel 8088 at the

25:22 time because the ibm pc was just coming

25:25 out in 83.

25:27 so i left commodore in september of 81

25:30 and he saw me and then um

25:34 i started working on that and so we

25:36 started working on a new video chip and

25:38 a new audio chip

25:40 uh because bobby who did the audio chip

25:42 on the vic commodore 64 was one of the

25:44 people who left with us okay with

25:46 okay so he did he was working the audio

25:48 chip and then we tried to get funding

25:51 to launch this commodore 80 or

25:54 our what we would have called these the

25:56 e-80

25:58 and um

25:59 unfortunately we weren't living in cal

26:01 in in silicon valley right

26:04 and uh we did get some

26:07 interest from venture capitalists in

26:10 california but unfortunately back then

26:14 people traded they said well ibm's got

26:16 the high end

26:18 and compact's got the middle range and

26:22 commodore's got the middle and the

26:24 bottom and there's no room for anybody

26:26 else

26:26 that's what i was told

26:28 so here i am

26:30 what are we going to do now so we

26:32 decided that

26:34 uh

26:35 we can't we don't have the funding that

26:37 we had some money okay but

26:40 we decided to pivot

26:42 finish the audio chip and become an

26:44 audio technology company which

26:46 ultimately became sonic

26:48 was it much of a leap to go from video

26:50 to audio or chips or chips or ah chips

26:53 are i mean to me audio is physics i mean

26:57 it's just like it's a sensory

26:59 interface to your i mean if i look at

27:01 any computer system i always look at it

27:03 as

27:04 it's a way of of augmenting our senses

27:08 you're hearing you're tactile with the

27:10 mouse your your um

27:13 the video

27:14 it's a way of interfacing with the

27:16 machine through our senses

27:18 and so i always look at it as a as a

27:21 physics problem that that how do i make

27:23 this work okay and audio is physics now

27:26 i'm not a musician i'm not that kind of

27:28 a

27:29 musical bob janice was okay

27:32 so we knew that uh we wanted to do a uh

27:38 again how do you create an opportunity

27:40 well there was these companies fairlight

27:42 kurzweil that were selling 10 000

27:44 digital sampling

27:46 audio products right keyboards

27:49 and for my background at collaborations

27:51 let's make it ship we'll do it cheap

27:53 so that's what we did we basically took

27:56 the um

27:57 uh we did a a

27:59 i think it was 16 voices at the time we

28:02 did a 16 voice digital uh system

28:06 which we called the mirage and we put

28:08 out a keyboard which was cost with 16.95

28:11 now i give fairlight and those guys the

28:13 credit because they they

28:15 seated the market and there were a lot

28:17 of musicians who wanted one

28:19 and we brought it down to a price that

28:21 everybody all the musicians who wanted

28:23 one and couldn't afford ten thousand

28:24 dollars could buy a digital sampling

28:27 keyboard yeah that's what we had in our

28:29 game studio was a mirage for exactly

28:31 that purpose

28:33 yeah that that's uh that's my baby

28:35 that's another one

28:37 so that was that was a great company it

28:39 was a lot of fun to work in there you

28:41 know and we had a good team of people it

28:43 was really good

28:44 back in the days of the vic one was it

28:47 uh intended that the chip would be for

28:49 the vic-20 or was it for general gaming

28:51 are we gonna sell it to coleco or what

28:52 was the plan

28:54 i mean it was it was purely for gaming

28:56 and that that was what i wanted to do so

28:59 we were going to try to sell the chip

29:00 because mos was fundamentally a chip

29:02 company at that time so we wanted to

29:05 sell the chip we were selling chips to

29:06 atari in 6502 in the roms so we wanted

29:10 to sell the next generation video chip

29:12 to somebody so um

29:15 with the chip came out it worked and

29:17 everything was good but we could never

29:19 get anybody to bite we spent about a

29:22 year

29:23 trying to get

29:24 somebody to say okay looking at calico

29:27 and those guys but nobody nobody wanted

29:30 to want to try it

29:32 so

29:33 um

29:35 i even remember i read the first time i

29:38 met

29:39 wozniak and steve jobs i was at the ces

29:43 show and we were showing them the the

29:44 vic the the vic one ship we were

29:47 introducing it at ces

29:49 and uh was jobs came by

29:51 and uh

29:53 we i had color

29:55 and apple didn't have color right

29:58 and and they were they were so curious

30:00 about how i got the color and and the

30:03 ram background structure that i did and

30:06 uh spent a lot of time querying me i got

30:09 to know them you know them a little bit

30:10 there right we met

30:12 those and so forth and

30:14 met back and forth quite a few times

30:17 but that was a video game and then in

30:20 1977 i guess it was

30:23 um

30:24 late 77 no yeah 77 sometime in that time

30:27 period 78 um

30:30 i needed i was interviewing people to

30:33 join commodore's engineering team and i

30:35 interviewed bob yanez who was at

30:38 villanova university in his senior year

30:41 and uh we brought him in for an

30:43 interview and taking through a tour and

30:45 i showed him the vic-20 development

30:47 system or not the victoria i mean the

30:49 vic 1 chip development system

30:51 anyway wow that's really cool can i take

30:54 one of these and and use it in my senior

30:56 project that going over and i went sure

31:00 okay

31:01 so he basically took that

31:03 and he added a keyboard and a little

31:05 little simple

31:07 os kind of a thing that he got from

31:08 somebody

31:09 and did a little video screen commodore

31:12 i mean a little essentially a very basic

31:15 little computer system okay that could

31:17 do a few things

31:18 write some things to the screen and so

31:20 forth

31:21 so he comes in in september

31:24 and brings that along

31:26 and we see that and literally like a

31:29 week later jack tramiel was showing up

31:32 and we decided you know what let's show

31:34 jack this

31:35 product here

31:37 and we showed it to him and he loved it

31:40 he went i want that

31:44 so

31:45 he then gets chuck pedal involved and

31:48 there was a lot of stripe there because

31:49 chuck didn't want to do a low end

31:51 computer he wanted to do a higher end

31:53 computer which was the pet product

31:54 that's right he was

31:56 one

31:57 so jack really insisted that they work

32:00 on a this this project with the vic-1

32:03 ship and turn it into something that is

32:05 a you know a an everyday

32:08 consumer computer

32:10 okay so

32:12 the project then moved from uh valley

32:14 forge out to palo alto

32:18 and um chuck paddle bill seiler um

32:23 bob a bunch of guys worked on putting

32:25 that

32:26 vic-20 together there okay

32:29 and nobody was assured it was going to

32:31 be a success or anything so actually

32:33 they rolled it out in japan first

32:37 okay it was called the instead of

32:38 calling the vic-20 it was called the vic

32:40 101 or something like that i can't

32:42 remember the exact name you want but

32:44 anyway there was it was introduced in

32:45 japan first

32:47 and it was produced in japan once they

32:49 finished the design in california and

32:52 then it was then

32:54 relabeled as a vic-20 and then

32:56 introduced to the rest of the world okay

32:59 in the implementation of a chip like

33:01 that as i understand it literally you've

33:03 got scanline counters going in both

33:05 directions and so you know which

33:07 character block you're in and you know

33:09 by it's simply ending with the last

33:11 three bits you know how far down you are

33:12 in a character definition right so it's

33:14 a big counter that's figuring out what

33:16 to display effectively is that kind of

33:18 right

33:18 well you you can look at any video

33:21 controllers nothing more than an x and y

33:24 counter system okay two master counter

33:27 systems so you count across in your x

33:29 you get to the end you reset to zero you

33:31 bump the vertical counter down one tick

33:34 okay and you just go through that

33:36 process and that's your master clocking

33:38 system if you will okay

33:40 so

33:41 anywhere along the line

33:43 you if you like for instance you go okay

33:45 i gotta go catch a i gotta go fetch the

33:47 uh

33:48 the pointer that points me to the

33:50 character that i'm supposed to fetch

33:52 well you know that i want to put a

33:54 character in a certain point the screen

33:55 so you're just essentially just doing a

33:58 comparison off of the x counter at that

34:01 point in time to say okay now go do this

34:04 all right

34:05 and if you think about how a sprite

34:07 would work

34:08 it's nothing more than that okay that

34:10 was the big thing when i went i mean

34:11 that was the major change from the vic 1

34:13 to the vic 2 is i was doubling the

34:16 resolution essentially but at the same

34:18 time adding sprites so a sprite is

34:21 nothing more than a character it's it's

34:24 16 by 16 bits

34:26 and

34:27 you

34:28 have an x and y pointer so as the

34:31 so what you're looking for is the y

34:33 pointer gets to the point you say okay

34:35 it's time to display this so now that

34:37 kicks in your x comparators

34:39 so every time that so then it's looking

34:41 for that x so then it gets it goes out

34:44 says ah let me go fetch the two bytes

34:46 that i'm supposed to display right now

34:48 and boom i'll overlay that on top of the

34:50 background

34:51 so then you have another sub counter

34:53 system that essentially manages all of

34:55 that but it's kicked off by the main two

34:57 counters so the whole video system is

35:00 nothing more than an elaborate scent of

35:03 of system of counters and comparators

35:06 that initiate fetches

35:08 and a serial port and i mean i'm

35:10 simplifying it but

35:12 it's it's a lot to keep track of but

35:14 right

35:15 very methodical

35:17 process

35:18 uh that you can architect out and and

35:22 and because it is

35:25 uh regular and and

35:27 orthogonal

35:29 i can't do the math in my head but i

35:31 would imagine that you actually get the

35:32 horizontal and vertical sink just by

35:34 every 280 ticks we're going to generate

35:36 one and every 32 which energy

35:39 up there it gets to this tick you make

35:41 vertical sync start and you get to the

35:43 next one and and you make it go away and

35:46 and so again it's

35:47 just lots of lots of comparisons

35:50 compares off of this these two master

35:51 counters

35:53 there's a guy on youtube called ben

35:54 eater i don't know if you've seen him

35:55 but he has a great series where he

35:56 starts with a 6502 and a breadboard and

35:58 he builds a computer and he gets to the

36:00 video section and he can only do about

36:02 200 by 200 resolution in color but he

36:04 does it all with ttl series logic chips

36:06 and you get a really good impression of

36:08 how it actually works

36:10 yeah

36:11 i was just at the um

36:13 the vintage computer forum in uh

36:16 a couple of weeks ago with bill hurd

36:19 and

36:20 it was fascinating

36:22 that while there were certainly a lot of

36:24 old guys like myself there there were a

36:26 lot of younger people there and what i

36:28 was fascinated by was and i started just

36:31 talking to what what what do you find

36:33 interesting and

36:35 the reply was was i thought was

36:36 wonderful it's like well

36:38 the commodore 64 type product

36:41 was the false first really fully capable

36:44 computer system but yet simple enough to

36:47 understand right so if you were to study

36:50 that as as okay how does a computer work

36:53 you can get in and understand all the

36:55 pieces and they're the same as today's

36:58 computer there's not i mean there's just

36:59 a lot more of it

37:01 and

37:03 with the exception of

37:05 cash systems and memory management

37:08 there's not

37:09 a whole lot of difference

37:11 um that were added to you know

37:13 everything just went faster and more of

37:15 it and faster

37:17 but fundamentally um

37:19 you if you you can you can study it

37:21 something like commodore 64 and really

37:23 get to understand all the pieces of the

37:25 computer

37:26 that can fit and they can still fit in

37:28 your head right

37:29 i just had a discussion with mark

37:30 zubikowski from microsoft who's been

37:32 there since ms-dos 1-2

37:35 and uh

37:36 i asked him what was the because he's

37:38 all the way through nt and all the i o

37:39 code and everything else but i asked

37:40 what was the last point that you think

37:42 you understood the entire system front

37:44 to back in depth and for him it was like

37:46 ms-dos 3.3 or something in that era

37:49 whereas where you got the nt he would

37:51 understand the i o subsystem entirely

37:53 but not the entire computer exactly it's

37:56 just there's just too much now and

37:59 no one person can actually absorb at all

38:02 right teams of people whereas well with

38:05 commodore 64 there was

38:07 like five of us

38:09 i mean 65 with two or three guys i mean

38:12 you can't do that today right

38:15 too complicated but hey that's why we

38:17 built computers to help us do these

38:18 things that's right

38:20 so in terms of process

38:22 uh how

38:24 was it how many mills was your actual

38:27 size you drew something of what we were

38:29 as for i mean the transistor

38:32 uh channel okay from from the drain to

38:34 the source okay that was our minimum

38:37 geometry we drew those at four mils

38:41 okay so four mils is um

38:44 i don't know my conversions anymore

38:46 ten thousand one hundred and sixty

38:47 nanometers i think right okay something

38:50 like that or one thousand and sixteen

38:52 yeah when i'm off by a factor of ten but

38:54 it's a lot of nanometers yeah it's big

38:56 okay now and then we would try they

38:59 would actually shrink that

39:00 photographically

39:02 at when they made the mask

39:04 down to 0.35 and in some cases 0.3 okay

39:08 so whatever as as the

39:11 photolithographic process improved that

39:14 way you could just shrink things

39:15 photographically and not have to go back

39:17 and redraw everything okay so generally

39:20 we we would draw at four mils

39:23 uh i'm not four mills uh it was point

39:25 four i'm sorry it goes off by

39:27 by a decimal right that's ten thousand

39:28 one sixty there you go

39:30 right yeah point four mills so and then

39:33 they would shrink it to point three five

39:35 and eventually they got the point three

39:36 so like the the most of my stuff was was

39:40 uh 0.35 mils and that was your smallest

39:45 reasonable dimension that you could do

39:47 there would you could do we could do a

39:48 contact between layers i think was

39:51 .25 mils

39:54 but that was it so that was pretty big

39:56 in comparison today's technology okay

39:58 yeah ten thousand versus what are we at

40:00 seven and five now right yeah it's crazy

40:03 yeah i mean yeah

40:06 um one thing i've always wondered is

40:08 when i worked on ms-dos there was no

40:09 reuse if you wanted to output a decimal

40:11 number you had to write the hex the

40:13 decimal conversion yourself other than

40:15 what was in the system bios when you

40:17 guys were designing chips did you go and

40:18 grab a section of logic from the vic 1

40:21 to make the vic 2 or was everything a

40:22 clean sheet from the beginning oh it had

40:24 it was clear you had to start over again

40:27 because okay it was double the

40:28 resolution um we were going to add more

40:30 features the sprites i mean it was you

40:33 know architecturally the you know the

40:35 dma and those kinds of pieces are needed

40:37 but everything was getting running

40:38 running faster now um

40:41 yeah so you start

40:43 you know that

40:46 here's how you did it again it's a big

40:48 counter assist control system

40:50 but

40:50 you started over again it really wasn't

40:52 okay edit a schematic and go to the next

40:55 thing we started over again

40:58 um in terms of reuse again did you have

41:00 macros for bigger blocks or not macros

41:03 but if you want to do a counter did you

41:04 have to lay out all the nor gates or did

41:06 you have a here's a counter block it was

41:08 a counter was essentially you would lay

41:10 out one bit of the counter okay

41:13 then you would have a carry out which

41:15 would go to the next bit

41:16 okay so when that kicked over so you

41:19 essentially just then have one cell that

41:21 you would lay out and you would step

41:22 that for as many bits as you needed in

41:25 the counter okay so you'd only lay it

41:28 out once so again you wanted to make

41:30 sure that you did your logic so that you

41:32 didn't have to lay it out so you made

41:34 sure that your your logic would go okay

41:36 so this output goes to this input and

41:38 you set it all up so you can just step

41:39 and repeat

41:41 yeah um before we leave the vic-20 then

41:43 i'm kind of worried about the system

41:44 software a little bit then who wrote

41:46 that and when did it go from becoming

41:47 just a layer for microsoft's basic

41:50 versus like a real kernel for other

41:51 developers to call yeah that was done by

41:54 bob bob russell bill seiler the team at

41:57 palo alto okay that was not done at

42:00 mls commodore about you know king of

42:03 prussia valley forge area um

42:06 so

42:07 they did that work there okay so um yeah

42:11 they took the the microsoft basic kernel

42:14 that we've got from bill gates for the

42:16 pet

42:16 and that became the

42:19 foundation for that and then they

42:20 layered on the other pieces

42:22 okay

42:23 um so there was an actual intent to

42:25 produce a kernel then it wasn't just an

42:27 outgrowth of the fact that we had to

42:29 make a basic layer for microsoft to call

42:31 no it was there was that yeah there was

42:33 a real effort i mean they

42:35 they made it into a real kernel at that

42:37 point yes bob russell's team and the

42:39 team were really responsible for that

42:41 okay

42:42 and going from the vic 1 to the vic 2

42:43 the biggest changes in my mind are the

42:45 change from static ram to dynamic ram

42:47 and uh obviously addition of sprites

42:50 resolution and the smooth scrolling

42:53 what else am i missing is there another

42:54 big piece there that

42:56 i want to add that was it right there

42:58 you you you described them um and that

43:01 was the vision and

43:03 uh

43:04 i started with the vic 2

43:07 before

43:08 the vic 20 was done

43:10 okay so

43:12 i wanted so i realized the vic

43:15 one was not a successful video game

43:18 chip

43:19 so i said okay what do i have to do to

43:22 make this

43:23 a really successful game chip okay and

43:26 that was the things we just talked about

43:28 the sprites the bezel resolution so on

43:31 and so on

43:32 um

43:33 so i actually started architecturally

43:36 to make the vic-20

43:38 a much better video gameship

43:41 but then the vic-20 became wildly

43:44 successful so that it was clear that we

43:46 were going to use the victor chip as the

43:51 video interface for the next generation

43:54 vic series computer

43:57 okay so it morphed into that but

43:59 in in actuality

44:02 there was nothing we really changed

44:04 because again a video display is the

44:07 same whether it's a gamer's computer

44:08 it's still a video display you may not

44:11 need sprites but

44:12 i still felt that

44:15 games were a good reason to have

44:16 computers exist right

44:19 now ti actually owned the copywriter

44:21 trademark on sprite so i'm guessing they

44:23 had a chip that had sprites or did they

44:25 yeah they they had a product and i

44:28 forget the chip number 74 some 94 i

44:31 forget the chip number on it

44:32 but they they're one of their chips had

44:35 sprites they had eight sprites they were

44:37 eight bit by eight bit

44:39 pretty s

44:41 not very capable okay

44:43 but they did develop that concept okay

44:47 and um i thought it was great i mean

44:50 great because one of the biggest

44:51 problems back then with microprocessor

44:54 speeds was how do you move something

44:57 around the screen

44:58 i mean you were using you know you had

45:00 to you had to be able to take a block

45:03 and move it to another block in the

45:04 screen somewhere

45:06 on with a complete xy flexibility

45:10 there just wasn't enough cpu power to be

45:13 able to do that effectively

45:14 so how do you move something easily on a

45:16 screen and that's the sprites was it was

45:19 a great solution back then

45:21 and so

45:22 um

45:23 i just extended the concept to say okay

45:26 i'm going to make them bigger

45:27 i'm going to add color

45:29 i'm going to add whether they can be

45:31 behind the background or in front of the

45:33 background uh i'm going to add collision

45:35 again collision detection was huge yeah

45:39 you had no way to do

45:41 and processes again weren't strong

45:42 enough to figure out who would collide

45:44 so having that is in in the chip

45:47 allowed you to be able to do collision

45:49 detection whether it was against two

45:51 sprites hitting together or whether it

45:53 was a sprite hitting a an object so you

45:56 had both sprite to sprite collision

45:57 detection as well as sprite to

45:59 background collision detection and you

46:01 only did it on non-transparent pixels

46:03 too if i'm right correct which made a

46:05 big difference as a programmer anyway

46:07 right exactly so you know having

46:11 i understood the problems that the

46:13 programmers were dealing with in trying

46:14 to get a complex video game with with

46:18 lots of moving objects and the other

46:20 nice feature the sprites they were

46:21 reusable so that once you finish the

46:25 16 bits in the in the y or the 16 or 16

46:28 lines in the y then you could reuse it

46:31 at the bottom portion of the screen

46:33 okay so a lot of guys did that and i saw

46:36 some amazing um

46:38 demonstrations where people had like 24

46:40 sprites

46:41 on the screen

46:44 i just saw one this year finally after i

46:46 guess it's been 40 years where somebody

46:48 did a full screen sprite where it's i'm

46:50 not entirely sure how they did it yet

46:52 but it's every 20 pixels they restart

46:54 another sprite of the 24 and they had it

46:56 across the entire screen so it's

46:58 effectively a single 320 by 200 sprite

47:01 which i had never seen before and i'm

47:02 wondering if

47:04 all that

47:05 thing too i saw yeah i saw a person i

47:07 mean like probably on video somewhere i

47:08 saw that it was incredible yeah

47:11 [Laughter]

47:12 somebody somebody spent a lot of time

47:14 doing that to figure out how to make

47:16 that happen

47:17 it was pretty impressive

47:19 now atari had i think was player missile

47:21 graphics i don't even remember what that

47:22 was they were very small i'm guessing

47:24 but and only a couple of them and

47:27 yeah um

47:28 i mean the atari video engine was

47:31 nothing more than a big shift register

47:34 okay it didn't have dma so the 6502 was

47:37 literally doing load stores so it would

47:40 take some information from the rom

47:43 and then store that uh based on the

47:46 program

47:47 in in the

47:49 in the shift register for the lawn

47:52 so you were all that was happening was

47:55 essentially it was just simply load

47:57 stores as fast as it could do

47:59 and then during vertical sync we tried

48:01 to do the game logic

48:04 it was amazing that they could

48:06 accomplish what they could accomplish

48:07 because a missile was nothing more than

48:10 a in putting a bib turning a bit on in

48:12 the sheer real stream that was going out

48:14 the processor had to keep track of and

48:16 try to stay up on top of that it was

48:18 incredibly difficult um i learned about

48:21 the uh the atari machine because like

48:23 one of the things when i left commodore

48:25 one of the things that i did i designed

48:27 a

48:29 since i knew about i knew it was how the

48:31 atari machine worked because i've done

48:33 the roms with them on it

48:35 i basically said well again i use the

48:38 same thing what if i took the cartridge

48:40 that we plugged into the thing

48:42 instead of making it raw make it ram

48:46 and then i put a processor out there

48:48 that would dma with that ram

48:50 so that

48:51 the atari

48:53 2600 became nothing more than a video

48:56 display manager

48:57 and then the external processor would

48:59 fill out the ram

49:01 and and

49:02 and the

49:03 software so it would essentially just

49:05 spew the stuff out onto the screen so by

49:07 having two processors you could do a lot

49:09 more video game stuff

49:11 so um

49:13 i developed that and then

49:15 after i left commodore it's the first

49:16 thing i did when i left commodore

49:18 um i tried to i liked i did license that

49:21 to atari all right

49:24 yeah but they ran into right before they

49:26 brought it out they rented they ran into

49:28 financial difficulty and never actually

49:30 brought it to market

49:31 you know it was one of those things that

49:33 uh

49:34 you know

49:35 it was going to turn like the 2600 into

49:37 like a vic 20 like computer at the time

49:41 you know but again it's just simply

49:42 saying okay just treat 2600 as a video

49:45 engine and don't have to do anything

49:47 just spew out the data

49:49 you know you could do it if it was doing

49:50 nothing else so as long as you have to

49:52 do any logic it was just doing load

49:54 stores all day long it could keep up and

49:56 do a 20 character display

49:59 one thing that's always fascinated me

50:00 and you touched on it a bit earlier is

50:02 how the vic chip knows at any given

50:04 pixel whether it should be rendering a

50:06 character or a sprite

50:09 and i'm not sure with the reuse how you

50:10 would make that work yeah well there was

50:13 a priority it was a priority um

50:16 register for each sprite to determine

50:18 where

50:18 what its priority in terms of the uh

50:21 this who is going to get displayed so

50:23 there was a a sprite priority system so

50:27 what sprite would be displayed over

50:28 another one and then there was a sprite

50:31 to background priority tree okay

50:34 so

50:35 so there was this huge

50:38 a big chunk of logic so you had all this

50:41 shifting stuff coming at you the

50:43 background information and the various

50:44 sprites and it would all funnel down

50:46 because eventually it had to become one

50:48 shift register so you'd have this entire

50:52 big child was literally a big chunk of

50:54 logic i know i had the whole chip right

50:56 here

50:57 i don't know you probably can't see it

50:59 it's probably too

51:02 oh really that's amazing yeah

51:04 yeah so this chunk of um sorry i gotta

51:07 get my prior get organized here okay

51:09 this chunk over here

51:11 there's your priority logic encoder

51:15 it's a big chunk of logic it is

51:18 holy this is all the sprite logic i mean

51:20 i mean literally this is your red this

51:22 this ram over here was your

51:25 uh ram for your um

51:27 uh

51:28 the line and the sprites that you had

51:30 and this is all the sprite logic and

51:32 this is the priority encoder and then

51:34 that all filtered up through here into

51:36 the output shift register and color

51:38 control

51:41 and how many transistors would be in a

51:42 chip of that size

51:44 oh this is probably

51:46 20 000 maybe okay

51:49 yeah i mean

51:51 yeah i think like the 6502 was about 10

51:54 000 i believe this was about double that

51:58 one other thing i was wondering is why

52:00 jack tramiel pushed so hard for 64k on a

52:02 machine that couldn't really use 64k was

52:04 it strictly marketing or was it

52:06 well

52:07 we originally designed it for 16k that

52:10 was the first

52:11 design architecture that we were going

52:13 to do okay we were so it was the it was

52:16 going to be dram anyway so we had to

52:18 have put all the logic and controls for

52:21 the dynamic ram

52:22 so during a meeting with jack one time

52:24 we're going over the progress uh he

52:27 really said listen

52:29 uh i believe that 64k rams are going to

52:32 become

52:33 the the normal the primary engine and

52:36 16ks are going to go away and that the

52:38 price of 64k is really going to drop so

52:42 from a

52:44 capability and well he really wanted for

52:46 marketing

52:48 and i said wow

52:49 you want to give me 64 candice machine

52:51 i'll take it

52:53 i mean yeah even though the machine

52:54 couldn't handle it all again by bank

52:57 switching and

52:58 various games i mean i really had to do

53:00 bank switching in rome so we just put

53:02 the bank switching capability so you

53:04 could get it all the ram even though it

53:06 really didn't have that space so you had

53:07 to play games to actually utilize it but

53:11 yeah it was it was fundamentally

53:12 marketing that was the

53:15 primary reason

53:17 and then

53:18 said okay how do we take advantage of it

53:20 right

53:21 it may have been after you left but i

53:23 believe there was an effort for was it a

53:24 comet or mega 65 or something a version

53:27 of the 64 with faster cpu and

53:29 yeah

53:30 yeah there was there was quite a few i

53:32 mean uh bill heard as i was leaving

53:35 um

53:36 i think i left in september

53:39 september 1st of 1982

53:41 and um

53:43 bill hurt came in i think in january of

53:45 83

53:47 and he really became the guy who was

53:49 propelling that whole commodore

53:52 line at that point he well the 128 and

53:55 so forth and um

53:57 so yeah he um

53:59 that that whole

54:01 there was quite a few products that were

54:06 developed i don't there was many more

54:08 developed than actually saw the light of

54:10 day and bill bill really has a good

54:13 history of that okay and i think that

54:15 really was one of the problems that

54:17 happened

54:18 is that

54:21 commodore once

54:23 once

54:24 my team left that that went to win sonic

54:27 and then jack left about a year or so

54:28 later two years later i think it was

54:31 commodore kind of lost its

54:34 its

54:37 lineage i guess you will i mean our

54:38 focus where there should be and and it

54:40 was a lot of competing factions

54:43 and jack was such a such a

54:46 strong player in the game

54:49 that it left the void

54:51 that no one ever really said okay we're

54:53 going to go do that and this is what and

54:55 they never really grabbed it and then

54:57 they went down the omega path and

55:00 i always was surprised i always thought

55:02 that

55:03 what i called the vic 80 or the

55:05 commodore 80 or the the uh

55:07 the 80 at that point

55:09 was going to be a a product

55:11 that

55:13 was based on the intel processor i

55:15 always thought that if commodore had

55:18 taken the amiga video set or some other

55:21 video processing capability and added

55:23 that to the ibm product line

55:26 okay and had and i know that they would

55:28 have really been upset about having the

55:30 license doss

55:31 but

55:33 i always felt that if they had gone down

55:35 that path it would have been

55:36 they would still be here today right

55:38 because they had

55:41 the video engine they had audio and and

55:44 they were ahead of the game when

55:45 everybody else in that in that graphics

55:47 engine area and but yet

55:50 because they didn't have a mainstream

55:52 processor they always were fighting

55:54 against that

55:57 let's see what else have i got here i

55:58 think that's almost oh one thing i want

56:00 to ask you about is on color on the vic

56:02 2

56:03 and i don't really understand this but

56:05 there's three lines come out and they

56:06 run to a 4066 chip that seems to be some

56:09 kind of multiplexer i'm trying to figure

56:11 out what that does what's that chip for

56:13 oh well that's actually that's actually

56:15 the color ring okay

56:17 that multiplexer essentially was a cheap

56:19 dma controller okay

56:22 so you have you have the data bus that

56:25 comes from the microprocessor because

56:27 you've got to fill out the color ram

56:29 okay and the video chip have to access

56:32 the color ramp okay

56:34 so

56:35 how do you

56:36 i've got a data bus from two things and

56:38 how do you get them to to talk to each

56:40 other all right so what i did was i said

56:43 okay i'm going to use

56:44 a 4066 as a rather than having to have a

56:49 buffer system that the dual buffer

56:51 control

56:52 you just use a pass transistor which is

56:55 what a 4066 is so

56:57 when when the video chip needed it i

57:00 would turn the thing off so that the

57:02 data bus would go right to the video

57:03 chip and i knew that i wasn't going to

57:05 be using it so i'd turn off the buffers

57:07 on the video chip and open up that past

57:09 transistor so the microprocessor could

57:11 get to it

57:13 okay so

57:14 it was just that because there was no

57:16 easy way i needed more bam and i didn't

57:18 have enough bandwidth to get all the

57:20 characters

57:22 and the sprite data and the sprite color

57:25 information

57:27 in in

57:28 in and i just didn't have enough dma

57:30 bandwidth so

57:32 i could fit it conveniently into the

57:34 dram somewhere and get another accesses

57:37 for that so i just stuck the color ram

57:40 in this static ram out there and and

57:43 talked to it through this past

57:44 transistor structure

57:47 you know it was it was like okay how do

57:49 i get around this problem i need color

57:50 information and um

57:53 that was the only way to do it that was

57:55 convenient

57:58 um what else is going to ask you oh in

57:59 the dawn lancaster book he talks about

58:02 an upstream memory tap and what i

58:04 believe he's doing is he has a separate

58:05 set of address lines and data lines that

58:07 go to the ram and he turns off cpu

58:10 access to the ram so that the video can

58:12 draw it

58:13 and that was one of your bigger

58:14 breakthroughs i think was with the

58:16 ability to have this trimming structure

58:17 so you never had to lock the cpu out

58:20 correct right that's by forcing the

58:21 memory to run twice as fast

58:24 as the cpu

58:26 and and making sure that that everything

58:28 was on alternate cycles as long as your

58:30 ram ran twice as fast as

58:33 the processor and video subsystem then

58:36 you had you never interfered with each

58:38 other so

58:39 all of the

58:41 constraints on the design were a

58:42 function of how fast the ram could go so

58:45 as long as your ram was faster

58:47 you could you could do

58:48 a true

58:50 not interfering dma structure

58:53 and and that was really important

58:54 because once you you know if you got to

58:56 shut down the cpu to get to the memory

58:59 you've just really limited what you can

59:00 do so i really wanted to avoid that

59:03 right

59:04 well since both have effectively de

59:06 facto exclusive access to the ram when

59:09 they want it why is it actually slower

59:11 when you're in the rasterized area and

59:13 displaying characters and stuff it's the

59:16 system is faster when you're in the

59:17 background area

59:19 well it's not it's the same i never shut

59:21 up i never shut the processor down i

59:24 think there's a 60 micro i do have to

59:26 shut it down in one area to be able to

59:27 go do a pre-fetch

59:29 i can't remember the details been 40

59:31 years ago

59:33 i i did do a pre-fetch for 60

59:35 microseconds i did have to shut the

59:37 processor down for like 60 microseconds

59:39 but that was it it wasn't during the

59:41 entire vertical blanking but it was a

59:42 pre-fetch i had to do i can't remember

59:44 the details right now but the process

59:46 has never ran much slower um

59:49 that i would call for blanking

59:51 it was only that pre-criteria where i

59:53 had to do the 60 microseconds so it was

59:55 yes it was a little slower but

59:57 it wasn't dramatic but i don't remember

60:00 the details of what the timing was yeah

60:02 i'm trying to remember why they had to

60:03 turn off the screen to load from tape i

60:05 guess is

60:07 oh

60:09 yes

60:10 that's a whole different

60:11 animal right there yeah

60:14 now that was um

60:15 in the whole take that was in the

60:17 operating system of the tape system

60:19 because they had the the shift register

60:21 wasn't

60:22 it wasn't running fast enough i don't

60:23 that was not my design area okay i did

60:26 not that came out of the the vic-20 and

60:29 bob uh bob russell worked on that uh

60:32 process there but i don't know the

60:33 details okay

60:35 well that's really all i've got if

60:37 there's anything more you want to throw

60:38 in here by all means tell me another

60:39 story but

60:40 fun um

60:43 i mean i

60:45 i really enjoyed the my atomic commodore

60:47 it was a lot of fun it prepared me to be

60:49 an entrepreneur which is really always

60:52 always what i wanted to be

60:54 um and

60:56 designing chips back then was it was so

60:59 exciting because you could you could

61:01 think of things

61:02 and

61:04 execute on them in in

61:07 in a reasonable period of time and the

61:09 costs were not the kind of cost you have

61:11 to deal with today and everyone wasn't

61:13 as complicated so it was like the wild

61:15 west if you will right

61:17 but it was fun it was fun to be able to

61:19 be part of that era and have an impact

61:21 on on what

61:23 what the world of computing turned into

61:26 so

61:27 definitely satisfying from that

61:28 perspective and uh enjoyed it a lot

61:31 so and it just prepared me for all the

61:32 other things i didn't like and

61:35 the companies that i that i've worked

61:36 with and started so

61:39 enjoyed it

61:40 cool thanks so much for being so

61:41 gracious with your time and patient with

61:43 the technical issues and

61:45 good well i hope you found it

61:47 interesting i sure did

61:49 okay good all right well dave thank you

61:51 very much and enjoyed it thank you

61:54 okay okay i'll talk to you later okay

61:57 bye-bye

61:58 now if you made it this far there's no

62:00 reason not to be subscribed to the

62:01 channel plus you don't want to miss the

62:03 next installment in the series featuring

62:05 bill hurd of commodore 128 fame

62:08 now if you have any interested matters

62:09 related to autism asperger's or asd

62:12 please check out my book on amazon

62:13 secrets to the autistic millionaire it's

62:16 got nothing to do with money and

62:17 everything to do with living a

62:18 successful life on the spectrum

62:21 it's everything that i know now that i

62:22 wish i'd known back then

62:24 remember i'm mostly in this for the subs

62:26 and likes so please be sure to leave me

62:27 one of each before you go today in the

62:29 meantime in between time i hope to see

62:31 you next time right here in dave's

62:33 garage

62:34 do it glenn do it

62:39 this little chair will be waiting for

62:40 one of you

62:41 and a rocking chair for another who

62:43 likes to rock

62:45 and a big armchair for two to curl up in

62:49 all next time on dave's garage

62:55 [Music]

63:04 [Music]

63:18 you

