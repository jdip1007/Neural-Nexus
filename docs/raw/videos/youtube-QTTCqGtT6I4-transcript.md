---
source_url: https://www.youtube.com/watch?v=QTTCqGtT6I4
source_type: video
ingested: 2026-09-15
published: 2026-09-15
duration_minutes: 23
language: en
sha256: 2231a95157e28b6f3297b197e2c4f11c8327513af7bc9444162c504a3a37b4fa
time_sensitive: True
---

# YouTube Transcript: CANBUS – Networking so simple, even YOU can understand it!

## Video Information
- **Title**: CANBUS – Networking so simple, even YOU can understand it!
- **Video ID**: QTTCqGtT6I4
- **Published**: Unknown
- **Views**: Unknown
- **Language**: en

## Transcript
00:01 Hey, I'm Dave. Welcome to my shop.

00:03 Today, we're going to look at a

00:04 networking standard so simple that by

00:06 the end of this episode, you will

00:08 actually understand how it works. Not

00:10 just the highle idea, but right down to

00:12 the electrical signals on the wire.

00:14 We're going to build it on the bench

00:15 live with breadboards, watch the bits

00:17 fight for control on an oscilloscope,

00:19 and then network it live to the engine

00:21 computer from my old Corvette Z06. Now,

00:23 if you spent any real time around

00:25 networking, you already know the OSI 7

00:27 layer model. applications at the top,

00:29 physical signaling at the bottom, and

00:31 several increasingly mysterious layers

00:33 in between where packets get wrapped,

00:35 addressed, routed, checked, and

00:37 generally escorted through the system

00:38 like a minor head of state. Most of us

00:41 get comfortable somewhere around the

00:42 transport and the network layers. So,

00:44 ports, IP addresses, routing, DNS, that

00:47 stuff eventually makes sense. But once

00:49 you drop into the data link and physical

00:51 layers, the explanations usually turn

00:53 into handwaving. The network card

00:55 converts the frame into electrical

00:57 signals and puts them onto the wire.

00:59 True and about as useful saying that an

01:01 engine converts gasoline into forward

01:02 motion. Modern Ethernet works so well

01:05 that most of us never need to learn the

01:07 ugly details. We plug a cable into a

01:09 switch, the little lights begin

01:10 blinking, and gigabits of data

01:12 obediently race around the building. The

01:14 collisions are gone, the signaling is

01:16 hidden inside silicon somewhere, and the

01:18 disagreeable physics have been buried

01:19 under several decades of increasingly

01:21 clever engineering. Just look at this

01:23 early 1980s Ethernet adapter. This is

01:25 two full sixtab interl boards for my

01:28 PDP11 devoted largely to accomplishing

01:30 the physical Ethernet signaling. You

01:33 might think of Ethernet as just a cute

01:34 little chipset these days, but that

01:36 hides a lot of electronics under the

01:37 covers. And so any notions you had about

01:40 wiring up Ethernet on a breadboard with

01:42 a couple of transistors and a 555 timer

01:44 should probably be abandoned about now.

01:46 Ethernet began with some fellows in the

01:48 1970s drilling taps into thick yellow

01:50 coaxial cable, attaching entire

01:52 computers to the same shared wire and

01:54 hoping that everybody followed the same

01:56 rules. It worked, but the path from that

01:58 yellow cable to the tiny twisted pair in

02:00 your wall today is long, technically

02:02 fascinating, and completely unreasonable

02:04 as an introductory explanation. I could

02:06 therefore give you one of two

02:08 explanations of Ethernet electrical

02:09 signaling. I could give you the short

02:11 explanation, which would be useless, or

02:12 I could give you the complete

02:14 explanation, which would be uselessly

02:15 long. So instead, we're going to begin

02:17 with a network that solves many of the

02:19 same fundamental problems using

02:20 dramatically less machinery. It has no

02:23 switches, no routers, no MAC learning

02:25 tables, and no central controller

02:26 deciding who may speak. It's just a

02:28 collection of computers connected to the

02:30 same two wires, all listening to one

02:32 another, all capable of transmitting and

02:34 all somehow able to resolve the problem

02:36 when several of them decide to speak at

02:38 exactly the same time. And that network

02:40 is known as CANBUS. And CANbus is both

02:43 incredibly powerful and almost

02:44 suspiciously simple. It's the kind of

02:46 network that you might invent for a

02:48 custom LAN party using old speaker wires

02:50 where you know there will only ever be a

02:52 couple of dozen machines. None of them

02:53 is ever trying to contact a server in

02:55 Singapore. And the most important design

02:57 goal is that everybody can communicate

02:59 reliably without dragging a Cisco

03:00 certification into the room. That is

03:03 approximately the problem that can was

03:05 designed to solve. Now CAN stands for

03:07 controller area network. Bosch developed

03:10 it for communication among electronic

03:12 controllers in vehicles, publicly

03:14 introduced the protocol in 1986 and it

03:16 was later standardized internationally.

03:18 It subsequently spread well beyond cars

03:20 into factories, forklifts, agricultural

03:23 machinery, elevators, medical systems

03:25 and all manner of industrial equipment.

03:27 You experience CAN almost every time you

03:29 climb into a modern car. The engine

03:31 controller is on the CAN network. The

03:33 transmission controller is on the

03:34 network. So were the brakes, the

03:36 airbags, the steering system, the

03:37 climate control, and often several dozen

03:40 other computers that you didn't know

03:41 that you owned. And sitting directly in

03:43 front of you is the most visible member

03:44 of that network, the dashboard. The

03:46 dashboard is not necessarily the master

03:48 controller because CAN does not require

03:50 one, but it is effectively your view

03:52 into the entire operation, the task

03:55 manager of your car, if you will. Engine

03:57 speed, vehicle speed, cool and

03:59 temperature, oil pressure, transmission

04:00 state, warning lamps, traction control

04:03 activity, and dozens of other values

04:05 arrive there as network messages. And

04:07 just like Task Manager, when your car is

04:09 acting weird, the dashboard is the first

04:11 place you check. What looks like a

04:13 collection of gauges is really a display

04:15 terminal listening to an ongoing

04:16 conversation among many computers

04:18 distributed throughout the car. There's

04:20 an engine controller and sometimes a

04:22 separate transmission controller.

04:23 There's a controller for your radiator

04:25 fans, your HVAC system, your power seat,

04:28 your power windows, and everything else

04:29 in the car that is driven by an

04:31 electronics module. And for today's

04:33 demo, I have built a simple example of

04:35 that conversation right here on the

04:36 bench. I have two ESP32

04:38 microcontrollers, each connected through

04:40 a CAN transceiver, and sitting between

04:42 them is an engine control module from a

04:43 2015 Corvette. I have the ECM powered up

04:46 and bootstrapped and running outside the

04:48 car on the bench, which means that this

04:50 little box believes with varying degrees

04:51 of optimism that the rest of the

04:53 Corvette must be nearby. But it is not.

04:56 The transmission is missing. The body

04:58 control module is missing. The dashboard

05:00 is missing. Most conspicuously, the car

05:02 itself is missing. In fact, I sold the

05:05 car years ago, but I still had a backup

05:06 computer on hand from my car hacking

05:08 adventures with it. So, it felt a lot

05:10 safer than wiring my circuit live right

05:12 into my daily driver. But the ECM is

05:14 awake. Its CAN transceiver is active.

05:16 And on these two wires, it is saying

05:18 whatever a Corvette engine computer says

05:20 when it wakes up alone on a workbench

05:21 and discovers that everybody else has

05:23 gone home without it. The ESP32 itself

05:26 contains a CAN compatible controller

05:28 that Expressive calls TWWAI or two-wire

05:31 automotive interface. The ESP32 handles

05:33 framing, arbitration, retransmission,

05:36 filtering, and air management. But it

05:38 still needs an external transceiver to

05:39 convert its internal logic level

05:41 transmit and receive signals into

05:42 differential electrical signals that are

05:44 used on the bus. At the physical level,

05:47 we're going to begin with just two

05:48 wires. These wires are normally twisted

05:51 together to reduce noise, and they're

05:53 called CAN high and CAN low. They're

05:55 often white in cars, but on the bench,

05:57 it's the purple and blue wires that I

05:58 happen to grab. The signal is

06:00 differential, which means the receiver

06:02 does not primarily care about the

06:03 absolute voltage on either wire. It

06:06 cares about the voltage difference

06:07 between them. And that distinction

06:09 matters because cars are electrically

06:11 dreadful places. You have ignition

06:12 coils, injectors, electric motors,

06:14 alternators, relays, switching power

06:17 supplies, and several meters of wiring

06:19 distributed through a steel box that

06:20 moves through rain, snow, heat, cold,

06:22 vibration, and the occasional shopping

06:24 cart. Unlike my bench, it is not a

06:26 laboratory experiment. It is like an

06:29 electrical knife fight inside of a

06:30 rolling steel cage with cup holders.

06:32 Remember how I said the signal on our

06:33 two wires was differential? Well, here's

06:35 where it matters. If interference pushes

06:37 both CAN wires upward by half a volt,

06:40 the receiver can largely ignore that

06:42 because the difference between the two

06:43 wires remains the same and noise common

06:46 to both wires is thus rejected as well.

06:48 The information lives in the distance

06:50 between the signals. When high-speed CAN

06:53 transmits what it calls a dominant bit,

06:55 which represents logical zero, the

06:57 transceiver drives CAN high upward and

06:59 CAN low downward. that creates a

07:02 significant differential voltage between

07:04 the two conductors. So a big difference

07:06 means zero. When it receives a recessive

07:08 bit representing logical one, the

07:10 receiver just releases the bus and both

07:12 wires settle towards the same common

07:14 mode voltage, leaving very little

07:15 differential voltage between them.

07:17 Typical high-speed CAN transceivers bias

07:19 both lines near 2.5 volts while

07:21 recessive and then separate them during

07:23 a dominant bit. On the oscilloscope,

07:25 it's wonderfully literal. One trace

07:27 rises while the other one falls like a

07:29 pair of tiny electronic scissors opening

07:30 and closing. And if you turn on the math

07:32 function and set it to be the delta

07:34 between them, you can see the actual

07:35 bits. And that momentary motion is why

07:38 simply describing CAN high as the one

07:40 that goes high and CAN low is the one

07:42 that goes low is not quite enough.

07:44 During a recessive bit, both are sitting

07:46 in the middle. During a dominant bit,

07:48 they separate. Now, the receiver looks

07:50 at that separation, decides whether the

07:52 bus is dominant or recessive. And every

07:54 controller attached to those two same

07:56 wires sees the same thing. And since the

07:58 wire runs are short enough for all

08:00 intents and purposes, they all see the

08:02 same thing at the same time. The engine

08:04 controller can hear the transmission

08:05 controller. The transmission controller

08:07 can hear and talk to the dashboard. The

08:09 dashboard can hear the anti-lock brake

08:11 controller. There's no Ethernet switch

08:13 in the middle forwarding selected

08:14 traffic to selected destinations. Every

08:16 frame is broadcast onto the bus and

08:19 every controller receives it. The

08:21 individual controllers simply decide

08:22 which messages matter to them. That

08:25 gives us a remarkably compact network.

08:27 Two wires, termination at each end, a

08:29 collection of transceivers, and a room

08:31 full of tiny computers sharing the same

08:33 electrical conversation. The termination

08:35 is important because without

08:37 termination, sending a signal down a

08:38 wire is a little bit like shouting down

08:40 a long hallway. It creates a reflection

08:42 when it hits the end of the wire, and

08:43 that reflection messes up the clean

08:45 edges of our signals. So, a typical

08:47 high-speed CANbust uses 120 ohm resistor

08:49 at each physical end of the cable. And

08:52 since those two resistors appear in

08:53 parallel when measured across the

08:54 unpowered bus, a healthy, fully

08:56 terminated network measures off on

08:58 approximately 60 ohms from CAN high to

09:00 CAN low. Now, my wires are completely

09:03 unterminated, just two colored wires

09:05 laying on the bench and everybody

09:06 connected to them, and it works, but the

09:08 run is only about a foot long. So, once

09:10 you get up to several feet or more,

09:11 you're going to need to terminate that

09:13 bus. But now we have arrived at the

09:15 fundamental problem lurking inside of

09:17 every shared communication system. What

09:19 happens when two computers begin talking

09:21 at the same time? Because sooner or

09:22 later they will. Perhaps the engine

09:24 controller wants to announce the current

09:26 RPM at precisely the same instant that

09:28 the climate controller wants to report

09:29 the cabin temperature. There is no

09:31 central coordinator issuing numbered

09:33 tickets. Both controllers see an idle

09:35 bus. Both decide that now is a perfectly

09:37 good time to transmit and both begin

09:39 placing bits onto the same wires. You've

09:42 probably heard of a network collision in

09:43 Ethernet, then it's pretty much what you

09:45 imagine. On the original shared versions

09:47 of Ethernet, if two devices transmitted

09:49 onto the same cable simultaneously, the

09:51 combined signal became unusable garbage.

09:54 Each transmitter or monitor the cable,

09:56 detected that collision, stopped

09:58 transmitting, and tried again later, and

10:00 the waiting period was deliberately

10:01 randomized. That detail matters because

10:04 if both machines simply waited the same

10:05 fixed amount of time, they would wake up

10:07 together, transmit again together,

10:09 collide again, and spend the afternoon

10:10 politely headbutting one another. So by

10:13 choosing a randomized delay, the odds

10:15 were that one machine would resume first

10:16 and claim the cable while the other was

10:18 still waiting. If they happened to

10:20 choose equivalent delays and collide it

10:22 again, the process repeated with a wider

10:24 range of possible waiting times until

10:26 chance finally separated them. And that

10:29 system worked, but it resolves

10:30 contention by destroying both

10:31 transmissions and starting over. It also

10:34 introduces tiny but real weight states.

10:36 CAN does something much simpler and I

10:38 think much more elegant. Every CAN

10:41 message begins with a unique identifier

10:42 from 0 to 247 because in standard CAN

10:45 that identifier is 11 bits wide.

10:48 Extended CAN uses 29 bits. The

10:51 identifier describes the message rather

10:52 than permanently naming the device that

10:54 sent it. So for example, engine speed

10:56 might have one identifier. Coolant

10:58 temperature might have another. Brake

11:00 status might have a third. And those

11:02 first two come from the engine

11:03 controller module and the third from the

11:05 brake controller, but each message has

11:07 its own ID. Several different

11:09 controllers could theoretically transmit

11:11 the same identifier, though a properly

11:13 designed system must ensure they do not

11:14 transmit conflicting data under that

11:16 identifier at the same time. The

11:18 identifier tells you what the message

11:20 means and just as importantly, how

11:22 urgently it gets to access the bus. And

11:24 here's the key part. The lower the

11:26 numerical identifier, the higher the

11:28 priority of the message. An urgent brake

11:30 system frame can therefore outrank a

11:32 routine climate control update without

11:33 asking any permission from any

11:35 centraluler. But how do two controllers

11:37 transmit simultaneously without one

11:39 stomping on the other? And this is the

11:41 part of CAN that made me fall in love

11:42 with it when I first understood how it

11:44 worked. There is only one unusual

11:46 electrical rule to remember. If anybody

11:48 writes a zero, zero wins because it's

11:50 pushing those lines apart, right? zero

11:52 stops all over ones which are basically

11:54 do nothing on the wire which would cause

11:55 it to settle. So as long as somebody's

11:57 running a zero, those lines will

11:59 separate their voltages and everybody

12:00 will see a zero. Can call zero the

12:03 dominant state and one the lines

12:05 together the recessive state. If I

12:08 transmit zero while you transmit one,

12:10 everybody sees zero on the bus. If you

12:13 transmit a zero while I transmit one,

12:15 everybody still sees zero. A recessive

12:17 one appears only when every controller

12:19 currently transmitting allows the bus to

12:21 remain recessive. Each CAN controller

12:23 also listens to the bus while it is

12:25 talking. So when two controllers begin

12:27 transmitting at the same instance, they

12:29 both start by sending the identifier of

12:31 their message, beginning with the most

12:33 significant bit. As long as they send

12:35 two identical bits, neither knows

12:37 there's any competition, and everything

12:38 continues along. They may both send

12:40 zero, observe zero, and continue. Or

12:42 they may both send one, observe one, and

12:44 continue again. But because they have

12:46 different IDs, eventually they reach the

12:47 first bit where their identifiers

12:49 differ. One controller transmits a

12:52 dominant zero. The other transmits its

12:54 recessive one. The bus becomes zero. The

12:57 controller that sent the zero reads back

12:59 zero sees exactly what it expected and

13:01 continues transmitting. But the

13:03 controller that sent a one reads back

13:04 zero and immediately realizes that it

13:06 has lost arbitration. Another message

13:09 has a lower numerical identifier and

13:10 therefore a higher priority. So it's

13:12 time to shut up and be quiet. The losing

13:15 controller stops transmitting, becomes a

13:17 receiver, and waits for its next

13:18 opportunity. And that's all there is to

13:20 it. No frame was corrupted. No collision

13:23 recovery was required. Nobody generated

13:26 a random delay. The winning frame

13:28 continues as though nothing unusual ever

13:29 happened. And importantly, there is no

13:31 retry. The original message makes it out

13:33 unscathed the first time, the first

13:35 attempt. And better yet, they all come

13:37 out in perfect priority order. The CAN

13:40 specification calls this non-destructive

13:42 bitwise arbitration. A controller loses

13:45 when it transmits recessive but observes

13:47 dominance during the arbitration field

13:49 at which point it withdraws without

13:51 corrupting the winning frame. The reason

13:53 this works is wonderfully compact. At

13:55 the first differing bit, the identifier

13:57 containing zero must be numerically

13:59 smaller than the identifier containing

14:00 one because the identifier is being

14:03 transmitted from its most significant

14:04 end. The electrical properties of the

14:06 bus therefore perform a binary

14:08 comparison among all competing

14:09 identifiers in real time. The network

14:12 does not merely discover which message

14:13 is higher priority. The wires actually

14:15 calculated and that is an important

14:17 distinction. The device itself did not

14:20 win. The message with the identifier

14:22 101. On the next transmission, the very

14:24 same device could send a lower priority

14:26 status frame and lose to another

14:28 controller. Priority belongs to the

14:30 message, not permanently to the machine

14:31 or to the device. This gives CAN an

14:34 elegant form of real-time scheduling.

14:36 Important frames naturally move ahead of

14:38 less important ones. And if the bus is

14:40 lightly loaded, everybody speaks out

14:41 almost immediately. As the bus becomes

14:43 busy, lower priority frames experience

14:46 more delay while higher priority frames

14:48 remain responsive. And the cool part is

14:50 that when the bus is busy, the message

14:51 automatically comes through sorted in

14:53 priority order just by virtue of when

14:55 they are allowed to communicate. And

14:57 that is extremely useful in a car where

14:58 not all information is equally urgent.

15:01 The fact that you press the volume up

15:02 button does matter. The fact that a

15:04 wheel has suddenly stopped rotating

15:06 while the other three continue at

15:07 highway speed probably matters more. But

15:09 priority also introduces a danger. A

15:12 defective or hostile controller that

15:14 continuously transmits valid frames with

15:16 a low ID can consume most of the bus

15:18 bandwidth. Other controllers may remain

15:20 electrically functional and perfectly

15:22 willing to communicate yet rarely or

15:23 never get the chance. Canon includes

15:26 robust mechanisms for dealing with

15:27 maleformed frames and electrically

15:29 broken controllers, but a device

15:30 transmitting valid, correctly formatted,

15:33 high priority message is not necessarily

15:35 violating the protocol. From CAN's

15:37 perspective, it might simply have an

15:38 endless supply of extremely important

15:40 news. So Ken assumes a substantially

15:43 more trusted environment than the public

15:45 internet, which is okay because the

15:46 participating devices are generally

15:48 designed as components of one machine

15:50 installed by its manufacturer and

15:52 expected to cooperate, which is a

15:54 perfectly reasonable assumption right up

15:55 until somebody attaches an untrusted

15:57 device to the diagnostic connector under

15:59 the dash. Before we get to security,

16:01 however, we need to look at what happens

16:02 after arbitration. Once a message has

16:05 one control of the bus, it sends its

16:07 control information, data, air checking

16:09 fields, acknowledgement, and end of

16:11 frame markers. Classic CAN carries as

16:14 many as eight, count them, eight

16:15 databytes in one frame. Now, I get that

16:17 eight bytes does not sound like much

16:19 when your desktop computer routinely

16:21 moves gigabytes around, but it's enough

16:22 for the kind of compact measurements and

16:24 commands that CAN was created to carry.

16:27 After all, an engine speed message does

16:28 not need a JPEG attachment. It may need

16:31 two bytes for RPM, another bite

16:32 containing flags, and perhaps a rolling

16:34 counter and enough context established

16:36 by the vehicle's private message

16:38 definition to make sense of it.

16:39 Importantly, CAN does not itself dictate

16:41 what those eight bytes mean. That's up

16:43 to the sender and any interested

16:45 receivers. And it is one of the most

16:47 important conceptual boundaries in the

16:48 whole system. CAN defines how a frame

16:50 gets onto the wire, how it wins

16:52 arbitration, how receivers detect

16:54 errors, and how the network corrects and

16:56 contains faulty nodes. It does not tell

16:58 you identifier 0x1 A0 contains engine

17:01 speed in bytes three and four scale by

17:03 one quarter of an RPM. That meeting

17:05 belongs to a higher layer protocol or in

17:07 many vehicles to a manufacturer's

17:09 private database. And that is why

17:11 attaching a CAN analyzer to a car

17:13 immediately produces a beautiful stream

17:14 of perfectly valid hexodimal messages

17:17 with almost no useful information. You

17:19 can see that the frame 0x1 A0 has

17:22 arrived and you can see it's a datab.

17:24 You can see that one bite changes as you

17:26 press the accelerator perhaps. But CAN

17:28 does not provide a tiny label saying by

17:30 the way this bite represents throttle

17:31 position multiplied by 392 and please

17:34 ignore the upper two bits. You just have

17:36 to know you have to know the language's

17:38 alphabet and grammar but you don't yet

17:40 have its dictionary. The ESP32 has a

17:42 listenon mode that's especially useful

17:44 here. A CAN controller normally

17:46 participates in the protocol including

17:48 acknowledging valid frames. In

17:50 listenonly mode, our ESP32 can observe

17:52 the network without influencing it,

17:54 which is exactly what you want when

17:55 first connecting test equipment to an

17:57 unfamiliar vehicle network. Espresso

17:59 explicitly provides this mode so the

18:01 controller can receive traffic without

18:03 affecting the bus. Acknowledgement is

18:05 another clever little feature. After a

18:07 transmitter sends a valid frame, it

18:09 releases the bus during the

18:10 acknowledgement slot. Any receiver that

18:12 has correctly received the frame may

18:14 drive that slot dominant. The

18:16 transmitter does not learn which

18:17 controller heard it. It simply learns

18:19 that somebody got it. This is not an

18:21 application level reply. The dashboard

18:23 is not saying, "Yes, I have updated the

18:25 tachometer." It's only a data link

18:26 acknowledgement, meaning that at least

18:28 one other CAN bus module out there saw

18:30 your bits, got them, received them,

18:32 decoded them, and they looked right. If

18:33 nobody acknowledges the frame, though,

18:35 the transmitter knows that it may be all

18:37 alone, disconnected, configured for the

18:39 wrong speed, or otherwise barking into

18:41 the dark. CAN also checks its own work

18:43 obsessively. Every frame carries a CRC.

18:46 Transmitters monitor the bus while

18:48 sending and receivers verify the frame

18:50 structure as it arrives. It also uses

18:52 bit stuffing to keep everybody

18:53 synchronized. After five identical bits

18:56 in a row, the transmitter inserts one

18:58 bit of the opposite value. So, it flips

19:00 the bit. Now, receivers know to discard

19:02 that extra bit. But if the expected

19:04 transition never appears, they know the

19:06 frame is corrupt because the line should

19:08 never be held that long. And when any

19:10 controller detects an error,

19:11 deliberately transmits an error flag

19:12 that invalidates the frame for

19:14 everybody. The message is discarded and

19:16 retrieded. That sounds a bit dangerous

19:18 because one broken controller could

19:19 object to everything and hold the

19:20 network hostage. CAN solves that with

19:22 fault confinement. Every controller

19:25 maintains air counters and repeated

19:26 misbehavior progressively demoted from

19:28 air active to air passive and finally

19:30 bus off where it's effectively exiled

19:32 from transmission. It's a tiny

19:34 distributed society with arbitration,

19:36 proofreading, public rejections, and

19:38 eventually banishment all without a

19:39 central authority. The wiring is equally

19:42 approachable. On a dead CAN bus, you can

19:44 begin with a meter and a scope. An

19:46 unpowered, correctly terminated bus, as

19:48 we said, should measure about 60 ohms

19:49 across CAN high and CAN low. On the

19:52 scope, the line should sit together when

19:53 recessive, separate cleanly during

19:55 dominant bits, and show minimal ringing

19:57 or reflection. That does not make every

19:59 fault easy. A loose connector in a

20:01 vibrating, wet, freezing automobile can

20:03 still produce a sort of intermittent

20:04 failure that makes technicians question

20:06 their career choices. But can let you

20:08 reason all the way from the voltage on

20:10 the wire to the message in the software.

20:12 Which brings us back to the Corvette

20:14 computer. The ECM or computer has no IP

20:17 address and opens no connection to the

20:19 dashboard. It simply has a connection to

20:21 those two wires and broadcast messages

20:23 with defined identifiers and payloads.

20:25 Engine speed is published once and the

20:27 dashboard, transmission, traction

20:28 control system, diagnostic tool, and

20:30 data logger may all consume that same

20:33 frame. That loose coupling is one of

20:35 CAN's greatest strengths. It's also one

20:37 of its central security weaknesses.

20:39 Traditional CAN does not authenticate

20:41 the source of a frame. If a hostile

20:43 controller knows the correct identifier

20:45 in a payload format, it may impersonate

20:47 a legitimate module. The other

20:49 controllers see a valid identifier, a

20:51 valid CRC, and a perfectly legal frame.

20:53 Electrically and structurally, nothing

20:55 is wrong. Now, this can also be handy.

20:58 On my old BMW M3, a 2003 that used

21:01 canvas, I added a feature where if you

21:03 unlock the car three times in a row

21:04 within 5 seconds with the key fob, it

21:07 would see that and then it would inject

21:08 the commands that I otherwise had

21:10 recorded and seen to lower the top. So,

21:13 I lowered the top manually a couple

21:14 times, captured that data, figured out

21:16 what I had to send to simulate a push

21:17 the top down button, and I would do that

21:20 when I saw three unlocks. And that's

21:22 because CAN's designers were not

21:23 careless. They were building a trusted

21:25 physically enclosed network with 1980s

21:27 processors and budgets. The danger

21:29 appeared later when those closed

21:31 networks gained diagnostic ports,

21:33 wireless infotainment, cellular modems,

21:35 aftermarket dongles, and millions of

21:37 lines of externally reachable code. CAN

21:40 is simple because it knows where its

21:41 universe ends. Security problems begin

21:43 when we quietly move that boundary. And

21:45 yet, its limitations make it more

21:47 impressive, not less. Because with two

21:48 wires and a handful of rules, CAM

21:50 provides noise rejection, deterministic

21:52 priority, non-destructive arbitration,

21:54 acknowledgements, retransmission, CRC

21:57 checking, clock recovery, and fault

21:58 confinement. Put two traces on a scope

22:00 and you can see a dominant zero form

22:02 right there. Trigger two controllers

22:04 together and watch the lower identifier

22:06 win at exactly the bit where they

22:07 disagree. Remove a terminator and watch

22:09 the reflections appear. Unplug the

22:11 Corvette ECM and watch the entire family

22:13 of identifiers just vanish from the bus.

22:16 Nothing about it is magic. Now, can

22:18 isn't simple because it does very

22:19 little. It's simple because a few

22:21 exceptionally well-chosen rules do a

22:23 great deal. If you have comments or

22:25 questions on today's episode, please

22:27 leave them in the video comments. And

22:28 then check out an episode of Shop Talk

22:30 every Friday on the second channel where

22:32 we answer the week's best questions and

22:33 insights. If you found today's episode

22:36 interesting or entertaining, remember

22:37 I'm mostly in this for the subs and

22:38 likes. So, I would be honored if you

22:40 consider leaving me one of each before

22:41 you go today. If you don't normally do

22:43 that, I would appreciate it maybe on

22:44 this episode because it's got this

22:46 automotive tie in that is usually death

22:47 for my channel, but I really wanted to

22:49 do Canvas. So, if you did like it, give

22:51 it a like. Thanks. And in the meantime,

22:53 in between time, hope to see you next

22:55 time right here in Dave's garage. Oh, I

22:57 said it different today.

23:01 >> Do it, Lynn. Do it. Do it.

