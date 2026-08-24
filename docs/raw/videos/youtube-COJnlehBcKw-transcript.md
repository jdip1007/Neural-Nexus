---
source_url: https://www.youtube.com/watch?v=COJnlehBcKw
source_type: video
ingested: 2026-08-23
published: 2026-08-23
duration_minutes: 13
language: en
sha256: ba4e5e37cf5a7568269f520f13289324decb1cf038e061ce01fc01d5b9a28c74
time_sensitive: True
---

# YouTube Transcript: Ultimate LED Effects: New Software and Hardware!

## Video Information
- **Title**: Ultimate LED Effects: New Software and Hardware!
- **Video ID**: COJnlehBcKw
- **Published**: Unknown
- **Views**: Unknown
- **Language**: en

## Transcript
00:00 today I'm going to take you step by step

00:02 all the way from one of the simplest LED

00:04 strip projects on through the most

00:05 complex up to an including delivery of

00:08 live custom effects from your PC to the

00:10 strips in real time over Wi-Fi I'll show

00:13 you the big picture from end to end to

00:15 get started let's begin with the basics

00:17 just a strip power and a module to

00:19 control it all here's a simple LED strip

00:22 setup a single individually addressable

00:24 strip connected to an esp32 module both

00:27 available from Amazon and by the way

00:29 everything you need is listed in the

00:30 video description when we Power It Up

00:33 the esp32 starts communicating with the

00:35 LED strip and sending the magical color

00:37 data to it it does this over a single

00:39 green normally data wire and so the only

00:42 connection from the chip to the strip is

00:44 one signal wire plus power and ground we

00:47 don't need to know anything about that

00:48 data signal for now other than it needs

00:50 to be connected it shows how each LED

00:52 can be addressed and set to its own

00:54 unique color but not much more to make

00:56 things more fun let's upgrade to a more

00:58 complete esp32 module the M5 stack Core

01:01 2 this M5 contains some important

01:04 accessories like a microphone a small

01:06 color display accelerometers and a lot

01:08 more but it's the audio microphone and

01:10 the display screen that we are really

01:11 interested in let's change over to the

01:14 M5 then when we connected back up to the

01:16 LEDs and power it up it's much the same

01:18 as what we saw before but if you look at

01:20 the screen we can see that it's running

01:21 a complete 16 band audio Spectrum

01:24 analyzer at about 30 frames per second

01:26 and it's displaying that Spectrum live

01:28 on the screen now it's a cool dis

01:29 display to be sure but what's more

01:31 important is that we have access to that

01:33 audio Spectrum data so we can use that

01:35 to drive our LEDs in some more visually

01:37 compelling ways the simplest case would

01:40 be a basic Vu meter that reacts to the

01:42 sound level and we can see that

01:43 operating here it's cute and an

01:45 interesting proof of concept showing

01:47 that the audio works but not something

01:48 you'd want to spend a lot of time

01:49 staring at so instead let's incorporate

01:52 the entire audio Spectrum into the

01:54 effect to visualize the entire Spectrum

01:56 we need more than a single strip we need

01:58 a matrix where we can draw hor

01:59 horizontally and vertically like a bit

02:01 map so we can draw the bars fortunately

02:03 RGB LED matrices are readily available

02:06 on Amazon so I grabbed a set of three

02:08 16x16 matrices wired up in series by

02:11 simply plugging one into the next the

02:13 LEDs internally form one long string of

02:15 LEDs wound back and forth across the

02:17 face of the Matrix this type of winding

02:20 is known as a bodon named after the way

02:22 that an ox might plow a field without

02:24 doing any backtracking to figure out

02:26 where a particular XY LED lives in this

02:28 overall strip it's a bit more complic at

02:30 as we must multiply the x coordinate by

02:32 the overall height and then add the Y

02:34 but because the Y winds back and forth

02:36 in alternate columns behind the scenes

02:37 the code actually has to figure out

02:38 whether it's an odd column or an even

02:40 column and then adjust accordingly

02:42 fortunately for us the night driver

02:43 software package that I'm using does all

02:45 this automatically you just plug the

02:47 Matrix in and connect the one signal

02:48 wire from there on out you can draw an

02:50 XY space and it appears on the LED

02:52 Matrix now we won't be running any

02:54 custom code though just installing the

02:56 Spectrum project from night driver and

02:58 it does this automatically

03:00 here we can see the Spectrum effect

03:01 running on the 48 X6 Matrix the sound

03:04 code does automatic volume leveling and

03:06 so the display adjusts of the room Audio

03:08 Level automatically it can handle

03:10 anything from Whispers to concert level

03:13 audio now this same software can also

03:16 drive a hub75 style Matrix and here we

03:19 see an example of the spectrum analyzer

03:21 effect being wired up to one these are

03:23 the same panels used to make those giant

03:25 video walls and so they're readily

03:27 available online as used Surplus from

03:29 even Amazon eBay and AliExpress with a

03:32 microphone and an IR remote control

03:33 connected you can step through a variety

03:35 of effects like this Audi graph there

03:37 are also novelty items like this

03:39 fireplace to keep me warm in the winter

03:41 and this Pac-Man chase scene there's a

03:43 pong clock and a dancing banana and a

03:45 nion cath as well as Conway's Game of

03:47 Life and about two dozen cool geometric

03:49 effects but now we're getting ahead of

03:51 ourselves because so far I have't even

03:53 said how I'm getting the software onto

03:54 this module in the first place because

03:56 normally this is a pretty big barrier to

03:58 getting started because typically teally

03:59 you're going to have to write code or at

04:01 least flash a chip yourself and that can

04:03 be complicated fortunately night driver

04:05 makes this easy because we can simply

04:07 plug your M5 in visit the web page

04:09 select the serial port and it will Flash

04:11 the module for us over the web

04:13 completely automatically when the

04:15 flashing process is complete the module

04:17 will boot up and prompt us for Wi-Fi

04:18 credentials which I'll provide having

04:21 Wi-Fi opens up a world of possibilities

04:23 as we shall see shortly Wi-Fi or not

04:26 once we have the night driver code on

04:27 the module we can use it to control the

04:29 LED and make them sound reactive the

04:31 sound code also features beat detection

04:34 which is to say that it's continually

04:35 listening to the music and looking for

04:37 regular Peaks which it considers to be

04:39 beats within the music to demonstrate

04:41 the beat detection I created a little

04:43 art project out of old glass electrical

04:45 insulators that my grandfather once

04:46 collected I added an individually

04:48 addressable LED ring inside the base of

04:50 each one and with the software installed

04:52 to configured to the insulators project

04:55 you can see that the glass insulators

04:56 react to the transitory beats in the

04:58 music and that the reaction depends on

05:00 how sharp and strong any particular bead

05:01 is I also used it to drive the fans in

05:04 my lean Lee threader case I wired all 10

05:07 fans together into one long chain and

05:09 configured the software for 16 LEDs per

05:11 fan and with the fan set project the

05:14 rest is all automatic in addition to the

05:16 flame effects there are several sound

05:18 reactive and beat reactive effects I've

05:20 added an infrared receiver to the module

05:22 so that I can control it from outside

05:24 the glass case with just a simple RGB

05:26 remote that allows me to change effects

05:28 or quiet the whole thing at the push of

05:30 a button one of my favorites in small

05:32 doses is this interesting spinning tape

05:34 reels effect that emulates the old tapes

05:36 of the 1960s IBM mainframes the software

05:39 I've been using on each of these

05:40 projects so far has been night driver a

05:42 completely free and open source project

05:44 that's on GitHub and that you can find

05:46 at night driver

05:47 led.com night driver is similar in

05:49 concept to the W LED package that you

05:51 might be familiar with but it's a fair

05:53 bit more powerful in the sense that it

05:55 supports effects that span multiple

05:57 strips effects generated on the PC color

05:59 data sent across the Wi-Fi and even

06:01 clock synchronized to the big atomic

06:03 clock in Boulder Colorado but wait

06:05 there's more with night driver the esp32

06:08 can actually control up to eight strips

06:10 in parallel with almost no loss in

06:12 performance when I first learned this I

06:14 was scratching my head trying to figure

06:15 out what could I make that requires

06:17 eight channels of LEDs and then it

06:19 struck me my patio umbrella my patio

06:22 umbrella has a Spokes and so I undertook

06:24 to add LED strips to each of them the

06:26 spokes are almost 2 meters long each so

06:29 the single one meter strip wouldn't cut

06:30 it so I literally cut it and then

06:33 soldered two strips end to end for each

06:35 of the spokes giving me about 250 LEDs

06:37 on each one then I attached each LED

06:39 strip to the underside of a spoke and

06:42 wired all the powers and grounds

06:43 together connected each to a beefy power

06:45 supply and so on each strip would be a

06:47 completely separate Channel connected to

06:49 a different pin on the esp32 and capable

06:51 of running different colors or even

06:53 different effects on each spoke I got it

06:56 all up and running and it looked great

06:57 it's become one of the main features of

06:59 my backyard at night and I learned an

07:01 important lesson just because you can

07:03 doesn't mean that you need to it was a

07:05 bit of extra cating and a lot of extra

07:06 wiring to have e completely independent

07:09 channels like this and it turns out not

07:10 to add very much almost none of the

07:13 effects really benefited from

07:14 independent Channel drawing and in the

07:16 vast majority of cases the spokes were

07:18 all mere copies of one another anyway

07:20 and that's why when a small Windstorm

07:22 finally destroyed the first version of

07:23 the umbrella I rebuilt version two as a

07:26 single Channel setup with one data lead

07:28 from the esp32 feating each of the

07:30 strips in parallel it appears the chip

07:32 can sink enough power or current for

07:34 eight signals on a single pin and so it

07:35 all works well that left me still

07:38 looking for a project where it made

07:39 sense to have different effects on each

07:41 Channel and I found a cool hanging lamp

07:43 on eBay I turned it upside down and then

07:45 added a mast to make it into a table

07:47 lamp instead of a hanging lamp and then

07:49 I stripped all over the factory

07:50 electronics and LEDs out of it next I

07:53 installed the esp32 module and then

07:55 connected it to the four strips one in

07:57 each arm of the lamp the data wire from

07:59 each strip connects to a different pin

08:01 on the esp32 and each one is a

08:03 completely independent Channel which

08:04 allows us to run different color flame

08:06 effects on each of the arms for example

08:09 like most of the projects the atomic

08:10 fire laap as I call it is also sound

08:13 reactive and has a built-in web server

08:14 so you can browse to it to configure

08:16 effects and so on it also Sports a

08:18 remote control so that you can step

08:20 through the effects and select colors

08:21 and so on and speaking of colors most

08:24 every color effect running here in my

08:26 shop is powered by an esp32 as well the

08:29 windows you see behind me are running a

08:31 simple color fill effect and each window

08:33 has its own esp32 connected to about 800

08:35 LEDs that ring the edge of the window of

08:39 course we can make it much more Dynamic

08:40 like we can set it the windows to flames

08:42 but that might be a little distracting

08:43 during the video so that's why I leave

08:45 it on solid colors when recording an

08:47 episode now it would be a lot of pain to

08:49 try to maintain all of these different

08:50 effects around the shop much less

08:52 coordinate or change the effects and

08:54 have them be consistent between the

08:55 strips that's when I decided that I was

08:57 going to add Wi-Fi to the mix

09:00 now as I mentioned there's an existing

09:01 package called wed that also has some

09:03 Wi-Fi support but it's quite different

09:05 wld uses what's knowing a UDP broadcast

09:08 and the timing and even success of UDP

09:10 isn't guaranteed it's basically fire and

09:12 forget it from the server and you hope

09:14 your strips all get the signal at about

09:16 the same time and if they all even get

09:17 it if they don't it looks terrible night

09:20 driver takes a slightly more rigorous

09:21 approach it uses tcpip sockets instead

09:24 of UDP which means the delivery of each

09:26 and every packet of color data is

09:27 guaranteed or at least you'll know both

09:29 the drop still ensuring that each strip

09:31 shows the same frame of the same effect

09:34 at the same time could be challenging so

09:36 what I wind up doing was sinking the

09:38 clock in each of the esp32s Via ntp to

09:40 the atomic clock in Boulder Colorado on

09:43 each of esp32 there's a circular buffer

09:46 of frames of color data up to the limit

09:48 of available memory and each one has a

09:50 time stamp that indicates when it should

09:51 be shown when a frame comes due it's

09:53 immediately showing on the LED strip and

09:55 as frames are received over Wi-Fi

09:57 they're added into that circular key Q

09:59 in this way all of the strips show the

10:02 exact same frame at the exact same time

10:04 now a basic esp32 can handle about 30

10:06 frames of data in its buffers and at 30

10:08 frames per second that means it can

10:10 survive about a 1C Wi-Fi hiccup but

10:13 because I wanted a bit more resiliency I

10:16 bought modules with PS Ram support and

10:18 then added psram support to night driver

10:20 and that gives each strip up to about

10:21 500 buffers or 15 seconds and if the

10:24 Wi-Fi is down for more than about 15

10:25 seconds it's likely really down but the

10:27 strips Will Survive more transient

10:29 issues without any Dropout this ability

10:32 goes well beyond just keeping two strips

10:33 in sync though it also enables you to

10:36 create an LED drawing canvas that spans

10:38 multiple disconnected strips for example

10:41 around the perimeter of the shop is an

10:43 ambient color strip I wanted the colors

10:45 to be continuous around the ceiling but

10:47 the cabinets aren't continuous and so I

10:48 didn't want to fish wires so I added

10:50 code instead that enabled spanning a

10:53 single LED strip effect across multiple

10:55 modules scattered around disconnected

10:57 physical locations that that means the

10:59 strips are connected to and take their

11:00 directions from the same server over

11:02 Wi-Fi and there's no other connection

11:04 between them yet they run in reliable

11:06 perfect sync now even I'll admit that

11:08 it's a bit of overkill for this ambient

11:10 strip but the fun doesn't end there

11:12 there's a guest house out back that

11:13 features an LED strip that runs for more

11:15 than 100 ft around its perimeter and

11:17 it's all 144 LEDs per meter that means

11:20 there are almost 5,000 LEDs in the strip

11:23 and they're connected to four different

11:25 esp32s at the server they're joined to

11:27 become a big single canvas and then

11:29 effects are rendered to the whole thing

11:31 and it just works thanks to night driver

11:33 my favorite effect is the fireworks

11:35 effect because the effect spans all four

11:37 modules virtually particles fly back and

11:39 forth from strip to strip without

11:41 interruption and are perfectly timed

11:42 when they cross strip boundaries you

11:45 might wonder why I'd go to all the work

11:46 of adding virtual Wi-Fi support when I

11:48 could I suppose just Cascade the data

11:50 wire from LED strip onto the next one

11:52 right and the problem that arises is the

11:54 frequency with which you can update the

11:56 LEDs this data signal is limited to

11:59 around 30,000 LEDs per second and at 24

12:02 bits of color it sounds admirably fast

12:04 and it actually is but there are still

12:06 some practical imitations it means you

12:08 can only do about 1,000 LEDs at once at

12:10 30 frames per second and that's why the

12:13 Cabana fireworks installation must be

12:14 split across four disconnected strips if

12:16 it were all one long strip you'd get at

12:19 most about 6 frames per second and

12:21 that's just not enough but with

12:23 synchronized Wi-Fi they draw in parallel

12:24 and they refresh it once and they run at

12:26 30 frames per second and it's all

12:27 beautiful now the night driver code is

12:29 all public and completely free open

12:31 source for non-commercial use under GPL

12:33 version 3 you can get it at night driver

12:36 led.com and in the next few months I'll

12:38 be releasing a dedicated Matrix driver

12:40 board in the form of the mesmerizer

12:42 which we saw a brief glimpse of earlier

12:44 if you're at all interested in

12:45 addressable LEDs or matrices they're one

12:48 of my passions so please make sure that

12:50 you're subscribed to the channel and

12:51 you've turned on the all notifications

12:52 for it that way you'll be notified when

12:55 the mesmerizer is released and for

12:56 future LED episodes thanks for joining

12:59 me out here in the shop today in the

13:00 meantime and in between time hope to see

13:02 you next time right here in Dave's

13:04 Garage

