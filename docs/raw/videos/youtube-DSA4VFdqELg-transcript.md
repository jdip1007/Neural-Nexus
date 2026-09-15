---
source_url: https://www.youtube.com/watch?v=DSA4VFdqELg
source_type: video
ingested: 2026-09-15
published: 2026-09-15
duration_minutes: 11
language: en
sha256: 2f1c977f6dd1239e9a0c388c0aebba89a397c13025a722850e6848e969dc026d
time_sensitive: True
---

# YouTube Transcript: Reliable Isn’t Always Better: TCP vs UDP

## Video Information
- **Title**: Reliable Isn’t Always Better: TCP vs UDP
- **Video ID**: DSA4VFdqELg
- **Published**: Unknown
- **Views**: Unknown
- **Language**: en

## Transcript
00:00 [music]

00:03 >> Hey, I'm Dave. Welcome to my shop. Now,

00:05 I've got a great UDP joke, but I'm

00:07 afraid you wouldn't get it, which is

00:09 basically the entire point of UDP.

00:12 If I send 10 packets across a network

00:14 and number them 1 through 10, most

00:16 people assume that the network's job is

00:17 simple, deliver all 10 in order without

00:20 losing any of them.

00:21 And most of the time, that's exactly

00:23 what happens. But sometimes packet five

00:25 just vanishes. Packet six arrives fine,

00:28 and the smartest thing the network can

00:30 do is absolutely nothing about it. No

00:32 retry, no recovery, no heroic attempts

00:35 to make things whole again. Just let

00:37 number five die.

00:39 And today I want to show you why that

00:40 can be exactly the right answer. I've

00:42 set up a simple experiment between two

00:44 computers where I can deliberately

00:45 murder one piece of network traffic in

00:47 transit. We're going to send the same

00:49 number of data twice, first with UDP and

00:52 then with TCP, and watch what happens in

00:54 Wireshark when number five disappears.

00:57 The difference is dramatic enough that

00:58 once you see it, you'll understand far

01:00 more about these two protocols than you

01:02 would from memorizing their header

01:03 fields.

01:04 Let's start with UDP.

01:06 The first four datagrams arrive exactly

01:08 as expected. Somehow number five gets

01:11 thrown into the electronic wood chipper

01:12 in the middle of the network. Then

01:14 number six arrives normally, followed by

01:15 seven through 10. So, the receiving

01:17 program ends up with 1, 2, 3, 4, 6, 7,

01:21 8, 9, and 10. There is no UDP error

01:24 message. UDP does not stop the network,

01:26 interrogate the routers, or send a

01:28 search party.

01:29 That datagram simply never arrives, but

01:31 life continues. Now, do the same

01:33 experiment over TCP. Again, the first

01:36 four pieces of data make it across. And

01:38 again, the next chunk, number five,

01:40 disappears in transit. Later traffic

01:42 still physically reaches the receiving

01:44 computer. But this time something

01:46 strange happens. The application appears

01:48 to stop after number four. Later TCP

01:51 segments can already be inside the

01:52 machine, safely received by the network

01:54 card, and sitting in kernel memory, and

01:56 TCP will still refuse to hand that data

01:59 to the program. That is called

02:01 head-of-line blocking, and it is one of

02:03 the most counterintuitive things in

02:04 networking.

02:05 TCP promises the application an ordered

02:08 stream of bytes. If byte number 50,000

02:11 is missing, TCP cannot simply hand over

02:13 a byte 51,000 and hope that nobody

02:15 notices. Doing so would violate the

02:17 abstraction that it has promised, so it

02:19 waits. Even when all the data beyond the

02:21 hole has already arrived, the

02:23 application is not allowed to see any of

02:25 it until that gap is repaired. And this

02:27 is the moment where the two protocols

02:29 stop being abstract and start having

02:31 real consequences.

02:33 Imagine the missing data is 20

02:34 milliseconds of somebody speaking in a

02:36 live voice call. The packet is detected

02:38 as lost, retransmitted, and finally

02:40 arrives, but by then another 100 or 200

02:43 milliseconds have passed. The data is

02:45 now technically correct and also

02:47 temporally useless.

02:48 We have perfectly reconstructed a tiny

02:50 slice of the past. Human speech can

02:52 tolerate a small missing fragment.

02:54 Codecs in our brains are surprisingly

02:56 good at filling little gaps, but what is

02:58 much harder to hide is latency. Once the

03:00 conversation starts feeling delayed,

03:02 people talk over top of each other, and

03:04 the whole interaction begins to fall

03:05 apart.

03:07 Games make the same principle even more

03:08 obvious. Suppose a multiplayer game is

03:11 sending frequent updates about another

03:12 player's position, 100, then 103, and

03:15 then 107.

03:16 If the update for 103 disappears, but

03:18 107 arrives correctly, there's almost no

03:21 reason to freeze the remote player at

03:23 100 while we dig through the network for

03:25 his former because we already know

03:27 something newer.

03:28 So, in both cases, stale data can be

03:30 worse than missing data.

03:32 And that is why the behavior we just

03:33 watched matters so much. TCP's refusal

03:36 to deliver later data is not a bug. It

03:39 is the direct result of the contract it

03:41 offers the application, every byte in

03:43 order. For some applications, that

03:45 contract is perfect. For others, it is

03:48 the wrong tool.

03:49 And now that you've seen the effect,

03:51 let's take a look at the machinery that

03:52 produces it.

03:54 UDP is almost comically small. Its

03:56 header is only 8 bytes: source port,

03:58 destination port, length, and a

04:00 checksum.

04:01 More importantly, each UDP datagram is

04:04 an independent message. If I send 10 of

04:06 them, the receiver can still tell them

04:08 apart. Message boundaries stay intact.

04:11 What UDP does not contain is just as

04:13 important. No sequence numbers to

04:15 guarantee their order, no

04:16 acknowledgements, no retransmission, no

04:18 reordering, and no built-in flow

04:20 control.

04:22 IP underneath it is a best effort

04:23 network, and UDP largely accepts that

04:25 bargain.

04:27 TCP takes the opposite approach. It is

04:29 not really thinking packets at all. It

04:30 thinks in bytes. Packets are just the

04:32 envelopes that carry portions of a

04:34 continuous byte stream across the

04:35 network.

04:37 When two TCP endpoints connect, they

04:39 exchange initial sequence information in

04:41 the SYN, the SYN-ACK, ACK handshake. And

04:44 from that point forward, every byte in

04:46 the connection lives in a numbered

04:47 space. If a segment begins with a

04:49 sequence number 50,000 and carries 1,000

04:52 bytes, the next segment should begin at

04:53 51,000.

04:55 Sequence number is not packet 17. It

04:58 tells the receiver exactly where these

05:00 bytes belong in the larger stream.

05:02 And acknowledgements work in the same

05:04 way. An ACK of 51,000 means I have

05:07 everything through byte 50,999.

05:10 The next byte I want is 51,000.

05:13 But back to our murder scene. The

05:15 receiver has everything up through byte

05:17 49,999,

05:18 so it's waiting for 50,000. Then a later

05:21 segment beginning at 51,000 arrives

05:23 successfully, as does maybe one at

05:25 52,000 and 53,000, but the receiver

05:27 cannot advance its cumulative

05:29 acknowledgement because there is still a

05:30 hole. It therefore keeps acknowledging

05:33 50,000. Another later segment arrives,

05:35 and again, it says 50,000. In Wireshark,

05:38 you can watch the acknowledgement number

05:40 freeze while later data continues to

05:42 reach the machine. That stuck

05:43 acknowledgement is the visible signature

05:45 of head-of-line blocking. Classic TCP

05:49 used repeated duplicate acknowledgements

05:51 as a strong signal. Three duplicate acts

05:53 for the same position was traditionally

05:55 enough for the sender to conclude that

05:57 the segment was lost rather than merely

05:59 delayed and to retransmit before the

06:01 normal timer expired. And that's called

06:03 fast retransmit. Modern stacks have more

06:06 sophisticated loss detection, but the

06:08 core idea remains. Acknowledgements

06:10 reveal not only what arrived, but where

06:12 progress stopped.

06:14 Selective acknowledgement or sack makes

06:16 the conversation even richer. Without

06:18 sack, the receiver can only keep saying,

06:20 "I'm still waiting for byte 50,000." But

06:22 with sack, it can also say, "And by the

06:24 way, I already have these later blocks,

06:27 so please don't send those again."

06:29 The sender can then repair only the

06:30 hole.

06:31 And if and when the missing segment

06:33 finally arrives, the most satisfying

06:35 moment in the demonstration happens.

06:37 That gap gets filled and the receive

06:38 window becomes contiguous again, and

06:40 everything that was waiting beyond the

06:42 hole is suddenly released to the

06:43 application all at once.

06:45 Data that appeared to have stopped comes

06:47 pouring through.

06:48 And that is head of line blocking made

06:50 physical. The later packets were not

06:52 necessarily late. Some of them had

06:54 already arrived. The delay was by the

06:56 TCP's contract, every byte in order.

07:00 For a zip file or an executable or a

07:01 database transaction or an SSH session,

07:04 that contract is exactly right. I do not

07:07 want 9.9999 gigabytes very quickly and

07:10 then a note saying that one critical

07:11 byte could not be located. Correctness

07:13 outranks punctuality.

07:15 But the moment the data is live audio,

07:18 rapidly changing game state or

07:19 telemetry, the value of waiting changes.

07:22 And that's the deeper point here. UDP

07:24 does not eliminate reliability. It

07:26 simply refuses to impose one universal

07:29 reliability policy on every application.

07:31 It lets the application decide which

07:33 information must arrive correctly and

07:35 which information is allowed to expire.

07:38 There's another practical difference

07:39 that becomes obvious the first time you

07:40 write real network code. UDP preserves

07:43 datagram boundaries. TCP does not

07:46 preserve application message boundaries

07:47 at all. Two UDP sends of hello and world

07:50 arrive as two separate messages, if they

07:52 arrive at all,

07:54 but two TCP sends of the same data may

07:56 arrive as hello world or he and then low

07:58 world and you know, all broken up. TCP

08:01 only promises that the bytes will

08:03 eventually arrive in the correct order.

08:05 Your application has to supply any

08:07 framing.

08:08 TCP also solves two problems that are

08:10 often a mashed together, flow control

08:12 and congestion control.

08:14 Flow control protects the receiver by

08:16 advertising its available buffer space.

08:18 Congestion control protects the network

08:20 by reacting to loss and delay signals

08:23 and by becoming less aggressive. A lost

08:25 segment on a high bandwidth high latency

08:27 path can therefore cost far more than

08:29 simply re-transmitting one segment. It

08:31 can stall ordered delivery, shrink the

08:34 congestion window and force the sender

08:35 to rebuild its rate cautiously

08:37 afterwards.

08:38 And that is why when looking at a slow

08:40 TCP capture, I care far more about

08:43 re-transmissions, duplicate acts, sack

08:45 blocks and periods where the

08:47 acknowledgement number stops advancing

08:49 than I do about every little header

08:50 field.

08:51 And all of this brings us to a modern

08:53 example of engineers deliberately

08:55 choosing the smaller contract, QUIC.

08:58 QUIC is the transport underneath HTTP/3

09:02 and it runs over UDP.

09:04 And at first that sounds almost a little

09:05 perverse because we spent decades making

09:07 TCP mature and reliable and then the

09:10 newest generation of web shows up riding

09:12 on the protocol whose reaction to our

09:14 missing package is to basically shrug.

09:16 And our experiment explains why. HTTP/2

09:20 can carry many logical streams over a

09:21 single TCP connection. That's better

09:24 than opening dozens of separate

09:25 connections, but underneath all those

09:27 streams, there are still one TCP byte

09:29 stream. If a single TCP segment

09:31 disappears, TCP's ordering promise

09:34 applies to the entire connection.

09:36 Later data belonging to completely

09:38 unrelated streams can be trapped behind

09:40 that hole. So, QUIC still provides

09:43 reliability, acknowledgements,

09:44 retransmission, congestion control, and

09:46 encryption.

09:48 But, because it implements its own

09:49 streams above UDP, loss on one stream

09:52 does not automatically freeze data

09:54 belonging to other independent streams.

09:56 QUIC does not make packet loss

09:58 disappear, it changes what must wait for

10:01 what. Same network, same missing data,

10:03 but three different contracts.

10:05 TCP says every byte in order. UDP says

10:08 every datagram that happens to arrive.

10:11 And QUIC says, "I want reliability, but

10:13 I also want to vote on which missing

10:14 data is allowed to stop everything

10:16 else." Once you've watched the missing

10:18 packet experiment, TCP and UDP stop

10:21 looking like two nearly identical

10:22 entries on a certification exam. They

10:24 become answers to a much more

10:26 interesting engineering question. When

10:28 the network loses something, what is the

10:30 value of waiting for it? For a file,

10:32 waiting is cheap and corruption is

10:34 expensive. For live audio, waiting may

10:36 be expensive and a tiny loss may be

10:38 almost free. For games and telemetry,

10:41 the answer can change from one message

10:42 to the next. Reliability is not an

10:45 absolute virtue anymore than speed or

10:47 consistency are absolute virtues.

10:49 Engineering begins when you ask what the

10:51 system is actually trying to preserve.

10:53 If the most important thing is every

10:55 byte, then TCP gives you an

10:56 extraordinarily capable machine for

10:58 turning an unreliable packet network

11:00 into something that looks like a

11:01 reliable stream. If the most important

11:03 thing is right now, sometimes the

11:05 smartest thing the network can do when

11:07 packet five disappears is exactly what

11:08 UDP did at beginning. Let it die. If you

11:11 found today's episode interesting or

11:13 useful, I'd be honored if you'd consider

11:14 leaving a like and a subscribe. In the

11:17 meantime and in between time, I hope to

11:18 see you next time, right here in Dave's

11:20 garage.

11:21 >> Do it, Glen. Do it. Do it.

