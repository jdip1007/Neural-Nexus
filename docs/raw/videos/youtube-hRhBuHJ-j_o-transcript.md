---
source_url: https://www.youtube.com/watch?v=hRhBuHJ-j_o
source_type: video
ingested: 2026-09-15
published: 2026-09-15
duration_minutes: 22
language: en
sha256: 60220122f0dcf5b6c29373c86a28e4ba1918ec70c0e37d9a6b516ae1bccd38c8
time_sensitive: True
---

# YouTube Transcript: The Secret RGB LED Features I Hid in this 1970 Lincoln Continental Mark III

## Video Information
- **Title**: The Secret RGB LED Features I Hid in this 1970 Lincoln Continental Mark III
- **Video ID**: hRhBuHJ-j_o
- **Published**: Unknown
- **Views**: Unknown
- **Language**: en

## Transcript
00:00 Hey, I'm Dave. Welcome to my shop.

00:02 Today's episode starts with what looks

00:04 like a very simple question. How hard

00:06 could it possibly be to add a third

00:08 brake light to an old car? And the

00:10 answer, as usual, is hard enough to

00:13 actually be pretty interesting. Because

00:14 this isn't just a story about sticking a

00:16 red LED strip on a bumper and calling it

00:18 a day. This is a story about taking a

00:21 1970 Lincoln Continental Mark III, a car

00:24 with only about 12,000 mi on it from

00:26 new, a car that still looks like it

00:28 slipped through a wormhole from Nixon's

00:30 first term, and adding an otherwise

00:31 invisible modern safety system without

00:33 drilling any holes in it, without

00:35 hanging some ugly plastic wart in the

00:36 rear window without making it look like

00:38 somebody attacked the classic luxury car

00:40 with the RGB lighting aisle from a micro

00:42 center. So, why should somebody watch an

00:44 entire episode about an LED taillight if

00:46 they're never actually going to build

00:47 one? Because the tail light is just the

00:49 visible part. The interesting part is

00:51 the translation layer hidden beneath it.

00:53 It's a tiny case study in embedded

00:55 systems, signal isolation, automotive

00:57 power, human factors, legacy

00:59 integration, state machines, timing

01:01 tolerances, safety priorities, and

01:03 difference between it works in my bench

01:04 and it works in the car. It's also a

01:07 story about translation because on one

01:09 side you've got a 55-year-old electrical

01:11 system built from switches, bulbs,

01:13 flashers, copper wire, and the kind of

01:15 cultural optimism that says a seatback

01:17 ending halfway up your spine is probably

01:19 all the neck protection a tough guy like

01:21 me really needs. And then on the other

01:23 side, you've got a modern ESP32

01:25 microcontroller running at hundreds of

01:26 millions of cycles per second, driving

01:28 individually addressable LEDs, parsing

01:30 timing windows measured in milliseconds,

01:32 and making decisions about whether the

01:34 car is breaking, turning left, turning

01:36 right, backing up, or doing some

01:37 combination of those things all at the

01:39 same time. And in between those worlds

01:41 is the really interesting part. A little

01:43 circuit board whose entire job is to

01:45 listen to classic cars speak in 12vt

01:48 grunts and translate that into clean

01:50 digital facts. And the reason all this

01:52 matters is pretty simple. Old cars are

01:54 beautiful, but they were not designed

01:56 for a world where the person behind you

01:57 might be checking a text message,

01:59 adjusting Apple CarPlay, eating fries,

02:02 and driving an 8,000lb SUV with the

02:04 kinetic energy of a small moon. And the

02:06 Mark III has another problem, which is

02:07 that it does not exactly have modern

02:09 head and neck support. So getting

02:10 rear-ended in this car is not something

02:12 I'm eager to experience as an

02:13 educational exercise. In fact, it's

02:16 something I'll go to some lengths to

02:17 actively avoid. Modern cars have a

02:19 center high-mounted stop lamp or CHMSL

02:22 because people notice it. It sits

02:24 higher. It's closer to the driver's line

02:26 of sight. And it gives the person behind

02:28 you another chance to realize that the 2

02:30 and 1/2 ton landot ahead of them is

02:32 actually stopping. But the Mark III

02:34 predates that requirement by a long way.

02:35 And I don't want to bolt anything

02:37 obvious onto the car. When the lights

02:39 are off, I want the car to look entirely

02:41 original. Not mostly original. Not

02:43 original except for the obvious LED bar,

02:45 but original. And fortunately, the car

02:47 gave me one tiny gift. Under the bottom

02:49 edge of the trunk, just above the

02:51 bumper, there's a gap of about/ an inch.

02:53 It's not perfectly straight, cuz of

02:55 course it isn't, but it runs across the

02:57 rear of the car in almost exactly the

02:59 place that you'd want to hide a light.

03:01 That became the slot, the little shadow

03:02 line where 6 ft or so of addressable

03:04 LEDs could disappear until called into

03:06 service. And this is where a simple

03:08 lighting project turns into a systems

03:10 project. If you're doing this on a

03:12 modern car, you might be tempted to go

03:14 looking for a CAN bus message because

03:16 there might be a nice little packet

03:17 somewhere that says the brake pedal is

03:19 down, the left signal is active, the

03:20 right signal is active, reverse is

03:22 selected, and maybe even what radio

03:24 station the driver is listening to. But

03:26 this car is from 1970. There is no CAN

03:29 bus. There's no body control module.

03:32 There's no friendly digital truth just

03:34 waiting to be queried. They're just

03:35 wires. And unfortunately, the wires do

03:38 not say what you wish they said. At the

03:40 rear of the Lincoln, I can see the left

03:42 lamp, and I can see the right lamp, and

03:44 I can see the backup lamps, but there's

03:45 no separate signal that says the brakes

03:47 are active. There is no separate signal

03:49 that says the left turn signal is

03:51 active. The same rear lamp can mean

03:53 different things depending on time and

03:55 context, and that is the whole trick.

03:57 Imagine the left rear lamp turns on.

03:59 What does that mean? It might mean the

04:01 driver is now signaling left. But it

04:03 might also mean that the driver has

04:05 pressed the brake pedal and that both

04:06 rear lamps are on. It might mean we were

04:08 in the middle of a more complicated

04:09 state where the brakes are being held

04:11 down and one side is blinking because

04:12 the driver is stopped and signaling a

04:14 turn. And that last case is the one that

04:16 turns the whole thing from a wiring job

04:18 into a state machine. We're

04:19 old-fashioned here in America and we

04:21 like things certain ways. We likes our

04:23 front signal lights amber and our rear

04:24 signal lights red and never the twain

04:26 shall meet. And while we're progressive

04:28 enough to finally allow amber rear

04:29 signals these days, if you're into that,

04:31 in 1970 there was just no chance.

04:33 Society just wasn't ready yet. And so in

04:35 those days, our rear signals were always

04:37 as red as the flags of our thermonuclear

04:39 adversaries. Which is all to say that on

04:42 an old American car like this, the brake

04:44 lights and the turn signals share bulbs.

04:46 So when you are braking, both rear lamps

04:48 illuminate. But if you were stopped at

04:50 an intersection with the brake pedal

04:51 down and then you signal right, the left

04:53 lamp stays on solid while the right lamp

04:55 blinks. Electrically, that is not

04:57 braking plus a right signal as a nice

04:59 clean pair of digital facts. Because

05:01 electrically the one side's steady and

05:03 the other side is alternating. The car

05:05 knows what it means because the car

05:06 created the actual condition. But my

05:09 circuit only gets to observe the

05:10 aftermath. That means it has to infer

05:12 the driver's intent. And inference is

05:14 where things get interesting. The

05:16 simplest version would say that if both

05:18 lamps are on, we're breaking. If only

05:20 the left lamp is blinking, we're

05:21 signaling left. If only the right lamp

05:23 is blinking, we're signaling the right.

05:24 And if neither is on, we're just driving

05:26 along, probably looking terrific. But

05:28 that's not enough because the real world

05:30 refuses to stay in the simple state

05:31 diagram that you would draw on the

05:33 whiteboard. For this, the

05:34 microcontroller has to know not only

05:36 what lamps are doing right now, but how

05:38 they got there. It has to remember

05:40 whether braking was already active. So,

05:42 it has to watch for edges, those moments

05:43 when the lamp changes from off to on. It

05:46 has to measure the timing between the

05:47 left and right sides. And if both sides

05:49 come on close enough together, say

05:51 within some small timing window, that is

05:53 probably the brake pedal being pressed,

05:54 even if there's two switches. But if one

05:57 side starts blinking by itself, that's

05:58 probably a turn signal. And once the

06:01 braking state has been detected, braking

06:03 remains active until both lamps are no

06:05 longer active. This is one of those

06:07 problems that looks trivial until you

06:09 actually try to code it correctly. The

06:11 brake animation itself is designed to be

06:13 conspicuous without being too

06:14 ridiculous. It starts illuminated

06:16 immediately because the whole point is

06:18 to say stop right now, not after a cute

06:20 startup animation. Then it blooms

06:22 outward from that initial center,

06:24 expanding until the entire strip becomes

06:26 red. During the first few moments, it

06:28 also pulses between medium and full

06:30 brightness, but it never actually goes

06:31 dark. That distinction matters because a

06:33 brake light that disappears during its

06:35 own attention getting animation is

06:36 defeating the purpose. The goal is not

06:39 to create a little time square under the

06:40 trunk. The goal is to be noticed by the

06:42 person behind me before physics holds a

06:44 vote on how the rest of my day is going

06:46 to go. I'm going to be very careful here

06:48 and say that I'm not claiming the system

06:50 is street legal. I looked at the

06:52 relevant lighting rules, particularly

06:53 FMVSS number 108 because that is the

06:56 federal standard that deals with vehicle

06:57 lamps and associated equipment. But

06:59 unless you have the right equipment, the

07:01 phototric testing, the mounting

07:02 validation, and all the rest of the

07:04 whole certification process, you should

07:07 not pretend that your garage project is

07:08 suddenly a certified automotive lighting

07:10 component. So for our purposes, this is

07:12 a show use only project and any legal

07:15 interpretation you make for your own car

07:17 is between you, your local laws, and the

07:19 officer who may not share your

07:20 enthusiasm for addressable LEDs. That

07:23 said, I still wanted to design it as

07:24 responsibly as I could. Red means

07:26 braking, amber means turn signal, white

07:29 means reverse, and the emergency mode,

07:31 which I added simply because it looks

07:32 extremely cool in the garage, is not

07:34 connected to the vehicle in any way that

07:36 allows it to activate accidentally. cuz

07:39 out of an abundance of caution, that

07:40 input is tied to ground. So, it can't

07:42 suddenly decide to do a red and blue

07:43 police style animation while I'm out on

07:45 public roads. But if you are a police

07:47 officer with an undercover 1970 Mark

07:49 III, then first of all, congratulations

07:51 on having tremendous taste. Say hi to

07:53 Canon for me. But for the rest of us,

07:55 this mode is for demonstration only.

07:57 Now, let's talk about the hardware

07:58 because this is where the project

07:59 becomes less like car customization and

08:01 more like building a small embassy

08:03 between two hostile electrical nations.

08:05 A car's electrical system is not a

08:07 polite 12vt clean. It's a nominal 12vt

08:10 system, which means it might be 12 volts

08:12 or maybe even 11 with the engine off,

08:14 closer to 14 or 15 when the alternator

08:16 is charging, lower during cranking, and

08:18 full of spikes, dips, inductive

08:20 nonsense, and the general electric mood

08:22 swings of an old vehicle. The ESP32,

08:25 meanwhile, expects civilized low voltage

08:27 power. It does not want to be introduced

08:30 directly to the Lincoln's lighting

08:31 harness any more than you want to drink

08:32 from a rusty fire hose just cuz you're

08:34 very thirsty. So, the board needed three

08:36 big functional blocks. It needed a power

08:39 supply to turn the vehicle's messy 12 to

08:41 15V world into a regulated 5V for the

08:44 microcontroller. It needed input

08:46 protection and isolation so the car's

08:48 lighting signals could be sensed safely.

08:50 And it needed the ESP32 itself, which

08:52 would run the logic and drive the LED

08:54 strip. My first approach, a similar

08:56 project for my 1970 GMC truck, actually

08:59 used relays. And relays are wonderfully

09:02 intuitive. The vehicle's 12volt signal

09:04 energizes the coil, the relay closes,

09:06 and a separate isolated 5V signal goes

09:09 to a GPIO pin. There's something

09:11 reassuringly mechanical about it. You

09:12 can hear it click. You can understand it

09:14 in one glance, and it works. But it's

09:16 not the best way to do it. There is a

09:18 better way. And for this PCB, I used

09:20 optoouplers. An optooupler is one of

09:23 those components that feels like a magic

09:24 trick until you realize how simple it

09:26 really is. Inside the little chip is an

09:28 LED and a light sensitive transistor or

09:30 detector. When the vehicle side sends

09:33 current through the internal LED side,

09:34 it shines across a tiny gap inside the

09:37 package. The detector on the other side

09:39 sees the light and switches the

09:40 microcontroller side signal. And so the

09:43 two sides are electrically isolated.

09:45 There is no copper path between the car

09:47 circuit and the ESP32's GPIO pin. The

09:50 information crosses the gap as light.

09:52 That is elegant. It is also exactly the

09:54 sort of thing you want when you're

09:56 connecting a delicate microcontroller to

09:58 a noisy automotive circuit. We don't

10:00 need to share the car's electrical

10:01 chaos. We only need to know whether a

10:03 lamp circuit is active or not. The PCB

10:05 itself was laid out in easy EDA, which

10:07 is made by JLCPCB, and that was all new

10:10 to me, but surprisingly approachable.

10:12 And one of the nice things about the

10:13 modern hobby electronics world now is

10:15 how absurdly powerful the tooling has

10:17 become. You can lay out the schematic,

10:19 assign real parts, route the board,

10:21 inspect it in 3D, and in some cases,

10:23 have the whole thing manufactured and

10:24 assembled for you. That still feels a

10:26 little like science fiction to somebody

10:28 who remembers etching their own PCBs.

10:30 For this project, I ordered bare PCBs

10:32 and then soldered the parts myself, cuz

10:34 I was only making one or two. The

10:36 connectors all live along one edge of

10:37 the board because in a car installation,

10:39 connector sanity matters. First, there's

10:42 an LED strip connector with ground,

10:44 data, and power. And then come the

10:46 vehicle inputs, backup lights, auxiliary

10:48 input, left tail light, right tail

10:50 light, chassis ground, and vehicle

10:52 12volt power. The power stage is a buck

10:54 converter, a switching regulator that

10:56 efficiently steps the car's voltage down

10:57 to 5 volts. A linear regulator would

11:00 burn the extra voltage away as heat,

11:01 which is fine for tiny currents, but bad

11:03 for anything bigger. A buck converter

11:05 works more like a little electronic

11:07 flywheel, rapidly switching energy into

11:09 an inductor and then smoothing it out

11:11 with capacitors so the output stays

11:12 regulated even as the input wanders

11:14 around. And then because no project is

11:17 complete without discovering something

11:18 awkward while explaining it, I realized

11:20 an important detail while planning this

11:22 episode. The board's 5V supply is

11:25 carefully regulated and the ESP32 is

11:27 being treated properly. But the LED

11:29 strip I used in this version is a 12volt

11:31 strip which means I just fed it directly

11:33 vehicle power. It works perfectly on the

11:35 bench and in the install. But from a

11:37 design purity standpoint, it's not ideal

11:40 cuz as we noted, the vehicle supply can

11:42 be noisy and the voltages can vary

11:43 substantially. The better design would

11:45 either regulate the 12volt LED supply as

11:48 well or use a 5V LED strip powered from

11:50 the clean 5V regulator on the PCB.

11:53 That's probably the easiest. It should

11:55 be able to handle the current of the

11:57 entire strip. Or at least that's the

11:58 plan. That's one of the fun things about

12:00 not knowing very much about electronics.

12:02 It turns out that pretty much everything

12:03 you can think of was already invented

12:05 decades ago. The relay version works,

12:07 but the optooupler version is still

12:09 better. And when it comes to any kind of

12:10 engineering, better has a flavor that

12:12 never really gets old. Now, a quick word

12:15 on the LEDs themselves. Because

12:17 addressable strips are one of the most

12:18 enjoyable things to play with in modern

12:20 electronics. A typical RGB LED strip of

12:23 this type lets you control each LED

12:25 individually. You don't simply turn the

12:27 whole strip red. You say LED number zero

12:29 is red at this brightness. LED number

12:31 one is red at this brightness. And LED

12:33 number 27 is amber. Each LED receives

12:36 data, keeps the part meant for itself,

12:38 and passes the rest down the line. That

12:40 lets us create animations that are not

12:42 just flashy, but semantically

12:43 meaningful. The left signal can sweep

12:46 amber from the center towards the left.

12:48 The right signal can sweep amber toward

12:49 the right. Reverse can illuminate the

12:51 whole thing white. Braking can bloom red

12:53 from the center outwards. And because

12:55 there are only a couple of hundred LEDs

12:56 in the whole chain, the refresh rate is

12:58 fast enough to avoid any kind of

12:59 noticeable flicker. In software terms,

13:02 the LED strip is basically a frame

13:04 buffer. It's a long skinny display, but

13:06 instead of pixels on a monitor, the

13:08 pixels are stretched across the rear of

13:09 a Lincoln. And like any display, what

13:11 matters is not just what you draw, but

13:13 when you draw it. So the ESP32 main loop

13:16 is centered around processing the inputs

13:17 and displaying the correct effect. It

13:20 checks the left and right lamp signals.

13:21 It checks backup. It checks auxiliary.

13:23 It decides whether braking is currently

13:25 active. It decides which animation has

13:27 top priority. And then it renders the

13:29 frame. The brake effect gets special

13:31 treatment because it must override

13:33 almost everything else. A turn signal is

13:35 useful, but a reverse light is also

13:37 useful. But a brake light is urgent.

13:39 When the brake event begins, the brake

13:41 animation takes priority because the

13:42 garbage truck behind you does not care

13:44 that your state machine was halfway

13:45 through a really cool amber sweep. And

13:47 this is one of those places where

13:49 software design and safety design line

13:51 up. Priority matters. The state machine

13:53 cannot be democratic. Some inputs

13:55 outrank some others. For turn signals,

13:58 the synchronization is the actual trick.

14:00 The car's original lamp is blinking

14:02 according to its own old school flasher

14:04 timing. You know those pots that go tick

14:06 tick tick. Yeah, just like that. I don't

14:08 want the LED animation running at its

14:10 own schedule and slowly drifting out of

14:12 phase like a badly dubbed movie. So when

14:14 the left lamp transitions from off to

14:16 on, the left signal animation resets and

14:18 starts again. Every flash from the car

14:20 becomes a timing sync mark. The LED

14:23 strip takes its cue from the original

14:25 lamp. That gives the result that the

14:27 amber animation always appears perfectly

14:29 synchronized with the vehicle's own

14:30 signal cuz it's not trying to replace

14:32 the car's lighting logic. It's following

14:34 it and it's enhancing what was already

14:35 there. And that distinction is

14:37 important. The system is deliberately

14:39 parasitic in the benign sense. It

14:41 observes the car. It does not take over

14:43 the car. It does not interrupt the

14:45 factory brake signals at all. It does

14:47 not sit between the driver and the

14:48 original lamps. So, if my board were to

14:50 fail, the factory light should continue

14:52 doing what they always did. And that's

14:54 the right philosophy when adding

14:56 electronics to a classic vehicle,

14:57 especially one that you want to keep

14:58 original. The modification should be

15:00 reversible and it should at least fail

15:02 in the least dramatic way possible.

15:05 There's also a neat little philosophical

15:06 point here about old systems and new

15:08 systems. The Lincoln's wiring harness

15:10 does not know what a state machine is.

15:12 It was not designed to express six

15:14 different semantic states through a nice

15:15 API. It just energizes wires. But when

15:18 you observe those wires over time, then

15:20 information appears. A single sample is

15:23 ambiguous, but a sequence over time has

15:25 meaning. And that's not just automotive

15:27 electronics. That's computing in

15:28 general. A bit is just a bit until you

15:30 know where it came from, when it

15:32 changed, and what state the system was

15:33 in before it changed. Context turns

15:36 voltage into information. And the best

15:38 example is breaking. Suppose the ESP32

15:41 sees the left lamp on and the right lamp

15:42 on. If those two events occur within a

15:44 small window of one another, it knows

15:46 that's breaking. But suppose the left

15:48 lap has been on for a while and the

15:50 right lamp is now blinking. That's

15:52 probably breaking while signaling right.

15:54 The same two inputs sampled at different

15:56 moments mean different things. And this

15:58 is why naive input pooling would give

16:00 naive answers. The timing window exists

16:02 because the ESP32 is much faster than

16:05 the system. is watching. The

16:07 microcontroller can observe the world

16:08 with absurd precision compared with the

16:10 mechanical and electrical realities of a

16:12 1970s car. If you ask it where the two

16:14 lamps turned on at exactly the same

16:16 time, the answer will almost always be

16:18 no. Because exactly to a 240 MHz

16:21 microcontroller is not the same as

16:22 exactly to a couple of brake light

16:24 switches, a turn signal switch, and

16:25 50-year-old wiring. The code has to be a

16:28 little forgiving. Within a few

16:30 milliseconds, we consider them

16:31 simultaneous enough. That's a

16:33 surprisingly common engineering pattern.

16:35 The smarter part of the system has to

16:36 learn not to be too smart. Precision

16:38 without tolerance becomes brittleleness.

16:40 Once braking starts, the system remains

16:42 in braking mode until both rear lamps

16:45 are off at the same time. That prevents

16:46 the brake animation from dropping out

16:48 just because one side is blinking due to

16:50 a turn signal. It also means the system

16:52 behaves like a driver expects. If I'm

16:54 stopped with my foot on the brake and

16:55 signaling right, I don't want the third

16:57 brake light to have an existential

16:58 crisis every half a second. I wanted to

17:00 keep saying this car is stock while also

17:02 allowing the amber turn animation to

17:04 communicate direction where appropriate.

17:06 And that balance between correctness and

17:07 clarity is the real design work because

17:09 you can make animations that are

17:10 visually impressive but semantically

17:12 confusing. You can make something that

17:14 looks amazing in a garage and terrible

17:16 in traffic. You can make a brake light

17:18 that's so clever it becomes ambiguous

17:19 and ambiguous lighting on the back of a

17:21 car is a bad idea. So the animations

17:23 need to be restrained. Red is brake,

17:25 amber is turn, white is reverse. Motion

17:27 supports meaning. It does not replace

17:29 meaning. The emergency mode is the one

17:31 exception and that's why it is isolated.

17:33 It uses red and blue for demonstration

17:36 purposes and it strobes and it takes

17:37 advantage of full color capability of

17:39 the strip. It's fantastic for showing

17:41 what the hardware can do. It's also

17:43 exactly the kind of thing you don't want

17:44 to accidentally trigger in public. Now,

17:46 mechanically, the install is almost as

17:48 important as a circuit. A classic car

17:50 like this deserves a light touch. The

17:52 strip needs to be hidden, aligned,

17:53 protected, and serviceable. It has to

17:55 survive vibration, temperature changes,

17:57 moisture, and the general indignities of

17:59 being mounted near the rear bumper of an

18:01 actual car. Bench projects live in ideal

18:03 conditions, but car projects live in the

18:05 weather, next to exhaust, next to

18:07 vibrating sheet metal, and downstream

18:09 from every puddle that you drive

18:10 through. I don't drive through puddles,

18:12 but mounting it is not just about making

18:14 it pretty. It's also about strain

18:16 relief, routing wires safely, avoiding

18:18 sharp edges, and making sure that

18:19 nothing can chafe through over time.

18:22 Automotive wiring failures aren't often

18:23 dramatic failures. They're slow

18:25 mechanical failures because a wire rubs

18:27 against the bracket or a connector hangs

18:28 where water collects. A solder joint is

18:31 asked to be a structural member. And

18:33 then one day, the thing that worked

18:34 perfectly in the garage becomes an

18:35 intermittent gremlin. And intermittent

18:37 gremlins are where hobby projects go to

18:38 become folklore. The other important

18:40 installation detail is that this system

18:42 is not trying to visually modernize the

18:44 car when it is off. That was the whole

18:46 premise. I don't want somebody walking

18:47 up to the Lincoln at a show and

18:49 immediately seeing a strip of LEDs. I

18:51 just want them to see the car. So, the

18:53 lighting only reveals itself when it has

18:55 something to say. And that is, I think,

18:57 the difference between a tasteful

18:58 modification and a gadget bolted to an

19:00 unwilling host. The best modifications

19:02 understand the object that they're

19:04 modifying. A 1970 Continental Mark III

19:06 is not a tuner car. It's not a cyberpunk

19:09 prop. It's a rolling personal luxury

19:11 coupe from an era when a hood could have

19:12 its own weather system. The lighting

19:14 should respect that. Hidden when silent,

19:16 unmistakable when active. And that is

19:19 why the final effect works so well. When

19:21 the brakes are applied, the red bloom

19:22 across the back of the car feels modern,

19:24 but not out of place entirely. It looks

19:26 like something the car might have had if

19:28 the technology had existed, and if the

19:29 safety rules of the time had demanded

19:31 it, then that's kind of the sweet spot.

19:33 There's also something satisfying about

19:35 solving this with a real PCB instead of

19:36 a dangling science experiment.

19:38 Breadboards are great for proving a

19:40 concept, but they are terrible for

19:42 permanence installations. Proto boards

19:44 are better and I've used them

19:45 successfully, including in the GMC. But

19:47 a custom PCB changes the character of

19:49 the project. The connections are

19:51 deliberate. The layout is repeatable.

19:52 The board has a purpose. It stops being

19:54 some wires in a microcontroller and

19:56 becomes a little embedded system. That

19:58 little embedded system has a job.

20:00 Observe, infer, decide, and display in a

20:02 loop. That pattern shows up everywhere

20:04 in computing. Sensors produce noisy,

20:06 incomplete signals. Software

20:08 reconstructs state. Outputs communicate

20:10 intent. Whether you're building a cloud

20:12 monitoring pipeline, a robot controller,

20:14 or a brake light for a classic Lincoln,

20:16 the basic loop is the same. The hard

20:18 part is not reading the inputs. The hard

20:20 part is understanding what the inputs

20:22 mean. That's the real lesson. Good

20:24 projects are not just a pile of clever

20:26 parts. They are constraints resolved

20:28 elegantly. The main constraint here was

20:30 make a modern visible third brake light,

20:32 but don't change the look of the car.

20:34 Don't depend on a CAN bus that doesn't

20:35 exist. Don't damage the factory wiring.

20:38 Don't expose the ESP32 to automotive

20:40 electrical noise. Don't confuse turn

20:42 signals with brake lights. Don't let a

20:43 demo mode become a roadside conversation

20:45 with the cops. And don't make it ugly.

20:48 The solution was a hidden addressable

20:49 LED strip, an isolated input board, a

20:51 regulated power supply, an ESP32, and a

20:54 state machine that understands that two

20:55 wires can tell a surprisingly

20:56 complicated story if you listen to them

20:59 carefully. And that to me is the fun of

21:01 it. It's not just that the back of the

21:03 Lincoln lights up with a slick red

21:04 bloom, although I will admit that part

21:06 still makes me grin. It's that the whole

21:08 thing is a tiny bridge across time. A

21:10 1970 wiring harness on one side, a

21:12 modern microcontroller on the other, and

21:14 a little optically isolated conversation

21:16 happening in between them. The car

21:18 speaks in lamps, the ESP32 speaks in

21:20 digital logic. And for a brief moment,

21:22 every time I hit the brake pedal, they

21:24 understand each other perfectly. If you

21:26 found today's episode interesting or

21:27 entertaining, remember that I'm mostly

21:29 in this for the subs and likes. So, I

21:30 would be honored if you would consider

21:31 leaving me one of each before you go

21:33 today. And if you have comments or

21:35 questions about the episode or the strip

21:36 itself, please fire away in the comment

21:38 section and then tune in every Friday to

21:40 Shop Talk on the Dave's Attic channel

21:42 where we answer the best questions. I'll

21:44 throw a link up to an episode here. Give

21:45 it a subscribe if you give it a watch

21:47 and enjoy it. In the meantime, and in

21:49 between time, hope to see you next time

21:50 right here in Dave's Garage. I'm going

21:53 to tell you what to do like signal left,

21:54 signal right, brake, shift into reverse.

21:58 >> Okay.

21:59 >> Do you know the hand signals?

22:00 >> No.

22:02 Do you remember riding a bike as a kid?

22:04 >> Yeah.

22:04 >> Your driver's test six weeks ago?

22:06 >> Yeah.

22:07 >> They teach you them?

22:08 >> Yeah.

22:08 >> Okay.

22:09 >> Oh, the handles right left.

22:10 >> Yeah. Yeah.

22:11 >> Yeah. I know that. I know that.

22:12 >> Okay. Ready? Your time to shine.

22:13 >> Okay. Okay.

22:15 >> Do it, Lyn. Do it. Do it.

