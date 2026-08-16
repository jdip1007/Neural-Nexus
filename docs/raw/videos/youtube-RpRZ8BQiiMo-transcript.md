---
source_url: https://www.youtube.com/watch?v=RpRZ8BQiiMo
source_type: video
ingested: 2026-08-16
published: 2026-08-16
duration_minutes: 23
language: en
sha256: 1c81051147be06c710a3889a48048da2ea805ecd0d78084328fb9cac8401876d
time_sensitive: True
---

# YouTube Transcript: Windows Longhorn Explained by Dave Plummer - Retired Microsoft Engineer

## Video Information
- **Title**: Windows Longhorn Explained by Dave Plummer - Retired Microsoft Engineer
- **Video ID**: RpRZ8BQiiMo
- **Published**: Unknown
- **Views**: Unknown
- **Language**: en

## Transcript
00:00 the degree to which eating dog food is

00:01 tolerable can be measured in the direct

00:03 proportion to how good the dog food

00:04 actually is and this was not good dog

00:07 [Music]

00:13 food hey I'm Dave welcome to my shop I'm

00:16 Dave plumber a retired operating systems

00:18 engineer from the MS Doss on Windows 95

00:20 days and today we're diving into one of

00:22 the wildest development stories in

00:24 Windows history The Saga of Windows

00:26 Longhorn it was the last product at

00:28 Microsoft that I ever worked on all I

00:31 know is that I retired while working on

00:32 it and after I left they had to entirely

00:34 reset the code base deduced from that

00:36 what you will but what was Longhorn well

00:39 most people would tell you that it's the

00:40 code name for what eventually became

00:41 Windows Vista Vista was what Longhorn

00:44 eventually became but it's nothing like

00:46 it was intended to be Longhorn is the

00:49 tale of big Ambitions technical

00:50 nightmares and an extraordinary comeback

00:53 if you've ever wondered why Vista turned

00:54 out the way it did or how a project that

00:56 Microsoft could go so off the rails that

00:58 management had to entirely hit the reset

01:00 button stick around this is the inside

01:03 story of Longhorn the Revolutionary

01:05 windows that almost was and how it Rose

01:07 from its own ashes told by somebody who

01:09 was there Longhorn was supposed to be

01:12 revolutionary in the early 2000s after

01:14 the success of Windows XP Microsoft's

01:17 plan was to follow up with an interim

01:19 release code named Longhorn before the

01:21 next major Windows code Nam black home

01:24 in fact the Coden name Longhorn itself

01:26 comes from a bar between those two ski

01:28 mountains Whistler and black home in

01:29 British col Columbia a nod that longhorn

01:31 would be a stop gap between Windows and

01:33 XP or Whistler and the big future OS to

01:36 be known as blackcomb but as development

01:38 went on Longhorn grew in scope it

01:41 started absorbing many ambitious

01:42 features that originally intended for

01:44 the future Black Comb release in other

01:46 words this minor interim release

01:48 ballooned into a major overhaul of

01:50 Windows and the goalpost would keep

01:52 moving so what was the vision well

01:54 Microsoft wanted Longhorn to reimagine

01:56 what Windows could be we're talking

01:58 about very fundamental Chang is under

02:00 the hood and a flash a completely new

02:02 user experience on the top one of the

02:04 crown jewels of this Vision was

02:05 something called winfs short for Windows

02:08 future storage the idea behind winfs was

02:11 to replace or augment the traditional

02:13 file system known as NTFS with a

02:15 database driven system the goal was to

02:17 be able to instantly search and organize

02:19 all of your files by their content tags

02:21 relationships and so on not just by file

02:24 names and folders your documents emails

02:27 photos and everything would actually

02:28 live in a database so that fin a file or

02:30 grouping information would be as easy as

02:32 querying data it was a bold plan to move

02:35 beyond the decades old metaphor of files

02:37 and folders into a richer smarter way of

02:39 storing information another pillar of

02:41 LongHorn's Vision was deep integration

02:43 of Microsoft's new NET Framework into

02:45 Windows now net was a managed code

02:48 platform meaning it was a memory safe

02:50 modern programming model that had

02:51 debuted in the early 2000s the longhorn

02:54 team wanted to leverage net to modernize

02:56 Windows development that meant new apis

02:59 and sub systems written in managed code

03:01 instead of the good old C++ win32 all

03:04 the way for example Longhorn introduced

03:06 Avalon a code name for the new

03:08 presentation subsystem essentially a

03:09 Next Generation graphical user interface

03:11 framework built

03:13 onnet Avalon itself would later become

03:15 known as the windows presentation

03:17 Foundation there was also Indigo a new

03:19 Communications and web services

03:21 framework later known as Windows

03:23 communication Foundation these were all

03:25 part of what Microsoft at the time

03:27 called the Winx Technologies signaling

03:29 that Longhorns developers were pushing

03:31 towards manage code and new Frameworks

03:33 for the future of apps it's not that the

03:35 windows kernel itself would be Rewritten

03:37 in C that was never the case or planned

03:40 but much of the user level

03:41 infrastructure and apis were planned to

03:43 get this net based overhaul bringing

03:45 safer code and quicker development to

03:47 Windows and we can't forget the user

03:49 interface dreams Longhorn was slated to

03:52 entirely revamp the windows UI with a

03:54 design language later dubbed Arrow a

03:56 clean glass-like visual Style with fancy

03:58 transparent effects animations and a

04:00 desktop composition engine to take

04:02 advantage of 3D Graphics Hardware

04:05 Windows xp's colorful Luna interface was

04:07 going to be yesterday's news Longhorn

04:09 would be Sleek modern and Visually Rich

04:12 features like a sidebar with gadgets for

04:14 weather news stocks and so on were

04:16 prototyped even the start menu and

04:18 taskbar were being

04:20 reimagined essentially Microsoft wanted

04:22 Longhorn to look and feel like a major

04:24 step into the future and under the hood

04:25 it truly was intended to be at the 2003

04:29 professional develop velers conference

04:30 or PDC Microsoft gave developers a

04:32 tantalizing Peak at Longhorn's promised

04:34 features in UI they demoed concept

04:37 screen showing a sidebar with live tiles

04:39 translucent Windows frames and a snaz

04:41 your start menu it felt like looking at

04:43 windows but a couple years into the

04:45 future internally folks were generally

04:47 amped at least at first Avalon Indigo

04:50 and winfs were often called the three

04:52 pillars of Longhorn Microsoft even

04:54 handed out early Longhorn builds to PDC

04:56 attendees a build actually numbered 4051

04:59 to showcase some of these Technologies

05:02 the press and developer Community were

05:03 buzzing about how Longhorn might change

05:05 everything it's not often that an

05:07 operating system promises to reinvent

05:09 multiple core pillars all at once

05:11 Longhorn was aiming for the sky but and

05:14 you knew a butt was coming big Ambitions

05:17 often come with big challenges as

05:19 development ramped up Longhorn started

05:21 to show signs that it was buckling under

05:22 its own weight those of us inside

05:25 Microsoft are connected to the project

05:26 could see these storm clouds gathering

05:28 on the horizon even as the hype was

05:30 building the project was in trouble and

05:32 it would soon become obvious to

05:33 everybody one major problem was that

05:35 with so many new features being

05:37 developed simultaneously the windows

05:39 code base itself became fragile and

05:40 Bloated early pre-release builds of

05:43 Longhorn when tested were not pretty I

05:45 recall colleagues testing these Builds

05:47 on high NPCs of the time and reporting

05:49 that memory usage went through the roof

05:51 and a big culprit was wifs it was an

05:54 amazing concept but the early

05:55 implementation was pretty memory hungry

05:58 testers noted that the winfs service

05:59 would gobble up RAM and CPU Cycles

06:02 endlessly in one build Outlook Express

06:04 the mail client had been modified to

06:06 store its emails in winfs and when winfs

06:09 bogged down it would take your email

06:10 down with it many testers simply

06:12 disabled winfs to get any usable

06:14 performance out of the system that's not

06:17 a great sign for a flagship feature

06:19 performance and memory issues were only

06:21 one facet stability was another the

06:24 development process for Longhorn was to

06:25 put it kindly chaotic with teams pouring

06:28 in new code for Avalon for Indigo and

06:30 the new desktop window manager for the

06:32 revamp shell and so on the integration

06:35 all these pieces became a nightmare we

06:37 had a tradition at Microsoft called Dog

06:39 fooding meaning using our own daily

06:41 builds of the OS to do our actual work

06:43 for Longhorn dog fooding was tough

06:45 builds were often too unstable to run

06:47 for very long the degree to which eating

06:49 dog food is tolerable can be measured in

06:51 the direct proportion to how good the

06:53 dog food actually is and this was not

06:55 good dog food I heard reports at the

06:57 build lab the team that compiles the

06:59 windows Source into actual installable

07:01 builds was constantly broken developers

07:04 would check in code that unknowingly

07:05 broke something else and it became

07:07 increasingly difficult to get a single

07:08 build of Longhorn where all the big

07:10 features work together without major

07:12 bugs one legendary Microsoft engineer

07:15 Dave Cutler the father of Windows NT

07:17 later quipped that the longhorn guys

07:19 just couldn't get Longhorn out of the

07:20 build lab that's a biting way to say the

07:22 team was writing code faster than they

07:24 could stabilize it now add to this mix

07:26 the challenge of backward compatibility

07:29 when Windows has always prided itself on

07:31 running older applications supporting a

07:33 vast array of hardware and basically not

07:35 breaking what people already have with

07:37 Longhorn this was extraordinarily hard

07:40 the new graphics engine meant that old

07:41 display drivers had to be Rewritten or

07:43 to run in compatibility modes the new

07:46 storage engine winfs was a radical

07:48 change that no third party software had

07:50 ever seen before and parts of the OS

07:52 were being refactored into manage.net

07:54 code which was unproven yet at such

07:57 scale ensuring that existing software

07:59 Services would continue to work on this

08:01 new fangled Longhorn was a massive

08:02 undertaking if you push too far with

08:05 something like winfest or a new security

08:06 model you might break a critical

08:08 Enterprise app or somebody's favorite

08:10 utility the longhorn team was walking a

08:12 tight RPP innovate aggressively but

08:14 don't break Windows not an easy

08:16 Balancing Act and then came an external

08:19 factor that really threw a wrench into

08:20 LongHorn's timeline Security in mid2

08:24 2002 Bill Gates sent his famous

08:25 trustworthy Computing memo essentially

08:28 mandating that security reliability

08:30 would become top priority across

08:32 Microsoft this was largely in response

08:34 to the wave of computer worms and

08:35 viruses such as code red nimda and the

08:38 Blaster worm in 2003 that were

08:40 exploiting Windows weaknesses the

08:43 windows team had to pause and secure the

08:44 house that meant diverting a lot of

08:47 developers to work on Windows XP Service

08:49 Pack 2 a major security focused update

08:51 and on server 2003 which was released in

08:54 2003 of course to make sure that those

08:56 were solid Long Horn development slowed

08:59 as many Engineers including myself were

09:01 retasked with improving the security of

09:03 Windows XP this was absolutely the right

09:05 call for customers XP needed those fixes

09:08 but it further delayed Longhorn and

09:09 Scattered the team features that weren't

09:11 near completion kept hanging out in a

09:13 half-done state while attention shifted

09:15 elsewhere by 2004 the organizational

09:18 chaos around Longhorn was becoming

09:20 evident internally there was a lot of

09:22 feature creep more and more ideas being

09:24 thrown into the mix without a realistic

09:26 plan for finishing them in any

09:28 reasonable time frame it felt like every

09:30 group had some cool Innovation they

09:32 wanted Longhorn to include and for a

09:34 while management seemingly said yes to

09:36 almost all of them the vision was Grand

09:38 perhaps too Grand one Observer later

09:41 described that his features being

09:42 written at an alarming rate with a

09:44 significant lack of QA or vision of true

09:46 requirement ouch morale and the team

09:49 started to slip it's demoralizing as an

09:52 engineer when you can see the light of

09:53 the end of the tunnel getting further

09:54 away and not closer some devs were

09:57 burning out from the long hours trying

09:58 to make all the moving Parts work others

10:00 grew frustrated that so much was being

10:02 built only to collapse every time the

10:04 latest build failed there was a real

10:06 fear that maybe this thing would never

10:08 quite come together around this time I

10:10 took a three-month sabatical and to make

10:12 a long story short I retired instead of

10:14 coming back part of it was that I never

10:16 drank the longhorn Kool-Aid some of it

10:19 was very cool don't get me wrong but I'm

10:21 an incrementalist not a revolutionary I

10:23 prefer to add things one solid feature

10:25 at a time rather than Reinventing

10:27 everything all at once as part of some

10:28 Grand Vision

10:29 but at the end of the day even though it

10:31 was just a small factor in my decision

10:32 to retire it almost seems like I dodged

10:35 a bit of a bullet as from what I heard

10:36 things didn't only got worse a

10:38 particularly telling anecdote from this

10:40 era comes from Dave Cutler the engineer

10:42 I mentioned earlier and if you haven't

10:44 seen my interview with Dave yet be sure

10:45 to check it out after this video in my

10:47 interview he shared his perspective on

10:49 Longhorn Cutler was leading a parallel

10:51 effort a version of Windows for 64-bit

10:53 processors based on the stable Windows

10:56 Server 2003 code he watched the longhorn

10:59 project with a critical eye he even

11:01 nicknamed it doesn't matter horn a pun

11:03 suggesting that longhorn didn't matter

11:05 or might never ship the reason he saw

11:08 that the client team was prioritizing

11:09 flashy features over solid engineering

11:12 and Chris says oh I can't live with that

11:15 says consumers don't expect the quality

11:18 that that the server people do we can do

11:21 it in a year and a half thereupon we

11:24 split the code base the server went one

11:26 way and the consumer vision went the

11:28 other way it wasn't long before the

11:31 consumer software hardly would build and

11:33 hardly would run so they're continuing

11:35 on with this buggy code base without all

11:38 those security fixes in it meantime we

11:40 got long horn over here still going and

11:44 its name is now morphed into does it

11:46 matter horn there was an internal split

11:49 the longhorn client team was churning

11:50 out new features quickly with the

11:51 attitude that consumer Windows could be

11:53 less rigorously engineered than server

11:55 Windows while the server team folks like

11:57 Cutler took a slower more methodical

12:00 approach to ensure stability at one

12:02 point Cutler noted how bad things had

12:04 got and basically told management This

12:06 is BS not the word I'm sure he used but

12:08 you guys should probably switch the code

12:10 base to the one the server team has been

12:11 working on all along we turned over some

12:14 code that you know like a shovel you

12:17 turnning over manure he was advocating

12:19 for scrapping LongHorn's messy core and

12:21 instead using the KN and good core from

12:23 Windows Server which by then included

12:25 all security improvements and the solid

12:26 groundwork from xps2 and server 03 you

12:30 can imagine that within Microsoft this

12:32 was a heated discussion it's never

12:34 Pleasant to consider throwing away years

12:36 of work and it certainly Bru am igos to

12:37 admit that the longhorn project had gone

12:39 too far off track then came the breaking

12:42 point in the summer of 2004 Microsoft's

12:45 leadership made a dramatic Decision One

12:47 almost unheard of at that scale they hit

12:49 the reset button on all of Longhorn on

12:52 August 27th 2004 it was publicly

12:54 announced that longhorn as it existed

12:56 was being reset practically this meant

12:58 that the existing Longhorn codebase

13:00 would be scrapped and development would

13:02 start fresh from the Windows Server 2003

13:04 sp1 codebase the team would then

13:06 carefully read the most important

13:08 Longhorn features on top of that stable

13:10 Foundation this was a massive course

13:12 correction now I left before the reset

13:15 but I remember hearing about the

13:16 announcement it was shocking even

13:17 internally imagine telling hundreds of

13:19 developers and testers all that work

13:21 that you've done for the past three

13:22 years we're going to set that aside and

13:24 do something else it was devastating and

13:27 yet oddly enough a relief for some some

13:29 devastating because nobody wants to see

13:31 their hard work tossed out but a relief

13:33 because by this point everybody knew it

13:35 wasn't working the project had become a

13:37 death march of sorts and now there was a

13:39 chance to make a fresh start the reset

13:41 also meant significant changes in scope

13:43 a lot of those Pie in the Sky features

13:45 had to be cut or postponed to later

13:47 releases the most high-profile casualty

13:49 was indeed winfs Microsoft announced

13:52 that winfs would not ship with the next

13:54 version of Windows it was simply too

13:56 behind schedule and too problematic they

13:58 did continue developing winfs separately

14:00 for a while there were even beta

14:02 releases of winfs for testers a year or

14:04 two later but ultimately winfs never

14:07 made it into a production Windows

14:08 release it was a case of an idea ahead

14:11 of its time brilliant but impractical to

14:13 ship back in

14:14 2006 another feature NextGen secure

14:17 Computing also known as Palladium which

14:20 was an ambitious security initiative was

14:21 also dropped from the release road map

14:24 Microsoft had to be ruthless only

14:26 including features that could be

14:27 realistically completed and stabilized

14:29 in the new time frame essentially

14:31 Longhorn had to be res scoped to

14:33 something achievable and so the team

14:34 regrouped they took Windows Server 2003

14:37 sp1 which was a solid reliable version

14:39 of Windows and used that as the new core

14:41 for Longhorn and from there they began

14:44 reintegrating those salvageable Parts

14:46 this time they applied the lessons

14:48 learned the development was much more

14:50 disciplined features like Avalon the new

14:52 graphics UI stack and indigo for

14:54 communications were still in because

14:56 they were far enough along and important

14:57 enough the new new desktop Window

14:59 Manager enabling those Arrow effects was

15:01 also retained but now everything was

15:03 built on a no unstable base instead of

15:05 that shaky

15:08 pre-retcon being followed client windows

15:11 and server windows were unified on the

15:12 same core going forward no more

15:15 Divergence where the server is stabled

15:16 and the client is a wild experiment they

15:19 would continue to share the same

15:20 fundamentals and indeed ever since that

15:23 reset Microsoft has kept client and

15:25 server Windows unlock step on a single

15:27 code base even if the releases don't

15:28 alow

15:29 which is a huge positive Legacy of this

15:31 Saga the development after 2004 was

15:34 essentially a Mad Dash to get the new

15:35 Longhorn now truly Windows version 6

15:38 ready to ship by mid 2005 Microsoft felt

15:41 confident enough to give it an official

15:43 product name Windows Vista the word

15:45 Vista was meant to evoke a beautiful

15:47 view a fresh perspective probably to

15:49 distance itself from the negativity

15:51 surrounding LongHorn's delays as Vista

15:53 took shape it became clear that it would

15:55 deliver some of LongHorn's promise but

15:57 not all so what made it and what didn't

16:00 well Vista what was once to be Longhorn

16:02 did ship with a lot of visible

16:04 enhancements the arrow gooey made it the

16:06 prime time Vista introduced the

16:08 translucent glass window frames smooth

16:10 animations and a new start menu with

16:11 integrated search the sidebar with

16:13 gadgets also appeared you could have a

16:15 clock weather RSS feed and so on on your

16:18 desktop sidebar a direct descendant of

16:20 the longhorn sidebar concept the instant

16:23 search capability was present through

16:24 the Explorer and start menu thanks to an

16:26 indexing service now this wasn't win s

16:29 the files were still on NTFS but you had

16:31 a fast index to search files and even

16:33 their file metadata which delivered some

16:35 of the user experience that winfs had

16:36 aimed for in Vista if you hit the start

16:38 button and start typing results pop up

16:40 almost instantly and that was new and it

16:42 felt pretty magical compared to the old

16:44 Windows XP search dog you do remember

16:46 the little search dog helper right Vista

16:49 also brought in the Avalon Graphics

16:51 infrastructure as the windows

16:52 presentation Foundation or WPF even if

16:55 the OS itself only used WPF in a few

16:57 places like parts of the media Center

16:59 app and certain system apps Indigo

17:01 shipped as well renamed to WCF enabling

17:04 modern ways for applications to

17:05 communicate over networks these were

17:07 delivered as part of The NET Framework

17:09 3.0 that came with Vista essentially

17:11 fulfilling the plan of integrating those

17:13 net pillars into Windows on the security

17:15 front the lessons of 2003 to 2004 were

17:18 deeply ingrained in Vista it shipped

17:21 with user account control a feature that

17:23 while annoying to many users initially

17:24 was a direct result of the new security

17:26 mindset even administrators would run

17:29 with limited privileges most of the time

17:31 to prevent malware or accidental changes

17:33 from Wrecking the system internally

17:34 Vista had been engineered with a much

17:36 more rigorous security development life

17:38 cycle meaning that more threat modeling

17:40 code reviews and testing for

17:41 vulnerabilities was done than earlier

17:43 windows so in many ways Vista was more

17:45 solid under the hood than even XP had

17:47 been even if it had got a reputation for

17:48 being a bit heavy that said vista's

17:51 launch in late 2006 wasn't all smooth

17:53 sailing although the development did

17:55 coales and Vista shipped it arrived with

17:57 a bit of a mixed reception many of you

17:59 probably remember the stories or

18:00 experienced it yourself Vista was

18:02 reasonably resource heavy and if you

18:04 tried to run it on a machine that was

18:06 fine for XP but not much more you were

18:08 likely in for a bad time it really

18:10 needed a decent GPU for the arrow

18:12 feature and more RAM than was common on

18:14 PC sold just a few years prior some

18:17 drivers weren't ready or were unstable

18:19 because Hardware vendors had trouble

18:20 keeping up with the changes the graphics

18:23 driver model in particular had changed

18:24 significantly to accommodate the new

18:26 desktop window manager so a lot of

18:28 people who upgr early on had issues with

18:30 devices not working or with system

18:32 crashes the Press was pretty harsh about

18:34 vista's problems and it gained a bit of

18:36 an unfair stigma I say unfair because

18:38 with a few updates and on proper

18:40 Hardware Vista was actually a pretty

18:41 solid OS but first impressions tend to

18:44 stick nonetheless Microsoft had

18:46 delivered what Longhorn became it was no

18:49 longer vaporware or endless beta Vista

18:51 was real for better or worse now

18:53 stepping back you might wonder was the

18:55 longhorn project a failure well yes and

18:57 no it failed to deliver on its original

19:00 promises when a Fest never shipped and

19:02 many of the more radical ideas were cut

19:04 and the schedule slipped dramatically

19:06 after all Vista arrived more than 5

19:08 years after XP whereas originally

19:10 Longhorn was thought of as a three-year

19:12 or less Gap it was also something of a

19:14 management failure and that it took a

19:16 near crisis for Microsoft to course

19:18 correct but LongHorn's Legacy is complex

19:21 and in many ways positive for one the

19:23 reset and recovery from Longhorn shaped

19:25 Microsoft's culture and Engineering

19:27 practices going forward the fact that

19:29 they eventually pulled a workable Vista

19:31 out of the disastrous Longhorn effort is

19:33 a testament to the company's ability to

19:34 learn and adapt albeit painfully post

19:37 Vista the windows team adopted more

19:39 disciplined planning the very next

19:41 release Windows 7 which came in 2009 was

19:43 essentially Vista done right and it

19:45 polished and optimized everything that

19:47 Vista introduced and it was a huge

19:48 success without The Crucible of Longhorn

19:51 Vista Windows 7 might not have been as

19:53 good as it was in fact a lot of folks

19:55 who skipped Vista and went straight to

19:57 Windows 7 were indirectly enjoying the

19:59 fruits of LongHorn's ambitious features

20:01 just in more refined form today whether

20:03 on Windows 10 11 Mac OS or even your

20:06 smart phone you expect to hit a search

20:08 box and find files or information

20:10 reasonably instantly win ifs's Grand

20:12 Vision didn't materialize but it

20:14 definitely push the envelope on what

20:15 users would come to expect Microsoft

20:18 ended up building a robust indexing

20:19 service into Windows first in Vista and

20:22 improved in later versions and

20:23 introduced the idea of libraries in

20:25 Windows 7 libraries are virtual folders

20:27 aggregating cont content type something

20:29 like what wiest's promise of organizing

20:31 by metadata would have done on the

20:34 developer side The NET Framework became

20:36 a core part of Windows development Vista

20:38 ship. net 3.0 and since then net has

20:41 grown by Leaps and Bounds and today we

20:42 have net 9 a huge ecosystem of apps and

20:45 tools built upon it the idea of using

20:48 manage code for safety and productivity

20:50 is now pretty mainstream at Microsoft

20:52 consider that Microsoft's latest

20:53 Frameworks and even parts of Windows 10

20:55 like the new Settings app parts of the

20:57 new start menu and so on use net under

20:59 the hood Longhorn was the inflection

21:01 point where net moved from a fringe

21:03 developer option to a core Windows

21:05 technology another Legacy the emphasis

21:08 on security from the longhorn reset era

21:10 stuck modern Windows starting with Vista

21:12 has a security architecture that's much

21:14 more robust UAC driver signing

21:17 sandboxing features and so on all took

21:19 root in that time frame while users

21:21 grumbled about permission prompts in

21:23 hindsight that was a necessary Evolution

21:26 if Longhorn hadn't hit the wall maybe

21:28 those security lessons would have come

21:29 even later with even more costly

21:31 consequences during the age of internet

21:33 connectivity and perhaps the biggest

21:35 lesson Longhorn taught was about project

21:37 management and focus you can have the

21:39 best engineers in the world and

21:40 Microsoft had plenty of brilliant people

21:42 on Longhorn but if the project lacks

21:44 clear Focus or if priorities keep

21:46 shifting and if you're trying to do too

21:47 much at once you can easily get a big

21:49 mess instead of a great product after

21:51 Longhorn Vista Microsoft became a lot

21:53 more careful about not letting Windows

21:55 projects get so unwieldly the cycle of

21:57 huge monolithic Windows releases gave

21:59 way to a more incremental approach and

22:01 eventually the windows is a service

22:02 model in Windows 10 it's ironic because

22:05 even though Longhorn aim to

22:06 revolutionize everything in one go the

22:08 way it actually influenced Windows was

22:10 by prompting it to a more evolutionary

22:12 Improvement in the future just the way I

22:14 like it from a personal perspective as

22:16 somebody who lived through some of the

22:17 longhorn Saga from the inside and watch

22:19 the rest from the outside it's a

22:20 fascinating cautionary tale it shows

22:23 that even a company with virtually

22:24 Limitless resources and a track record

22:26 of shipping big products can get in over

22:28 its head

22:29 the story of Longhorn is one of huus and

22:31 humility Microsoft reached for the Stars

22:33 stumbled but then humbled itself to

22:35 regroup and ultimately deliver something

22:37 worthwhile and many of the Innovations

22:39 did survive in some form it just took a

22:41 couple of releases and several more

22:42 years to fully B them so that's the

22:45 story of Longhorn in a nutshell a dream

22:47 of a revolutionary OS an epic struggle

22:49 to deliver it and a dramatic reset and

22:51 then ultimately the birth of Windows

22:53 Vista a scarred but significant

22:55 milestone in the windows lineage it's a

22:57 story of overreaching by also of

22:58 learning and recovery and it left an

23:00 imprint on all windows releases that

23:02 followed if you found this sneak peek

23:04 behind the scenes informative or

23:05 interesting please remember that I'm

23:06 mostly in this for the subs and likes so

23:08 I'd be honored if you consider leaving

23:09 me one of each before you go today and

23:11 if you're already subscribed thank you

23:13 if you've got a question or comment

23:15 about this video please put it in the

23:16 comments and once a week not only do we

23:18 genuinely read them online we also go

23:20 through and we answer them every Friday

23:22 on shop talk be sure to check it out on

23:24 the Dave attic Channel which is a

23:25 separate Channel but you can go there

23:27 and find episodes going back for several

23:29 months of shop talk and I think or at

23:31 least I hope that you'll enjoy them in

23:33 the meantime and in between time hope to

23:35 see you next time right here in Dave's

23:37 Garage

