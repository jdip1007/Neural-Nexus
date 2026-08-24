---
source_url: https://www.youtube.com/watch?v=SR8ESCmUYLY
source_type: video
ingested: 2026-08-24
published: 2026-08-24
duration_minutes: 18
language: en
sha256: 16c41807bfd6c36f251ddb2b4af7e7226c8d4705edcdbcdb338cfcafe6eb1a35
time_sensitive: True
---

# YouTube Transcript: Hidden Code: How Slot Machines Actually Work - The Computer Inside

## Video Information
- **Title**: Hidden Code: How Slot Machines Actually Work - The Computer Inside
- **Video ID**: SR8ESCmUYLY
- **Published**: Unknown
- **Views**: Unknown
- **Language**: en

## Transcript
00:00 I'm going to ruin slot machines for you.

00:02 And then right at the end, I'm going to

00:04 partially unrune them by showing you how

00:06 to spot the one rare situation where a

00:08 slot machine might actually become a

00:10 better than even money bet. Not because

00:12 of luck and not because it's due, but

00:14 because of math. Today, we're going to

00:16 take apart one of the most misunderstood

00:18 computers on Earth, the modern slot

00:20 machine. Not with a crowbar, because

00:22 that tends to end rather badly, but from

00:24 the inside out, starting with the exact

00:26 instant that you press spin. We'll

00:28 follow that button press into the random

00:29 number generator through the hidden

00:31 virtual reels past the pay table, the

00:33 bonus engine, the progressive meters,

00:35 and the regulatory rules that keep the

00:37 whole thing just barely on the right

00:38 side of legal. And when we're done,

00:40 we'll answer the question that really

00:41 matters. Are these machines fair, or are

00:43 they carefully legalized psychological

00:45 warfare with a bill validator attached?

00:47 The answer, annoyingly, is yes. They are

00:50 fair in a very narrow mathematical

00:52 regulator approved sense. They're also

00:54 engineered from the carpet up to exploit

00:56 every quirk in human reward processing

00:58 that they're illegally allowed to touch.

01:00 They can't decide to simply cheat you.

01:02 They can't secretly punish you for

01:03 winning. They can't manufacture fake

01:05 near misses after the fact. But inside

01:08 those rough boundaries, they can create

01:10 the feeling of progress where none

01:12 actually exists, celebrate losses as

01:14 wins, make random outcomes feel

01:16 personal, and turn almost into one of

01:18 the most profitable words in the casino.

01:20 And that boundary, the line between

01:22 illegal deception and legal persuasion

01:24 is where that whole machine really

01:26 lives. That tension between the legal

01:28 and the ethical is fascinating to me as

01:30 somebody with autism. I was once of the

01:32 opinion that as long as it was entirely

01:34 literally true, it was fair game. And

01:36 that came back to bite me because humans

01:37 are much more complicated animals than

01:39 that. And the first secret is that the

01:41 reels are not the game. On a modern

01:43 sloth, whether you're looking at a

01:45 physical set of stepper reels, a video

01:46 grid full of buffalo, dragons, lightning

01:48 balls, or three suspiciously overfed

01:51 pigs, what you're seeing is just a

01:52 display. It is not the source of the

01:55 chance. It is not slowing down because

01:57 the machine is deciding whether it likes

01:58 you or not. It's not just missing

02:01 because the motor was almost there. The

02:03 decision was already made deep inside

02:05 the machine before the animations even

02:07 started. In gaming regulator language,

02:09 the machine is an electronic gaming

02:11 device and the actual game lives in the

02:12 approved software, the protected

02:14 storage, probability tables, pay tables,

02:16 meters, logs, and a random number

02:18 generator that is treated less like a

02:20 helper routine and more like the sacred

02:22 furnace at the heart of the casino.

02:24 Nevada's current technical standards

02:26 require that the random selection

02:27 process meets a chai squared goodness of

02:30 fit test which prohibits also drawing

02:32 random RNG values for future play

02:34 requiring protection against outside

02:36 interference and for all games approved

02:38 after on I think it is January 1st 2027

02:41 they require a cryptographically secure

02:43 pseudo random number generator and

02:44 recognized randomness test batteries to

02:46 be built in. So here's what happens when

02:48 you actually press spin. Your button

02:50 press generates an input event, probably

02:52 a software interrupt. The game software

02:54 samples the current RNG output, scales

02:57 that number into the game's probability

02:58 model, maps it to real positions or

03:01 symbols or bonus events, evaluates the

03:03 pay table that results, determines the

03:05 exact win or loss, updates the meters,

03:07 and only then does it even begin to show

03:09 you the little drama of spinning the

03:11 reels. The reels are basically a puppet

03:13 show. The math is the puppeteer. That

03:15 means that stopping the reels early does

03:17 not change your odds at all. Pulling the

03:19 handle does not add luck and yelling,

03:20 "Come on, baby." does not increase the

03:22 entropy. Though I admit it may increase

03:24 the entertainment value for nearby

03:25 patrons. Now, software random number

03:28 generators are deterministic in the same

03:30 boring way that almost all software is

03:32 deterministic. Given the same algorithm,

03:34 the same seed, and the same sequence of

03:36 calls, you get the same outputs. If you

03:38 start with the number seven and the next

03:40 number is 38, that's because it's always

03:42 38 when you seed with a seven. The

03:44 sequence is random over time, but it's

03:46 completely deterministic from the turn

03:48 to turn. So, if it generated one result

03:50 per pull, you'd get the same win loss

03:52 sequence every single time. That sounds

03:55 terrifying until you remember that the

03:56 machine is required to not use any

03:58 static seeds and that it must cycle the

04:00 RNG continuously at a minimum average of

04:03 100 times per second and not to queue up

04:06 future plays waiting for you. The key is

04:08 not that a computer can produce magic

04:10 randomness. The key is that the exact

04:12 instant that you press the button mixed

04:14 with the approved seating and continuous

04:15 cycling makes the sampled state

04:17 practically unknowable. Even if you knew

04:20 the algorithm, you would still have to

04:21 know the exact internal state at the

04:23 exact instant that your finger landed.

04:25 Human timing is a meat-based jitter

04:28 generator. And for once, our sloppy

04:29 reaction time is doing real security

04:31 work here. The timing of our button

04:33 press is being used to generate what is

04:35 essentially a truly random value from a

04:37 pseudo random number generator. And that

04:39 is also why the machine can never be

04:41 due. A slot machine does not sit there

04:43 getting embarrassed because it has not

04:44 paid out in a while. It has no

04:46 conscience and absolutely no memory of

04:48 fairness from turn to turn, which is the

04:50 important part, and no little accountant

04:52 inside saying, you know, Dave's been at

04:54 this machine for 40 minutes. Maybe toss

04:55 him a bonus now and then. With ordinary

04:57 independent slot outcomes, the last spin

04:59 does not owe the next spin anything. If

05:02 you walk away and the next person hits

05:03 the jackpot, you did not leave a hot

05:05 machine. They did not benefit from the

05:07 money that you just pumped in

05:08 beforehand. They simply pressed the

05:10 button at a different instant and

05:11 sampled a different result. Now, that's

05:13 emotionally unsatisfying, which is why

05:15 casino floors are full of mythology, but

05:17 it is technically the whole point. And

05:20 the second secret is virtual reels. And

05:22 this is where slots went from mechanical

05:23 gambling machines into mathematical

05:25 entertainment engines. A classic

05:27 mechanical slot, the old ones with three

05:29 reels and 22 stops or symbols on each

05:31 reel only had 22 to the 3r or 10,648

05:36 possible combinations. So that limits

05:38 how rare and therefore how large any

05:40 jackpot can be. A 1984 patent changed

05:44 the industry by decoupling the physical

05:45 reels from the probability reel. The

05:48 machine could now have say 22 physical

05:50 stops visible to the player but 64, 128,

05:53 or 256 virtual stops in the math. So the

05:56 RNG pecks from the virtual reel and in

05:58 the software maps that hidden stop to

06:00 the displayed symbol. The patent known

06:02 as the Telz patent after its inventor

06:04 describes physical reels as displays of

06:06 the RNG selected result rather than the

06:08 game itself, allowing payout odds

06:10 independent of the physical reel

06:12 combinations. That one idea explains a

06:14 huge amount of slot machine weirdness.

06:16 You may look at a reel and see a jackpot

06:18 symbol, a blank, a jackpot symbol, and

06:20 another blank, and your brain says,

06:21 "Well, that symbol's all over the place.

06:23 I should get it more often." But the

06:24 virtual real may map a very few hidden

06:26 stops to the jackpot symbol and a

06:28 mountain of hidden stops to the blanks

06:30 around it. The display is not

06:32 necessarily lying in a legal sense, but

06:34 it's also not a transparent histogram of

06:36 probability. It's more like a subway

06:38 map. Useful, simplified, and absolutely

06:40 not drawn to scale in any way. And this

06:43 is where regulation steps in because a

06:44 casino does not get to do whatever it

06:46 wants. In Nevada, gaming devices must

06:49 theoretically pay back a mathematically

06:51 demonstrable percentage of all amounts

06:53 wagered. and that percentage cannot be

06:54 less than 75% for each wager available

06:57 for play. They must determine outcomes

06:59 by chance, skill, or a disclosed

07:01 combination and display rules and

07:03 outcomes in an accurate, non-misleading

07:06 way. That does not mean that you will

07:08 personally get back $75 from every $100

07:10 you play. It just means that the

07:12 approved math model over the expected

07:14 life of the game and a vast number of

07:16 plays must meet the minimum. In real

07:18 casinos, actual returns are usually much

07:20 higher than the minimum law. But the

07:22 difference between theoretical return

07:24 over millions of spins and what happened

07:26 to my $200 bill on Tuesday is roughly

07:28 the difference between climate and

07:30 weather. Once I was in a casino and a

07:32 slot tech came over to pay a hand pay,

07:33 which at the time was a bit of tax

07:35 paperwork that you had to go through for

07:36 any win over 1,000. Now it's 2,000 or

07:39 so. And while she was working her way

07:41 through the menus, I happened to film

07:42 what she was doing, and it revealed a

07:44 payout table on that machine of 95%.

07:50 The payout percentage is not the same

07:52 thing as volatility, however. Two

07:54 machines can both return 90% in theory

07:56 over a long span, while one gives you

07:58 lots of little hits, and the other keeps

08:00 most of the return locked away behind

08:01 rare bonuses and jackpots. The first one

08:04 kind of feels like a slow leak, whereas

08:06 the second one feels like being ignored

08:07 by a day to occasionally buy you a

08:09 motorcycle. Casinos care about hold

08:12 percentage, which is the share that they

08:13 keep over time. But players care about

08:15 whether the game session felt alive.

08:18 Game designers care about both because

08:19 the best revenue machines are not merely

08:21 the ones with the highest edge. It's the

08:23 one that keeps you going and sitting

08:24 there for a long enough period for the

08:26 edge to quietly do its work. And this is

08:28 why denomination matters. As a general

08:31 rule, penny machines tend to have higher

08:33 casino margins than higher denomination

08:35 machines. While higher denomination

08:37 machines often have better theoretical

08:39 returns, but also larger absolute bets

08:41 and scarier varants. Think of it as

08:43 being something of a bulk discount. So

08:46 yes, one practical way to improve your

08:47 odds is to avoid the lowest denomination

08:50 most feature-heavy machines and play

08:51 games with better published or

08:52 historically observed returns when you

08:54 can find them. But that's not a winning

08:56 system. That's just choosing a slightly

08:58 less hungry furnace. Recent Nevada

09:00 reporting has continued to show penny

09:02 slots is especially lucrative for

09:03 casinos and consumer slot payback guides

09:06 have long described the same broad

09:07 denomination pattern. Now, let's talk

09:09 about the most famous psychological

09:11 trick in slots. The near miss. You land

09:13 two jackpot symbols and the third one

09:15 sits just above the payline, looking

09:17 like fate just stumbled on the carpet a

09:18 bit. The really important regulatory

09:21 distinction is that the machine cannot

09:22 decide that you lost and then swap in a

09:24 more exciting losing display after the

09:26 fact. GLI11, one of the major technical

09:29 standards used across gaming

09:30 jurisdictions, says that after selection

09:33 of the game outcome, the game must not

09:34 display a near miss by making a second

09:36 variable decision that affects what is

09:38 shown to the player. If the RNG picked a

09:41 losing outcome, the game cannot

09:43 substitute a different, more emotionally

09:44 abusive losing outcome just because it

09:46 wants to make you keep playing. That

09:48 rule has some history behind it. In the

09:50 late 1980s, Nevada regulators confronted

09:52 machines that used a secondary process

09:54 to create misleading near- miss

09:56 displays, and roughly 10% of Nevada slot

09:59 machines were reportedly retrofitted

10:00 after authorities concluded players were

10:02 being misled by a near- miss feature.

10:04 The modern rule is very clear. The

10:07 machine may not look at a boring loss

10:08 and then dress it up as a heartbreak.

10:10 Ah, but here's the twist. A machine can

10:12 still produce lots of near misses if

10:14 those near misses are baked into the

10:15 approval probability structure from the

10:17 start. If the virtual reel has lots of

10:20 slots mapped to blanks immediately above

10:22 or below a jackpot symbol, the RNG is

10:24 still fairly selecting from the approved

10:26 real map. No secondary decision is

10:29 needed. The near miss arrives naturally

10:31 just from the math in the same way that

10:32 a loaded looking but legally approved

10:34 dice game can still produce frustrating

10:36 almost. Now that's not so much a

10:38 loophole as it is the central philosophy

10:40 of regulated slot design. The math must

10:43 be approved, fixed, auditable, and

10:44 honestly executed. But the presentation

10:47 can be engineered to be maximally

10:48 compelling within those rules. And near

10:50 misses are powerful. Research on

10:52 gambling near misses has found that they

10:54 can increase motivation to continue

10:55 gambling and recruit reward related

10:57 brain circuitry even though they deliver

10:59 no monetary reinforcement. That's the

11:02 psychological magic trick. Your rational

11:04 brain says, "Well, it's a loss." While

11:06 the older machinery in the basement

11:07 says, "Almost. Do it again." A slot

11:10 machine cannot legally lie about the

11:12 result, but it can absolutely arrange

11:14 the result space so that losing often

11:15 feels like progress. The same thing

11:18 happens with losses disguised as wins.

11:20 On a multi-line video slot, you might

11:22 bet $3 to win back 40. Mathematically,

11:25 you just lost $2.60, but the machine may

11:28 still flash, ding, animate, and throw a

11:30 little parade because one of your lines

11:31 technically paid. Researchers call these

11:34 outcomes LDWs or losses described as

11:36 wins. And studies have found that they

11:38 can cause players to overestimate how

11:40 often they are winning. It's not false

11:42 accounting. Your credit meter is

11:43 accurate. But emotionally, the machine

11:45 has turned a net loss into a tiny

11:47 celebration, which is a bit like your

11:49 bank charging you an overdraft fee and

11:50 then letting out the balloons. Modern

11:53 slots add another layer with perceived

11:54 persistence. These are the games where

11:56 pots fill with coins, fireworks stack

11:59 up, pigs get fatter, or some glowing

12:01 meter creeps towards what looks like

12:02 your destiny. The player's brain sees

12:04 accumulation and assumes the probability

12:06 is improving. Sometimes it is, but often

12:09 it is not. In perceived persistence, the

12:12 display creates the feeling of progress.

12:13 While each spin can remain

12:15 mathematically independent, even though

12:17 you see all these coins up here in a

12:18 bowl, the actual display has no idea

12:20 what's going on with that. The bonus

12:22 might trigger when the pig is skinny or

12:24 not trigger for ages when the pig looks

12:26 like it swallowed a sectional sofa. Now,

12:28 industry discussions distinguish

12:29 perceived persistence from true

12:31 persistence, where a game state really

12:32 does accumulate toward a reward. True

12:35 persistence is where things get

12:36 genuinely interesting for advantage

12:38 players. A must hit by progressive, for

12:40 example, has a jackpot that must be

12:42 awarded before a displayed ceiling. The

12:45 hidden trigger point is selected after

12:46 the previous jackpot resets, and as

12:48 wages push the meter upward, the

12:50 expected value can improve. Near the

12:52 top, under very specific conditions, the

12:54 machine can become a positive

12:55 expectation. That does not mean that the

12:58 average vacation player has discovered

12:59 free money. It means professionals may

13:02 stock banks of machines looking for rare

13:04 states where the published rules and the

13:05 current meter create a temporary edge.

13:08 The casino knows this and the

13:10 manufacturer knows this and the

13:11 regulators allow it because the game is

13:12 operating exactly as approved. The

13:15 vulture at the machine is not hacking

13:16 the slot. He's reading the math off the

13:18 surface better than everybody else. Now,

13:20 bonus games deserve their own myth

13:22 busting. When you pick one of those five

13:24 boxes, is your answer even real? Well,

13:26 the answer depends on the approved game

13:28 design. Sometimes the prize is

13:30 determined by your selection from a

13:31 randomized field. Sometimes the outcome

13:33 was predetermined and the picking

13:35 sequence is just entertainment. But the

13:37 rules and the display have to be

13:38 consistent with the approved design.

13:40 Nevada's current technical standards

13:42 even say that for certain predetermined

13:43 player selection features where the

13:45 prize is the same regardless of what the

13:47 player selects, the game may not display

13:49 other prize values at the conclusion of

13:51 the feature as though those were genuine

13:53 missed opportunities. That's a

13:55 surprisingly important little rule

13:56 because it stops the machine from

13:57 inventing a fake universe where you

13:59 could have picked the huge prize when

14:01 mathematically you never could have.

14:03 Casinos also cannot simply tighten the

14:04 machine because you sat down with a

14:06 players card or because someone in

14:07 surveillance thinks your shirt looks

14:09 lucky. Payts and configurations can be

14:11 changed over time through approved

14:13 logged secure processes and modern

14:16 systems can be worked but the machine

14:17 cannot adapt its theoretical return

14:19 based on prior payouts or your personal

14:21 session. GLI1 explicitly prohibits

14:24 modifying or discarding RNG selected

14:26 outcomes due to adaptive behavior and

14:28 says events of chance must be

14:30 independent except as provided by the

14:32 rules. The machine is not allowed to say

14:34 that this guy's up 400 bucks, so

14:36 activate revenge mode. If it feels like

14:37 that just happened, welcome to variance,

14:39 the casino's best unpaid employee. So,

14:42 are slots honest? And in the engineering

14:44 sense, a regulated slot machine is one

14:46 of the most scrutinized computers most

14:47 people will ever touch. Its control

14:49 programs are verified. Critical memory

14:51 is checked. The RNG is tested. The

14:53 meters are recorded. Air states tilt the

14:56 machine. Doors and logic areas are

14:58 locked. Communications are protected.

15:00 Regulators, independent labs,

15:02 manufacturers, and casino accounting

15:03 systems all have a stake in making sure

15:05 the box does exactly what its approved

15:07 math says it does. The machine is not

15:10 supposed to cheat because cheating would

15:11 endanger the license that lets the

15:12 entire building print money legally. But

15:15 in the human sense, the machine is

15:16 absolutely not neutral. It is a

15:18 carefully tuned experience that uses

15:19 intermittent reinforcement, sound,

15:21 animation, near miss structure, small

15:23 frequent returns, bonus anticipation,

15:26 perceived progress, and volatility to

15:28 keep you engaged. It does not need to

15:30 predict you. It does not need to rig the

15:32 next spin. It does not need a secret

15:34 camera reading your soul. The legal math

15:36 already favors the house. The psychology

15:38 merely keeps you feeding samples into

15:40 the math system for a longer period. And

15:42 that's the real secret life of slot

15:44 machines. They are not crooked in the

15:45 back alley sense. They are something

15:47 more interesting and frankly more

15:48 impressive. They are regulated

15:50 probability engines wrapped in theater.

15:52 The law constrains the random number

15:54 generator, the payback floor, the

15:56 display rules, the accounting meters,

15:58 the security, and the independence of

15:59 the events. Then designers walk right up

16:01 to that fence and build the brightest,

16:03 loudest, most emotionally persuasive

16:05 carnival that they can without crossing

16:07 the line. So the next time you see a

16:08 machine flash so close or celebrate a

16:10 40cent return on a $3 bet or show you a

16:13 pot of gold that looks like it's ready

16:14 to burst, you should know what you're

16:15 really looking at. Not luck warming up,

16:18 not a machine that's due, not a secret

16:20 schedule. You're actually watching fixed

16:22 approved mathematics wearing a sequin

16:23 jacket doing close-up magic with your

16:25 dopamine system. Now, there's one

16:27 exception to the there are no winning

16:29 systems rule that's worth understanding

16:31 because it's not really so much a system

16:32 so much as the math peeking out from

16:34 behind the curtain. Some machines have

16:36 what's called a poolled progressive

16:38 jackpot where a little slice of every

16:40 eligible wager goes into a shared prize.

16:42 So you might see a game like Meltdown

16:44 where the big bonus starts at $25,000,

16:46 but because nobody has hit it for a very

16:48 long time, it's sitting there now at 100

16:50 grand, growing like a radioactive

16:52 fishing lure. At that point, the

16:54 question is obvious. Has the jackpot

16:56 grown so large that the machine is now

16:58 actually a good bet? And the answer is

17:00 maybe. But unless you know the hidden

17:02 probability of hitting that progressive,

17:04 you can't prove it from your side of the

17:05 glass. The way to think about it is that

17:07 every extra dollar above the reset value

17:10 adds expected value to each eligible

17:12 spin, but only in proportion to the

17:14 chance of actually winning it. If the

17:16 jackpot is $75,000 above reset, then

17:18 your chance of hitting it is one in

17:20 100,000. That extra meter value is still

17:22 meaningful. But if the chance is 1 in 10

17:24 million, it's mostly casino wallpaper.

17:26 At some sufficiently gigantic jackpot, a

17:29 progressive can actually become positive

17:30 expectation, meaning that over a large

17:32 number of plays, the math would favor

17:34 the player. But that does not mean that

17:36 you are more likely than not to win. You

17:38 may still lose almost every single spin.

17:41 It just means the rare hit has become

17:42 large enough to compensate for all the

17:44 losing spins in between. Few of us would

17:46 be wise to ride that train to its

17:48 ultimate destination. If you have

17:50 comments or questions about today's

17:51 episode, please leave them in the

17:53 comments section below cuz I do try to

17:54 read them all. And then every Friday on

17:56 Shop Talk on the Dave's Attic channel,

17:58 we answer and discuss all the best user

18:00 insights and questions. Check it out.

18:01 I'll throw a link up here. So give it a

18:03 subscription if you happen to enjoy an

18:05 episode. If you found today's episode to

18:07 be interesting or entertaining, remember

18:08 that I'm mostly in this for the subs and

18:10 likes. So I'd be honored if you would

18:11 consider leaving me one of each before

18:12 you go today. And in the meantime, and

18:14 in between time, I will see you next

18:16 time right here in Dave's Garage.

18:18 >> Do it. Do it. Do it.

