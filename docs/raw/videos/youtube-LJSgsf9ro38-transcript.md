---
source_url: https://www.youtube.com/watch?v=LJSgsf9ro38
source_type: video
ingested: 2026-09-15
published: 2026-09-15
duration_minutes: 22
language: en
sha256: 29c6d2c0dfe6644dcb5faffb8cf6af12c8537875c00638cd266c85ac0f7f9769
time_sensitive: True
---

# YouTube Transcript: The Controversial Flock Cameras Tracking Every Car — Full Breakdown

## Video Information
- **Title**: The Controversial Flock Cameras Tracking Every Car — Full Breakdown
- **Video ID**: LJSgsf9ro38
- **Published**: Unknown
- **Views**: Unknown
- **Language**: en

## Transcript
00:00 There's a camera sitting beside a road

00:01 somewhere near you right now that

00:03 doesn't care if you're speeding, doesn't

00:04 write tickets, and might not even be

00:06 recording actual video. But the moment

00:08 your car rolls past, it can read your

00:10 license plate, guess the make, model,

00:13 color, and body style, log the exact

00:15 time, location, and direction, fire that

00:17 data up over the cellular network, and

00:19 make the whole event searchable in just

00:21 seconds. One photo, not very exciting.

00:24 But link thousands of those cameras into

00:26 one database, and each photo becomes a

00:28 breadcrumb. Connect enough breadcrumbs

00:30 and you've got an interesting trail. And

00:33 that in a nutshell is the promise and

00:35 the controversy of flock safety cameras.

00:38 Police departments say these systems

00:39 help recover stolen vehicles, find

00:41 missing people, catch getaway cars, and

00:43 turn a vague gray SUV witness

00:45 description into real investigative

00:47 leads. Privacy advocates counter that

00:50 the same network quietly builds a

00:51 searchable record of where everyday

00:53 people drive without asking permission,

00:55 without probable cause, and without a

00:57 warrant. Today, I'm not here to cheer

00:59 for one side or dunk on the other.

01:01 Instead, I'm going to tear the

01:02 technology apart conceptually, following

01:04 the bits from the roadside into the

01:06 cloud, see what exactly the system

01:08 records, including what it doesn't know,

01:10 and examine the real benefits, the real

01:13 risks, the safeguards, the loopholes,

01:15 and the tough legal questions. Now, I

01:17 fancy myself something of a law-abiding

01:19 libertarian, which means I guess I think

01:21 there should be as few laws as are

01:22 necessary, but people should at least

01:24 follow the ones that we have. And that's

01:26 part of the problem with Flock cameras

01:28 because, as you'll see, the camera

01:30 itself is almost the least interesting

01:32 part. The best known Flock product is

01:34 the Falcon automated license plate

01:36 reader or ALPR. Physically, it is a

01:40 compact roadside camera that can be

01:41 installed without trenching in power or

01:43 network cabling. Many installations use

01:45 a solar panel for power and an LTE

01:47 cellular modem for connectivity, which

01:49 means a camera can be placed at a

01:51 subdivision entrance, an intersection, a

01:53 parking lot, or a rural road without

01:55 waiting for somebody to pull Ethernet

01:57 through the sewer system. Flock handles

01:59 much of the installation and operates

02:00 the system as a subscription service

02:02 rather than merely selling a camera in a

02:04 box. That architecture is one reason the

02:07 system is spread so quickly. Traditional

02:09 municipal camera projects become

02:11 miniature public works programs

02:12 involving poles, permits, power drops,

02:15 fiber, network closets, and a conference

02:17 room full of people debating who owns

02:18 the conduit. But a self-contained solar

02:21 and cellular node skips much of that.

02:23 It's essentially an internet of things

02:25 device with a badge nearby. And if you

02:27 can get power to it and it's in cell

02:29 range, that's all it needs.

02:31 Conceptually, the image processing

02:33 pipeline works much like any other

02:34 modern machine vision system. First, the

02:37 camera needs an exposure that freezes a

02:39 moving vehicle without turning the plate

02:40 into a white reflective rectangle. The

02:43 software then identifies a vehicle and

02:45 plate region within the frame, corrects

02:47 for angle and perspective, separates the

02:49 individual characters, performs optical

02:51 character recognition, and normalizes

02:54 the result into a candidate plate

02:55 number. At the same time, additional

02:57 computer vision models classify the rest

02:59 of the vehicle. Is it a sedan, a pickup,

03:02 an SUV, or what is it? Is it red, gray,

03:05 blue, or a color best described as

03:07 rental car beige? What manufacturer and

03:09 model does it most resemble? Are there

03:11 visible roof racks, bumper stickers,

03:13 damage, or other distinguishing

03:15 characteristics? Flock refers to this

03:17 collection of characteristics as a

03:19 vehicle signature, or a vehicle

03:20 fingerprint. Its current search tools

03:22 can use plate numbers, partial plates,

03:24 make, model, color, location, time, and

03:27 natural language descriptions such as a

03:29 white sports car with a racing stripe.

03:31 The company also advertises location

03:34 searches, convoy analysis, hot lists,

03:36 custom alerts, and real-time routing

03:38 tools. Now, it matters a lot to me

03:40 personally where the characterization is

03:42 actually done. If it's all happening on

03:44 the device using a entirely local model,

03:46 I'd be both impressed and relieved.

03:49 Impressed because that's a lot of AI

03:50 juice to squeeze for a little box like

03:52 this, and relieved because it would then

03:54 mean that the images of you in your car

03:56 never leave the box. If the block cannot

03:59 and does not store them and they can

04:00 never leave, I could give this thing a

04:02 pass. But there are just two problems.

04:04 First, the precise division of labor

04:06 between the processor inside the camera

04:08 and the software in Flux Cloud is an

04:10 implementation detail that is not

04:12 publicly documented deeply enough for us

04:14 to draw any reliable conclusions or make

04:16 even a block diagram. But in so far as I

04:19 can tell, every detection is forwarded

04:21 as both an image and a set of extended

04:23 metadata about that image. So, it's not

04:26 just recording the fact that your

04:27 license plate value is spotted on your

04:29 blue BMW a mile from your house. It's

04:31 also sending the image this time and

04:34 every time that it sees you. And that

04:36 database of images and metadata is where

04:38 the system stops being merely a camera

04:40 and starts becoming something more like

04:42 Google for cars. Suppose a convenience

04:44 store camera captures a gray SUV leaving

04:47 right after a robbery. The plate is

04:49 unreadable, but the vehicle has a roof

04:51 rack and damage to the left rear bumper.

04:53 An investigator can search nearby flock

04:56 cameras for gray SUVs matching those

04:58 characteristics during the relevant time

05:00 window. Instead of manually watching 6

05:02 hours of footage from 20 cameras, the

05:05 investigator gets a much smaller set of

05:07 candidate vehicles. Doesn't prove that

05:09 any of them was involved and it does

05:11 produce leads. If the plate number is

05:13 already known, the search becomes much

05:15 more direct. Enter the plate and the

05:17 system can return the points where the

05:18 participating cameras observe that plate

05:20 during the retention period. A single

05:23 camera tells you that the vehicle passed

05:25 one location at one time. Multiple

05:27 cameras can show a direction or a route.

05:30 More cameras produce a more complete

05:31 route. And this is the semantic fault

05:34 line running through the entire debate.

05:36 Flock describes its core ALPR product as

05:39 taking point-in time images of vehicles

05:41 on public roads rather than continuously

05:43 tracking people. And that is technically

05:46 accurate. There's no transmitter

05:48 attached to your axle and the Falcon

05:49 does not follow you home like a tiny

05:50 airborne probation officer. But critics

05:53 respond that querying many point in time

05:56 observations is still a form of

05:58 tracking. And that is also technically

06:00 accurate because just as a movie is

06:02 merely a sequence of still images, a

06:04 travel history is merely a sequence of

06:06 timestamp locations. The distinction

06:08 becomes less meaningful as camera

06:10 density or image frequency arises. For

06:12 those of you who took a little sequel in

06:14 college, think of it this way. The

06:16 individual records are not where the

06:18 power lives. The power lives in the join

06:20 across tables. The license plate reader

06:23 also operates as a real-time alerting

06:25 system. Police can subscribe to what are

06:27 commonly called hot lists. These may

06:29 include license plates associated with

06:31 stolen vehicles, wanted suspects, Amber

06:34 or Silver alerts, missing people, or

06:36 other active investigations.

06:38 Flock says it system integrates with

06:40 criminal justice databases such as the

06:42 National Crime Information Center. When

06:44 a matching plate passes a camera, the

06:46 system can notify officers or analysts

06:48 immediately. From a software

06:50 perspective, this is a classic publish

06:52 and subscribe system. The hot list

06:54 contains events of interest. The

06:55 roadside cameras publish vehicle

06:57 detections. The platform compares each

07:00 event against the subscriptions and

07:01 pushes an alert when there's a match.

07:03 And speed matters, not of the vehicle,

07:05 but of the report. A stolen vehicle

07:08 report that's checked manually tomorrow

07:09 is just an investigative record. But a

07:11 detection delivered to an officer 30

07:13 seconds after the car passes an

07:15 intersection can become an interception.

07:17 And an interception can end or prevent a

07:19 crime. Not in a minority report kind of

07:22 way, but in their there was actually a

07:23 cop there when I needed one way. Police

07:26 departments using these systems describe

07:28 them as valuable for recovering stolen

07:29 vehicles, locating missing or endangered

07:32 people, responding to crimes in

07:33 progress, corroborating timelines, and

07:36 identifying vehicles when witnesses can

07:37 provide only a partial description. Some

07:40 cities report successful recoveries and

07:41 arrests, although attributing a change

07:43 in overall crime rates specifically to

07:46 cameras is much harder than documenting

07:48 individual cases in which a detection

07:50 was actually useful. And that

07:51 distinction is important. A screwdriver

07:53 can unquestionably repair a machine, but

07:55 proving that buying more screwdrivers

07:57 reduce mechanical failures throughout

07:59 the city is a much larger statistical

08:01 problem. Case utility and crime

08:04 reduction are not the same metric. The

08:06 camera also does not know who is

08:08 actually driving. Now, a separate law

08:10 enforcement data system may connect that

08:12 plate with the registered owner, but the

08:14 registered owner might not be behind the

08:15 wheel. The vehicle might be borrowed or

08:18 rented or sold without updated records,

08:20 carrying a stolen plate or displaying a

08:21 temporary plate printed by a homing jet

08:23 printer that has begun to reconsider its

08:25 life choices. Flock says that its core

08:28 LPR system does not use facial

08:29 recognition and is designed to collect

08:31 vehicle information rather than

08:33 identifying the occupants. Some

08:35 municipalities also state that their

08:37 deployments are not connected directly

08:38 to the DMV or commercial vehicle history

08:40 databases. But because law enforcement

08:43 can use other authorized databases, a

08:45 plate observation can still become

08:47 associated with the person during an

08:49 investigation. So calling license plate

08:51 data either a personally identifiable or

08:53 completely anonymous misses the nuance.

08:56 Your plate is not your face, but neither

08:57 is it a random number with no connection

08:59 to human activity. It's more like an IP

09:01 address. By itself, it identifies a

09:04 device or vehicle with additional

09:06 records and context that can often be

09:08 connected to a person. And then there is

09:10 accuracy. ALPR is an inference system,

09:13 not a divine revelation engraved on a

09:15 stone tablet. Rain, glare, darkness,

09:18 plate frames, dirt, motion blur, unusual

09:21 fonts, damage, viewing angle, and

09:23 visually similar characters can all

09:25 affect the read. A seven can become a

09:27 two. The letter O can become a zero. One

09:30 state's plate design can look like it

09:32 was created specifically to defeat

09:33 machine vision and possibly human vision

09:35 as well. And in some parts of Canada,

09:37 plates aren't even rectangles, they're

09:39 bears. model. Internally, the

09:41 recognition model will normally produce

09:43 a candidate result and some measure of

09:45 confidence. Setting a strict confidence

09:48 threshold reduces false matches but can

09:50 miss legitimate plates that would

09:52 otherwise be read. Relaxing the

09:54 threshold catches more possibilities but

09:56 increases false positives. This is the

09:59 same precision versus recall trade-off

10:01 that appears in spam filters, medical

10:02 screening, antivirus software, and every

10:04 other detector that must decide whether

10:07 something looks enough like a target.

10:09 From a programming standpoint,

10:10 heruristics are useful, but they are by

10:12 definition imperfect. And that is why a

10:15 responsible deployment treats a plate

10:17 reader alert as a lead requiring

10:19 confirmation, not as probable cause

10:21 descending directly from the cloud. Here

10:23 in Redmond, Washington, for example,

10:25 they say that alerts must be verified

10:26 before any action is taken. Other

10:29 policies likewise require officers to

10:31 visually confirm the plate and check

10:32 that the hot list entry remains still

10:34 valid. This procedural distinction

10:37 matters enormously. If the computer says

10:39 a stolen black Range Rover just passed

10:41 by, an officer should verify that the

10:42 photograph actually shows the correct

10:44 plate, that the alert has not expired,

10:46 and that the vehicle description makes

10:48 sense. An algorithmic match plus human

10:51 confirmation can be a useful tool. An

10:53 unverified match followed by a

10:55 high-risisk felony style stop can turn

10:57 one mistaken character into a very

10:58 frightening encounter or worse.

11:01 Documented ALPR errors and incorrect hot

11:03 list entries have resulted in innocent

11:05 motorists being detained and sometimes

11:06 they're at gunpoint. Those incidents do

11:09 not mean every alert is unreliable, but

11:10 to the extent that an exception

11:12 disproves the rule, they also

11:14 demonstrate why the human validation

11:16 step cannot be treated as optional

11:18 ceremonial paperwork. Now, we arrive at

11:20 privacy, where the details matter more

11:22 than the slogans. Flock's default

11:24 retention period for license plate data

11:26 is 30 days. The company says images and

11:29 metadata are encrypted during

11:30 transmission and at rest with cloud data

11:32 protected using AE26 encryption.

11:35 According to its policy, information

11:38 remains on the roadside camera only

11:39 temporarily and is removed after upload

11:42 and is hard deleted from the cloud when

11:43 the retention period expires unless

11:45 another period is required by law or

11:47 established in the customer agreement.

11:50 30 days is not forever and that's a

11:52 meaningful safeguard. A short rolling

11:54 window limits how far into the past an

11:56 ordinary search can actually reach. It

11:58 also reduces the consequences of a

12:00 database breach compared with preserving

12:02 years and years of travel records. But

12:04 default is not the same thing as

12:06 universal. Local laws and contracts can

12:09 require or permit different retention.

12:12 Now, Flock says that an agency seeking

12:14 extended retention beyond the legal

12:16 requirements can obtain up to one year,

12:17 but the company requires approval from

12:20 an elected official or governing body.

12:22 An evidence downloaded from the system

12:24 for a legitimate cause can be retained

12:26 under the AY's own separate evidence

12:28 policies after it disappears from the

12:30 live flock database. In other words,

12:33 automatic deletion applies to the

12:34 platform's rolling data store. It can't

12:37 make a screenshot already exported into

12:39 a case file spontaneously evaporate like

12:41 an old Mission Impossible tape. Once

12:44 it's in the wild, so to speak, it's a

12:45 bell that can't be unrung. Flock also

12:48 says that the customers own their data

12:50 and that it does not sell customer data

12:52 and that sharing is opt-in rather than

12:54 automatic and that agencies control

12:56 which organizations can receive access.

12:58 Its security materials describe

13:00 role-based access controls, audit

13:02 logging, anomaly monitoring, SOC2 type 2

13:06 review, ISO 27001 controls, and

13:09 tamperresistant search logs. I take some

13:12 comfort in the notion that every search

13:13 is logged. That's a substantial

13:16 improvement over an invisible query box

13:17 with no accountability. A log can and

13:20 will record who searched when they

13:22 searched, the stated purpose of the

13:24 search, the case number if they are

13:25 required to provide one, the offense

13:28 type and which camera networks were

13:30 actually queried. Flux transparency

13:32 portal can expose portions of that

13:34 information publicly, including

13:35 anonymized usage statistics and sharing

13:38 relationships. But you need to remember

13:40 one key thing. A log is a witness, not a

13:42 guard. Logging a misuse does not prevent

13:45 it unless somebody reviews the log,

13:47 recognizes the pattern, and imposes some

13:49 consequences. Every Windows

13:51 administrator knows this problem. You

13:53 can enable exquisite auditing on a

13:55 server, but if the event log is a

13:57 digital addict that no human actually

13:59 visits until after the burglary, it

14:01 provides forensics rather than

14:02 prevention. Flock has been adding more

14:05 preventative controls including optional

14:07 required case numbers, keyword filters

14:09 intended to block searches that are

14:11 prohibited by state law, labels

14:13 identifying requests originating from

14:15 federal organizations, and restrictions

14:17 on federal access to certain state data.

14:20 The company argues that local elected

14:22 officials should determine the permitted

14:23 uses and that the platform should

14:25 provide the tools to enforce and audit

14:27 those choices. So, they don't really

14:29 want to be in the business of making up

14:30 the rules. They just want to know what

14:32 they are and follow them. It sounds like

14:34 there's also evidence that policy

14:36 controls can fail or prove incomplete.

14:38 In 2025, an Illinois Secretary of State

14:41 audit found that US Customs and Border

14:43 Protection had gained access to Illinois

14:45 plate reader data in violation of state

14:47 restrictions. Illinois ordered the axis

14:49 shut down and Flock paused its federal

14:51 pilot while adding further controls. The

14:54 episode can be read in two ways. Critics

14:56 see proof that promise guard rails did

14:58 not prevent the prohibited access while

15:00 supporters can point that the audit

15:02 trail detection shutdown and subsequent

15:04 controls as the accountability system

15:06 actually working correctly after a

15:07 failure. And both readings contain some

15:10 truth. Security engineers live in that

15:12 uncomfortable territory all the time.

15:14 Another concern is network sharing. A

15:16 city may own 50 cameras but gain search

15:19 access to detections from neighboring

15:20 jurisdictions that have agreed to share.

15:23 That can be extremely useful when a

15:25 kidnapping suspect, stolen car, or

15:27 robbery crew crosses municipal

15:28 boundaries. Because if old movies have

15:30 taught me anything, it's that criminals

15:32 have shown remarkably little respect for

15:34 the county line. But data sharing also

15:36 changes the privacy equation. A resident

15:39 may debate and approve 20 cameras

15:41 locally only to discover that the

15:42 effective searchable network is

15:44 regional, statewide, or even larger.

15:46 Critics argue that a federation of

15:48 individually modest systems can become

15:50 something no single community

15:52 consciously approved of or even really

15:54 considered in advance. Mind you, this is

15:56 also the same architecture that made the

15:58 internet useful. Independent networks

16:00 agreed to exchange traffic and the

16:02 combination became much more powerful

16:03 than any individual network. The

16:06 difference is that the internet packets

16:07 usually belong to willing participants.

16:09 Cars passing public cameras do not

16:11 negotiate peering agreements. There's

16:14 also an important product distinction.

16:16 The classic Falcon LPR has generally

16:18 been described as a vehicle focus system

16:20 taking still images rather than acting

16:22 like a conventional continuously

16:24 monitored CCTV camera. But Flock's

16:26 broader platform includes dedicated

16:28 video cameras. And in 2025, the company

16:31 announced optional live and recorded

16:33 video capability for existing LPR

16:35 hardware as well as colllocated video

16:37 products. That means a community

16:39 evaluating flock cameras needs to ask

16:42 exactly which hardware, software

16:44 options, and retention policies are

16:45 enabled rather than relying on generic

16:47 descriptions based on the brand name.

16:50 Asking whether a Flock camera records

16:52 video is therefore a little bit like

16:53 asking whether a Windows machine runs

16:54 SQL Server. Some do, some don't, and the

16:57 logo on the case doesn't answer it for

16:59 you. The legal question is evolving for

17:02 much the same reason. Courts have

17:04 traditionally held that drivers have

17:06 little expectation of privacy in a

17:07 license plate displayed openly on a

17:09 public road. And even I get that. But

17:12 the modern question is not merely

17:13 whether an officer may look at the

17:14 plate. It's whether the government may

17:16 automatically collect millions of public

17:18 observations, retain them, aggregate

17:20 them, and search them retrospectively.

17:23 In a 2025 federal case from Kansas, a

17:25 district court rejected a fourth

17:27 amendment challenge involving nine flock

17:29 detections over roughly 4 hours. The

17:31 court distinguished those limited

17:33 observations from continuous cell phone

17:35 or GPS tracking and noted that the

17:37 30-day retention period reduced its

17:39 concerns, but the same decision

17:41 explicitly warned that a denser and more

17:44 pervasive network could eventually

17:45 approach the kind of systemic tracking

17:47 that raises constitutional problems.

17:50 That is a remarkably balanced

17:51 description of the technology itself.

17:53 The constitutional question may depend

17:55 not just on what one camera does, but on

17:58 scale, density, retention, search scope,

18:00 and how the data is used, which leads to

18:03 the most useful way to think about

18:04 flock. The camera is a sensor. The cloud

18:07 service is an index. The hot list is an

18:09 alerting rule. The sherry network is a

18:12 federation. None of these components

18:14 inherently knows whether the person

18:15 operating the search is trying to find a

18:17 kidnapped child, recover a stolen truck,

18:19 identify a robbery suspect, monitor a

18:22 protest, investigate immigration status,

18:25 locate someone seeking medical care, or

18:27 satisfy a personal curiosity that has no

18:29 legitimate law enforcement purpose.

18:31 Because purpose does not live in the

18:33 lens. Purpose lives in policy,

18:35 permissions, oversight, and in the

18:37 person that is allowed to sit at that

18:39 keyboard. supporters see a machine that

18:41 observes purely public facts more

18:43 consistently than a patrol officer ever

18:45 could. It does not become tired,

18:47 distracted, or decide that one driver

18:49 looks a little more suspicious than

18:50 another. It records vehicles rather than

18:53 skin color, and it can give officers a

18:54 timely objective lead when minutes

18:56 matter. Critics answer that decisions

18:58 about where the cameras are placed and

19:00 which plates enter the hot lists, which

19:02 neighborhoods receive scrutiny, which

19:04 agencies share data, and which alerts

19:06 trigger stops are all human decisions.

19:09 Automating observation can reduce one

19:11 form of discretion while multiplying the

19:13 reach of other forms. Supporters note

19:15 that most detections are never actually

19:17 searched and disappear automatically

19:19 after the retention period. Critics

19:21 reply that innocent people are still

19:23 recorded first and filtered by suspicion

19:25 later. Supporters emphasize encryption,

19:28 audit logs, local ownership, opt-in

19:30 sharing, and the absence of facial

19:32 recognition in the core ALPR product.

19:34 Critics point out that encryption

19:36 protects data from outsiders, not from

19:38 an authorized user performing an

19:40 inappropriate search, and that a vehicle

19:42 history can reveal sensitive

19:43 associations without ever identifying a

19:45 face. Neither side is arguing about

19:48 imaginary capabilities. They're

19:50 assigning different weight to the same

19:51 engineering facts. And perhaps that is

19:54 why the debate has become so heated.

19:56 Flock cameras are not a hypothetical

19:57 future surveillance technology humming

19:59 inside of a lab somewhere. They are

20:01 practical, affordable, easily deployed

20:03 network appliances that solve real

20:05 investigative problems while creating

20:06 real governance problems at the same

20:08 time. A community deciding whether and

20:10 how to use them therefore has more

20:12 meaningful questions available than

20:14 simply asking whether cameras are good

20:15 or cameras are bad. So what offenses

20:18 justify a search? Must every search

20:20 include a valid case number? Are

20:23 searches for minor offenses allowed? Who

20:25 may create a custom hot list? How

20:27 quickly must stale entries be removed?

20:30 Must every alert be visually confirmed?

20:33 Which agencies may share that data? Are

20:36 federal requests handled differently? Is

20:38 access to sensitive locations

20:40 restricted? Who reviews the audit log?

20:42 Are misuse statistics published? Are

20:44 they public? How long is data retained?

20:47 Can exports live longer than that? Does

20:49 the public know where the cameras are

20:51 and which capabilities are actually

20:52 enabled on them? As for me, I think the

20:55 technology is incredibly impressive, as

20:57 are the potential applications, but the

20:59 ways in which the cameras can and

21:00 sometimes are used are, as my kids say,

21:03 a little sus. So, as usual, the devil is

21:06 in the details of how the system is

21:07 implemented. Answering those questions

21:09 does not eliminate disagreement, but it

21:11 moves the argument from bumper sticker

21:13 philosophy into actual systems design.

21:16 Back when I was working on operating

21:17 systems at Microsoft, we learned that

21:19 privilege by itself was not

21:20 automatically good or bad. Kernel mode

21:22 is necessary to make the computer work,

21:24 but because the consequences of error

21:26 are so much greater, kernel code

21:28 receives stricter rules. Smaller

21:30 interfaces, deeper review, and more

21:32 aggressive auditing. A connected plate

21:34 reader network deserves the same kind of

21:36 thinking. The more powerful the query,

21:37 the narrower the permission should

21:39 become. The broader the sharing, the

21:41 more visible the audit should be. The

21:43 longer the retention, the stronger the

21:45 justification should be. And the more

21:47 consequential the alert, the more

21:49 important the human verification

21:50 becomes. So, this is not a verdict on

21:53 the camera. It's simply how engineers

21:55 handle a system with a large blast

21:56 radius. A flock camera may help locate a

21:59 missing child one day and record a

22:00 thousand completely ordinary errands the

22:02 next. Both facts can be true. Its

22:05 usefulness comes from remembering events

22:07 that would otherwise be forgotten. Its

22:09 privacy implications come from exactly

22:11 the same feature. The machine does not

22:13 resolve that tension for us. It merely

22:15 puts it into a database. If you have

22:18 comments or questions about today's

22:19 episode, please leave them in the video

22:21 comments. And remember that we actually

22:22 answer and discuss each week's best

22:24 topics every Friday on Shop Talk on the

22:26 Dave's Addict channel. I'll put a link

22:28 to an episode up here. Please check one

22:30 out. If you found today's episode

22:32 interesting or entertaining, remember

22:33 that I'm mostly in this for the subs and

22:35 likes. So, I'd be honored if you would

22:36 consider leaving me one of each before

22:38 you go today. In the meantime, and in

22:40 between time, hope to see you next time

22:41 right here in Dave's Garage.

22:44 >> Do it. Do it. Do it.

