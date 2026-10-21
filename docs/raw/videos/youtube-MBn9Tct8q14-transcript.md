---
title: YouTube Transcript: Session 6: Ponzi
created: 2026-10-21
updated: 2026-10-21
type: source
domain: ai
classification: general.media
tags: [youtube, transcript, MBn9Tct8q14]
sources: []
published: 2026-10-21
time_sensitive: True
---
source_url: https://www.youtube.com/watch?v=MBn9Tct8q14
source_type: video
ingested: 2026-10-21
duration_minutes: 155
language: en
sha256: ab4ab39327a23336eea44d59c7c78342cdf6e59a737785e94d3d211e2d0a3abb
---

# YouTube Transcript: Session 6: Ponzi

## Video Information
- **Title**: Session 6: Ponzi
- **Video ID**: MBn9Tct8q14
- **Published**: Unknown
- **Views**: Unknown
- **Language**: en

## Transcript
00:00 [SQUEAKING]

00:02 [RUSTLING]

00:03 [CLICKING]

00:07 

00:11 HAZHIR RAHMANDAD: OK,
let's get started.

00:13 So today, we have
the Ponzi model.

00:16 Basically, interestingly
enough, we kind of

00:20 asked Yvonne and Ryan
to basically work

00:28 on this Ponzi model a while back
as part of their PhD admission

00:34 process.

00:35 So they are familiar
with the problem

00:37 as well, although
kind of the version we

00:39 gave them was a little bit
different but largely similar.

00:43 And the basic prompt is to
build a model of the Ponzi,

00:49 try to stay grounded
in the case,

00:51 but also think of a
more generic version

00:54 that can apply to other
settings, Ponzi-like schemes

00:58 or schemes that may not be
nefarious as Ponzi was but maybe

01:03 even legal as long as you are
not deceiving the investors,

01:08 it is fine.

01:09 So let's start with what we
did in the previous sessions

01:14 as well, which is what
were your common challenges

01:19 and take it from there.

01:21 So what were some of
the common challenges

01:25 that you were facing as you were
trying to build the Ponzi model?

01:30 

01:33 And folks online, please
unmute yourself and chime in

01:36 and don't wait for us.

01:39 AUDIENCE: I think I'm just
approaching it fundamentally

01:41 the wrong way, but I was having
challenges with the timing of--

01:47 like if they had more
trust, there's the chance

01:49 that they [INAUDIBLE]
they continue their lease

01:52 and their payout is different.

01:54 And it's more dependent on what
the rate of return was promised,

01:58 and maybe I was just
overcomplicating it

02:00 and couldn't make any
sense [INAUDIBLE].

02:03 HAZHIR RAHMANDAD: How to
make the timing of investment

02:10 versus expectations
of return to work.

02:18 It's an interesting question
because you think about it

02:21 at an individual level, it
becomes a messier problem

02:23 that, for each individual, I
was promised three months ago

02:27 with a 50% return.

02:29 Am I getting that
or not and so on?

02:32 What else?

02:35 AUDIENCE: So there's
the element of trust

02:37 of customers in this scene.

02:39 I was a little bit unsure
how visible the business

02:44 is to the customers, but
how much information they

02:47 have from inside the business.

02:49 I went with full visibility,
but I wasn't very comfortable.

02:53 

02:56 HAZHIR RAHMANDAD: Very
important question.

02:58 So if they have no
visibility, then

03:03 the only signal
anybody would get

03:05 is when the Ponzi
fails to pay off.

03:11 Then you can assume there might
be investigations or people talk

03:15 about it and analyze what his
story is versus how viable

03:18 that the story is, and they
start to build some visibility

03:21 into what might be happening.

03:24 And the bigger than the gap
between what he's saying

03:27 and what he's doing creates a
more serious perception problem

03:35 in the public.

03:37 Good, so that's
another important piece

03:39 of the model how
to think about it

03:41 and how much do you want
to model trust explicitly

03:45 and how do you deal with that.

03:47 Other issues, other challenges?

03:51 

03:57 AUDIENCE: Mine was,
[INAUDIBLE], if I'm

04:01 trying to do that in
an individual level

04:04 or an agent-based model,
and the running time

04:08 is just a crazy number.

04:10 HAZHIR RAHMANDAD: So it became
expensive computationally.

04:14 Yes.

04:15 

04:22 It's an interesting example.

04:25 Go ahead.

04:25 AUDIENCE: No, I was
just going to say

04:27 I find it difficult
to generalize

04:28 the exact same model between
Ponzi and Social Security,

04:32 even though they're
very similar.

04:33 But I was trying to [INAUDIBLE]
for a while and then give up.

04:37 HAZHIR RAHMANDAD:
OK, that's fair.

04:39 

04:48 Great.

04:49 

04:52 Any other issues?

04:56 So as we go through it, we will
try to touch on some of these,

05:00 I think, more explicitly.

05:02 I think these are good
problems to have in mind

05:05 because they are
important and tough ones.

05:07 So I guess when I'm looking
at the Ponzi model--

05:11 and I think actually Yvonne
brought up an important question

05:14 that we usually don't
ask in this class

05:16 that what level of
aggregation in terms

05:19 do you go all the way to agents?

05:21 And we have been building
aggregate models in the class

05:24 pretty much for
all of the cases,

05:26 but I think also
for everything, we

05:29 could have gone a
significant level of detail

05:34 at a lower level of
detail to individuals

05:38 or to individual houses
in the retrofit model

05:44 or in the predator-prey for
individual predator or prey.

05:50 So you could have built
very detailed models.

05:56 Part of it is that
we are focused here

05:58 on some of the more aggregate
modeling challenges,

06:02 and part of it is the
computational cost.

06:04 Even though the costs with
increased computational powers

06:08 are increasingly, for a
single simulation, trivial,

06:11 not really something
to worry about.

06:14 But as soon as you want to do
more serious analysis, which

06:17 includes calibration
specifically,

06:20 things will be different.

06:21 That is, if you need hundreds
of thousands or millions

06:25 of simulation for a
simple calibration run,

06:28 then simulation times
that go beyond a second

06:33 will be terribly slow.

06:37 And again, your computational
resources are important.

06:44 So that can change some
of the analysis, some

06:47 of the trade-offs.

06:48 There are two other significant
trade-offs that come to my mind.

06:53 One is that when you go into
building agent-based models,

06:59 it is actually very
intuitive in the sense

07:01 that the concepts are concepts
you deal with in the real world

07:05 more closely.

07:06 So we think of a person,
we think of an animal,

07:09 we think of a house as
a very concrete object.

07:13 And as soon as you are
building a model of that thing,

07:15 that's the first thing
that comes to mind.

07:17 And sometimes,
that means you may

07:19 lock into that level of
aggregation just out of habit,

07:24 out of simplicity,
rather than by thinking

07:27 whether that is the right
choice for your problem.

07:31 And therefore, it has
this kind of an attractor

07:34 in the space of possibilities
that you may converge to

07:38 without enough thinking.

07:39 It doesn't mean it
is the wrong choice.

07:41 It's just that there is a risk.

07:43 There is a kind of
a psychological risk

07:45 of locking into that level of
aggregation, where it is not

07:50 the right choice.

07:51 And then you have
basically not thought

07:55 through the process correctly.

07:56 So that's a subtle but, I
think, actually a very important

08:01 feature of this.

08:02 And to add to
that, there is also

08:06 kind of demand
side pressures that

08:08 may push you towards
that level of more

08:11 detailed level of aggregation.

08:12 That is, people get
impressed when you show them

08:15 graphics with some
agents moving around,

08:19 or deers and wolves kind
of attacking each other

08:25 or whatever that might come
out of an agent-based model.

08:29 It is kind of cool, and cool
is going to increase demand

08:36 from your audiences to
see something like that,

08:40 or you get applauded for
showing something like that.

08:43 And then that increases
the kind of behavioral bias

08:47 we may have towards that
level of aggregation-- again,

08:51 very explicit.

08:52 It doesn't mean sometimes
that is not the right choice,

08:55 but it means there is a built
in bias in favor of that

08:58 level of aggregation
you need to be aware of.

09:01 So that's one set of
questions or issues

09:06 beyond computational question
that we talked about.

09:09 Then there is a
third set of issues.

09:12 And that is about understanding
where the behavior comes from.

09:17 So we emphasize, even
though we haven't

09:19 done as much deep
analysis in this course,

09:22 but we emphasize
building a relationship

09:24 between the structure
that generates

09:26 the behavior and the behaviors
that we are observing.

09:29 If we don't understand where
the behavior is coming from,

09:31 we are saying, that's
just not going to cut it.

09:35 You're not generating
much insight.

09:37 You can't tell whether
it is a bug or a feature

09:40 of the simulation that you
are learning from or being

09:45 misled by.

09:46 So you really need to
make that connection.

09:50 And basically, when
you have thousands

09:52 and thousands or millions
of interacting objects

09:56 in an obscure code,
obscure in the sense of you

09:59 can't delve deeper
as easily to see

10:03 what are the causal chains that
create those macro outcomes you

10:06 care about, it is
much, much harder,

10:09 even with the kind of
deterministic, differential

10:13 equation models with just a
handful of state variables,

10:17 the stock variables.

10:18 We have a hard time
explaining them.

10:20 I think we have seen a few of
those examples in this class,

10:24 but more generally, this
is a pretty hard problem,

10:27 and that is why it is
a very active research

10:29 area to just-- what
are the best ways

10:31 to make the connection
between the structure

10:33 and behavior in the
much, much simpler case

10:37 of deterministic models
with few interacting parts.

10:42 Now you go to a
stochastic models

10:44 with orders of magnitude
more interacting parts.

10:48 The problem becomes really hard.

10:50 I mean, I'm not
saying it is hopeless,

10:52 but there is not even a
serious literature trying

10:55 to do that in a systematic way.

10:57 So then you end up
with all these kind

11:00 of very detailed
models that people

11:02 say, yes, this is the behavior.

11:04 And then you say, why is
that behavior happening?

11:08 And they say, oh, it is
an emergent behavior.

11:10 What do you mean by emergent?

11:11 Basically, it means I don't
understand what's happening.

11:14 So not that emergence
doesn't exist

11:17 as a construct of
microlevel interactions

11:20 can create counterintuitive
macrolevel outcomes,

11:24 but as a way to push
aside understanding,

11:31 that is a bad concept to use.

11:34 So those are three of
the reasons I'm usually

11:38 trying to push myself to think
hard at the beginning, what's

11:42 the right choice in terms
of the level of aggregation,

11:45 rather than going down
the trajectory of building

11:48 a very detailed
model and then being

11:52 disappointed for any of these
reasons that we discussed.

11:55 

11:59 So very generally, when is
it a good idea to use an ABM?

12:02 I've heard something
that if you want

12:04 to look at the distribution
of something across regions,

12:06 it's good.

12:07 So distributions are
potentially important.

12:09 So you need more details to
get the distributions well.

12:14 And there are interactions--
for example, network structure,

12:20 how it impacts outcomes.

12:22 To capture that, you really
need to go one level deeper.

12:25 And sometimes that
is really important.

12:28 In diffusion models,
when you're looking

12:30 at local diffusion,
sexually-transmitted diseases,

12:34 they go through local networks.

12:35 Modeling those at the
network level adds value.

12:39 Now that once you understand
how it works at that level,

12:43 you could actually build
more aggregate models that

12:45 capture the features of that
more detailed model as well.

12:50 So sometimes, it
is actually a way

12:52 to discover what is
the mechanism that you

12:55 need to capture at a higher
level of aggregation.

12:58 So many of the kind of
good agent-based modelers

13:02 kind go between these levels
because they say, sometimes, I

13:05 need to actually go very deep,
build all of these things,

13:09 and then I'll discover that
there are two or three core

13:12 mechanisms that need to be
accounted for in the more

13:15 aggregate version of the model.

13:17 Then I can build a more
aggregate version of the model

13:19 that has those features.

13:21 But at the beginning,
I didn't know that.

13:23 So that's another way.

13:25 There is a kind of
another possibility,

13:28 and that is when
policy levers are

13:31 very customized at the kind
of level of individual.

13:34 And you need to see the
impact of those policy levers

13:38 that are kind of
differentiated based

13:40 on very detailed
characteristics of actors.

13:43 So that's another area.

13:45 So those are some examples.

13:47 AUDIENCE: Just a
general questions,

13:50 which I think is related.

13:51 Then how do people
understand the behavior

13:54 of ABMs because, surely, some
people do it [INAUDIBLE]?

13:57 HAZHIR RAHMANDAD:
Yeah, so I think

14:01 the best practice is they try
their best at the level of agent

14:05 to make sure it is very robust.

14:07 So all of the extreme
condition thinking

14:09 that we bring to
our equations, they

14:10 run through that for
the individual agent.

14:14 And so that with the range
of inputs that it can get,

14:19 it behaves meaningfully
and reasonably.

14:22 So that way, you make sure
the model is generally robust,

14:25 and at least you are not looking
at noise or kind of error

14:29 in code or something,
but it doesn't fully

14:33 explain what is
generating the behavior.

14:37 Then it is basically we went
through the kind of hypothesis

14:43 testing by cutting loops.

14:44 So you have a hypothesis for
what is generating things.

14:47 And then you cut
the loops, and you

14:49 see whether that
behavior goes away.

14:51 You can do that type of
deep analysis with an ABM.

14:54 That is, whenever
you see a behavior,

14:57 you should come up with a
hypothesis for explaining it.

15:00 Then go through
cutting that mechanism

15:03 and seeing whether that
behavior goes away.

15:05 So that scientific
method of testing

15:08 applies to ABMs as well as any
other model as well as bigger

15:11 problems, other problems.

15:13 So that's the channel typically.

15:16 What happens in
practice is that it

15:18 is harder to do, so you
usually end up with models that

15:22 are dynamically simpler-- that
is, they have fewer feedback

15:25 mechanisms and
interacting parts,

15:29 conceptually interacting
parts, but then

15:31 much more detail within the
components that you have.

15:35 So you may have agents that
are people interacting.

15:41 And in our setting,
it might normally--

15:44 in an aggregate model, you may
have just a reinforcing loop

15:47 of a Bass diffusion model.

15:49 And you say, OK, this
is a very simple model.

15:52 Let me add this
and that and that.

15:54 In that ABM formulation,
you may stick with that,

15:57 but then you start to say, OK,
what is the tail of distribution

16:02 of adoption doing
to the rest, or how

16:04 it is changing the dynamics.

16:06 And then you would incrementally
add complexity and understand.

16:11 So those are ways to do it.

16:12 But none of those are kind
of algorithmic automated ways

16:17 of doing deep analysis.

16:20 So going back to
the question of--

16:25 

16:31 I would be typically
looking at when

16:34 I'm looking at the Ponzi model,
so this is about investment.

16:42 So you have people who
are investing in Ponzi

16:45 or in whatever the scheme
you're talking about.

16:48 There is money that they bring
in and then is paid to people.

16:51 So there's kind of the
stock of money that matters.

16:54 And then there is liabilities,
what Ponzi owes people.

16:58 And these two are
conceptually different,

17:00 even though they are
close to each other.

17:01 And if you don't make that
conceptual distinction,

17:04 and you try to mix them
together, things don't work out.

17:07 So that's one of
the first places

17:09 that sometimes people have
trouble with this problem.

17:13 Then there are the dynamics of
investor acquisition and people

17:17 leaving the scheme
and what drives that.

17:20 I think kind of there
are basic formulations

17:23 you can use from standard
methods like Bass diffusion

17:27 model with word of
mouth, with saturation.

17:30 But then there is this risk
and reward considerations.

17:35 How do you decide what
is the infectivity

17:37 or what is the adoption
rate at any point in time

17:41 or the withdrawal rate
at any point in time?

17:44 And that goes to the
question of reputation

17:46 that has some brought up.

17:48 How do you make
good formulations

17:50 for reputation that
are operational?

17:52 You can connect it to risk
and reward very closely.

17:57 They are well-balanced
in the sense

17:59 that when you formulate the
model for initial condition,

18:06 whatever is kind of
ponzi's initial condition,

18:09 it works with that.

18:10 But then you can think
about the extreme

18:11 when everybody now trusts
Ponzi or the other extreme when

18:15 everybody has lost trust
in him and his scheme,

18:20 the model should behave.

18:21 That trust formulation
or reputation formulation

18:23 should work well.

18:26 And then all kinds of
robustness to extreme conditions

18:31 are important as well.

18:32 So those are questions
when I'm entering,

18:34 looking at these models
in the back of my mind.

18:37 I'm just kind of highlighting
what is happening.

18:39 So now is a good time
to switch to the models.

18:43 And I think we have
a dozen of them.

18:47 So let me bring them.

18:49 Let's go through a few of them.

18:53 So let's first look at how the
stocks and flows are structured

18:57 across different ones.

18:58 So this is, in a way,
the first session

19:01 we have a more
open-ended problem.

19:05 So I expect a lot more
variance in this one compared

19:08 to the previous ones
because the previous ones

19:10 we had a lot of detail in how
the problem was defined already.

19:17 So this is by Ross.

19:19 And here, we have
investors stocks and flows,

19:23 so new investors and
investors at maturity.

19:29 And I assume, by
investors at maturity,

19:33 Ross means people
who are basically

19:37 have invested with Ponzi.

19:39 They have reached
maturity of their notes.

19:42 They should either
get their money back

19:46 or reinvest into Ponzi.

19:50 And that's kind of what
it is structured here.

19:53 Conceptually, those are
good categories to have.

19:55 There is a question-- do you
need a stock for investors

19:59 at maturity, or
it is fast enough

20:01 that process that this is really
the flow of people leaving

20:07 or going through maturing?

20:08 And then at that
point, they split.

20:10 They decide which
path they take.

20:15 It is an interesting
question, which

20:18 I think, in the Ponzi's
case, this is also

20:21 a good idea, potentially,
to have that explicitly,

20:24 but it may be a
bit of an overkill.

20:28 Then you have the principle
that is owed, principle invest,

20:32 and interest owed at maturity.

20:35 So that's how much
these people are owed.

20:37 And then you have money at hand.

20:40 And then you can, for
accounting purposes,

20:43 look at the money
that was collected.

20:45 So I like these
stocks and flows.

20:47 You have people.

20:48 You have money that--

20:51 liabilities.

20:52 This is money owed
and then actual money.

20:55 Let's see how others have this.

20:58 So this is what we just opened.

21:04 This one is Jason's.

21:07 So Jason has also
peoples, but this

21:11 is closer to assignment 4, so
people who are not interested,

21:16 then potential investors, new
investors, mature investors,

21:21 and former investors.

21:24 And then you have new
funds and mature funds

21:31 which go with mature investors,
if I'm understanding correctly.

21:35 But what does the meaning of
the new versus mature investors

21:39 mean here?

21:40 AUDIENCE: The thought
was, in reality, the money

21:46 that everyone brings
in ages with them

21:48 as they go through the fund,
but their returns will only

21:54 mature if investors
earn returns, which

21:58 are coming from the
total funds that we're

22:00 taking from the new
people total fund divided

22:05 by the mature population.

22:07 

22:09 HAZHIR RAHMANDAD: So what is the
definition of mature investor

22:12 versus new investor?

22:13 I just want to understand
what's the distinction.

22:16 Is it the people--
so mature investors

22:18 are similar to Ross's,
people whose investment

22:22 has reached maturity?

22:23 AUDIENCE: Yeah.

22:23 HAZHIR RAHMANDAD: OK, got it.

22:24 AUDIENCE: After a year,
you're not earning anything.

22:26 And then--

22:26 HAZHIR RAHMANDAD: It's
actually 45 days or something

22:28 when they get into the maturity.

22:31 But then these guys can't
reinvest, so they don't go back.

22:36 So that's the assumption
in this model.

22:39 This one is from Alban.

22:42 

22:46 So Alban also has an-- oh,
actually, the previous one.

22:51 Does it have money
separated from what is owed?

22:55 So this is money or what--
they are the liabilities?

23:01 AUDIENCE: I don't have
the liability explicitly--

23:03 HAZHIR RAHMANDAD:
So that probably

23:06 will create some
problems, although we

23:08 should look at it to be sure.

23:10 Then Alban has this
structure with investors

23:16 that are potential investors
active, waiting to be paid.

23:20 So this is very similar
to Ross's structure.

23:24 And then investors
that have left.

23:27 Then you have the
liability or debt,

23:29 and you have the
cash in the scheme.

23:31 So this is kind of
similar architecture

23:34 that we saw with Ross's model.

23:37 And I think it's a good
set of options to have.

23:41 This one is search-ins.

23:45 And we have investors
potential versus those

23:50 that are current investors.

23:53 Then you have
money that is owed,

23:56 and then you have
money available.

23:59 So this is separating cash
and liability, and then

24:06 total defaulted payment.

24:09 So you're capturing
something that

24:11 can be traced into basically
trust reputation based

24:17 on defaults.

24:19 So that's one way to
capture the trust dynamics.

24:23 So that's this model.

24:27 AUDIENCE: We have Hesam's
here with cash, liability,

24:36 and so Hesam is formulating
people rather than people

24:42 as how much money they
can bring into the scheme.

24:48 And that's OK.

24:49 I think that's also--

24:50 HAZHIR RAHMANDAD:
I didn't consider

24:52 [INAUDIBLE] maturity period.

24:54 That's something I thought
investors can cash their money

24:57 and profit--

24:58 At any point in time, yeah.

25:00 That's not too bad.

25:03 I think it could work fine for
as-- it's a good first order

25:08 approximation.

25:09 So we could talk about that.

25:10 So this is kind of the fairly
simple but has similar ideas.

25:16 And as long as you are
in the recruited funds,

25:20 you are reinvesting potentially.

25:22 So the reinvestment
is not separated,

25:24 if I understand correctly.

25:26 

25:28 Then we have Cathy's.

25:32 So we have the investors, those
who are not willing to invest,

25:38 those who are
potential investors,

25:41 and those who are the
current investors.

25:44 There is a flow
back to not willing.

25:47 There is a flow back to not
willing from most of the stocks.

25:51 And then reinvesting can
be captured here as well.

25:55 Then you have cash.

26:01 Then you have trust.

26:04 You don't have liabilities.

26:06 You have something
about failure.

26:09 This is just accounting, not
really having any feedback

26:12 into the rest of the system.

26:14 So the trust is the
more important part,

26:17 if I understand correctly.

26:19 OK, good.

26:21 So this is also missing
the liability part,

26:23 which could prove important.

26:26 

26:30 This one-- Gerardo's
model has delay.

26:39 I don't know what
that delay is about.

26:41 So it's the investment goes into
this and then comes out and--

26:50 we need to look at it more
closely to understand that.

26:53 But it seems to
be money that is--

26:55 what's that?

26:58 AUDIENCE: [INAUDIBLE]
structure to captured

27:01 the effect of the
debt visibility

27:05 on the credibility
of the investor.

27:08 So it's a really bad name,
delay, but this is the sense.

27:15 And there is another page
just for the [INAUDIBLE].

27:18 HAZHIR RAHMANDAD: I see.

27:19 I see.

27:20 So this is more about the
credibility, this part.

27:24 And then you have the money
at hand, available liquidity.

27:31 That's the money at hand.

27:33 I don't know if you
have the-- and then

27:36 you have the Bass diffusion
type for investors

27:39 versus potential investors.

27:41 And then [INAUDIBLE]
has nothing.

27:44 

27:50 Great.

27:50 And let's see next one.

27:53 

27:57 This one is Jake's.

28:01 So we have investors that are
scheme seem susceptible, yes,

28:09 scheme susceptible population.

28:11 This is-- can go into
investors and then

28:15 go into formally invested.

28:19 And then if they're unpaid,
they wouldn't go back.

28:23 Then you have the money and--

28:27 AUDIENCE: The way
I thought about--

28:29 I mean, my liabilities
is a simpler one,

28:31 where it's just desired money in
terms of if I know somebody soon

28:34 I'm going to have
to pay out, then

28:36 I go and hastily try to recruit
two more to or multiple more

28:41 to Venmo.

28:42 HAZHIR RAHMANDAD: I see.

28:43 So we can revisit kind
of the formulations

28:47 there in the next round.

28:48 And then I think this
is the last one, Ali's.

28:54 AUDIENCE: [INAUDIBLE]

28:55 HAZHIR RAHMANDAD: So this
is similar to the sum--

28:59 funds, liabilities, and cash.

29:01 So you guys coordinate
with each other.

29:04 But that's all right.

29:07 That's all right.

29:07 

29:10 So now kind of big picture--

29:13 we had these three, four
categories of people.

29:18 You could break it down
based on whether they

29:21 are potential investors
from scratch or unwilling

29:24 and then become potential
and then become investors.

29:28 I think capturing
unwilling population

29:30 is an interesting idea.

29:32 I think a lot of
investments, people

29:35 start with being very skeptical.

29:37 But you could also
capture that skepticism

29:40 through some
mechanism about trust.

29:42 That is, everybody is
a potential investor

29:45 is just that they are very
skeptical at the beginning.

29:49 That is, the priors,
the initial perception,

29:52 if you hear somebody is
promising 50% return in 45 days

29:56 is like, this is a
scam, I'm not going

29:59 to look at it even
or think about it.

30:02 So there are these
two different ways.

30:04 But if you are going with
the second way of using trust

30:08 to model that, you
need a machinery

30:11 for modeling trust, that
probably needs a stock

30:14 variable somewhere there.

30:15 So that it changes over time.

30:17 That is, you need to put an
initial value for the trust

30:20 level or kind of expected return
or something along those lines.

30:24 Then we have the
liability and the cash.

30:29 Those are pretty
physical, clear as well.

30:31 Then the fourth stock
and flow is about trust.

30:34 Now whether you capture it
as explicit stock and flow

30:38 or not is a choice.

30:39 And I think most of you
have simpler versions

30:42 based on return rate of whether
you are able to pay back--

30:47 your formulating that.

30:48 Now let's start doing deep
dives into perhaps the liability

30:54 and cash part.

30:55 It is kind of instructive
because they're not

30:59 super complicated, but they
have enough interesting pieces

31:06 to make it worth
taking a look at them.

31:09 So this is Ali's.

31:12 We can just look at this
one as a starter point.

31:15 So when you recruit investors,
you are issuing liability.

31:22 And this is in the
units of people--

31:26 oh, sorry, funds because you
guys are modeling it as funds.

31:29 So that simplifies
your life that way.

31:33 So the liability goes
there and the same amount

31:35 goes into your incoming cash.

31:36 So that's straightforward.

31:39 Then, at the end of the period,
so you have a delivery time--

31:46 I'm sorry, let me see.

31:48 How does the exit happen?

31:50 So you have people who are--

31:52 

31:55 so there is a indicated--

31:57 AUDIENCE: You have a confidence
in the business, which is

31:59 characterized by [INAUDIBLE].

32:01 HAZHIR RAHMANDAD: Yes.

32:03 So you are assuming-- so this is
actually an important assumption

32:06 here, that this confidence is
cash divided by a liability plus

32:11 some small number so that you
don't have overflow when you

32:16 get--

32:16 AUDIENCE: People know
that how much cash--

32:18 HAZHIR RAHMANDAD: Yes,
so the assumption here

32:20 is very important.

32:21 So there are two assumptions
that are important.

32:23 The first one is the bigger
one is that people know what

32:26 is the cash that Ponzi has.

32:28 That is usually not
a good assumption.

32:30 I mean, we could debate,
but most of the businesses

32:36 don't have all of their
detail financials visible,

32:41 at least not the ones that
are not publicly traded.

32:43 Now, publicly-traded companies
have a lot more requirements

32:46 for visibility.

32:47 And part of it is
exactly these dynamics.

32:49 That is, once you
remove that visibility,

32:52 the balancing feedback
loops go away,

32:56 and things can get really messy.

33:00 So I would be OK as
long as you understand

33:07 that you're making a
strong assumption here

33:09 and have a way to get out
of that strong assumption.

33:12 That is, you can say, OK,
I have this switch that

33:15 says how much this
confidence matters versus

33:19 some other version of confidence
that is not reliant on this cash

33:24 to liability ratio.

33:26 I mean, you could even have
that ratio raised to some power.

33:30 And if that power
is 0, basically, you

33:34 get to there is no
effect from this side

33:38 or something along those lines.

33:40 So right now, if liability
is much bigger than the cash,

33:46 then indicated
withdrawal goes up.

33:48 The way it is
formulated is liability

33:51 multiplied by deserting
factor multiplied

33:54 by 1 minus confidence.

33:56 So deserting factor
is just a factor

34:01 that takes care of the units.

34:03 So 5% of people leave
every day as soon as--

34:08 assuming that there is no
confidence, looking back

34:11 at this formulation.

34:13 But let's be a little bit--

34:18 this is cash divided
by liability.

34:20 So if cash divided by
liability-- then as long as cash

34:24 exceeds liability,
this number should

34:27 be above 1 which leads
to negative values for 1

34:32 minus confidence.

34:34 And negative values
for 1 minus confidence

34:37 are not a good idea because,
then, your settling liability

34:41 thingy will go negative.

34:44 AUDIENCE: So the assumption
is that this is a scheme.

34:48 HAZHIR RAHMANDAD: No,
so that's not-- yeah,

34:49 but you shouldn't
build assumptions

34:52 like that hidden
inside equations.

34:54 So the key thing here is let's
go with the first assumption

35:00 that people can see the
confidence or can see the cash

35:04 and can calculate
the confidence.

35:06 Still, the confidence
should not go above 1

35:09 in the next part
of the equations.

35:11 Maximum confidence is 1.

35:13 So as such, you want this to
be minimum of 1 and this ratio

35:19 rather than the ratio alone.

35:22 Otherwise, you create the
risk of settling liability

35:26 going negative.

35:27 And then that breaks
down the whole model.

35:31 And yes, in practice, this model
cash is always below liability

35:36 unless you have situations where
you are investing, actually,

35:42 or you bring your
own money into it.

35:44 And both of those
are not impossible.

35:47 

35:51 Now what I like about
this is how simple it is.

35:55 That is, you're just
saying a fraction of people

35:57 will leave the scheme if
they are not confident

36:02 that things are working and
then as soon as they leave--

36:11 I mean, as soon as the
confidence goes down.

36:14 Now, deliverable cash is
kind of a maximum rate

36:19 that you can impose on how
much withdrawal you could have.

36:26 And how are you accounting for--

36:29 

36:31 so you're accounting
for growth in liability

36:34 using this compounding rate.

36:35 So basically, interest rate
goes into compounding interest.

36:40 And so this is also a nice,
simple way of doing it.

36:44 Now you have this--

36:46 AUDIENCE: The reason for
this is that the Ponzi

36:48 person is getting caught.

36:50 So the liability
cannot go grow forever.

36:54 HAZHIR RAHMANDAD: So that's
actually an interesting point.

37:01 AUDIENCE: [INAUDIBLE]

37:02 HAZHIR RAHMANDAD:
Yeah, I don't like

37:03 the way you have formulated it
by just cash bigger than one

37:06 or some kind of ad hoc thing.

37:08 So even if you want to put
some kind of a switch that

37:11 says scheme going bust, and
then if scheme going bust

37:16 has not happened, you continue
with this accumulation

37:19 of liability, otherwise you
wouldn't, rather than build it

37:24 inside the equation,
it's the same idea,

37:26 but it's kind of being
built into the equation that

37:28 doesn't work.

37:29 AUDIENCE: So this is also
saying that a confidence is

37:31 when people never withdraw.

37:33 HAZHIR RAHMANDAD: It is saying
that if confidence is 1,

37:36 people will never withdraw.

37:37 Exactly.

37:37 So is that a good assumption?

37:41 Probably not.

37:42 That is, people would
not leave their assets

37:47 for eternity with the scammers.

37:49 At some point, they want
to use that investment.

37:53 So as such, the formulation
for indicated withdrawal

37:57 perhaps should have
a scaling factor

38:00 that goes from a
maximum withdrawal rate

38:04 when there is no confidence
to a minimum withdrawal rate.

38:09 That is when everybody thinks
this is very legit, no risk.

38:14 But at some point, I would
like to take out my money.

38:17 And so there is a kind
of a maximum residence

38:20 time and a minimum
residence time,

38:21 which are the 1 over
those deserting factors.

38:26 AUDIENCE: This is
another thing--

38:27 I remember you telling us that
every relationship in the model

38:32 should have some
controlling parameter.

38:36 So in this example, if I
were to do this formulation,

38:39 the other issues
aside, I think I

38:42 would be trying to have some
of sensitivity of withdrawal

38:46 and confidence or something--

38:48 HAZHIR RAHMANDAD:
So let's separate

38:49 the two things from each other.

38:51 Not every equation needs
a controlling parameter.

38:54 Some equations are just
mathematical operations

38:57 that bring things together,
so that's not the case.

39:00 Then there is the question of,
OK, sensitivity to confidence

39:05 or something like that.

39:06 Would that be helpful?

39:09 I could go either way.

39:11 So there are two different
ways to formulate.

39:13 So Alexander's question
is an important one

39:15 that is, here, we have
1 minus confidence.

39:18 So once confidence is
defined, this equation

39:21 is deterministic and
is driving things.

39:24 So I could do two things.

39:26 I could add a
parameter here that

39:28 says the sensitivity
of withdrawal

39:30 to confidence-- so if you think
of this one minus confidence

39:34 as a switch that moves
between those two

39:36 extremes of maximum withdrawal
rate and minimum withdrawal

39:40 rate, it could be
a linear thing,

39:43 but it is still could be 1 minus
confidence raised to some power,

39:46 and that power can regulate
how nonlinear that response is.

39:50 Or I can build that
nonlinearity or that response,

39:54 whatever I call it, inside the
confidence equation itself.

39:58 That is, in the
equation for confidence,

40:01 I could make it to
change nonlinearly

40:03 rather than just being the
ratio of the two things

40:06 to be nonlinear.

40:09 I think both of them are
feasible, meaningful ways

40:13 of doing things.

40:14 In this equation, I would
probably do the latter.

40:17 That is, I would build that
inside the confidence equation

40:22 so that when I look at
that confidence variable,

40:25 it is already informing me about
how strong this mechanism is

40:31 kicking in because, otherwise,
I'm calling it confidence.

40:35 But it is some half-baked
variable that is not really

40:40 operating in my model,
and therefore, it's

40:42 not very informative
to double-click on that

40:45 and look at its graphs.

40:46 So that would be
my solution, which

40:49 means I would make the
confidence equation have that--

40:54 if you want to have
sensitivity raised

40:56 to the power of some
sensitivity, take care of it

40:59 there.

40:59 And then when you come here,
you just use that concept.

41:03 Then you can look at the
confidence variable directly.

41:06 AUDIENCE: So your suggestion
is to have, I guess,

41:08 exactly one of the two.

41:10 HAZHIR RAHMANDAD: Yes,
but not both of them.

41:13 So why not both of them?

41:15 Because in this
case, there is no--

41:18 the intermediate construct
that you're generating,

41:21 so let's say, we
made this confidence

41:23 and it had its own parameter.

41:24 And then in the next step,
we had a separate parameter.

41:27 So we had two parameters.

41:30 There are serial
parameters that are just

41:32 compounding on each other.

41:33 We are not taking anything
else from this confidence

41:36 to go in another direction
that has an impact.

41:38 We don't have observables on it.

41:40 So you basically have
redundant parameters,

41:43 and redundant parameters
will cause havoc

41:45 later on when you want to
estimate the model, when you

41:48 want to understand the model.

41:49 So it doesn't help.

41:52 AUDIENCE: I'm just
wondering if you

41:53 can clarify what this
liability construct means

41:58 [INAUDIBLE] supposed to mean.

41:59 HAZHIR RAHMANDAD:
So it is supposed

42:00 to mean how much
Ponzi owes people

42:03 based on how people think
they are owed, or based

42:08 on the contacts because
they are writing contacts

42:10 to pay these people back.

42:14 AUDIENCE: So it's how much
people think they are owed?

42:17 HAZHIR RAHMANDAD: Yes.

42:18 Well, how much people are
owed, let's say that way.

42:21 Let's keep it that way.

42:23 Why are you confused with the
distinction between those two?

42:27 AUDIENCE: Because when
you make an investment,

42:29 you're assuming some risk.

42:31 So why should I--

42:34 HAZHIR RAHMANDAD: So yes,
risk-- let's separate it.

42:37 So risk is about
investments that don't

42:42 have promised rates of return.

42:44 This has a fixed
promise rate of return.

42:46 Now, risk in the sense that it
is part of the business-- that

42:49 is, if it doesn't pay.

42:51 I'm not cheated.

42:52 I invested in the stocks, and
the stocks go up and come down.

42:56 And therefore, even
if it is average

42:58 8% per year over the
last two decades,

43:01 I may be unlucky and get minus
20%, and I can't complain.

43:06 This is not that
type of investment.

43:08 So it was an investment that
says 45 days, 50% return,

43:13 we will guarantee that.

43:15 AUDIENCE: And
then, so with that,

43:18 how is this capturing
that dynamic?

43:24 HAZHIR RAHMANDAD:
So the way this

43:25 is capturing it is a bit tricky.

43:28 So what is the problem
with this formulation

43:30 in terms of Ponzi's stories?

43:32 It is a nice kind
of formulation,

43:34 keeping things very simple.

43:36 But what is the shortcoming
in connecting it

43:39 with Ponzi's story?

43:42 AUDIENCE: [INAUDIBLE]
maturity period.

43:44 HAZHIR RAHMANDAD:
Basically, it doesn't

43:45 have the maturity period.

43:47 So what does that
mean in this case?

43:50 AUDIENCE: You have to
be ready today to--

43:52 HAZHIR RAHMANDAD: It means
as soon as you're matured,

43:55 what will happen in this model?

43:58 It is reinvested
back into Ponzi.

44:01 Now that reinvestment
in the real world

44:04 didn't happen automatically.

44:06 Ponzi was not telling you,
oh, if you didn't come and get

44:09 your money at day 45, I will
reinvest all of your investment,

44:15 and it will grow
exponentially forever.

44:18 He was saying, no, you have
to come get your money,

44:21 then come back and reinvest.

44:23 If you want to do
that, you're welcome.

44:25 But that creates
this kind of group

44:27 of people who have
matured their investments

44:30 but have not yet decided
whether to reinvest or not.

44:34 And that's why the formulation
that Ross and Albon and a couple

44:37 others had makes this a little
bit more explicit and, as such,

44:41 adds some additional value for
the context of Ponzi's story.

44:45 Is the distinction
clear in this case?

44:47 That's pretty important
in the actual story

44:52 because, then, you can
actually create situations

44:54 where the bottleneck is the
payment processing system,

44:59 and that may or
may not help you.

45:02 I mean, sometimes,
it can even help you

45:04 because I'm paying everybody
with my fastest speed.

45:07 It's just that I just have one
processor who's paying people,

45:10 so I'm not failing
to pay people.

45:13 It's just a slow process.

45:15 Yes, wait here.

45:17 There is a three day line
to get your money back,

45:20 and there is another three
day line to invest it back.

45:23 And you can do both of those.

45:25 So capturing all
of that complexity

45:30 requires a lot more
structure, but we

45:34 want to be clear what is
missing when you are going

45:37 with this simple formulation.

45:39 But otherwise, this is a pretty
nice, decent formulation.

45:43 So as soon as you
settle the liability,

45:45 basically, you are paid
or you withdraw the money,

45:50 that money goes out of cash.

45:52 Note that cash availability
is a constraint on that.

45:56 So this is kind of a
maximum delivery rate

45:59 based on availability of cash.

46:01 So if you are not
settling liabilities

46:04 here because delivery
is constrained by cash,

46:09 now things start to look
bad for Ponzi in this case.

46:16 Now I'm not seeing
how that is reflected.

46:20 That is, your
measure of confidence

46:22 here is only getting feedback
from this ratio of cash

46:27 to liability.

46:29 The day that Ponzi
is not paying people

46:32 because he doesn't
have cash, that

46:34 is a very different
day from the day

46:37 before when he was paying people
whatever they were asking for.

46:43 Whereas in this
model, confidence

46:44 is only this kind
of gradual decline

46:48 based on the ratio
of cash to liability.

46:52 AUDIENCE: One thing that
happens though is, because we

46:55 will pay that liability out.

46:57 So if he's short on cash,
whatever cash there is

47:00 will go out in that one day.

47:02 So cash drops to 0.

47:04 Confidence drops to 0.

47:05 It's not exactly as it should
be, but it [INAUDIBLE].

47:07 HAZHIR RAHMANDAD:
So you're right.

47:09 In that sense--
and you could also

47:11 capture it using some additional
nonlinearity in the definition

47:14 of confidence that you have
a cliff-like behavior that

47:18 as long as cash to liability
is above 0.1 or 0.2,

47:23 nothing is happening because
nobody is really seeing it.

47:26 So raising it to a small power,
like raising that ratio to power

47:30 of 0.3 or 0.2, will
give you that behavior

47:34 that you have a cliff like end,
but otherwise, things are fine.

47:39 And that would do a decent job.

47:41 So this is kind of
good to think about it,

47:45 that how does this confidence
formulation address this failure

47:51 mode.

47:52 

47:55 So I'm OK with it, but with
the caveat that then you

48:02 need to make sure this
delivery time is small enough

48:04 that feedback is not lost.

48:09 

48:11 AUDIENCE: One more
formulation question.

48:13 HAZHIR RAHMANDAD: Yes.

48:14 AUDIENCE: [INAUDIBLE] do
compounding interest [INAUDIBLE]

48:16 cash?

48:18 [INTERPOSING VOICES]

48:20 AUDIENCE: Oh, this is the--

48:21 HAZHIR RAHMANDAD: Yes, that's
just that if cash-- yes,

48:24 so that's not really doing much.

48:27 And then he has his
own investments.

48:30 So this is nice to have what
the actual investment of Ponzi

48:34 might be.

48:34 So if there was a legitimate
business, like Social Security,

48:38 you could have that
investment going into it.

48:41 That's fine.

48:44 And then because they have
formulated it with liabilities,

48:49 once you're getting funds
out, you're getting funds out,

48:53 and you're getting
investors out.

48:55 And that's fine.

48:56 There's nothing strange
happening there.

48:59 And then these people, after
a while, may decide to return.

49:03 So this part of the
formulation of people returning

49:07 without any concern for
confidence or anything else

49:11 is a little bit kind of
not a great alternative.

49:17 So the way I would
think of it is

49:19 that people would return only
if the confidence level is high,

49:24 and if you have that
confidence already defined,

49:27 you can use the same
construct for informing

49:30 whether people return to the
pool of potential investors.

49:36 There is also nothing here
about the rate of return

49:40 impacting the choices to join.

49:44 So the recruitment
factor that you have here

49:47 in your Bass diffusion
type of a model

49:49 is kind of just a free
parameter, whereas in practice,

49:53 it should be tightly coupled
to the promised interest rate

49:57 and to the confidence.

49:59 So both of those
are important inputs

50:02 into the recruitment factor.

50:06 AUDIENCE: [INAUDIBLE]

50:08 HAZHIR RAHMANDAD: Oh, you
have feedback from confidence.

50:11 AUDIENCE: But you're right,
not from the interest rate.

50:13 HAZHIR RAHMANDAD: Yes, but
not from the interest rate.

50:15 AUDIENCE: Reality should
be some of measure

50:17 of the fund's interest rate
and the investment interest

50:20 rates [INAUDIBLE]
comparison [INAUDIBLE].

50:24 HAZHIR RAHMANDAD: Yeah.

50:25 AUDIENCE: You can't
go [INAUDIBLE].

50:26 AUDIENCE: So just
to clarify, when

50:27 you're saying the
promised interest rate,

50:29 people are comparing it
to the reference rate,

50:32 so if it's higher
than reference.

50:35 HAZHIR RAHMANDAD: Yes, exactly.

50:37 AUDIENCE: --like
market administrators.

50:39 HAZHIR RAHMANDAD:
Yeah, so the way

50:41 I would probably formulate it, I
would think of the confidence--

50:46 I would even name it as this
is the risk of losing my money.

50:52 So if that risk is 0, then I
believe the promised interest

50:59 rate.

51:00 And if that risk
is 1, they might

51:03 then my expected return
rate is minus 100%

51:08 or kind of equivalent to that.

51:11 And then I will formulate
that risk of losing my money.

51:17 I try to formulate
it very robustly

51:20 and then calculate the expected
return rate using that, perhaps

51:27 with some additional sensitivity
that, OK, people are risk averse

51:33 so that they don't just
look at the expected return,

51:35 but there is kind of a
risk-adjusted expected return.

51:38 So you can add volatility
cost to it as well.

51:45 Then that becomes kind
of the key driver.

51:48 And that's what I meant by when
you're talking about confidence

51:51 in this model or
trust or reputation,

51:54 building a very operational
version of it really helps.

52:00 So in this case, that
operational version

52:03 would be something like,
what is the probability

52:07 that I'll lose my money?

52:09 It will be between 0 and 1.

52:10 You can then use it in
calculation of expected return

52:14 into risk-adjusted
expected return.

52:16 And then those risk-adjusted
expected returns

52:18 can make up for attractiveness
of this scheme compared

52:24 to the alternative schemes.

52:26 And then the Bass
diffusion model-- remember,

52:29 what's the idea of
Bass diffusion model?

52:31 It is about diffusion
of information.

52:34 So it is about people knowing
about this risk-adjusted return

52:40 rate.

52:40 If the risk-adjusted return rate
is below the market return rate,

52:47 then nobody will adopt it.

52:50 People will become aware of it.

52:53 So the Bass diffusion model,
what it does makes people aware,

52:59 but then their decision
whether to invest

53:01 or not could actually
come from the true--

53:04 or the market perceived
risk-adjusted return.

53:11 AUDIENCE: So how
would you do this?

53:13 How would you do this
risk-adjusted expected return?

53:16 So you have the expected
return and that makes sense.

53:18 You just multiply
the probability.

53:20 You just take it to some power--

53:24 HAZHIR RAHMANDAD:
Yeah, so I guess,

53:25 in the kind of
finance literature,

53:27 they just have a
volatility factor

53:28 that says it is your risk--

53:33 so there is a linear--

53:36 so minus some alpha multiplied
by a standard deviation

53:39 of the return that you
expect becomes your kind

53:43 of risk-adjusted return.

53:45 So it is the mean
minus some beta

53:50 by standard deviation of the
return rate for that asset

53:57 class.

53:59 So you can use
something similar.

54:01 But here, you are
not calculating

54:02 the standard deviation.

54:05 So you're calculating the risk
that your money will be lost.

54:08 You need to then go
from there to something

54:11 like a standard deviation of the
volatility or kind of a measure

54:16 of volatility in return.

54:19 I haven't gone through
making those calculations.

54:21 You could--

54:22 AUDIENCE: Is volatility really
what matters here, or is it

54:25 rather that there's a
nonlinear response to losses

54:28 that losing $1 is much worse
than gaining [INAUDIBLE].

54:32 HAZHIR RAHMANDAD: So there are
really two different things.

54:35 So the underlying reason why
people are sensitive to risk

54:41 is the same psychological
story that losing $1

54:45 is worse than gaining $1 or more
utility loss than gaining $1.

54:50 That's why people are
sensitive to volatility.

54:52 So the underlying
mechanism is the same.

54:56 But how you translate
this probability of loss

54:59 to an equivalent
volatility is not obvious

55:03 because it's a question
about the distribution

55:11 of the interests or the kind of
return that you would expect.

55:16 I would not go through
building a whole machinery

55:20 for that distribution because
there are a bunch of assumptions

55:24 that go into it, but
ultimately, it is just

55:25 something like a parameter.

55:27 So I would just have
a parameter that

55:29 translates this probability
into its impact on my expected

55:38 return.

55:40 So you could think about
promised versus kind

55:45 of full loss, which is minus
100% or per sum, that 45 days,

55:52 as the range.

55:53 And then you are
scaling between the two.

55:56 So that probability is a
number between 0 and 1.

55:59 So raise it to a
power and do this--

56:03 switch between the two.

56:04 That should do OK.

56:05 I think that would be
a decent first cut.

56:09 AUDIENCE: Question-- it
wasn't an easy decision for me

56:12 to can go with confidence or
trust or any measure of that

56:16 [INAUDIBLE].

56:18 Do we need to start with
that or [INAUDIBLE]?

56:20 HAZHIR RAHMANDAD: So it's
a very good question.

56:23 And here, you have
stocks in the sense

56:25 that you are using the liability
and cash, which are both stocks.

56:29 So the inertia in the
payments is showing up

56:32 in these two stocks.

56:33 So that was why
I didn't actually

56:35 bring up this as a problem
that you don't have inertia.

56:39 If you were getting
it, for example,

56:41 from this flow rate of actual
payment versus desired payment,

56:46 I would have signaled that as
another issue to think about.

56:51 But more generally, there is
a question of spread of news

56:56 about whatever the
signal is and that is not

57:00 captured in this model.

57:01 You are assuming cash is known
today, and not only that,

57:07 people are responding
to it right away.

57:10 Not a great assumption.

57:12 So an explicit delay
process for perception,

57:16 spread of the information
becomes relevant as well.

57:21 Yeah?

57:22 AUDIENCE: So I know I'm
talking about this [INAUDIBLE],

57:24 but even if expected
return is low--

57:31 I'm just thinking about this--
so long as that recruitment

57:34 factor or whatever this
infectivity is positive,

57:36 then everyone will
eventually join, just

57:39 over a longer period
of time, right?

57:41 HAZHIR RAHMANDAD: Yes.

57:42 AUDIENCE: So long
as it's positive.

57:44 And so that seems a little odd.

57:47 HAZHIR RAHMANDAD:
So why is it odd?

57:49 So if this is the
best investment

57:51 available in a
marketplace, why is it odd

57:54 that everybody would try it?

57:56 AUDIENCE: Well, I guess--

57:58 

58:01 sorry.

58:01 AUDIENCE: [INAUDIBLE]

58:03 AUDIENCE: I guess I was thinking
that in the case that it's not--

58:07 I was thinking about of it
being some ratio to the--

58:14 yeah, I guess I
was thinking of it

58:15 as being as it being some ratio
to some reference to a term

58:19 and that if the
ratio is small, so it

58:21 is worse than the reference--

58:22 HAZHIR RAHMANDAD: Oh,
as soon as it is worse,

58:24 it shouldn't then
create-- and that

58:26 was the point about this effect
on your recruitment factor.

58:31 Again, with the caveat
that the Bass diffusion is

58:34 kind of conflating two
different things-- the diffusion

58:36 of information about
this thing that exists

58:40 and the decision to
actually become an investor.

58:43 These two are separate
from each other.

58:45 In the current version, they are
combined into a single action

58:50 that is recruiting of investors
whereas, in the real world,

58:54 it is when a lot of people
are investing with Ponzi,

58:58 a lot of people will learn about
this investment opportunity,

59:01 and then they have a
separate gate for deciding

59:04 whether to invest in it or not.

59:05 And that separate
gate is informed

59:08 by-- so I would probably,
if I wanted to capture this

59:11 separately, I would
have, rather than

59:13 this going to the
recruited funds,

59:15 it goes to considering Ponzi
for investment or something

59:22 like that.

59:22 AUDIENCE: [INAUDIBLE] exposed.

59:23 HAZHIR RAHMANDAD: Exposed, yeah.

59:24 So that's kind of similar to
the exposed state in the SCIR.

59:29 AUDIENCE: [INAUDIBLE]

59:30 HAZHIR RAHMANDAD: Sure.

59:31 AUDIENCE: --trust
and confidence.

59:32 So if you believe
[INAUDIBLE] when

59:38 I wanted to show
this [INAUDIBLE]

59:42 and then suddenly, [INAUDIBLE].

59:46 HAZHIR RAHMANDAD: Good.

59:47 So if you have a
stock, the signal

59:50 that is going into
it, whether this

59:52 is the current version
of the confidence

59:54 that this model has or
some alternative would have

59:57 a sudden shift, but
then, yes, the input

60:03 into that delay function would
have a sudden shift because--

60:08 and you would like it to have.

60:10 The sudden shift
comes from the fact

60:12 that you don't have money to
pay people or some other way.

60:16 So for example, you may have
people investigating you.

60:21 Journalists were
writing about Ponzi

60:23 and investigating what
is this guy doing.

60:26 And that was actually
the trigger mostly.

60:29 So a couple of articles that
came in Boston Globe and other--

60:34 I'm not sure if it
was Boston Globe,

60:36 but in a couple of
news outlets were

60:40 the triggers to runs on Ponzi.

60:42 One of them, he managed
to control the other one.

60:46 He ultimately couldn't
with some delay.

60:49 So in that sense, there
is the information

60:55 coming in that is changing
the trustworthiness

61:00 of this investment very
quickly, either because he's not

61:03 paying people or because
somebody is investigating them.

61:06 Then there is the spread of that
information in the population.

61:09 And a simple delay has
a kind of a delay in it,

61:16 so people wouldn't know
about it overnight.

61:19 But in these cases, the
real world of perception

61:23 is very asymmetric.

61:24 The adjustment time
for that delay,

61:27 if the confidence is
increasing, people hear about it

61:31 but more slowly because
it's like, yeah, I actually

61:34 haven't invested in Ponzi,
and I got my money back.

61:37 That's an interesting kind of--

61:39 I'm not sure if I
will go and talk

61:41 about it with a lot of
people because now that's

61:43 a good investment for me.

61:44 I don't want others to saturate
that investment opportunity.

61:48 I'm more likely to
just keep it to myself.

61:51 But as soon as
somebody is not paid,

61:53 everybody starts
shouting, oh, my cousin

61:56 has invested with Ponzi.

61:58 Let me call them and tell
them or just go and bring them

62:00 to the line because, otherwise,
they wouldn't make their money.

62:03 This thing is collapsing.

62:04 So that asymmetry you can
capture in the delay function

62:10 for perception.

62:11 So you would have a delay
time that is very small when

62:16 things are going down.

62:18 But when things are going up,
it would be a longer delay time.

62:23 So that would be a little
bit more advanced formulation

62:26 but pretty standard.

62:27 So is what I'm saying
clear because--

62:33 yeah?

62:34 AUDIENCE: [INAUDIBLE]

62:35 HAZHIR RAHMANDAD: Sure.

62:36 So the switch would be
basically the flow for the delay

62:43 is desired minus current level
of a stock divided by a time

62:47 constant.

62:48 So now, rather than dividing
it by just the time constant,

62:51 you divide it by if then else.

62:54 AUDIENCE: [INAUDIBLE]

62:55 HAZHIR RAHMANDAD: Yes, desired
is bigger than the stock T1.

62:58 Otherwise, T2.

62:59 That's all.

63:01 So that was a good point.

63:04 And I think that asymmetric
delay may work well.

63:07 So we kind of beat
this model enough.

63:11 Let's go to some
random other one.

63:14 So I don't know--

63:15 whose is this one.

63:16 So Alban's, so let's take
a look at Alban's model.

63:21 So here, we have
potential investors

63:28 who invest who are waiting
to be paid who are not

63:33 interested in this scheme.

63:36 The rate of becoming--

63:39 so with a payback time of,
in this case, three months.

63:44 Was it three months or 45 days?

63:45 I don't remember.

63:46 Was it three months?

63:47 AUDIENCE: 45 days.

63:48 AUDIENCE: It was 45 days.

63:49 AUDIENCE: [INAUDIBLE]

63:52 HAZHIR RAHMANDAD:
Yes, 45 days, 50%.

63:58 So this is good because
you get the investors going

64:02 to this stock, and then they
decide it's operationally

64:05 a little bit cleaner to
follow and kind of also

64:08 avoids the problem with that.

64:09 But of course, it adds one
level of one additional stock.

64:16 The Bass diffusion model idea
is, again, pretty standard

64:20 here, except that the adoption
fraction also has some effective

64:24 expected return rate,
and expected return rate

64:29 is coming from claimed
interest rate of the scheme

64:33 and confidence in the scheme.

64:35 So this is very close to what
we talked about right now.

64:39 And we could take a look
at how it is formulated.

64:42 It is claimed interest
rate multiplied

64:44 by confidence in the scheme.

64:46 

64:48 It's largely unit-consistent.

64:51 That's good.

64:52 And then the confidence
scheme is coming

64:54 from that fulfillment ratio.

64:56 So you may remember,
we talked about one way

64:59 to capture it is
looking at how much he's

65:03 paying people versus what people
were expecting to be paid.

65:06 And as soon as that
ratio starts to fail,

65:10 then you have a
very strong signal.

65:12 So that fulfillment ratio
is a number between 0 and 1

65:20 that he raises to a power for
this sensitivity of confidence.

65:26 And what should this
sensitivity of confidence

65:30 to fulfillment ratio be?

65:31 Should it be below 1 or above 1?

65:34 So that fulfillment ratio
is a number between 0 and 1

65:40 that says what
fraction of what people

65:42 are asking for you are paying.

65:45 Would you put the
sensitivity of confidence

65:47 to fulfillment rate
below 1 or above 1?

65:50 That's the question.

65:52 So think about it for a second.

65:54 

65:57 And why?

65:58 

66:11 AUDIENCE: [INAUDIBLE]

66:12 HAZHIR RAHMANDAD: So
you would say below.

66:13 Why?

66:14 

66:17 AUDIENCE: Well, not
really because--

66:20 HAZHIR RAHMANDAD: So
if I'm paying only 50%

66:23 of what people are asking for,
if I go with a below 1 number,

66:30 then the indicated
confidence will be 0.9.

66:36 If you actually want
it to be close--

66:38 if I pay even 90% of
what people are owed,

66:42 that's usually signal enough
that this thing is going

66:44 to be bankrupt in 24 hours.

66:47 Everybody will be attacking
the doors of Ponzi.

66:51 So that means the confidence
or indicated confidence

66:54 should now go down
to 0.01 or something,

67:01 some very small number.

67:02 So that requires a much--

67:05 I mean, above 1 number.

67:10 So that's to think about this.

67:12 And then, to his credit, Alban
has the asymmetric adjustment

67:18 here as well.

67:19 So basically, he's accounting
for that difference,

67:22 which is very nice.

67:23 It's exactly the formulation we
just talked about [INAUDIBLE].

67:29 So that's good.

67:30 And then this
confidence, the parts

67:37 that are feeding into adoption,
it's an interesting part

67:44 because this needs to
go to 0, essentially,

67:48 as soon as confidence
starts to go down.

67:52 

68:03 So then Alban also
has the effect

68:09 of expected interest rate
on fraction returning, which

68:16 is good.

68:18 I like to use the
same effect here

68:21 because, conceptually,
it is coming

68:23 from the same underlying
cost-benefit analysis,

68:26 so creating a separate
channel for it

68:28 would not be adding much
value, and it introduces

68:31 more free parameters.

68:35 So this is fine.

68:36 

68:40 Let's see.

68:43 Yes?

68:44 AUDIENCE: So I know a
few of the submissions

68:46 have this idea of investors
who are active investors who

68:51 are waiting.

68:51 But it seems like the only
residence time in the w

68:55 here is the minimum
processing time.

69:00 Couldn't you just have
combined the two stocks?

69:04 

69:08 I guess I'm just asking
what the purpose of it is.

69:11 HAZHIR RAHMANDAD: So the
purpose of this stock?

69:14 AUDIENCE: Yeah.

69:16 HAZHIR RAHMANDAD: Yes,
you could combine it

69:18 because it is a
short period of time.

69:22 And that short period
of time is coming from--

69:26 AUDIENCE: [INAUDIBLE]

69:28 HAZHIR RAHMANDAD: Minimum
money processing time.

69:31 Well, part of it is
coming from that.

69:36 Yes, that's true.

69:37 That's the main driver.

69:38 So the time constant in
that stock is fairly short

69:44 and, therefore, there
shouldn't be many people

69:46 left in that stock.

69:48 

69:51 And then you go back
to the formulation

69:53 we saw with Ali's model,
which I think is fine.

69:56 I don't think there is any
problem with using that.

70:00 The only thing is
that this allows

70:02 you to track people a
little bit more concretely

70:06 in this intermediate state,
that they want to be paid,

70:11 but they are not accruing
additional liability.

70:16 So that's the core issue.

70:18 So that way, he can basically
say, OK, I will pay.

70:25 As soon as somebody
gives me money,

70:27 I'll add 50% to it or 100%
to it depending on what time.

70:32 So he's using one
third per month.

70:37 

70:40 Why is it per month?

70:41 So this is actually interesting.

70:44 I am not following
what is happening.

70:46 AUDIENCE: Alban, [INAUDIBLE].

70:48 HAZHIR RAHMANDAD:
Oh, Alban, go ahead.

70:49 

70:53 AUDIENCE: Oh, I was just
trying to say that [INAUDIBLE]

70:57 to start because
the word of mouth

71:00 is only coming from
an active investor,

71:02 once you are
waiting in the line,

71:04 you're probably
waiting for get paid.

71:07 And if the fulfillment
ratio is not 1,

71:10 then you are waiting in line
to get there, you probably

71:13 don't [INAUDIBLE].

71:15 HAZHIR RAHMANDAD: So
that's another reason

71:18 that might be a good reason.

71:20 But now there is an
interesting piece here.

71:22 If I understand it
correctly, Alban,

71:27 when you have debt
in the scheme,

71:31 that debt continues to
grow until you are paid

71:38 and you get out of--

71:41 you're cashed out, correct?

71:44 AUDIENCE: Yes.

71:44 HAZHIR RAHMANDAD: So at
least in Ponzi's story,

71:47 that's not how it works.

71:48 Basically, as soon as
the term has finished,

71:52 you are not accruing interest.

71:54 So the formulation
for that inflow--

71:58 so that was why I
was a bit confused

72:01 was it can be even simpler.

72:04 You don't need the debt
in the scheme multiplied

72:09 by claimed interest rate.

72:11 You just need a claimed
interest rate that

72:12 is a fraction of the cash in.

72:18 So it would be 1
plus that fraction.

72:21 So if it is 50% over
45 days, it would

72:26 be 1.5 multiplied by cashed in.

72:29 And then that becomes
how much he owes people

72:31 as soon as they are going in.

72:34 You don't accumulate
this forever.

72:38 That would do a better
job of accounting here

72:41 than the current version because
here, people who are investors

72:45 there waiting to be paid
continue to accrue liability

72:49 or Ponzi continues
to accrue liability.

72:54 So that's a minor--

72:58 AUDIENCE: Yeah, I misunderstood
the [? contract. ?]

73:00 HAZHIR RAHMANDAD:
No, that's fine.

73:01 That's otherwise pretty good.

73:04 Let's see.

73:05 Then there is the
max cash out that

73:09 should control the actual
cash out, which does.

73:15 And then this creates the
debt fulfillment ratio, which

73:22 impacts actual getting paid.

73:35 And then that impacts
people who leave.

73:39 And what fraction return depends
on effect of expected interest

73:44 rate.

73:45 Now I think this is all good.

73:48 There is a subtle thing
here, pretty subtle,

73:52 but it might be interesting
to think through it.

73:56 So let's assume that
fulfillment ratio overnight

74:03 falls from 1 to 0.

74:06 Basically, this is the
night that Ponzi goes bust.

74:09 So the confidence in the scheme
starts to go down very rapidly.

74:14 But it actually starts
at a high level.

74:18 So the fraction
returning to Ponzi

74:22 will actually be 1 at
the very beginning of it,

74:24 or a large number.

74:26 Most of them will return
to put their money back.

74:30 But at that very
point in time, these

74:33 are people who are
not being paid.

74:36 That is, the actual getting
paid is much smaller.

74:40 So for a period,
because of the delay

74:43 in confidence in
the scheme, you have

74:46 people who are not paid
but still are going

74:49 back and reinvesting in Ponzi.

74:53 And that's just not how the
things would actually work.

74:58 So I probably would
have this fraction

75:02 returning to A to be bounded
by the debt fulfillment ratio

75:07 as well.

75:07 That is, it shouldn't go above
that or something like that.

75:10 Is that clear?

75:12 Yeah, go ahead.

75:14 AUDIENCE: Well, so I know
we've kind of been talking

75:16 a lot about the confidence
idea, but in my head,

75:21 system confidence
is always going

75:23 to be either 1 or 0 basically
because that's basically

75:30 what the debt [INAUDIBLE]
rate is going to be.

75:32 Either people are getting paid
or one person didn't and now

75:36 it's all canceled, and
Ponzi probably won't even

75:39 talk to new investors
because he knows,

75:41 eventually, somebody's
going to come from him,

75:43 so he's going to
get out of there.

75:44 So it feels like the confidence
matters less on the system

75:49 confidence and more just on your
exposure to-- an individual's

75:53 exposure to the idea that
this can work and has worked.

75:57 HAZHIR RAHMANDAD: So
that's a good observation

75:59 on the downside.

76:00 That is, as soon as there is no
payment to even a single person,

76:05 things will unravel
very quickly.

76:07 But on the upside that is
people building confidence

76:11 into it, the reason
at the very beginning,

76:13 these schemes don't
go to the roof is

76:16 that most people are skeptical.

76:18 That is, their
initial assessment

76:20 is that it's probably a scheme.

76:22 We haven't seen the evidence.

76:24 Maybe it takes a
couple of years.

76:26 But we are not--

76:27 I'm not going to invest in it.

76:28 So that building of confidence,
it starts from a small number.

76:32 That is, their priors is
that 90% this is just a scam.

76:37 But after six months, I'm seeing
my friends getting paid back.

76:42 I would say, well,
maybe it is not 90%.

76:45 Now, it is 60% in my
assessment, and I haven't

76:48 seen any negative signal.

76:50 As soon as I see a negative
signal, hell breaks loose.

76:57 Yeah?

76:57 AUDIENCE: [INAUDIBLE] also have
average investment [INAUDIBLE]?

77:01 

77:04 HAZHIR RAHMANDAD: We
could, but then we

77:07 are kind of adding a
mechanism that is already

77:10 can be captured in the
number of investors.

77:15 So in a way, I think
what Ali and Hesam did,

77:20 which was how much
money can be invested,

77:23 takes care of that
to some extent,

77:24 although it has its own kind
of storytelling problems,

77:28 that money doesn't
talk with money,

77:29 it is people who
talk with each other.

77:32 But I'm OK with keeping
it simpler this way

77:36 rather than making the amount
of investment endogenous,

77:39 even though, in practice,
that was part of the story.

77:41 That is, people would go, yeah,
I just put a dollar here and see

77:44 what happens.

77:46 But next time, if
it worked, I would

77:47 put $10 or whatever was the
scale of the investment.

77:52 AUDIENCE: The idea [INAUDIBLE].

77:55 HAZHIR RAHMANDAD: Go ahead.

77:56 AUDIENCE: On the idea
of the [INAUDIBLE]

77:58 I still feel like that's not
necessarily a system confidence

78:02 thing.

78:02 I am becoming more
confident because I

78:04 have been exposed to more
and more of my friends

78:07 who have been successful.

78:10 So that isn't that going to
be, on the individual level,

78:13 dependent on percentage exposure
of my friends who have done it?

78:20 HAZHIR RAHMANDAD: So
partly yes, but partly

78:26 depends on information
diffusion mechanism

78:28 you hypothesize is operating
in that environment.

78:31 So is it only my friends?

78:33 Do I see news items about
Ponzi and this scheme

78:36 that might be actually working?

78:39 Do I hear from people talking
about it in the corner streets?

78:42 So the more you expand
that, the more generic

78:47 for the whole population,
you can talk about.

78:50 Now the Bass diffusion model
is essentially doing that.

78:53 That is, it is saying
people talk about it

78:55 with their friends, and if
they have experienced it,

78:58 they will talk about it more.

78:59 So you could basically think
of this Bass diffusion model

79:03 to be doing that for you with
the caveat that I mentioned,

79:07 that Bass diffusion model
takes people to the state of I

79:10 am now considering.

79:12 And then there is a
process of conversion

79:15 that may take some
time and depends

79:18 on whether that
expected rate of return

79:20 is high enough at that point in
time, based on their perception.

79:24 

79:27 So I think this is a
pretty good model, Alban.

79:31 I haven't checked
every equation.

79:34 So let's actually
do a simulation here

79:36 to just see what's the
baseline behavior in the model.

79:41 So we have investors.

79:46 

79:52 So more and more
people are investing.

79:54 But at some point, it stops.

79:55 And the reason it stops
is that the confidence

79:58 crashes because it has
a very short delay.

80:04 So you see that the confidence
goes up slowly as we discussed

80:08 and then crashes very quickly.

80:09 This asymmetry delay
does the job nicely here.

80:15 And then the cash in this
scheme, it is crashing.

80:22 It's an interesting
double dip here.

80:27 So what is happening that
is creating that double dip?

80:32 So part of it is cash out
being slowed down, I think.

80:41 And then part of it is
cash in being shut down.

80:44 So if we look at what is
driving it, so cashing

80:54 slows down for a little
bit and then crashes.

80:58 

81:02 Cash out starts to go down
because of the constraint

81:06 on how fast you pay.

81:09 

81:22 So max cash out--

81:23 13 million.

81:25 Yes, this is exactly
when the max cash out

81:28 starts to become the
binding constraint.

81:33 So for a few periods, max cash
out keeps the stock of cash

81:40 to go down even faster.

81:43 But then there is no inflow.

81:44 And then it goes to 0.

81:51 That all makes sense.

81:54 And then you have investors
that are waiting to be paid.

81:59 

82:03 So when he can't pay, basically,
people wait there to be paid.

82:09 And that actually creates an
interesting reinforcing loop

82:13 because then you have
desired to be getting paid

82:17 and, therefore, you have
bigger desired cash out.

82:22 I mean that strengthens
the rapid adjustment

82:26 at that point in
time because you can

82:28 settle your accounts basically.

82:31 I think the behavior
makes sense in this case.

82:34 One thing that would
have been nice to have

82:37 here is to have two things.

82:40 One is to have actual
return of the investment,

82:45 if Ponzi was actually
making money or investing

82:47 this in some meaningful
investment that

82:50 had a rate of return here.

82:52 And then comparison
of expected rate

82:56 of return of the scheme versus
some outside option for people

83:03 for their investments so
that they decide whether to--

83:06 so this adoption
fraction comes from that.

83:08 It is kind of built into this
max effect and sensitivity

83:12 factors.

83:13 But having an explicit
external investment option

83:16 would make it nicer.

83:18 But this is pretty good.

83:19 

83:23 So maybe we should take
a break, 10-minutes.

83:28 We can come back and
look at a few more models

83:31 and then go to the next
few weeks assignment.

83:36 So maybe for this part,
let's get volunteers.

83:41 Who wants us to
look at their model?

83:45 Cathy?

83:46 Sure.

83:47 

83:50 Let's see.

83:51 This is Cathy.

83:54 AUDIENCE: I think?

83:55 Yeah.

83:55 So I don't have
liabilities, and then I

83:57 think I heard you
say-- so I'm driving

84:00 the kind of indicated payout to
current payout from the flows.

84:04 HAZHIR RAHMANDAD:
So let's actually

84:05 look at that because
let's see whether it works

84:09 or what are the challenges.

84:10 So basically, you
have cash on hand.

84:13 And it is coming from investment
and average investment

84:17 amount and something else.

84:21 It's investment or
reinvesting also.

84:23 That's fine.

84:24 AUDIENCE: Oh, and I also found a
bug at 908 in my investors stock

84:32 formulation.

84:33 Could you click into the
equation for that really--

84:36 HAZHIR RAHMANDAD: So in the
investor stock formulation.

84:39 AUDIENCE: It should be minus
reinvesting plus reinvesting.

84:41 I think when it
autopopulated it--

84:45 it should be both
minus and plus.

84:48 HAZHIR RAHMANDAD:
Sorry, what do you mean?

84:50 AUDIENCE: Like minus
reinvest plus reinvest.

84:52 AUDIENCE: It goes out
and then it goes back in?

84:54 AUDIENCE: Yeah.

84:55 HAZHIR RAHMANDAD: Ah.

84:56 

84:59 So what it basically means is
that it doesn't have any impact.

85:02 AUDIENCE: Exactly.

85:03 So I wanted to ask about that.

85:04 I wanted this capturing
thing to happen just

85:09 for face validity reasons.

85:11 And then [INAUDIBLE]
overwrites it every time I

85:15 open the formula.

85:16 And so that indicates
that it's not that good.

85:20 And I think that
the better way to do

85:22 it is this two-flow
maturing investor thing.

85:27 HAZHIR RAHMANDAD: And
basically, that's what you--

85:30 it forces you to
do for good reasons

85:32 because, otherwise, it's
very confusing for people

85:34 looking at it.

85:34 And then it really doesn't
have any impact on that stock.

85:38 So basically, you would have
an outflow and an inflow.

85:41 And then the outflow
informs the inflow directly.

85:43 AUDIENCE: Exactly.

85:45 So these are discrete packets
of, like, you have your 45 days.

85:50 

85:52 I guess, the way I was
thinking about it is.

85:54 You just need not
investors and investors.

85:57 And they can just cycle
between each other.

86:00 The whole reinvesting
thing is not at all--

86:02 the actual individual, whether
they [INAUDIBLE] doesn't matter.

86:06 It has no influence.

86:07 HAZHIR RAHMANDAD: So
you would put them back

86:09 into the noninvestors
or potential investors,

86:12 and then they can
come back and decide.

86:15 That's right.

86:15 You could do that.

86:16 I don't think that is wrong.

86:19 The only thing is that
in different models,

86:22 people have implemented
it differently.

86:24 But the investment decision is
not just a decision to invest.

86:28 In most of these
models, it's also

86:31 being informed about this
investment opportunity.

86:34 So people are using Bass
diffusion model in most of these

86:37 to drive that investment flow.

86:40 So if you put them into
potential investors,

86:43 now there is a kind
of additional process

86:46 of being informed about
this opportunity that

86:49 doesn't apply to these
people who are reinvesting.

86:51 If we had it into those kind of
an intermediate stage of people

86:56 who know about this
opportunity but have

86:58 to decide right now whether
to invest in it or not,

87:02 then it would be a better fit.

87:04 So you go into there and then.

87:05 

87:08 So that's that.

87:10 So now, here, the
inflow is clear.

87:12 The outflow is the
more interesting thing.

87:15 So you have the minimum time to
pay that puts the upper bound--

87:19 so it's a minimum of cash on
hand divided minimum time to pay

87:23 and indicated payout.

87:27 I'm OK with this, but
perhaps a good idea

87:31 to separate that max
feasible payment or something

87:34 as a separate variable.

87:36 It's mathematically equivalent
but a little bit cleaner.

87:42 And then the indicated payout
is coming from how many people

87:48 are cashing out.

87:50 

87:53 And then the amount owed
at payout, which is just

87:58 a promised fraction expanded.

88:03 

88:13 So right now, the
payout is happening.

88:17 That is investors are leaving.

88:19 

88:24 But if there is no money,
they are not paid, correct?

88:29 AUDIENCE: Yes.

88:31 HAZHIR RAHMANDAD: So how do
you account, accounting-wise,

88:36 about how much money
is lost in this scam?

88:40 That is, when all
is said and done,

88:45 how do you calculate how much
money was owed and never paid?

88:50 AUDIENCE: So those are the
scamages, the scam damages,

88:53 so that's just the indicated
payouts minus the payouts.

88:58 HAZHIR RAHMANDAD: Got it.

89:00 So yes, then this works.

89:03 That is basically
what you have here,

89:06 this additional
stock of scamages

89:09 is doing what you could also
do with the liabilities.

89:14 But it is the gap between the
cash and the liability that is--

89:20 not the cash and liabilities.

89:22 What he had to
pay and he didn't.

89:26 AUDIENCE: I suppose I
just didn't have a--

89:30 because investors can't
observe liabilities,

89:34 I like what Jake said
about liabilities

89:38 being a pressure on
the scheme leader

89:42 to go recruit more people.

89:44 I didn't think about that.

89:45 But other than that, I
didn't have a good feedback

89:50 story about what are
liabilities doing outside of--

89:55 HAZHIR RAHMANDAD: Accounting.

89:56 AUDIENCE: --accounting.

89:57 HAZHIR RAHMANDAD: Yeah,
so I think that's fair.

89:59 And liabilities are really--
their first-order effect

90:03 in this model is
actually accounting.

90:05 So that's why once you
have it in this way,

90:09 it does that accounting job.

90:10 Now the reason this
is working partly

90:13 is that you are getting
everybody out at the 45 days.

90:17 They are not any more investors.

90:20 They are people who had invested
and had to be paid at that time.

90:25 And if they weren't
paid, bad luck.

90:29 They are not willing to
invest or some other category.

90:34 Now the reinvesting part is
tricky here because it is not--

90:38 

90:46 because you have the
cash out, and cash out

90:48 is coming from what?

90:49 This is from the payout
time and total investors.

90:54 AUDIENCE: So
investors are leaving.

90:56 And then some fraction
decide to reinvest.

90:58 HAZHIR RAHMANDAD: I see.

90:59 I see.

91:00 AUDIENCE: And those who
don't just cash out.

91:03 And I assume the baseline
fraction deciding to reinvest

91:08 is 0.9.

91:09 And then that decrements
by losing trust.

91:13 HAZHIR RAHMANDAD: Yeah, so
you have these people who

91:16 are reinvesting in
this way of thinking,

91:19 assuming that this reinvesting
basically doesn't do anything

91:22 to the stock that
is on the flow.

91:24 That flow has no effect.

91:26 AUDIENCE: I think the
assumption is that they

91:28 have to go see their money.

91:31 They can't just say, I guess--

91:35 there has to be some proof
that their return existed.

91:40 HAZHIR RAHMANDAD: Yes.

91:41 And the way they do
it in this case is--

91:50 so you are getting the
indicated payout from cash out.

91:54 So this is only people who
decide not to reinvest.

91:56 AUDIENCE: No, it's also coming
from reinvesting as well.

91:59 HAZHIR RAHMANDAD: Oh, OK.

91:59 It is coming from reinvesting.

92:01 Got it.

92:02 

92:07 And you need that because
you get to reinvesting

92:11 to also impact investments.

92:15 Yes.

92:17 So this is actually
the right way

92:19 of doing it in the case
of Ponzi because they

92:24 had to go and get the money
and then go back and invest it.

92:27 So I think that's fine.

92:29 In fact, all you
need to do is to have

92:31 this reinvesting without
having it impact the investors.

92:34 That's basically
what is happening.

92:39 I mean, you just don't
need this flow variable

92:43 to be a flow variable.

92:44 It just is an
auxiliary variable.

92:46 AUDIENCE: [INAUDIBLE]

92:48 HAZHIR RAHMANDAD:
And then your model

92:49 will be fine on that front.

92:51 

92:55 Population growth-- it's
an overkill for this model.

92:59 AUDIENCE: Oh, I was wondering--
so the last question was

93:02 how do you get it to be
sustainable over time.

93:06 And population growth--

93:07 HAZHIR RAHMANDAD: I see.

93:07 I see.

93:08 So you were thinking
that population growth

93:09 could be a driver of that.

93:11 So that's interesting.

93:14 The first-order answer
is, well, you also

93:17 need to have return
on your cash.

93:19 That is, you need to
grow the pot of money.

93:22 That's important.

93:23 So that is currently
missing but could be added.

93:29 AUDIENCE: I suppose
I was assuming it

93:31 was purely a scam, [INAUDIBLE].

93:34 HAZHIR RAHMANDAD: Yes,
then it is the slow growth.

93:39 That's the only way is that
within a finite time horizon,

93:43 you might be able to sustain it
if you are not too attractive.

93:47 So perhaps Madoff was
closer to this model

93:51 because he sustained
it for decades,

93:53 if I remember correctly,
more than 20 years.

93:57 And that was
basically, yeah, this

94:01 is not an unbelievable
rate of return.

94:03 He was just kind of a little
bit more stable than the market

94:06 and a little bit better than the
average investment opportunity

94:09 in the market.

94:10 AUDIENCE: And he never had
to-- or he didn't often

94:12 have to show
someone their money.

94:14 HAZHIR RAHMANDAD: Yeah,
so that's also part of it.

94:17 But nobody is showing all
the money in the account.

94:21 Whoever wanted to be paid
back, he would pay them back.

94:25 So in that sense, he
was paying things back.

94:28 But then he would reinvest.

94:30 So whether this--
so right now, you

94:33 have reinvesting going both
into the indicated payout

94:36 and investment.

94:38 You could say, for
Madoff, he didn't

94:41 use either of these channels.

94:43 That is, it didn't go
into the indicated payout,

94:45 but it also didn't
go into reinvestment.

94:47 And there will be a
bit of a difference

94:49 because your max cash out
becomes more quickly binding

94:55 if you have both of them
in the indicated payout.

94:58 But not a big deal.

95:02 AUDIENCE: [INAUDIBLE]
could have actually gone

95:04 on for a long time if there
wasn't an exogenous shock to

95:07 [INAUDIBLE].

95:08 HAZHIR RAHMANDAD:
Yeah, basically.

95:11 AUDIENCE: [INAUDIBLE]

95:13 HAZHIR RAHMANDAD: Yeah, exactly.

95:15 It could have continued.

95:16 AUDIENCE: He might have
started as early as the 1970s

95:19 [INAUDIBLE].

95:20 HAZHIR RAHMANDAD: Oh my god.

95:21 OK.

95:23 AUDIENCE: So you could wait a
few minutes longer [INAUDIBLE].

95:26 But what's the point
of the scamages?

95:28 Is that just because
it's just a [INAUDIBLE]?

95:31 HAZHIR RAHMANDAD:
Yeah, it is, but it

95:33 is important for
accounting because that's

95:35 one of the key
outcomes in this case.

95:39 And then let's look at
the trust equations.

95:42 So trust is coming fraction.

95:46 This indicated trust, and
indicated trust is coming,

95:51 effective fraction
of obligations met.

95:53 So this is kind of perceived
fraction of obligations met.

95:58 So you have this
perception delay here.

96:01 What's the idea of having
this intermediate perception

96:05 delay and then the trust,
again, adjusting with some time

96:10 constant?

96:11 AUDIENCE: It could do without.

96:13 I think the idea, though, is
just that people don't get paid,

96:19 and then it takes some time
for them to tell people.

96:23 HAZHIR RAHMANDAD:
Yeah, but that is also

96:25 inside the trust and
investment slow adjustment

96:29 that the reason that is
adjusting as a stock with--

96:33 and nicely, you have also
the asymmetric adjustment

96:36 is basically that, that
it takes time for people

96:40 to learn about it.

96:41 And so I wouldn't have a
separate delay process here.

96:46 It's kind of too much overlap.

96:49 Now you have an
S-shaped function.

96:53 AUDIENCE: Yeah, so actually the
function that's active right now

96:57 is an exponential
reactivity parameter--

97:04 the bottom.

97:04 HAZHIR RAHMANDAD:
This last part.

97:06 So this is similar to
what Alban had as well.

97:09 So then that--

97:10 AUDIENCE: I want it just
to fall very quickly.

97:12 HAZHIR RAHMANDAD: Yeah, so
that reactivity parameter

97:16 would be-- yeah, so
you have a large value

97:18 so that it goes quickly to 0 if
you're not meeting obligations.

97:24 Good.

97:25 So that's working fine.

97:27 I'm not looking at
the logistic one.

97:31 Yeah, this should
work fine, I think.

97:35 Well, we didn't look
at-- so this trust,

97:40 where does it impact things?

97:41 One is on adoption fraction.

97:44 So if trust goes down, you're
bringing the adoption fraction

97:48 down linearly with trust.

97:52 So we have one nonlinearity
for this reactivity parameter

97:57 that then reflects in trust.

98:01 Yeah, that's fine.

98:03 AUDIENCE: So I think if
I were to make an edit,

98:06 I would also have it affect time
to forget and just blow that

98:10 to infinity or
something-- or very high.

98:13 HAZHIR RAHMANDAD:
Time to forget.

98:15 Forget what?

98:15 AUDIENCE: So people become
not willing to invest,

98:18 but then eventually--

98:19 HAZHIR RAHMANDAD: Oh yes, so
you don't have this decide not

98:25 to invest is impacted by trust.

98:28 But becoming willing
to invest is not.

98:33 And therefore, they would
continue to become interested.

98:37 AUDIENCE: Yeah, so
I think that's--

98:40 AUDIENCE: Why do
we even need that?

98:42 HAZHIR RAHMANDAD:
Why do I need what?

98:44 AUDIENCE: Forgetting.

98:46 The people who get scammed
are susceptible to get

98:50 scammed again.

98:51 And I think it was another
thing that I added thinking

98:56 about how could this go on.

98:58 HAZHIR RAHMANDAD: So it is
not just time to forget.

99:00 So we need to be a little bit
careful about what exactly

99:04 is happening conceptually.

99:05 So potential
investors are people

99:07 who are willing
to invest in Ponzi

99:10 and then not willing to
invest are people who

99:14 are not interested in Ponzi.

99:16 And let's for a minute
forget about this deciding

99:21 not to invest part, so
just the inflow from not

99:24 willing to invest to
potential investors.

99:27 That flow is capturing the idea
that some people had no interest

99:32 in Ponzi at the very beginning.

99:35 And then, over time,
they become interested

99:40 and they're willing to
consider it in some sense.

99:43 

99:48 But they don't know
about it, correct?

99:50 Because they haven't
heard about it.

99:53 AUDIENCE: I assumed--

99:55 HAZHIR RAHMANDAD: But because
the potential investors--

99:57 AUDIENCE: --are coming
out of investors as well,

100:00 then they know
about what happened.

100:02 HAZHIR RAHMANDAD:
Yeah, so that's

100:04 why I'm saying this is
kind of conceptually

100:06 a little bit unclear
what is happening here.

100:09 So the not willing
to invest right

100:11 now includes people
who know about Ponzi

100:15 but are not willing
to invest, and people

100:17 who don't know about
Ponzi and are not

100:19 willing to invest just
because they are not

100:23 into financial
investment, for example.

100:27 So which of the two?

100:30 AUDIENCE: I think it's
everybody knows about Ponzi.

100:32 HAZHIR RAHMANDAD: So
that's your assumption,

100:34 that everybody
knows about Ponzi.

100:36 But then if everybody knows
about Ponzi, why do you

100:39 have Bass diffusion model?

100:40 AUDIENCE: No, so
that everybody--

100:42 

100:45 sorry, everybody would
be willing to invest

100:48 if they knew about it.

100:49 I think my initial people
not willing to invest is 0.

100:54 So everybody who's in that
not willing to invest stock

100:57 is either a potential
investor or somebody who would

101:00 or somebody who has.

101:01 HAZHIR RAHMANDAD: Oh, OK.

101:02 So these are people
knowing about Ponzi

101:06 but not willing to invest.

101:07 So at the beginning this is 0.

101:12 That makes it
internally consistent.

101:14 

101:17 So this is different
from assignment

101:19 for people not
interested in VCRs

101:24 because the price was too high.

101:27 It is different.

101:29 OK, good.

101:30 So in that case, then
just making this time

101:33 to forget dependent on trust
and investment would, I think,

101:38 take care of the people
forgetting about this.

101:47 Good.

101:47 So if we run this, now
if I run this right now,

101:50 because of this reinvesting
going into investors,

101:52 things may not work well.

101:54 AUDIENCE: I think it works if
you do plus reinvesting minus

101:56 [INAUDIBLE].

101:58 HAZHIR RAHMANDAD: Or
doing this this way.

102:00 

102:07 Ah, because we have
the other model open.

102:10 

102:14 So we get the collapse,
as we expected.

102:24 And the reason is that
the fraction of obligation

102:28 met collapses.

102:32 So that fraction is one.

102:36 And how come that
fraction goes to 50%?

102:42 Because in the very
long term, you just

102:45 can't pay 50% of
what he's getting.

102:50 I mean--

102:51 AUDIENCE: He can pay
back what he receives.

102:54 HAZHIR RAHMANDAD:
And then fraction

102:56 deciding to reinvest in
the long term is not zero.

103:02 It's kind of 6% reinvest,
even though they are not

103:07 making any money.

103:07 So kind of long-term things
are not that meaningful here

103:12 because, basically,
once you have crashed,

103:14 you have crashed in these.

103:16 But it is still informative
about how the underlying

103:20 formulations are working.

103:21 So in that sense, it is not
a bad idea to look at those.

103:24 

103:29 I think pretty much everything
is in the meaningful space

103:39 and is working decently.

103:41 Now you have a relatively
large total population

103:44 that basically people come into
the population, many of them

103:51 just leave into not
willing to invest.

103:53 Some of them go in at the
very long term, get burnt,

103:57 and then that way,
they come back.

103:59 So that's not also
unrealistic completely.

104:03 And then Ponzi doesn't have
much money all the time.

104:08 It's kind of hand to mouth.

104:11 OK, cool.

104:12 AUDIENCE: [INAUDIBLE]

104:13 HAZHIR RAHMANDAD:
Yes, Anne, go ahead.

104:15 

104:20 Somehow we are not hearing you,
even though you are not mute.

104:24 AUDIENCE: Maybe your microphone.

104:26 AUDIENCE: Let me know.

104:27 HAZHIR RAHMANDAD:
Now it is good.

104:28 Thank you.

104:29 AUDIENCE: So I used your
reason for reinvesting would be

104:35 [INAUDIBLE].

104:37 HAZHIR RAHMANDAD: Yes.

104:38 So the formulation that
Cathy has here says people--

104:47 so basically, people
who are reinvesting,

104:49 they get out of the
stock and instantaneously

104:53 come back into the stock.

104:55 So as such, the net effect
on the stock of investors

105:00 is 0 because you come out
and then you come back in.

105:04 So that's why it is
not an actual flow

105:06 in the mathematical sense,
even though, conceptually, it

105:08 is both an inflow and outflow.

105:10 

105:14 AUDIENCE: Oh, I have
another question.

105:15 HAZHIR RAHMANDAD: Sure.

105:16 No, no, that's good.

105:17 AUDIENCE: So I was thinking
about the relationship

105:21 between investors and cash.

105:24 I think, in a lot of the
models, when investors leave

105:30 or there's one when
investors leave,

105:32 which is they're no
longer contributing cash

105:35 to the Ponzi scheme.

105:37 But what about
investors who vary

105:41 the cash that they
reinvest at different times

105:45 depending on trust?

105:47 So maybe early on were
reinvesting all of the money

105:52 that you made plus principal
back into the scheme.

105:56 But over time, you slowly
reduced the amount of cash

105:59 that you reinvested.

106:00 How would we capture
something like that?

106:03 HAZHIR RAHMANDAD:
Yes, so basically,

106:05 in all of the formulations
we have seen so far,

106:08 although kind of
Ali and Hasem have

106:10 a little bit of a different
version that kind of combines

106:13 the two effects, but in
most of the formulations

106:15 we have an amount that
each person-- average

106:18 investment amount that's
kind of a fixed parameter.

106:21 Now you could have a couple
alternative versions of it.

106:26 One is that the
average investment

106:27 amount can change over time.

106:30 Now if we do that, and
that's something also,

106:32 Cathy, for you to
keep in mind, if you

106:35 do that, then your
formulation starts

106:37 to fail because then the amount
that is indicated payment

106:42 is not based on the current
average investment amount,

106:45 but based on the
delayed version of it.

106:47 Then you would need either
the liability or some hack

106:50 to account for how those average
investment amounts are changing.

106:54 And then back to
your question, Anne,

107:00 there is also the
reinvestment, what

107:02 fraction of the money
that you get back

107:04 do you want to reinvest.

107:06 Now that is less
important in the sense

107:10 that you already have a
fraction deciding to reinvest.

107:14 This is fraction of people.

107:16 But for each person,
you're assuming

107:18 it is 0 or 1, that is
either reinvest or reinvest.

107:22 Now, if you had this
intermediate range of I

107:25 am reinvesting only
50% of what I got,

107:28 it is OK to think of them as
half a person who reinvested

107:33 fully and half a person
who didn't reinvest at all,

107:36 and you get the same
result. So in that sense,

107:41 having a continuous fraction,
deciding to reinvest,

107:44 takes care of that
issue by and large.

107:47 That is, it gives you enough
flexibility on that front.

107:50 Where the difference
is more salient

107:53 is the average
investment amount that

107:55 may change over time as people
build confidence or lose

107:59 confidence.

107:59 And it's more in the
building confidence part.

108:02 That is, at the
beginning, people

108:04 don't have confidence
about these things,

108:06 so they are willing to test it
with the small amounts of money

108:09 to see, maybe it works.

108:10 Like Bitcoin-- I
mean, when it started,

108:14 people would just
put a few dollars

108:15 to see what this thing is.

108:17 It's a matter of curiosity.

108:18 But then if, six
months later, they

108:20 see that they made
a lot of money,

108:22 they are willing to
put more money and then

108:24 more money and more money, and
now becomes $1 trillion market,

108:29 even though it doesn't
have any meaningful return.

108:32 It's a different story.

108:35 

108:39 In that sense, if you
wanted to capture that,

108:41 I think there is definitely
a way to do that.

108:44 You can basically use the thrust
to drive the average investment

108:47 amount, and it cannot go beyond
whatever is people's typical

108:51 saving or ability to invest.

108:56 To be honest, in these
investment schemes-- now

108:59 Ponzi is a bit of an
old-school, physical

109:02 get cash, go to the bank,
get slips of paper back.

109:08 But these days,
you probably want

109:11 to break the market
into different sectors.

109:14 So small investors are
very different story

109:18 than large investors,
and there are these kind

109:21 of mega whales of investors.

109:23 And probably you separate the
model for those categories

109:28 because their sources
of information,

109:30 their depth of knowledge
about what you do or don't do

109:33 is different.

109:35 If somebody is going to spend
or invest $100 million with you,

109:40 they'll definitely spend
quite a bit of money

109:43 figuring out whether
you are a trustable.

109:44 

109:49 But that's beyond our
problem definition for sure.

109:53 Others?

109:54 Anybody else wants us
to look at their model?

109:57 

110:04 Everybody is shy?

110:05 AUDIENCE: A couple of questions.

110:07 HAZHIR RAHMANDAD: Sure.

110:07 AUDIENCE: I was missing
some big parts of the story,

110:10 so I didn't have any notion
of promises or liabilities.

110:15 Instead, I had return
rates, reported returns,

110:20 so the investment
manager returns money,

110:26 and then the reports
of those returns

110:29 feed back to give
you new investors.

110:33 I guess--

110:34 HAZHIR RAHMANDAD: OK, let's
look at what you're doing here.

110:37 So this is your model.

110:39 So you have new investors.

110:40 These are people who
basically have invested,

110:42 and their investment
has not matured.

110:44 After a while, they
become matured.

110:46 When you are matured,
you want to leave.

110:49 I mean, lifetime
is killing them.

110:52 It's a bit hard, but you stay--

110:56 AUDIENCE: For some time.

110:57 HAZHIR RAHMANDAD: For some time.

110:58 But what's the idea
of this some time?

111:00 Five years you're
staying in this stock.

111:01 So what's the point of being
in this stock for five years?

111:05 AUDIENCE: Basically,
at some point,

111:08 you decide you want to get out.

111:11 HAZHIR RAHMANDAD: No,
but get out of what?

111:13 This is a mature investor.

111:15 If I understood you correctly,
when we first mentioned it,

111:17 you said these are people whose
investment has already matured.

111:21 That means they are not
earning any interest.

111:23 So why would I-- oh, you are.

111:25 AUDIENCE: Yeah, so it takes a
minute before they can start.

111:29 I was [INAUDIBLE] on the story.

111:33 For the first year,
they're just waiting,

111:34 and then, at maturity,
they start accruing.

111:40 HAZHIR RAHMANDAD: Ah,
so the new investors

111:43 are the ones who haven't yet--

111:45 AUDIENCE: They're not
accruing any interest.

111:47 HAZHIR RAHMANDAD:
Accrued interest.

111:48 So how are you capturing that?

111:51 So funds are going into this.

111:53 This is money that
investors put.

111:56 Maturing-- OK, this
goes to the next step.

112:00 Then I'm accruing interest.

112:05 Where does that
get accounted for?

112:08 AUDIENCE: All
that's happening is

112:09 we're taking the total
pot of money, [INAUDIBLE]

112:12 new and old funds and
spreading it over everyone

112:16 in the old population.

112:18 So I'm in the old population.

112:22 I came in with some
initial investment.

112:25 And my returns are
equal to whatever

112:27 is currently in the total pot
divided by whatever I invested.

112:33 HAZHIR RAHMANDAD: Wait, that's
not how your return is actually

112:36 calculated.

112:40 AUDIENCE: [INAUDIBLE]

112:42 

112:43 HAZHIR RAHMANDAD: So
what you are being paid

112:46 is the average money that
is associated with you.

112:49 So you have an aging chain--

112:51 AUDIENCE: No, you're--

112:54 HAZHIR RAHMANDAD: I'm just
looking at the formulation

112:56 for fund depletion.

112:58 It is investor exit multiplied
by average old member balance.

113:03 And average old member balance--

113:05 AUDIENCE: It's not going
into the right spot.

113:06 HAZHIR RAHMANDAD: Yeah, so this
part, the actual money being

113:09 dispersed, is based on
how much you invested

113:13 and it accrues no interest.

113:15 Then you have this
other thingy here,

113:17 which is reported old
account balance, where

113:20 you are calculating
something different, which

113:23 is total fund divided
by mature investors.

113:29 And that number will be larger
than average old member balance.

113:33 And then you are calling
that reported balance.

113:36 But you're not taking
that out of the funds.

113:39 So that's two errors--

113:42 18 out of 20.

113:45 AUDIENCE: That's not bad.

113:46 No, it's worse than that.

113:48 The main question I have is
about the Bass diffusion part.

113:51 I know this is wrong.

113:54 So I did one more into the VCR
model, where becoming interested

114:00 is driven by the return
relative to the reference.

114:04 And then it's a normal
information diffusion.

114:08 But mostly everyone
else seems good.

114:11 The investment probability
depends on the return.

114:15 So my question is this--

114:17 HAZHIR RAHMANDAD:
So this is actually

114:19 an important difference.

114:22 So this is the Bass
diffusion model.

114:24 Once you are in the
potential investors,

114:28 you will be investing basically.

114:32 And that's kind of what
you are formulating.

114:36 So if, today, you have
learned that Ponzi is a scam

114:42 and is not trustable--

114:44 now you don't have that part
very clearly accounted for here.

114:48 But let's assume you had it--

114:50 still, these potential investors
will be adopting with the same--

114:54 

114:57 AUDIENCE: Unless
they flow back into--

115:01 HAZHIR RAHMANDAD:
How do they flow back

115:03 based on the indicated billing?

115:05 So that may work.

115:08 So max indicated willing to
invest minus actual willing

115:13 to invest versus minus
potential investor divided

115:18 by time to become interested.

115:20 I mean, you adopted this
from the homework assignment,

115:24 and this is kind of a
[INAUDIBLE] formulation

115:26 that we put in that assignment
to make it simple enough that we

115:32 can give it to students.

115:34 But it's not the perfect
one because, basically, it's

115:36 saying the time to become
interested is symmetrical.

115:40 That is, the time
to become interested

115:41 and time to lose interest.

115:43 Whereas in this case, if
you are moving backwards,

115:51 the chances are it
is a much faster move

115:53 backwards than the forward part.

115:56 But putting that aside--

115:58 AUDIENCE: Just the
choice of where to--

116:00 HAZHIR RAHMANDAD: Yes,
but putting that aside,

116:02 you still will have
people-- so today,

116:04 everybody knows this is a scam,
but you have 100,000 people

116:08 in potential investors.

116:10 You will continue to turn
them into new investors

116:14 even though none of them should.

116:16 So that is not--

116:18 so you do need the impact on
the actual investor transition.

116:24 

116:27 And the other parts, you already
know some of the challenges.

116:30 AUDIENCE: It's not
the right story.

116:31 HAZHIR RAHMANDAD: OK, cool.

116:32 

116:37 Any other one?

116:40 

116:42 This is Cathy.

116:45 

116:48 AUDIENCE: Mine is different
in that it just captures-- in

116:50 that it doesn't capture a lot
of what you're talking about,

116:53 but it does have the pull.

116:56 HAZHIR RAHMANDAD: Yeah,
let's take a look.

116:58 Let's take a look.

116:59 So this is Jake's.

117:01 So we have the different
categories of investors,

117:06 so scheme susceptible group.

117:10 This goes grows with
population growth rate.

117:13 They may decide to join--

117:19 AUDIENCE: That's just
going to be [INAUDIBLE].

117:21 HAZHIR RAHMANDAD: So you
have a collapsed function.

117:23 So as long as it
has not collapsed,

117:26 it is minimum of this kind of
maximum rate and then desired

117:32 people rate.

117:33 So a couple of items here
that comes to my mind

117:36 just quickly-- so first,
this expression here,

117:41 even though it is kind of
unit consistent and does

117:44 the job for you, it is using
time step inside formulations.

117:48 And using time step inside
formulations is not a good idea.

117:52 And the reason it is not a Good
idea is that it is conceptually

117:55 doesn't exist in the real world.

117:56 There is nothing
called time step.

117:58 It is fully a mathematical
artifact needed

118:04 for numerical integration.

118:09 So you don't want to use those
concepts inside things that have

118:14 a meaning inside the model.

118:16 In this case, the meaning is
that the scheme-susceptible

118:20 population cannot be
depleted instantaneously.

118:25 Or it can-- actually, with
this one in [INAUDIBLE] it can,

118:30 but you cannot exceed a maximum
rate of depleting these people.

118:37 So just have minimum time to
deplete the scheme susceptible

118:42 population as a parameter.

118:44 Don't use time step.

118:45 So that's standard.

118:47 And then the other one
is the collapse thingy.

118:51 I'm a little bit worried
what is happening

118:53 inside the formulation for it.

118:55 Until we go into
it, I don't know.

118:57 Just the term collapse
sounds a very switchy thing,

119:00 and I'm wondering whether you
wanted it to be a very kind

119:03 of 0-1 switch, or is it
something that you want to work

119:07 for you continuously?

119:08 If it is continuous--

119:10 AUDIENCE: It's 0.

119:11 HAZHIR RAHMANDAD: And
then these are people.

119:14 So ultimately, this is
actually more interesting.

119:17 Part is what is the
desired people rate.

119:19 And the desired
people rate is coming

119:22 from desired money and
average investor contribution.

119:28 So basically, you have
something about desired money,

119:36 which is a complex formulation.

119:38 So it's current investors
divided by promised return

119:41 time multiplied by average
investor contribution multiplied

119:45 by promised return factor.

119:48 So basically, you're saying if I
need to pay people $1,000 based

119:54 on their maturing rate, I
need $1,000 of new investment.

120:00 So that's my desired money.

120:02 Is that the idea?

120:04 AUDIENCE: Yeah.

120:04 So Ponzi is going to recognize,
I have to pay out twice,

120:09 so I'm going to
go get two people.

120:10 HAZHIR RAHMANDAD:
Yeah, so that's

120:13 an interesting story
that is basically

120:17 Ponzi's proactively trying to
go and recruit investors, which

120:21 perhaps happens.

120:22 Now, I don't know
the story of Ponzi,

120:25 how much that played a
role because probably

120:28 the word of mouth type of things
were much more important driver

120:32 of investment acquisition.

120:34 But in Madoff's
story, perhaps this

120:37 was important as
well, I don't know,

120:39 or some of the
other schemes that

120:41 are more slow burning,
the active engagement

120:45 and recruitment of
investors may be important.

120:55 AUDIENCE: My thought was
maybe that even if there

120:59 was a lot of demand
to invest, Ponzi

121:02 would recognize if everybody
invests at once, that's

121:04 going to be a problem for me.

121:07 HAZHIR RAHMANDAD: Yeah,
that's an interesting idea.

121:09 So basically, you're saying
Ponzi keeps the new investment

121:15 at an optimal
level of sorts that

121:17 is close to what he needs to
just pay back the maturing

121:24 investors.

121:25 So that way--

121:26 AUDIENCE: To prove
that he can do it

121:28 because he can go to anybody
and call 50 people that they

121:32 know and say this works.

121:34 HAZHIR RAHMANDAD:
That's interesting.

121:35 So I like that.

121:39 But the way I would
capture that idea,

121:41 if I wanted to incorporate
that idea in the model,

121:44 would be to have this
act as a gate for getting

121:48 new investors when they
have been convinced

121:52 of becoming a new investors.

121:54 So I would have
the Bass diffusion

121:56 model to transform people from
not interested to interested.

122:02 And then, from that interested
into actually getting

122:06 their money into the
scheme, it is gated by Ponzi

122:10 accepting their
money, essentially,

122:12 and Ponzi can, at that point,
put an upper bound on that.

122:16 He cannot control the lower
bound if there is nobody willing

122:20 to invest because now he
has lost his reputation--

122:23 he goes bust.

122:26 That's an interesting idea.

122:27 I think it does make sense
for the kind of designing

122:33 a good scam.

122:36 Good that is working, not good
for the human utility functions.

122:43 

122:46 Current investors--
and then they

122:51 have the promised
rate of return.

122:55 They try to cash out, but
sometimes, they don't succeed.

123:00 And you have the
time step going here

123:02 to limit the money out as well.

123:05 So that's a little
bit of kludgy as well.

123:07 So you want that.

123:09 And then the ratio of--

123:11 AUDIENCE: I think, originally,
they were all promised return

123:13 time rather than time stuff, but
at some point, I switched one

123:16 and then I got it.

123:18 HAZHIR RAHMANDAD: And
then if you are not

123:20 paying what people
are asking for, this

123:23 is what will happen here?

123:25 Anything happens in your model?

123:28 AUDIENCE: So the
second that you have--

123:32 the switch for
collapse variable is

123:34 going to be the one that
you want to look at,

123:38 which is above--

123:39 switch for collapse, yeah.

123:41 Collapse and switch collapse
are the exact same thing.

123:43 Earlier, I iteratively
built it [INAUDIBLE] there.

123:48 So the second bit--

123:50 HAZHIR RAHMANDAD: So
basically, you either

123:53 don't have the money
coverage that is 1

123:55 or you have some
unpaid population,

123:58 you kind of kill everything
in the operation.

124:01 You have the collapse,
which in this case

124:04 means nobody is accepting
investor equity.

124:06 I mean, Ponzi is trying,
but nobody is paying him.

124:11 

124:14 AUDIENCE: So the second you
don't pay one person, suddenly,

124:17 it's over.

124:19 HAZHIR RAHMANDAD: OK.

124:19 So I think this is kind of
working for you because it grows

124:28 exponentially as
long as Ponzi is

124:33 able to bring people in,
but then, at some point,

124:37 it collapses.

124:38 So it's an interesting
story here.

124:41 So let's look at what
is happening here.

124:43 So there is the
exponential growth phase.

124:46 Then there is a kind
of a slowdown phase.

124:48 So what is driving slowdown?

124:51 AUDIENCE: The
slowdown phase starts

124:53 when the game-susceptible
population just

124:58 is equal to the-- it
becomes equal to the growth

125:01 in population rather
than having some excess.

125:04 HAZHIR RAHMANDAD: Yes.

125:06 So for a while,
population growth

125:10 becomes the bounding factor.

125:15 AUDIENCE: And then you run out
of cash that you would saved up.

125:18 HAZHIR RAHMANDAD: I see,
so you had saved up.

125:20 But how did you save up?

125:24 Because you were recruiting just
enough to pay back these people.

125:29 How is it that you save money?

125:32 AUDIENCE: I think it's
because your reinvestors who

125:35 are convinced, oh, this--

125:37 basically everyone
who invests is

125:38 going to reinvest in
this case, so you always

125:40 have their cash in
the system apart

125:43 from the time that it
takes them to actually--

125:46 HAZHIR RAHMANDAD: Yeah, so
you have the reinvestment

125:49 process also here.

125:51 And that allows you
to accumulate money.

125:54 

125:56 So you're bringing
in new investors

125:58 even though you actually
don't necessarily

126:00 need all of those new investors
at the beginning of the time.

126:05 AUDIENCE: Correct.

126:06 HAZHIR RAHMANDAD: Got it.

126:08 It's interesting.

126:09 It has kind of these
challenges we talked about,

126:14 but it has an
interesting feature

126:16 that other models
didn't have, and that

126:18 is kind of the pool
from Ponzi side

126:21 for getting money or kind
of putting a gate on how

126:24 much money he is trying to get.

126:27 Cool.

126:29 So I think this was pretty good.

126:32 Across the models,
there were several

126:34 that had most of the
components in a good shape.

126:38 I think we could
go through more,

126:40 but I want to get to the other
parts of the conversation

126:45 because next week and the week
after, we don't have class.

126:54 It's Sloan innovation
period, and then it

126:57 is spring break at MIT.

126:59 So we would be meeting up
April 4, something like that.

127:07 So that's a bit of a time.

127:10 So for that longer time,
we have the next session--

127:21 for next session, we have
the market growth model.

127:24 Now this is basically
adopted from Jay Forrester's

127:30 famous market growth paper.

127:33 Don't look at that model
so that you build it

127:36 from scratch on your own.

127:38 And it is not replicating
exactly what the market growth

127:41 model does.

127:41 It has a couple other
additional pieces to it.

127:46 This is also like
Ponzi, a little bit kind

127:48 of broader boundary.

127:50 You might formulate
things a bit differently.

127:52 So it's about a
company that is selling

127:56 a durable product in a limited
market, but a large market.

128:01 It is in a monopolistic
setting, so you don't need

128:03 to worry about competition.

128:07 And you're kind of looking
at the market growth

128:10 from inception all
the way to maturity.

128:13 And this is a product
that is complex

128:16 and life-long kind
of durable products.

128:20 So they sell it through
direct sales force.

128:24 This is not a Bass diffusion
type of a word of mouth.

128:27 People hear about it and come
and order a million dollar item.

128:32 It's kind of a much more
structured go and sell it type.

128:38 And the firm's
heuristic is to allocate

128:42 a fraction of its revenue to
Salesforce for selling things.

128:46 And also, if they can't--

128:53 if they don't have
product, they can't sell.

128:56 Basically, their
delivery delay increases.

129:01 They make it to order.

129:03 That is, there is a backlog.

129:04 When they get orders, they
will make the products.

129:06 It's not that they have an
inventory of the product.

129:10 And if they can't
deliver on time,

129:13 they promise a delivery delay.

129:14 If they can't deliver
on time, customers

129:17 become less interested
to buy from them.

129:19 So the success rate
of their sales force

129:22 in selling the product
goes down if they are not

129:25 delivering on time.

129:28 Their manufacturing
operations have--

129:32 

129:35 it takes time to
build the facilities.

129:38 And the signal they look at to
decide to expand manufacturing

129:42 capacity is the delivery delay.

129:45 So they use that to expand
their manufacturing facilities,

129:54 and those facilities
stay around for a while.

129:58 But they also
depreciate, ultimately.

130:03 You want to build a model of
the dynamics in this setting,

130:07 kind of the historical case
that you are trying to explain

130:11 is this is a very good
market in the sense

130:14 that these guys have
a monopolistic setup,

130:17 they have the market, and they
have a good product in general,

130:23 but they have seen kind of
ups and downs in their growth.

130:26 They have been growing, but have
been seeing ups and downs in it.

130:29 So that's the reference
mode of sorts.

130:31 But you also want to
understand what is driving it

130:37 and what are the alternative
policies that may help

130:40 them avoid the ups and downs.

130:44 So that's the big
picture of the case.

130:49 Now, this is, again,
a model that I'm

130:54 explaining the components
of it-- in a way,

130:57 I'm telling you the
mechanisms to model.

131:00 You didn't need to go and
do the research to decide

131:02 what are the mechanisms.

131:04 So as such, it is a simplified
modeling task compared

131:07 to most real-world problems, but
it has more moving components

131:11 than some of the previous work.

131:14 So we could think about
what are the questions that

131:20 come to your mind, thinking
about this formulation right now

131:23 or this problem
definition right now.

131:27 What are some of
the things you say,

131:30 OK, I don't know how to think
about it or how to model it.

131:33 We could have maybe five or
seven minutes of conversation

131:37 around questions, and then
we can switch to your problem

131:43 definitions for your personal
problems, which some of you

131:47 have already shared.

131:48 

131:54 AUDIENCE: Maybe the depreciation
of factories [INAUDIBLE].

132:00 HAZHIR RAHMANDAD: Yeah.

132:02 So it's a very important
part of the model

132:06 to build the production
facilities as well.

132:09 And there is kind of two
or three pieces to it

132:12 to do it well.

132:13 One is it takes time
to build things.

132:15 So you have to separate work
in progress factories that

132:19 are kind of under
construction versus factories

132:21 that are constructed.

132:23 Then there is the
depreciation of factories

132:25 that are already constructed.

132:26 That depreciation, perhaps a
simple delay function works,

132:32 but a simple delay function
with higher order delays.

132:35 If you have a first order
delay, it's kind of weird

132:39 because production
facilities don't

132:42 start depreciating the
day they are built,

132:45 so accounting for that
would be important.

132:48 Then going back to your
question about I have a factory.

132:53 Does it mean it is producing
at its full capacity or not?

132:58 The answer is it doesn't need to
be producing at full capacity.

133:02 If you don't have
demand, it shouldn't

133:03 be because then you would
be in a different business

133:07 model with inventory.

133:09 And even there, you
wouldn't produce

133:13 when there is no customer.

133:16 So accounting for that
capacity utilization--

133:19 so there is a capacity
utilization feedback

133:21 that you need to keep in mind.

133:23 AUDIENCE: [INAUDIBLE]
if we're running

133:25 at full capacity [INAUDIBLE].

133:28 HAZHIR RAHMANDAD: That's
an interesting observation.

133:32 Don't worry about that.

133:33 

133:36 In practice, it is not
a very clear-cut case.

133:40 So for simpler equipment,
whether it is running or not

133:45 does make a difference
in the depreciation time,

133:47 but not running
something actually

133:49 can lead to
depreciation as well.

133:53 If you leave your
car in the garage,

133:55 it actually depreciates
as fast as if not faster.

133:59 A lot of the parts may rot
in place and rust in place.

134:03 So that's the argument.

134:06 AUDIENCE: Same
thing with planes.

134:08 HAZHIR RAHMANDAD: Good question.

134:09 Other thoughts, questions in
how you think about this model?

134:14 You have a little bit
more time, but you also

134:16 have your personal
projects to define.

134:20 AUDIENCE: [? Oscillation? ?]

134:22 HAZHIR RAHMANDAD: You
don't have to expect that,

134:25 but you would try to see
whether you can get oscillations

134:31 from it.

134:32 And what are the conditions
under which oscillations happen?

134:37 And on the bonus
side, this one kind

134:40 of in the original model and the
version that is your baseline,

134:44 the fraction of revenue
that goes to the sales force

134:49 is a fixed number.

134:51 | can endogenize that based
on marginal productivity

134:55 of the sales force
or how useful is

134:59 to have sales force
at any point in time.

135:00 So that adds a separate feedback
mechanism that is interesting

135:03 and may change some
of the dynamics.

135:06 I actually haven't built
that version myself,

135:08 so I'm curious to
see how you do it.

135:11 I mean, if you had time,
that's a good expansion.

135:13 AUDIENCE: Endogenize
[INAUDIBLE]?

135:15 HAZHIR RAHMANDAD:
Yeah, endogenous.

135:17 Endogenize is something
about your sales

135:20 force size or budget or--

135:23 sales force size is endogenous.

135:25 Sales force budget as a fraction
of total revenue is not.

135:30 

135:33 Good.

135:34 Go ahead.

135:36 AUDIENCE: So when you
manufacturing operation

135:38 with the backlog, that
means that they only

135:40 produce what customers order.

135:42 HAZHIR RAHMANDAD: Exactly.

135:43 So when customers order,
it goes into a backlog.

135:46 That drives desired delivery.

135:50 That desired delivery is
fulfilled based on production

135:54 but is bounded by your
production capacity.

135:57 And if you have
plenty of capacity,

136:01 you will produce
all that is desired,

136:05 and you will have excess
capacity that is not used.

136:08 If you are bounded
by capacity, you

136:11 are delivering as
much as you can,

136:15 but you are not fulfilling
the customer's demand.

136:18 So that's the balancing act.

136:23 AUDIENCE: [INAUDIBLE]
don't have any measure

136:25 of quality of the product?

136:27 HAZHIR RAHMANDAD:
Yeah, so right now,

136:29 we are assuming the quality
of product is either

136:31 exogenous or fixed or whatever.

136:33 It's not part of the--

136:35 AUDIENCE: [INAUDIBLE]

136:37 HAZHIR RAHMANDAD: Yes, for now,
assume price is also fixed.

136:39 AUDIENCE: --impacting the
customers is this [INAUDIBLE].

136:42 HAZHIR RAHMANDAD: Only
the delivery delay

136:44 that is changing the customer's
utility in this case.

136:48 AUDIENCE: [INAUDIBLE]

136:51 HAZHIR RAHMANDAD: Delivery
delay as a proxy for price?

136:54 AUDIENCE: Because
it decreases demand.

136:56 HAZHIR RAHMANDAD: Yeah,
so it is a feedback.

136:58 It is not price feedback
because price has

137:01 its own impact on your budget.

137:03 So price is
completely ignorable.

137:06 You need it in the machinery
of your machine, your model.

137:10 And you need a very
simple accounting sector

137:13 to think about, OK, costs
and benefits and net gains

137:18 and so on.

137:20 AUDIENCE: So delivery
delay signals the firm

137:23 to expand their
production capacity.

137:25 HAZHIR RAHMANDAD:
That's correct.

137:27 AUDIENCE: That means there's
always interested customers.

137:30 HAZHIR RAHMANDAD:
Yes, so this is--

137:32 now the size of the
market is limited.

137:35 So it's not an
infinite size market.

137:37 And it is a durable good.

137:39 So once you buy it, you
don't need it for a while.

137:43 So the maximum demand
is constrained.

137:47 But that maximum demand
is materializing.

137:53 What fraction of it
you can materialize

137:56 depends on your
sales force partly.

138:01 So your sales force is going
and getting these people.

138:07 AUDIENCE: But does
the demand change

138:08 because it's monopolistic,
so there's no competition?

138:11 HAZHIR RAHMANDAD:
So it does change

138:13 because of the durable
nature of the product.

138:18 So that's the constraint.

138:21 There is also, of course, your
sales force effectiveness.

138:24 So if your sales force-- you
don't have anybody to sell,

138:27 you wouldn't sell anything.

138:28 

138:31 AUDIENCE: So the
delivery date delay

138:33 doesn't at all impact the
customers [INAUDIBLE].

138:37 HAZHIR RAHMANDAD: They do.

138:38 It does.

138:39 It changes the effectiveness
of your sales force.

138:43 So that's how it affects it.

138:45 

138:50 The writeup has
these details in it.

138:53 So this is a shorter version
than what is in the writeup.

138:58 For the last 10-15 minutes,
I wanted to go back

139:01 to the personal
projects, and basically,

139:05 my plan is to read through what
you have submitted or will be

139:08 submitting in the next day or
two so that I can give you some

139:13 feedback and you can
adjust it, rework it,

139:17 get to the level that
you feel comfortable,

139:19 you know how to move forward.

139:21 Now, so far, as you have seen,
we have defined the problems.

139:26 If you remember in the memo
note that I had and also briefly

139:30 in the first session
we discussed,

139:32 there are different ways
to define a problem.

139:34 You may start from
a reference mode

139:36 that you are trying to
explain and understand.

139:39 You may start from
a set of mechanisms

139:42 that you are trying to model.

139:43 You may start from policy levers
that you want to then find.

139:47 What are the
mechanisms, what that

139:49 need to be captured to measure
the reference [INAUDIBLE].

139:53 In this class, so far, in
all of our assignments,

139:55 we have gone with
the second approach

139:57 of giving you the mechanisms
and asking you to build

140:00 models of those mechanisms.

140:02 In some ways, this is the
simpler way of doing things.

140:04 That is, basically, I have
already removed a lot of things

140:10 that you could consider.

140:12 I've kind of given you,
these are the mechanisms

140:14 you want to have.

140:15 Ignore everything
else so that we

140:17 can have more focused
conversation about formulations

140:21 and so on.

140:23 It may not be easy for you to
get to this type of a problem

140:29 definition because whatever
you're interested in,

140:32 you don't know what is it
that you need to focus on.

140:35 So as you think about
it, first of all,

140:40 do your best in defining what
is important or interesting

140:46 to model in terms of mechanisms
to capture the problem that

140:50 might be more motivated
by a reference mode

140:53 or by some policy questions
by some pain point.

140:58 And then I'll try to help
you with that process.

141:02 So whatever you
have written down

141:04 or are writing down for this
first draft, I'll look at it

141:08 and try to turn
it into something

141:11 that is a bit more
closer to mechanisms

141:15 so that you don't need
to go through the process

141:18 of clarifying a problem and
the feedback mechanisms that

141:23 will need to be in the
model versus those that

141:25 are not to be in the model.

141:28 But that is not an easy task.

141:30 I'm just highlighting
it because that's,

141:32 in some ways, the more
vaguely defined, harder part

141:36 of modeling, going from a
broad problem definition

141:40 into what are the
mechanisms that need

141:41 to go into a simulation model.

141:44 So I want to be helpful on that.

141:47 But maybe for the few minutes
that we have, if any of you

141:51 want to say, OK, I felt confused
because I was thinking about it

141:54 and I had no clue how to do it,
or this is the problem space,

141:58 but I don't know
what to focus on,

142:00 we can have a little
bit of a conversation

142:02 on a couple of cases, I think,
with this limited time we have.

142:05 That's what I wanted to
talk about before we close.

142:09 AUDIENCE: So just to clarify,
talking about going from problem

142:15 of interest to mechanism?

142:17 HAZHIR RAHMANDAD: Yes, exactly.

142:21 I mean, whatever you had--

142:24 I haven't read through the
ones that were submitted,

142:26 so I don't know
what is in there,

142:28 but if anybody wants to
bring it up as a case

142:31 because they felt
confused or didn't know,

142:34 I'm happy to have
that conversation.

142:36 Go for it.

142:37 AUDIENCE: What I was thinking
of doing was talking about

142:40 how does the fashion resale
industry affect brand

142:44 recognition for luxury brands.

142:46 So it kind of reminded me
of the car case for GM.

142:51 It was the used cars,
but the difference

142:54 is there's no leasing
program in luxury.

142:57 So my idea was you
have luxury brands that

143:00 want to gain, to some
extent, brand recognition

143:02 within their clientele,
but for luxury brands,

143:05 they don't want the wrong
clientele using it because it

143:08 ruins their brand image.

143:11 So there is a level of,
well, they want the--

143:15 you could argue, like
in Supreme's case,

143:17 the resale market really
helped build up like the clout

143:20 and how attractive it was.

143:22 But then you can also
see high luxury brands

143:26 like Hermes having
a lot of people

143:28 wear Birkins,
especially people who

143:30 aren't like their
ideal clientele

143:32 is tanking their luxury status.

143:38 And so then I was
trying to figure out

143:41 where does that line start
between resellers and not

143:46 resellers because there's a lot
of different types of resellers.

143:50 That's kind of my--

143:51 HAZHIR RAHMANDAD: So this is
a very interesting problem.

143:54 I think it's a good problem in
the sense that it is dynamic.

143:56 It kind of has
important trade-offs.

143:58 It has stocks and flows
that you can imagine.

144:01 So good space.

144:02 I don't know enough
about the topic,

144:04 but from just that 30-second
introduction that you gave,

144:09 it feels to me you may need to
have two categories of customers

144:16 based on their willingness to
pay something that might be

144:20 the one piece of the story.

144:24 You may care about
your product's life

144:29 in the sense of some
quality versus how long it

144:34 will last trade-off, and
something about price

144:39 that you assign.

144:40 So for a product, you
decide on the price,

144:42 and you decide on
that quality measure.

144:45 And you might bring
down the price

144:49 and bring down the quality.

144:51 You may get more of
the low willingness

144:56 to pay customer sector segment,
which is much bigger customer

144:59 segment.

145:00 And you may still have
a good margin on that,

145:03 but then that may erode
your attractiveness

145:06 for the high brand group.

145:11 So think about a model where
you have adopter, nonadopter

145:17 for two groups of
customers, and then

145:21 you have something about
their attractiveness for each

145:25 of these groups that comes
from your price, your quality,

145:31 and your exclusivity,
or how much

145:34 the other group is using it.

145:36 So for the low willingness
to pay customers,

145:39 having high willingness
to pay customers

145:41 becomes a factor
of attractiveness,

145:44 but the reverse is
actually negative.

145:47 So that becomes kind of
the heart of your model.

145:51 I would say that works well.

145:53 And don't go
anywhere beyond that.

145:55 That's already pretty--

145:57 AUDIENCE: I guess my question
for when you're optimizing where

146:03 should this brand position
themselves is it's not

146:08 profitability
because, obviously,

146:10 a Macy's is much more
profitable than a Gucci.

146:14 But they choose to
stay in that space

146:17 because they value
something about it,

146:20 whether it's the status
or the artistic value

146:22 that they perceive that they're
gaining from being there.

146:25 So I don't--

146:27 HAZHIR RAHMANDAD: That's
an interesting observation.

146:29 So don't worry about
optimizing in that sense,

146:35 but worry about whether they can
thrive in their desired market

146:41 segment.

146:42 That is, if they are
targeting the high customers,

146:45 can they thrive there
and still have a foothold

146:49 in the other market,
under what conditions?

146:52 So keep it to that level of
I'm interested in this question

146:55 rather than optimizing
for the whole market.

146:59 I think that's a good problem.

147:00 It would work out well.

147:02 Good.

147:04 Anybody else?

147:05 

147:10 AUDIENCE: I was thinking
about there's a contrast--

147:15 basically, book sales are up
but reading rates are down,

147:19 and my hypothesis for why that
is that the reason for buying

147:24 a book is less so for the human
capital of consuming it but more

147:30 so for the signaling and
cultural and social benefits

147:33 that you get from having
it and carrying it around

147:38 and having it on your shelf when
people come over, et cetera.

147:42 And yeah, so I think it's
more so like a simple paradox

147:50 explanation with some
reinforcing dynamics

147:53 around social value
of book makes it

147:57 so that reading the
book doesn't matter,

147:59 makes it harder and less
important to you to read books.

148:04 And so that's how we get these
sales increasing, reading--

148:07 HAZHIR RAHMANDAD: So
just for me to understand

148:10 the sales of
physical books are up

148:13 or sales of books, audio
and physical together are,

148:17 but not physical--

148:18 AUDIENCE: All
formats sales are up.

148:20 HAZHIR RAHMANDAD: So each
format alone is also growing.

148:23 Physical books also
have been growing.

148:25 AUDIENCE: Physical
books are growing.

148:27 Audio-- yeah.

148:28 HAZHIR RAHMANDAD: OK,
so that's number one.

148:30 Then you're saying reading
of it is actually declining.

148:33 Is it reading across all--

148:38 AUDIENCE: So the
survey question is,

148:40 in the last 12-- or
two survey questions.

148:42 In the last 12 months,
have you read a book

148:45 not for work or school?

148:47 And then second question
is, how many books

148:50 have you read in the last 12
months not for work or school?

148:53 And both of those,
it's like 50% of people

148:55 now haven't read a
book in the last year.

148:58 And the average number of books
has gone from 20-ish to 8.

149:04 HAZHIR RAHMANDAD: Interesting.

149:05 But when you say,
have you read a book,

149:08 people report their audiobook
consumption as reading a book?

149:12 Is that how the survey is--

149:15 AUDIENCE: I think the question
hasn't been consistent

149:18 over the 30 years, but I
think in the recent surveys

149:21 they say audiobooks
count, and they should

149:26 report audiobooks [INAUDIBLE].

149:27 HAZHIR RAHMANDAD: Got it.

149:28 Got it.

149:31 AUDIENCE: So I don't think
this is a book format story.

149:34 HAZHIR RAHMANDAD: Yes.

149:36 AUDIENCE: I think this is a
book like a BookTok, which

149:39 is like the TikTok book
phenomenon that really blew up

149:43 across the pandemic story.

149:45 

149:47 HAZHIR RAHMANDAD:
So the story you

149:49 are telling as this is a
story of social boasting

149:55 that I have some books or
I read books or whatever,

149:59 that is interesting.

150:05 It's probably not that complex.

150:09 There is a feedback
loop of people

150:13 see books as a status
symbol, and that

150:15 may get reified as more
people use it with that idea.

150:22 And that drives demand.

150:24 But then what is bringing
down the actual consumption

150:29 of books--

150:31 AUDIENCE: [INAUDIBLE]

150:33 HAZHIR RAHMANDAD: --is
a different story.

150:34 That is, basically, it becomes
a little bit exogenous-y.

150:38 What I mean by
exogenous is that there

150:40 is a mechanism that is
driving one reference mode,

150:43 and that is books are becoming
status symbols in some circles.

150:48 And then there is
another mechanism

150:49 that is bringing down books
consumption in your story.

150:53 And that might be people
are busy with other things,

150:58 or there is so much of
time going to social media

151:00 or they are not literate enough.

151:02 I don't know what, but you
come up with some hypothesis,

151:05 and then you can code it into
your model and get it to work.

151:11 But because they are kind
of detached from each other,

151:15 these two parts of the puzzle--

151:20 AUDIENCE: I guess I was
thinking of connecting them

151:23 because you're spending
time talking about it,

151:26 and you're spending time on
social media kind of hunting

151:29 what's the next thing I need
to get to signal my continuing

151:35 reader status.

151:37 And you're spending time--
one is spending time

151:40 doing that instead of actually
consuming the thing that they

151:44 bought.

151:45 AUDIENCE: I was wondering,
is the reading rates go down,

151:50 is that among everyone?

151:51 I guess my question would be,
among people who are actually

151:55 in BookTok, if you
only surveyed them,

151:58 their reading rates
might actually be up.

152:00 So that might not be related.

152:02 It might just be
like, in general,

152:04 people would rather watch
YouTube or scroll Instagram,

152:07 so reading rates are down.

152:08 But among BookTok people, yes,
it's a social status symbol,

152:12 but they also are probably
also reading books.

152:14 AUDIENCE: Yeah, no,
that's a fair point.

152:16 The reading rate
surveys are US adults,

152:18 and then they break it
just by the standard things

152:20 that you break down
by, but it's not

152:22 surveying people who are
in these communities.

152:25 So totally that could
be a breaker here.

152:29 HAZHIR RAHMANDAD:
So then, I mean,

152:31 it could be that Oriana's kind
of hypothesis is more of a

152:36 now you have these
concentrated groups that

152:38 consume a lot of
books, and then you

152:41 have the general population
that is not consuming much.

152:44 And it's kind of a question
of heterogeneity more

152:47 than a question of the two
mechanisms you're highlighting.

152:54 Now that is actually
an interesting--

152:56 that might be even more
interesting for a modeling

152:58 practice type of situation.

153:01 That is, how do you capture
this type of heterogeneity?

153:04 That is, it is happening,
perhaps across other product

153:09 categories, that as
people become more focused

153:14 in their narrow
niche areas, you may

153:18 get more consumption of
something among some groups

153:23 but less among others.

153:25 So trying to actually capture
that heterogeneity in a stock

153:31 and flow structure
with minimum complexity

153:35 is pretty interesting.

153:37 It becomes, again, kind
of exogenously driven.

153:41 It might not be
feedback-rich, but see

153:47 what you can tell about the
feedback mechanisms that

153:51 can be important.

153:52 And then capturing just the
stock and flow part of it

153:56 that generates the heterogeneity
is also interesting.

153:58 So that would be my suggestion.

154:03 I think we are
running out of time.

154:06 So with that, if you haven't
submitted your problem

154:11 statement, please do.

154:12 I will try to work on it
on the feedback next week

154:16 and get it back to you so you
have a little bit more time

154:19 to go back to it, edit
it, and these problem

154:23 definitions that I
mentioned over the email,

154:26 they are for you to be a
little bit more connected

154:29 with the problem but also have
create more of diverse models

154:36 that we can look at in the
last couple of sessions.

154:41 If you are OK with it, we
will share those for others

154:44 to also make it a concrete
problem that others

154:47 can tackle it as a modeling
challenge if they get a chance.

154:52 So those are the
purposes, but you

154:54 don't have to share it
broadly if you don't want to.

154:57 OK, cool.

154:59 Thank you.

155:00 

