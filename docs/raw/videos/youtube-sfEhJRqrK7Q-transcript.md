---
title: YouTube Transcript: Session 4: Predator Prey with Carrying Capacity
created: 2026-10-21
updated: 2026-10-21
type: source
domain: ai
classification: general.media
tags: [youtube, transcript, sfEhJRqrK7Q]
sources: []
published: 2026-10-21
time_sensitive: True
---
source_url: https://www.youtube.com/watch?v=sfEhJRqrK7Q
source_type: video
ingested: 2026-10-21
duration_minutes: 147
language: en
sha256: 00ef6bfeb1ebad8af7046200c89896dc644b7714d2d63b3ef96ebee23db65d70
---

# YouTube Transcript: Session 4: Predator Prey with Carrying Capacity

## Video Information
- **Title**: Session 4: Predator Prey with Carrying Capacity
- **Video ID**: sfEhJRqrK7Q
- **Published**: Unknown
- **Views**: Unknown
- **Language**: en

## Transcript
00:00 [SQUEAKING]
[RUSTLING] [CLICKING]

00:09 HAZHIR RAHMANDAD:
Good to see you all.

00:12 We have the predator
prey model today.

00:15 And actually, a lot of
you submitted models.

00:20 So that's great.

00:22 We can jump in.

00:23 

00:26 Actually, so predator prey
model, very, very classic--

00:33 of course, we had a little
bit of an extended version

00:37 to think about carrying capacity
for the prey-- think of a deer

00:42 and wolf model with vegetation.

00:45 And we wanted to focus on
a simple but robust model

00:50 and, to the extent that you
can, think about model analysis

00:54 as well.

00:56 So that was the
problem definition.

00:59 And let me turn off the
light on the presentation.

01:02 That probably helps
with the recording.

01:05 So maybe we can get started
with your reflections

01:12 on things that were challenging.

01:15 That's usually helpful for
focusing the conversation

01:19 on what might be more
useful feedback as we

01:22 go through the models because
we have several models.

01:25 And we may not have time
to cover everything.

01:28 So whoever likes to
share, go ahead and share

01:33 what were some of
your major challenges

01:37 as you were going
through the model.

01:41 STUDENT: [INAUDIBLE]

01:44 

01:50 HAZHIR RAHMANDAD:
So can you tell me

01:51 more what was
challenging with it?

01:53 STUDENT: Yeah.

01:55 So because there are a lot
of behaviors that [INAUDIBLE]

02:02 HAZHIR RAHMANDAD: That's good.

02:03 So what are the behaviors
you were trying to get?

02:06 STUDENT: I wanted
[INAUDIBLE] actually

02:10 be a little bit lower when deer
were less dense and higher when

02:15 they're more dense.

02:17 And they're needs to be a
maximum and minimum consumption

02:27 level that wolves
can actually live

02:28 on that has to do with that.

02:32 And honestly, the
difficulty [INAUDIBLE]

02:36 

02:42 HAZHIR RAHMANDAD: Good.

02:44 I think this might have been one
of the more common challenges,

02:48 not only for predation, but
also for the other side-- that

02:50 is, consumption of vegetation
has a challenge to it.

02:56 Good.

02:57 Other challenges that
anybody faced in modeling?

03:02 STUDENT: The biggest
challenge was

03:04 I was trying to conceptualize
the model based on [INAUDIBLE]

03:09 HAZHIR RAHMANDAD: Yes.

03:09 STUDENT: But then I have
this memory [INAUDIBLE]

03:13 which it didn't go well.

03:14 HAZHIR RAHMANDAD:
OK, very interesting.

03:16 So tell us more.

03:17 So it's interference from the
memory of classical models.

03:27 STUDENT: [INAUDIBLE]
And I'm sorry to say

03:29 that I did the whole model with
a new conceptualization, a more

03:33 realistic conceptualization.

03:35 But then I went back to the
mathematical model [INAUDIBLE]

03:40 what I remembered.

03:41 HAZHIR RAHMANDAD: Yes, yes.

03:43 Yeah?

03:43 STUDENT: So the other challenge
was operationalization, extreme

03:51 conditions.

03:52 If we don't have any deer,
we shouldn't have any wolves.

03:57 And that was also one
of the [INAUDIBLE]

04:00 wolves did not
grow on their own.

04:03 HAZHIR RAHMANDAD: Mm-hmm.

04:04 

04:13 Yeah, good, good.

04:18 Other challenges?

04:20 Jason?

04:22 STUDENT: [INAUDIBLE] I
found it hard to get away

04:30 from the very basic
story of thinking

04:34 in terms of an agent-based model
of deer and wolves interacting.

04:40 And at the end,
what I settled on

04:44 was something that
[INAUDIBLE] you

04:47 don't need to model those
interactions directly.

04:52 HAZHIR RAHMANDAD: So
how does that thinking

04:53 about those interactions
make it more complex for you?

04:56 STUDENT: It distracted from
what is the important features

05:06 [INAUDIBLE] At the end, the
rates that we wanted to compare

05:13 and put together don't
require these more

05:18 microscopic interactions
to think about.

05:22 HAZHIR RAHMANDAD: OK.

05:23 So you were starting with
microscopic interaction

05:25 between deer and wolves.

05:27 And you couldn't get
to any good solution

05:30 for the more aggregate problem.

05:32 Could you get to a good solution
for the individual-based model?

05:35 If you were building an
individual-based model,

05:37 do you think it would
have been easier?

05:39 That's interesting.

05:40 We can come back to that.

05:41 I'm not sure.

05:42 I think, actually, the
individual-based model

05:44 in this case is more complex
than the aggregate one.

05:47 But we can see.

05:49 Any other reactions?

05:51 STUDENT: Well, I just forgot the
time step size was important.

05:54 HAZHIR RAHMANDAD: So how does
the time step play a role?

05:57 STUDENT: I just couldn't
get it to calibrate

05:59 when I set it equal to 1.

06:02 And I needed to set it to 0.25.

06:03 HAZHIR RAHMANDAD:
OK, good point.

06:05 So that's a very general
rule, lesson that time step

06:10 is actually not a construct
that has a conceptual meaning

06:13 in the real world for us.

06:14 Real world is a
continuous world.

06:17 So if the behavior of your model
is sensitive to time step-- that

06:20 is, you change it
and the behavior

06:22 changes-- it means that you
have too big a time step.

06:25 Just bring it down
further, divide it by 2,

06:27 and divide it by 2 until there
is no change in the behavior.

06:30 That's a very simple
heuristic that usually works.

06:34 Oh, Anne, go ahead.

06:36 And somehow, we
are not seeing you.

06:37 I don't know what's
the problem here.

06:40 STUDENT: Are you
sharing the screen?

06:42 I don't think you're
sharing the screen.

06:44 HAZHIR RAHMANDAD: Ah, that
might also be a problem.

06:48 OK, so let's continue.

06:50 Basically, we were
discussing common challenges.

06:52 Anything else that
anybody wants to share on

06:55 what was challenging in this
week's modeling work for them?

07:00 And then we dive deeper.

07:03 STUDENT: I'm just debating
whether [INAUDIBLE].

07:07 

07:14 HAZHIR RAHMANDAD: So that's a
generally an important question,

07:17 whether you go with a single
flow or separate birth and death

07:21 rate.

07:21 And in fact, separate
birth and death rate

07:23 from natural causes
versus natural death

07:26 rate from predation.

07:27 So that's another good question.

07:30 OK, let's look at some of the
models that you have built

07:34 and see how you have handled
some of these complexities.

07:39 So that would require
opening a bunch of models.

07:42 I'll just open the
version B for those of you

07:45 who have submitted two
because we can look at them.

07:51 OK, so this is a good enough
number to get us started with.

07:54 So this one is for Sahin.

07:59 So let's take a look.

08:04 So stocks, we have
the prey population,

08:07 predator population,
and vegetation.

08:09 So I think everybody is
pretty much on the same page

08:14 about that.

08:15 Some of you have broken
it down by two age groups.

08:19 The majority have not,
from a quick look.

08:23 So let's look at one of them.

08:29 And we can see how the ideas
are working for the rest.

08:34 So this is the vegetation side.

08:38 And there is a regeneration
rate for vegetation.

08:42 The regeneration rate, I
think, is fairly common

08:47 and fairly standard to think of
it as a fractional regeneration

08:53 rate, as a first cut.

08:57 So who has used a
similar formulation?

09:00 Basically, the stock multiplied
by a fractional growth rate.

09:05 Anybody has a formulation
that is different

09:07 and wants to share that
or think about that?

09:13 Let's look at your model then.

09:15 STUDENT: I mean, it's not
that much more complicated.

09:17 It basically just creates
the idea [INAUDIBLE]

09:20 HAZHIR RAHMANDAD: Very good.

09:21 So that's actually an important
consideration, if we want to--

09:26 so let's see.

09:28 I think I had your
model somewhere.

09:31 It's just hard to know which
model we are looking at.

09:35 STUDENT: [INAUDIBLE]

09:36 HAZHIR RAHMANDAD: Yeah.

09:36 STUDENT: [INAUDIBLE]

09:40 HAZHIR RAHMANDAD: So here,
you have max vegetation level

09:46 impacting regrowth rates.

09:48 Let's take a look at this.

09:49 So max vegetation minus
vegetation divided by time step

09:52 here.

09:53 So you are basically--

09:57 this is actually a very
different formulation.

09:59 It's not problematic.

10:01 So there are two
different logics

10:03 that you can think
about when you're

10:04 thinking about
regeneration of vegetation.

10:07 One is that you need
seeds that come from that

10:10 vegetation to regenerate.

10:13 The other is that, as
vegetation gets denser,

10:17 it competes with itself for
food, for water, for sunlight.

10:22 And that brings down
its regrowth rate.

10:24 And therefore, it cannot
go above some level.

10:28 So vegetation alone model
without deer and nothing

10:33 should not grow
exponentially forever.

10:36 So this is what Jake's model
accounts for more strongly.

10:41 So this model says, there
is a total vegetation level

10:44 that is feasible to
have in the area.

10:47 Now, here, we don't have
the area explicitly.

10:50 You could have a max density
multiplied by the area

10:53 to give you the max
vegetation level.

10:58 And then you look at that versus
the current level of vegetation.

11:02 And you would say,
vegetation is trying

11:04 to grow back to that level.

11:06 So this formulation does that
alternative conceptualization.

11:10 I would say this is more robust
for the extreme condition

11:16 that we discussed-- that is, the
exponential growth in vegetation

11:19 forever is not going to work.

11:21 It does have a downside.

11:23 And that is, if you are
running out of vegetation,

11:27 the regeneration rate-- and
therefore, the growth rate--

11:30 is actually going to collapse.

11:33 And that is a challenge in
many of the actual ecosystems.

11:37 When you have too
much of the prey,

11:40 basically, deer in this
case, eating the vegetation

11:44 to the bone, then
they don't regenerate.

11:46 And that becomes a bottleneck.

11:48 Whereas, in this model, the
increase in the vegetation

11:51 will be always very robust when
you don't have much vegetation.

11:55 So this is actually a
non-trivial formulation

11:59 to get both of these factors
play a role in your overall rate

12:05 of vegetation.

12:06 STUDENT: Do you
have any preference

12:07 between adding max vegetation
like this versus just having

12:13 two variables that
[INAUDIBLE] what you calculate

12:19 your regeneration [INAUDIBLE]

12:22 

12:29 HAZHIR RAHMANDAD: So I'm not
quite following the two options.

12:32 So one is max regeneration
rate or max total vegetation--

12:36 STUDENT: No, either you take
it into account like this--

12:38 HAZHIR RAHMANDAD: Yes.

12:39 STUDENT: [INAUDIBLE] there's
one maximum amount of--

12:49 maximum amount of--

12:50 HAZHIR RAHMANDAD:
Shipment in that case.

12:52 STUDENT: Or like paperwork
and processing just because

12:54 of how many [INAUDIBLE]

12:58 HAZHIR RAHMANDAD:
So that formulation

12:59 plays a more important
role in the outflows.

13:02 So we will get to the outflows.

13:04 I think, for the
inflow here, we need

13:06 a formulation that actually
brings both of those ideas

13:09 together.

13:11 STUDENT: So we have
been trying this.

13:13 And I think it has a
little bit of downfall

13:16 because, if the max
vegetation is very high--

13:20 imagine it's like here.

13:22 And you have two deer only.

13:24 And suddenly, the inflow
at the very first beginning

13:26 is very large and they grow very
rapidly, whereas, if we like

13:32 multiply it by the
fractional growth--

13:34 HAZHIR RAHMANDAD: Wait, wait.

13:34 This is not for deer.

13:35 This is for vegetation.

13:37 STUDENT: I was just
giving a sensible example.

13:39 But in general, in any species,
if the max level is very high,

13:44 so suddenly the inflow
is very large compared

13:47 to the exponential growth
that it controls [INAUDIBLE]

13:52 HAZHIR RAHMANDAD: Yes.

13:53 And it also partly reflects
whether you are using

13:57 a single flow or double flows.

14:00 That is, in a two-flow
model, you could actually

14:04 have this regeneration
rate being exponential,

14:07 being a direct
multiplier of the stock.

14:13 But then you could have an
outflow that grows significantly

14:18 as you have more density.

14:20 And at some point, it saturates.

14:22 It doesn't allow it to go up.

14:24 So that would be one way to
capture the non-linearity rather

14:30 than putting everything
into the inflow.

14:32 Now, there is some physics
behind it either way

14:36 that you need to capture.

14:37 So one way of thinking
about the physics of it

14:40 is that, OK, the seeds are
spread, but they don't grow.

14:43 They don't even start
to grow because they

14:45 don't have the sunlight and
the water that they need.

14:48 And so as such, the
inflow is disrupted.

14:51 So I need to capture
it in the inflow.

14:53 The other conceptualization
is saying, well,

14:55 the seeds are spread.

14:56 They start to grow, but
they die out very soon.

14:59 So the outflow is much higher.

15:01 You could go with
either of those

15:02 and still have a story to tell.

15:06 Alexander?

15:06 STUDENT: So trying
to capture both,

15:08 I used the logistic
function in the inflow.

15:11 So it has the property
where, if there's little

15:16 then you'll have that
reinforcing loop.

15:18 But then it doesn't go above.

15:19 HAZHIR RAHMANDAD: Yeah,
that's generally a good idea.

15:21 But let's actually
check out your model.

15:24 I don't remember.

15:26 STUDENT: I didn't
include vegetation.

15:28 I just did part A.
But I did it for deer.

15:31 HAZHIR RAHMANDAD: OK,
so we can take a look

15:32 at the model you have for deer
and see how that is playing

15:38 a role in the formulation.

15:42 STUDENT: So I called
it the natural change

15:44 in prey population.

15:45 So that's supposed to
capture-- it's not only births,

15:48 but it's also
supposed to be deaths.

15:50 HAZHIR RAHMANDAD: So this is
really a single flow version,

15:54 net flow version.

15:56 Now, net flow, this model is
simple, but it is not trivial.

16:01 And you will see
that many of you

16:03 had a challenge getting the
inflows and outflows robust.

16:06 So when you combine inflow
and outflow, it is very risky.

16:10 It becomes even
harder because you

16:13 need to keep in mind
what is happening

16:16 both for the inflow and outflow.

16:17 So this is prey multiplied
by their natural birth rate.

16:23 This is the part that is
the positive growth rate.

16:27 And then here, you
have this whole thing

16:33 multiplied by a factor.

16:35 This factor is net
positive as long

16:40 as prey is below its
carrying capacity.

16:44 And once prey exceeds
its carrying capacity,

16:47 that ratio becomes above 1.

16:49 1 minus that ratio
becomes negative.

16:52 Now, you have a net loss rate.

16:56 So this is how Alexander
has formulated it.

17:01 And it works well.

17:03 I think this does OK in
creating a population that

17:07 grows exponentially, gets
to a saturation point,

17:13 and stays there for
a single species

17:17 without influence
from anything else.

17:20 So this is a meaningful,
decent formulation

17:26 if you are doing a single
flow version of it.

17:31 My worry with this
formulation is

17:33 that the mechanics of birth
and death are missing.

17:37 So you don't as
easily tell a story.

17:41 It is more a
mathematical function

17:43 that works OK and gives you
what you want and is perhaps

17:47 equivalent to another model.

17:49 That is, if you had the
model with natural birth

17:54 rate multiplied
by prey as inflow,

17:57 this model would then
have an outflow, which

18:00 is prey to the
power of 2 divided

18:02 by carrying capacity multiplied
by natural birth rate.

18:06 Now, that is not a
very intuitive outflow

18:10 because where does the prey
to the power of 2 come from?

18:13 It comes from a meaningful idea
that too much density leads

18:17 to more killing of the prey.

18:19 So as such, you
can tell a story.

18:23 And mathematically, it works
very nicely because then it

18:26 saturates at carrying capacity.

18:28 

18:30 STUDENT: I spent like 45
minutes on this yesterday.

18:32 If you did the math
if I do the math,

18:34 basically what it is
is it's kind of odd,

18:39 but basically the outflow is
essentially the prey population

18:44 divided by some
reference lifespan--

18:47 so what the lifespan of prey
is at the carrying capacity--

18:50 multiplied by-- I think it's
the ratio of capacity to--

18:57 yeah, multiplied by the
ratio of capacity to prey.

19:01 HAZHIR RAHMANDAD: The prey
should be in the numerator, not

19:03 the denominator.

19:04 STUDENT: As in like prey's
in the numerator, and then

19:08 the denominator, the lifespan.

19:09 It's a first order
draining process.

19:11 HAZHIR RAHMANDAD: Yes, yes.

19:12 It will be a first order.

19:13 So basically, the natural
birth rate of prey

19:17 will be 1 over the
lifespan in that version,

19:21 in the outflow
conceptualization.

19:24 You're right.

19:25 OK.

19:26 So this is one way to do it.

19:27 And it would work
OK in this case.

19:30 And I just forget.

19:32 

19:36 Any other formulations for
vegetation growth rate?

19:43 STUDENT: [INAUDIBLE]
I have one mistake.

19:46 But I only did it
for the inflow.

19:49 So I realized that's
wrong [INAUDIBLE]

19:53 HAZHIR RAHMANDAD: OK, so let's
take a look at your model

19:56 to see what we had.

19:59 

20:07 So this is the
carrying capacity.

20:09 And your vegetation growth
has a max vegetation

20:13 and vegetation growth rate.

20:17 STUDENT: It shouldn't be growth
rate times max vegetation,

20:19 but just max vegetation.

20:21 HAZHIR RAHMANDAD: Yes.

20:22 So if you remove this max
vegetation multiplication,

20:25 because that one
doesn't actually work,

20:29 then you have
vegetation growth rate--

20:36 so this has units problems
as well or maybe not.

20:43 So if the growth
rate is one per year

20:45 and you have max
vegetation, then the units

20:48 will be fine because the
second part is dimensionless.

20:54 

20:58 STUDENT: Yeah, that should
be just the vegetation.

21:00 HAZHIR RAHMANDAD: So it
should be the vegetation,

21:02 if you want to-- yeah.

21:03 And if you make it
vegetation, then it

21:05 becomes very similar to the
formulation that Alexander had.

21:09 STUDENT: But then
it's wrong still.

21:11 I mean, based on
what you're saying,

21:13 it's still wrong because
then it can go negative.

21:16 HAZHIR RAHMANDAD: So
this can go negative.

21:19 So if you don't have--

21:20 

21:23 I mean, I don't know where--
oh, this is the stock,

21:26 your carrying capacity.

21:28 So it is not going
to go negative,

21:31 if you don't have
any other inflows.

21:33 So if this is the only
inflow to the stock,

21:36 the stock will grow until it
reaches the max vegetation.

21:41 But as soon as it reaches max
vegetation, this will shut off.

21:46 It becomes 0.

21:47 And therefore, it cannot go
above that max vegetation.

21:51 In fact, even if it goes
above max vegetation,

21:53 this becomes an outflow
for the vegetation.

21:55 It kills vegetation and, as
such, brings it back to the max.

22:00 So it is not
problematic, in the sense

22:02 of going negative, if you
think of it as a two-way flow,

22:06 not as a one-way flow.

22:08 STUDENT: Yeah, that's what I
meant, that it can only work

22:10 if it's a net flow [INAUDIBLE]

22:14 HAZHIR RAHMANDAD: Yes.

22:15 But as an inflow, it is
still doing an OK job

22:18 because here you
have the consumption

22:21 of vegetation by deer.

22:23 You don't have the natural
death of vegetation

22:27 as the grass gets dry
and dies after a while.

22:31 So that part is actually
already built into here.

22:36 So it is a two-way flow
in your model as well.

22:39 OK.

22:40 So you got an idea.

22:43 So basically, yes,
exponential growth type

22:47 with only vegetation multiplied
by a natural growth rate

22:52 is a possibility.

22:54 But the possibility has the
downside of becoming too strong.

22:59 So you do want to think about
the impact of carrying capacity

23:04 of the land for vegetation.

23:08 One way to do it is similar
to what Alexander did,

23:11 which made me think of
it as a two-way flow.

23:15 Another is to have, basically,
a consumption or a natural death

23:24 rate of vegetation that
will grow as vegetation

23:29 becomes denser.

23:31 You need to have
one of those two.

23:32 And because we have the
same story with the deer,

23:35 we can go through
the formulations

23:36 in the deer population
and, in fact,

23:38 with the wolves, that will
give more info on how you

23:44 have been thinking about it.

23:46 So let's go back to--

23:51 

23:53 oh, we can go to any
of the models for--

23:57 let's just pick another one.

24:00 So this one this is Alisa.

24:03 OK, so Ali has just simple
names-- n0, n1, n2--

24:13 which I suspect this is--

24:17 this is the wolf, predator.

24:19 And then you have the deer
as n1 and n2 being the grass.

24:24 So here, you have
the death rate that

24:27 is coming from the--
the birth rate that is

24:30 coming from just regeneration.

24:32 And then you have the
death rate that is--

24:36 let's look at this equation.

24:38 So I'm a little bit-- so
just looking at this graph,

24:41 I can't follow what the logic of
that equation is because there

24:45 are four, five different--

24:48 six arrows going
into that equation.

24:50 So the logic will be complex.

24:53 You are combining six different
things into a single flow.

24:56 Not a good idea.

24:57 Break down the logic.

24:58 It's clearer for
anybody to look at it,

25:00 but also will be clearer
for you because you can then

25:04 open up each of those pathways
and see how it is impacting

25:08 your overall flow variable.

25:10 So that's just a
simple process thing.

25:13 Don't drop in 100
things together.

25:16 Now, we have n2--
that is the grass--

25:20 multiplied by its natural
fractional death rate

25:26 plus n2 divided by normal n.

25:32 What is normal n?

25:33 STUDENT: It's a unit correction.

25:34 HAZHIR RAHMANDAD: OK.

25:35 So unit corrections are
risky things to use.

25:39 That is, if you're just adding
something to fix your units,

25:43 it means you're in trouble.

25:45 Your logic is not working well.

25:47 Almost always, there is a
way to fix the units based

25:51 on the mechanisms rather than
adding just ad hoc parameters.

25:56 So think of those as fault
factors you shouldn't use.

25:59 There are situations-- like,
if you're raising something

26:01 to a power in Vensim, it
gives you an error no matter

26:04 what, if you have a
unit for that element,

26:09 and then you want to make it
dimensionless to not get it.

26:15 So there are very rare cases
you need fudge factors,

26:17 but don't use them.

26:20 But this is ultimately some--

26:22 maybe even a value of 1.

26:24 But you have the grass
multiplied by grass carrying

26:30 capacity.

26:32 And then this
thing is multiplied

26:34 by grass itself, ultimately.

26:39 So I'm not following that logic.

26:41 Can you tell what it is?

26:42 STUDENT: The first thing
that you pointed out

26:44 is natural death rate.

26:45 Second one is kind of
like a carrying capacity

26:49 if they reach a limit.

26:51 So it slows--

26:54 HAZHIR RAHMANDAD:
It slows it further?

26:56 STUDENT: Yes, it slows it
further, and then kills grass.

26:58 HAZHIR RAHMANDAD: But
why is it multiplied

27:00 by carrying capacity n2?

27:03 STUDENT: I was thinking
of a factor that--

27:07 HAZHIR RAHMANDAD: Yes, but
don't think about factors

27:09 in this abstract way.

27:11 Factors can be any number,
any mathematical number.

27:14 And then you have
infinite possibilities.

27:16 And you can't narrow down
into something meaningful.

27:20 So actually, carrying capacity
is a meaningful concept.

27:23 So if you have n2 divided by
carrying capacity of n2-- that

27:27 is, the total grass that
possible-- that ratio

27:32 becomes basically how close
you are to carrying capacity.

27:36 And then you are saying, as we
get closer to that ratio of 1,

27:43 then the natural death rate goes
up and, in this case, linearly.

27:48 So it can become double--

27:51 well, not double.

27:54 Then it has to be multiplied
by some fractional--

27:59 STUDENT: Right.

28:00 [INAUDIBLE] same as the
fractional death rate.

28:03 That's why I did
multiplication communication.

28:05 HAZHIR RAHMANDAD: OK.

28:06 And then you have ny divided
by normal n multiplied

28:09 by impact of predator n1.

28:12 So basically, you
are looking here

28:15 at the deer eating the grass.

28:21 But you're multiplying
that by n2.

28:24 Why is that?

28:26 STUDENT: So here's the thing.

28:29 If we don't have any grass,
we shouldn't have any outflow.

28:34 HAZHIR RAHMANDAD: Very good.

28:35 So everybody has had a
version of this thinking,

28:38 I think, most of you
have been thinking.

28:41 And then the way you have
implemented-- many of you--

28:43 I had a very quick look
at some of the models--

28:45 was this idea that you
multiply by the grass

28:49 so that you capture the fact
that, if you don't have grass,

28:53 the consumption of
grass should go down,

28:57 which goes up to some
point to address that need.

29:02 But what kind of
a problem does it

29:03 create, if you just multiply the
grass, in this case, by the deer

29:12 by some constant as
the outflow, which is

29:15 what this formulation is doing?

29:17 Katherine?

29:17 STUDENT: It doesn't account for
the appetite being constrained.

29:21 So if you have infinite
grass, then the deer

29:23 are going to be eating
so much grass [INAUDIBLE]

29:26 HAZHIR RAHMANDAD:
Yes, very good.

29:28 So that's a very big
robustness problem.

29:30 And it's not really just
a robustness problem.

29:32 It is really the
physics is gotten wrong.

29:35 If you have infinite
grass and one deer,

29:38 that single deer will be
consuming infinite grass.

29:41 That is not going to happen.

29:43 So there is a serious
constraint on how much

29:48 grass can be
consumed by the deer

29:51 that this type of multiplicative
constraint does not address.

29:57 Does that make sense?

30:00 So let's actually look at that
in a few other formulations,

30:03 because this is really at
the heart of the tougher

30:05 formulations in this model.

30:09 So let's look at some
other random models.

30:12 

30:16 Whose is this one?

30:17 This is Oriana's.

30:18 

30:23 So this is the vegetation.

30:25 And you have--

30:27 STUDENT: [INAUDIBLE]

30:30 HAZHIR RAHMANDAD: Yeah, we could
go and look at the prey one.

30:33 So you can see that the logic
is actually very similar.

30:35 So you can look at either
of the prey or vegetation.

30:40 And the underlying structure
shouldn't be that different.

30:46 So here, the version
you have is prey--

30:51 STUDENT: This is
like the prey that

30:52 died because of the predators.

30:54 HAZHIR RAHMANDAD: Yes, yes.

30:56 And then the prey
predator death rate is--

31:00 yes?

31:01 STUDENT: [INAUDIBLE]

31:03 

31:06 HAZHIR RAHMANDAD: It depends on
the predator and prey required

31:12 per prey per day--

31:15 predator per day.

31:16 So this is the constraint that
Kathy mentioned that, OK, you

31:21 want to have some amount
of consumption based

31:25 on how many predators you have.

31:27 So this is a good indicator.

31:29 This is the desired consumption
of prey by the predator.

31:35 So far so good.

31:36 But in the next part
when you multiply that

31:39 by the prey population,
you get two problems.

31:43 First of all, you get the
same equation that Ali had.

31:47 Basically, it is the
equivalent equation.

31:50 The second problem
is a unit problem.

31:52 So what is the unit problem?

31:56 This should be in deer per
wolf per day or per month

32:01 or whatever is the unit.

32:03 Multiplied by the wolf,
it becomes deer per month.

32:07 Now, it is in the
right unit for outflow.

32:10 You multiply that by the deer.

32:13 You would not get the
right unit as well.

32:16 So that's the challenge.

32:17 And it probably shows
up in the units as well.

32:20 OK, let's look at some
more formulations.

32:25 I think-- let's see if we
have any of the folks online

32:31 their models we can check out.

32:34 Let's look at Gerardo's model.

32:37 So Gerardo has two
stocks for each of the--

32:42 or at least-- yes, for these two
groups and also for vegetation.

32:47 Two stocks are fine.

32:48 Nothing wrong about it.

32:50 It adds to your headache for
keeping track of the fact

32:54 that, OK, yes, the baby
prey could be eaten as well.

33:00 So do you want to
capture that or not?

33:03 They are actually easy prey.

33:06 And so in this version,
that is not captured.

33:12 So for now, let's assume
this is not a problem.

33:16 Let's not worry about the
baby prey and their fate.

33:20 Assume they all
grow to maturity.

33:27 And if you make that assumption,
this average maturity time

33:29 works fine.

33:31 Now, we have starving.

33:35 We have death rate from average
prey lifetime and eaten prey,

33:43 which is from the predators.

33:51 So this is an
interesting question.

33:54 Do we need all of
the three pathways?

33:57 Or do we need fewer?

34:00 So I like to have two,
separating the hunting

34:06 and harvesting
from natural death.

34:11 The separation between natural
deaths and starving death

34:16 is harder to pin down.

34:20 It feels to me they are
too close to each other.

34:27 But sometimes, it
may be helpful.

34:30 

34:33 OK.

34:33 For now, let's
focus on the eaten

34:35 prey because those
two-- that adds

34:37 another layer of complexity.

34:41 So eaten prey in
Gerardo's equation

34:47 is based on desired
prey-- desired

34:50 prey are coming from predators.

34:53 So this is the same
equation that Oriana also

34:56 had, predators multiplied by
their average consumption.

35:00 This is the desired.

35:01 That's good.

35:02 This is what we want to have.

35:05 Then let's go to the equation.

35:09 This looks more complex now.

35:11 So this is max of 0 and
minimum of desired prey

35:17 versus prey divided by
feasible time to eat the prey.

35:22 So is the logic clear?

35:27 

35:31 Who wants to take a stab at
explaining this logic, what's

35:34 happening here?

35:35 

35:43 STUDENT: [INAUDIBLE]

35:46 

35:48 HAZHIR RAHMANDAD: So
basically, the max of 0

35:50 is saying it
shouldn't go negative.

35:54 Now, this should not
go negative anyway.

35:57 So this is another kind of a
stylistic idea to keep in mind.

36:01 That is, the second part of
the equation should be robust.

36:05 It should not go
negative no matter what.

36:07 Putting this max
0 does two things

36:10 that are not necessarily good.

36:12 One is that it makes your
equation a bit too complex.

36:15 So when I'm looking
at it, I have

36:16 to process that and
make sense of it.

36:18 The second thing is that,
for whatever reason,

36:21 if your other equations
lead to a negative value

36:24 because they were not
correctly formulated,

36:26 this hides that error.

36:28 So you actually don't
want to add these max

36:31 0 thingies everywhere.

36:34 As long as you have
taught through why

36:36 the equation shouldn't
go negative, let

36:40 the equation do its work.

36:41 Don't add another
layer of protection.

36:44 OK, so simpler solution
would be just the minimum.

36:49 So now, this
minimum, it is either

36:53 what the prey wants
to eat or what the--

36:58 sorry, what the
predators want to eat

37:01 or what the prey can offer.

37:03 And that's what
the prey can offer.

37:05 Here, it's formulated
very simply as number

37:09 of prey divided by the minimum
time to harvest or something--

37:16 that is, minimum time
to find prey to eat

37:18 or something like that.

37:20 This is actually a
pretty good formulation.

37:22 This is a good starting point.

37:24 This is perhaps the simplest
formulation you can use.

37:30 So if you want-- anybody who has
a critique for this formulation?

37:35 Alexander?

37:36 STUDENT: So just the Min
creates this sharp behavior.

37:41 And so this is
essentially the same

37:42 as the shipment formulation.

37:45 And so for that, you typically
use a soft [INAUDIBLE]

37:52 HAZHIR RAHMANDAD: So the
critique that Alexander said

37:55 is that this creates a very
discontinuous behavior.

37:58 That is, as long as pray divided
by feasible time to eat prey

38:02 is even slightly above
desired prey rate,

38:08 then you get the desired.

38:11 Whereas in reality, in
nature, preying on prey

38:17 is kind of a very
engaging task that

38:21 very much depends on the
density of the population.

38:24 So it is not that it
is hard to get it,

38:28 and then it becomes
completely abundant.

38:33 So abundance emerges
more continuously.

38:36 So that softmax, which we have
different ways of formulating

38:40 it, could be useful.

38:42 Is that clear, the core idea?

38:44 But this is a better
formulation than the other ones

38:48 we have seen because it
doesn't have the problem that,

38:50 now, if we have infinite
prey, the consumption of prey

38:56 by a single predator
goes to infinity.

38:58 It would not happen.

39:01 STUDENT: I was wondering if
you do not [INAUDIBLE] Does

39:14 that resolve some
of your issues?

39:16 I know, fundamentally, I guess
the infectivity model isn't

39:20 the same as prey
eating, but you can

39:22 imagine the prey
going from alive

39:25 to the stomachs of predators.

39:26 It's like their contact
frequency is how often they

39:29 see each other [INAUDIBLE]

39:31 

39:33 HAZHIR RAHMANDAD: Yes.

39:34 So the part that
physically distracts

39:38 from that conceptualization
is that you

39:42 see all these lions seeing
all deer around them,

39:45 but they are not
hungry at the time.

39:47 So they don't go and eat them.

39:49 That's the part.

39:50 Whereas the virus says,
oh, if there is somebody,

39:53 I'll catch them.

39:55 It doesn't wait for you.

39:57 It doesn't have any satiation.

39:59 So the satiation is not captured
in the Bass diffusion model.

40:03 And that makes it not
a good formulation.

40:06 STUDENT: What about
the fact that there

40:07 are different populations?

40:08 Because in Bass diffusion,
it's one population just

40:12 changing states.

40:12 But these are different
[? kind of things. ?]

40:15 HAZHIR RAHMANDAD: Yeah, so--

40:16 STUDENT: [INAUDIBLE]

40:19 HAZHIR RAHMANDAD: So if you
had a kind of an animal that

40:25 was just into killing their prey
regardless of their hunger--

40:30 STUDENT: [INAUDIBLE]

40:31 HAZHIR RAHMANDAD:
Yeah, so like humans

40:33 going and shooting animals
without eating them, then

40:36 you get closer to a
multiplicative function

40:40 that, as soon as you
have an interaction,

40:43 an interaction comes with the
multiplication of the density

40:46 of the two species.

40:48 So in that sense, it gets
closer to Bass diffusion

40:51 or to that multiplying
the two populations.

40:54 Now, it is not a Bass diffusion
model because of what you said.

40:58 It's two different species.

41:00 But the rate of decline for
one is a function of both.

41:04 That's the idea.

41:05 STUDENT: So I didn't do
this, but something--

41:09 I didn't do this formulation.

41:10 But something I was
thinking about a lot

41:12 was something about the
effectiveness of predators.

41:15 Maybe they're really bad at
hunting or something like that.

41:18 How would this
formulation capture that?

41:20 Or how would you include that?

41:21 HAZHIR RAHMANDAD:
The effectiveness

41:22 of the predators in hunting?

41:26 STUDENT: Yeah.

41:27 HAZHIR RAHMANDAD: So they
have a desired consumption.

41:30 But then there is
a separate concept

41:31 that you are saying is about
their effectiveness that

41:35 may bound how much
they can consume.

41:39 So that, basically, would
come in this formulation

41:43 from that softmax.

41:44 The current one that Gerardo
has wouldn't capture it.

41:47 But a softmax formulation
would say, OK,

41:52 you can grow your consumption.

41:58 But even if you have quite
a bit of prey around,

42:03 you don't get to
your desired level.

42:05 You need to have a
huge amount of prey

42:08 to be able to get to
your desired level.

42:11 Actually, maybe I
should-- give me a second.

42:15 Let's see if it works.

42:19 Let's say here we have
the max consumption

42:32 possible from how many deer
you have divided by desired.

42:41 

42:45 It's very hard to do this by
hand, but that's what it is.

42:50 And here is basically what
fraction of the desired you

42:56 get to consume.

43:01 So what Gerard has is,
at the point 1 and 1,

43:12 we go the 45 degree
line up to here.

43:16 And from this point on,
it's just a straight line.

43:20 So this is Gerardo's equation.

43:23 Now, Alexander's point
was that you need a softer

43:34 approach towards the end.

43:37 So this becomes the alternative,
that you have the softmax.

43:43 And then the point that
I was making, in response

43:46 to Alexander's other
comment about efficiency

43:49 of predator in prey is that
the slope of this curve

43:55 could be different.

43:56 So you could have this curve.

43:57 Or you may have something
that more looks like this.

44:00 Oops, it goes down--
goes up like this.

44:03 So the less efficient
predators are

44:06 suffering unless there is a
lot more prey in the landscape.

44:11 So that's one way to capture
it, not the only way.

44:16 OK.

44:18 Do we have--

44:19 STUDENT: [INAUDIBLE]

44:20 HAZHIR RAHMANDAD: What do
you mean as an alternative

44:22 to the mean formulation?

44:24 I used a lot of--

44:25 I don't know a
better alternative.

44:26 Practically, we use
a lookup function.

44:28 OK, great.

44:29 So let's actually-- then this
is very much aligned with what

44:31 we are right now discussing.

44:33 So how can you
solve this problem?

44:37 There are two general ways--
analytical functions or table

44:44 functions.

44:45 Table function is
pretty straightforward.

44:47 You have this max
divided by desired

44:50 as the input to
your table function.

44:53 And you get the
shape that you want.

44:54 You plug it in.

44:56 That's nice and clean.

44:58 System dynamicists are
comfortable with it.

45:01 Outside of system dynamics,
people would say, what's that?

45:05 That's too many
degrees of freedom.

45:06 That's confusing.

45:07 I can't follow it.

45:08 Give me an equation.

45:10 So then you need to have at
least an analytical alternative

45:15 for other types of audiences.

45:18 So anybody has a
feel for how you

45:21 can get the flexibility
for these different curves

45:26 with an analytical function that
does all of the things we want?

45:30 Jason, what would
be your suggestion?

45:31 STUDENT: The one I
landed on was input

45:36 divided by 1 plus the input.

45:39 To get flexibility, you could
raise that whole quotient

45:42 to some exponential
power [INAUDIBLE]

45:45 HAZHIR RAHMANDAD: OK.

45:46 So let's call this
x for simplicity.

45:49 STUDENT: So it's x plus
1 over-- or x over--

45:51 HAZHIR RAHMANDAD: So
your formulation is x--

45:55 STUDENT: Divided by 1 plus x.

45:57 HAZHIR RAHMANDAD:
Divided by $1 plus x.

45:59 STUDENT: Right, because
it gives you the property

46:01 that when x is 0 you get the 0,
0 because the numerator is 0.

46:08 HAZHIR RAHMANDAD: OK.

46:09 STUDENT: And then
it will approach--

46:11 HAZHIR RAHMANDAD:
It would approach 1.

46:13 STUDENT: It approaches
1 as x goes to infinity.

46:15 HAZHIR RAHMANDAD: OK.

46:17 STUDENT: The problem is it's
kind of a slow approach to--

46:20 HAZHIR RAHMANDAD: Yes.

46:21 STUDENT: So you
could speed that up.

46:24 HAZHIR RAHMANDAD: Yes.

46:25 STUDENT: Speed that up
by putting an exponent

46:28 around the whole thing.

46:30 HAZHIR RAHMANDAD: So you raise
this to some larger power?

46:33 STUDENT: Yeah.

46:33 HAZHIR RAHMANDAD: OK.

46:34 Are you following?

46:35 This is exactly the type
of thinking you want to do.

46:38 That is, OK, I want something
that starts from 0, goes to 1.

46:42 x over 1 plus x does that.

46:44 So that's nice.

46:45 But then it doesn't
approach fast enough.

46:47 And it doesn't have any
degrees of freedom right now.

46:49 You don't have any parameter
associated with it.

46:52 So you can't get different
saturation speeds.

46:56 So this is not yet doing well.

46:57 So now, Jason's
next step was, oh,

46:59 maybe we can do this, raise
this to the power of alpha.

47:02 

47:06 And then that perhaps
gives us something

47:11 a little bit more flexible.

47:15 Remember that, between 0 and
1, x values between 0 and 1

47:20 is a very active
region for this input.

47:24 So you want a formulation
that works in that region.

47:27 So if you have, let's
say, close to 1--

47:33 so if you get 1,
in this case, this

47:35 becomes 0.5 raised to
the power of alpha.

47:40 Well, it is important.

47:43 So if it is 0.5, what
do you want it to be?

47:50 Do you want it to
go above 0.5 or do

47:52 you want it to go below 0.5?

47:54 

47:57 STUDENT: You want
it to be below.

47:59 HAZHIR RAHMANDAD: Yes,
because if it is above 0.5,

48:01 it is going to violate
another constraint here,

48:05 that you cannot exceed the y
equals x line because the y

48:13 equals x line-- that is, the
output equals the input--

48:17 means your max
divided by desired--

48:25 that is what you
get out of this--

48:27 will need to be
multiplied by the desired.

48:30 So if it is y equals x line,
then max divided by desired

48:39 is going to be multiplied
by the desired.

48:43 This gives you the max.

48:45 Now, any value above one above
x equals y-- if this is y,

48:50 this is our output--

48:54 STUDENT: Would give
you more than desired.

48:55 HAZHIR RAHMANDAD: This
will lead to more than max,

48:58 not more than desired.

48:59 So this is the problem.

49:01 So if you call this
thing y, then you

49:05 are going to multiply
y by the desired.

49:09 

49:13 And if you multiply
y by the desired--

49:16 let's, for a second, think of
a situation where y equals x.

49:22 And what is x?

49:24 We see it on the right-hand
side of the screen.

49:27 It is max over desired.

49:31 So that means these two lead
to max over desired multiplied

49:38 by desired is the total.

49:42 Let's call this z.

49:44 This is the consumption.

49:48 So that means the consumption
will be equal to what?

49:55 Max.

49:55 

50:00 So this is saying that whatever
is the output of this function

50:11 should not go over
the line y equals x.

50:18 So that's another
constraint that we have,

50:20 which we didn't think about
before this, for making

50:25 a robust formulation.

50:27 STUDENT: That is
where the constraint

50:28 comes from this [INAUDIBLE].

50:31 HAZHIR RAHMANDAD: Yes.

50:33 STUDENT: [INAUDIBLE]

50:36 HAZHIR RAHMANDAD: 0.5.

50:37 So I said, if x is 0.5, x
divided by 1 plus x-- oh sorry,

50:43 if x is 1--

50:44 STUDENT: [INAUDIBLE]

50:45 HAZHIR RAHMANDAD: It's 0.5, yes.

50:47 So it is below.

50:50 So it is fine for that one.

50:52 You're right.

50:53 STUDENT: Right.

50:54 The problem is, though, if
you want anything stronger,

50:56 you wind up with stuff above it.

50:58 HAZHIR RAHMANDAD: At some
point, it could go above.

51:01 That is, at the very
beginning, at the slope

51:05 of-- at the starting
point, the slope

51:10 is right now x at
the very beginning.

51:15 And so that gives a 45-degree
line at the beginning.

51:20 So this, without alpha, will
never go above 45-degree line.

51:24 But as soon as you add alphas
that are below 1, for example,

51:30 to go up faster, then it goes
above the 45-degree line.

51:35 So that's not a big problem.

51:38 You can solve that.

51:40 And the way to solve that--
so actually, first of all,

51:42 you need alphas that are smaller
than 1 for a sharper increase

51:50 because that gets you
closer to 1 more quickly.

51:53 And then you can have,
basically, the minimum of x--

52:03 

52:05 this is y equals x
and this function

52:11 that you just came up with,
so x divided by 1 plus x

52:26 to the power of alpha.

52:28 This does the job OK.

52:31 STUDENT: But it still
has some pretty sharp--

52:34 or it will have
some point where--

52:35 HAZHIR RAHMANDAD: Yes, there
will be a discontinuity.

52:38 STUDENT: There will
be a kink in there.

52:38 HAZHIR RAHMANDAD: There
will be a kink, yes.

52:40 And actually, it is not
very easy to come up

52:43 with a formulation that
doesn't have the kink.

52:45 You can, but you basically
need to build a much more

52:50 complex formulation.

52:51 So this is one version.

52:52 You could do other ones.

52:54 So you could use an exponential
approach to the line rather than

53:00 this polynomial approach.

53:02 So if you want to do the
exponential approach,

53:04 you still need the mean
of x and something.

53:08 But that something
could be 1 minus e

53:14 to the power of minus alpha x.

53:24 So if x is a large
number, 1 minus e

53:27 to the power of minus
alpha x becomes--

53:31 

53:35 STUDENT: [INAUDIBLE]

53:36 HAZHIR RAHMANDAD: If x is
a large number-- that is,

53:38 we are on the right-hand
side of this graph--

53:41 this e to the power of
minus something becomes 0.

53:45 And therefore, you
get to 1 as the total.

53:49 So you're exponentially
getting close to that.

53:52 You're approaching that curve.

53:53 So that's an alternative.

53:54 I'm not sure which
one is better.

53:56 To see which one is
better, you actually

53:57 need to graph them for
different values of alpha

54:00 and see which ones are
qualitatively closer to what

54:02 you want.

54:03 Alexander?

54:04 STUDENT: So I mean,
if you were going

54:06 to have a kink in this
anyway no matter what,

54:08 why not just do
what Gerardo did?

54:10 HAZHIR RAHMANDAD: Because
this gives you the flexibility

54:13 to capture the other factor
that you talked about,

54:17 which is important in this case.

54:20 So that's, I would
say, the primary thing.

54:23 And the other thing is
that it doesn't completely

54:26 remove the effect.

54:28 It just changes the
speed of the effect,

54:31 whereas the min function
completely removes the effect.

54:34 It has two very
different regions.

54:37 So it shuts off
some feedback loop,

54:41 whereas this version leaves the
feedback loop on, but weakens it

54:45 over time.

54:45 So as such, the kink
is not as strong.

54:48 The impact is not as strong.

54:50 STUDENT: More of a
process question--

54:53 I can see where you would come
up with this if you're starting

54:56 from the point of
I'm going [INAUDIBLE]

55:02 But if you start from the
point of hunting effectiveness

55:06 [INAUDIBLE] it takes a while
to land here on your own.

55:11 HAZHIR RAHMANDAD: So I
think the logic to get

55:15 gets you here very quickly
is I have predators,

55:19 they want to eat prey,
they have a desired value.

55:23 So that is the driver.

55:24 That's like the demand
in an inventory model.

55:28 But then if I don't
have enough prey,

55:31 I need to bring down their
ability, their fulfillment

55:34 ratio, their ability to
get the prey they want.

55:37 So I just need a
formulation to capture that.

55:40 That's the fast route to
get to close to this step.

55:45 Then you need to go back
into your memory of, OK,

55:49 what are the ways to capture
these consumption of something

55:53 out of a stock that is satiated
on the one hand by the demand

55:58 and on the other hand by the
availability of the stock.

56:00 And that's where, if you
remember your assignment 6

56:04 from 873, you would be able to
do that fairly straightforward

56:11 using that formulation.

56:12 STUDENT: So you start
from the story design.

56:15 HAZHIR RAHMANDAD: Yes.

56:15 Hassan?

56:18 STUDENT: Can we use
a second [INAUDIBLE]?

56:21 Then for that formulation,
we actually know

56:24 where the alpha is that
will create [INAUDIBLE]

56:27 So we can limit the alpha
so that it will never

56:29 pass [INAUDIBLE]

56:31 HAZHIR RAHMANDAD:
So yes, but you

56:34 want it to also start at
the slope of 45 degrees.

56:41 STUDENT: Yeah, so the
second half of it.

56:43 So we'll put the
inflection point at 0.

56:45 HAZHIR RAHMANDAD: Yes, but
the sigmoid at the second half

56:48 at the inflection point
of the slope is flexible.

56:53 STUDENT: Yeah, but we know where
that limit of that slope is.

56:56 HAZHIR RAHMANDAD: Yes, yes.

56:57 We know limit of the slope.

56:58 But I'm saying that
you actually want

57:00 it to be at the max consumption
rate at the very beginning.

57:05 So this is also an interesting
but likely, reasonable approach

57:11 that basically, if
people are starving

57:13 or the predators are
starving and there is only

57:17 so much prey, they will try
to get as much as they can.

57:21 That's the idea.

57:22 STUDENT: [INAUDIBLE]
there's just one

57:24 value that fits these limits.

57:25 Then we don't have
any control over it.

57:27 HAZHIR RAHMANDAD: Yes, exactly.

57:28 So this min function actually
brings that second constraint

57:32 into your equation, but has the
kink that Alexander highlighted.

57:36 STUDENT: Could you
explain what you

57:37 were saying a minute ago about
weakening the balancing feedback

57:41 loop?

57:41 HAZHIR RAHMANDAD: Yes.

57:42 So here, we have one
balancing feedback loop

57:47 that is more deer, more
consumption, and therefore less

57:54 deer.

57:55 So that's the
first order control

57:59 that we need to avoid
the stock going to 0.

58:02 So that feedback loop in the min
function, in Gerardo's version,

58:10 would only operate where the
x is between 0 and 1, OK?

58:15 And as soon as it is above
1, that feedback loop

58:19 goes away because,
in this formulation,

58:24 the predator gets as
much prey as it wants.

58:28 And therefore, that feedback
loop is not active anymore.

58:31 Now, this is not
fundamentally wrong.

58:34 Those feedback loops
saturate at some point

58:37 and are not active anymore.

58:39 But making it a very quick
shift between those two domains,

58:45 for all kinds of
analysis, becomes

58:48 a little bit less easy to
trace why this is happening.

58:53 Even in some
optimizations, it becomes

58:55 helpful to have those
feedbacks active so

58:58 that it pushes the
optimization engine to find

59:01 the right balance.

59:02 Otherwise, that
parameter never works.

59:06 STUDENT: So OK.

59:07 When we have this kink--

59:11 I see.

59:11 So then when we have
this kink to the left,

59:14 when we do this thing,
then it's always active.

59:18 HAZHIR RAHMANDAD: It is
always active, exactly.

59:21 STUDENT: Yeah, that
makes a lot of sense.

59:22 HAZHIR RAHMANDAD: And in
fact, in a table function,

59:25 you don't have it always
active because, ultimately,

59:27 you put a value that
says maybe at level

59:30 x equals 3 it saturates.

59:31 So table functions are not,
in this case, necessarily

59:35 the best tool.

59:36 You define it and you
can't control it as easily.

59:39 You have to go and
manually change it.

59:40 So I like the
analytical function

59:42 for all of those reasons.

59:45 Good.

59:45 So if you build
this part, this can

59:49 go both into the
consumption of prey

59:52 and the consumption of the
vegetation by the prey.

59:59 So both of the stocks
can be constrained

60:02 by a mechanism like this,
by a formulation like this.

60:06 And that will basically
do the kink thing.

60:11 But Gerardo's formulation
is a decent starting point.

60:16 It is not fundamental--
it doesn't

60:17 have any fundamental problems.

60:19 It's just has this
non-trivial jump.

60:27 OK.

60:28 So now that we saw that, let's
actually look a little bit more

60:31 at Gerardo's formulation and
see if there is anything else

60:37 we want to discuss there.

60:39 And Gerardo, we
haven't heard you.

60:41 We just have been
discussing your model.

60:43 

60:49 STUDENT: I was out
of time this week.

60:51 And I think that there are a lot
of things wrong in this model.

60:55 

60:58 HAZHIR RAHMANDAD:
But actually, you

61:00 had the better
formulation so far

61:02 for the most challenging part.

61:04 So that's good.

61:04 

61:08 STUDENT: [INAUDIBLE]

61:09 

61:13 HAZHIR RAHMANDAD: Yeah.

61:14 STUDENT: Jason was suggesting
doesn't necessarily

61:17 have a max or a
minutes baked into it.

61:19 HAZHIR RAHMANDAD:
Yes, let's look at it.

61:23 STUDENT: [INAUDIBLE]
current consumption over 1

61:28 plus a max consumption.

61:32 HAZHIR RAHMANDAD: Where am I?

61:34 So this is your--

61:37 STUDENT: [INAUDIBLE]

61:38 HAZHIR RAHMANDAD: Yes,
let's go for the deer.

61:40 STUDENT: [INAUDIBLE]

61:42 HAZHIR RAHMANDAD: OK.

61:42 So for the deer, we have
the effective deer lifespan.

61:46 And then we have
predation of mature deer.

61:49 And you do have the predation
of juvenile deer, which is good.

61:52 If you have juvenile
deer, they will be eaten.

61:54 STUDENT: I think current
consumption is kind of the one.

61:57 HAZHIR RAHMANDAD: Yes.

61:58 So let's look at the
current consumption.

62:00 STUDENT: So I have
that idea of there's

62:03 a success rate in hunting, which
admittedly is just static here.

62:08 But it is made into something
that is like [INAUDIBLE]

62:13 HAZHIR RAHMANDAD: Yeah, so let's
go to the current consumption

62:16 and then--

62:18 OK.

62:19 So attack rate multiplied
by hunt success rate--

62:25 those two together
are always together.

62:27 So think of that as
just a single parameter.

62:30 So it makes the world a little
bit easier to make sense of.

62:33 STUDENT: But you
could change it.

62:35 HAZHIR RAHMANDAD: Yes, you
could change it, absolutely.

62:37 And if you made one
of them dynamic,

62:39 you can see the value of
having the parameters.

62:43 So one parameter multiplied
by the deer population

62:47 raised to the power of 2.

62:49 So the idea is that, as
the deer population grows,

62:53 the consumption rate
can go up divided

62:55 by 1 plus some time constant.

63:02 STUDENT: It's not
a time constant.

63:04 So if you look at
time to consume here,

63:06 it's basically setting
the maximum amount

63:09 of deer consumed per day.

63:11 HAZHIR RAHMANDAD: Yeah.

63:12 So basically, you
have the numerator

63:16 divided by 1 plus some parameter
multiplied by that numerator.

63:21 So let's think about
that formulation.

63:23 So x divided by 1 plus alpha x.

63:26 STUDENT: And alpha is the max.

63:28 Alpha is like 1 over the max.

63:32 HAZHIR RAHMANDAD: OK.

63:35 So that formulation, if
x is 0, it goes to 0.

63:39 That is, if you
don't have any deer,

63:42 there is no consumption
per predator.

63:46 If x is a very large
number, then this

63:51 converges towards 1 over alpha.

63:59 So if alpha is then your 1 over
maximum rate that you want,

64:08 you get what you want
out of this formulation.

64:14 So tell me about where
the power 2 came from.

64:17 STUDENT: The power
2-- so I originally

64:20 wanted something that
depended on density a lot

64:25 and depended on basically
interactions between wolves

64:30 and deer and their success rate.

64:33 And then through a lot of
back and forth thinking

64:37 about that specifically, I
originally just had deer.

64:41 And then I was thinking back
through, admittedly with AI,

64:46 this particular idea of I want
it to depend more on [INAUDIBLE]

64:50 HAZHIR RAHMANDAD: Yes.

64:51 STUDENT: And so it suggested
the idea [INAUDIBLE]

64:54 

64:55 HAZHIR RAHMANDAD: Yeah.

64:56 So basically, you used
a more mathematical way

65:00 of trying to get
to a function that

65:02 does what you want it to do.

65:03 That is, when the
density is low,

65:05 you don't get as many
deer hunted per predator.

65:11 And as the density goes
up, you get more and more,

65:14 but then it saturates.

65:16 And this does all
of those things.

65:20 So what are the
problems with this?

65:22 So the first problem is
that the units don't match.

65:26 And the reason the units don't
match is that time to consume--

65:32 STUDENT: Well, I called
it time to consume.

65:34 HAZHIR RAHMANDAD:
It doesn't matter.

65:36 Whatever is the unit, because
it is 1 plus this thing,

65:39 1 is dimensionless.

65:43 STUDENT: Yeah.

65:43 

65:46 So is that term,
the second term.

65:48 HAZHIR RAHMANDAD: Ah.

65:49 STUDENT: So the numerator
is like consumption.

65:51 And then time consuming deer
cancels out that consumption.

65:55 HAZHIR RAHMANDAD: I
see, I see, I see.

65:57 Then the units can work.

65:59 You're right, you're right.

66:02 OK.

66:04 So then the main
problem that remains

66:07 is just it is hard to consume
this equation in terms

66:11 of the micro-mechanisms.

66:14 And if we go through the actual
exact equation and we compare it

66:21 with the one that we designed,
the question of whether

66:24 the 45-degree line constraint
gets violated here or not,

66:29 with an alternative
conceptualization that thinks

66:31 of deer availability as--

66:35 or max consumption rate of
deer as another constraint--

66:38 that I don't know how
it will pan out here.

66:42 That is, in this function
of 1 over 1 plus alpha x--

66:46 or x2 divided by
1 plus alpha x2,

66:50 whether you may go over the
45-degree line in the range that

66:56 we are considering.

66:57 It's not something
I can mentally do.

66:59 We would have to write it down.

67:01 And that's why having a story
that breaks down the logic

67:07 will help a little bit more
with getting good formulations.

67:11 STUDENT: I mean--

67:12 HAZHIR RAHMANDAD: But
this does the job.

67:14 So this is good because it
does the things that we want.

67:17 It shuts off consumption
when there is no deer.

67:21 It allows for max
consumption per predator

67:25 or desired consumption
per predator

67:28 when we have plenty of deer.

67:30 It has the softmax story.

67:32 It has a free
parameter, that alpha 1.

67:35 So it has all of
those characteristics.

67:38 So it is good on
all of those fronts.

67:41 STUDENT: But I guess my
thing is, isn't there

67:46 a more reasonable story to--

67:49 HAZHIR RAHMANDAD: To match this?

67:51 STUDENT: To this than to
something that has a kink in it?

67:56 HAZHIR RAHMANDAD: So this one,
again because we haven't done

68:02 the analysis with the 45-degree
line, may violate that.

68:05 I don't have the
intuition right now.

68:08 STUDENT: What would it mean
practically [INAUDIBLE]

68:11 HAZHIR RAHMANDAD: So
if it violates it,

68:13 it means that at
some levels of prey--

68:18 the rate of consumption of
prey exceeds the maximum rate

68:24 that, based on
random interactions,

68:28 is even feasible
to happen in that--

68:31 with the density of
deer that is available.

68:34 So that becomes-- so let's
say it takes some time

68:38 to prey any deer.

68:40 There is a literally
physical time that you need.

68:44 And it takes some
time to find the deer.

68:49 You add those two together.

68:51 There is a minimum time to
catch a deer, so to speak.

68:57 So if you have very few
deer, the total predation

69:01 should not exceed that.

69:03 Whether that will happen here
or not we cannot tell from

69:06 the equation.

69:07 STUDENT: I think that
might be what my attack

69:09 rate is because it's like--

69:14 HAZHIR RAHMANDAD:
It is a parameter.

69:15 I'm just saying-- so the
attack rate right now

69:20 is trying to capture that idea.

69:23 But because you have just
deer to the power of 2 playing

69:26 something, it is not clear how
it actually ends up downstream

69:31 when you get the
total consumption.

69:34 But it does the job.

69:36 In fact, so this
one actually doesn't

69:39 have the flexibility to change
the slope of how fast you

69:44 converge.

69:46 You just change the height of
where the total consumption

69:52 per predator converges to.

69:56 If you want to
make that flexible,

69:59 you would play with
the power here.

70:01 So you can go with power
of 2 or 3 or whatever.

70:03 So that becomes the
alpha equivalent

70:06 for the other
formulation we saw.

70:09 OK, this is a nice
alternative to think through.

70:13 And thanks for bringing
that up [? and ?] never.

70:15 

70:18 OK.

70:21 Anybody else wants to look at
their formulation for this part?

70:25 

70:28 So Kathy also wants--
let's go to Kathy's.

70:30 Let me see.

70:32 OK, good.

70:33 STUDENT: So it's a different
analytical formulation.

70:36 It has the same problem,
where it needs to be--

70:39 it goes above the
45-degree line.

70:41 So that--

70:42 HAZHIR RAHMANDAD:
Yeah, so let's start

70:46 looking at it step by step.

70:48 So you have also separated the
starvation from natural deaths.

70:51 And as I said,
it's a little bit--

70:57 we can get to that
equation as well.

70:59 So I think that's
a separate equation

71:01 than eating of the deer.

71:03 So let's focus on this one.

71:04 And this has four
things going into it.

71:06 So I have to open it
and see what it's doing.

71:10 So minimum effective
RDD and deer.

71:15 What is RDD?

71:16 STUDENT: Relative deer
density, so how many deer

71:20 over some reference, like
full density amount of deer.

71:23 HAZHIR RAHMANDAD: OK,
multiplied by indicated deer

71:27 eaten versus deer divided
by minimum time to eat deer.

71:32 So this is similar to what we
had with Gerardo's formulation.

71:37 And this first part is a
little bit more involved.

71:41 So let's look at
what that is doing.

71:44 So indicated deer
eaten comes from wolf

71:49 multiplied by wolf appetite.

71:51 So this is the desired, OK.

71:54 And then this relative RDD
is adding another constraint

72:02 on consumption that is--

72:07 OK.

72:08 So let's look at this
equation and make sense of it.

72:10 So it is max of 0.

72:11 OK.

72:12 It shouldn't go negative.

72:14 Some parameter A
multiplied by 1 minus e

72:19 to the power of minus B
relative deer density.

72:25 So if deer density is very
high, this thing turns into--

72:32 the exponent goes to a
large negative number.

72:36 e to the power of
that goes to 0.

72:38 1 minus that becomes 1.

72:40 It goes to A.

72:42 But in this case--

72:44 OK.

72:44 So that's for high
deer densities.

72:47 This goes to a number A. And
for lower deer densities,

72:53 it can go down to 0, basically.

72:57 So if it is 0 deer density,
that e to the power of blah,

73:04 blah becomes 1.

73:05 So this thing is--

73:08 so it's very similar
to the equation

73:10 that I wrote for the other part.

73:13 And this is saying per predator.

73:21 So what's the unit for A?

73:23 All of these are dimensionless.

73:26 So why do you need A here then?

73:29 STUDENT: So A is 1 currently.

73:31 I was thinking though that there
is kind of a gluttony effect.

73:34 And maybe I want want it to go
to 1.2 or something like that.

73:38 HAZHIR RAHMANDAD: But why
not capture that already?

73:40 

73:44 You see, human
learning is very slow.

73:47 OK, so why don't you capture
that involved appetite?

73:51 Because ultimately,
this is going

73:52 to be multiplied by appetite.

73:55 So it is just one
degree of freedom

73:57 that is not
well-defined and doesn't

73:59 do anything extra for you.

74:01 So don't add that type of a--

74:04 STUDENT: Yeah, I was
thinking of wolf appetite

74:06 as the equilibrium.

74:09 But if they have 100
deer in front of them,

74:12 maybe they'll eat extra, I
guess, over and above that.

74:16 But right, it doesn't
need to be there.

74:18 HAZHIR RAHMANDAD: Yeah,
because whatever it does,

74:20 it will ultimately be
multiplied by this.

74:22 A. It will never--

74:24 and then you don't need the max
with 0 thing as well, I think.

74:30 STUDENT: That's true.

74:31 I removed it when
we were talking.

74:32 HAZHIR RAHMANDAD: Yeah,
you don't need that.

74:34 And then yeah, beta does the
thing for slowing it down.

74:40 So yeah, this
should work as well.

74:43 So this way, you have the
45-degree constraint going

74:49 through the min function.

74:51 And you have the
other constraints

74:53 kicking in through limiting
how many deer the wolf can eat.

74:58 So this works fine.

74:59 I think that's good.

75:02 

75:06 OK.

75:07 Let's start looking
at the starvation

75:09 equations or let's take a break.

75:12 STUDENT: Break.

75:13 HAZHIR RAHMANDAD: Yeah,
I think it's a good time

75:15 to take a break, 10 minutes.

75:19 So this is Jason's model.

75:21 Let's take a look at
a couple of items.

75:25 So we had the predation of
deer from desired consumption.

75:33 And then you have the
desired fulfillment ratio.

75:38 So this is the formulation
we talked about

75:43 in following the same idea as
the shipment from inventory.

75:49 So there is a max
feasible consumption,

75:51 deer divided by minimum
time to capture,

75:54 versus the desired consumption
that gives a prey sufficiency.

75:59 Let's just make sure we
know the formulation.

76:02 This is the max
divided by desired.

76:04 OK.

76:04 It's very similar to
what we just discussed.

76:07 And then this goes into
a fulfillment ratio

76:10 that, right now,
we talked about it.

76:12 You highlighted that.

76:15 And we said how you can actually
overcome some of the challenges

76:20 with this formulation to get
it to do what you want to do.

76:25 And then you get the
deaths just from predation.

76:30 Let's go to starvation part.

76:32 

76:39 So you have the general
death from old age.

76:43 So deer, after a
while, they die.

76:45 That's very standard, simple.

76:47 You take care of it that way.

76:49 Then you're saying a
fraction of the deer

76:54 is at risk of dying
from starvation.

77:02 

77:05 So to calculate that--

77:08 I'm not following
the units here.

77:11 Oh, you have deer also here.

77:13 OK.

77:14 Where did the deer come from?

77:17 STUDENT: It's the first order.

77:18 So there's some minimum--

77:19 HAZHIR RAHMANDAD: Oh, yeah.

77:20 There is deer inside here.

77:21 STUDENT: So if they don't eat
for two weeks, they'll die.

77:24 And then that flow gets
closer and closer to 0,

77:29 depending on how
satiated they are.

77:30 HAZHIR RAHMANDAD: OK, so you're
saying deer divided by deer time

77:34 to starve is the death
rate from starvation.

77:41 If satiation is 1,
then nothing happens.

77:49 STUDENT: Right.

77:49 HAZHIR RAHMANDAD: So that's
how you close this valve off,

77:53 basically.

77:54 STUDENT: Yeah.

77:55 HAZHIR RAHMANDAD:
OK, that's fine.

77:58 I think the risk I see with that
is the deer satiation equation.

78:03 It needs to be turned on only
in relatively extreme conditions

78:08 or cases.

78:10 That is, you have significant
lack of malnutrition.

78:14 Otherwise, it starts
killing deer quite rapidly.

78:18 STUDENT: [INAUDIBLE]

78:21 HAZHIR RAHMANDAD: But
in this formulation,

78:23 we can't see that, because
it's the calculation

78:25 of deer satiation,
that determines it.

78:28 And in this case, you have
just a grass fulfillment ratio,

78:31 which is the ratio
of what the grass is

78:35 available for the desired
consumption for the deer.

78:39 STUDENT: Yeah, [INAUDIBLE]

78:40 HAZHIR RAHMANDAD: That's good.

78:40 So this is actually a
very important piece.

78:43 And I was looking at
some of the other models.

78:45 Some of them didn't
follow this idea.

78:47 So note here, the grass
fulfillment ratio--

78:52 that is, what fraction of the
desired consumption by deer

78:56 is actually happening because
of the availability of grass--

79:00 is having an impact on
the grass consumption.

79:03 But it also feeds back
into deer starvation.

79:08 It is very important to
use the same concept,

79:11 rather than defining this
concept in another way,

79:15 in another part of the
model, because the underlying

79:18 concept is deer does
not get to eat grass

79:22 or does get to eat grass.

79:24 It's the same thing.

79:25 It's the two sides
of the same coin.

79:26 STUDENT: It's easy to see it, if
you scroll down to the wolves.

79:31 It's the same thing,
but I just broke it down

79:34 into more steps--
actual deer consumption,

79:36 and then wolf satiation, i.e.

79:39 it's the fraction that they ate
divided by what they desired,

79:43 which is equivalent
to the desired ratio.

79:47 But that story,
that is [INAUDIBLE]

79:49 HAZHIR RAHMANDAD: Yes.

79:50 So both of those give the
same answer mathematically.

79:53 But the version down
here is saying, OK,

79:55 this is the desired consumption
versus actual consumption.

80:00 That ratio gives satiation.

80:02 And it is a good practice
to spell out those steps

80:05 because if, for whatever reason,
you add another mechanism that

80:08 changes the actual
consumption, for example,

80:12 it would not be captured in
that fulfillment ratio alone.

80:16 It will be captured
in something else.

80:18 So it is fine to add
this extra variable,

80:21 even though it is ultimately
the same as desired fulfillment

80:25 ratio.

80:25 Is the logic here clear
what we are talking about?

80:29 STUDENT: Yeah.

80:30 HAZHIR RAHMANDAD: If you
feel anything is, OK, I'm not

80:32 following, raise your hands.

80:34 I wouldn't know.

80:35 But we would pass it
too quickly, then.

80:38 OK, so the only place that
I'm a little bit unsure

80:43 is that this wolf
satiation should

80:47 be the same thing
that goes into here

80:51 and get 1 minus that satiation.

80:53 STUDENT: [INAUDIBLE]

80:54 HAZHIR RAHMANDAD: No, I know.

80:55 But I'm saying, it
may be too strong

80:58 a feedback of starvation
because time to starve

81:03 is relatively short.

81:05 And then basically, OK,
biologically, what happens?

81:09 If you don't get to eat what you
desire to eat, you get thinner.

81:14 And your desire
for eating actually

81:17 goes down because your
metabolic rate goes down.

81:21 And then you reduce
your activity level.

81:24 And you do all these things.

81:25 STUDENT: [INAUDIBLE]

81:27 HAZHIR RAHMANDAD: So there
are all these balancing

81:29 loops that you wouldn't
start dying right away.

81:31 In fact, for anybody like us,
we may actually live for a while

81:39 without eating at
100% of our desire--

81:43 2,200 calories or
whatever it is.

81:46 If I bring that down
to 2,000 calories,

81:48 it doesn't mean that
I'll start to die.

81:51 It just means I'll probably
equilibriate at 2,000 calories.

81:56 Even if you bring
it down to 1,500,

81:59 you may equilibrate
at that and not die.

82:01 Now, if you bring it to 1,000,
then you will probably die after

82:05 maybe a few months or something.

82:07 So that's the thinking
that gives me the feeling,

82:10 OK, this wolf satiation
shouldn't directly

82:13 go into the death.

82:15 It needs to be
transformed somehow.

82:17 And the transformation should
make it keep it closer to 1.

82:23 That is, if the satiation is
0.7, I should push it up to 0.95

82:32 or something like that.

82:35 You see the logic why--

82:38 the way to think about this?

82:39 So then how would you do that?

82:41 So what is the right
or easy way to do this

82:45 with the current
formulation that Jason has?

82:47 

82:56 Any suggestions?

82:57 Anybody?

82:58 

83:03 STUDENT: I mean, when you have
wolf satiation [INAUDIBLE]

83:11 HAZHIR RAHMANDAD: Yeah, yeah.

83:12 Well, not desired consumption.

83:15 Wolf satiation-- OK, so
the story I was telling

83:20 STUDENT: [INAUDIBLE]

83:21 HAZHIR RAHMANDAD: Included
a feedback into desired

83:23 consumption, you're right.

83:24 But that's too much.

83:26 That's messy.

83:28 So that was not
what I was asking.

83:30 I was asking for a
simple formulation that

83:33 gets wolf satiation and
gives you effective wolf

83:36 satiation on death rate.

83:39 Basically, right now, Jason
is equating wolf satiation--

83:43 or 1 minus wolf satiation
with death effect.

83:47 STUDENT: [INAUDIBLE] [? x ?] the
wolf satiation to some exponent.

83:56 HAZHIR RAHMANDAD: OK, so what
should the exponent range be?

83:59 So let's say we have wolf
satiation to the power of alpha.

84:03 Should the alpha
be small or big?

84:05 STUDENT: [INAUDIBLE]

84:06 HAZHIR RAHMANDAD: It
should be smaller than 1.

84:08 So if alpha is 0, you shot
off this feedback loop.

84:13 That is, basically,
there is no starvation

84:16 because anything to the
power of 0 is still 1.

84:20 And therefore, this
thing goes away.

84:22 If alpha is 1, it is
the current formulation.

84:26 So somewhere between that range
is where you want alpha to be.

84:30 And that's a good way
of formulating this

84:32 because wolf
satiation will never

84:35 go above 1 the way
it is formulated here

84:37 because it is always
actual divided by desired.

84:41 So at max, it will be 1.

84:42 So I'm fine with that range.

84:44 It will all work.

84:46 Is the idea clear?

84:48 So that's a good formulation.

84:50 I think, with that correction,
this does a decent job.

84:55 We talked about the
issue of whether we

84:57 want to combine them
or separate them.

84:59 Now that I'm seeing how
you have separated them--

85:01 and I think some of the others
have done a similar thing--

85:04 I like it.

85:04 It is fine.

85:05 I don't have anything
against it because the logic

85:09 of natural death from old
age is easy to capture

85:12 using this lifespan.

85:14 And then you can
separately capture it here.

85:17 So this is fine.

85:19 Ali?

85:20 STUDENT: [INAUDIBLE]
I had this issue also.

85:23 And I found it very last minute.

85:25 So I think, if you don't
have any vegetation,

85:29 deer would grow because
there is no control

85:33 on the [? earthworms. ?]
So what I'm trying to say

85:37 is that the outflow
from vegetation

85:40 should be the
inflow to the deer.

85:43 [INAUDIBLE] of the vegetation
should be the inflow

85:51 to the birth rate of the deer.

85:53 HAZHIR RAHMANDAD:
OK, very good point.

85:54 So now, this is an important
biological question for us

85:58 who are not biologists and have
no clue about how deer life

86:03 spans are.

86:04 So the question is, if people
are-- or deer are starving,

86:08 would they have babies?

86:10 And the short answer
is not as many.

86:13 Basically, the
stress of starvation

86:16 brings down their birth rate.

86:18 So that is another way to
potentially have a feedback

86:24 into the system.

86:25 So that definitely is a logical,
biologically sound idea.

86:32 Now, there is a question,
do I even want to do that?

86:36 And the reason for
asking that question

86:39 is, this outflow
is pretty strong.

86:42 And you have control over it.

86:44 And it is proportional
to the size of the deer.

86:47 Basically, you have deer divided
by some time constant and so on.

86:51 So you can say I'm capturing
those unborn babies as death.

86:58 So you are a pro-life
person or something.

87:04 So that's one way of
making the argument

87:10 that I don't need to
separately capture it

87:13 because then I would
add some other parameter

87:15 and some other structure.

87:17 And I'm perfectly fine
with that recognition,

87:21 and then saying
I'm not doing it.

87:23 But it's good to have
that recognition.

87:27 OK, great.

87:30 So I think this is working
fine with the couple of ideas

87:33 that we mentioned.

87:36 We didn't have the--

87:40 yeah, so the grass is
growing exponentially here.

87:43 It doesn't have
any balancing loop.

87:47 So if you leave the grass
unchecked with the deer,

87:57 then it grows exponentially.

88:00 And that is a problem that this
formulation doesn't capture.

88:05 Now, again, for that, you could
have a grass death separately.

88:10 Or you could use Alexander's
or some alternative version

88:14 that uses the single flow
for grass and saturates that.

88:21 Great.

88:22 Let's see.

88:23 Anybody else want to bring a
question from their models?

88:28 I think we have really
discussed the key issues.

88:31 So we can open it to any models.

88:34 Alexander, do you
want to take a look?

88:35 Sure.

88:38 STUDENT: About the predation
rate and the death rate.

88:43 So I completely--

88:45 I guess I implicitly
assumed that animals

88:48 have insatiable appetites.

88:49 So I forgot about the whole
capacity thing and things

88:51 like that.

88:52 And I focused a lot on
the hunting efficiency.

88:56 HAZHIR RAHMANDAD: Uh-huh.

88:57 STUDENT: And so basically,
what I wanted to capture

89:00 was that, as there's fewer
deer, wolves can't hunt as well,

89:08 can't hunt as well.

89:09 And then their efficiency
maxes out at some point.

89:11 So that's the top
half of the model.

89:14 HAZHIR RAHMANDAD: OK,
so let's look at it.

89:20 So you have the hunting
efficiency multiplied

89:23 by the number of the predators.

89:25 So this hunting efficiency
is what we already

89:28 have seen in various formats.

89:31 And that comes
from some reference

89:34 multiplied by some effective
availability of prey.

89:38 And that effect is a fraction
of carrying capacity,

89:45 so prey divided by
carrying capacity of prey.

89:50 It should be fine.

89:51 So that number, if the model
works well on other fronts,

89:56 would always be between 0 and 1.

89:59 But you can never be sure
because you can actually start

90:01 from beyond carrying capacity.

90:04 You can throw in too many
prey in a natural environment.

90:10 And then effective prey
population and efficiency is--

90:15 STUDENT: So it's similar to what
Jason was suggesting earlier.

90:19 It's x over 1 plus
x to some alpha.

90:24 And then I put that 2 in the
beginning so it's such that,

90:26 when that fraction
is equal to 1,

90:29 then the efficiency is
[INAUDIBLE] So without the 2,

90:34 and let's say the sensitivity
is 1, then if the fraction is 1,

90:38 then this whole
effect would be 1/2.

90:40 And so I put in
the 2 so that way,

90:41 when the fraction
is 1 [INAUDIBLE]

90:43 HAZHIR RAHMANDAD: Yeah.

90:45 STUDENT: So I just
wanted to bring this up

90:47 because I approached
this differently

90:50 than a lot of other people.

90:51 And I just wanted to
know what the issue is.

90:53 HAZHIR RAHMANDAD: Yeah,
so let's think about it.

90:55 So we already have talked a
little bit about some of these.

90:59 So basically, this
one is saying,

91:06 at carrying capacity
levels of prey population,

91:11 we give predators
what they want.

91:17 And higher levels
wouldn't happen

91:28 because this fraction of
prey carrying capacity

91:30 should not go above 1.

91:34 So anything below that will
lead to less consumption

91:40 per predator.

91:44 And how much less depends on
this sensitivity parameter.

91:48 You're currently
putting it at 2.

91:50 So this leads to a
relatively sharp reduction.

91:56 That is, so the table
function-ish view

91:59 is more like this.

92:00 This is 0 to 1.

92:01 It goes quickly up, which
means it is very sensitive.

92:08 If you don't have enough deer,
the amount of consumption

92:11 goes down non-linearly.

92:14 So you wouldn't have a problem
with hitting the 45-degree line

92:19 in our other version
of the formulation,

92:23 as long as your sensitivity
parameter is above 1.

92:27 

92:34 We do have the issue that maybe
that is too harsh, maybe--

92:41 that is, to predators.

92:44 That is, they
could consume more.

92:46 

92:52 So we said that, at
the 0 level of prey,

92:57 the 45-degree line in the other
conception is a potentially good

93:03 reference curve.

93:04 And the argument there was that,
if there is prey to be eaten

93:11 and there is plenty
of predators,

93:13 they'll be eating the
prey with the maximum rate

93:16 feasible that comes from
prey divided by number of--

93:22 minimum time to consume prey.

93:25 So that was the argument for
targeting the 45-degree line

93:29 as a reference line.

93:31 Now, you may argue
that is not the case.

93:34 That is, the search
process for the prey scales

93:46 non-linearly with its density.

93:48 That is, if the
density is very small,

93:52 it doesn't go down the
rate of consumption--

93:57 linearly, it goes non-linearly.

93:58 And I think your
equation, Jake, also

94:02 had that alternative
way of justifying it.

94:05 So I want us to be clear about
what the formulations are

94:09 doing in both of these cases.

94:11 In your case, I'm not sure
because we haven't connected

94:14 it fully to that formulation.

94:16 In this case, it is
making the assumption

94:18 that the non-linearity in
preyability is significant.

94:24 And therefore, even
if there is some prey,

94:26 they would not be hunted
because they can't be found.

94:30 They go into some
holes and something.

94:32 I don't know.

94:32 And that's OK, as long as you
know that's the assumption

94:36 you're making.

94:39 STUDENT: So yeah,
I was thinking--

94:41 I just want to bring this
up because [INAUDIBLE] I

94:42 was thinking about
the search process

94:44 as opposed to the [INAUDIBLE]

94:45 HAZHIR RAHMANDAD: Yes, but you
also have basically the desire.

94:50 It is built into your parameter
reference hunting efficiency.

94:54 That's basically the desired
parameter in your setup.

94:58 And its units should be in
deer per wolf per month.

95:02 So it is really just the desire.

95:04 

95:08 STUDENT: OK.

95:08 So I think, in that case,
my mistake was is that I--

95:12 OK.

95:13 I think my mistake,
in that case,

95:14 was that I didn't realize that.

95:16 I wasn't thinking
about [INAUDIBLE].

95:18 So then when I talk about
the effect of hunting

95:20 on the wolf death rate
in the lower half,

95:23 I'll have a separate
parameter, which is

95:24 the required prey per predator.

95:26 And now, I see that
they're [INAUDIBLE]

95:28 HAZHIR RAHMANDAD: Yes.

95:29 Conceptually, these two are
very similar to each other.

95:32 And basically, you shouldn't be
creating yet another process.

95:37 Now, this yet another
process will give you

95:40 a number that is very
comparable probably

95:45 with the parameters
you have chosen.

95:46 And then you have another
sensitivity thingy here.

95:50 So maybe, ultimately,
it doesn't matter,

95:53 in terms of degrees of freedom.

95:55 You have plenty of
degrees of freedom

95:57 to get the behavior you want.

95:58 But it reduces the clarity
of the formulation.

96:02 STUDENT: I guess I was
thinking maybe there's

96:04 a predator who really
wants to eat a lot of prey,

96:07 but is really bad at it.

96:08 And that's why I had--

96:10 I mean, unironically.

96:11 And that's why I had separate--

96:15 it kind of ran through my mind.

96:16 And that was my
haphazard justification.

96:18 But yeah, so I
see the-- and then

96:21 I also see how the
hunting adequacy, which

96:23 is just prey hunted
divided by required,

96:26 is similar to that effect.

96:29 HAZHIR RAHMANDAD: Yeah.

96:30 So basically, this
sensitivity parameter

96:34 can take care of the
efficiency consideration.

96:39 And then the desired parameter
should mean the desired.

96:44 STUDENT: Yeah, so I see
how it's very similar.

96:46 HAZHIR RAHMANDAD: Yeah.

96:47 STUDENT: And then I guess
I just wanted to bring up

96:49 as well how it affects it.

96:51 So I had predator
deaths be the same.

96:55 And then what I had is that
this effect, which we discussed

96:58 the issues with,
basically changes

96:59 how long hunters live with
logistics so that hunter

97:03 lifespan is weighted.

97:04 HAZHIR RAHMANDAD: Yeah.

97:05 So now, basically, you have the
version with a single outflow

97:13 rather than two
separate outflows.

97:14 So we saw Jason's two outflow.

97:16 Let's look at this
single outflow version

97:18 and see how it works.

97:20 So you have the hunter lifespan.

97:22 And you are just
reducing the lifespan.

97:24 So that's a very
natural, good alternative

97:27 because, even if you're
dying from starvation,

97:30 you're dying after a while.

97:31 So your lifespan has ended.

97:33 So as such, this is
also a good formulation,

97:36 the basic starting point.

97:37 Now, we have to get what
is the hunter lifespan.

97:40 You have the minimum hunter
lifespan and the maximum hunter

97:43 lifespan.

97:43 This is the natural.

97:45 The maximum is
the natural if you

97:46 have all of the food you need.

97:49 And then the minimum is
the starvation time horizon

97:52 that Jason was talking about.

97:55 And then this is some kind
of a weighted average.

97:57 So this effect
multiplied by maximum,

98:00 1 minus effect multiplied
by minimum, this is fine.

98:03 I like that way of shifting
between those two life spans.

98:09 Then the key question is, how
does this effect get formulated?

98:14 It needs to be between 0 and
1 because that switch requires

98:18 you to be between 0 and 1.

98:20 Otherwise, it doesn't work.

98:21 So you have hunting
adequacy, which

98:24 is how much you eat versus
how much you are requiring.

98:30 Again, keep in mind that this
required value should probably

98:35 be just hunting
efficiency multiplied

98:38 by predator or something.

98:40 But that put aside, this
is also a decent input

98:43 into the formulation.

98:45 And this haunting adequacy
should not go above 1,

98:49 if it is correctly formulated.

98:51 Now, in this version, it
may go above 1 depending

98:56 on the parameters chosen.

98:57 That is, if the required
prey per predators

99:00 is smaller than this hunting
efficiency parameter--

99:04 and it's probably not the case
in Alexander's So this is 2.

99:07 That one was 1.5.

99:10 So it wouldn't go above 1.

99:11 But technically, it could
if somebody comes and plays

99:14 with the parameters.

99:16 Everybody is following
what we are saying?

99:19 So you see, on the
top, hunting efficiency

99:24 is multiplied, after
some adjustments,

99:28 by the number of predators.

99:29 That's the actual prey hunted.

99:31 In the bottom, hunting required
as the predators multiplied

99:36 by this required prey.

99:38 So this gives a different number
than the maximum up there.

99:42 And if the maximum up there
is bigger than this number,

99:49 the ratio of hunting
adequacy exceeds 1.

99:53 And if that exceeds 1,
things get messed up

99:58 because now this has--

100:01 this ratio should not exceed 1.

100:06 Now, in this formulation, maybe
it is kept between 0 and 1

100:10 using the exponential.

100:11 So let's look at this equation.

100:13 STUDENT: [INAUDIBLE]

100:14 HAZHIR RAHMANDAD: Yeah, so
this is a logistic one that

100:16 says e to the power of some
alpha hunting adequacy minus 1

100:23 divided by same thing plus 1.

100:26 STUDENT: Yeah, I also
screwed up the parentheses,

100:28 I realized here.

100:29 HAZHIR RAHMANDAD: OK.

100:30 STUDENT: The entire denominator
is taken to the exponent.

100:32 But my intent was
to do logistic.

100:34 HAZHIR RAHMANDAD: Yes,
you need the parameter--

100:38 sorry you need another--

100:41 STUDENT: [INAUDIBLE]
I think the second--

100:48 HAZHIR RAHMANDAD: Is extra?

100:50 No, this is fine, e to
the power of whatever

100:55 you have up there divided by
e to the power of sensitivity.

101:02 I think it is fine.

101:05 Maybe this one is--

101:07 STUDENT: Yeah, that one.

101:08 HAZHIR RAHMANDAD: This
one is misplaced, yes.

101:09 So this should be here.

101:10 OK.

101:11 But the basic idea
works well here.

101:15 So it is saying, if hunting
adequacy is 1-- that is,

101:19 you have plenty, that you
have what you wanted--

101:22 then e to the power of 0 divided
by-- so you get a value of 0.5

101:30 out of this expression.

101:32 Is that what you wanted to get?

101:34 STUDENT: I was thinking
of hunting adequacy

101:36 as basically this is like--

101:40 I was thinking of it more of
like this is some minimal level.

101:45 And that if you go
below this level,

101:47 your lifespan is going
to go really down.

101:49 HAZHIR RAHMANDAD: OK.

101:50 So this is an important
consideration.

101:53 So Alexander talked about it.

101:55 And he tried to
anchor the operating

101:58 point of this relationship to
the value of hunting adequacy

102:05 equals to 1 means
some lifespan that

102:09 is the middle of the starving
time and the full lifetime.

102:15 That is not intuitive for me.

102:19 Hearing that, I would say,
OK, I can follow your logic.

102:22 But if hunting adequacy-- the
way I think of the concept

102:26 is, if it is 1, then I
should get my full lifespan.

102:30 Why do you kill me halfway?

102:32 So it is not wrong.

102:35 Mathematically, it
probably works OK.

102:38 But conceptually, it is
harder to justify it.

102:41 There is also, technically,
you want your operating point

102:45 for your model, when you
are normalizing your model

102:48 and trying to set your
baseline equilibrium level, not

102:53 to be somewhere in the middle of
these time constants or things

102:57 like that.

102:58 It just becomes much harder to
put the model in equilibrium

103:02 and get it to behave well.

103:04 You want it to be somewhere
in a more normal range.

103:08 Here, more normal means you
have your adequate life.

103:13 The deer is plentiful, probably.

103:15 And grass is plentiful
or something like that.

103:18 Now, this is a complex model.

103:20 Putting it into
equilibrium is not trivial.

103:22 So you may need to
think more about it.

103:25 And I haven't looked at it.

103:27 So this works, but has
those characteristics.

103:31 Great.

103:32 It was good to look at this.

103:36 But the idea of a single flow
with this type of feedback

103:41 all works, all meaningful.

103:43 

103:45 Also, the formulation
here is a kind of S-shape

103:52 when you have the logistic.

103:56 STUDENT: And that was
kind of intentional.

103:58 My point was saying that,
when you're crossing over

104:03 that threshold of what
you need, your lifespan

104:05 improves quite a lot in
that short little range.

104:10 HAZHIR RAHMANDAD: Yes.

104:12 So You were making
that very responsive.

104:17 

104:23 So I would have probably
thought of hunting adequacy

104:28 to keep it between 0 and 1,
and then normalize around

104:32 the value of 1-- that is,
make that the equilibrium

104:37 region or the baseline region.

104:40 And then you can have
a sigmoid function

104:47 if you think there
is non-linearity,

104:49 which there might be.

104:51 Yeah, if I have 90%
of what I want to eat,

104:54 my life span wouldn't
come down as fast.

104:57 And then there is a point that
it does come down very fast.

105:00 And then it doesn't matter
if I'm getting 10% or 20%.

105:04 I'm going to die.

105:05 So that is fine.

105:07 I think the S-shaped
logic here does

105:10 have a good biological
support for it.

105:15 STUDENT: But you were saying
that the anchor should

105:17 be on the ends of
these distributions?

105:21 HAZHIR RAHMANDAD: Not always.

105:22 So in this case, it
is hard because, when

105:24 you put it to the end
of the distribution,

105:26 it wouldn't saturate.

105:28 So you have to go a
lot, to a lot of deer.

105:32 And a lot of deer
may not give you

105:34 equilibrium on the other
parts of the model.

105:36 So that's why I'm saying putting
this model into equilibrium

105:39 is not actually always easy.

105:41 You need to-- so in terms of
the explaining and the logic,

105:47 it is easier to put
your anchor at the point

105:51 where you're getting
what you want.

105:54 In terms of getting the
analytical equilibrium,

105:57 it may or may not be.

105:59 You have to write it and see if
you can get [INAUDIBLE] Good.

106:05 Anybody else wants to
look at their model?

106:09 Anything else that is here
that we want to look at?

106:12 STUDENT: [INAUDIBLE]

106:15 HAZHIR RAHMANDAD: Yes.

106:16 STUDENT: In my mind there's
a requirement [INAUDIBLE].

106:18 

106:22 What was the bit about hunting
efficiency should actually be--

106:25 HAZHIR RAHMANDAD: Oh, yes.

106:27 So here, the hunting
efficiency is a parameter

106:32 that is basically saying how
many deer per wolf per month

106:36 are being hunted.

106:39 OK.

106:40 And then there is the
required prey per predator.

106:44 That is too how many
deer per wolf per month

106:49 is desired to be hunted.

106:51 And the two are conceptually
very close to each other.

106:55 Now, Alexander had
this idea in mind

106:57 that I want-- maybe my
hunters are not good hunters.

107:01 And in fact, in this
version, then they

107:04 should die in some way.

107:07 I'm not simulating it.

107:09 There are other reasons for it.

107:10 They're not going extinct.

107:12 But if they can't even hunt what
they desire in their best case,

107:18 then they are in big trouble.

107:19 That's challenging for them.

107:24 But I was saying, it is better
not to separate these two

107:27 parameters, to have
a single one that

107:29 is desired prey per predator.

107:33 That desired will determine
both the required hunting

107:37 and hunting efficiency.

107:39 That's the same
thing, basically,

107:41 except that hunting
efficiency also

107:42 has the effect of prey
population and efficiency.

107:46 STUDENT: [INAUDIBLE] I need
15 deer a year to survive.

107:54 But at this base rate,
I'm going to eat 25.

107:58 HAZHIR RAHMANDAD: Yes.

108:00 So that difference comes from
effective prey population.

108:03 So that is captured here.

108:07 But otherwise, it
should be the same.

108:10 OK.

108:11 [? Albert? ?]

108:13 STUDENT: [INAUDIBLE]

108:15 

108:33 HAZHIR RAHMANDAD: So we
have the predator, prey.

108:35 And let's look at a few things.

108:39 So consumption
rate of prey comes

108:44 from consumption per predator.

108:50 Sorry, consumption
is per predator.

108:52 And that comes from
normal consumption

108:54 per predator and effect
of density on consumption.

108:59 So effect of density
on consumption

109:02 comes from density of prey
versus a reference density,

109:08 and then normalized by
sensitivity of consumption rate

109:14 to density.

109:16 So we can see this.

109:17 

109:21 So this is if y density
equals reference--

109:26 so let's think of the
reference density of prey

109:29 to be maximum carrying capacity.

109:33 Is that what you had
in mind, [? Albert? ?]

109:37 STUDENT: No.

109:37 HAZHIR RAHMANDAD: No.

109:38 So what is that?

109:41 STUDENT: I was anchoring
from the prey death rate.

109:49 So there's a death rate that is
if you have ample food, that's

109:53 a fraction of death rate.

109:55 And that implies the
normal consumption rate, so

110:02 the desired consumption rate.

110:04 And that anchored the
reference density.

110:08 That is, in that density, you
will have that consumption rate.

110:16 HAZHIR RAHMANDAD: But this is
not anchored to anything else.

110:19 This is just a number
reference by density.

110:24 So it's just how many prey
per unit of land you can have.

110:32 STUDENT: So in that
kind of density,

110:34 then the predator can
have catch how many--

110:41 HAZHIR RAHMANDAD:
Yes, they can get,

110:42 how many deer they want to get.

110:45 So that's fine.

110:47 But if this is not the maximum
for predator population--

110:53 for prey population, sorry.

110:55 It's not the maximum
density for prey population,

110:58 then this ratio of y
divided by reference y--

111:03 STUDENT: Can go beyond--

111:04 HAZHIR RAHMANDAD:
Can go beyond 1.

111:05 And then that ratio raised
to this sensitivity power

111:09 can go beyond 1, which means
that consumption per predator

111:15 can go above the normal
consumption per predator.

111:19 And that you don't
want to happen.

111:22 STUDENT: I was in the
similar realm with Kathy

111:25 that, if you have
more density, then

111:28 you might go above your
normal consumption.

111:31 HAZHIR RAHMANDAD: Yeah, maybe.

111:32 But even then it
should saturate.

111:37 That is, yeah maybe somehow
you could argue for 20% more,

111:41 but it shouldn't go to infinity.

111:43 And this allows it to
go to large numbers.

111:46 And I'm not seeing yet--

111:49 we can look at it.

111:49 But I'm not yet seeing how the
prey population would remain

111:53 below the reference density.

111:54 And therefore, I
suspect this ratio--

111:58 and therefore, this effect--
could exceed 1 very easily

112:01 in this model.

112:04 So that would be perhaps
the primary issue.

112:08 Now, there are
different solutions.

112:10 And we discussed different
ways of formulating it.

112:13 But ultimately, this effect
should saturate at 1.

112:17 And then you multiply it
by normal consumption.

112:20 And you can call that
maximum consumption

112:22 so that when you multiply
it by maximum, you get--

112:27 by this effect, you
get maximum at the end.

112:29 You can't go above that.

112:32 But the rest makes sense.

112:34 And then you have
consumption per predator.

112:39 That creates a food
scarcity effect

112:43 compared to the normal
consumption per predator.

112:46 That's good.

112:46 That's the same
idea we discussed.

112:49 And it is good to get it from
this part of the formulation,

112:52 rather than another parameter
being defined for that.

112:57 Then you have the effect of
food on death rate of predator.

113:01 So that effect is--

113:06 let's see.

113:07 This is also-- so
this is e to the power

113:17 of some parameter multiplied
by this food scarcity.

113:22 And for now, let's think
about the active range

113:25 of food scarcity to be
mostly between 0 and 1,

113:28 even though it could go
above 1 in our formulation.

113:34 We can look at the
equation for food scarcity.

113:36 

113:40 OK, so maximum of 0
and normal consumption

113:45 minus actual consumption
divided by normal consumption.

113:51 So if normal minus--

113:58 OK, I see.

113:59 So 1 here means you don't
get anything to eat.

114:03 You don't get any
of what you want.

114:06 STUDENT: Food
scarcity of 1 means--

114:10 HAZHIR RAHMANDAD: Yes, food
scarcity of 1 means famine.

114:12 And because of the max
0, even if y consumption

114:15 goes above desired or normal,
it doesn't go below 0.

114:22 So it is robust on that part.

114:26 So this works fine.

114:27 So now, with that understanding,
let's go back to the equation

114:32 for effective-- so this
number is between 0 and 1.

114:35 1 means significant scarcity.

114:39 So then that
significant scarcity

114:41 is multiplied by
some multiplier,

114:52 e to the power of that.

114:53 

114:57 That can lead to
large death rates.

115:00 

115:04 And then 1 minus
fractional death

115:06 rate of r with ample
food, it should not go--

115:13 

115:19 So I have a unit problem
here that I'm not sure--

115:23 STUDENT: The 1 should be the
max fractional death rate.

115:27 HAZHIR RAHMANDAD:
Ah, it should be

115:28 max fractional death rate, yes.

115:30 STUDENT: Because we don't
want it to go beyond 1.

115:32 HAZHIR RAHMANDAD: Yes.

115:33 So this is both a unit
problem and a little bit

115:36 of a conceptual issue because--

115:39 so fractional death
rate can go above 1.

115:43 That is, per unit of time,
more than 100% can die.

115:48 That is, if the unit
of time is one year

115:50 and you're going to
die in two weeks,

115:53 the fractional death rate
could be 50 rather than 1.

115:59 So you don't need to
worry about 1 being a--

116:02 and therefore, you
need to explicitly put

116:05 the max fractional death
rate because its unit is 1

116:09 over year in this population
because your, I think,

116:12 time is year rather than month.

116:14 So that's the
source of confusion.

116:16 You may come into this and you
put 1 because you say, yes,

116:19 death rate cannot go above 1.

116:22 But it can, actually.

116:23 If the unit is 1 over year,
it is not a probability.

116:26 It is per unit of time.

116:28 But if we had max fractional
death rate divided

116:32 by fractional death
rate here, that

116:35 becomes OK because now you're
saying we switch to the regime

116:44 where you are killing the deer
with the maximum rate possible.

116:49 This is 1 over--

116:51 it's related to their
starvation period.

116:55 

116:59 This works.

116:59 But it is a very
clunky formulation

117:02 because this exponential
leads to things

117:06 going up, and then getting
hit by this other ceiling

117:09 that you are imposing.

117:10 So it creates this weird
non-linearity that I don't like.

117:16 It's not doing what you really
want to see in the real world.

117:23 It doesn't happen that way.

117:25 But it puts meaningful feedback
from consumption of deer

117:34 to the death of predators.

117:37 OK, that was good to look at.

117:39 And then the fractional death
rate is straightforward.

117:44 And then you have
[? exogenous ?] [? deaths. ?]

117:46 You have [? assumptions ?]
for that.

117:48 That's good.

117:49 You have the natural death rate,
I assume, fairly similar story

117:55 down here for this.

117:57 And then regeneration
right now is exponential.

118:00 OK, good.

118:05 So maybe we have time to look,
rather than at the model,

118:10 look at some model analysis.

118:12 Anybody wants to
look at their model

118:16 and how its behavior
is explained?

118:19 Anybody who has given
it some thought?

118:21 I saw a couple of you had
submitted some simulation

118:25 analysis as well.

118:26 So Ross, you had some?

118:30 STUDENT: I did, but
my model was basically

118:33 the mathematical model, so yeah.

118:36 HAZHIR RAHMANDAD: OK, let's
quickly look at your model.

118:38 If it is too mathematical,
I may not be able to--

118:43 too mathematical, in the sense
that it is hiding the stories.

118:47 No, this is Jake's.

118:49 

118:53 OK, this one is Ross.

118:57 No, it is not too mathematical.

118:59 It has prey and
vegetation and so on.

119:02 OK, let's run this.

119:03 

119:09 STUDENT: [INAUDIBLE]

119:10 HAZHIR RAHMANDAD: OK, good.

119:12 Good practice.

119:13 Everything starts
from equilibrium.

119:14 Great job.

119:16 Is it analytical
equilibrium or is it--

119:18 STUDENT: It is analytical.

119:19 HAZHIR RAHMANDAD: OK, perfect.

119:21 STUDENT: [INAUDIBLE]

119:24 HAZHIR RAHMANDAD: And
what's the switch?

119:26 STUDENT: Oh, it's for
deforestation shock.

119:29 I specified for four years
that's going to happen.

119:33 HAZHIR RAHMANDAD: Oh OK, so you
have a shock for deforestation,

119:36 for example?

119:37 STUDENT: Yeah.

119:37 HAZHIR RAHMANDAD: I see.

119:38 So you can turn
it on to see what

119:40 happens if you take out some--

119:45 oh, OK.

119:46 

119:49 Huh.

119:50 STUDENT: [INAUDIBLE]

119:52 

119:55 HAZHIR RAHMANDAD:
So you are turning

119:57 on this shock for how long?

120:01 For 48 months.

120:04 Is that correct?

120:05 STUDENT: Yeah.

120:06 HAZHIR RAHMANDAD: So
let's bring it down.

120:08 

120:13 STUDENT: It's a step.

120:15 HAZHIR RAHMANDAD:
So there is a pulse.

120:17 So you can see the pulse
in the fractional death

120:20 rate of the vegetation.

120:21 Basically, more vegetation is--

120:24 and perhaps, this
model-- yeah, this model

120:27 has a built-in oscillatory mode.

120:31 So even if you bring it
to a very small pulse,

120:36 it is still would
create something.

120:38 But it is interesting.

120:40 So with the smaller
magnitudes, it

120:44 takes more time for the pulse
to become stronger, yeah.

120:48 But ultimately, I think it
will get to a limit cycle.

120:53 I mean, I don't know
the formulation.

120:55 We didn't go through your
model's formulations.

120:57 OK.

120:58 But this is good.

121:00 Now, we need to
actually understand

121:02 what is happening in
a model like this.

121:05 And you don't have the
start time for this.

121:09 So one challenge is, with an
oscillatory mode of behavior,

121:15 where do you get it started?

121:16 Because things are
moving too rapidly.

121:20 Have you gone through
trying to understand it?

121:24 STUDENT: I guess I have
rates underneath the graph.

121:28 And I tried to look at more
initial when the shock starts

121:33 in the beginning.

121:36 HAZHIR RAHMANDAD: When the shock
starts, where do you have it?

121:38 Oops.

121:39 

121:45 STUDENT: Looking at the first
0 to 20 maybe time horizon.

121:49 HAZHIR RAHMANDAD: Yes.

121:50 So one of the good
things to do is

121:52 to reduce the time
horizon because you

121:54 don't want to see everything.

121:57 And you can do that in the
time axis part in Vensim.

122:02 In fact, you get the
shock around time 10.

122:06 So we don't really
care about before that.

122:09 And by time 20, 30, 30-ish,
we have the core dynamics

122:15 unfolding.

122:16 So we don't need
to go above that.

122:18 So let's make those as our--

122:22 

122:27 what happened?

122:28 End time is 30?

122:29 STUDENT: Yeah.

122:30 HAZHIR RAHMANDAD: OK.

122:31 Now, typically, Vensim
would not update the graphs

122:41 when we change this.

122:42 But if we now look
at the vegetation,

122:45 it hopefully shows us, yes,
between these two times.

122:49 OK.

122:50 So let's go through
the causal tracing

122:52 and see what is happening that
creates these oscillations

122:56 or at least come up with
a hypothesis for it.

122:59 This is an important process.

123:03 So we don't know what is
generating the oscillations.

123:06 How do we figure that out?

123:07 So start with
whichever you want.

123:10 In this case, vegetation would
be a good starting place.

123:15 The vegetation comes from what?

123:20 You can look at the
causal trace graph.

123:24 It comes from restoration
and destruction.

123:27 Restoration depends
on vegetation alone.

123:30 And you know it is
a reinforcing loop.

123:32 It's not going to create
oscillations for you.

123:35 So you don't even need to go
down the path of figuring out

123:39 restoration.

123:41 There is another
signal to it as well.

123:42 The destruction rate
initially goes up.

123:46 You see, this small
jump up is what

123:50 is triggering the initial
decline in vegetation.

123:52 So that is the driver of
the behavior that gets

123:56 us started with everything.

123:57 So you would know I need to
actually trace destruction rate

124:01 and see where that comes from.

124:04 Now, as I'm thinking
about that, I'm

124:06 worried about this time horizon
because this is too messy.

124:10 I can't easily see.

124:11 So let me limit the
time even further.

124:15 So rather than 30,
let's go to 15.

124:22 And maybe-- yeah, let's keep
9 and see how things go.

124:29 So now, we are going to look
at the drivers of destruction.

124:35 And now, you can see a
clear oscillatory mode.

124:39 

124:43 So what is driving it?

124:45 It is partly the vegetation.

124:48 But that cannot be
the main driver.

124:51 It has to be prey
population that

124:55 is driving the oscillation
because vegetation was coming

125:00 from the destruction rate.

125:04 So then we need to figure out
why the prey population is

125:09 going down.

125:10 

125:17 Then prey population is
based on birth and death.

125:24 So it's interesting.

125:28 

125:34 STUDENT: In this formulation,
the birth rate [INAUDIBLE]

125:39 HAZHIR RAHMANDAD: Yeah, so
I haven't looked at that.

125:41 But my first reaction
was that the shock here--

125:44 the discontinuity
here is very sharp.

125:47 STUDENT: If the birth rate is--

125:49 

125:52 HAZHIR RAHMANDAD: But
before we look at it--

125:54 because normally, you wouldn't--
you shouldn't be needing

125:58 to think about what the
formulations were as much

126:01 as looking at these and deciding
which of these two drivers,

126:04 birth or death, is more likely
to explain the prey population

126:08 dynamics.

126:10 That's the key question.

126:11 And the prey population
is going down.

126:15 But the question is, which of
these two is driving it down?

126:21 Is it because birth is going
down or death is going down?

126:25 What's the answer?

126:25 STUDENT: Birth.

126:26 HAZHIR RAHMANDAD: It should be
birth because death going down

126:29 doesn't lead to prey
population going down.

126:34 So death cannot be the driver.

126:37 It should be the birth
rate that is driving it.

126:40 So now, we can click
on that and see

126:44 what are the drivers of that.

126:47 OK.

126:48 Prey birth rate is going down.

126:51 It could be because of
vegetation going down

126:54 or could be because of the
prey population going down.

126:58 This is a little bit
more tricky at this point

127:01 because, yes, if the prey
population goes down,

127:05 birth rate will also go down.

127:07 So how do I know which
one is driving it?

127:10 Let me look at the valley, The,
minimum in the prey birth rate.

127:17 That is where my cursor is
now on all of the graphs.

127:21 That valley, where we have
the minimum birth rate,

127:27 is happening after the
minimization of vegetation,

127:32 but happening before the
minimization of the prey

127:36 population.

127:38 You see that?

127:39 That's a very important
signal for which of these two

127:42 is more likely to be
driving the behavior.

127:46 Which of the two?

127:47 STUDENT: Vegetation.

127:49 HAZHIR RAHMANDAD: Vegetation.

127:50 So that takes us where?

127:54 Back to where we started.

127:56 So what does that mean?

128:01 What does it mean?

128:04 What does it mean?

128:05 

128:09 It means we have a
candidate hypothesis

128:14 for what feedback
loop is generating

128:17 the oscillations here.

128:19 The candidate hypothesis
is that more vegetation--

128:24 or less vegetation leads
to less prey population,

128:29 which leads to more vegetation--
less vegetation consumption,

128:35 which leads to more
vegetation, which reduces this.

128:38 So this is a balancing
feedback loop.

128:41 It has two stocks on its way--
vegetation and prey population--

128:45 which means it is a higher
order balancing feedback loop.

128:49 So it can generate oscillations.

128:51 The first order balancing
feedbacks cannot generate

128:54 oscillations, but this one can.

128:56 So this is good.

128:57 You already have
a good hypothesis.

129:00 But remember, it is
still a hypothesis.

129:02 So then the question is,
how can we disrupt this?

129:08 Or how can we change this
hypothesis's strength

129:14 and see whether it
changes the behavior?

129:17 So any suggestions
for how would you

129:21 change the strength
of this hypothesis?

129:25 STUDENT: [INAUDIBLE]

129:26 HAZHIR RAHMANDAD:
Anne, go ahead.

129:28 

129:34 STUDENT: OK, cool.

129:36 I think I missed the
explanation for why death rate--

129:41 or rather, why birth rate and
not death rate rates cannot

129:44 affect prey population.

129:46 HAZHIR RAHMANDAD: Sure, let's
look at the prey population

129:48 again.

129:50 So the prey population,
we looked at the causes.

129:53 It can be either birth or death.

129:55 What is it we are
trying to explain?

129:56 The fact that prey
population starts to go down.

129:59 So the fact that it
starts to go down

130:03 means that its birth
should have been going down

130:07 or its death should
have been going up.

130:09 The death is not going up.

130:11 So that means the only
plausible explanation

130:14 is that the birth was going
down, which is the case.

130:17 You could actually use the
valley thing as well here.

130:21 That is, if you go to the
valley of the prey population,

130:25 you see it happens after
the prey birth rate,

130:28 the valley value of
the prey birth rate.

130:30 So that is the driver of what
is happening to the population.

130:35 Whereas, for the death, It is
happening at the same time,

130:38 which is coming from
the stock directly.

130:40 OK.

130:41 Is that clear, Anne?

130:43 STUDENT: Yes, thank you.

130:44 HAZHIR RAHMANDAD: Sure.

130:45 OK, so now, we need a
test for our hypothesis.

130:49 Our hypothesis was that the
prey birthrate, prey population,

130:58 degeneration, vegetation is
the cause of the oscillations.

131:03 So if that is the case,
if I disrupt this feedback

131:06 loop at some point in that
period we are looking at,

131:11 it should disrupt
the oscillations.

131:14 Now, I need to disrupt that
feedback loop without disrupting

131:17 anything else.

131:18 So that part is not trivial.

131:21 

131:24 One way might be to
stop the prey birth

131:27 rate from oscillating.

131:29 If I can rewrite the prey
birth rate to not oscillate,

131:38 to switch to a
fixed number, then I

131:41 have disrupted the
oscillatory mode.

131:44 That's one way to do it.

131:45 Now, we could write
equations to get that going.

131:48 Or we could see what was the
initial value for this variable.

131:53 So it was around 15.

131:56 So I'm going to say to do this.

131:59 So I right click on it.

132:00 I override the default behavior.

132:03 And I would say at time--

132:10 well, if I make it a constant,
and the value should be 15--

132:20 

132:23 let's see if it
is starting at 15.

132:27 Yeah, m is at 15.

132:29 So what are you seeing?

132:32 All of the
oscillations went away.

132:34 And the vegetation is now
going all the way to 0

132:38 because we brought it below
its equilibrium level.

132:43 And then it cannot
restore itself.

132:47 That's partly a function of
how these are formulated here.

132:53 I haven't even looked
at the equations.

132:56 But now, we have
a good hypothesis

132:59 for what feedback loop is
driving that oscillatory mode.

133:02 This was the practice I
wanted you to go through

133:05 because this is how you
identify potentially

133:09 important structures
that are driving

133:14 the behavior you are seeing.

133:16 Alexander?

133:17 STUDENT: Instead of changing the
value of the birth rate itself,

133:20 it seems like there's
that parameter that's

133:24 next to it that controls the
relationship between vegetation

133:26 and birth rate.

133:27 Could you have set
that parameter to 0

133:29 or whatever it is?

133:30 HAZHIR RAHMANDAD: The
problem with that is-- yes.

133:32 But that parameter
perhaps is not

133:34 doing what we wanted it to
do because that parameter--

133:37 my most likely guess is that
it is multiplied by vegetation.

133:41 So if I bring this one to
0, then my prey birth rate

133:47 is going to vanish.

133:50 And then I'm going to change
the prey beyond its equilibrium

133:55 change.

133:55 So this way, at least,
I'm looking at its value

133:58 being at its equilibrium
value, which was 15,

134:01 and seeing how that
intervention impacts it.

134:04 If I basically kill all the
prey or don't let them be born,

134:10 there are more-- it is a
more disruptive intervention

134:13 into the dynamics.

134:14 It will achieve the same thing,
in the sense of disrupting

134:18 that feedback loop, but it
disrupts a lot of other things.

134:21 Even the disruption I
introduced is too much.

134:23 So the best way to intervene
is to keep this as it was.

134:30 We could even do that.

134:31 But basically, put an
if/then/else equation here

134:35 that before time, let's say, 12
it is whatever is the equation.

134:41 At time 12, it switches
to 15, to the value

134:44 that was the equilibrium.

134:46 And then you see whether
the oscillations stop

134:49 at that time 15-- at time 12.

134:52 We could do that
just so that we--

134:55 I mean, now a lot of
things will change.

134:57 So I'm not sure if
we'll get what we need.

134:59 But this would be if/then/else
time is smaller than 12,

135:10 then use this formulation.

135:13 Otherwise, be 15.

135:15 Now, this is all bad.

135:18 I'm putting parameters
into equations and so on.

135:20 Don't follow this practice.

135:21 I'm just showing a
simple piece here.

135:27 And then we come here.

135:30 We go there.

135:33 We just give a shock.

135:38 

135:43 And we make the--

135:49 yeah, we don't need all of
this long and laborious shock.

135:54 

135:58 OK, so everything is
happening as we discussed,

136:02 except that this might be--

136:03 

136:13 prey birth rate never goes down.

136:15 So why is that happening?

136:17 Anybody knows?

136:18 STUDENT: When is your--

136:20 HAZHIR RAHMANDAD: Oh, because
at time 12, we have the shock.

136:23 And I switched this at time 12.

136:24 So exactly, this was not--

136:28 

136:33 if I do it as 14, then we
start to see the oscillation

136:37 before this goes.

136:40 So that's my guess.

136:41 

136:46 OK.

136:48 Yes.

136:49 Now, you can start to see the
oscillations start to happen.

136:52 But then as soon as
we turn them off--

136:55 turn the switch off,
at this point in time,

136:58 there is no more
oscillation going.

136:59 So this tells you that this was
a good hypothesis for explaining

137:03 the oscillations.

137:05 STUDENT: Why do
you need the step

137:07 as opposed to just changing
the parameter value

137:10 as you're saying?

137:12 Because I was thinking
that you could just--

137:14 when you were doing it
earlier, when you just

137:16 changed the parameter value
for birth rate to always be 15,

137:19 you can just
compare the two runs

137:21 because that's the only
thing you're changing.

137:23 Why was that too
much of a disruption?

137:27 HAZHIR RAHMANDAD: So I like to
see that the oscillations are

137:32 starting, and then disrupt it
and see that the disruption

137:37 happens instantaneously.

137:38 As soon as I introduce
this, oscillations go away.

137:41 That's a very strong
signal for me.

137:44 The other way, I would
never see this start.

137:47 So there could be other
things that are happening.

137:49 Now, in this case,
it's easy enough

137:51 that I'm comfortable
going with that,

137:53 but it may not
always work as well.

137:58 OK.

137:59 I think this is good.

138:01 And basically, you folks had
the core structures in place.

138:07 The most common problems-- so
the two most common problems--

138:10 first was these outflows from
the prey or from the vegetation

138:16 not being constrained correctly.

138:19 That is, you let things go out
too much, even if you don't have

138:23 predators, for example, with the
multiplicative formulations that

138:27 were very common.

138:28 The second issue
was the death rates

138:34 that are due to starvation.

138:36 We wanted robust
formulations for those.

138:38 And some of them were
not very well formulated.

138:42 And the third thing is
to make sure they are not

138:45 getting their signals from
different parts of the model.

138:48 That is, you don't create new
parameters that are overlapping.

138:53 We also learned these
constrained formulations

138:57 for removing things
out of stocks that

138:59 does not overwhelm the stock.

139:01 This is something
you have seen before.

139:03 It is in the molecules as well.

139:04 If you look at the molecules,
you will see that as well.

139:08 

139:12 OK.

139:12 

139:15 Yeah, so we talked about these.

139:18 

139:22 Yeah, I think that's good
for the predator prey.

139:27 Let's spend the last few minutes
on the next week's assignment.

139:32 So next week, you are working
on a model of drug development

139:36 pipeline.

139:37 So drug development
has multiple stages.

139:42 You have coming
up with compounds.

139:45 Then you have animal trials
and laboratory tests.

139:49 Then you get into
phase I trials.

139:51 And then you get to phase II
trials and phase III trials.

139:55 And then you launch it
into the marketplace.

139:58 So if you want to make
some amount of money,

140:01 you have to manage this
pipeline from a decade

140:04 or more before to have
the revenue today.

140:08 This is also very stochastic.

140:10 For our purposes, don't worry
about the stochasticity.

140:14 That's too much to
capture in your model.

140:17 Focus on a deterministic version
that basically says each stage

140:22 has a failure rate.

140:23 These failure rates are
actually pretty high, typically.

140:27 So across the three
phases of trials,

140:31 total failure rate is in
the order of 90% or more.

140:35 But it is what it is.

140:39 So with that, your goal
is to formulate the start

140:44 rate for phase I for entering
into phase I. So think

140:50 of those previous steps
as easy to manage.

140:53 So the company can decide to
have 100 new drugs per year

140:58 this year started
into phase I or five

141:01 or whatever is the
number, so that they

141:04 can get the revenue that they
want to have a few years down

141:09 the line.

141:10 So basically, they need to
have some revenue projection.

141:15 And that revenue
projection, think of it

141:18 as a exponential curve.

141:20 That is, we want
our current revenue,

141:23 but growing at a
5% rate per year.

141:28 We want our revenue to
be growing 5% per year.

141:31 How do we start the initial
entry initial start of the phase

141:42 I so that we get
the desired revenue

141:46 trajectory in the long term?

141:48 And this is a stock
management problem.

141:50 That is, if you have too many
items also in the pipeline,

141:53 you don't want to
get started too much.

141:57 And it should be robust
to any percentage.

141:59 So if rather than 5% you go
to 0%, it's a steady state.

142:05 That should work fine.

142:06 Even if you have a
declining rate-- that is,

142:10 I want to actually shrink
my operation and close

142:12 shop in 10 years or
20 years or whatever--

142:15 that should also work.

142:17 So that's your marching
order for this week.

142:22 STUDENT: Resource constraints,
should we think about those?

142:25 HAZHIR RAHMANDAD: So no, unless
you're really pushing yourself.

142:29 So right now, no
resource constraints

142:31 on the start of the projects.

142:35 In reality, there is actually
a very serious optimization

142:39 problem because, as you
increase the number of drugs

142:42 that you start, the
likelihood of success

142:44 actually comes down because you
are pushing in lower probability

142:49 items.

142:50 So a good model would
actually capture that.

142:54 And then you have
to decide how much

142:56 cost there is versus
how much expected

142:59 benefit given this reduction
in the likelihood of success.

143:04 Hassan?

143:07 Go ahead, Anne.

143:09 STUDENT: So how does the
company get the revenue

143:11 at the end of the
number of drugs

143:14 that make it to the last stage?

143:16 HAZHIR RAHMANDAD: Yes.

143:17 Then they go into the market.

143:19 They stay on the
market for a while.

143:22 And then they come
out of the market

143:24 because, basically-- they
don't come out of the market.

143:27 Their patents expire.

143:29 Generics come in.

143:30 You stop making money from them.

143:32 Now, you don't fully stop
making money out of them.

143:35 But for first order
approximation,

143:37 let's assume, once
the patents expire,

143:40 you are not going to make
any more money on that drug.

143:43 Now, reality is a
little bit more complex.

143:47 STUDENT: [INAUDIBLE]
the clinical trials

143:49 system has threshold dynamics
embedded to the last stage of

143:55 [INAUDIBLE]

143:57 HAZHIR RAHMANDAD: No.

143:58 So the threshold
dynamics in the sense

144:00 that the availability of
other drugs on the market

144:02 impacts the acceptance
rate or what?

144:05 STUDENT: Yeah, so for
it to get FDA approved,

144:08 it has to outperform whatever's
on the market in some sense.

144:10 HAZHIR RAHMANDAD: Yeah,
exactly, so the availability

144:12 of other drugs.

144:13 No, don't worry about that.

144:14 That's too much to
do in this model.

144:17 So this is really
the stock management,

144:22 but with failure rate
and with growing demand

144:27 and how you incorporate
those into your modeling.

144:32 So as such, it is not very
different from your stock

144:35 management in assignment 6.

144:38 But it has these
additional pieces.

144:42 So in light of the time, we
have, let's just think about--

144:48 basically, you should
start from what you already

144:52 know for stock management, but
then incorporate failure rates.

144:57 Make sure you are
incorporating adjustments

145:00 for different stocks.

145:01 So there are desired levels
for each of these stocks

145:03 in the work in progress.

145:05 That is, you have phase
I, phase II, phase III.

145:08 These are your work in
progress equivalents

145:12 for the inventory management
model that you need to adjust.

145:18 And then when you get
the full model in place,

145:23 you want it to be able
to match your desired

145:26 revenue over the longer term.

145:29 You want it to also get
there relatively quickly.

145:34 So if it is starting
from a point

145:37 that it is not matching
the desired trend,

145:41 it can quickly move
towards that desired trend

145:46 and not overshoot or
oscillate in a weird way

145:53 when you're exposing
it to a step function,

145:55 a step increase in desired
revenue, for example.

146:00 So those are the key
consideration sets

146:07 for a good model.

146:09 Questions?

146:10 

146:13 STUDENT: Failure rates
can happen at any stage?

146:15 HAZHIR RAHMANDAD: Yes,
failure rates at any stage.

146:17 Put a parameter for the
fraction that get failed.

146:20 Use first order delays.

146:22 Don't worry about the fact that
these clinical trials take time

146:26 and are not really first order.

146:27 It is OK for our purposes to
go with first order delays.

146:30 STUDENT: [INAUDIBLE]

146:32 

146:35 HAZHIR RAHMANDAD:
No, they also expire.

146:37 So there is a life cycle, yeah.

146:39 STUDENT: But they don't have
a failure rate [INAUDIBLE]

146:41 HAZHIR RAHMANDAD: No, they
don't have a separate failure.

146:43 So for now, assume
each drug on the market

146:45 creates some amount
of revenue per year.

146:50 And that's all you care about.

146:53 Jason?

146:55 STUDENT: Should we assume
constant failure rates

146:57 [INAUDIBLE]

146:59 HAZHIR RAHMANDAD:
Constant for now.

147:00 So don't worry about that.

147:04 Good?

147:06 OK.

147:08 

