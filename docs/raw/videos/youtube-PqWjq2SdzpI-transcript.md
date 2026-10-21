---
title: YouTube Transcript: EXPOSED: The Windows Rootkit Scandal by Sony
created: 2026-10-21
updated: 2026-10-21
type: source
domain: ai
classification: general.media
tags: [youtube, transcript, PqWjq2SdzpI]
sources: []
published: 2026-10-21
time_sensitive: True
---
source_url: https://www.youtube.com/watch?v=PqWjq2SdzpI
source_type: video
ingested: 2026-10-21
duration_minutes: 20
language: en
sha256: dab887d37726522a17e4a9ec90db2b0f84ab9859f3a183781181b4a8278c0c0e
---

# YouTube Transcript: EXPOSED: The Windows Rootkit Scandal by Sony

## Video Information
- **Title**: EXPOSED: The Windows Rootkit Scandal by Sony
- **Video ID**: PqWjq2SdzpI
- **Published**: Unknown
- **Views**: Unknown
- **Language**: en

## Transcript
00:00 now you and i both know that we only

00:02 ever made copies for limited personal

00:04 archival use but i'm not talking about

00:05 you and me i'm talking about the regular

00:07 people and they copied a lot of music

00:09 illegally

00:10 for shame

00:15 [Music]

00:22 hey i'm dave welcome to my shop

00:24 did you know that sony once shipped a

00:25 roof kit on 22 million copies of its own

00:28 cds and what's even more surprising is

00:30 that they did it completely

00:31 intentionally in order to hijack the

00:33 operating system install their own drm

00:36 code phone home about your listing

00:37 habits and then hide it from not only

00:39 the users but even microsoft themselves

00:42 and they did it by exploiting one of the

00:43 very components that i was the dev

00:45 manager for back at microsoft way back

00:47 in the day

00:48 i'm dave plummer retired software

00:50 engineer from microsoft going back to

00:51 the ms dawson windows 95 days and if you

00:54 subscribe i'll even let you sit in the

00:56 front row

00:57 it's one of the tales from my microsoft

00:59 days that i've been putting off telling

01:00 for a while because i've been a bit

01:02 scared to talk about it it was a little

01:04 too close to home being one of my own

01:06 components and sony's a pretty big

01:07 company but it's been more than 16 years

01:09 at this point so i think i might as well

01:12 let it all out and the irony in all of

01:14 this is that i'm actually something of a

01:15 sony fanboy i mean i'm literally

01:17 recording this on a sony fx3 camera of

01:20 which i own multiple and i'll later

01:22 watch it back on my sony oled tv as i

01:24 listen to it on my sony xbr receiver or

01:26 my sony noise cancelling headphones so

01:28 when i found out that sony had used its

01:29 collective mic to basically exploit and

01:31 attack one of my own components within

01:33 windows i was more than a little shocked

01:35 but i need to back up let's jump in the

01:37 wayback machine and travel to the year

01:39 of my retirement from microsoft 2003 so

01:42 i can set the stage

01:44 now when it comes to a huge project like

01:46 microsoft windows ultimately every

01:48 component needs to have an owner there

01:50 was even an excel spreadsheet somewhere

01:52 on a server that listed each component

01:53 to the operating system and its owner

01:55 along with their name email address and

01:57 sometimes even their home phone number

01:59 in case of emergency like if it was an

02:00 important component such as the thread

02:02 scheduler or the heap manager

02:04 some components are not under active

02:06 development anymore but they still need

02:07 an owner assigned to them in case

02:09 something comes up with them so for

02:11 example i might own task manager and

02:12 product activation and even the shell

02:14 copy engine and stuff like that all of

02:16 which are generally getting feature work

02:18 or changes made during the current

02:20 release

02:21 but at the same time i would be assigned

02:22 a number of what i'd call legacy

02:24 components just for the sake of them

02:25 being able to have a responsible adult's

02:27 name assigned to them so i wound up

02:29 owning things like calculator and cd

02:31 auto run

02:32 and those of you who know a little bit

02:33 about the sony root kit probably already

02:35 sensed where this is going and that it

02:37 has nothing to do with calculator and

02:38 you're right as an aside you might think

02:41 that owning something like calculator

02:42 would be dry and boring and it probably

02:45 is until one day when someone finds an

02:47 edge case bug and calc returns a bad

02:49 result well it's never happened yet

02:51 thankfully i mean there are odd edge

02:52 cases like subtracting two from the root

02:54 of four doesn't always yield exactly

02:56 zero that sort of thing but nothing like

02:58 the old pentium floating point bug where

03:00 you'd get an outright wrong answer back

03:01 from f div but trust me checking code

03:04 into calculator or being the name on the

03:05 code review line can have a certain

03:07 amount of pucker factor because the

03:09 stakes involved are really high and the

03:11 press would be really bad if you did

03:12 make a mistake

03:14 cd auto run was more like what you're

03:16 thinking a boring state-old component

03:18 that nobody loved maybe a few people

03:20 hated and that normally just did his job

03:22 year after year with few people noticing

03:24 it

03:24 as this name implies cd autorun is code

03:27 that runs inside the shell's explorer

03:29 process and when a new cd is inserted

03:31 into the drive it raises an event that

03:33 the shell monitors for so it knows when

03:36 and what has happened

03:37 when the drive is ready the disk spins

03:39 up the shell suddenly takes a peek of

03:40 the disk to see if there's a setup

03:42 program or similar that should be

03:43 launched automatically

03:45 that way when you put in a cd for a

03:46 program or a game it just starts your

03:48 mom doesn't have to look up the name of

03:50 the program to run in a manual or search

03:52 around the disk for it with file

03:53 explorer so it sounds like it could be a

03:55 handy feature and indeed most of the

03:57 time it is but it could also be the

03:59 source of bugs if whomever authored the

04:01 cd didn't do it properly or if a cd that

04:04 really shouldn't even be auto running

04:05 keeps popping up a useless window every

04:06 time you insert it most of the time

04:08 however autorun was just something that

04:10 people didn't think about at all because

04:12 like i said it just did the same

04:13 predictable thing every year

04:15 so while there was no major feature work

04:17 planned for autorun there was still

04:19 periodic maintenance done on it to make

04:20 it easier for developers a better

04:22 experience for consumers more reliable

04:24 more robust and so on

04:26 and those features were all done by a

04:27 french canadian fellow that worked for

04:29 me at the time whose name was stefan

04:31 now the french pronunciation of stefan

04:33 doesn't come through outlook very well

04:34 though so he literally had to change his

04:36 microsoft alias a few weeks into his job

04:38 there because too many people were

04:40 misreading it or reading it lazily and

04:42 calling him stephanie but i digress

04:44 stefan was a great engineer and otter

04:46 run was a bit of a waste of his talents

04:47 but everybody's got to start somewhere

04:49 and that's kind of where he started

04:51 little did he know how exciting it was

04:52 going to become

04:54 now the story i'm going to lay out for

04:55 you here today doesn't paint a very

04:57 flattering portrait of sony back in the

04:58 early 2000s

05:00 for example when pressed by a reporter

05:01 about the root kit a vp told the

05:03 reporter

05:04 most people i think don't even know what

05:06 a root kit is so why should they care

05:07 about it

05:08 moreover some of the attitudes towards

05:10 the consumers were completely

05:11 adversarial now granted this was at a

05:14 time when a lot of people were getting

05:15 their music illegally with napster and

05:17 so on but rather than run off and invent

05:19 a great streaming service like apple did

05:21 sony was going to be content with

05:22 ferociously defending its territory

05:24 to show what their attitude was like

05:26 back in those days consider what their

05:27 senior vp had to say at an industry

05:29 conference back then

05:31 the industry will take whatever steps it

05:33 needs to protect itself it will not lose

05:35 that revenue stream no matter what

05:38 sony is going to take aggressive steps

05:40 to stop this

05:41 we will develop technology that

05:43 transcends the individual user we will

05:45 firewall it at the source we will block

05:47 it at your cable company we will block

05:49 it at your phone company we will block

05:51 it at your isp we will firewall it at

05:53 your pc

05:55 we shall fight on the beaches we shall

05:57 fight on the landing grounds we shall no

05:59 heroes i just getting into it but i

06:00 should stop now it's never a good sign

06:02 when a company sees their very own

06:04 customers as an existential threat and

06:06 decides to go to war with them where's

06:08 the love sony and how did we get to this

06:10 place would ed sony so backed into a

06:12 corner and afraid that it started

06:13 drawing up battle plans in two words

06:16 napster and dat

06:18 although dat is an acronym for three

06:19 words so that's four words but never

06:21 mind napster is really a subject big

06:23 enough for its own video but in summary

06:24 it was a peer-to-peer mp3 sharing system

06:27 where you could find pretty much any and

06:28 all music all free and completely in

06:30 violation of pretty much every law and

06:32 moral principle out there there were two

06:34 primary reasons i think that people

06:36 resorted to such piracy the first was

06:38 the legitimate need to make a backup of

06:40 your cd or to get a decent copy for your

06:42 car something i think you were always

06:44 entitled to at least one of then the

06:46 second is something i'll call the

06:47 collector instinct it's something i've

06:49 seen people do with pirated software as

06:51 well once people start to build a

06:52 collection they collect just for the

06:55 sake of collecting and they mentally

06:56 keep score by the size of their

06:58 collection they collect music or

07:00 software and they store it and catalog

07:02 it even if they never listen to it or

07:03 play it so there was that but the first

07:06 reason that single legal copy issue

07:08 became suddenly much more important with

07:10 the release of digital audio tape

07:11 commonly known as that or d-a-t i'm told

07:14 that you've always been allowed to make

07:16 one copy of your media for personal

07:18 non-commercial purposes and when people

07:20 were using analog audio cassettes which

07:22 were generally fairly poor quality and

07:24 got worse with each use or even just

07:25 over time the industry didn't mind as

07:27 much

07:28 cd was so much higher in fidelity that

07:30 people would continue to buy cds even if

07:32 bootleg cassettes were available just

07:34 because cd quality was that much better

07:36 but with that that was suddenly no

07:38 longer true that can run full 16-bit

07:41 samples at 44.1 kilohertz the same as a

07:43 cd so it's able to make a perfectly

07:46 lossless copy of a cd and you can make a

07:48 copy of the copy and a copy of the copy

07:50 and a copy of that copy and even that

07:52 will be literally identical to the

07:54 original cd this was the industry's

07:56 greatest fear come true perfect fidelity

07:58 copies of copies with unlimited

08:01 generations

08:02 the first serious proposed solution was

08:04 known as copy code and it was basically

08:06 a notch filter detector

08:08 the content would be mastered with a 3.8

08:10 kilohertz notch filter applied and that

08:12 machines would be required to include a

08:14 chip that would detect such material and

08:15 then refuse to copy it

08:17 there was only one major problem you

08:19 could hear the difference with the notch

08:21 filter and many will tell you that it

08:22 wasn't subtle and reportedly was not

08:25 even that effective either so people

08:26 pushed back hard enough that it

08:27 ultimately killed the proposal

08:30 things then settled down a bit when sony

08:32 bought cbs records because now sony was

08:34 both a record label and a maker of dat

08:36 recorders

08:37 the next perhaps more reasonable

08:39 approach then was a serial copy

08:40 management system that prevented digital

08:42 copies of copies it was enacted by

08:44 congress in 1992 and it also imposed

08:47 taxes on blank cds that could be used to

08:49 store music

08:50 so that meant there would be a

08:51 difference between data cdrs and music

08:53 cdrs and the taxes on music blanks were

08:56 high enough that they were close to the

08:58 price of buying a pre-recorded cd from a

08:59 music store

09:01 what rendered it all moved however was

09:02 effective lobbying by the computer and

09:04 electronics industries that exempted

09:06 personal computers from the act

09:08 it would actually mean that if you

09:09 bought a blank music cd to duplicate a

09:11 pre-recorded cd in a home theater

09:13 machine of some kind it would run you

09:14 perhaps 15

09:16 but if you did it on your pc you could

09:18 do it for a buck seems like a bit of an

09:20 oversight to me but if nothing else it

09:22 set the stage also for the massive

09:24 amounts of digital piracy that would

09:25 erupt with napster tons of software

09:27 aimed at creating and consuming pirated

09:30 music came out and both windows and the

09:32 mac introduced easy ways to rip and copy

09:34 music tracks from pre-recorded cds

09:37 you'll note that i'm just straight

09:38 coming out and assuming this is usually

09:39 piracy and i'm straight up calling it

09:41 that now you and i both know that we

09:43 only ever made copies for limited

09:45 personal archival use but i'm not

09:47 talking about you and me i'm talking

09:48 about the regular people and they copied

09:50 a lot of music illegally

09:52 for shame

09:53 what no one knew or even suspected was

09:55 how far sony would go to protect its

09:57 turf what they did next was completely

09:59 unprecedented they root kitted every

10:02 windows machine into which one of their

10:03 protected cds was inserted so let's talk

10:06 about roof kits let's say you are a very

10:08 bad man and you want to write some very

10:10 bad software there's some very bad stuff

10:12 you write your very bad virus and you

10:14 give it a name like benji.cis and you

10:16 infect machines and so on like a virus

10:18 but you are extra clever and you want to

10:20 be elusive and hard to find and hard to

10:22 remove you're so clever in fact that you

10:24 hack the windows apis for find first

10:26 file and find next file so that when

10:27 anyone even the windows shell or a virus

10:30 scanner for example looks right in the

10:32 folder where benji.cis lives it just

10:34 comes back empty

10:35 it's a ghost because you've hacked the

10:37 apis to lie and say it's not even there

10:40 now a command prompted virus scanner

10:41 will skip over it too as i said because

10:43 not even windows can see it at that

10:45 level anymore this is of course a

10:47 problem and it's one that super

10:48 developer mark russonovich now technical

10:50 head of azure at microsoft set out to

10:53 solve back in 2006 he was working on a

10:55 tool called rootkit revealer that would

10:57 as you can likely guess from the name

10:59 detect rootkits it did so by doing

11:02 things at the lowest level possible down

11:04 at the anti-core apis or even the driver

11:06 level and then up at the highest level

11:08 and comparing the results

11:10 anything below the level of your hacked

11:11 api will still see benji.cis but it will

11:14 be invisible to everything above it by

11:16 comparing the results of a very low

11:17 level enumeration with the high level

11:19 api calls rootkit revealer would detect

11:21 any discrepancy as a potential rootkit

11:23 attack one day when mark was working on

11:26 the latest version of rootkit revealer

11:27 that set off the cloaking alarm

11:29 he was surprised as he's quite careful

11:31 about installing software only from

11:32 reputable sources so how could he have

11:34 picked up a rootkit all the normal scans

11:36 came back empty so he did what folks

11:38 like mark do in such a situation he

11:40 broke out the kernel debugger to get

11:42 medieval on it on a 32-bit system the

11:44 windows kernel normally lives in an

11:46 address range that always starts with

11:47 eight so all the service routines level

11:49 up at eight bajillion hex code loaded by

11:51 the user later will be located somewhere

11:53 else entirely like at a high address

11:55 starting with an f

11:56 a quick look through his system kernel

11:58 service table revealed at least two

12:00 obviously patched functions on closer

12:02 inspection he verified that those

12:04 patched functions were pointing to

12:05 driver code living in a file that was

12:08 cloaked

12:09 there that distortion see it

12:11 now while you can't see a file that's

12:13 cloaked in this matter it's still there

12:18 and you can load and access it if you

12:19 know its full path

12:22 [Music]

12:25 so equipped with this knowledge he

12:26 simply copied the cloaked driver file to

12:28 a new folder where he was able to see it

12:31 and then he was able to load it into the

12:32 ida pro disassembler and take a closer

12:34 look at the code

12:36 mark b mark the first thing he did was

12:38 find a bug in it like the fact that

12:39 allowed for unloading the driver which a

12:41 shamed piece of code like that can never

12:43 actually do as somebody might be about

12:45 to just execute it then there's no way

12:47 to inform them or prevent that from

12:48 happening which leads to a blue screen

12:50 mark spent a good deal of time on the

12:52 technical trail of the rootkit and i'll

12:53 include a link to his blog in the video

12:55 description that details most of it

12:57 long story short however what he

12:59 confirmed is that sony had installed the

13:01 rootkit on his machine and that it was

13:02 drm or digital rights management

13:04 software better known as copy protection

13:07 he must have acquired it when he had

13:09 inserted one of their music cds into his

13:11 machine at some point

13:12 the technology had apparently come from

13:14 a developer known as first for internet

13:15 originally and sony's decision to use it

13:17 on music cds meant that it was included

13:19 on some 52 different titles

13:21 they called it extended copy protection

13:23 or xcp for short

13:25 over 22 million cds would be shipped

13:27 with some form of copy protection in

13:29 this period and 2 million of those would

13:31 be specifically the xcp rootkit variant

13:34 the estimates for how many machines were

13:35 ultimately infected range from a few

13:37 hundred thousand to over a million

13:39 depends on how you're counting which

13:40 version of the root kit and there was

13:42 two and

13:43 one was kind of worse than the other but

13:44 both are similar and don't get

13:46 permission and so i'm kind of lumping

13:48 them in together but i want to talk

13:49 about xcps in particular

13:51 the xdp protection prevented you from

13:53 ripping the raw audio tracks off of the

13:55 cd

13:56 the software remains resident in the

13:58 user's system intercepting all accesses

14:00 of the cd drive to prevent any media

14:02 player or ripping software other than

14:04 the one included with xcp itself from

14:06 accessing the music tracks of the sony

14:08 cd

14:09 it didn't matter which cd ripping

14:11 software you used because it was done

14:13 down at the driver level

14:14 and of course since you couldn't read or

14:16 play the tracks yourself you couldn't

14:18 duplicate them either which was the

14:19 primary intent of the whole thing you

14:21 might be surprised that so many people

14:22 would willingly agree to install such a

14:24 thing

14:25 well it helps that it didn't matter

14:26 whether you accepted the eula that big

14:28 license agreement that you normally skip

14:30 over during setup or not according to

14:32 wikipedia if you declined it still got

14:34 installed

14:35 of course the euler didn't even mention

14:37 the copy protection system anyway so i

14:38 guess it's not surprising or meaningful

14:40 in the end anyway

14:41 aside from the legal and ethical

14:43 questions surrounding the secret root

14:44 kitting of up to a million of machines

14:46 rasanovic's technical analysis of the

14:48 rootkit code revealed a number of other

14:50 concerns

14:51 first it contained bugs and security

14:53 holes that could be exploited by

14:54 malicious worms and viruses

14:56 because it was buggy and ran down within

14:58 the kernel any such exploits provided

15:00 instant privilege escalation to

15:02 administrative rights

15:04 next he noted that it was always running

15:05 in the background consuming both cpu and

15:07 memory regardless of whether a cd was

15:09 even inserted or not

15:11 and as mentioned earlier it contained

15:12 bugs and design defects that meant

15:14 attempts to stop and start the driver

15:16 could blue screen the entire machine and

15:18 finally it provided no one installer and

15:21 cloaked itself in such a way that

15:22 anything but a truly surgical and expert

15:24 attempt to remove it could yield a

15:26 system that wouldn't boot or that would

15:27 boot with missing drives

15:29 soon after mark's mention of the

15:31 problems several of trojans and worms

15:33 were released by hackers that exploited

15:34 xcp security holes

15:36 some were intended simply to aid

15:38 cheating in online games but others were

15:40 more sinister

15:41 so i said that people didn't know what

15:42 rootkit was anyway so why should they

15:44 care but now that they knew the

15:46 computing public was by and large

15:47 outraged when they found out

15:49 and sony was forced to release a removal

15:51 tool

15:52 now the only problem was that it didn't

15:54 actually remove the root kit it merely

15:55 uncloaked it better yet in order to even

15:57 download the removal tool you had to

15:59 sign up with your email address and

16:01 agree to receive bulk emails from

16:02 third-party marketing companies at least

16:04 according to the included privacy policy

16:06 that you were required to accept in

16:08 order to proceed through the process

16:10 as icing on the cake the uninstaller

16:12 which as i said didn't even really work

16:14 also installed an activex control marked

16:16 safe for scripting that contained

16:18 backdoor methods

16:19 microsoft responded by using the little

16:21 known method known as the activex kill

16:23 bit to remotely disable that activex

16:25 control

16:26 but perhaps i've said too much

16:29 eventually sony did release a new and

16:32 improved removal tool which was both new

16:33 and improved in the sense that it

16:35 actually did something

16:36 sony continued to promise that there

16:37 were no security risks associated with

16:39 the anti-piracy technology despite

16:41 multiple reports of viruses and malware

16:43 actively exploiting it ultimately the

16:45 u.s cert branch of the department of

16:47 homeland security issued an advisory

16:48 about the dangers of the sony root kit

16:50 along with helpful advice such as do not

16:53 install software from sources that you

16:55 do not expect to contain software such

16:56 as an audio cd

16:58 it's a bit maddening giving that it was

17:00 effectively a silent drive by install

17:01 once you got the setup rolling and none

17:03 of the users had any idea that they were

17:04 even installing it but soon after the

17:07 lawyers rode to the rescue

17:12 new york and massachusetts issued

17:14 advisories and the state of texas sued

17:15 sony bmg and multiple class action

17:18 lawsuits were filed against them in new

17:19 york and california

17:21 all this unwanted scrutiny revealed

17:23 other problems as well such as the fact

17:24 that the sony rootkit had included open

17:26 source software such as an mp3 encoder

17:28 from a software publisher that was

17:30 actually gpl they believe and they

17:32 didn't follow the license agreement in

17:33 any way by now sony was in enough hot

17:36 water that it had to capitulate they

17:38 settled most of the legal actions now

17:40 you're too late to submit a claim now

17:41 but if you head in time you could have

17:43 received seven dollars and fifty cents

17:45 and one drm free sony album of your

17:47 choosing

17:48 sony pulled all the remaining xcp titles

17:51 from the shelves

17:52 as i said i'm quite a fan of most sony

17:54 products and i'm guessing there must

17:55 have been a massive cultural shift in

17:57 the days since this all happened which

17:58 was back in the 2005 to 2007 time frame

18:02 i don't think they would have survived

18:03 otherwise

18:04 which executives remain from those days

18:06 i have no idea but for those that do i

18:08 hope and assume that their attitudes

18:10 towards the consumer have evolved a bit

18:12 the xcp protected cds plainly carried

18:14 the xcp logo and carried an explanation

18:17 similar to the following

18:19 this cd is equipped with xcp copy

18:21 protection technology preventing the

18:23 downloading or burning of the musical

18:24 content

18:26 one thing you can be sure they all did

18:27 have in common was that they lacked the

18:29 official cd logo because their wonky

18:31 protection format didn't comply with the

18:33 official cd standard known as the red

18:35 book

18:36 could you get infected by it today well

18:38 you have to have a 32-bit version of

18:40 windows but believe it or not if you did

18:41 you still can on the current 32-bit

18:44 build of windows you'll be prompted so

18:45 that it can't do a drive-by installation

18:47 on you but if you press and go on and go

18:50 through the steps it will indeed install

18:52 unfortunately when i saw somebody try

18:53 their system would no longer boot for

18:55 some reason so i don't recommend you try

18:57 it even out of curiosity one good thing

18:59 did come of all this i think the public

19:01 got its first taste of music drm and it

19:03 was such a bitter pill that it really

19:05 laid the groundwork for the music

19:06 streaming ecosystems like spotify and

19:08 itunes the notion that we were going to

19:11 buy and collect individual drm audio

19:13 tracks just wasn't going to happen

19:15 the big services provide by and large

19:17 every song you want online and you can

19:19 play your own local tracks for content

19:21 that you own that they do not have

19:23 and so doing they address both sides of

19:25 the coin that we talked about earlier

19:27 the legal backup copy issue and the

19:28 collector instinct that's good not only

19:30 do you get essentially infinite copies

19:32 of your music but your music collection

19:34 is also essentially limitless in size

19:36 as long as the subscription costs are

19:38 fair it's a great solution for everyone

19:40 certain types of artists don't fare as

19:42 well with streaming revenue as they did

19:44 with album sales but it opens up the

19:45 doors for others and the world keeps on

19:47 spinning into the futures steve miller

19:49 would have said a long time ago

19:51 if you enjoy this kind of industry tale

19:53 told from an insider perspective i'd be

19:55 honored if you consider subscribing to

19:56 my channel so you don't miss future

19:58 episodes in the windows war stories

20:00 series

20:01 and check out the playlist for prior

20:02 episodes

20:03 i don't have any patreons and i'm not

20:05 selling anything i'm just in this for

20:06 the subs and likes so please be sure to

20:08 leave me one of each before you go

20:10 actually i am selling one thing but i

20:12 don't keep the profits that's the

20:13 classic dave's garage mug available in

20:15 the channel store

20:16 any and all channel profits from views

20:18 and merchandise in calendar year 2021

20:20 are being donated to the uw autism

20:22 center so grab a mug where the

20:24 satisfaction of knowing that you helped

20:25 a kid is absolutely guaranteed to make

20:27 your coffee taste better not a guarantee

20:30 thanks for joining me out here in the

20:31 shop today in the meantime in between

20:33 time i hope to see you next time right

20:35 here in dave's garage

20:37 [Music]

