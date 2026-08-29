---
source_url: https://www.youtube.com/watch?v=ePwo3P1iZO4
source_type: video
ingested: 2026-08-29
published: 2026-08-29
duration_minutes: 15
language: en
sha256: 66dc0a64fd5fea66e7d5eecc5e916b514bbb8bfd84d1c5ad0942733ea1ccd87d
time_sensitive: True
---

# YouTube Transcript: The "Do Anything" Chip: FPGA

## Video Information
- **Title**: The "Do Anything" Chip: FPGA
- **Video ID**: ePwo3P1iZO4
- **Published**: Unknown
- **Views**: Unknown
- **Language**: en

## Transcript
00:00 [Music]

00:01 foreign

00:02 [Music]

00:07 welcome to my shop today in Dave's

00:10 Garage we're going to take an

00:11 introductory look at the chips that can

00:12 be made to do almost anything the fpgas

00:15 or field programmable gate arrays

00:17 they're logic chips that can be

00:19 programmed to do almost anything that

00:20 you can conceive of and rather than

00:22 having to build a physical chip or a

00:24 circuit board you simply design the

00:26 circuit and software and then upload it

00:27 to the fpga

00:29 and fpga is a bit like Lego for Hardware

00:31 when you want to build a chip to do some

00:34 tasks you can gather up the circuitry

00:35 needed and virtually assemble it like a

00:37 Lego project and rather than your design

00:39 being burned into the Silicon like a

00:41 prom the fpga gets programmed to do

00:44 whatever it is that you want to do and

00:45 then it can be reprogrammed any number

00:47 of times

00:48 it's easy to say build or design a chip

00:50 but what does that actually mean well at

00:53 a high level an fpga is made up of a

00:55 large number of configurable logic

00:57 blocks or clbs that can be programmed to

00:59 perform various functions each clb

01:02 contains a number of logic gates such as

01:04 and or or not Gates and as well as

01:06 flip-flops and other basic logic

01:08 building blocks the Lego pieces if you

01:10 will and combining these logic gates and

01:12 other building blocks in different ways

01:14 allows you to create complex digital

01:16 circuits so let's spend a minute talking

01:18 about those Gates because that's about

01:19 all you really have to understand to

01:21 make sense of the rest of this

01:23 basic logic gates are the fundamental

01:25 building blocks of digital circuits

01:27 there are electronic circuits that

01:28 perform a logical operation on one or

01:31 more binary inputs to produce a single

01:33 binary output which can be either one or

01:35 zero

01:36 there are several types of basic logic

01:37 gates each with its own specific logic

01:39 function let's take a look at them the

01:42 or gate imagine you have two smoke

01:44 detectors and you want an alarm to sound

01:46 when either one is tripped and they

01:48 should keep alarming if both are tripped

01:50 of course in that case you'd want an or

01:52 gate an or gate takes two or more signal

01:55 inputs and produces an output signal if

01:56 either of the input signals is high or

01:58 both if all the inputs are low then the

02:01 output is also low

02:03 and gate an and gate takes two or more

02:06 signals and produces an output signal

02:08 only if all the input signals are high

02:10 otherwise the output is low

02:12 not gate a not gate also known commonly

02:16 as an inverter has a single input and

02:18 produces the opposite value at its

02:20 output that is if the input is high the

02:22 output is low and if the input is low

02:23 the output is high just the opposite

02:25 nand gate a nand gate is a combination

02:28 of an and gate and a not gate it

02:31 produces the opposite output of an and

02:33 gate meaning that the output is low only

02:35 when the input signals are high and it's

02:37 high for any other input combination nor

02:39 gate a nor gate is a combination of an

02:42 or gate and a not gate it produces the

02:44 opposite output of an or gate meaning

02:46 that the output is high only when all

02:47 input signals are low and low for any

02:50 other input combination

02:51 now in addition to the basic logic gates

02:54 I mentioned earlier there are also a

02:55 couple of other types of logic gates

02:56 that can perform more complex logical

02:58 operations here's just a few quick

03:00 examples the xor gate an xor gate also

03:04 known as an exclusive or gate takes two

03:06 input signals and produces a high output

03:08 if the two input signals are different

03:10 if the two inputs are the same then the

03:12 output is low you can think of it as any

03:14 one input but not both or neither

03:17 xnor gate an ex nor gate also known as

03:20 an exclusive nor gate is a complement of

03:22 an xor gate it produces a high output if

03:25 the two input signals are the same and a

03:27 low output if the inputs are different

03:28 so if the two inputs match the result is

03:31 true

03:32 buffer a buffer is a logic gate that has

03:35 a single input and a single output the

03:37 output of the buffer is the same as its

03:39 input with no logical operation

03:40 performed buffers are often used to

03:42 amplify or transmit signals without

03:44 changing their logical State

03:46 multiplexer a multiplexer or mux for

03:49 short is a logic gate that has multiple

03:51 inputs but just a single output it

03:53 selects one of the inputs to pass

03:55 through to the output based on a set of

03:56 control signals d multiplexer a d

03:59 multiplexer or demux for short is the

04:02 opposite of a multiplexer it has a

04:04 single input but multiple outputs and it

04:06 selects one of the outputs to receive

04:07 the input signal based on the set of

04:09 control signals the gates can have more

04:11 than just two inputs and they do still

04:13 roughly what you'd expect so a four

04:15 input or gauge turns on when any

04:17 combination of its inputs is turned on

04:18 except for all off in an and gate with

04:21 four inputs will only turn on when all

04:23 four inputs are on

04:25 these logic gates can also be combined

04:27 to create more complex logical functions

04:29 for example the combination of an and a

04:31 not gate can be used to create the NAD

04:33 gate and the combination of a nor gate

04:35 and a knot gate can be used to create an

04:37 and gate

04:38 by combining these basic logic gates in

04:40 various ways you can create digital

04:42 circuits that Implement a wide range of

04:44 complex functions such as arithmetic

04:45 operations memory storage and decision

04:47 making fpga is also typically include a

04:50 number of input output i o blocks that

04:52 allow you to connect the fpga to

04:54 external devices such as sensors

04:55 displays and other digital circuits the

04:58 i o blocks can be configured to support

05:00 a variety of different interfaces such

05:02 as serial parallel or even ethernet one

05:04 of the main benefits of using an fpga is

05:07 that it allows you to implement custom

05:08 digital circuits that are tailored to

05:10 your specific needs without the need to

05:12 design and actually fabricate a custom

05:13 chip this can be useful in a variety of

05:16 applications such as prototyping new

05:18 Hardware Designs implementing custom

05:19 Digital Signal processing algorithms or

05:21 building high performance Computing

05:23 systems

05:24 your alternative would be to design an

05:26 entire chip in Silicon known as an Asic

05:28 for application specific integrated

05:30 circuit as an example think of a chip

05:32 like the video chip in a Commodore 64.

05:34 you're going to produce millions of them

05:36 so in the long run it's cheaper to

05:38 produce an Asic because while an fpga

05:39 could be programmed to do the job at

05:41 least today they are a lot more costly

05:43 that's why you see fpgas follow the

05:46 money if you're building just one of a

05:48 comparative handful of MRI machines for

05:50 example and you want the ability to

05:52 field upgrade the logic later then on

05:54 fpga likely makes more sense

05:56 it's the same deal with the space and

05:58 defense Industries wherever money meets

06:00 the need for a quick iteration or

06:01 turnaround you're likely to find fpgas

06:04 in use

06:05 however fpgas can be more complex to

06:07 work with than other types of

06:08 programmable logic devices such as

06:10 microcontrollers or Digital Signal

06:12 processors

06:13 it's because they require specialized

06:14 tools and knowledge of digital logic

06:16 design to use effectively

06:18 additionally fpgas are typically more

06:21 expensive than other types of

06:22 programmable logic devices which makes

06:23 them less accessible for hobbyists or

06:25 DIY projects

06:27 so what about microcontrollers why would

06:30 you choose an fpga instead of a

06:32 microcontroller well fpga's and

06:34 microcontrollers are both types of

06:35 programmable devices but they have

06:37 different strengths and weaknesses and

06:38 are suited for different types of

06:40 applications

06:41 microcontrollers are typically optimized

06:43 for executing a set of predefined

06:45 instructions or firmware that controls

06:47 the behavior of the device they

06:49 typically have a small amount of on-chip

06:50 memory and peripherals such as perhaps

06:52 timers interrupts and communication

06:54 interfaces which makes them well suited

06:56 for a wide range of embedded systems

06:58 applications such as controlling Motors

07:00 collecting sensor data or interfacing

07:02 with external devices

07:04 fpgas on the other hand are designed to

07:07 be highly configurable and customizable

07:08 allowing you to create custom digital

07:10 circuits that are tailored to your

07:12 specific needs they're typically used in

07:15 applications that require high

07:16 performance Computing or Digital Signal

07:18 processing such as image or audio

07:19 processing cryptography or network

07:21 processing fpgas can also be used to

07:24 implement custom Hardware accelerators

07:26 for specific tasks such as crypto

07:28 machine learning or artificial

07:29 intelligence algorithms

07:31 one of the key advantages of fpga's over

07:34 microcontrollers is their flexibility

07:36 fpgas can be reprogrammed or

07:38 reconfigured multiple times allowing you

07:40 to quickly iterate and modify your

07:42 digital circuit designs without having

07:43 to create new physical circuits or

07:45 boards so if your satellite isn't doing

07:47 what you want you can reprogram it in

07:49 place both on the bench before and on

07:52 the Fly after launch this can be a major

07:54 advantage in applications where rapid

07:56 prototyping or development is important

07:58 another advantage of fpgas is their high

08:01 performance because fpgas can be

08:03 customized to implement specific digital

08:05 circuit functionality they can often

08:07 outperform general purpose

08:08 microcontrollers or dsps for certain

08:10 tasks they are also highly parallel

08:13 which means they can perform multiple

08:14 operations simultaneously making them

08:17 well suited for applications require

08:18 high-speed processing of large amounts

08:21 of data consider the case where the CPU

08:23 wants to check if any of eight gpio

08:25 lines are triggered it might have to

08:27 issue a separate interrupt and I O

08:29 instruction plus a comparison eight

08:31 times to get the answer whereas an fpga

08:33 can do it in a single clock cycle with a

08:35 large or gate it seems that for most any

08:38 task that you can express in an fpga it

08:40 will likely be the faster solution

08:43 overall the choice between an fpga and a

08:45 microcontroller depends on the specific

08:47 requirements of your application if you

08:49 need a general purpose device that can

08:50 execute predefined instructions a

08:52 microcontroller will be the best choice

08:54 but if you need a highly configurable

08:56 device that can be customized to

08:57 implement specific digital circuit

08:59 functionality the fpga is likely the

09:01 better option

09:03 now to use an fpga you need to program

09:05 it with a configuration file that

09:06 specifies the desired circuit design

09:08 functionality this configuration file is

09:11 typically loaded onto the fpega each

09:13 time the device is powered on or reset

09:15 they start up blank

09:17 fpgas have what is called a

09:19 configuration memory that stores the

09:21 configuration file this memory is

09:23 typically implemented using a type of

09:25 non-volatile memory called flash memory

09:27 now in volatile memory retains its

09:29 contents even when powered off making it

09:31 the ideal choice for storing the fpga

09:33 configuration file

09:34 it can be self-contained within the fpga

09:36 or more commonly live as an external

09:38 chip on the board when the fpga is

09:41 powered on or reset it reads the

09:43 configuration file from the flash memory

09:44 and uses the configure the digital

09:46 circuit functionality and then once the

09:48 fpga is configured it behaves as if it

09:50 were just a physical digital circuit

09:52 implementing the desired functionality

09:54 the role of a flash memory is critical

09:56 in the fpga configuration process

09:58 without a valid configuration file in

10:01 flash memory the fpga will not be able

10:02 to operate correctly because it would

10:04 remain effectively blank Additionally

10:07 the flash memory must be fast enough to

10:09 enable the fpga to read the

10:10 configuration file quickly and

10:11 efficiently so it boots promptly

10:14 because the fpga configuration file is

10:16 stored in non-volatile memory it can be

10:18 programmed or reprogrammed multiple

10:20 times without the need for a physical

10:21 circuit board or chip in fact in most

10:25 designs the fpga is programmed from

10:27 scratch using the configuration file

10:28 stored in the flash memory every time

10:30 the chip boots so to completely modify

10:32 the fpga you're really just rewriting

10:34 the configuration in the flash storage

10:36 and then rebooting this allows you to

10:38 quickly iterate and modify your digital

10:39 circuit designs without having to create

10:41 new physical circuits or boards

10:44 to program an fpga you typically use a

10:46 hardware description language such as

10:48 verilog or vhdl to describe the desired

10:51 logic functionality your Hardware

10:53 description language is then compiled

10:55 into a configuration file that can be

10:57 loaded onto the fpga

10:59 once the configuration file is loaded

11:01 onto the fpga the device will behave as

11:03 if it were an actual physical chip that

11:04 you had custom designed to do whatever

11:06 it is you plan to do

11:08 however as noted there are some

11:09 challenges associated with using fpgas

11:12 as I mentioned earlier programming fpgas

11:14 requires specialized knowledge and tools

11:17 additionally fpgas can be more power

11:19 hungry than other types of programmable

11:21 logic devices which can be a concern for

11:23 certain applications particularly those

11:25 powered by batteries or where Heats may

11:27 be a concern

11:28 so fpgas are a powerful digital circuit

11:31 design tool especially in applications

11:33 where performance and flexibility are

11:35 critical

11:35 while they can be more complex and

11:37 expensive to work with than other types

11:39 of programmable logic devices they offer

11:41 a level of customization and performance

11:43 that can be difficult to achieve with

11:44 other Technologies fpgas are used in a

11:47 wide range of applications across

11:49 Industries including Aerospace

11:50 telecommunications medical devices and

11:53 Industrial control systems in Aerospace

11:56 fpgas are often used for real-time data

11:58 processing and control in systems such

12:00 as avionics and satellite Communications

12:03 in telecommunications fpgas are used for

12:06 implementing high-speed network

12:07 interfaces and digital signal processing

12:09 algorithms in medical devices fpgas can

12:12 be used for implementing real-time

12:14 monitoring and control systems and an

12:16 industrial control systems fpgas are

12:19 used for implementing complex control

12:20 algorithms and interfacing with sensors

12:22 and other devices

12:24 now there are several types of different

12:26 fpgas available on the market each with

12:28 its own strengths and weaknesses some

12:30 fpgas are optimized for high performance

12:32 Computing tasks While others are

12:34 designed for more low power applications

12:35 some fpgas include specialized Hardware

12:38 blocks such as Digital Signal processors

12:41 or high-speed transceivers to enable

12:43 specific functionality

12:45 in recent years there has been growing

12:47 interest in using fpgas for machine

12:48 learning and artificial intelligence

12:50 applications because fpgas can be

12:52 customized to implement specific

12:54 algorithms they can be used to

12:55 accelerate certain types of machine

12:57 learning tasks such as neural network

12:58 inference

13:00 in addition to traditional fpga devices

13:02 there are also hybrid devices that

13:04 combine fpga functionality with other

13:06 types of processing elements such as

13:08 microprocessors or Graphics processing

13:10 units or gpus

13:12 these hybrid devices offer the

13:13 flexibility of fpgas along with the

13:16 performance of other processing elements

13:17 making them well suited for a range of

13:19 high performance Computing applications

13:22 one of the main Trends in the fpga

13:23 industry is the move towards cloud-based

13:26 fpga development and deployment this

13:28 allows designers to work with their

13:30 fpgas on a virtual basis without needing

13:32 to purchase or manage physical devices

13:35 cloud-based fpga Services can also

13:37 provide access to specialized hardware

13:39 and software tools that may not be

13:41 available to designers working with the

13:42 traditional fpga devices

13:44 another Trend in the fpega industry is

13:47 the development of Open Source fpga

13:49 tools and platforms these initiatives

13:51 aim to make fpga technology more

13:53 accessible to a wider range of designers

13:55 and developers by providing free open

13:58 source tools for fpga development and

14:00 deployment

14:01 now as with any technology there are

14:03 also potential drawbacks to using fpgas

14:06 in addition to the complexity and the

14:08 cost associated with programming fpgas

14:10 there may be concerns around security

14:12 and reliability

14:13 because fpgas can be reprogrammed

14:15 there's always a risk of malicious

14:17 actors using them to perform

14:18 unauthorized operations or accessing

14:21 sensitive data additionally because

14:23 fpgas are highly configurable there is a

14:25 risk of unintentional errors or bugs

14:27 creeping into the design that could lead

14:29 to system failures or other issues

14:31 despite these challenges fpgas remain an

14:34 important tool for digital circuit

14:35 design and are likely to continue to

14:37 play a key role in circuit design for a

14:39 long time to come

14:40 if you're interested in tinkering with

14:42 an fpga to learn more about it there are

14:44 several starter kits that resemble an

14:46 Arduino or a Raspberry Pi they come with

14:49 all of the support logic flash RAM and

14:50 Communications built in so you can start

14:52 learning and building immediately I'll

14:54 put a link to a few examples in the

14:56 video description

14:57 thanks for joining me out here in the

14:58 shop today now remember I'm mostly in

15:00 this for the subs and likes so if you

15:02 enjoy this episode please be sure to

15:03 leave me one of each before you go today

15:06 and if you or someone you know may be on

15:07 the autism spectrum check out the free

15:09 sample of my book on Amazon secrets of

15:11 the autistic millionaire it's got

15:13 nothing to do with money and everything

15:14 to do with living a successful Life

15:16 along the Spectrum it's everything I

15:18 know now that I wish I'd known back then

15:19 check the link in the video description

15:22 in the meantime and in between time hope

15:24 to see you next time right here in

15:26 Dave's Garage

