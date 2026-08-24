---
source_url: https://www.youtube.com/watch?v=DM4rZZBqXVM
source_type: video
ingested: 2026-08-24
published: 2026-08-24
duration_minutes: 15
language: en
sha256: 204b12e4d22dc7793360d632ec0abe8319395987f0011c4336305e010d725e06
time_sensitive: True
---

# YouTube Transcript: Bare Metal Programming - Booting From the Switches

## Video Information
- **Title**: Bare Metal Programming - Booting From the Switches
- **Video ID**: DM4rZZBqXVM
- **Published**: Unknown
- **Views**: Unknown
- **Language**: en

## Transcript
00:00 greetings professor falcon

00:03 shall we play a game

00:05 [Music]

00:13 hey i'm dave welcome to my shop if

00:15 you've ever looked at old computers like

00:16 the altair the mci or even the venerable

00:19 old pdp-11 you've no doubt seen their

00:21 impressive front panels with dozens of

00:23 switches and cool blinking lights but

00:25 what do they all do and how do you use

00:27 them how did they use the front panel to

00:29 actually bootstrap and run a classic

00:31 computer back in the day we'll follow

00:33 along as today we're going to program

00:35 the computer from war games the mzai

00:36 8080 completely from scratch using only

00:39 the front panel switches and leds and

00:41 i'll show you exactly how it's done

00:43 we'll cover all the important steps

00:45 along the way without any hand waving

00:47 i'm going to write a small demo program

00:49 in assembly language and then compile it

00:50 to hex and then convert it to binary and

00:52 then enter it into the front panel and

00:54 finally execute the code to watch the

00:57 leds display the amazing for 1975

01:00 results in about 15 minutes you'll know

01:02 exactly what the front panel is for and

01:05 how to enter the code and data needed to

01:06 bootstrap almost any old computer system

01:09 the front panels of a few classic

01:10 computers are at least to me some of the

01:13 most beautiful and fascinating displays

01:14 out there oh sure a machine like the

01:16 altair might be fairly basic and looks

01:18 to have been made of the types of

01:20 switches and components that you could

01:21 ostensibly pick up at a radio shack back

01:23 in the day

01:24 because the goal for the altar was in

01:26 part to reduce costs since it was

01:28 targeted towards individuals and

01:29 enthusiasts rather than large companies

01:32 and universities but other systems had

01:34 more time budget and style i think a few

01:36 are downright beautiful and we'll take a

01:38 look at a few of the best

01:39 now you have to keep in mind that back

01:41 in those days going back to the mid 70s

01:43 and before computers typically did not

01:45 ship with a rom operating system of any

01:47 kind there was no built in basic no

01:49 command shell no interpreter to fall

01:51 back on when you turned it on it didn't

01:54 drop into any kind of input prompt it

01:55 just sat there empty doing absolutely

01:57 nothing

01:58 even if you wanted to load your program

02:00 from a roll of paper tape you'd at least

02:02 need a short program to do the actual

02:04 reading of that paper tape and the only

02:06 way you could enter that program would

02:08 be using the front panel switches you

02:09 had to start somewhere and all that you

02:11 had to start with was memory in the

02:12 processor the switches were your only

02:14 gateway

02:16 each front panel might have a few lights

02:17 and switches specific to that model of

02:19 course but almost all shared a few basic

02:21 elements that we're going to be

02:22 concerned with today

02:24 at a minimum we need the ability to

02:25 inspect the location in memory and some

02:27 way to store our own byte at any

02:29 particular address of that memory and

02:31 then finally some way to say go to start

02:33 the computer executing that basic

02:35 functionality usually provided in the

02:36 form of a set of switches for the

02:38 address that you wish to inspect or

02:40 modify

02:41 the switches correspond to the binary

02:43 bits of the memory address once you've

02:45 entered the address in question in

02:47 binary of course you can press a button

02:49 to fetch the current value stored at

02:50 that location and display it on the leds

02:53 that show the contents of the data bus

02:55 the value is displayed there in binary

02:57 again using the led display

03:00 if you wish to store a new value at that

03:02 address you set the data switches to the

03:03 value in question that you want and then

03:05 press the switch labeled commit or store

03:07 or write or something similar whatever

03:10 data value you've entered via the

03:11 switches would then be stored at the

03:13 address you had previously specified

03:14 through the address switches

03:17 some of the front panels on the less

03:18 expensive machines like the altair and

03:20 the mci are overloaded which is to say

03:22 that there are 16 switches and they're

03:24 all used for setting the address and

03:25 then some of them are reused as just the

03:27 data switches

03:29 once you set the address and press

03:30 examine it puts that address on the bus

03:32 after which you use the lower eighth

03:34 switches to set the data value you plan

03:36 to store there

03:37 one that i've always been fascinated

03:39 with is the pdp-11 produced at about the

03:41 same time as the altair but as part of a

03:43 long line of pdps that came long before

03:46 it from digital it clearly inspired what

03:48 would be found on the personal computers

03:49 of the day because the address space is

03:52 larger it contains switches for 22 bits

03:54 of address space and for 16 bit words by

03:57 comparison the pdp 8 which is of course

03:59 a fair bit older features only 12 bits

04:01 of address space on the front panel 12

04:04 bits doesn't sound like a lot and since

04:05 it can only address 4096 different

04:08 locations it really isn't but it helps

04:10 to know that the registers and memory

04:11 slots on the pdp's were 12 bits instead

04:13 of 8 so it's not quite as limited as it

04:16 seems at first glance

04:18 the pdp 10 shown here features 18 bits

04:20 of address space and very odd bytes

04:22 featuring 36 bits instead of just eight

04:25 but what you're really looking at here

04:26 is not the computer itself but the

04:28 computer that was used to start the

04:30 computer you see a pdp 10 was a full on

04:32 mainframe and to boot it you could even

04:34 use a smaller pdp11 minicomputer to do

04:36 the job so the front panel that you're

04:38 actually interacting with here is a pdp

04:40 1140 front end and so that panel looks

04:43 about the same as that of a pdp 11.

04:45 before we can key anything into the

04:47 front panel however we need a program to

04:49 actually key in and it better be short

04:51 because i don't feel like toggling in a

04:52 few kilobytes by hand maybe like a

04:54 couple dozen bytes at most but what can

04:56 we actually accomplish in a program that

04:58 short since we're really doing this as a

05:00 proof of concept i decided a little

05:02 program to scroll the led data display

05:03 like knight rider ought to be sufficient

05:05 and so that's what we're gonna do

05:07 but i still need to write the code and

05:09 once i have that code i have to use an

05:10 8080 assembler to turn that code into

05:12 actual program bytes and then i need to

05:15 turn those program bytes into raw binary

05:17 that i can enter via the front panel

05:19 then i'll enter the program and fire it

05:20 off and we'll watch it do its work

05:22 to get started let's head over to the

05:24 desktop and drop into the editor while

05:25 i'll write the little app to scroll the

05:27 leds

05:28 so the first thing we need is going to

05:30 be an assembly language program that

05:31 will do the countdown of the leds for us

05:34 and i'm going to make you just

05:36 put up with me pasting it in here

05:38 instead of me typing it live for the

05:40 effect because hey you got stuff to do

05:42 too

05:42 but let's take a look at how this code

05:44 actually works

05:45 org0 means we're going to start the code

05:47 at address zero zero zero zero next

05:50 we're gonna move 1 into a

05:53 now we're going to rotate a right

05:55 through the carry and what that does is

05:58 it moves everything in a down by one bit

06:00 and it puts whatever was in bit 0 into

06:02 the carry flag so it has the effect of

06:04 setting the carry next we're going to

06:06 move a to b 254 now this is actually the

06:10 inverse bit mask of what you see on the

06:11 display because the bits are backwards

06:13 from which we expect one is off zero is

06:15 lit and so in order to get a single bit

06:18 lit we need to have all but one bits set

06:21 in this mask so this is just the inverse

06:23 or the xor of one

06:25 now out ff takes the byte in the

06:27 accumulator which right now would be fe

06:29 and it's going to send it out to the

06:31 display of the leds on the front panel

06:34 every time you see an out ff that's what

06:36 that's doing now this is doing a load x

06:38 sine extended of d and e with a value

06:41 one now when i say d and e that's

06:43 because there's two registers two eight

06:44 bit registers d and e that you can treat

06:46 as a pair of registers d e as a 16 bit

06:49 register and there are certain

06:50 instructions like lxi which is load

06:52 extended immediate that will treat them

06:54 as a 16-bit register pair this will load

06:57 the value 1 into the register and of

06:58 course that's just going to set the

07:00 lowest bit and everything else will be

07:01 set to zeros in both of the registers

07:04 same here h and l which are high and low

07:06 are being set to zero all the way

07:08 through

07:09 next we're doing a double precision add

07:12 which is the registers in d e plus the

07:14 register values in hl put back into hl

07:17 each time we come through here it's

07:18 going to add 1 to the hl pair

07:21 if it doesn't overflow if it doesn't

07:23 carry then we're going to go back to

07:25 delay and we're going to do the add

07:26 again so we're just going to loop in

07:27 this little tight loop here adding one

07:29 until the carry overflows meaning that

07:31 we've reached ffff and passed it by one

07:34 now this rlc is actually what shifts the

07:36 bit pattern on the display it started

07:39 out as fe now we're going to shift it

07:41 left one

07:42 it shifts through itself so whatever is

07:45 in bit 7 goes back to bit 0. to make any

07:48 use of assembly language however we

07:50 actually have to assemble the code and

07:52 that is convert it into the raw bytes

07:54 that the computer is going to expect

07:56 now of course it's not going to want

07:57 bytes it's going to want bits but we'll

07:59 get there the next step for now we're

08:01 going to get to the bytes

08:02 and i simply paste my code into an

08:04 online 8080 assembler with a pretty

08:06 printer and look it pops out all nicely

08:08 formatted i'm going to grab this with

08:10 the bytes and all so i can paste it into

08:12 my document here

08:19 now you can see this is my original code

08:21 my original comments and now we have the

08:23 hexadecimal bytes for move immediate a

08:26 which is going to be 3e and the value 0

08:28 1

08:29 rotate accumulator right is 0f

08:32 here we have 3e again because it's move

08:34 immediate a but this time the value is

08:36 fe

08:37 out is d3 and the port is ff

08:40 load extended immediate and it's going

08:42 to actually specify the full 16 bits

08:44 that are being passed into the two

08:45 register pair

08:48 21 hex is going to be the instruction

08:49 for loading into the hl pair 16 bit

08:51 immediate and here are the 16 bit values

08:54 now it's always going to be low high

08:56 so in this case it was 0 1

08:59 is the first byte

09:02 0 0 is the high byte so it looks like 0

09:05 1 0 0 looks like 100 when you're looking

09:07 at it just sequentially but you have to

09:09 read it backwards because in intel

09:11 assembly the values go from least

09:13 significant bit to most significant byte

09:16 19 is our hex code for dad

09:19 of the de bridge

09:20 repair you're always going to use hl as

09:23 the other register pair by the way so it

09:25 just has to specify the d pair here

09:28 and so on jnc delay

09:31 7 is your rotate left and then we have

09:33 c3 2 0

09:35 zero zero we're gonna go back to this

09:37 instruction which is our loop label

09:39 don't worry if that doesn't make a great

09:41 deal of sense what you need to know is

09:43 that for these instructions there are

09:44 numeric values that the compiler or

09:47 assembler actually is going to assign to

09:48 those but our front panel doesn't have a

09:51 hex input it has a binary input so what

09:53 to do i'm going to grab this column of

09:56 hex digits

09:59 i'm going to go to a web page

10:01 that has a handy converter where i can

10:02 paste in hex digits

10:04 i'll say pad the leading zeros and i'll

10:06 say i want a binary conversion

10:08 here we go

10:11 this is 345tool.com by the way

10:19 there are my binary digits

10:23 i should probably number them just so i

10:24 know what i'm doing later

10:26 let me do that

10:28 [Music]

10:30 now there and to confirm that we have

10:32 the right number of binary bits you can

10:35 see i started 12 13 14 and here i go 12

10:38 13 14 ending with a zero

10:41 so these become the actual bits for the

10:44 instructions for my program that i'm

10:45 going to need to enter into the front

10:47 panel

10:48 so we started with a little algorithm

10:49 here written in this lengthy language we

10:51 converted that to hexadecimal and then

10:54 we converted the hex decimal to binary

10:57 now that we have a binary sequence that

10:59 we can enter into the front panel it's

11:00 time to learn how to use those switches

11:02 and leds and remember there are three

11:04 important operations that we'll be

11:05 performing first we'll use the 16

11:08 switches to set the address that we care

11:10 about into the address bus

11:11 our program will start at address 0 in

11:13 our case when we press examine that

11:16 address is placed onto the address bus

11:18 and the current value of that location

11:20 will be shown on the display

11:22 for each of the program bytes we will

11:23 set the lower 8 switches to the value

11:25 that we want to store at that location

11:27 and then press deposit to put that byte

11:29 into memory there one nuance to be

11:31 prepared for is that when we press

11:32 deposit next it advances the address bus

11:35 by one byte before storing the value

11:37 that means we only enter the base

11:39 address which is zero at one time after

11:42 that we'll just be hitting deposit next

11:44 setting the switches to the value of the

11:45 next byte we want to store and repeating

11:47 until we've entered all of the bytes

11:49 that'll make more sense once you've seen

11:51 it in person so let's head on over to

11:53 the inside

11:55 now to access or get to any address on

11:57 the msi we simply enter that address in

12:00 binary and press examine

12:03 the current value of the address bus is

12:05 not the switches but rather whatever the

12:08 address bus lights say but when i set a

12:11 value like address three and then press

12:13 examine you'll see the address bus jumps

12:15 to three and this is the value that's

12:17 currently stored at three

12:19 now let's enter something

12:21 let's go to address zero and we're gonna

12:23 put 0 by leaving all of these down

12:26 so now we're examining the contents of

12:28 address 0. when i press deposit it's

12:30 going to take

12:31 these 8 bits and deposit them in the

12:33 current memory location so when i do

12:34 that these bits should clear

12:37 and they do

12:39 and if i set the bottom four bits on

12:41 and i pressed deposit you'll see the

12:43 bottom four bits are now on

12:46 so to enter my program all i'm going to

12:48 have to do is set the toggles starting

12:50 at address zero press deposit and then

12:53 for each subsequent one deposit next

12:55 because that pre-increments the counter

12:57 of what address you're pointing at

12:59 and it will store each of the bytes that

13:01 i give it in memory

13:03 let's start with the first byte

13:06 zero zero

13:11 i'm going to say deposit i'd address

13:13 zero

13:14 next i'm going to move on to the next

13:16 byte but before i do anything else i'm

13:18 going to key in that byte which is all

13:20 zeros but a one and i'll say deposit

13:23 next

13:24 then move on

13:27 [Music]

13:59 and that should be all 20 bites

14:00 deposited now if i set my address bits

14:04 back to zeros as they are and i press

14:06 examine i should see

14:08 the bit pattern here i'm going to step

14:09 through them really quickly to check my

14:11 work

14:12 [Music]

14:19 looks right to me so far

14:21 so going back to address zero i'll press

14:22 examine and if i hit run my program

14:25 should execute

14:28 you can see the led pattern stepping

14:29 across the programmed output which is

14:31 the value we set when we do an out ff

14:34 and so it's displaying the contents of

14:36 the accumulator rotating it left and

14:38 then pausing it for a little bit so we

14:39 actually get a delay and can see the

14:41 step visually

14:42 i hope you enjoyed our tour of those

14:44 mysterious front panels and i'd like to

14:46 thank you for taking the time to join me

14:47 out here in the shop today i really

14:49 enjoy making these more narrowly focused

14:51 videos on older tech so if you enjoyed

14:53 it please consider leaving a like and

14:54 subscribing to the channel both help a

14:56 great deal with the algorithm especially

14:58 when i see it in response to these types

14:59 of episodes

15:01 now if you have any interested matters

15:02 related to autism asperger's or asd

15:05 please check out my book on amazon

15:06 secrets of the autistic millionaire it's

15:08 got nothing to do with money and

15:10 everything to do with living a

15:11 successful life on the spectrum it's

15:13 everything i know now that i wish i'd

15:14 known back then remember i'm mostly in

15:16 this for the subs and likes so please be

15:18 sure to leave me one of each before you

15:19 go today in the meantime in between time

15:21 i hope to see you next time right here

15:23 in dave's garage

