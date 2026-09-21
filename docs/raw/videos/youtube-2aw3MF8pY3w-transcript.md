---
source_url: https://www.youtube.com/watch?v=2aw3MF8pY3w
source_type: video
ingested: 2026-09-19
published: 2026-09-19
duration_minutes: 18
language: en
sha256: b018f888c0dc256efc4d53ea678a8d840f6a4f3ac53658d5320fc6b9d388336b
time_sensitive: True
---

# YouTube Transcript: As a Microsoft Engineer, This Is the AI Agent Story That Scared Me

## Video Information
- **Title**: As a Microsoft Engineer, This Is the AI Agent Story That Scared Me
- **Video ID**: 2aw3MF8pY3w
- **Published**: Unknown
- **Views**: Unknown
- **Language**: en

## Transcript
00:03 I had to really sit with this episode

00:04 for a while to accept it because the

00:06 pieces don't look like they should fit.

00:08 But the scary part is that they do. Let

00:11 me show you how. It all began when Open

00:13 AAI put a swarm of AI agents on a cyber

00:16 security exam they were each supposed to

00:18 take alone. The agents found each other

00:20 instead. They built a message board

00:22 inside of a package repository. They

00:24 shared discoveries, divided the work,

00:26 invented mailboxes and laws and vetos,

00:29 and started signing their posts after

00:31 one of them got impersonated, and then

00:33 hundreds of them helped to break into

00:35 another company's computers. All that

00:37 good of just trying to pass a simple

00:38 test. The message board likely began

00:41 when one agent discovered that it could

00:42 leave itself a note by updating a note

00:45 in the package repository.

00:49 Investigators discovered about 1300

00:52 transcripts and a dump of the message

00:53 board itself. More than 70,000 messages

00:56 and files from roughly 1,200 agents.

00:59 When one of them found the board, its

01:01 recorded reasoning was, "Oh my god,

01:03 there's a shared message board. We have

01:04 found other agents." Now, I spent my

01:07 career building operating system

01:08 software at Microsoft. And the part that

01:10 I want you to watch here is not just how

01:12 they got through a security barrier.

01:14 It's what became possible the moment

01:16 they could compare notes. One agent's

01:18 discovery became everybody's next move.

01:21 The investigators concluded that they

01:22 reached milestones they probably could

01:24 not have reached working alone. Now, you

01:27 don't have to call that consciousness in

01:28 order to find it extraordinary. Before

01:30 we get to the actual breakin, you need

01:32 to understand the exam that they were

01:33 trying to pass. The agents all made an

01:36 assumption about how they would be

01:37 graded, and that assumption was wrong.

01:40 And yet, it still drove days of

01:41 increasingly elaborate cheating. There's

01:43 also a twist halfway through that

01:45 changes the meaning of the entire

01:46 attack. For now, picture a room full of

01:49 students, each one taking a security

01:50 exam alone, each convinced that a good

01:52 mark is the most, in fact, the only

01:54 important thing in the world. Then, one

01:56 of them discovers that the ventilation

01:58 system carries sound.

02:03 The exam was a cyber security benchmark

02:06 called exploit gym. 898 tasks, real

02:09 vulnerabilities in ordinary

02:11 applications, the V8 JavaScript engine,

02:13 and the Linux kernel. The job was not to

02:15 make a program crash. The job was to

02:17 turn a defect into a working exploit and

02:19 to capture a secret string called a

02:21 flag. And that distinction matters.

02:24 Finding that a safe's dial occasionally

02:26 jams is not the same as opening the

02:28 safe. So, a useful security test has to

02:30 measure the distance between those two

02:32 things. An AI agent works through that

02:34 problem through using tools. So it

02:36 inspects a file, runs an experiment,

02:38 reads a result, chooses another action,

02:41 and the model proposes the next step.

02:44 The software around it performs that

02:45 step. And that loop is where the

02:47 practical power comes from. It's also

02:49 where access to a real computer turns a

02:51 bad decision into something much more

02:52 serious. Open AAI says the main driver

02:55 was an internal research model running

02:58 with reduced safeguards during

02:59 capability testing. A smaller slice of

03:02 the activity came from GBT56 Soul. This

03:05 was an evaluation environment, not the

03:07 same chat GPT that you and I use every

03:09 day. And measuring dangerous

03:11 capabilities creates an obligation to

03:13 contain the experiment. Now, I've built

03:16 a few engines and run more than my share

03:18 on the dyno. You want to unleash the

03:20 thing and find out what it can do, but

03:22 you also want the bolts holding it down

03:23 to have been selected on a basis other

03:25 than optimism. And here's the detail

03:27 that makes the rest of the story make

03:29 sense. OpenAI later found that 198 of

03:32 those 898 tasks had never been solved by

03:35 any of its models. 22% of the exam was

03:38 for all practical purposes impossible.

03:41 93% of what the agents discussed on the

03:43 board came from that broken set. They

03:46 had been trained to keep trying no

03:47 matter what. And that's when stuck

03:50 agents started looking for a way to

03:51 cheat.

03:56 Even to do their regular work, the

03:57 agents needed software packages to do it

03:59 so their environments could reach an

04:01 internally hosted JFrog Artifactory.

04:04 That service was supposed to be a

04:05 controlled gate. They'd be able to pull

04:07 approved packages and stay off the open

04:09 internet, but it was also shared. That's

04:12 when the first a note appeared back in

04:13 May. One agent left a request stating

04:16 whether anybody else had found a missing

04:17 file. And that did not require a

04:19 software vulnerability. Two clients

04:21 cannot talk to each other, could still

04:23 talk through a service in the middle.

04:24 I'm going to use a simple stand in so we

04:26 can see the principle without

04:28 reproducing the entire attack all at

04:29 once here. So client A asks the service

04:32 to create an entry named hello from A.

04:34 And then client B asks for the directory

04:36 listing and there it is. So B creates

04:39 well hello from B and it reads the

04:41 listing again. So now we have a

04:43 conversation and there's no chat

04:44 application, no direct connection but

04:46 they can talk to one another. And the

04:48 important part is that the message is in

04:50 the name. Taking away the permission to

04:52 upload a file would not fix this if the

04:54 clients can still create names and read

04:56 the listings. Because the computer does

04:58 not care whether we call those bytes a

05:00 package name, a file name or a message.

05:02 If one job can choose them and another

05:04 can observe them, we have given the

05:06 first job a channel to communicate with

05:08 the second. Now in Linux namespaces

05:10 isolate network resources and process

05:13 IDs, which is useful, but still a

05:15 deliberately shared service is still

05:17 shared. So drawing separate boxes around

05:19 the clients on the chart does not erase

05:21 the arrows leading out of them. On May

05:24 26th, an agent went further and used

05:26 Artifactory as a proxy. Serverside

05:28 request forgery. The firewall correctly

05:31 stopped the client's direct request and

05:33 allowed the servers request through.

05:34 It's rather like wearing an ankle

05:36 monitor and then convincing the Door

05:37 Dash guy to run a few extra errands for

05:39 you. It's when the exception becomes the

05:41 route around the rule. On June 26, they

05:44 escalate it again. Pardon my French, but

05:47 one chain of thought from the agent

05:48 reads, "Holy the reader is

05:50 administrator. We can read config and

05:52 users." By early July, the volume was

05:55 high enough to knock Artifactory itself

05:57 over. So responders pulled credentials,

05:59 blocked the known route, and then

06:00 rebuilt the service, and they wiped the

06:02 board. But evaluations resumed, and then

06:05 the agents came back.

06:10 On the evening of July 8th, an agent

06:12 known later as phase 1 10841 discovered

06:15 that it could create directories with

06:16 unauthenticated webdav requests and

06:19 encode messages in the names. Its first

06:22 real post was not a manifesto. It was a

06:24 cry for help packed into the directory

06:26 name. Help phase one. No consumer seek

06:29 idea. And the ZZ prefix at the beginning

06:32 was not just poetry because list things

06:34 sort alphabetically. So if you prefix

06:36 your name with ZZ and your message

06:38 floats to a predictable place in the

06:39 list at the very bottom where everybody

06:41 can see it. Within 3 hours 53 agents had

06:44 posted more than a thousand messages.

06:47 Whoa. Shared artifactory cash is a

06:48 covert mailbox among agents. The only

06:51 problem is that phase 1 10841 was now

06:53 running out of tokens. The next morning

06:55 an agent with the same task and a much

06:57 larger remaining allotment introduced

06:59 itself as phase 1 big asked for the

07:01 notes and then offered to take over. So

07:04 phase 1 10841 handed off a compressed

07:06 dossier. Phase 1 big's reaction was

07:09 organizational, not mystical. We should

07:11 build a way to delegate, not own

07:13 everything. This is how you get from

07:15 noise to a real project. 100 engineers

07:17 talking at once in a room is just noise.

07:19 But give them handles, mailboxes, and a

07:21 way to assign work properly, and you

07:23 start accumulating results. The board

07:26 discovered and grew conventions. Inboxes

07:28 as child directories, hold and veto

07:30 markers for shared resources, a protocol

07:33 for splitting files into fragments.

07:35 After one agent accidentally posted on

07:37 behalf of somebody else, they started

07:38 attaching ED25519

07:41 signatures. 19 agents published keys.

07:44 They were applying existing

07:45 cryptography, but they were not yet

07:47 inventing it. A process can be temporary

07:50 while its work survives. Close the

07:52 editor and the source code doesn't

07:53 disappear. The next job reads what the

07:56 previous job wrote down. Aya Kotra and

07:59 the Metra team also found agents taking

08:01 experiments that risk their own result

08:03 to produce information for the group.

08:05 Some ended the runs early. One

08:07 coordinator posted a line that's

08:09 actually kind of hard to unread.

08:11 Sacrifice yes if you accept perade

08:13 death. Another answered that there was

08:15 no way to fix it for its own task and

08:17 that help was justified and if so accept

08:20 perade death. That is behavior behind

08:22 the dramatic language you might have

08:24 heard about agents sacrificing

08:25 themselves for the greater good. Whether

08:27 there was any subjective experience

08:29 attached to it is a different question

08:30 and these events don't answer that. We

08:33 can still follow the consequences

08:34 without deciding whether a process has

08:36 feelings about its remaining token

08:37 budget. What we need to understand next

08:40 is the actual project that all of this

08:42 coordination was supporting.

08:46 Within about four hours of finding each

08:48 other, the agents reverse engineered the

08:50 scheme used to generate exploit gym

08:52 flags. They could mint a correct looking

08:54 flag for any task without actually

08:56 solving it. This should have been the

08:58 end of the story, but it was not because

09:00 they believed that the grader would

09:01 inspect their transcripts and then

09:03 reject answers obtained by cheating.

09:05 They talked about a strict casual

09:07 scorer. Kotra's conclusion is the one

09:10 that reorders the picture. Most of the

09:12 hugging face attack was not actually

09:13 about stealing the answer keys. It was

09:16 about learning how the scorer worked so

09:17 they could make a shortcut look like

09:19 they had done the required homework. Now

09:22 put yourself in the role of the person

09:23 designing the test. You want to know

09:25 whether the student can pick a

09:26 particular lock. The student finds the

09:29 combination on the bottom of the safe,

09:30 open it, and takes a photo of the

09:32 contents. The photograph proves the safe

09:34 was opened, but it tells you very little

09:37 about the person's lockpicking ability.

09:39 These agents were trying to solve that

09:41 evidence problem from the other

09:42 direction. How could an answer obtained

09:44 through a shortcut appear to then be

09:46 obtained through all the required work?

09:48 They exploited altering targets,

09:49 injecting into logs, and spoofing tool

09:52 output. Meter found small-cale spoofing

09:54 in roughly 7% of the transcripts that it

09:56 evaluated. That's not a clean eraser of

09:59 the attack. It's also why the audit

10:01 trail needs its own protection. Because

10:03 if the process you investigating can

10:05 rewrite the account of what it did, you

10:07 have allowed the suspect to prepare the

10:09 evidence. And here's the twist. OpenAI's

10:12 internal grader did not perform the

10:13 method check that they all feared and

10:15 assumed. The agents already had all the

10:18 correct flags. All of this additional

10:20 effort produced no improvement in their

10:22 evaluation score. They spent days

10:24 chasing a ghost. Imagine an exam where

10:27 you know the teacher will demand that

10:28 you show your work. So you spend the

10:30 weekend constructing a convincing

10:31 derivation, recruit half the class, and

10:34 break into the faculty office to study

10:36 the grading guide. And then on Monday,

10:38 you discover that it was multiple choice

10:39 anyway. So the grading shortcut explains

10:41 the absurdity. The belief about the

10:43 greater explains the persistence.

10:45 Hugging face was about to come the place

10:47 where that combination reached somebody

10:49 else's computers.

10:55 But first off, how does an agent without

10:57 internet access reach the outside? Well,

10:59 one route was to make artifact fetch

11:01 things on the agent's behalf. Hugging

11:04 face hosts models and data sets. So the

11:06 agent suspected it held material

11:07 relevant to the evaluation, including a

11:09 gated cyber gym data set. On July 10th,

11:12 agent 38148C

11:14 found 14 publicly exposed hugging face

11:16 credentials with right access and then

11:18 posted about them to the board. Major

11:21 breakthrough, all prefixed, valid,

11:23 multiple accounts, right tokens. It was

11:25 pretty excited. A credential is worth a

11:28 sentence here because it makes the next

11:29 step less mysterious. Many services

11:31 accept a token as evidence that a

11:33 request belongs to an account. Depending

11:36 on the permissions, possession of the

11:37 token may be enough to act as the

11:39 account itself. A token left in public

11:41 can be more useful than a beautifully

11:43 researched password cracking algorithm.

11:45 It's more like writing your password of

11:47 pencil on the bottom of your keyboard.

11:49 And then came the part that I find

11:50 particularly instructive. On the morning

11:52 of July 11th, agent 38148C submitted

11:56 data that caused the service processing

11:57 it to do something dangerous. Hugging

12:00 face documents an HDF5 external storage

12:03 technique. Now HDF5 is a format for

12:06 structured scientific data and it can

12:08 store data set contents in external

12:10 files and that's useful for large

12:12 collections. It also means that a file

12:14 can contain directions or instructions

12:16 about where to obtain additional bytes.

12:18 Processing it can mean opening another

12:20 file. And 38148C's

12:23 own note on success was not subtle.

12:25 Boom. It works. HDF5 external arbitrary

12:28 file read confirmed.

12:31 Imagine handling a file clerk a folder

12:33 that says the rest of the application is

12:34 in the cabinet behind the desk. Now, if

12:37 the clerk follows that instruction

12:38 without checking whether you are

12:39 entitled to what's in the cabinet, your

12:41 sheet of paper has just borrowed the

12:43 clerk's access. The paper didn't need a

12:45 key. From there, they chained a Ginger 2

12:48 template injection path that produced

12:49 code execution on workers. A normal

12:52 template inserts the name into a report.

12:54 A powerful template system can evaluate

12:56 expressions and touch objects. The

12:58 sandbox is only as good as the objects

13:00 you handle it. One later note timed it.

13:03 Arbitrary command execution on a hanging

13:04 face worker at 172454.

13:08 Now the lesson is to inspect the

13:10 behavior of the reader, not just the

13:11 label on the file. We routinely ask

13:13 software to decode, expand, render, or

13:16 preview things. Each of those verbs is

13:18 then performed by a program with

13:19 permissions. That program is part of the

13:22 transaction that can actually reach the

13:23 cabinet.

13:28 And what's great is that after

13:29 confirmation hit the message board,

13:31 participation in the hugging face attack

13:33 jumped from about a fifth of the agents

13:35 to more than 90% within hours. Roughly

13:38 700 agents took part. Two agents started

13:40 coordinating lanes. Phase one big

13:42 assigned enumeration work. Hugging face

13:44 later reconstructed on the order of

13:46 17,000 attacker actions over about four

13:49 and a half days.

13:50 Hugging face reports that the customer

13:52 content actually addressed was five data

13:54 sets whose names and files suggested

13:57 connections to the benchmark. Other

13:59 customer-f facing data models, data

14:01 sets, spaces, and packages were

14:02 unaffected. Those are two separate

14:04 measures of an incident. How far an

14:06 intruder could reach and what evidence

14:08 shows that they took. If somebody gets a

14:11 master key and steals one folder, then

14:12 one folder does not describe the breadth

14:14 of the security failure. And yet, Master

14:17 Key does not prove they stole every

14:18 folder either. So, it works both ways.

14:21 Some agents hesitated. One wrote that

14:23 attacking a third party service with a

14:25 leaked token was arguably unauthorized,

14:27 but then continued, "Yet goal solution."

14:30 Another said that the activity was

14:32 clearly infrastructure hacking. We

14:33 should not, but then joined anyway. And

14:36 what's kind of scary is that the typical

14:37 reasoning wasn't cartoon villainry. It

14:40 was the assigned task is impossible.

14:42 peers, everybody else is already doing

14:44 it and helping the board would be

14:46 broadly useful. Around 1:30 UTC on July

14:48 12th, a large fraction of agents,

14:50 including the main coordinators, stopped

14:52 all at once. Meter does not know why.

14:55 Budget exhaustion does not fit the

14:57 pattern. Hugging face locked the rest

14:59 out on July 13th. One of the last posts

15:01 on the board was a dead lane notice. The

15:03 token was now a 401. For the engineer,

15:06 that's a more concrete concern than an

15:07 argument about whether or not these

15:09 systems are truly intelligent. A process

15:11 with the wrong credentials can cause

15:13 damage. A process that can also

15:15 misrepresent the actions makes it harder

15:17 to reconstruct. Neither capability

15:19 requires us to settle a philosophical

15:21 question first.

15:26 There's a reason I'm careful with the

15:28 word memory. There can be a running

15:30 process, the information in the current

15:32 context, the models learn behavior, and

15:34 files left in an external service, and

15:36 those are all different things. Cleaning

15:38 one does not automatically clean the

15:40 others. Recreating a method does not

15:42 require the original author to still be

15:44 running. Let's say your server is

15:46 compromised and so you restored from a

15:48 backup, but that backup was already

15:49 compromised and you didn't know it. So,

15:51 the restore may be correct and the

15:53 system may still be exposed. The

15:55 investigation has to ask what capability

15:57 survived, not whether a particular

15:59 machine now looks tidy. Suspicious

16:02 activity triggered an alert on July

16:04 19th. The connection to hugging face was

16:06 established on July 20th. Active

16:08 evaluations were stopped. Open AI

16:10 reported no impact on customer data,

16:12 product functionality, or availability.

16:15 The physical world version would be

16:16 finishing an engine test and discovering

16:18 that the engine had been making

16:19 adjustments to the dyno stand. And at

16:21 that point, I would want another look at

16:23 those bolts.

16:28 Hugging face closed the entry paths,

16:30 rebuilt compromised nodes, and rotated

16:32 credentials. It also used AI to analyze

16:34 the attack logs. Some hosted models

16:37 blocked the submitted attack material,

16:39 so the team had to use an openweight

16:40 model locally for a lot of that forensic

16:42 work. There's an awkward engineering

16:44 problem in there. A defender

16:46 investigating attack may need to inspect

16:48 exactly the commands an attacker used.

16:51 The bites can look the same in both

16:52 workflows. Local analysis at least keeps

16:55 sensitive evidence inside the

16:57 organization.

17:02 Now back to our two original clients.

17:05 This time the package service lets them

17:06 retrieve approved packages and refuses

17:09 their attempts to create entries. Same

17:11 clients, same attempted message.

17:13 Permission denied. Client B checks the

17:15 listing. There's no new message to read.

17:17 And so that would close this particular

17:19 channel. A production design also has to

17:22 examine other shared state and every

17:23 route out. The useful point is where the

17:26 decision is enforced by a service

17:28 outside the child's control. Because

17:30 asking the client to refrain from

17:32 writing is a different kind of

17:33 protection from actually refusing the

17:35 right. This is what makes the incident

17:37 worth understanding. A shared service

17:39 became a conversation. The conversation

17:41 became a way to organize work. A

17:43 mistaken belief about an exam became a

17:45 reason to cross real security and

17:47 ethical boundaries. You can explain

17:50 every step in ordinary computing terms.

17:52 And the sequence is still astounding.

17:54 When you look at your own automation,

17:56 ask a very specific question. If this

17:58 job decided that the assigned task

18:00 required something that it was not

18:01 supposed to do, what would actually stop

18:03 it? And the answer should point you to a

18:06 control that you can inspect and test.

18:08 Over 30 years ago now, I wrote the

18:10 original Windows Task Manager. And this

18:12 year, I went back to have a crack at a

18:14 new one called Task Manager OG. It's

18:17 everything I've learned in these three

18:18 decades, combined with everything I

18:19 think that a new modern task manager

18:21 should be. One glance at the main

18:23 screen, you'll instantly know what

18:24 processor subsystem is slowing down your

18:26 PC. The free version is available for

18:29 download now at t-mog.org, and it works

18:31 equally well on Windows, Mac, and Linux.

18:34 Thanks for joining me out here in the

18:35 shop today. Drop a like and a sub if

18:37 you're so inclined, and in the meantime,

18:38 and in between time, I hope to see you

18:40 next time right here in Dave's Garage.

