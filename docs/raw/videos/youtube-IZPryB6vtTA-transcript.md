---
title: YouTube Transcript: Session 3: Energy Efficiency Co-Flows
created: 2026-10-20
updated: 2026-10-20
type: source
domain: ai
classification: general.media
tags: [youtube, transcript, IZPryB6vtTA]
sources: []
published: 2026-10-20
time_sensitive: True
---
source_url: https://www.youtube.com/watch?v=IZPryB6vtTA
source_type: video
ingested: 2026-10-20
duration_minutes: 150
language: en
sha256: 6dc81e927b1989ed7fffda29f33fac15f523eb82d724507cf2a73662600025de
---

# YouTube Transcript: Session 3: Energy Efficiency Co-Flows

## Video Information
- **Title**: Session 3: Energy Efficiency Co-Flows
- **Video ID**: IZPryB6vtTA
- **Published**: Unknown
- **Views**: Unknown
- **Language**: en

## Transcript
00:00 [SQUEAKING]

00:01 [RUSTLING]

00:03 [CLICKING]

00:05 

00:10 HAZHIR RAHMANDAD:
OK, so for today,

00:15 we can actually do a
quick recap on SEIRb.

00:19 So as we discussed, I think we
covered pretty much everything.

00:24 There were a couple of items
that when I decided, OK, maybe I

00:28 should build a solution-ish
model to share with you,

00:34 I noted that we didn't
discuss it as closely,

00:37 so I wanted to bring up
those couple of items.

00:40 And then we can switch
to our main work.

00:44 So last week, Alexander
asked the question about,

00:50 how do we handle the waning
of immunity due to natural

00:54 versus vaccine-based immunity?

00:58 And the challenge is
that if you have somebody

01:01 who had gotten vaccinated and
then later they got the disease,

01:07 they have both natural immunity
and vaccine-driven immunity.

01:11 And you need to decide
how do you route them.

01:14 Do you send them back
to the group that

01:17 is susceptible but
vaccinated-- that is,

01:21 keep their vaccine immunity,
but wane their natural immunity?

01:27 Or send them to the group that
is susceptible and completely

01:33 unprotected-- that is wane
both of them at the same time?

01:37 Or even send them to
the group of recovered

01:41 but without vaccine
immunity-- that

01:44 is wane the vaccine immunity,
but not the natural immunity?

01:48 And then later, the natural
immunity waning happens.

01:51 And we didn't really discuss it.

01:53 And I gave a quick answer
that wasn't quite going

01:57 through the details of it.

01:59 So I wanted to highlight how
to deal with that situation,

02:02 because it's a fairly
common situation, actually,

02:05 when you have these multiple
stages and different movements

02:10 across different
multiple stages-- that

02:11 is, for example, you can both
go right and down, if you are

02:17 thinking of the two dimensions.

02:19 So here is the model
I put together.

02:25 And here, we are really
talking about what

02:28 is happening on
the right-hand side

02:32 from people who are
vaccinated and recovered.

02:39 And then what happens
to them, basically?

02:41 So one possibility for them is
to wane their natural immunity

02:47 and go into the vaccinated
susceptible population.

02:52 Another possibility for them is
to wane their vaccine immunity

02:58 and go up into
recovered population

03:03 without vaccine protection.

03:05 And we also discussed
a possibility

03:09 of these people waning
both types of immunity

03:12 and going to unvaccinated
susceptible population.

03:16 And the critical idea
here to keep in mind

03:20 is that we usually don't want
to have two different state

03:24 transitions happening
at the same time.

03:27 So the long jump from recovered
vaccinated all the way

03:33 to susceptible and unvaccinated
has these double jumps.

03:38 That is, you're capturing two
different state transitions

03:41 at the same time.

03:42 And it is hard to do that
internally consistently.

03:46 So as a good heuristic, avoid
doing that, and do one jump.

03:52 And then when you do one
jump, it is very easy.

03:55 Basically, both
jumps can happen with

03:57 their own independent rates.

04:00 Now, there are some
underlying assumptions when

04:02 you make that type of movement.

04:06 That is, you're saying
the two types of immunity

04:09 are independent of each other.

04:11 One can wane with its
own rate and the other

04:14 can wane with its own rate, and
the two don't impact each other.

04:19 That is an assumption.

04:21 Now, if you want to
relax that assumption,

04:22 you really have to model
how they are interdependent.

04:26 That is, when you
get vaccine immunity

04:31 and then you get
the disease, you

04:34 go into a different type
of a state that changes

04:37 your rate of immunity loss.

04:42 So that becomes a little
bit more complex but doable.

04:46 Here, we are keeping
the simple assumption

04:48 that the two sources of immunity
are independent of each other.

04:52 And then it becomes the simple
formulation that we have here.

04:56 It's actually very
straightforward, very

04:58 parallel with what is happening
in the rest of the method.

05:01 That is, you have
the vaccine waning,

05:04 which is with the vaccine
efficacy duration.

05:08 So this is the same
time constant with which

05:11 we are waning the immunity
of Vaccinated S going back

05:15 into Unvaccinated S. So the
same time constant works

05:21 for both of them.

05:22 And similarly, we have the
waning of natural immunity,

05:30 so vaccinated waning
of natural immunity,

05:33 that happens with the natural
immunity period, which

05:37 is the same parameter
used to wane

05:39 the immunity for the
recovered population.

05:43 Natural immunity period
is also operating here.

05:46 So this keeps things fairly
simple, fairly clean.

05:51 And the things are
internally consistent.

05:57 And you can actually
now do the calculations,

06:02 for example, how long a typical
person entering the Vaccinated R

06:08 state will remain
in this state, which

06:13 is the harmonic average
of the two time constants.

06:22 You can calculate what's the
probability that they go up

06:28 versus they go down.

06:29 You can do all of the kind of
equilibrium-type of analysis

06:34 you may be interested in
once you lay this out.

06:39 So that's number one.

06:40 And in fact,
theoretically, you could

06:44 have the waning of
vaccine immunity

06:50 during the period you are
vaccinated and infected.

06:52 You could actually go up into
unvaccinated and infected stock

06:59 because your
immunity from vaccine

07:01 is waning during
that short period.

07:03 In fact, that is probably a
little bit more correct in terms

07:07 of the machinery of the model.

07:09 But because this is
a very short period

07:11 and you could kind of
assume that during the time

07:15 you are getting sick,
actually, waning of immunity

07:19 stops because your immune
system is responding

07:21 very heavily and so
on, I think it is also

07:24 OK not to include that flow
variable in this model.

07:28 So that's kind of a
choice that we are making.

07:32 It's not something
we are missing.

07:33 So that's number one.

07:35 Any questions on
that conversation

07:37 on this part of the model?

07:40 

07:45 So then one more
very minor thing,

07:49 but something that is
important for accounting.

07:52 We talked about the current
fraction of population

07:58 that is willing to vaccinate.

08:00 We said that's an important
concept we need for calculating

08:07 the vaccination rate.

08:10 So the way we formulated
vaccination rate up here

08:13 is that we said, we need to have
the unvaccinated fraction that

08:19 is willing to vaccinate.

08:22 That unvaccinated fraction
that is willing to vaccinate

08:25 comes from the
current fraction that

08:27 is willing to vaccinate
of the total population

08:30 versus vaccinated fraction.

08:32 And vaccinated fraction is all
of the vaccinated people divided

08:36 by all of the people and current
fraction willing to vaccinate.

08:40 Normally, you may think
of it as a fixed number.

08:43 It's just a fraction
of population

08:45 that is willing to vaccinate.

08:47 But if you think
about these dynamics,

08:50 if you had a disease where
vaccine was very protective

08:53 and the disease was
very deadly, people

08:57 who are unwilling
to vaccinate are

08:59 likely to get the
disease very frequently

09:02 and die at a much higher rate.

09:06 In which case, the
fraction of people

09:08 who are willing to vaccinate
is dynamically changing.

09:11 That is, over time that
fraction is increasing.

09:14 So you need to capture
that dynamic explicitly.

09:18 So that's another wrinkle that
we didn't really talk about.

09:22 But for an internally
consistent clean model,

09:25 we need to capture that.

09:27 Now to capture that, you need to
accumulate the vaccinated dead.

09:31 You need to basically
see how many

09:33 people who aren't
unvaccinated that are dead

09:38 and then calculate what
fraction of the population

09:41 remains that is willing
to get vaccinated.

09:50 And total population is
accounting for those deaths.

09:53 So the unvaccinated
that is dead is removed

09:57 from the total population.

09:59 So those two, I think, are
kind of two small pieces

10:04 from last week that we
didn't close the loop on.

10:07 We also didn't discuss
the equilibrium conditions

10:10 explicitly.

10:12 And the equilibrium conditions,
I think a couple of you--

10:15 so I think you submitted
one and Jason submitted one,

10:19 so that was nice.

10:20 I think those who submitted
it for the situation

10:24 that we had the waning
of natural immunity

10:29 but not vaccination and
no behavioral response.

10:32 So without those, it is a
fairly straightforward setup.

10:37 You can solve it
for the case where

10:39 we do have behavioral
response, as well,

10:41 depending on the formulation
you use for behavioral response.

10:45 So in the paper that I
shared through email,

10:49 there is a section
that actually I

10:50 go through solving of
that equilibrium condition

10:54 with behavioral response.

10:56 So take a look at that.

10:57 That might be kind of helpful
for thinking through the case

11:05 with behavioral response, which
is the more realistic one.

11:09 And then the vaccination
and waning of vaccination,

11:13 it is a linear model, so
I think it is solvable,

11:16 but it becomes a
messier problem.

11:18 So it's something
you can actually

11:21 try defining the problem
cleanly for ChatGPT

11:25 and see if it can solve the
equilibrium condition for you.

11:31 You should be able to at least
define the problem very clearly

11:35 for it to work.

11:36 So that was kind of the couple
of items I had on the SEIRb.

11:43 Any questions on SEIRb before
we move to our coflows of energy

11:50 efficiency?

11:53 OK, so the main
part of work today

11:58 is to look at the models
for energy coflows.

12:01 And so basically,
the coflow structure

12:05 is probably something
that most of you had seen.

12:09 But some of you, it might
have been new for you.

12:11 So that would be
a little bit more

12:13 of the work to just learn
the basics of the coflows.

12:16 And then we were
asking for something

12:19 that was a little bit more
than just plain vanilla coflow.

12:22 A coflow structure for tracking
energy efficiency requires

12:27 capturing vintage effects,
capturing retrofits-- that is,

12:31 changing of the energy
efficiency that has limits--

12:36 and new technology that may be
introduced and change the limits

12:44 to efficiency gains
so it can make

12:47 it more feasible to introduce
effective, meaningful retrofits.

12:54 And ultimately, we are
looking for formulations

12:57 that are robust for
capturing the overall energy

13:01 consumption given various
types of interventions

13:05 in terms of investing
in retrofits,

13:07 investing in efficiency energy
technology introduction,

13:12 and changes in the
rates of building

13:14 coming into the pipeline.

13:16 So that was the
problem definition.

13:18 So let's now go and see
the submissions we have.

13:23 So a good piece of feedback
that you guys provided

13:27 last time was maybe
focusing on one aspect

13:32 and going through
multiple models

13:35 is easier cognitively
rather than going

13:37 through multiple
models very quickly

13:40 and discuss different
aspects on all those models.

13:43 So let's try that idea today.

13:46 So I'll open multiple models
that have been submitted.

13:50 We can do a quick
look at each aspect

13:55 or how people are capturing
those and see how it goes.

14:00 So we'll learn as we go, in
terms of how effective it is.

14:06 

14:11 So I'm opening the
available models.

14:17 So we have the vintage flows.

14:24 So these are the buildings, Ali?

14:26 AUDIENCE: Yes.

14:26 HAZHIR RAHMANDAD: OK.

14:27 So the vintage is the buildings.

14:31 And then you have buildings
under construction.

14:33 That's OK but not really
central to our problem.

14:37 We could just skip that.

14:39 So we have new
buildings coming in.

14:41 And these buildings
have average lifetime.

14:46 And then the
vintages, probably you

14:48 are dividing it to
different stages.

14:55 

15:00 And you have three stages.

15:03 But how is it--

15:05 AUDIENCE: I think you
have to move it back.

15:08 HAZHIR RAHMANDAD: So why is that
this last removal time is not

15:11 dependent?

15:12 Oh, is it dependent on
the average lifetime?

15:14 OK.

15:16 So it's just a 1/3 of that.

15:19 AUDIENCE: Yeah, the right group.

15:20 HAZHIR RAHMANDAD: OK.

15:21 So that's just the stock
and flow of buildings.

15:23 Fairly straightforward.

15:25 Average residence time
in each, I assume,

15:28 is 1/3 third of the total
or something like that, yes.

15:33 So for each of
these flows, it is

15:36 that stock divided by the
average lifetime divided

15:40 by 3, assuming we
have three vintages.

15:42 And that's fine.

15:44 Then, you have this
retrofitted on the top,

15:48 which I don't know what it is.

15:49 So let me see what
you have below here.

15:56 And then you have energy
consumption of vintage.

15:59 

16:03 So what is the energy
consumption of vintage?

16:05 So what's the definition
of that variable for you?

16:07 AUDIENCE: So we could have gone
with two conceptualizations--

16:11 either considering the
efficiency of each building

16:14 and then multiply
it by something

16:16 that gives us the energy
consumption or the other way

16:18 around.

16:18 So we can assume a baseline
energy consumption.

16:24 And the technology
on the bottom is

16:25 going to reduce energy
consumption in that case.

16:28 HAZHIR RAHMANDAD: OK,
so this is basically

16:30 energy consumption of all
of the buildings together.

16:34 So this is kilowatt
hours per year.

16:36 AUDIENCE: Exactly.

16:37 HAZHIR RAHMANDAD: OK.

16:40 And it is basically
initialized to be

16:45 the vintage multiplied by the
initial energy consumption.

16:50 So all of that is good.

16:51 

16:55 Now, how does retrofitting
work in this setup?

17:02 AUDIENCE: Retrofitting?

17:03 Well, I made a very
simplistic assumption,

17:05 just it happens to
the oldest buildings.

17:08 HAZHIR RAHMANDAD: Ah, so
that's an important assumption

17:10 you're making, that retrofits
happen to the last vintage

17:14 not to other ones.

17:16 So let's track what is
happening with your last vintage

17:19 in this case.

17:20 So in the last vintage,
you have retrofitted

17:24 buildings versus not
retrofitted buildings.

17:29 So you are basically
separating buildings

17:40 by whether they are
retrofitted or not.

17:43 So that's one way to do it, but
it's probably not the easiest

17:49 way.

17:49 There is probably an
easier way to do it.

17:54 And what you're doing here
is that you are taking away

17:59 the energy consumption
of the vintage

18:04 based on retrofitting rate.

18:10 So as you retrofit, you're
taking away how much?

18:17 AUDIENCE: All of the averages.

18:19 HAZHIR RAHMANDAD: All of
the average consumption

18:23 that those retrofitted
buildings have.

18:29 AUDIENCE: This is
our thought process.

18:34 HAZHIR RAHMANDAD: Yes?

18:35 AUDIENCE: If there is
natural demolition rate,

18:38 so it's like a regular
coflow that you see.

18:41 HAZHIR RAHMANDAD: Yes.

18:41 AUDIENCE: But then
we were thinking

18:43 that if you are retrofitting
some of these buildings,

18:46 so a fraction of them will get
retrofitted, so in addition

18:51 to the natural outflow of
the energy consumption,

18:54 something additionally should
be subtracted from the energy

18:59 consumption to account for the
decline of the stock of energy

19:04 consumption for the buildings.

19:07 HAZHIR RAHMANDAD: Yes.

19:08 So this is important when
we are doing coflows.

19:11 The first thing is that
for the main flow, which

19:14 is in this case, buildings,
every stock that you have,

19:17 you usually need to have
equivalent stock for the coflow.

19:24 Otherwise it becomes very
hard to keep track of things.

19:27 It is very easy
to make mistakes.

19:29 Not impossible to do it right,
but I don't recommend it

19:32 at the beginning.

19:33 So in this case, we have a
violation of that heuristic.

19:36 That is, we have the vintage
tree versus retrofitted tree.

19:39 These are different
groups of buildings.

19:42 But the coflow here, this
energy consumption of vintage

19:47 is basically capturing
the energy consumption

19:50 for both of these groups.

19:52 AUDIENCE: There's
another stock offering

19:54 if you go further
on in this model.

19:56 HAZHIR RAHMANDAD: Ah, OK.

19:58 Sorry.

19:59 So this is because I
didn't look closely.

20:04 Thank you.

20:04 So this energy consumption
of retrofitting tree

20:06 is exactly what you
are trying to do.

20:10 Now, it's much easier to keep
it here within the same stock

20:17 and flow chain.

20:18 And then when you are reducing
energy consumption from a group,

20:25 you are doing the
retrofitting on it.

20:28 So I think the confusion
for you or the challenge

20:31 here is that at one time,
you're taking them out,

20:36 you are removing all of the
retrofitted, all of the energy

20:40 consumption that goes
with them, and then

20:43 you go up there and create
this other stock that is having

20:49 the retrofitted value for--

20:51 AUDIENCE: New
energy consumption.

20:53 HAZHIR RAHMANDAD: New
energy consumption, yes.

20:55 So this actually should work.

20:57 That is, it shouldn't be wrong.

21:00 It probably does
what you want to do.

21:03 Basically, you're
taking this group,

21:06 the action of retrofitting
reduces their energy consumption

21:10 per building.

21:12 So it does what you want to do.

21:15 

21:19 It is not the simplest kind
of formulation for this case.

21:25 We'll see how
others have done it.

21:28 But let's see if the basic logic
here is working for other parts.

21:32 So once you are in this
stock, then when you leave,

21:36 you are taking out the
retrofitted average, which

21:40 is what you should be doing.

21:42 So that's good.

21:42 

21:47 And the average time--

21:49 AUDIENCE: That is also a
very simplistic assumption.

21:53 So maybe I should have
used another average.

21:55 HAZHIR RAHMANDAD:
So then there is

21:56 the question of retrofitting
rate, where it is coming from.

21:59 And you are using the investment
process to drive that decision.

22:08 And as long as you are
using the investment

22:13 process, an independent
process to retrofit things,

22:17 to move items between Vintage 3
and Retrofitted 3, you are OK.

22:23 You don't need to worry
about the demolition

22:26 rate or the average
lifetime thing,

22:28 assuming that the
lifetime doesn't

22:30 change because of retrofitting.

22:33 And you can actually change
that assumption as well.

22:36 That would be OK as well.

22:37 But with that assumption, I
think this would work fine.

22:42 Now, let me take a look at
the equations you have here.

22:44 So removal rate for Vintage 3 is
Vintage 3 divided by this total.

22:52 And then this--

22:56 AUDIENCE: I took the idea
from, like this here, we

22:59 had death and recovery.

23:00 HAZHIR RAHMANDAD: Yes.

23:01 So in a way, you're
saying at the end

23:04 of their life of
the buildings, you

23:10 may be doing one
of the two things.

23:12 Either you demolish
it or you retrofit it.

23:15 That's what you are modeling,
the way you're modeling.

23:17 Is that what you wanted to do?

23:19 OK.

23:20 So again, that's an assumption.

23:22 If you make that assumption,
that's how the world works,

23:25 that's OK.

23:26 We need to be clear
about that assumption.

23:28 So here you're calculating
total removal rate.

23:32 A fraction of it
gets demolished.

23:34 1 minus that fraction goes
retrofitted or vice versa.

23:37 And that retrofit rate,
then these buildings

23:43 have a new life,
which is how long they

23:48 will stay in this third
stage or in fourth stage.

23:54 Now, it is really a fourth
stage, not a third stage.

23:57 And you're assuming
that residence time

23:59 is the same as the last
stage demolition rate.

24:03 So these are the assumptions
that go into Ali's model.

24:07 That is, the retrofit is kind
of giving it a new life or 1/3

24:12 of a new life with a new level
of consumption of energy that

24:18 comes from whatever that
initial retrofit technology is.

24:25 So with those
assumptions, this model

24:27 is doing it correctly, at
least for this third stage.

24:30 Now, for the previous
stages, you haven't added it.

24:33 And that adds a few
complexities because then you

24:37 are creating different lives
for retrofitted versus not

24:41 retrofitted buildings.

24:43 And those different lives, you
have to track them separately,

24:45 so it creates kind
of a stock and flow

24:47 change for those
other stages that may

24:50 feel a little bit intimidating.

24:53 Now there is the New
Building Energy Consumption.

24:58 

25:02 AUDIENCE: So the idea was,
whatever the new technology is,

25:09 we're going to take an average
with the potential maximum we

25:15 can get.

25:15 It's like a weighted average
so that we can account

25:19 for the maximum efficiency
that these buildings can get,

25:26 because these are old buildings,
so they cannot achieve

25:29 the efficiency of
the new buildings.

25:33 HAZHIR RAHMANDAD: So
what you need to do here

25:36 is to be tracking how
much improvement you

25:42 can do for each vintage.

25:45 And that improvement that
you can do for each vintage

25:47 is a characteristic of
that vintage itself.

25:52 So it requires a
coflow that tracks

25:56 that characteristic over time.

26:00 So this one doesn't
seem to be doing that.

26:05 Is that correct?

26:06 AUDIENCE: Exactly.

26:07 It just assumes whatever the
best technologies out there,

26:11 just a fraction of those.

26:12 HAZHIR RAHMANDAD: Yes.

26:13 So it makes some
fractional assumption.

26:17 AUDIENCE: And that
fraction is actually

26:19 coming from the
average consumption,

26:21 like before being retrofitted.

26:24 So because the average
consumption of the old building

26:27 is already low, it kind
of adjusts for that.

26:30 HAZHIR RAHMANDAD: Yes.

26:31 So you are getting the
average consumption

26:35 from the old building
energy efficiency.

26:41 AUDIENCE: That sort of
was the characteristics

26:44 of that group of buildings.

26:46 HAZHIR RAHMANDAD:
Yeah, that's how it

26:47 is working as a characteristic.

26:49 And because you are separating
retrofitted versus old buildings

26:54 that have not been retrofitted
here, it kind of works.

26:57 That is, that characteristic
is telling where it currently

27:00 stands.

27:01 You are putting, now, the bottom
in a time-moving parameter.

27:07 And then just say a fraction of
that is what you can achieve.

27:13 So I think it can work.

27:16 I haven't looked through this
specific formulation closely

27:19 enough to see what is happening.

27:21 OK, good.

27:24 This is doing something
that is reasonable.

27:29 Nothing is obviously wrong.

27:31 Now, this part I haven't thought
through the extreme conditions

27:36 for the formulation you have.

27:37 This is a little bit complex,
but it's probably a good time

27:41 to switch to some
of the other models,

27:42 see how they are laid out.

27:45 But here, let me just
understand what is this.

27:48 This is the New Building
Energy Consumption.

27:51 So this is capturing the
change in technology.

27:55 And this is
exogenous, basically.

28:00 AUDIENCE: We're assuming
that the baseline technology

28:02 consumption is 1 and
whatever innovation

28:04 that we have is trying
to reduce that maximum 1,

28:08 that maximum value.

28:10 

28:13 HAZHIR RAHMANDAD: OK.

28:14 So the technology can
be exogenous here.

28:17 By and large, that's not
a problematic assumption.

28:21 

28:24 So I'm OK with that.

28:26 Although, a better
formulation would

28:30 allow the limits of technology
to depend on the vintage

28:35 as well.

28:37 But this formulation
wouldn't capture that.

28:40 

28:45 Yeah, so for me, the
better formulation

28:47 would be a coflow that captures
the potential for improvements

28:53 for each vintage.

28:54 And then you can change
that potential endogenously.

29:00 OK, let's look at
some other models.

29:03 

29:07 Next one is Jake's.

29:11 

29:14 AUDIENCE: First time working
with coflows or subscripts,

29:16 so I learned a lot.

29:17 HAZHIR RAHMANDAD: OK, good.

29:20 That was a challenge.

29:23 So you have your
three vintages--

29:28 new buildings, mature
buildings, old buildings.

29:31 You have the three
time constants

29:33 for them, some construction
rate, which is exogenous.

29:37 That's good.

29:38 Then, we have the energy
usage of new buildings,

29:42 energy usage of
mature buildings,

29:44 energy usage of old buildings.

29:45 So these are the coflows
similar to Ali's formulation.

29:50 You're calculating the
averages, pushing things forward

29:53 based on the averages.

29:54 That's also fine.

29:56 

30:00 AUDIENCE: So for
those two flows,

30:02 I had an assumption
that for energy usage,

30:04 there would be some,
as you age, that there

30:07 would be some
inefficiency that's

30:09 added in to energy
consumption kind of is

30:11 how I thought about it.

30:12 HAZHIR RAHMANDAD: Yeah.

30:14 So that's basically kind
of wear and tear reduces

30:17 energy efficiency idea.

30:20 So that's an
interesting mechanism.

30:22 Even though we
didn't ask for it,

30:24 it's nice that you captured it.

30:25 I think it's a meaningful idea.

30:30 Perhaps you could include
it for the new buildings

30:32 as well, because
new buildings are

30:34 subject to the same
type of dynamics.

30:38 Let's look at the
equation for that.

30:40 So you're saying the mature
buildings are increasing

30:46 their energy consumption
with a rate that

30:53 is coming from new buildings
aging and mature building energy

31:00 flows per unit.

31:01 So in a way, if I'm
understanding you,

31:04 and tell me if that's
an incorrect assessment,

31:07 you are saying as soon
as you enter this stage,

31:10 some additional flaws come with
you, which increases your energy

31:16 consumption per unit.

31:18 So that's why you're using
the inflow into this stock

31:23 for adding these flaws.

31:26 And that's fine.

31:29 Conceptually, that's
one way to capture it.

31:33 Now, it has a little bit of a
challenge in terms of robustness

31:39 when I change the time constant,
for example, for becoming old.

31:44 So why is that?

31:46 So this is an interesting
kind of wrinkle here.

31:49 So we have these
mature buildings

31:53 staying in this stock
for time to become old.

31:56 And during that time, they
are accumulating these flaws.

32:00 That's the idea.

32:01 But to keep things simple,
Jake said, OK, well,

32:05 as soon as these guys
go into the next stage,

32:08 I'm going to give them all of
the flaws they will acquire

32:11 or half of the flaws they will
acquire, some measure of that,

32:16 and be done with
it and not worry

32:18 about this introduction of
flaws during the time you

32:22 are in this stock.

32:24 So that means if I
change this time constant

32:26 because I want to
have more stocks,

32:30 so I break it down
into smaller steps,

32:34 the mature building
energy flaws per unit

32:38 will not change automatically.

32:41 Whereas, it actually has to.

32:43 In fact, it is something
about per unit of time,

32:48 how much kilowatt hour per
square foot you are adding,

32:54 you multiply that by time
to becoming old to get

32:59 this parameter you have.

33:01 So doing that makes it robust
to this extreme condition

33:04 I'm talking about.

33:06 Now, this is one way to do
it, which puts everything

33:09 at the beginning.

33:11 What's an alternative
way to do this?

33:14 AUDIENCE: You can separate the
time constant to accumulate.

33:18 HAZHIR RAHMANDAD: So can you
speak up, Aldan, and explain

33:21 what you're trying to?

33:23 AUDIENCE: So I think you can
separate the time to become old

33:25 and the time to
accumulate those flaws.

33:29 So you can have the
rate, so you can

33:37 have another auxiliary
variable coming

33:40 from the start, the maturing
building, for example,

33:45 and divide it by
time to the flaw.

33:50 HAZHIR RAHMANDAD: So you
could take that new parameter

33:53 that I mentioned,
which is how many flaws

33:56 per unit of time per mature
building will be added,

34:00 and use that parameter,
multiply that

34:04 by the number of
mature buildings

34:07 to create a new
flow into the energy

34:11 usage of mature buildings.

34:13 That works just as fine and
gives very similar results

34:16 to what Jake has.

34:17 So I slightly prefer
that alternative

34:21 because it is a little
bit closer to how

34:23 things happen in reality.

34:25 That is, continuously,
these things

34:27 are being added based on
how many buildings you have,

34:30 rather than at the
very beginning when

34:31 these buildings come
in, you're dumping them

34:34 with this kind of step function
reduction in energy efficiency.

34:42 But that's a nice addition
that Jake had conceptualized.

34:47 Now let's look at the
thing we were focusing on,

34:50 which is the energy efficiency
gains for mature buildings

34:55 coming from retrofits.

34:57 So that flow variable
is, if average efficiency

35:04 of mature buildings is
higher than the lowest

35:07 feasible efficiency, then
retrofit benefit, otherwise 0.

35:19 Yeah, tell us.

35:21 AUDIENCE: I don't know that this
is necessarily the best way.

35:24 I unfortunately did two ways
of getting the retrofit benefit

35:28 from technology.

35:29 One is on these two
flows, and then one

35:31 is going to be on the new
building, like new stock.

35:35 So the idea was,
I just didn't want

35:38 the benefit you would gain
from efficiency to bring you

35:44 below a minimum average
efficiency for the buildings

35:48 there because they can't go
below a theoretical minimum.

35:54 And I was running into
issues specifically

35:57 with these flows where
it was, even though I

35:59 have limits involved elsewhere.

36:01 So I add it here.

36:03 HAZHIR RAHMANDAD: Yes.

36:04 So whenever you
see if-then-else,

36:07 you need to be a little
bit kind of thinking,

36:09 is there a better way to do it?

36:11 Not always, but sometimes, most
often actually you can find one.

36:16 Here, you have also
mature and the cohort

36:19 subscripts, which
kind of confuses me.

36:21 So can you tell what the
subscripts are doing here?

36:24 Because I didn't realize this
is also subscripted here.

36:27 AUDIENCE: So that's a bit of me
learning how to use subscripts.

36:32 Everything in this whole model
has cohort basically on it.

36:36 But the lowest
feasible efficiencies,

36:39 there is a different
lowest feasible efficiency

36:42 of kilowatt hours per square
foot for old, new, and mature.

36:46 And so I basically
wanted it to be,

36:49 as soon as new buildings enter
into these mature or old stocks,

36:54 you get some inefficiencies.

36:57 That whole average is
going to go up above that.

37:00 So you're going to get
retrofit benefit bringing back.

37:02 HAZHIR RAHMANDAD: Got it.

37:03 Got it.

37:04 So first of all, I
think let's recognize

37:09 what Jake is doing here
with the cohort subscript.

37:13 So he's creating a copy of
the model, the model that we

37:18 are seeing on the screen,
for different cohorts

37:21 and running that
through the simulation

37:26 for different cohorts,
which is good.

37:28 It's actually a better way to
capture the cohorts than just

37:32 age-tracking the cohorts.

37:35 I didn't tell you to do it this
way just to keep things simple,

37:38 but if you have done
it, that's great.

37:42 The formulation
here is then saying

37:44 there is a lowest feasible
efficiency for the mature stage

37:50 for any of the cohorts,
that if you're above that,

37:57 you can get benefits
of retrofits,

37:59 otherwise not with
this if-then-else.

38:01 That's the idea.

38:02 Now let's see where this
lowest efficiency comes from.

38:06 It's just a number.

38:07 So this one, for new
versus mature versus old,

38:16 it is using different numbers.

38:21 So that's just the parameter.

38:23 So this parameter is the
thing that we thought

38:27 could depend on the technology.

38:33 That is, basically the
technology for retrofits

38:37 could shift up or
down this parameter.

38:40 So the idea was to capture the
technology through this lowest

38:50 feasible efficiency.

38:53 Or at least that was the
idea that I had in mind

38:56 for the technology effect.

38:57 Now, that is not what
you are doing here.

38:59 So what you are doing is
changing the technology

39:04 for the new buildings, if
I'm getting it correctly.

39:09 AUDIENCE: So realistically,
at the top of this model,

39:13 there's technological limits.

39:15 

39:19 And that's coming to a value,
technological effectiveness

39:22 of retrofits.

39:23 I have that as like,
it becomes an S-curve

39:26 as there's more investment.

39:29 And then when I was trying to
think about how to really get

39:35 the benefit from that,
incorporating it below,

39:38 I introduced what I think is
probably wrong of another.

39:43 There's technological
limits overall

39:45 that come from what the
overall benefit would be

39:50 and then for each cohort.

39:52 Or for each stage of
building, I wanted

39:55 there to be its own
minimum efficiency

39:59 that you're working toward.

40:00 HAZHIR RAHMANDAD: I see.

40:01 So this technological
effectiveness of retrofits

40:04 is subscripted based on cohort.

40:07 So you are getting a change in
the technological effectiveness

40:12 per cohort.

40:14 And then where does it go?

40:18 And, Anne, you
asked a question, we

40:19 should get to that, if I didn't,
please bring it up again.

40:24 So it's going into New
Building Tech-Enabled.

40:29 AUDIENCE: Yes, it
goes both into,

40:30 there's a retrofit benefit
for new buildings and one

40:36 to retrofit.

40:37 HAZHIR RAHMANDAD: I see.

40:38 So this is a little bit
doing two different things

40:43 with this concept.

40:45 One is that for
new buildings, you

40:48 are able to have lower energy
efficiency to start with.

40:53 Is that how it
operates down here?

40:55 New building efficiency?

40:57 AUDIENCE: Yeah.

40:57 HAZHIR RAHMANDAD: Yes.

40:58 So that would be one path.

41:01 And then it is also helping
with retrofit benefits,

41:05 which comes from the
effectiveness of retrofits.

41:10 So per unit of investment
or per unit of retrofitting,

41:18 how much benefit you will get,
how much reduction you will get.

41:22 So that's, I think, what Jake
is trying to capture here.

41:26 

41:29 AUDIENCE: Yeah.

41:29 HAZHIR RAHMANDAD: OK.

41:30 So it may work.

41:35 It is also complex
because this concept here,

41:41 really, one thing is how
much retrofits can bring down

41:46 your energy efficiency, another
is, per unit of investment.

41:51 And you don't have
investment explicitly,

41:54 you're just doing a fractional
thing, but per unit of activity,

41:58 how much consumption
do you bring down?

42:02 How much do you bring down
the energy consumption?

42:04 These two are kind of
convoluted here a little bit.

42:08 The affect through the retrofit
benefit captures the second one.

42:13 The effect on the original
level of energy efficiency

42:18 that goes through the new
building minimum efficiency

42:21 is setting the baseline level.

42:26 But neither of those
actually captures the effect

42:30 on how far down
you can bring it,

42:33 which is the lowest
feasible efficiency.

42:37 So this is all
about assumptions.

42:40 If you assume the mechanisms
that are important

42:43 are these ones, that's OK.

42:47 But what I think I had, at least
in mind in defining the problem,

42:51 was more focused on
changing this lower

42:54 limit and how much you can
bring it down with retrofits.

43:02 And then the
efficiency of retrofits

43:04 per unit of investment,
we could still

43:07 make that dynamic based on how
close you are to that limit.

43:12 That is typically the
efficiency of investment

43:15 goes down as you get
closer to the limit.

43:18 So the first units of retrofits
are very cheap, very effective.

43:23 They bring down
things very quickly.

43:25 The later units are less
effective and so on.

43:28 But we could have that
conversation separately.

43:32 Anne, bring up your
question, I didn't get it.

43:38 AUDIENCE: Yeah, I thought that
for one of the parameters,

43:42 he had like an if-then-else.

43:44 HAZHIR RAHMANDAD: Yes.

43:45 

43:48 AUDIENCE: It's just more of
like a methodological question.

43:50 I was wondering if
that was necessary?

43:54 HAZHIR RAHMANDAD: So, no.

43:56 Yeah, it is not necessary.

43:58 So basically this equation, and
this is just kind of simple,

44:06 you can just write it as
5, 6, 7, and that's it.

44:11 And it should never be 0
because the cohort will always

44:15 be one of those three.

44:16 So this is how you
define parameters that

44:19 depend on the subscript levels.

44:23 You just put the three
numbers separated or N numbers

44:26 for the N different elements.

44:28 AUDIENCE: Now I've learned more.

44:29 HAZHIR RAHMANDAD: Yeah.

44:31 Great.

44:33 OK, let's switch
to another model.

44:36 For each of these models,
we could go one level deeper

44:39 and do some more real analysis
of seeing how well they behave.

44:44 But I want to get more of the
different conceptualizations

44:48 in place before we
do any deep dive.

44:51 If we get a chance, we
will do some deep dives.

44:53 OK, next one is
coming from Jason.

44:56 

45:05 OK, so we have the
buildings, similar story--

45:11 average building life
divided into three.

45:15 That's all standard,
straightforward.

45:19 Then, energy for new buildings,
energy for mature buildings,

45:24 energy for old buildings--

45:26 pretty similar.

45:28 Those are all in place.

45:31 Then there is the
energy reduction.

45:34 And this one, again, you could
have it for new buildings

45:37 as well.

45:38 

45:42 And the amount of energy that
you can bring down, here, let's

45:49 look at the equations
you're using here, Jason.

45:52 

45:55 So you have a current
energy efficiency factor,

45:58 which I assume is time based.

46:01 AUDIENCE: Yes, it's
for new construction,

46:03 they're being built with that.

46:05 HAZHIR RAHMANDAD: Yes,
so that's the current.

46:08 And that sets the max
achievable energy efficiency

46:12 for mature buildings.

46:14 AUDIENCE: With a delay.

46:15 HAZHIR RAHMANDAD: So let's take
a look at this formulation,

46:18 see what is happening here.

46:20 So you have a smooth
function that says,

46:23 take the current energy
efficiency of buildings,

46:26 delay it by some time, and that
becomes the achievable energy

46:35 efficiency for mature buildings.

46:39 And what is this time to
develop mature state of art?

46:45 So you're saying, as we improve
our energy efficiency technology

46:51 for new buildings,
that also determines

46:55 our ability for retrofits,
but with a delay

46:59 for changing those
technologies into technologies

47:02 for retrofitting?

47:03 AUDIENCE: Right.

47:04 HAZHIR RAHMANDAD: Am I
getting it correctly?

47:06 AUDIENCE: That's the
assumption I'm playing with.

47:09 HAZHIR RAHMANDAD:
Yeah, that's OK.

47:11 We want to be clear about
our assumptions first,

47:13 and then we could
discuss whether that

47:15 is the best assumption or not.

47:17 So the assumption
here is that there

47:20 is new building technology that
improves energy efficiency.

47:25 And then for retrofits,
they basically

47:29 follow the same technologies.

47:30 That is the technology that
sets the lower bound for energy

47:37 consumption.

47:38 So that only comes
with a delay, and that

47:43 sets the energy efficiency
for the mature buildings

47:48 at any point in time.

47:50 And similarly, a
very similar thing

47:52 but with a different
time delay impacts

47:56 the old buildings maturity
level or energy efficiency.

48:02 AUDIENCE: Yeah.

48:03 HAZHIR RAHMANDAD: OK,
so that's the idea.

48:05 Now let's do a few mental
extreme conditions.

48:10 So let's say buildings take a
long time in this first state

48:15 before they go to mature.

48:17 So let's say this is
30 year before they

48:20 go to the mature state.

48:23 But the time to develop mature
state of the art is very fast.

48:31 Then, what will happen?

48:32 We have buildings that
are the old designs,

48:40 but very soon they are able to
absorb a lot better technology

48:50 in terms of enhancing
their energy efficiency.

48:55 That's not fundamentally wrong.

48:57 I don't think that's necessarily
something that I can say

49:00 is breaking some law.

49:04 So it could happen.

49:07 AUDIENCE: I considered
anchoring that time

49:09 to develop mature state of the
art to that transition constant,

49:15 but I couldn't come up
with a good story to do it.

49:18 HAZHIR RAHMANDAD: Yeah, so
it is really the question,

49:21 the conceptual question is
whether the technologies

49:24 for improving energy efficiency
are tied to the technology

49:28 or to how the building
is built or they

49:32 are tied to some external
technologies that

49:35 are being renovated
and improved regardless

49:39 of how the building is built.
And these two conceptualizations

49:43 are not wrong.

49:45 It really is a matter of
expert opinion on how much

49:49 you put a weight on
one versus another.

49:52 But what is, I think, helpful
is to have something that really

49:58 ties to the building, and
then change that based

50:01 on the technologies of the day.

50:03 That gives you a lot
more flexibility.

50:06 So if you tie your ability
to get mature buildings,

50:13 bring down their energy
efficiency to mature buildings,

50:16 that is it is a feature
of mature buildings,

50:19 then you can play with that.

50:20 You can bring it down
faster or slower,

50:23 and you can get that
hint from the existing

50:26 technologies in the marketplace
and have any delay for that.

50:31 That all works.

50:32 And then you set that
limit in a way that remains

50:36 with that mature building.

50:38 And when it goes to the old
building stage, it goes with it.

50:41 So it is a coflow that
carries that underlying

50:46 potential with it.

50:48 So that would be a more
robust, general way

50:51 of doing it than what you have
here, which kind of may work OK,

50:57 but may also, in some settings,
miss this correspondence.

51:03 And that creates a problem.

51:05 So I think the rest of this
model is fairly straightforward.

51:09 It's doing the same thing for
the energy of old buildings.

51:13 And then there is some kind
of aggregation, correct?

51:17 Or is there something else?

51:18 

51:21 AUDIENCE: That's all
that's happening.

51:22 

51:25 I just averaged over all
of them to get the full,

51:30 so I could compare system
level and cohort effects.

51:33 HAZHIR RAHMANDAD: Yeah, yeah.

51:34 And you do want to have an
improvement here as well.

51:39 AUDIENCE: Yeah.

51:40 HAZHIR RAHMANDAD: So
conceptually, there

51:42 is nothing different from old
building versus new buildings

51:45 versus mature buildings for
being candidate for energy

51:50 efficiency retrofits and so on.

51:52 But because they have
better energy efficiency

51:56 at the beginning, they are
closer to that potential.

51:59 It's not very cost effective,
so people may not do it.

52:02 So that decision to how much
you invest in energy efficiency

52:08 is important.

52:09 Right now, you're taking
that decision just

52:12 buy some time constant.

52:13 

52:18 Actually, let's look
at that equation.

52:19 So right now, you're saying
we take the energy efficiency,

52:24 we compare it with the minimum,
and you just close that gap.

52:27 

52:38 Yes.

52:39 So this minimum energy
required for mature buildings

52:42 is coming from the technology
and how many buildings you have.

52:46 And you try to close that
gap over a time constant.

52:51 That's an OK first-order
approximation but really kind

52:54 of skips all of the
decisions on how

52:57 do you allocate
limited resources, how

52:59 do you decide whether it is
cost effective, and so on.

53:01 You can't do that
with this formulation.

53:04 But as a first cut, it is
a decent starting point.

53:08 AUDIENCE: Can I ask a question?

53:10 We're just talking about
potential retrofitting

53:13 for new buildings.

53:14 I think it actually
may be very cost

53:18 effective to do this when
you're building a building

53:20 if there is a recent jump.

53:22 HAZHIR RAHMANDAD: Yeah, exactly.

53:23 AUDIENCE: Because they
last a lot longer.

53:25 HAZHIR RAHMANDAD: Exactly.

53:26 AUDIENCE: They're not as close.

53:27 HAZHIR RAHMANDAD:
Exactly, exactly.

53:30 Yeah.

53:30 And that's actually a good
reason also to include them,

53:35 but also to make the decisions
on retrofit investment subject

53:41 to some measurement
of lifecycle cost

53:45 benefits of doing the retrofits
at that stage for that building.

53:50 So you would basically have
the life expectancy of building

53:55 and the delta in
energy consumption

53:57 that you will get from that.

54:00 And then that marginal benefit
multiplied by the time horizon

54:05 gives you the total benefit.

54:07 And then you can compare that
with the total cost of retrofit.

54:11 And that becomes a more
solid decision heuristic.

54:17 AUDIENCE: Just
one last question.

54:18 Regarding that
second coflow part,

54:20 I didn't have that
much information.

54:24 Is the reason that we
need that coflow, is it

54:27 because that this first coflow
gets contaminated by the cost?

54:32 HAZHIR RAHMANDAD: Exactly.

54:33 AUDIENCE: It's not
in the original.

54:35 HAZHIR RAHMANDAD:
So it is really

54:37 that they have
different purposes.

54:39 So one of them is tracking
what is happening now

54:43 inside the energy
consumption story.

54:47 The other is tracking
some underlying feature,

54:51 some underlying feature about
how much you can actually

54:54 go towards building
more efficient.

54:57 So these are two different
features of buildings.

55:00 So you need two different
coflows for them.

55:02 That's basically the
core insight from this.

55:06 So let's look at another model.

55:08 

55:20 So Gerardo has a simpler model.

55:22 I suspect it is not.

55:26 AUDIENCE: Yeah, I
didn't want to remove--

55:27 HAZHIR RAHMANDAD: OK,
you have subscripts here

55:30 for building type.

55:32 And what you're doing is that
technology advancement brings

55:38 down the cost of energies.

55:45 AUDIENCE: I have
different groups.

55:46 HAZHIR RAHMANDAD: Oh,
you have different,

55:49 also, you have
building groups here.

55:50 Got it.

55:51 Yes.

55:53 Yes.

55:54 I see, I see, I
see, OK, thank you.

55:56 So you have the buildings
that are constructed.

56:03 Interesting.

56:04 And so basically
you have built--

56:11 yeah, tell us.

56:13 AUDIENCE: I use subscript
for how buildings are built.

56:21 Like, for example, for the three
types of buildings in subscript.

56:36 And that, in my
opinion, my assumption

56:43 would be the winter
effect in the subscript.

56:47 And I would put improvement
with the retrofit in the float.

56:56 And so this is our--

56:59 HAZHIR RAHMANDAD: Yes.

57:00 So actually, one thing, so
this is a general comment

57:05 beyond this specific
case, is that if you

57:08 have a subscript like
here, TypeA, TypeB, TypeC--

57:14 you also have Class A,
Class B, Class C buildings.

57:17 It just makes it hard
for us to follow.

57:20 I don't know whether,
for example, these

57:22 are the same thing
you're trying to model

57:25 or very different concepts.

57:27 Class and type are the
same or are they different?

57:29 Can you tell what is TypeA,
TypeB, TypeC versus Class

57:32 A, Class B, Class C?

57:34 AUDIENCE: Yes, OK.

57:35 I'll explain it to you.

57:36 So in my assumption,
the subscript,

57:42 I did subscripts for modeling
the technological, for example,

57:49 I was thinking about a good
house more or a house building

57:58 segment or technological
type of building.

58:03 HAZHIR RAHMANDAD: OK,
so that's the type?

58:05 AUDIENCE: The type, exactly.

58:07 And the class is
the energy class.

58:10 HAZHIR RAHMANDAD: Yes, got it.

58:12 So basically, you are
capturing retrofits

58:15 through moving buildings
in different categories.

58:20 So it kind of gets close
to Ali's formulation.

58:24 That is, you're moving
buildings from those

58:28 that don't have retrofits.

58:29 So call it building Class
C, to Class B to Class A.

58:34 So rather than a
continuous conception

58:36 of, OK, we invest and we
bring retrofits continuously,

58:42 this is kind of two steps
for bringing things down.

58:45 

58:51 And then there is
a cost for each

58:53 of these steps of improvement.

58:56 And you may have a
budget, so that tells you

59:00 how much the building goes down.

59:03 And this is a messy formulation.

59:09 So let's actually look
at this formulation that

59:13 has a few things that should
be done in a different way.

59:16 So first of all, you have this
if-then-else Buildings Class

59:19 Type.

59:20 Don't worry about the
subscripts BuildingType.

59:23 It's the same.

59:25 The formulation is the
same for all of them,

59:27 so it doesn't matter here.

59:28 If this thing is
above 0, do drain it.

59:33 Otherwise, go to 0.

59:37 So this is basically
what Gerardo

59:44 has done to avoid draining
the stock Class C below 0.

59:52 And this is not a good
way of doing that.

59:56 It's basically a
very hard constraint

59:59 that says, do
whatever rate you want

60:01 to do, and then kill the
outflow as soon as you get to 0.

60:07 And this is a recipe for going
under 0, small amounts under 0,

60:12 because it has to go under 0
for this solution to kick in.

60:18 It also kind assumes
that every last building

60:23 is available for retrofits,
for improvements, it's visible,

60:28 it's easy to find it,
it's easy to convince

60:30 the owners to do the retrofits.

60:34 So that's also another
problem with this formulation.

60:38 So what's the standard
formulation here?

60:40 We have seen versions of
this in the basic course.

60:45 Anybody wants to share what
the standard solution to this

60:49 might be?

60:51 Kathy, do you want
to take a stab?

60:53 

61:06 So don't worry about the
rest of the formulation.

61:08 Just how to get rid
of the if-then-else

61:10 and replace it with
something that is

61:14 a bit more robust and cleaner?

61:16 

61:25 AUDIENCE: Would you just
want a first-order draining?

61:28 HAZHIR RAHMANDAD:
Would you speak up?

61:30 AUDIENCE: Would you just
want a first-order draining?

61:34 HAZHIR RAHMANDAD: I can't hear.

61:36 AUDIENCE: Sorry.

61:36 Would you just want to do
a first-order draining?

61:41 HAZHIR RAHMANDAD: So you
could do a first-order limit

61:45 on draining.

61:46 That is, you say
maximum drain rate,

61:49 and that maximum drain
rate is the stock divided

61:52 by a minimum time to retrofit.

61:55 And then that becomes the
constraint as a maximum level.

62:00 Then you take the minimum
of that maximum drain rate

62:03 and whatever is
your formulation.

62:06 So is that clear?

62:06 That's a very simple,
standard solution

62:09 that we use whenever we want
to put a first-order constraint

62:14 on how fast we are draining.

62:16 So stock of tasks
in a project model,

62:19 you don't put a if-then-else
tasks are above 0,

62:22 do it, otherwise don't do it.

62:24 You put, it's the minimum of
max task completion and task

62:29 completion from resources.

62:32 For shipments, it's a minimum
of maximum shipment rate

62:36 and shipment from demand or
whatever you want it to be.

62:41 OK, so that's kind of
basic stuff on that front.

62:47 Then, you have other things
coming into this efficiency

62:51 improvement for classes, which
is the budget divided by cost

62:56 multiplied by building
type, cost sensitivity,

62:59 some sensitivity fraction.

63:02 

63:07 So why do you need
two parameters?

63:09 Why do you have cost
for improved building

63:12 from C to B and building
type cost sensitivity?

63:15 Can you tell what was
the idea, Gerardo?

63:18 AUDIENCE: The idea was that
for the type of buildings

63:22 that we add into
the subset, it will

63:25 be different for how
much you need to deliver.

63:30 HAZHIR RAHMANDAD:
Yes, so that would

63:31 be the cost for improving
building from C to B.

63:36 Why do you need a separate
sensitivity parameter?

63:39 I'm just not following the
need for two different.

63:43 

63:52 AUDIENCE: One's enough?

63:53 HAZHIR RAHMANDAD: Yeah.

63:54 

63:57 Yeah, because this also has
three different drivers.

64:01 So there is a little bit of
a proliferation of parameters

64:04 that don't do anything here.

64:06 So you don't want to have that.

64:07 That's generally the idea.

64:10 So this is taking
buildings one level down

64:14 and allows that to happen.

64:17 Right now, your demolition is 0
for all of these things, which

64:22 is not going to work well.

64:25 You would just
accumulate buildings

64:27 and they will never
be demolished.

64:28 

64:31 Yes.

64:32 So the demolition
rates, right now

64:36 you don't have
aging of buildings,

64:37 which is another problem.

64:38 But putting that
aside, you definitely

64:41 need to have outflows from
these stocks of buildings.

64:44 Otherwise, buildings
will stay around forever.

64:47 So a set first-order delay,
a first-order draining

64:51 would be the
simplest formulation

64:53 that would be Building
Class C divided

64:55 by life of Building Class C or
lifetime of building in general.

65:02 So those are some of
the key feedback here.

65:07 Then you have all
of these buildings

65:10 at different classes being
accumulated into Cumulative

65:14 Building Type Consumption.

65:16 So tell me what
this thing is doing.

65:21 So I think I know
what it is doing.

65:25 And it is not the exact
right way to do it.

65:28 So basically, what
you need here,

65:31 you are trying to add up
what is the total building's

65:35 consumption of energy or
consumption rate for energy.

65:41 AUDIENCE: Yeah.

65:42 HAZHIR RAHMANDAD:
And that is the sum

65:49 of the buildings multiplied
by energy use per building,

65:55 in this case.

65:58 And this is in kBTU per month.

66:03 Yes, so this is your total
energy consumption, I see.

66:06 And then you have the
cumulative energy consumption

66:09 from beginning of
the time up to now.

66:10 So this is not wrong.

66:11 This is also fine.

66:13 So the core idea is now you
have this other technology

66:20 side that is changing the cost
of efficiency improvements,

66:28 I think.

66:29 

66:32 Yes.

66:32 So the cost of energy efficiency
improvements in this model

66:36 is being improved
exogenously through

66:39 some technological advancement.

66:43 And then that makes it
cheaper to shift buildings

66:49 from one stage to the other one.

66:53 Now this one is not
capturing the effect

66:56 we were talking about.

66:57 So there are two
different possibilities.

66:59 One is that I'm making it
cheaper to bring down the cost

67:03 to retrofit.

67:06 The other is, I'm making it
possible to do more retrofits,

67:11 that is, get to lower
levels of energy

67:14 consumption per square foot.

67:17 I was more focused
on the latter.

67:19 This formulation
tackles the former.

67:22 This captures reductions in
the cost of energy efficiency,

67:26 but doesn't capture the fact
that your Building Class

67:32 A may now have even a lower
energy efficiency because now we

67:38 have developed
better technologies.

67:39 Or you could, in fact, think
of other classes that are not

67:44 typically available to be
visited at the beginning

67:48 of time, but then by 2000s, you
have new classes of buildings

67:53 in terms of energy efficiency
that become available to others.

67:58 So that's kind of the
effect we are talking about.

68:02 And then the other problem
is that every building,

68:06 with enough investment, can
go all the way to Class A,

68:08 so this is missing
on the part about,

68:11 OK, some things are just
not realistic or feasible.

68:15 For that vintage of buildings
that was built in 1950s,

68:20 you can't make them zero homes
unless you completely got them

68:26 and rebuild them, which is a
different story than retrofits.

68:31 OK, so that's a good
conversation on this model.

68:36 Let's go to the next one.

68:38 

68:41 This is Hassam's.

68:42 

68:48 AUDIENCE: Presentation on this
maybe a little bit different

68:50 from how we worked on the
conceptualization together.

68:53 It has a subscript.

68:54 HAZHIR RAHMANDAD:
This is subscripted

68:56 so that you can basically
add the number of vintages

69:03 as you want.

69:04 Great.

69:05 So you have the built
area, which is buildings,

69:07 and you have retrofitted areas.

69:13 So let's look at the
subscripting part

69:15 because that's something that is
new for some of the folks here.

69:19 So here, Hassam is subscripting
items on vintage ranges.

69:29 AUDIENCE: These are
subranges I ended up using.

69:31 HAZHIR RAHMANDAD: Yes.

69:32 So you have the
subscript range vintage.

69:38 And this vintage
accounts for, so you

69:42 can have V1, V2, V3, et cetera.

69:47 

69:50 And if I look at the
vintage members, elements,

69:54 right now it is only 3.

69:57 So the way this formulation is
formulated, it is not incorrect.

70:04 This is fine, but it is
not the most efficient way

70:07 to formulating these.

70:09 And the reason is that now if
I want to add a force element,

70:13 I have to define a
force formulation.

70:17 But that force formulation
would basically

70:20 be the same as V3 formulation.

70:23 

70:27 AUDIENCE: The goal was to have
a first, a middle, and an end.

70:29 HAZHIR RAHMANDAD: Exactly.

70:30 So that's how you would do.

70:32 AUDIENCE: But it didn't work
well, so I ended up using this.

70:34 HAZHIR RAHMANDAD: So
you couldn't figure out

70:36 how to do the subranges so that
you can get the first, last,

70:41 and middle formulation to work.

70:43 That's fair.

70:44 It's not a trivial thing.

70:46 It needs playing around.

70:48 I gave an example age model
inside Vensim that does it,

70:52 I think.

70:53 So check that out.

70:55 That's a good way.

70:56 But for those who are not yet
following what this is doing

70:59 or what this one can do, right
now we have three vintages.

71:05 That's easy.

71:06 You just build them.

71:07 But if you wanted
to have 100, then

71:10 doing it manually
just becomes so messy,

71:13 you're not going to even try it.

71:16 The structure that
Hassam has here

71:20 allows him to basically
do that without creating

71:25 copies of the model 100 times.

71:29 You can just do it with
the same formulation

71:32 that you have done for three.

71:33 So that's the thing
that is nice about it.

71:36 Now, for that to
work, you need to do

71:40 a little bit of subscript
manipulation in Vensim.

71:43 That is, you would say,
OK, new buildings only

71:47 enter into the first
element of the subscript,

71:52 and demolition only happens to
the last element of subscript.

71:57 For everything in
between, what is happening

72:00 is that they are
getting aging buildings

72:05 from the previous cohort and
they are sending elements

72:10 to the next cohort.

72:12 So you need to do that using
subranges, in Vensim lingo,

72:19 to do it effectively.

72:22 It takes a little bit
more time than I want

72:25 to allocate to do that here.

72:27 So let's not do it together.

72:29 If I get the chance, I may put
together a model that has that,

72:32 but that's the idea.

72:34 And then conceptually,
essentially, you

72:37 are doing a similar
thing as Ali,

72:40 in terms of moving buildings
into a retrofitted stage

72:45 and with that, moving
their energy consumption

72:51 to the level that
is corresponding

72:53 to the retrofitted ones.

72:55 AUDIENCE: This allows
for retrofitting

72:57 on all three vintages.

72:58 HAZHIR RAHMANDAD: Yes.

72:59 And this allows for
retrofitting on everything.

73:03 The technology for retrofits--

73:07 AUDIENCE: So I'm
doing the same thing

73:09 that Ali did, which I
have a new technology

73:12 and I'm assuming that the new
technology for new buildings

73:15 is the same as the gold
standard for retrofitting.

73:20 So the new technology
for retrofitting

73:22 will be a weighted average
between the current energy

73:25 efficiency and the best
that they can get right now.

73:29 HAZHIR RAHMANDAD: Yes.

73:30 

73:34 OK, weighted average between
the current energy efficiency

73:38 of that cohort.

73:39 AUDIENCE: And it's
going in to retrofitted.

73:40 HAZHIR RAHMANDAD: Yes.

73:43 OK, OK, good.

73:46 Yeah, that basically
hard codes the limit

73:51 that you can achieve as
this weighted average.

73:55 It doesn't allow you
to dynamically change

73:58 that based on new
technologies and so on.

74:00 So that's kind of the downside
of not having a third coflow.

74:04 AUDIENCE: The impact
of retrofitting,

74:06 for example, which can
make it endogenous,

74:08 but that is not trivial.

74:11 HAZHIR RAHMANDAD: Yes.

74:12 Well, but that limit is the key.

74:17 That is, right now you are
basically getting everybody

74:20 to this new retrofit level.

74:22 

74:26 AUDIENCE: Yeah, the new
retrofit level, but it

74:28 is a weighted average between--

74:30 HAZHIR RAHMANDAD: Yeah.

74:31 

74:36 AUDIENCE: Actually, we were
thinking that the new efficiency

74:39 or energy consumption
is somewhere

74:41 between the maximum and the
original of that cohort.

74:48 The simplest way is
taking the average.

74:50 It will be exactly
the middle point.

74:52 HAZHIR RAHMANDAD: Yeah.

74:55 And that parameter
impact of retrofitting

74:57 is shifting whether it
is in the middle or not.

75:00 Yeah.

75:03 So you could make that
parameter a function

75:12 of basically the cohort
you are looking at,

75:16 the vintage you are looking at.

75:17 And then that could change
dynamically in some way.

75:22 That would be how you
would do the history

75:26 or kind of capture the history.

75:29 Good.

75:31 I'm not going through
the details here.

75:34 I think the rest
is probably sound.

75:37 So let's look at maybe one more
model before we take a break.

75:46 So let me do this.

75:49 Yes.

75:51 So this is Anne's.

75:52 

76:08 Go ahead, Anne.

76:10 AUDIENCE: I tried to do
like the subscripts thing.

76:14 But there's also
a very big wrong,

76:16 as I'm showing
here, where I don't

76:18 know why I thought that an
efficient building consumes

76:22 more energy.

76:22 I think I did it late at night.

76:24 HAZHIR RAHMANDAD: Yes.

76:25 AUDIENCE: Yeah.

76:26 HAZHIR RAHMANDAD: It's OK.

76:28 We can define efficient
as inefficient.

76:31 So energy inefficiency
of building vintage.

76:33 AUDIENCE: Yes, that's the word.

76:34 HAZHIR RAHMANDAD: Yeah.

76:36 Yeah.

76:38 So basically, this is energy
consumption type of a thing, so

76:43 variable namings.

76:45 AUDIENCE: Yes, the variable
name is off as well.

76:47 It should be energy consumption.

76:50 HAZHIR RAHMANDAD: Yeah.

76:51 So the units are OK but not OK.

76:54 So you have kilowatt hour
per square meter, which

76:59 is the right unit, but it
should be kilowatt hour divided

77:02 by square meter so that
your buildings would

77:05 be in a square meter and then
the average energy efficiency--

77:10 OK, you have the units building.

77:11 So this is actually important
for unit consistency.

77:19 Yeah, this is hard to
make unit consistent

77:21 if you don't do it right.

77:23 So the buildings, they
are in square meters.

77:27 That's easy.

77:28 You could also go with
just number of buildings,

77:31 but then you're missing the
square meter, which is probably

77:34 better, or square feet,
which is a better.

77:36 AUDIENCE: Yeah, I think went
with number of buildings.

77:39 HAZHIR RAHMANDAD: Yes.

77:40 So if you do that, then the
unit for energy consumption

77:44 per building would be kilowatt--

77:48 it's actually not
kilowatt hour, it's

77:50 kilowatt per building rather
than per square meter.

77:56 Or you could make it kilowatt
hour per year per building

78:00 or per square meter.

78:02 So those are the options.

78:05 AUDIENCE: The averages,
it was then per building.

78:08 HAZHIR RAHMANDAD: Yes.

78:09 But I'm just saying the units
that you are putting here

78:15 should be kilowatt hour per
building per year or something

78:29 like that so that
when you multiply that

78:34 by the number of buildings,
the total energy consumption--

78:41 or actually, no, this
is not per building.

78:45 This is for all buildings.

78:47 This is kilowatt hour per year.

78:49 This is for the stock.

78:52 And then for per
building value, it

78:58 becomes kilowatt hour
per building per year.

79:04 So the time units are kind of
missing from this formulation.

79:09 And the unit consistency
is not enforced

79:13 when you don't have
the right units here.

79:16 So that's the unit part.

79:18 Now let's look at
the constructs.

79:21 So you have one
stock for buildings,

79:30 so you don't have
multiple life stages.

79:34 You have the vintages
captured using subscripts,

79:37 if I'm understanding
you correctly.

79:39 So you're using subscript year.

79:42 And by the way, using
the subscript year

79:44 is going to be very
confusing because you

79:46 can have built-in units of year,
so things will become messier

79:51 when you use year as
your subscript name.

79:55 It may even result in
some errors in Vensim.

79:59 But let's not
waste time on that.

80:06 So the way you are
capturing it is

80:09 that you are looking at the
retrofit potential, which

80:13 is coming from maximum possible
efficiency of building vintages,

80:19 and that is determined by the
technology that is affecting

80:27 that max possibility.

80:31 So the way you are capturing
that is for each unit,

80:36 there is an initial
vintage, then

80:41 there is a gain from technology
for each type of a unit.

80:47 And then the technology goes up
that shifts the marginal unit

80:52 of benefit from retrofits.

80:56 And this creates the
maximum possible efficiency.

81:00 And then you look at the gap
between the current energy

81:06 efficiency, minus current
energy efficiency.

81:14 

81:18 So this is kind of where, again,
lack of units become a problem.

81:22 Because right now, retrofit
potential is going to impact.

81:28 

81:33 OK, you're looking at
the gap and then closing

81:35 the gap with the time constant.

81:36 So that's kind of similar
to Jason's formulation.

81:41 But here, for different,
what you call vintages,

81:45 which are not aging,
but that's OK,

81:48 you have for different
vintages, different potentials.

81:54 So that's nice because now
you do have that underlying

82:00 feature of vintage captured kind
of inside these two parameters.

82:06 So in the marginal gain and
initial possible efficiency

82:10 parameters, you have
captured how much

82:13 energy efficiency is feasible
to get for different buildings.

82:19 Now we have this confusion about
energy efficiency versus energy

82:23 consumption that may actually
create weird behaviors here.

82:26 I haven't thought that through.

82:30 OK, good.

82:31 Thank you, Anne.

82:32 Any questions,
comments on this one?

82:37 Why don't we now take a break?

82:40 I think it's a good time
to spend a few minutes

82:43 resting and refreshing.

82:46 It's dense, looking at models.

82:51 So perfect mixing assumption
comes basically with everything.

82:58 You can't get rid of it.

83:01 So it will always be there.

83:03 If you need more
resolution, that is,

83:06 separating whatever you
have into categories based

83:10 on some feature, you
need more stocks.

83:13 That is, you need to
explicitly separate them.

83:17 So there is no avoidance.

83:19 Once you have a
single stock, you

83:21 have the perfect
mixing assumption.

83:24 Now, in these
cases, you may think

83:27 that I'm doing something
that removes perfect

83:30 mixing by doing a fixed delay.

83:32 So I have entry and the
removal with a fixed delay,

83:35 or with the first sixth-order
delay or whatever.

83:39 That is actually
not doing the job

83:42 in the way your mind kind
of sees, because it creates

83:47 six different stocks for
a sixth-order delay that

83:50 is in the background happening.

83:52 So it is doing the
disaggregation.

83:55 It is just not
showing it to you.

83:58 But you don't have access
to those intermediate stocks

84:02 and therefore you can't
manipulate them directly.

84:07 So that means you cannot fully
use the additional complexity

84:13 you have introduced.

84:15 You cannot really get
information from those

84:19 intermediate stocks, and that
makes it harder to actually do

84:24 things consistently.

84:25 Now sometimes that is OK.

84:26 That's why we do use
higher-order delays.

84:30 But as soon as you use
higher-order delays, usually

84:33 the stock that is capturing
the sum in the middle,

84:37 you can't do other
things with it.

84:39 You can't add a flow variable
to it because you lose control.

84:45 You don't have
control over what is

84:46 happening in the 6 stocks that
need to, in parallel, happen

84:50 to this.

84:51 So that's why it's better to
just not do it in most cases.

84:55 AUDIENCE: So just be
comfortable with that.

85:00 HAZHIR RAHMANDAD: Yes.

85:01 AUDIENCE: Know that
it's happening.

85:02 HAZHIR RAHMANDAD: Yes.

85:03 But the bigger kind
of the process lesson

85:06 is, if you need heterogeneity,
you need to disaggregate.

85:12 And if you are using
higher-order delays going around

85:18 the stocks-- that is, you also
have the stock that is impacted

85:22 by inflow and outflow of
that higher-order delay--

85:27 don't manipulate anything
else inside that stock.

85:29 That is, don't use other
flows coming in or out of it,

85:32 or otherwise you lose
control because now you

85:36 have lost your parallelism with
the hidden stocks in your delay

85:41 function.

85:42 Those are the key ideas.

85:44 OK, I think we have one more
model left and that is Alban's.

85:49 So let's bring that up.

85:51 

85:54 So this one is also doing the
subscript-based formulation

86:03 for the cohorts or
for the vintages.

86:08 So this is similar
to Hassam's model.

86:15 

86:22 If you look at the formulation
here, for C1, the cohort 1,

86:28 the inflow is New
Building Construction.

86:31 The outflow is
Building Aging for C1.

86:34 For C2, it is Building Aging
for C1 that is increasing it,

86:38 Building Aging for
C2 that decreases it.

86:42 For C3, it is Building Aging
C2 minus Building Demolition.

86:46 So very similar, and also Alban
hasn't done the more general

86:52 formulation that would
allow him to basically solve

86:59 this problem at a scale
without adding new equations,

87:02 but that's a separate thing.

87:04 We can actually probably do
that, take a quick look at that

87:08 together.

87:10 OK, so Building Demolition
and Time for Demolition,

87:15 et cetera, those are
straightforward, I think.

87:19 

87:23 So that's for just
the demolition.

87:25 Sorry.

87:25 And the Building
Aging is aging cohort.

87:28 

87:30 So this Average Time for
Demolition should be 30 years.

87:35 So after you got 40, then you
have another 30 years to go.

87:38 Is that how things are working?

87:39 OK.

87:40 So this is not the uniform
distribution that others had

87:43 used, 20-20-20 or
something, this is 20-20-30.

87:48 And that's OK.

87:49 There is nothing
wrong with that.

87:52 So building aging
is straightforward.

87:54 Then you have the total
energy consumption

87:57 for buildings of each age.

88:00 You have the average energy
intensity of buildings.

88:04 So that average energy intensity
controls the movement of item.

88:10 And then you have the increasing
energy consumption that

88:14 is coming from new buildings.

88:16 This is fine.

88:19 And then you have the retrofit.

88:20 So this is really the
interesting space that we have.

88:25 And this is done through
comparing indicated total energy

88:31 consumption after retrofit
versus the current total energy

88:34 consumption divided
by time constant.

88:37 So this is a very
similar formulation

88:38 to a couple other
formulations we saw.

88:43 You just look at the total
minus indicated divided

88:48 by time to finish retrofit.

88:54 And this is because it is
decreasing, so it is an outflow.

88:58 It is the total minus indicated.

89:02 If it was an inflow, it would
be indicated minus total.

89:07 So this is working fine.

89:10 Again, with the caveats
that we mentioned,

89:12 that this kind of
time-constant-based

89:15 doesn't allow you to
think about investment

89:17 and allocation and all those
things that you may care about.

89:21 And then where does the
indicated come from?

89:24 It is total buildings
multiplied by average energy

89:27 intensity of buildings
that are retrofitted.

89:32 And we have this
thing that is fraction

89:34 of buildings under retrofit.

89:36 So let's look at this.

89:37 I don't know what's
happening inside this.

89:41 So you have buildings.

89:44 This is just for units, for
scaling of the per building

89:48 item to everything.

89:50 So this part you don't
need to worry about.

89:53 The next part is what the
meat of the equation is.

89:57 So fraction of buildings
under retrofit multiplied

90:01 by average energy
intensity of building

90:04 retrofitted plus
1 minus fraction

90:11 of buildings under
retrofit multiplied

90:14 by average energy intensity
of buildings for this cohort.

90:19 So tell us what you are
trying to do, Alban, here.

90:22 I'm not completely sure.

90:24 AUDIENCE: So the fraction of
building under the retrofit

90:26 is controlled by investment.

90:29 So the investment
increased the fraction

90:31 of building under retrofit.

90:35 And then the indicator
total energy consumption

90:38 is lowest retrofitted multiplied
by the energy intensity of those

90:44 retrofitted plus those
not retrofitted multiplied

90:49 by the energy intensity
of those not retrofitted.

90:53 HAZHIR RAHMANDAD: So
at any point in time,

90:56 you're saying there is
a fraction of buildings

90:58 that are being retrofitted.

91:00 Is that the idea?

91:03 

91:10 So if that fraction is small,
then everything will be smaller.

91:19 

91:25 AUDIENCE: If it's zero, then--

91:29 HAZHIR RAHMANDAD:
Nothing happening, yes.

91:31 And if that fraction is 1, then
everybody is moving towards--

91:36 AUDIENCE: The retrofitted.

91:37 HAZHIR RAHMANDAD:
--the retrofitted.

91:39 So this is kind of
thinking of retrofitting

91:41 as a continuous process.

91:43 And at any point in time,
you could be retrofitting,

91:51 or some subset of buildings
could be retrofitting.

91:55 And it is a random subset.

91:57 AUDIENCE: Right.

91:58 HAZHIR RAHMANDAD: So
that allows for assuming

92:01 that they are the average.

92:03 They have the average
and they can go down

92:06 to the required level.

92:09 

92:14 Yeah, I think this should work
because as you turn it on,

92:20 it will drain things.

92:21 You turn it off, the
average has come down

92:26 and there is less room to do,
but there is still room to do.

92:30 OK, yeah, this looks fine.

92:34 And then that gives
you flexibility

92:37 for investment formulation that
determines fraction of buildings

92:45 that are under retrofit.

92:47 Now, this is a little
bit more tricky.

92:52 So you have the fraction.

92:53 You get a number
between 0 and 1.

92:55 And you can do a step
function or whatever you do.

92:58 

93:04 And you are saying retrofit
cost per square foot.

93:08 

93:12 How do you make sure
this fraction remains

93:14 between 0 and 1?

93:16 

93:25 AUDIENCE: Yeah, I missed it.

93:26 Yeah, this is not accurate.

93:29 HAZHIR RAHMANDAD:
Yeah, it's not obvious

93:31 that it would remain
between 0 and 1.

93:33 

93:38 Because that fraction needs
to be between 0 and 1.

93:40 Now, what is
conceptually also tricky

93:44 here is that you have
a cost for retrofitting

93:49 that you're trying to
reflect in this parameter,

93:52 retrofit per square
foot, but you also

93:58 have the time to
finish retrofit,

94:07 which controls how much
retrofitting actually happens.

94:11 

94:17 So if I allocate some
amount of investment,

94:21 so this is investment in
retrofit that I allocate,

94:29 how do I know?

94:35 

94:42 OK, so let's actually run this
model because you have a step

94:45 function.

94:45 So it's possible to
see what's happening.

94:52 So we can have an
investment that goes up.

94:57 

95:03 So the fraction of buildings
goes to 0.2 or something,

95:07 I think.

95:09 Yeah.

95:10 OK, so that's good.

95:12 Then, average energy consumption
is going down beforehand

95:25 because newer
buildings are coming in

95:29 with lower energy efficiency.

95:32 And then retrofits turn on.

95:35 And average energy intensity
can go down even further.

95:45 Max energy efficiency here is,
for C1 is 0.2, for C2 it is--

96:08 so we have that same issue
that these maxes are now fixed.

96:14 Of course, you could,
I guess, change them

96:17 with the step functions here.

96:19 So that is where you
would be changing those.

96:25 But they are applying to
the C1, C2, C3 rather than

96:31 the buildings.

96:33 So this is kind of
where a coflow would

96:37 associate these maximums
to the underlying buildings

96:42 and track them moving
with the buildings

96:44 as new buildings
are added and so on.

96:47 Whereas the current
formulation fixes them.

96:50 So this, you start
in year 1900, you

96:56 have the same
underlying values as you

97:01 would have for buildings
that are introduced in 2000

97:04 and so on.

97:05 So that's why this is not
the best way to do it,

97:08 even though it is good that
it is separated for the three

97:10 different cohorts and allows
you to set them separately,

97:17 how far they can go down.

97:18 And you have formulations here
with investment that similarly

97:22 would bring down this.

97:25 Now, OK, let's look
what is happening here

97:29 in energy intensity
of buildings.

97:35 And so for C1, we had
higher or we had lower.

97:55 We could get a lot of
efficiencies that what C1 has.

98:01 C1 has a gain of 2.

98:04 So what is this
gain doing exactly?

98:07 So that's the formulation
for average energy intensity

98:10 of retrofitted building.

98:13 So that formulation
is 1 minus this max.

98:26 

98:32 Ah, so this is actually an
interesting formulation.

98:38 So who wants to take a stab at
critiquing this formulation?

98:44 So we have the max energy
gain from retrofit.

98:46 For now, assume
it is a constant.

98:48 Right now, it was 0.2 for
C1 and 0 for C3, I think.

98:54 

98:59 And then average energy
intensity of buildings

99:02 is the average for that cohort.

99:05 So what could go wrong
with this formulation?

99:08 

99:18 AUDIENCE: Where is average?

99:20 Where is the output variable?

99:22 HAZHIR RAHMANDAD: Yeah,
let's look at that.

99:24 So the average energy intensity
of buildings is distinct here.

99:30 And then the output of this
average energy intensity

99:34 of buildings
retrofitted is going

99:35 to the indicated total
energy consumption,

99:38 which later brings down the
total energy consumption.

99:43 So what can go wrong here?

99:46 

99:53 To see what can go wrong, let's
run this simulation a little bit

99:58 longer.

99:59 So do we have final time here?

100:02 

100:06 Oh, no.

100:07 

100:11 OK, let hit stop.

100:13 

100:27 OK, so we added a little
bit of investment.

100:30 Actually, quite a
bit of investment.

100:33 And now rather than going to
whatever year we are going,

100:38 let's go a little bit longer.

100:40 

100:50 OK, let's see what
is happening here.

100:55 Average energy efficiency.

100:58 

101:02 Oh, sorry.

101:04 

101:07 So this is 2060.

101:09 So let's make this
between 2050 and 2100

101:20 so that we don't get
weird behaviors here.

101:25 And now if I increase it
to a little bit longer,

101:29 let's see what happens.

101:31 

101:36 Let's actually go
further than 2100.

101:46 2200, OK.

101:58 AUDIENCE: Negative.

101:59 HAZHIR RAHMANDAD: OK.

102:00 So total energy consumption
is going negative actually

102:09 for one of the groups.

102:11 AUDIENCE: The first cohort.

102:12 HAZHIR RAHMANDAD: Yeah.

102:14 And average energy consumption
also going 0 and negative.

102:18 So why is this happening?

102:20 Well, first of all,
why is it going to 0?

102:25 Because Alban put a constraint,
10% or 20% improvement.

102:31 How is it going 90%
improvement and it's still

102:33 continuing improving?

102:37 AUDIENCE: It's a different time.

102:38 90% of that fraction
is being improved.

102:41 HAZHIR RAHMANDAD: Yeah, exactly.

102:43 So this is the problematic
assumption in the formulation

102:49 here, is that the average energy
intensity of buildings that

102:54 are retrofitted is whatever is
this max efficiency gain, or 1

103:00 minus that max efficiency
gain, multiplied

103:03 by current average
energy efficiency.

103:06 So if I brought down
average energy efficiency,

103:09 let's say, from
energy consumption,

103:11 let's call it, intensity, from
1, I brought it down to 0.8.

103:16 It should stop there, but
it doesn't because now

103:19 it is 0.8 multiplied by 0.8.

103:22 Now it can go 0.64.

103:24 And then it is 0.64
multiplied by 0.8.

103:27 And it continues to go down.

103:29 So that's why this can
go down to any number.

103:38 Now, that's number one.

103:41 The second thing is,
why does it go negative?

103:45 AUDIENCE: Because of
the time step maybe.

103:48 It should have been stopped.

103:50 HAZHIR RAHMANDAD:
Yes, so this process

103:53 should have stopped it at 0.

103:57 And therefore a little
bit surprised why this

103:59 is going to negative values.

104:04 So for that, I like
Ali's suggestion

104:08 of looking at the
simulation time step.

104:18 That could be a culprit.

104:21 Looks small enough.

104:23 I'm not sure if that
would explain it.

104:27 AUDIENCE: Isn't the
average going below 0?

104:30 HAZHIR RAHMANDAD: So the average
is going below 0 as well.

104:33 So let's look at this.

104:35 

104:38 You see at the very end, you
get negative numbers here.

104:42 AUDIENCE: For the blue.

104:43 HAZHIR RAHMANDAD: Yes.

104:44 It doesn't matter.

104:45 If you get it for one,
there is a problem.

104:48 So this should not go
negative at any point in time.

104:53 The buildings are there.

104:54 Let's just make sure
the buildings are not

104:56 doing something weird.

104:58 No, the buildings are in
equilibrium, so that's good.

105:00 

105:19 And then energy consumption is
just going out from the stock.

105:29 AUDIENCE: It's probably the
intensity for the new building.

105:36 The red string going down.

105:37 HAZHIR RAHMANDAD:
Ah, it might be.

105:39 It might be.

105:40 Yeah, so if the intensity
for new buildings

105:43 is going to negative values,
then we would have that problem.

105:49 Yes, so that's the reason.

105:51 So that's just
the ramp function.

105:55 So this is not a
formulation issue.

105:57 So this is a good
summary on this one.

106:06 OK, I think, kind of big
picture, the formulations

106:14 that several of you have
for multiple vintages

106:17 and capturing the energy
consumption, those are good.

106:20 That's the basics
you want to have.

106:24 Everybody is missing
kind of the best

106:26 way of formulating the
underlying potential

106:30 for enhancing energy
efficiency, which you should

106:36 do as a separate coflow, as a
separate coflow that tracks what

106:44 is the underlying potential.

106:46 And that can go up and down with
investments in its own sake.

106:52 So that would be
the cleanest way

106:55 to capture all the things
that we want to capture.

106:59 Then, there are two
additional things

107:01 that you can do to
enhance the model.

107:04 One is this way of building
the model with subscripts

107:08 so that you can add more cohorts
or less cohorts, or more or less

107:12 vintages without any problem.

107:14 I'll show you how to do
that in a simple example.

107:19 Second is thinking
through the allocation

107:22 of resources, or whether
it is cost effective

107:25 to invest in energy
efficiency based

107:30 on the parameters of the model
in a more rational formulation.

107:36 That starts to become
more challenging.

107:38 And that wasn't really part of
the problem definition the way

107:42 I set it up, but it's
a nice challenge.

107:45 So those are the two things.

107:47 If I get the chance, I may try
to do something around those,

107:51 but I don't know how much
time I will have for that.

107:55 Let's do, then, one
other thing, and that

107:57 is looking at this
subscript-based way of doing

108:08 cohorts or doing vintages.

108:10 AUDIENCE: I have a question.

108:11 HAZHIR RAHMANDAD: Yes?

108:12 AUDIENCE: Is there a way to
rescue Alvin's formulation

108:16 with the averages?

108:17 HAZHIR RAHMANDAD: Yes,
so that's a good point.

108:19 Sorry.

108:20 Thanks for bringing that up.

108:21 So basically, this
formulation doesn't

108:23 need the effect of this
average intensity of buildings.

108:27 So to rescue the
formulation, the simplest

108:31 is to make the average
intensity of building

108:35 after retrofit a number that
is coming from the underlying

108:39 technology.

108:40 AUDIENCE: And not
anchored to that.

108:42 HAZHIR RAHMANDAD: Not anchored
to the current average energy

108:46 intensity.

108:47 So that would be a
very easy solution.

108:50 You just remove that
multiplication, basically.

108:54 Then, of course, you need
to be unit consistent

108:56 so the efficiency gain
from retrofit cannot be

108:59 dimensionless.

109:00 It then needs to be the
maximum energy efficiency

109:04 or kind of minimum
energy consumption

109:06 feasible for that cohort
or something like that,

109:09 which is what we want to
actually capture in a coflow

109:13 explicitly.

109:14 That's exactly what you would
have in the coflow structure.

109:18 Yeah, other questions
on this one?

109:22 AUDIENCE: I just have a general
question on multiple coflows.

109:26 HAZHIR RAHMANDAD: Yes?

109:28 AUDIENCE: When is a
good place to start?

109:31 Where is a good place to start?

109:32 Because I was
working on a model,

109:35 which I can't remember
how many complex chain,

109:38 maybe like 20 or so.

109:41 And it was just very bizarre.

109:43 HAZHIR RAHMANDAD: So why
did you need 20 different?

109:46 AUDIENCE: I was working
on developing it.

109:50 That was exactly my point.

109:51 How do you reduce the
number of coflows?

109:53 Because it would have
made the model very dense.

109:55 That's grown an aversion
to me in multiple coflows.

109:59 HAZHIR RAHMANDAD: Yes.

110:00 So I haven't actually
seen anything

110:03 with 20 different coflows.

110:05 I have a hard time
seeing the value of it,

110:10 just because it is
very hard to keep

110:13 track of the interactions
in a consistent way.

110:16 That's the core issue.

110:17 That is, you want to
have these dynamic things

110:21 if they're adding value for
the dynamics of the model.

110:24 But if you have 20 features,
then the interaction

110:27 between these features
becomes a big mess.

110:30 You can't really track in your
mind how things are interacting.

110:34 So I would be hesitant
to have that many.

110:37 AUDIENCE: My understanding
from today's discussion

110:41 was when you have two
different characteristics

110:44 of the main chain, which
are inherently different,

110:47 it makes sense to
have multiple coflows.

110:49 Then the question is, when is it
way too many different tracks?

110:52 HAZHIR RAHMANDAD:
So it is really

110:54 the question is, does it
impact the dynamics you really

110:57 want to capture?

110:58 So in this case, the
dynamics we really

111:00 want to capture--
the first-order one

111:02 is the energy efficiency
that has to be there.

111:04 It's kind of or
energy consumption.

111:06 And then the underlying limits
or underlying opportunities

111:12 is also important.

111:13 That is the heart
of retrofitting

111:15 and how far you can retrofit.

111:16 So that's why we include it.

111:18 We are not including coflows
for the color of buildings

111:20 or whatever else.

111:23 There are hundreds
of other dimensions

111:24 you can think about
about buildings.

111:26 What's the height of buildings?

111:29 Yeah.

111:30 AUDIENCE: I guess one signal
that you would need one more

111:33 is, as you're building
this and this average thing

111:37 that Alban has done, which
is attempting to capture

111:40 that effect doesn't work.

111:43 You might be like, OK, there's
some other dynamic attribute

111:46 that needs to be tracked.

111:47 

111:50 HAZHIR RAHMANDAD: Yeah.

111:52 OK.

111:53 Any other questions?

111:56 Let's then take a look at this.

111:58 This is a simple
Vensim model that

112:01 comes with Vensim installation.

112:02 So you can inspect
it yourself as well.

112:04 But let me remove the
subscripts for a second.

112:09 So this is an aging chain model,
age model, whatever you call it,

112:16 that has births and aging,
which aging includes death.

112:22 That simplifies the formulation
for reasons you will see.

112:25 So rather than demolition
in our previous example,

112:29 you could just have aging
to include demolition

112:33 for the buildings.

112:34 Now, let's look at
the formulations here.

112:38 So it is saying for
population, it's

112:45 coming on this other screen.

112:49 So there are two equations.

112:52 For infant group,
their rate of change

112:56 is birth minus aging of infants.

112:59 Very straightforward.

113:02 The trick is in
the next equation.

113:04 So for all but
youngest group, which

113:07 is a collection of all
of the other groups--

113:11 so if you look at
the age elements,

113:17 it has child, teen, middle,
and old as well as infant.

113:21 So the model
includes a subbranch

113:27 which is a subset of the full
range called All But Youngest,

113:33 which includes child,
teen, middle, and old.

113:35 And I'll show you
how to make that.

113:37 It's saying for
all of those guys,

113:40 the formulation is
aging of previous cohort

113:43 minus aging of all but youngest.

113:46 So now you have
another complex thing.

113:48 What is this previous cohort?

113:51 So the previous cohort
is another subrange

113:56 consisting of infant,
child, teen, and middle.

114:01 This is the previous
two All But Youngest.

114:05 So it takes the
previous element.

114:09 So now think about
what Vensim does.

114:11 For every element
of All But Youngest,

114:14 so it starts with
child, it says, OK,

114:18 what is the aging of the
previous cohort's first element.

114:23 The previous cohort's
first element is infant.

114:26 So it looks at the
aging of infant

114:29 as the inflow and aging of
that first element of All

114:33 But Youngest as the outflow.

114:35 Then it goes to
the next element.

114:37 For the teen, it says,
what is the second element

114:42 of previous cohort,
which is child?

114:45 And what is the second
element of All But Youngest,

114:49 which is teen?

114:50 Calculates it and
third and the fourth

114:52 until it ends that subrange.

114:55 That's how it
calculates everything.

114:57 So the logic is simple.

114:59 That's all you need to do.

115:00 But note that you
need two new subranges

115:03 to track what is happening
and to make these movements.

115:09 Now, all of this is fine, except
that these subranges also need

115:14 additional features for them
to work, for Vensim to know

115:18 that these two subranges are
mapping to into each other, that

115:22 is the first element
of the first one,

115:24 and the first element
of the second one

115:27 can work with each other
in the same equation.

115:29 Otherwise, Vensim will give
you an error that you are

115:32 comparing apples and oranges.

115:35 You are trying to mix infants
and children, I don't like that.

115:40 So you have to
instruct Vensim that it

115:42 is legitimate to map the
first element of this subrange

115:46 to the first element of
that subrange, and so on.

115:49 So then you need to do that
within the subscript definition

115:54 thingy, which is usually
somewhere around here.

115:58 

116:05 AUDIENCE: It's in the upper row.

116:07 HAZHIR RAHMANDAD: Yeah?

116:08 AUDIENCE: Yes.

116:10 HAZHIR RAHMANDAD:
Yes, here it is.

116:12 So this is All But Youngest.

116:16 You see when you go
into this definition,

116:19 it highlights these
four elements.

116:22 This is previous cohort.

116:24 It shows the other
four elements.

116:26 The way you define
these is you can

116:29 New a subrange or you
can Edit subranges.

116:35 So I'm going to edit
this subrange so that you

116:37 can see how it is defined.

116:40 So the previous cohort is
defined as infant, child, teen,

116:45 and middle.

116:46 And then this is the critical
piece that is not trivial.

116:50 You need to do it.

116:52 It takes it and says it
maps into All But Youngest.

116:56 That is, there is a one-to-one
mapping from elements of this

117:00 to All But Youngest.

117:02 And you actually need to do
it also for definition of All

117:06 But Youngest.

117:07 

117:10 Oh, actually, it just needs one
of them because in one equation

117:13 it is using one
mapping to the other,

117:16 but not the other
to the first one.

117:18 Kathy?

117:19 AUDIENCE: If you're using
the previous cohort,

117:24 if you're using a
separate age that

117:26 maps onto another
for some reason,

117:27 but you're not using
it in a way that it

117:29 has to map, does that mapping
specification mess that up?

117:34 HAZHIR RAHMANDAD: So
the key to mapping

117:36 is that they should
have the same number.

117:38 Otherwise, it wouldn't work.

117:40 I don't know if it
gives an error or not.

117:43 It probably should.

117:45 AUDIENCE: Yeah, I guess If
you want to use the mapping

117:50 we defined subrange
for something

117:54 separate for some
reason with the fact

117:57 that it maps onto
something, like cause Vensim

118:00 to say that you can't
use it in isolation?

118:04 HAZHIR RAHMANDAD: No, no.

118:05 So mapping doesn't restrict you.

118:07 It just gives you
options that you can use.

118:10 Mapping does not
add any restriction.

118:12 Now, let's see what this does
for you that is valuable.

118:16 So let's say rather than
five groups of population,

118:20 I wanted to have also
another group, oldest.

118:27 So I can just add
in this subrange.

118:30 Oh, actually, I shouldn't
add it in this subrange.

118:32 First, I should add
it in the main range.

118:35 Otherwise, this gets confused
that this subrange includes

118:39 elements that are
not in the range.

118:41 So let me close this.

118:43 I would go into the age.

118:45 I'll do Edit the range.

118:48 

118:50 And I'll add the oldest
here, then close this.

118:56 Then I can go into All But
Youngest, edit subrange,

119:04 add the oldest.

119:08 And then I can go to previous
cohort, edit subrange.

119:15 

119:18 And then what should I add here?

119:21 AUDIENCE: Old.

119:22 HAZHIR RAHMANDAD: Old, exactly.

119:23 

119:28 So now the model should be fine.

119:33 That is, if we run this
model, it just works OK.

119:36 Now we have added another
element to the cohort.

119:38 So that's the basic idea.

119:42 Now, you can do this in
a much more flexible way

119:45 even-- not much more, but
more flexible than this even.

119:49 And the way to do
that would be, I'm

119:51 going to create the subscripts
here without applying it

119:57 to the model so that you just
see how to create subscripts

120:01 that have this characteristic.

120:03 So I'm going to say, I
need a new subscript range.

120:09 So let's call it test.

120:13 And the way I define
it is t1 and tlast.

120:23 

120:29 I'll call it tlastset.

120:30 

120:35 Or actually, let's do it
this way, tmid, tlast.

120:43 

120:49 OK, so now it seems like
it has three elements.

120:54 But in reality, I'm going
to add a lot more elements.

120:59 So then, I'm going to
create a new subrange.

121:04 So let's look at test.

121:06 Right now, test has
only three elements.

121:10 Now I can go and create a new
subrange and call it tmid.

121:14 

121:16 Oh, it is already defined.

121:18 So Vensim doesn't
let me do that.

121:20 So that means I have to first
define tmid then do this.

121:25 So that means I need to kill
the equation for this range

121:31 before I can do that.

121:33 Sorry.

121:34 

121:50 OK.

121:50 I can kill it on this screen,
so I just delete that variable.

121:54 

121:58 And, yes.

122:00 

122:08 Yes, the best software ever.

122:10 

122:14 And somehow it didn't go away.

122:18 I think Vensim is
crashing on us.

122:20 Oh, no.

122:21 

122:25 OK.

122:25 Now it is removed.

122:26 So first we create a
new range, call it tmid.

122:32 

122:38 New Subscript Range, tmid.

122:43 

122:47 And the equation
then comes here.

122:50 Let me bring it to
the other screen.

122:52 So here, I'll just
define it as t2 to t10

123:00 or whatever you want
the range to be.

123:03 So now we have tmid
that includes t2 to t10.

123:08 Now, we define a
new range, test.

123:16 

123:31 It consists of
tfirst, tmid, tlast.

123:37 

123:41 Now you see that
tmid thing went away.

123:45 It's now incorporated into
the test subscript range

123:51 because it saw that,
OK, it consists

123:54 of tmid and other things.

123:56 So now it has all of these
elements built into it.

123:59 Now we can create new subranges.

124:02 So we can have a subrange for
the first until number 10.

124:07 And to do that, we
would say tbefore.

124:11 

124:14 That consists of
tfirst and tmid.

124:19 

124:23 So now tbefore is the first
one until the 10th one.

124:28 And then you do another one
that says tafter, which is tmid,

124:39 tlast.

124:39 

124:44 So tafter is now this subset.

124:47 Now you do your mapping.

124:49 So you can go into
the equation here

124:53 and say this maps into tbefore.

125:01 Oops, sorry.

125:01 

125:05 And in fact, you can
make the mapping two way

125:08 by this sign, which will then
take care of both way mappings.

125:15 So this takes care
of any equation

125:17 that uses one for the other
or the other for the one.

125:22 Oops, maybe it
doesn't like this.

125:26 OK, so if it is not
liking this, then you

125:28 need to do the
mapping separately.

125:31 At some point, it used to be
working that way, but that's OK.

125:35 So now you can do also the same
in the tbefore if you need to.

125:39 So all of this mess
that we did allows

125:43 us to have very
efficient editing

125:47 of all of these
subscripts in one step.

125:51 So now I can go to
subrange, editing tmid,

125:56 and rather than t10,
I will say no, I want

125:58 to have 100 population groups.

126:01 And voila, you have it all.

126:03 And everything is
internally consistent.

126:06 And your model now
goes from 10 subscripts

126:08 to 100 subscripts with
just one small edit.

126:12 So this is a useful
efficiency thing.

126:15 Now, most of your normal
models for this class

126:18 doesn't need any of this.

126:20 I just highlighted
it as a capability

126:22 you will benefit from for
more operational models that

126:27 do need detailed complexity.

126:30 Any questions on this part?

126:31 AUDIENCE: One detail I
just want to deconstruct.

126:33 When you did the mapping, why
was it going into tbefore?

126:40 I lost track of what you showed.

126:42 HAZHIR RAHMANDAD: Yes.

126:43 

126:47 So for the other equations,
in definition of tafter,

126:54 I had it go into tbefore.

126:56 So what does it mean?

126:57 It means that when you are
writing equations for tafter,

127:02 elements of tafter, or
equations that use tafter,

127:05 you can use on the right-hand
side of the equation, things

127:09 that are subscripted
with tbefore.

127:12 So the bearers or the
kind of aging of tbefore

127:19 should come into the
equation for tafter.

127:22 That is why I need that mapping.

127:25 So that's the idea.

127:27 OK.

127:27 

127:30 This is really not in
conceptual, just Vensim tips

127:33 and tricks, but useful for
building more complex models.

127:39 Let's now switch.

127:41 Any questions on the
modeling task for this week?

127:45 I think we actually
haven't quite

127:47 gone through showing
one that has all

127:49 of the characteristics we want.

127:53 Again, if I get the chance,
I'll try to build one.

127:55 But I think we have
discussed the core ideas.

127:59 Let's then switch to
our task for next week.

128:03 

128:15 OK, so next week in exercise
4, what you are going to build

128:22 is a predator-prey model with
carrying capacity for the prey.

128:27 So think about it as
kind of wolf and deer

128:29 model or kind of different
incarnations of this.

128:33 There are different fishes that
one is caught by the other one.

128:36 There is rabbit and fox example.

128:39 You can use your own favorite
or unfavorite animal.

128:42 But this version,
what you want to build

128:47 is also including vegetation.

128:49 That is, the herbivore
is going to need food

128:55 for their own
sustenance and survival.

128:58 It's not that they'll grow
infinitely no matter what.

129:01 So this is a little bit
more complex version

129:04 of the traditional
predator-prey model.

129:09 So let's have a little
bit of a conversation

129:12 around the key architectural
choices for this model

129:15 so that we are aligned on
that as you get started

129:19 working on this for next week.

129:21 This is perhaps less complex in
terms of the detail complexity

129:27 than what we worked
on this week,

129:29 but it is a dynamically
more complex model.

129:34 So going through the testing of
the performance is really key.

129:39 If you don't do the performance
tests and understanding

129:43 of the model, you are
losing a lot of the value

129:46 that this model may generate.

129:48 Of course, you can go online
and find predator-prey models.

129:51 This is one of the oldest
models in mathematical biology,

129:54 going to 1920s, and Lotka and
Volterra independently kind

130:00 of formulated similar
models in the 1920s.

130:03 So it's now known as
Lotka-Volterra model as well.

130:08 Don't go and pick up
other people's models.

130:10 Just build it from scratch and
wrestle with any challenges

130:15 that you may see.

130:16 With that in mind, let's define
a good problem definition.

130:22 So how would you see your model
as a good model in this case?

130:29 Or what's a good problem
rather than the model?

130:33 We'll talk about the
model features later.

130:35 

130:48 AUDIENCE: We could talk
about any challenges

130:52 with the population
of one type of animal

130:54 can be addressed
with this model.

130:57 We have policymakers.

130:58 We have, for example, too many
animal crossings with deers.

131:03 

131:08 HAZHIR RAHMANDAD: Good,
so kind of one policy-type

131:11 of application is we
care about an ecosystem

131:15 and its sustainability, its
effect on the surrounding

131:21 environment.

131:23 It might be side effects of
animals who may act as pests.

131:29 They may eat your crops,
they may create accidents,

131:35 or they may be threats
for your wildlife.

131:38 The question is, you
need to understand

131:41 what this ecosystem is doing
before you can intervene

131:44 in any meaningful way, because
these things are very messy.

131:48 You go and kill the
predator, the whole ecosystem

131:53 may collapse or get into weird
dynamics that will create

131:57 lots of side effects for you.

131:58 So that's the policy
space question.

132:01 Now, for policy
questions like that,

132:05 this would probably be too
simple a model because usually

132:10 you just don't have just two
species that are interacting.

132:13 So then you need to actually
capture the core species

132:17 within the whole ecosystem.

132:19 And that may end up to be a
kind of a predator-prey model

132:24 on a steroid, where you
have multiple species that

132:28 are eating each other or
coexisting with each other,

132:32 eating the same food.

132:34 And so that becomes an extension
of this model for the more

132:39 serious policy applications.

132:41 

132:44 What else might be relevant as a
problem definition for our case?

132:51 The policy one is pretty good.

132:53 It's a good guiding
one, but also more

132:55 complex than what you can handle
in the one week time you have.

132:59 

133:06 AUDIENCE: Build a
model for how can we

133:09 explain oscillatory
patterns of population sizes

133:16 that have the same data.

133:19 But what relationships
give rise to this kind

133:23 of repeated cycle of births?

133:25 HAZHIR RAHMANDAD: Yeah, that's
a good alternative formulation.

133:28 So this is more
reference-mode-based problem

133:32 definition.

133:33 There are good
examples in the data.

133:35 This is actually how, I
don't remember whether it

133:38 was Lotka or Volterra.

133:39 One of them started it.

133:40 It was basically
the fish populations

133:43 in the fisheries
in Atlantic Ocean

133:46 that they were measuring and
seeing these oscillatory modes

133:50 over multiple years.

133:51 And it was very
confusing what is

133:53 happening that creates
oscillations in the fish

133:56 population.

133:57 So that was kind of one
of the major drivers.

134:00 Now, if you focus only on the
oscillatory mode of behavior,

134:04 the way I'm defining
the problem here

134:06 to include the carrying
capacity for the prey

134:09 may not be that relevant.

134:11 That is, down the line, you
would say, why do I even include

134:15 this carrying capacity thingy?

134:19 So that, partly in this case, is
a problem definition more driven

134:25 by mechanisms that
could then generate

134:28 a few different reference modes.

134:30 So oscillations would be one
of those reference modes,

134:33 but perhaps there would
be overshoot and collapse

134:35 possibility perhaps.

134:37 So it is basically expanding
the reference modes

134:43 to include things that may
come from these mechanisms,

134:47 rather than just having
a fixed reference mode

134:49 that we are trying to replicate.

134:52 And that means we are
focusing on mechanisms

134:57 and capturing them well without
adding other mechanisms that

135:02 don't directly help
with this subset

135:08 and seeing what kind of
reference modes come out of it.

135:11 That becomes a more
interesting, relevant exercise

135:15 for our purpose than just
capturing a single reference

135:18 mode.

135:19 AUDIENCE: That
makes sense to me.

135:21 But what I find I struggle
with is articulating

135:24 that as a problem statement.

135:28 So the idea conceptually
makes sense to me,

135:31 But it's not really good
enough to write down

135:33 what other patterns of
behavior might arise from it.

135:36 HAZHIR RAHMANDAD: Absolutely.

135:37 So in that memo also I kind
of discussed these three types

135:40 of problem definitions.

135:42 One is reference-mode driven.

135:44 One is policy-question driven.

135:47 That was closer with
what Hassam said.

135:50 And the third is
mechanism driven.

135:52 That is, you have a
set of mechanisms.

135:54 You want to investigate
what comes out of those

135:58 and only those mechanisms.

136:00 And in this case, we are
saying we have two populations.

136:03 They interact with each other,
one eating the other one.

136:06 That's a core mechanism.

136:08 They have their
deaths and births.

136:10 That's kind of implied in this.

136:12 If you don't have that,
nothing works in this system.

136:16 And then the one that
is being eaten also

136:19 eats some other resource
that regenerates itself.

136:23 That is grass or trees
or shrubs or whatever

136:27 it is, the food for the
deer in this case example.

136:33 So that's the set of
mechanisms that are relevant.

136:37 Now, how to formulate
it in a robust manner?

136:40 That's the primary task.

136:43 And the second task is exploring
what kinds of behaviors

136:47 can come out of this combination
or these set of mechanisms.

136:51 So I think that is the problem
definition close enough

136:55 for what you need.

136:57 What is stocks?

136:59 What do we need?

137:00 What are the sources of inertia?

137:02 And what are good
stock variables?

137:05 Thoughts on that?

137:07 Let's hear from somebody online.

137:09 We have been keeping
you too quiet.

137:13 Anybody wants to take a stab
on identifying the stock

137:18 variables that are relevant?

137:21 AUDIENCE: Predators.

137:22 HAZHIR RAHMANDAD:
Predators, there you go.

137:23 You have one in your hands.

137:25 Excellent.

137:26 So this was a very good
show-and-tell from Jake.

137:32 So predators, for sure.

137:34 Basically, that's the
population that we care about.

137:37 Now there is a question in
the selection of stocks,

137:40 whether we want to
put everybody together

137:43 as a single stock of predator
or perhaps separate them

137:47 based on age groups.

137:51 I am OK with putting
everybody into a single stock.

137:56 That's what the traditional
Lotka-Volterra does.

138:01 Adding age groups
may be relevant

138:04 because it introduces some
additional nuance delays that

138:07 may actually contribute to
more of the oscillatory mode

138:10 of behavior.

138:11 So if you have time or interest,
feel free to explore that.

138:17 But don't go more than two
stock variables per species

138:22 because you don't need that much
resolution in terms of age here.

138:28 So that's good.

138:30 So for predators,
one or maximum two.

138:34 Similar thing for prey,
that's also all you need.

138:38 Anything else?

138:39 Any other stocks?

138:42 Kathy?

138:42 AUDIENCE: I would put something
about vegetation in there.

138:45 HAZHIR RAHMANDAD: Yeah,
something about the vegetation,

138:48 the resource capacity,
carrying capacity for the prey.

138:52 So for that, you could
also use a single stock

138:59 or consider larger number
of stocks, maybe two.

139:03 Again, very much depends on
what reproduction process

139:07 the carrying capacity has.

139:09 So for example, if kind of
trees were the primary source

139:15 of food for the deer, then
breaking down into two

139:20 would make sense.

139:21 Because if you eat
the smaller trees,

139:25 they wouldn't grow
to the age that they

139:28 would be fruitful and so on.

139:31 And that will have some
interesting additional dynamics.

139:35 Again, for your use case,
feel free to go with one.

139:40 Don't go more than two.

139:42 And perhaps start with one
anyway to keep things simple

139:47 for yourself.

139:48 And then if you have time and
interest, explore having more.

139:53 OK, so those are some of
the stock conversations.

140:01 Let's spend the last
few minutes on what

140:07 are the good tests for
performance and robustness

140:10 of the resulting model.

140:11 What are the things that
should happen in the model?

140:17 What are the robustness
conditions you can test?

140:20 What are the key inputs
to change and outputs

140:22 to track for those tests to
be well specified and useful?

140:29 So what are your
thoughts on that?

140:34 I'm happy to write down
your suggestions for tests.

140:41 

140:43 AUDIENCE: This might be kind
of the thing we were just

140:46 talking about of,
can we actually

140:48 create the expected reference
mode behaviors we can

140:53 by introducing shocks that
we think will create them?

140:55 HAZHIR RAHMANDAD: Good.

140:56 Can we recreate the expected
reference modes, e.g.

141:06 oscillations?

141:08 

141:14 What else?

141:15 

141:19 Actually, thinking about inputs
and outputs is also good.

141:22 So what inputs would this
model potentially take?

141:30 AUDIENCE: The reproduction
rate of each species.

141:33 HAZHIR RAHMANDAD: So you
would have various parameters

141:35 that are potential inputs.

141:37 

141:44 AUDIENCE: Initial states.

141:46 HAZHIR RAHMANDAD: And
initial states, yeah.

141:48 

141:55 Good.

141:55 

141:58 So we haven't really introduced
much else in this model.

142:01 This is a very
self-contained model the way

142:04 we have conceptualized
it so far.

142:09 You could consider shocks from,
OK, let's go and hunt the deer

142:15 or hunt the wolf
type of a situation.

142:18 So hunting could very much be
part of your most policy levers,

142:25 but also shocks to the system
if you want to consider that.

142:28 And it kind of makes it closer
to the policy application

142:32 questions you have.

142:33 So hunting of both species
might be useful to consider.

142:42 AUDIENCE: In the same line, you
have changing land application.

142:47 HAZHIR RAHMANDAD: Yes,
changing land availability.

142:52 Good.

142:55 AUDIENCE: What is changing land?

142:56 HAZHIR RAHMANDAD: So basically,
build houses, cut the trees

143:00 and build houses or
something like that.

143:02 AUDIENCE: Yeah, like
environmental encroachment.

143:04 HAZHIR RAHMANDAD:
Environmental encroachment

143:06 would be another relevant
shock to the system.

143:12 AUDIENCE: Should we also
include the area available,

143:15 like the size?

143:16 HAZHIR RAHMANDAD: So
that's a good question.

143:19 If you want to try
this alternative,

143:22 then area becomes another
stock variable rather than

143:27 a parameter.

143:30 Now, you could still deal
with it as a parameter,

143:33 but it is a messier system
to do it as a parameter.

143:38 It might be easier to think
of it as a stock variable

143:41 if you want to go
down that road.

143:44 AUDIENCE: Similar
to hunting, you

143:45 could think about disease
killing one of the populations.

143:49 HAZHIR RAHMANDAD:
Yeah, so basically this

143:50 would be exogenous shocks
that are reducing I think

143:55 this is a good set of inputs.

143:57 So outputs that you want to
track, the obvious one is

144:02 the populations of all
species and carrying capacity

144:18 is a pretty basic
important thing.

144:24 We don't have very
clear policy questions

144:26 so we don't need to
define more KPIs.

144:29 OK.

144:32 Now, other robustness tests,
tests that you would feel

144:41 are worth considering?

144:44 AUDIENCE: The extreme
conditions of the population,

144:47 like if I take out
some of the population.

144:48 HAZHIR RAHMANDAD: Yes,
take out some population.

144:52 

145:01 Good.

145:03 That's a good suggestion.

145:05 AUDIENCE: Compliment is
expanding one population.

145:11 HAZHIR RAHMANDAD:
Yeah, perhaps making

145:14 carrying capacity not a binding
constraint, for example.

145:18 

145:24 You could also consider adding
one of the other species

145:30 at the beginning
of the simulation.

145:32 So that's more playing
with the initial states

145:35 because that's more continuous.

145:37 0 is a qualitatively different
thing for these models.

145:40 

145:45 AUDIENCE: Just a
clarifying question,

145:46 are we thinking we might have
to figure this out on our own?

145:50 Carrying capacity
is a stock variable.

145:56 HAZHIR RAHMANDAD: So you should
decide how it works best.

146:01 But conceptually, it is what
your deer needs to survive.

146:06 So that's what
you need to model.

146:10 Yeah.

146:10 

146:13 And the other general
point for this model

146:18 is, try actually doing it
in more than one iteration.

146:23 That is, don't try
to put everything

146:24 in the first iteration.

146:28 You could even do it
in three iterations.

146:30 That is, build the part for
deer, just the deer population

146:34 in infinite, happy life,
and then introduce the wolf,

146:41 and have the two-species version
without any carrying capacity.

146:45 Then, add the carrying capacity.

146:47 And at every step,
test that your model

146:50 does the right things.

146:52 Make sure you have
inputs and outputs.

146:55 If you wanted, you felt more
comfortable with jumping

146:58 through these, you
can build that deer

147:02 and wolf at the same time,
then add the carrying capacity.

147:07 Make sure your models
are unit consistent.

147:10 Make sure you understand what
is happening in your model.

147:12 So we will probably do
more simulations next time

147:16 on this one.

147:18 OK, I think this is a good
coverage of the key items.

147:23 So, go through iterations--

147:28 deer, then add wolf, then
add carrying capacity.

147:38 

147:41 And that recommendation
is based on where

147:47 you stand modeling-wise.

147:49 This is not a very
complex model.

147:51 So by the end of
this course, you

147:53 may feel comfortable that,
OK, I just bring all of them

147:57 together in one round
and that's fair as well.

148:00 Any questions for
this assignment?

148:05 AUDIENCE: I have question.

148:09 When we talk about
carrying capacity,

148:11 we are talking about what
the deer eats, right?

148:15 So vegetables are what they eat.

148:18 HAZHIR RAHMANDAD: Yes.

148:19 Basically, that's it.

148:20 

148:24 The key thing we are focused
on on carrying capacity

148:26 is food for the deer.

148:28 Now, that food itself is
not a fixed amount that

148:34 is out there in a form
and the deer eat it

148:36 and then everybody goes extinct.

148:39 But it is a rejuvenating
thing on its own.

148:44 It can regrow when it
is not fully eaten.

148:49 So that has dynamics and that
requires a stock variable, as we

148:54 discussed, and perhaps even two
stock variables if you want.

148:59 AUDIENCE: Should we submit
simulations with our models?

149:04 HAZHIR RAHMANDAD: Good question.

149:05 

149:10 Actually, so let's
do it this way.

149:14 So analyze one
interesting scenario.

149:19 And you can pick it from
your final model, whatever

149:23 is your final model.

149:26 Set the parameters so that it
creates the scenario you think

149:29 is interesting.

149:30 It might include oscillations or
some other behavior, overshoot

149:33 and collapse or
something, and analyze it.

149:36 And by analyze it, I mean,
be able to tell the story,

149:40 what structures are
generating that behavior

149:42 at different points in time.

149:45 And come prepared to share that.

149:50 If you get a chance to write
it down and copy and paste

149:54 a few graphs, that's great.

149:56 So that would be good.

149:58 

150:00 Analyze one key behavior
out of the model

150:11 and fully understand it.

150:14 Excellent.

150:16 Anything else?

150:17 

150:20 Online folks?

150:23 OK, great.

150:25 So enjoy your weekend.

150:27 Enjoy, we have something here
happening in a few minutes,

150:30 I guess, some journal club.

150:32 Yep, OK.

150:34 Those online, have a good
rest of your day or night.

150:37 And we'll see you next week.

150:40 

