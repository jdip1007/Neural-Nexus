---
title: YouTube Transcript: Session 7: Market Growth with Boom and Bust
created: 2026-10-20
updated: 2026-10-20
type: source
domain: ai
classification: general.media
tags: [youtube, transcript, sESpvrtk7Ck]
sources: []
published: 2026-10-20
time_sensitive: True
---
source_url: https://www.youtube.com/watch?v=sESpvrtk7Ck
source_type: video
ingested: 2026-10-20
duration_minutes: 145
language: en
sha256: 098fccb62fc7651267c3c196f6554705f689953e3299cdd882354bf56ca71a4d
---

# YouTube Transcript: Session 7: Market Growth with Boom and Bust

## Video Information
- **Title**: Session 7: Market Growth with Boom and Bust
- **Video ID**: sESpvrtk7Ck
- **Published**: Unknown
- **Views**: Unknown
- **Language**: en

## Transcript
00:00 [SQUEAKING]

00:02 [RUSTLING]

00:04 [CLICKING]

00:06 

00:09 HAZHIR RAHMANDAD: This week, we
are looking at the market growth

00:12 model.

00:14 So this is kind of inspired
by Forrester's market growth,

00:19 but has a few additional
components to it.

00:22 So I kind of have that
there is a total market size

00:25 and this is a durable product,
so there is a replacement

00:29 purchase and there is a first
time purchase type of a dynamic.

00:36 The part that is the product is
sold through the direct sales

00:39 force is pretty
similar to Forrester.

00:44 And you start with a fraction
of total revenue being allocated

00:47 to the sales force, and
then their productivity

00:52 depends on the delivery
delay, but also

00:55 on availability of customers.

00:57 And that's kind of the
additional component

00:59 to the classical market
growth model of Forrester.

01:04 There is a
manufacturing operation.

01:06 You have a backlog
for ordered products.

01:10 You are not holding
inventory, so it

01:11 doesn't have the complexities
of inventory management.

01:14 It has a little bit
of additional piece

01:16 for backlog management.

01:18 And then it's kind of
calculation of excess delivery

01:20 delay.

01:21 So those are the big picture of
what the scope of the problem

01:26 was.

01:26 Hopefully, you have worked on
it and you know the challenges.

01:32 It would be good to hear your
thoughts on the challenges

01:35 you have faced in
terms of things

01:38 that you noticed where-- and
let me just make this screen.

01:44 Oh, actually, you
can just type here.

01:46 

01:49 Let's see.

01:50 AUDIENCE: Not a
specific formulation,

01:52 but I just found this one very
difficult to do iteratively.

01:55 HAZHIR RAHMANDAD: Interesting.

01:56 AUDIENCE: Like it felt like
everything tied very closely

01:59 into each other.

02:00 So as I was trying to come up
with the formulation for one

02:02 thing, I found that I needed
to do a lot of structures

02:05 for the other.

02:06 And then when I had
problems, I found

02:08 it more difficult to
diagnose as a result.

02:10 HAZHIR RAHMANDAD: Interesting.

02:11 So can you tell us
what was your process?

02:16 Where did you start,
and where did you

02:18 find it more
challenging to isolate?

02:24 AUDIENCE: Yeah, so I started,
I think, with the order backlog

02:33 through to delivered
goods, just trying

02:35 to make the very
basic framework there.

02:42 But then I felt like I needed
to go a step up from that

02:45 of how many orders there were.

02:48 I felt like I needed some level
of the sales force immediately.

02:52 And because I needed the
sales force immediately,

02:54 I felt like I needed
revenue immediately,

02:57 because I felt like I
needed revenue immediately.

02:59 It all just played
in together at once.

03:01 HAZHIR RAHMANDAD: I see, I see.

03:02 So this is actually a very
good question and approach.

03:06 That is, you want as much
as possible to have chunks

03:08 of model that are fairly
clean, independent,

03:12 and then you add a chunk.

03:13 And so I like Jake's
approach, trying to do that.

03:16 And this model, in my view, is
not necessarily that much harder

03:20 to do it compared to
many other models.

03:24 Perhaps even some of
the chunks are easier.

03:26 And your approach was good.

03:28 So you have a kind
of a production

03:29 sector, the production.

03:31 There is a production
capacity, orders are coming in

03:33 and are going into
the backlog, and then

03:36 delivered out of the backlog.

03:37 So that part you can formulate
and have exogenous orders.

03:41 That's actually how
you would do it.

03:43 You can create exogenous
orders, have a step function,

03:46 go into it, see how things
go, have exponential growth

03:49 going into it, how it works,
and be done with that part.

03:53 Then there is a
mechanism for ordering,

03:56 and there the exogenous
drivers might be available

04:02 customers and delivery
delay that is perceived.

04:05 So if you make those
two as exogenous inputs

04:09 into the sales force
productivity effectiveness part,

04:15 that can also create its
own chunk of a structure.

04:20 And then what remains?

04:26 So the delivery delay is coming
from the production side.

04:30 And then yeah, that would be it.

04:33 Now, there is a market side if
you want to have it separately.

04:36 That is how many
customers are available.

04:39 So I think with
those three chunks,

04:41 you could isolate each of
them relatively smoothly.

04:44 So the customer side, there will
be a sales force coming into it

04:50 or even a sales
rate coming into it,

04:55 and that will take care of it.

04:57 That would be how
I would cut it.

04:58 But we can go through
some of the examples

05:02 or how different
students have done it

05:05 and see how that
has been tackled.

05:08 Good.

05:08 Other challenges?

05:10 

05:21 So we can-- let me
just close this thing

05:27 so it doesn't confuse us.

05:29 Let's look at the submissions.

05:32 

05:36 OK, so let's actually do
a little bit of a browsing

05:42 of models for sector.

05:46 So this is Ross's we have.

05:49 And let me just--

05:51 so we have the demand
side, potential demand.

05:54 

05:59 Hmm, that's interesting.

06:00 So, yeah.

06:05 That's interesting.

06:08 Yeah, so I like it.

06:11 This is actually an
interesting way of doing it.

06:13 I have to look at
the formulations.

06:15 But basically, Ross is kind
of formulating the customer

06:19 sector and the demand part
together in a single stock

06:23 and flow structure,
which should work fine.

06:28 Then we have the reputation,
we have the sales force,

06:32 and we have the
factory building part.

06:38 So these are the right
stocks in a high level view.

06:43 That's great.

06:43 Let's look at a few more.

06:45 

06:50 Album has production capacity
and production capacity work

06:55 in process, backlog, tracking
of profits, potential customers,

07:03 customers, and then
the return rates.

07:08 That depends on the
differentiation.

07:10 And then you can get the sales
from that return rate and sales

07:16 force.

07:16 So pretty much the same
key stock variables.

07:20 Great.

07:20 

07:26 Oriana.

07:27 We have sales force.

07:31 We have reputation
for delivery delay.

07:35 We have customers who are moving
between interested and current.

07:42 And there is we should see
what that part is done and then

07:47 potentially interested.

07:48 So there is a little bit of
additional diffusion dynamics,

07:53 maybe, here.

07:54 We should look at that.

07:57 So actually, can you tell
what is the distinction

08:01 between the three categories?

08:03 So customers are the ones that
currently have the product.

08:06 Interested customers are
the ones who want to buy it.

08:10 So that creates--

08:12 AUDIENCE: So my idea was that
there's whatever product there

08:15 is, they're going to be
like x could potentially

08:18 have use for it.

08:19 And then the sales
force lets those people

08:22 know that it exists.

08:23 Then out of those people
who now know that it exists,

08:26 depending on the
reputation of the company,

08:29 a certain portion
are going to buy.

08:30 HAZHIR RAHMANDAD: I see.

08:31 AUDIENCE: I never-- like,
there should be a return back,

08:34 like customers and interested
customers back potentially,

08:37 like--

08:37 HAZHIR RAHMANDAD: I see.

08:38 So in a sense here,
the sales force

08:41 is not needed for
repeat purchases,

08:44 for replacement purchases?

08:46 Is that a correct understanding?

08:47 AUDIENCE: Yeah, but if I just
added an additional flow pack,

08:52 it would--

08:52 HAZHIR RAHMANDAD:
Yeah, so either you

08:54 could take them here so
that now they have to be,

08:56 or the rate for purchase
here could be bottlenecked

09:02 by the availability
of sales force

09:04 rather than just being kind of
a fraction based on reputation.

09:08 So that would be
another way to do it.

09:10 But then you didn't even need
the potentially interested

09:12 customers.

09:13 You could have one.

09:15 Got it.

09:15 And then you have the
view for the backlog.

09:20 So you have the backlog,
factory, authorized number

09:25 of factories.

09:26 So this is capturing
the delay in the process

09:28 of generating factories.

09:31 And the units are OK.

09:32 That's great.

09:33 AUDIENCE: May I
just ask a question?

09:34 HAZHIR RAHMANDAD: Sure.

09:35 AUDIENCE: How did you
deal with the depreciation

09:39 rate of both vectors?

09:43 HAZHIR RAHMANDAD: So this is
a first order depreciation

09:45 in this case.

09:46 AUDIENCE: I meant in deciding
how many to construct.

09:49 HAZHIR RAHMANDAD: Oh,
construction of factories.

09:51 So this is coming from pressure
to expand factories, which

09:55 is coming from delivery delay.

09:57 And then there is--

10:02 so we haven't yet gone
through these equations.

10:04 So I just wanted to
get a quick overview

10:06 of the structures or the stocks
that different students are

10:09 using.

10:10 Then we can go
through the equations.

10:11 I think there might be issues
that could be improved here.

10:16 Let's see if this is--

10:18 searching.

10:19 So we have the customers
who are interested

10:24 and those who have purchased.

10:27 So this is pretty similar
to the first couple of--

10:31 and then sales force
impacts that purchase rate.

10:33 It's kind of a little
bit complicated there.

10:35 We need to look
at the equations.

10:37 Orders come here.

10:40 That creates a delivery
delay through shipment,

10:43 which depends on the stocks.

10:45 Perceived capital stock.

10:46 And then perceived
delivery delay

10:49 is impacting the
expansion of capacity.

10:53 So that also makes sense.

10:55 There is the issue of capacity,
capital stock adjustment time,

11:02 and how that is captured
or kind of work in process

11:05 for capital is not explicit
here, but otherwise looks good.

11:10 Ann's model, let's
Zoom in a little bit.

11:14 So we have customers
who are potential,

11:20 then become interested.

11:24 Then they're waiting
for their orders.

11:27 So Ann is accounting for
this intermediate stage

11:32 of waiting orders.

11:35 We'll have to look
at this equation

11:37 to see how it maps
into the backlog story.

11:43 This adds a little
bit more complexity,

11:45 but core concepts are similar.

11:48 Sales force is straightforward.

11:52 And then cash reserve
for sales force wages.

11:55 So she's accounting
for money in the bank,

12:00 rather than directly taking
the sales force from revenue.

12:03 So that adds one more stock
that others didn't have.

12:07 It's OK, but may
not be necessary.

12:10 And then we have the facilities
and death of the buildings,

12:17 or death to buildings.

12:18 That's very revolutionary.

12:20 

12:24 OK.

12:25 

12:30 And then we have here Hisam's
products that are owned,

12:37 orders that are in backlog,
potential customers.

12:40 So this is kind of
capturing backlog

12:42 similar to Ross in the
same stock and flow

12:46 structure as the customers.

12:48 And that should work fine.

12:50 We have the sales force
driving the sales.

12:55 It should also have
some impact on--

12:59 

13:04 yeah, so that kind of
takes people back here.

13:07 So there is kind of
a question there,

13:09 whether that's the best
way to handle it or not.

13:12 Then production capacity under
development and production

13:15 capacity.

13:16 Great.

13:17 And then did we check?

13:21 Yes.

13:21 

13:26 Gerard's model
has the reputation

13:30 for delivery delay, I
assume, adopters, and those

13:36 who become willing to rebuy.

13:38 So that's kind of
the purchasing part.

13:45 There is more complexity here
in terms of potential adopters

13:48 becoming interested.

13:49 And then you can convince
those interested into becoming

13:52 adopters.

13:54 That's fine.

13:55 It's an interesting
alternative because you're now

14:02 using sales force to
drive interest, and then

14:05 these people, maybe
with a delay, adopt.

14:07 

14:10 And that delay is regulating how
likely it is for them to adopt.

14:20 And alternatively, they
may decide not to adopt.

14:24 So this is a little bit of a
different conceptualization,

14:27 which might be pretty good.

14:29 I have to look at it a
little bit more closely.

14:31 And then we have the similar
production capacity dynamics

14:36 here.

14:37 

14:39 This one is Alexander.

14:43 So we-- yes.

14:45 

14:48 Backlog, installed base.

14:53 So you have a little
bit of a co-flow

14:55 of products versus customers.

14:58 And that's also nice to have.

15:00 You account for different units,
for people versus products.

15:08 Sales force, and then you have
in the other view the capital,

15:16 the production capital
as a single stock.

15:19 

15:22 And then we have Jason's,
so potential customers

15:35 versus customers
with the sales rate.

15:40 Order fulfillment has the
delivery delay and backlog.

15:46 And then delivery delay
gets perceived by customers

15:50 separately than by the company.

15:54 All of that makes sense?

15:57 Capacity acquisition.

15:59 

16:02 So we have the capacity and
capacity under development.

16:06 So that's also fairly
clean and standard.

16:11 And then sales force is
just the stock sales force,

16:15 which makes sense, with
some adjustment time.

16:18 OK, good.

16:19 

16:22 This is Cathy's.

16:24 Let me see if I missed somebody.

16:25 No.

16:26 Cathy's.

16:28 So accounting is the last group.

16:32 So we have customers who
are potential with purchase

16:39 orders with the product.

16:43 So customers with
purchase orders

16:44 are the ones waiting in the
backlog of stock, basically.

16:47 So they have the--

16:48 

16:51 yeah.

16:51 And then customers
with the product,

16:56 and then customers who
don't have the product,

16:59 and then they need to
decide to come back.

17:02 So this takes care
of backlog and--

17:06 

17:08 yeah, so all of that
is accounted for.

17:11 It's actually an
interesting piece.

17:13 So a quick look
at this structure.

17:17 What it tells me is that--

17:22 so this is a quick deeper dive
into to a heuristic you can use.

17:30 So I look at this stock
and flow structure.

17:33 If you put all of the stocks
together as a bigger stock,

17:36 what are the inflows?

17:38 

17:41 Do you see any inflow to that
full stock and flow structure?

17:45 Nothing.

17:45 What about an outflow?

17:48 There is an outflow.

17:50 So as soon as I see
that, it tells me

17:53 that ultimately, this market
will be drained to nothing.

17:58 And that is kind of a little
bit of an unrealistic setup.

18:05 So kind of zooming
out and thinking

18:08 of a mix of stocks and flows,
whether they are together,

18:14 conserving whatever you
are trying to do or not,

18:18 and they potentially lead
to an absorbing state that

18:21 is nobody or nothing, that's
kind of important to have

18:24 in the back of your mind.

18:25 Now, sometimes
that is realistic.

18:27 That is, for some
things there is actually

18:29 an absorbing state where
there is nobody left

18:31 or no money left, or whatnot.

18:33 But in this case, I think
that's not, probably,

18:36 the most realistic alternative.

18:40 And then you have rookie sales
force, experienced sales force.

18:44 So there is kind of additional
dimension of rookie dynamics,

18:49 which are pretty relevant,
even though it wasn't

18:51 part of the problem definition.

18:53 That's nice to have.

18:55 And then you have the backlog
and the manufacturing capacity.

19:00 Now, this is also a little
bit more complex here.

19:03 You have units in
production queue.

19:05 So this is kind of the back,
the normal backlog, the way

19:10 I would have thought about it.

19:12 But then you have
units in production.

19:14 So we should look at these
in a little bit more depth.

19:16 I don't know.

19:18 AUDIENCE: I was thinking that
the units in production queue,

19:22 that's just-- like, that's the
list of customers or orders I

19:26 need to fill.

19:27 And then I'm limited
by my capacity

19:29 on actually starting the
manufacturing process.

19:34 So I separated those.

19:35 HAZHIR RAHMANDAD: So your
manufacturing process kind

19:38 of limits the production starts.

19:43 And after a fixed time,
they end, basically.

19:49 Yeah, and your total backlog
would be the sum of these two.

19:51 So you would have the delivery
delay calculated correctly,

19:54 that average delivery delay.

19:57 Yeah, that's fine.

19:59 

20:01 It's sounds right.

20:03 It's probably
overkill, in the sense

20:06 that you don't need two stocks
to capture this process.

20:10 Basically, if you
had the outflow

20:12 to be regulated by
manufacturing capacity,

20:15 that would do the same
thing, ultimately, for you.

20:18 Very similar.

20:19 Not exactly the same thing.

20:20 So mathematically, there is
some difference between the two,

20:22 but I wouldn't worry too much
about that difference here.

20:26 OK, good.

20:27 

20:31 OK.

20:33 So Andreeva, we
have sales force,

20:42 customers with potential versus
current with some return rate.

20:49 And here, you are
not distinguishing

20:52 between first-time customers
versus those returning ones.

20:56 So that has some implications
in terms of formulations,

21:02 but that's fine as well.

21:05 Backlog is fairly standard.

21:10 Factories under
construction, constructed.

21:13 And you're calling
these factories

21:15 depreciating, [INAUDIBLE].

21:16 Is it a stock that
you want to track?

21:20 Do you do anything with it?

21:22 AUDIENCE: [INAUDIBLE]

21:23 HAZHIR RAHMANDAD: Yeah,
it's not being used?

21:24 Yeah, OK.

21:25 That's fine.

21:27 OK.

21:27 That all makes sense.

21:31 Did you see the sales force?

21:32 Yes.

21:33 OK.

21:34 And then Ali's model has
the backlog, delivery delay,

21:43 by the market, by the company.

21:45 So you are taking delivery
delay perceived by the market

21:48 from delivery delay
perceived by the company.

21:52 That's an interesting idea.

21:53 I don't know.

21:54 I think you could
calculate them separately,

21:57 I think as [? Katy ?]
I think had done.

22:00 But whether it is taken from
the perception of the company

22:05 is a little bit
of a harder sell.

22:07 Because the company has access
to a bunch of information

22:10 that it's not going to directly
share to inform the customers.

22:13 Customers are using their
own channels of information.

22:16 So as such, I wouldn't take--

22:21 yeah.

22:22 Capacity, capacity
under construction.

22:25 That's a standard.

22:27 And then we have the
customer structure here.

22:31 So this is current customers.

22:34 They become potential.

22:36 You pitch to customers.

22:39 And then they can become
current customers.

22:43 So you have the pitching
process kind of very explicit.

22:47 And that is what is coming
from the sales force.

22:51 So this is allowing you to
separate the step of acceptance

22:55 that is driven by delivery
delay from the step of trying

23:02 to influence pitching.

23:08 That's good.

23:09 That's one way to kind of
overcome that potentially

23:12 a little bit more
challenging formulation

23:14 and keeping it very operational.

23:19 Good.

23:19 Sales force, recent
revenue backlog--

23:25 and we saw the rest.

23:26 OK.

23:27 Great.

23:27 

23:37 Finally, we have Jake's.

23:41 So how come Jake's comes last?

23:45 Daniels is not the first
letter [INAUDIBLE] of it.

23:50 AUDIENCE: I think
you opened it first.

23:52 HAZHIR RAHMANDAD: Somehow, yeah.

23:53 But I thought I
had sorted things

23:56 based on alphabetical order.

23:59 OK.

23:59 So we have the backlog,
work in progress,

24:10 finished goods, delivered goods.

24:13 So you have this additional
detail on the delivery of goods

24:19 just based on some delays.

24:21 So the capacity is what
does the production,

24:27 but these delays introduce
some additional complexity

24:32 in terms of delivery delays.

24:40 That's interesting.

24:41 So actually, let's now do a
little bit of a deeper dive here

24:44 and understand what's
happening here.

24:46 So units are all fine.

24:51 So the story of--

24:54 people purchase.

24:55 This goes into
outstanding order backlog.

24:59 Production capacity
allow us to process this.

25:04 Now, you are combining
kind of probably two things

25:07 into production.

25:11 AUDIENCE: Yeah, my
thought was like,

25:17 you're going to be able to
start work in progress--

25:22 basically run at full
capacity if you need to

25:24 just based on the backlog,
but you can't go above that.

25:26 HAZHIR RAHMANDAD: OK.

25:27 So the equation here
has a little bit

25:29 of a unit problem for me.

25:30 So I think of available capacity
to be in widgets per year

25:35 or units per year.

25:37 But it seems you're using some
definition of capacity that

25:41 is in the units of units, not
in the units of units per year.

25:44 Can you tell what is--

25:47 AUDIENCE: Yeah.

25:48 In my head, capacity is like--

25:50 it's not necessarily
units per year,

25:51 but you can have x amount
of widgets currently

25:57 on the product line basically.

26:00 Like, at any given time, that
is a unit that can be somewhere.

26:05 HAZHIR RAHMANDAD: I see.

26:06 So you are saying you have
a number of factories, which

26:12 you just call it as a factory.

26:14 Then unit capacity
per factory-- you're

26:17 calling it unit per factory.

26:20 So you are kind of removing time
from the production capacity.

26:26 You are translating it into work
in process capacity in terms

26:31 of number of units that
are on the factory's floor.

26:37 AUDIENCE: Yeah.

26:39 HAZHIR RAHMANDAD: And then you
have a processing time of sort,

26:41 time to process orders, that
basically captures how fast you

26:47 drain that capacity.

26:49 So this could work.

26:52 I think technically
it is not wrong,

26:55 but it is not the standard way
we typically formulate these.

26:58 So the standard way is
to think of capacity

27:01 in units per unit of time--
so widget per year or month.

27:07 This is our production capacity.

27:08 That production capacity
then would directly

27:11 go into your production start
as one of the constraints

27:14 of that minimum function.

27:15 So it would be minimum of
the production capacity

27:18 and the outstanding order
backlog divided by time

27:27 to process order or minimum
time to process order.

27:29 Because then it
would be minimum time

27:31 to process order rather
than time to process order.

27:36 The definition of
this thing right

27:38 now is kind of doing two
very different things.

27:41 So time to process
orders, on the one hand,

27:44 in your current formulation,
is acting as minimum time

27:48 to process order to put an upper
bound on how fast you can drain

27:52 or you can produce given
how much backlog you have.

27:57 So even if you have
infinite capacity,

27:59 you cannot drain the outstanding
order backlog with an infinite

28:03 speed because you have a
constraint in terms of number

28:08 of items in the backlog.

28:11 Then there is a separate
time constant for how fast

28:15 your factory produces
the units it has

28:18 in its working process, which is
the way you were conceptualizing

28:23 it in our first part
of the conversation,

28:25 going back to the
available capacity.

28:30 So if you're saying
available capacity,

28:32 it is the total number of
units on the factory floor,

28:35 then it takes, for example,
10 days, or 10 months,

28:39 or whatever to process that.

28:42 You would divide that capacity
by that processing time

28:45 to get your average
rate of outflow

28:49 from the-- and
right now, those two

28:51 are conflated into
this single parameter.

28:54 So that is one of the
places where these two time

28:58 constants should not be
the same but are the same.

29:00 So that's--

29:00 

29:04 AUDIENCE: Or, yeah, I
think the actual time

29:08 to complete production
is going to be the time

29:10 to complete production
after work in progress.

29:12 It's literally
just the time to go

29:14 from order to get on the floor.

29:18 HAZHIR RAHMANDAD: Yeah.

29:19 AUDIENCE: But yeah.

29:20 HAZHIR RAHMANDAD:
So that would be--

29:22 

29:25 so that's a little
bit tricky because--

29:28 so now let's assume
your production capacity

29:33 is very small.

29:34 Well, because it is very small,
then you don't start production.

29:38 But once you start it, it
will go through this time

29:42 to complete production.

29:43 So basically, time
to process orders

29:46 plus time to complete production
is the total time for production

29:50 in your conceptualization.

29:51 So you have the
degrees of freedom

29:53 you need to basically
get this to work.

29:56 That makes sense.

29:59 So it's more kind of following
the standard formulation would

30:03 make it a little bit cleaner.

30:05 But also, you don't then need
all of these intermediate steps.

30:09 Basically, here, you are
adding two additional delays

30:11 into the delivery.

30:13 And so this is kind of another
important architectural choice.

30:19 What are the time
constants for my stocks?

30:21 The stocks for
finished good delivery,

30:24 work in process delivery--
if they are relatively fast,

30:27 then I don't need them.

30:28 If I think they are fairly
long-- so this is 0.2 months--

30:33 AUDIENCE: 0.2 years.

30:34 HAZHIR RAHMANDAD:
0.2 years, sorry.

30:35 This is 0.125 years.

30:38 So these are in the
order of a month or two.

30:43 If my other time constants
are kind of in that order,

30:49 then it makes sense to separate
them or be explicit about them.

30:53 If other time constants
are a little bit longer,

30:56 then it makes sense
to bring all of them

31:01 together into a
single structure.

31:05 So time to perceive
delivery delay--

31:08 you have 0.25 years as well.

31:09 So it's in the same ballpark.

31:11 So maybe this separation
is justified--

31:14 or reputation adjustment time
a year for the outsiders.

31:22 OK.

31:23 So I think this part
is working fine,

31:26 at least in the
basic physics of it.

31:28 Now you have shipping going
into received products.

31:34 AUDIENCE: Yeah.

31:35 You mentioned earlier it's
sort of split between people

31:38 and units-- it's not.

31:39 These are just in
terms of units.

31:40 Like, the interest of market
is just going to be units here.

31:43 It's like a potential
holder, not a-- yeah.

31:45 HAZHIR RAHMANDAD: Yeah.

31:45 So it would have been easy
to make that transition,

31:48 but you don't also need
to if you are assuming

31:51 each person is buying one unit.

31:52 That's fine.

31:53 And I think for this purpose,
we are not changing that.

31:56 So it's OK to have
the same units.

31:58 So when you deliver something--

32:00 so this is market
waiting for orders.

32:02 This is really what I think
should be deciding the delivery

32:06 delay.

32:08 So where does the
delivery delay come from?

32:10 So right now, you
have it from time

32:13 in backlog based on orders
outstanding in backlog divided

32:18 by the production
start plus time

32:21 to complete production
plus time to ship.

32:24 So you're adding these
three steps together.

32:28 AUDIENCE: Yes.

32:28 HAZHIR RAHMANDAD:
So that's probably

32:31 the same as what
you would do if you

32:33 had market waiting for orders
divided by received products.

32:38 So that probably would
give the same answer.

32:41 It's a good thing to test that.

32:43 Alexander?

32:43 AUDIENCE: [INAUDIBLE]
ask-- back to the WIP

32:46 and finished goods [? chain. ?]
Shouldn't the latter two flows

32:49 be constrained by
capacity in some way?

32:52 Because I'm thinking
that-- let's say capacity

32:54 is initially super high.

32:56 So then you have a lot
in the work in progress.

32:59 And then, suddenly,
capacity drops.

33:00 HAZHIR RAHMANDAD:
Yeah, absolutely.

33:02 So this formulation is
not fully consistent

33:06 with those scenarios--
that it is assuming

33:08 that once you are in
the production process,

33:11 the production capacity
wouldn't change anymore

33:14 for those batches.

33:16 So that is, basically, the
time constant for changing

33:19 the production capacity is
much longer than the time

33:22 constant for changing the
units in the production.

33:25 But it does create extreme
condition problems, as you say.

33:29 Exactly.

33:30 And that's one of the reasons
the standard formulation just

33:34 says, have one place
where production capacity

33:37 is operational, typically at the
very outflow of that backlog.

33:41 And then don't worry about
the intermediate steps.

33:44 Yeah.

33:45 So you're right.

33:46 I think you can come up with
extreme conditions like that

33:49 that will break
this formulation.

33:51 OK.

33:52 So that delivery delay
should work fine.

33:56 You get the delivery
delay perception here.

33:59 Then you have a delay reputation
that comes from that perception.

34:03 So there is a little
bit of a question,

34:06 what is this perception
doing in factory construction

34:14 sensitivity?

34:15 So this is similar
to what Ali had,

34:17 which is there is a
perception by company,

34:22 and then there is a
perception of delivery delay

34:24 by the customers.

34:26 But you are getting the
perception of delivery delay

34:28 by customers, which is this
delay reputation, from perceived

34:34 delivery delay by the company.

34:36 And these two, again, are a
little bit different pathways

34:39 information-wise.

34:40 So I would perhaps have
separate single delays,

34:46 both of them taken from
this current delivery delay

34:48 but with different times.

34:52 I think in terms of the
actual behavior of the model,

34:54 they would be very similar.

34:56 It's basically a
second order delay

34:57 versus a first order delay.

34:59 So it's not going to
make a big difference,

35:01 but it is sometimes
conceptually cleaner that way.

35:05 Now, yours has a little
bit of additional change,

35:09 that you're normalizing
the delivery delay that

35:12 is perceived by the company
versus the desired delivery

35:16 delay that they may have.

35:21 So it's really kind of the ratio
of those two that is input or--

35:26 so it's the minimum of the--

35:29 or wait, so delay reputation--

35:33 AUDIENCE: I just didn't want
[? them ?] to go below zero.

35:36 HAZHIR RAHMANDAD: Yes.

35:37 

35:40 Customer desired delivery delay
minus perceived delivery delay

35:46 divided by reputation
adjustment time.

35:51 So customer desired delivery
delay minus perceived delivery

35:56 delay-- that becomes--

35:58 

36:00 so this is actually not--

36:02 AUDIENCE: Yeah, that's
not right, is it?

36:04 HAZHIR RAHMANDAD:
It is not right.

36:06 So let's throw out the
minimum for us in our mind.

36:08 This part really is not
operational for most

36:10 of the behavior.

36:12 So what remains is the
customer desired delivery delay

36:15 minus perceived delivery delay.

36:17 So it is closing the gap
between perceived delivery

36:20 delay and customer
desired delivery delay.

36:23 

36:26 AUDIENCE: [INAUDIBLE]

36:27 HAZHIR RAHMANDAD: And then
it takes it into this delay

36:30 reputation stock.

36:31 So it is integrating the
difference between those two

36:34 things with some
adjustment time.

36:37 So integrating the
difference between--

36:39 so if customer desire is
always two months and perceived

36:43 delivery delay and the actual--

36:46 or sorry, the perceived
delivery delay is three months,

36:50 it is integrating minus
one months over time.

36:52 It's, like, adding and
adding to that stock.

36:55 So that's not what
you want to do.

36:57 So this is not correct.

37:00 So what you need is simply,
if you wanted to normalize,

37:03 you would say, I'm looking at
perceived delivery delay divided

37:07 by customer desired
delivery delay,

37:09 or, minus that divided by
something, as your indicated

37:14 reputation.

37:15 And then you would
have indicated

37:16 reputation minus
delay reputation

37:20 to inform the equation.

37:22 OK.

37:23 So that's delivery delay.

37:26 Factories-- this is kind
of a one stock version.

37:31 That gets a gap based
on the desired factory.

37:36 And desired factory
is coming from--

37:40 OK.

37:40 So this is--

37:41 AUDIENCE: Add together
work in progress

37:43 and the current
backlogs, basically.

37:45 HAZHIR RAHMANDAD: Yeah.

37:46 So it's looking at
the current backlog.

37:49 That is the work in progress,
outstanding order backlog

37:56 together.

37:59 Why-- oh, yeah.

38:01 So it's a little
bit tricky here.

38:05 So this is going to make it
harder for me to right now think

38:09 about it.

38:10 Because you're using
this capacity only

38:13 to drain this outstanding order
backlog relatively quickly.

38:22 But then you are using the
work in progress backlog

38:26 to expand the desired
factory as well.

38:31 And that makes things
a little bit harder

38:34 to make sure it is
fully consistent.

38:37 So if for whatever reason we
increase this time to complete

38:40 production, we increase the
work in progress backlog

38:45 by a factor of 10, now
your desired factory

38:48 will go up by a factor of
10 even though you are not

38:57 changing the purchase rate.

39:01 So now, at one level,
that is correct

39:06 because your time to complete
production has increased.

39:09 So you now need a lot more
work in process capacity

39:13 on the floor of the factory.

39:15 So it is not wrong
in that sense.

39:17 But the way we think
about factories,

39:19 that's more confusing.

39:22 So it is, again, kind of
an indicator for using

39:25 the standard formulation.

39:26 

39:29 And then here you would
be basically missing, OK,

39:34 what is the effect of desired
delivery delay, so to speak.

39:41 Again, that is now embedded.

39:44 So there is the effect of
delivery delay on the top.

39:47 But then there is the
effect of desired delivery

39:49 delay on what you want
the desired factory to be.

39:55 That is now embedded
inside these stocks

39:57 because they change with the
time to complete production

40:01 and time to process orders.

40:03 And the inherent
assumption here is then

40:05 that the desired delivery delay
is the sum of these two delays.

40:10 That's all kind of hidden
inside that formulation.

40:14 It makes it less
transparent for somebody

40:19 who is reading them all.

40:20 But I don't think it is wrong.

40:22 I'm just thinking it
can be simplified.

40:26 OK.

40:26 And then you have capacity
replacement plus something

40:31 about closing the gap.

40:32 But let's go into
this formulation.

40:34 So you can't remove factories.

40:36 That's important.

40:37 That's good.

40:38 Capacity replacement
plus factory gap

40:42 multiplied by construction
sensitivity divided by time

40:45 to build new factories.

40:47 So construction sensitivity is
coming from your delivery delay.

40:53 And you have customer desired
delivery delay versus perceived

40:56 delivery delay.

40:57 Now, this is a ratio-- so the
ratio of perceived delivery

41:13 delay to customer desired
delivery delay is 1.

41:17 Then this multiplicative
system will give you

41:23 a quarter, a value of 0.25,
which is your base sensitivity.

41:28 You're going to then
multiply your factory

41:35 gap by that sensitivity.

41:39 And then you would divide it
by time to build new capacity.

41:44 So that is fine.

41:46 It is closing the gap
with a time constant.

41:49 But if you notice,
basically, you

41:51 have two parameters
that are double counting

41:54 or just kind of redundant.

41:56 So the factory
construction sensitivity

41:58 has a parameter which
is multiplicative.

42:01 And then you are dividing that
by time to build new capacity.

42:06 And therefore, they
are fully collinear.

42:11 You don't need both of them.

42:13 So as such, it's
basically redundant.

42:19 AUDIENCE: How would you
get unit consistency?

42:23 [INAUDIBLE] sensitivity effect
on the time constant and then

42:28 [INAUDIBLE]

42:29 HAZHIR RAHMANDAD: Yeah.

42:29 So I think conceptually,
I see the appeal

42:36 of having a parameter
that changes

42:39 the strength of this feedback.

42:41 I probably would have used
a power function rather than

42:45 a linear multiplication.

42:47 And then the two would
have had different effects.

42:51 So it would have been that ratio
of perceived versus customer

42:57 desired raised to some power.

42:59 That would probably
do a better job.

43:02 OK.

43:03 So I think this
should work fine.

43:05 And then you have this
basic delivery here.

43:08 OK.

43:09 These are pretty meaningful
with a few places

43:17 that we could do better.

43:19 Sales force is converting
people who are interested.

43:26 And the conversion rate depends
on sales force outreach.

43:32 This is kind of how many
people they can reach out to.

43:37 AUDIENCE: The conversion rate
doesn't depend on sales force

43:40 average, but the sales does.

43:41 HAZHIR RAHMANDAD: Yes.

43:42 AUDIENCE: [INAUDIBLE]

43:43 HAZHIR RAHMANDAD: Yeah,
so you have the outreach.

43:45 And then conversion rate depends
on maximum, a reputation effect.

43:50 And what else does it affect?

43:53 So if you don't have any
total interested market,

43:57 how would you shut
off the sales path?

44:04 So you have it in here.

44:05 No, actually, you
do have it here.

44:07 

44:10 OK.

44:11 So the question I was asking
is-- the first order control

44:15 for the sales outflow.

44:18 And you want that
to be dependent

44:20 on total interested market.

44:22 It is coming here.

44:23 It is just not as visible.

44:24 So there is a maximum yearly
outreach per sales person

44:27 that is feasible versus
your yearly outreach that

44:31 comes from these people.

44:32 And you are probably using
some minimum function here.

44:37 Yes, minimum of
this yearly outreach

44:39 and maximum possible
per salesperson.

44:42 So that's fine.

44:43 That would do the job.

44:45 Now, again, the assumption
that goes into this equation

44:48 is important.

44:48 So the assumption that
goes into this equation

44:50 is that, basically,
if you don't have

44:54 enough people in
the market compared

44:56 to the capacity of
your sales force,

45:00 the utilization
of the sales force

45:03 goes down linearly with how
many people are in the market.

45:08 So that assumption
basically says

45:10 sales force people are not
that capable of identifying

45:16 open leads.

45:18 That is, if the
open leads go down,

45:20 you linearly are bringing
down the effectiveness

45:24 of your sales force people.

45:26 Whereas, if there are
just enough people,

45:29 the sales force will be fully
utilized at their 100% capacity.

45:36 So that utilization function
is kind of a little bit

45:40 too extreme on both sides.

45:41 That is, if I have
just enough people who

45:46 are interested in the product
as my sales force capacity,

45:50 it is a little bit
unrealistic to think

45:52 that the sales force capacity
will be used at its maximum.

45:56 And on the other hand, if
I have 80% of that number,

46:02 bringing down the utilization
by 20% may also be unrealistic.

46:07 So some softer adjustment using
one of the utilization functions

46:12 that we have seen in
other exercises as well

46:15 would probably be
a better idea here,

46:18 even though this is not wrong.

46:19 This is a good starting point.

46:20 So this would do OK.

46:23 But there are better
formulations there.

46:26 But otherwise, this is fine.

46:28 And it takes care
of the sales the way

46:31 you want it, again, with
the caveat that this now

46:35 assumes every new sales
is very much the same

46:41 as every repeat sales.

46:44 So that time to identify
new leads versus go back

46:49 to your old customers is
usually very different.

46:52 And therefore, it does
make sense potentially

46:55 to separate those two.

46:57 But this is a
simpler formulation.

46:59 And it's fine to have
a simpler formulation.

47:01 Just be conscious that you
are making that choice.

47:03 And I think some of the folks
have an alternative here.

47:06 OK.

47:07 I think formulation-wise this
is a good summary of what

47:11 is happening here.

47:12 I assume you have not--

47:16 you have a fixed
sales force fraction.

47:19 Yes.

47:19 So this fraction is fixed.

47:22 And then we have the accounting
that takes care of it.

47:25 OK.

47:25 Let me just go to
some random other--

47:27 AUDIENCE: [INAUDIBLE]

47:28 HAZHIR RAHMANDAD: Yes.

47:29 Go ahead.

47:30 AUDIENCE: [INAUDIBLE] Just going
back to the capacity [INAUDIBLE]

47:35 this is kind of what I
was asking about early on.

47:37 

47:41 Yeah, so I had this
issue where just

47:44 something that I was considering
was that factories take

47:46 two or three years to build.

47:48 And so if a factory
is deprecated,

47:52 you can't just
immediately replace it.

47:53 HAZHIR RAHMANDAD: Yes.

47:54 AUDIENCE: Right?

47:55 So--

47:55 HAZHIR RAHMANDAD: Yes.

47:56 So that's right.

47:57 So this is definitely
a simplification

47:59 that, in case of this
exercise, I would have--

48:02 I think in the
problem definition,

48:04 there is a conversation
about the time it

48:06 takes to build the factories.

48:07 So I think a better formulation
would include the factory

48:10 under development stock.

48:11 And in fact, I would also
use higher order delays

48:15 for depreciation of factories.

48:17 First order depreciation is kind
of a weird thing for a factory.

48:22 The year you built
a factory, you

48:23 don't start throwing it
out of your capacity.

48:27 So at least a third
order delay is due there.

48:30 Even for completion of factories
out of the work in process,

48:34 that also makes sense to
have a higher order delay.

48:38 So that would be probably
a not cleaner necessarily,

48:43 but a more realistic solution.

48:46 All right.

48:46 So which is this one?

48:50 So this is Kathy's.

48:53 Let's take-- so
manufacturing here,

48:57 we had these units that are in
the queue versus in production.

49:02 We talked about-- it's a little
bit similar to Jake's part,

49:07 that you probably don't
need all of that detail.

49:11 But it could work just fine.

49:14 So the way you are
doing it is also

49:15 similar to Jake in the sense
that the production start

49:19 is gated by the capacity.

49:23 And so this is one
of those places

49:27 that I'm now not sure
what is happening.

49:30 So the manufacturing
capacity, you also

49:33 have it in units rather
than units per unit of time.

49:36 So that's exactly the same issue
that we had with Jake's point.

49:40 And again, I think
that's deviating

49:44 from standard formulations
that will make some challenges.

49:47 Now, it doesn't
mean it is wrong.

49:49 So let's look at what is
happening with the-- so you

49:51 are saying the
units in production

49:54 are stopping or kind of
limiting what capacity remains.

50:01 Whatever is not in the
production opens up

50:04 a gate for starting production.

50:07 And that gate is controlled
by some minimum time

50:09 to start production.

50:12 And that minimum time
to start production also

50:15 gates the desired
production start.

50:18 This is actually very similar
to Jake's formulation, I think,

50:22 mathematically.

50:23 It has the same problems with--

50:26 yeah, I think it will work.

50:29 It wouldn't generate any
wrong results, but it is--

50:34 AUDIENCE: My question is, what
is including this [INAUDIBLE]?

50:40 Because I think the
problem statement

50:41 said, assume just a backlog,
no work in progress.

50:47 So [INAUDIBLE] just
right on backlog.

50:51 And there was no capacity in
use and non-working capacity.

50:55 So I didn't even
think to do that.

50:56 HAZHIR RAHMANDAD: Yeah.

50:57 I don't know.

50:58 What were you trying to do?

50:59 What were you trying to get
out of this formulation, Kathy?

51:02 Do you remember when
you were doing this?

51:06 AUDIENCE: Wow,
[INAUDIBLE] yeah, I

51:10 think I was just picturing
in my mind what is happening.

51:16 Units are kind of-- oh, these
are the orders we have to fill.

51:20 OK.

51:20 That's different.

51:21 When do we get to
start something?

51:23 When we have an
available slot for it?

51:27 What are the slots determined
[? by, ?] the capacity?

51:29 So I think I was just really
like taking it literally

51:32 from that image in my mind.

51:34 I wasn't, like, abstracting.

51:36 And then the capacity thing--

51:39 I think it was just a
product of my brain.

51:45 But I had it originally in units
per month and more so standard.

51:51 And then I started thinking
about the slots idea

51:55 and how that would kind
be easy to implement.

51:57 And so I changed it all last
minute to units and just carry

52:00 [INAUDIBLE].

52:01 HAZHIR RAHMANDAD: Interesting.

52:02 So that makes it a little
bit more clear for me

52:04 how you thought through it.

52:05 And I think the process lesson
out of that is, on the one hand,

52:09 being operational-- just
you try to be operational.

52:12 Being operational is usually
a good skill and good thing

52:15 to do in the modeling because
you have a tangible thing

52:18 that you're trying to track.

52:21 But then it sometimes gets
you too much into the weeds.

52:24 And you may get lost in a
model that is out of balance.

52:28 That is, it has too much
detail in some sector

52:30 and is kind of missing other
feedback, complexity parts that

52:35 may be more important.

52:35 Now, I don't think you
are missing something here

52:37 on the other side, necessarily.

52:39 But just that
creates a trade off.

52:43 There is really no
easy solution to that.

52:46 This is kind of a skill you have
to build of, OK, let me go deep,

52:51 have an operational story,
but then ask myself,

52:53 how can I summarize?

52:55 Do I need all of
that complexity?

52:57 And I think the time
constants for these

53:00 and what it buys you--
do I use, for example,

53:03 these units in
production differently

53:05 from units in production queue?

53:06 You're not.

53:07 You're just basically
adding up both of those

53:10 to calculate a delivery delay.

53:12 So why do I need--

53:14 AUDIENCE: Well, so I'm using
them differently in that one

53:18 of them is capacity constrained
and one of them isn't.

53:22 Like, there's no constraint
on me taking orders.

53:26 And so I didn't want to meter
the process of taking orders.

53:30 I wanted to meter the process
of starting production.

53:34 AUDIENCE: Why are we
taking orders [INAUDIBLE]?

53:37 AUDIENCE: I can't hear you.

53:38 What are you--

53:38 HAZHIR RAHMANDAD:
So taking orders

53:40 is units entering
queue, correct?

53:41 AUDIENCE: Yeah, yeah.

53:42 And I didn't want that to be
capacity constrained because--

53:45 HAZHIR RAHMANDAD: So
that's not capacity

53:46 constrained in a single stock.

53:48 So think about a
situation where,

53:51 rather than having
these two stocks,

53:52 you just didn't have this flow.

53:54 This was the one single stock.

53:56 And the outflow here was
constrained by the capacity,

54:00 your total capacity.

54:01 That's the solution that
would sidestep these problems.

54:05 OK.

54:05 Your average
delivery delay is now

54:08 calculated as units in
production plus units

54:10 in production queue
divided by unit delivery.

54:17 And then, what is
the customer delay?

54:21 Oh, that's just the [INAUDIBLE].

54:22 So that's the x.

54:23 OK.

54:24 That's fine.

54:26 If it goes 0, it becomes
expected [? delivery. ?]

54:30 AUDIENCE: Yeah, I
didn't really know

54:31 what was the best thing to
make the x in that case, but

54:35 [INAUDIBLE].

54:35 HAZHIR RAHMANDAD: Yeah.

54:37 So if your delivery
rate goes to 0,

54:41 basically the average delivery
delay is a very large number.

54:46 That basically says
things are not good.

54:49 So if you use expected
delivery delay,

54:51 that's not the best choice.

54:52 It is actually saying,
this is the level

54:54 that people will be happy with.

54:56 So if ever this model
touches the situation when

54:59 there is no delivery,
it will create

55:02 delivery delays that are
very attractive to customers.

55:04 And as such, that's
not the right choice.

55:07 Now, in your simulation,
you may never see that.

55:11 So you may not
understand or see it

55:14 in terms of the actual behavior.

55:16 But when you are
putting that equation,

55:18 this is the thinking
that you have to do?

55:21 AUDIENCE: But what
if there are no units

55:23 in production [INAUDIBLE]?

55:25 AUDIENCE: Yeah,
so I was thinking

55:26 if there are no
units in production,

55:28 it's because there
are no orders.

55:32 There's nothing going on.

55:33 Therefore, there's no reason
for the perceived delay

55:38 to really deviate
from the expectation.

55:39 HAZHIR RAHMANDAD: So
basically, then you

55:41 have a 0 numerator
and a 0 denominator.

55:47 AUDIENCE: Yeah.

55:48 HAZHIR RAHMANDAD: So that
is a different situation.

55:50 That happens rarely in this
model because as long as--

55:55 AUDIENCE: It's just
that the first--

55:56 HAZHIR RAHMANDAD: Getting
these stocks to be 0

55:58 is very hard because
it requires somehow

56:00 emptying anything that was in
the stocks in the first place.

56:04 Whereas, getting the flow
to be 0-- that's basically,

56:07 if you shut off production, it
goes to 0-- now, in your model,

56:11 not really.

56:11 Because this also
depends on the stock.

56:13 So this part of
the delivery delay

56:17 is always average completion
time unless units in production

56:21 goes to 0.

56:22 But the way units in
production goes to 0

56:25 is when you shut off this flow
through, for example, not having

56:29 capacity or something.

56:31 Anyway, this is OK.

56:33 There's nothing bad here.

56:35 And perceived
delivery delay-- fine,

56:37 you are using some smooth
function, I assume.

56:40 And smooth 3 might be an
overkill-- just a simple smooth.

56:45 So a smooth 3 is information
delay third order.

56:50 You usually don't use it
that much because it requires

56:55 a measurement system
that has multiple steps

56:59 and then kind of
maybe cobbled together

57:01 with some additional
perception of stakeholders.

57:04 It is only in those situations
where a higher order

57:07 smooth function is justified.

57:08 Typical perception
processes are very much

57:10 first order delays, first order
smoothness-- but not a big deal.

57:15 I would put a box around things
that have a smooth or delays so

57:20 that, when I look
at the diagram,

57:22 I quickly see what
are the hidden

57:24 stocks in the formulation.

57:29 And then you have the
delivery based reputation

57:34 as just the ratio
of these two things.

57:38 And you are saying it
doesn't go above 1.

57:44 So that is, if--

57:47 it doesn't go above 1?

57:50 Yes, doesn't go above 1.

57:53 So if this ratio is customer
delivery delay expectation is

57:57 much larger than
perceived delivery delay,

58:00 you want to filter
out those situations

58:03 and say, delivery delay
based reputation is OK.

58:05 It's 1.

58:07 That's OK.

58:08 Nothing wrong there.

58:09 But when I see that
formulation, I also

58:11 have in the back of my
mind that you're basically

58:14 removing information about
situations where delivery

58:19 delay is even better than
what the customers want

58:22 for downstream usage
of this variable.

58:24 And do I want to do that?

58:27 There is always a question.

58:28 Now, I may want to do it
because it simplifies my life

58:33 to worry about the range.

58:35 I know now that this is
always between 0 and 1.

58:38 So in all other places, I just
use it with that assumption.

58:41 I don't think about it.

58:42 But on the other hand,
I'm stopping myself

58:46 from having more nuanced
formulations that

58:48 may benefit from the fact that,
OK, I now have a situation where

58:53 I'm doing really well compared
to what the customer is--

58:55 but a little bit of
a trade off there.

58:59 OK.

58:59 So manufacturing capacity
fairly similar to Jake's, I

59:05 think, in terms of
having a single stock.

59:09 Lifetime-- again, first order
delay not the best formulation.

59:13 Missing work in process--

59:15 not the best
formulation, but OK.

59:18 And then indicated
manufacturing capacity--

59:21 you are getting it from this
units in production queue.

59:25 So this is one of these
places that things

59:27 start to get messy
because you're

59:29 ignoring units in production.

59:31 You're just getting it from
units in production queue.

59:33 

59:36 And then you're just generating
the gap between the two.

59:39 So you are not
getting the feedback

59:41 from the delivery delay that
is perceived by the firm.

59:45 So that's an important missing
part of this whole thing.

59:51 Now, it is not that it
is completely missing.

59:53 Because when your
delivery delay is high,

59:55 these units in
production queue go up.

59:57 So as such, it is
implicitly there.

60:02 But this is just not the
cleanest formulation.

60:05 It is also missing the
replacement pathway.

60:10 So this will create
a steady state error.

60:12 AUDIENCE: [INAUDIBLE]

60:14 HAZHIR RAHMANDAD: So if
manufacturing capacity

60:16 decommissioning is missing
from the replacement

60:20 or from the new builds,
in the steady state,

60:24 you always have an
error-- error in the sense

60:26 that you are not getting
what you have desired.

60:30 So manufacturing
capacity is always

60:34 above your actual
manufacturing capacity.

60:37 So that's bad stock
management in general.

60:41 Is that part clear?

60:43 Anybody has a question on that?

60:44 Because that is not a
trivial, obvious thing.

60:47 But if you have built stock
management structures,

60:51 you have come across that thing.

60:53 That is, for the
stock management

60:55 to be internally consistent
and give the desired values,

60:59 you always need two
different components.

61:02 One is replacement of anything
that is going out of the stock.

61:07 The other is closing the
gap between the desired

61:10 level and the current level.

61:12 If you only have
the closing the gap

61:14 between desired
and current level,

61:17 you will have what we say
is a steady state error.

61:21 It means in the steady state,
the outflow is not replaced.

61:28 And therefore, there should
be a gap between the desired

61:32 and actual to generate enough
inflow to equate the outflow.

61:38 So therefore, by definition,
your desired level

61:42 will always be above
your current stock

61:45 in the equilibrium.

61:46 And that is just not right.

61:48 So that's important.

61:50 Hassan?

61:51 AUDIENCE: In the
text of the question,

61:54 you first suggested that we
look more into the pressure that

61:58 these [INAUDIBLE]
disclaimer, I didn't.

62:02 I went for the
[INAUDIBLE] and I knew

62:04 that I didn't [INAUDIBLE]
but that doesn't

62:09 apply to when we're
formulating based

62:11 on the pressure in the company.

62:12 HAZHIR RAHMANDAD: Yeah.

62:13 So the pressure based--

62:14 kind of the intuition
there is that the firm

62:17 is creating an anchor based on
their current level of capacity

62:25 and then decide whether
to expand or contract.

62:28 And if it is expanding, it
is coming from the pressure

62:32 to expand.

62:32 So that anchor and adjustment
is a different formulation

62:36 for stock management compared
to replacing what is coming in

62:40 and adding the--

62:43 AUDIENCE: The
pressure formulation

62:45 based on the intensity of
change that the company actually

62:50 does based on that pressure.

62:52 There is a chance
that they will have--

62:55 HAZHIR RAHMANDAD:
They will overshoot.

62:56 AUDIENCE: Yeah, or they can't
keep up with [INAUDIBLE].

62:58 HAZHIR RAHMANDAD: Or they
can't keep up, absolutely.

63:01 So that pressure-based
formulation alternative-- first

63:04 of all, even in that one, you
do need the replacement piece.

63:10 If you don't have the
replacement piece,

63:12 it will create a
steady state problem.

63:15 Because there's always
kind of an outflow.

63:17 And the inflow is just
always trying to catch up.

63:20 So there will be a gap
between the desired, which,

63:23 the desired can come from your
current level with the pressure.

63:26 But still, there will be a gap.

63:27 So as such, that is also
having the same problem.

63:32 It's just that, where
does the desire come from?

63:35 Does it come from the
customer orders or something

63:37 along those lines?

63:38 Or does it come from the
delivery delay perceived

63:44 and the anchor being
current capacity?

63:49 I think both of them
are pretty legitimate.

63:51 And in fact, the behaviors
may not be that different.

63:55 In fact, anchoring to what
is the current backlog

63:59 or current recent
customer order rates

64:03 is less prone to big swings.

64:07 Because if you have a
very strong or very weak

64:10 response to that pressure,
then your desired levels

64:15 will not be matching
or will be overshooting

64:19 what the customers are asking.

64:20 And that creates instability.

64:22 But I asked for that
formulation exactly

64:24 because of that challenge.

64:26 That is how Forrester
formulated it.

64:30 And that is one
of the reasons you

64:33 get kind of very unstable
behaviors in the market growth

64:37 models.

64:37 If you went with the more
standard stock management,

64:41 it is actually a
little bit more stable.

64:43 Now, I haven't done the
full comparison there.

64:48 AUDIENCE: Could
you explain again

64:49 why it's more unstable if you
do it with delivery [INAUDIBLE]?

64:52 HAZHIR RAHMANDAD: So when
you are doing it with the--

64:55 there is an impact of
delivery delay on expansion.

64:58 So your desired factory level
would be your current factory

65:03 level multiplied by some
effective delivery on capacity

65:09 expansion.

65:10 That effective delivery
on capacity expansion

65:14 is dependent on some parameter
or some table function.

65:17 But let's say a parameter.

65:18 And it can be sharper
response or slower response.

65:23 And that sharpness is not
controlled in any direct way

65:27 by how big is your
delivery delay

65:31 or how big is your
customer demand currently

65:35 compared to your capacity.

65:36 So ultimately, if your customer
demand is in widgets per year

65:40 or widgets per month,
and your capacity is also

65:44 in widgets per month,
you want the two

65:46 to be matching with the
potential extrapolation

65:50 that demand is growing.

65:51 So let me look forward
a few months based

65:54 on how long it takes to create
capacity so that I'm matching

65:58 the demand I expect to have
six months or two years

66:02 from now, whatever is your
work in process delay.

66:06 That is kind of the more
clean, logical approach,

66:14 in the sense that you have a
anchor that directly takes you

66:18 to serving the customers
exactly at the rate

66:21 that they are going to come in.

66:24 You can add a buffer
or whatever you want.

66:26 But the alternative doesn't
provide that direct mapping.

66:30 And therefore, you can be too
fast in expansion or too slow

66:35 in expansion.

66:37 AUDIENCE: Oh, wait.

66:37 Hold on.

66:38 I thought you were saying
that the delay formulation's

66:41 anchoring is what may
lead to more instability.

66:45 Whereas, the alternative
that you're saying is,

66:47 this is more stable, yeah.

66:49 HAZHIR RAHMANDAD: The
one that is more stable--

66:51 or not necessarily stable,
but cleaner in the sense

66:55 that it is more rational--

66:56 is the one that gets
the desired production

67:00 rate from the expected
customer order rate

67:07 and then from that calculates
the desired production capacity.

67:12 AUDIENCE: Which is what
Kathy's doing, right?

67:14 HAZHIR RAHMANDAD:
Which is what Kathy

67:16 is doing, with a caveat
that Kathy is not

67:18 taking it from
the units entering

67:22 queue, which is the demand.

67:24 She's getting it from this
stock here and then turning it

67:28 into a stock thing.

67:30 Because this
manufacturing delivery

67:31 is also not in the units
of widgets per month.

67:35 But it is in the units
of units or widgets.

67:38 So that creates a little bit
additional messiness here

67:42 that I can't mentally
simulate fully.

67:47 AUDIENCE: So two more
technical questions.

67:49 So first is that, because this
firm is producing to a backlog,

67:53 they have some desired
shipments, which

67:54 is the backlog divided by some
desired shipment time-- again,

67:57 with a single stock [INAUDIBLE].

67:59 So what is the
difference between using

68:01 that versus the order rate?

68:04 HAZHIR RAHMANDAD: It
should be about the same.

68:06 So basically, you do the backlog
divided by delivery delay.

68:10 You get the average level
of the orders coming in.

68:14 So as such, it is a little
bit more stable a signal.

68:17 So if you have a lot
of ups and downs,

68:19 that's a better formulation.

68:21 For a deterministic model
that doesn't kind of

68:23 have noisy things, then it
doesn't make a difference.

68:26 AUDIENCE: And then
my second question

68:28 was that Jake kind of
did both, actually.

68:30 Like, he determined the
indicated capacity level

68:34 by the backlog
level or something.

68:37 But then the time was
adjusted by this pressure

68:40 due to delay essentially.

68:41 Because he had this [INAUDIBLE].

68:43 HAZHIR RAHMANDAD: Yes.

68:44 So basically, he was
thinking of closing the gap

68:47 to be more sensitive
or less sensitive

68:50 based on the delivery
delay that is observed.

68:54 And that is actually a nice
formulation in the sense

68:57 that, you are closing the gap no
matter what, but how fast you're

69:03 closing the gap is partly driven
by how bad the delivery delay

69:09 situation looks like.

69:10 So I think I like that,
as it kind of conceptually

69:13 captures a bunch of these
problems we are trying to solve.

69:17 OK.

69:18 I think this is good
conversation in this model.

69:21 Just a quick thing-- so I assume
you are using a fixed sales

69:25 force--

69:28 not fixed, fractional
sales force.

69:30 AUDIENCE: Yes.

69:30 HAZHIR RAHMANDAD: OK.

69:31 So that's fine.

69:33 That's fraction of revenue.

69:35 I'm not going into through
the rookie dynamics.

69:39 I assume they are coming from
the standard formulations

69:42 in Stearman.

69:43 AUDIENCE: [INAUDIBLE]

69:45 HAZHIR RAHMANDAD: Yeah.

69:46 Good.

69:47 Let's do a couple more models.

69:51 Let's see.

69:51 Who's is this one?

69:52 Ann.

69:54 OK.

69:55 So again, we have the
facilities, first order

70:01 draining--

70:02 not the best
alternative, but OK--

70:05 new construction, coming
from gap from threshold.

70:12 

70:16 OK.

70:16 So the new construction--
let's look at the equation.

70:19 This is a little bit--

70:22 so you have the total
facilities divided by time

70:25 to expand multiplied
by effective delivery

70:29 delay on capacity expansion.

70:30 Ann, can you explain
what you were thinking

70:32 in formulating it this way?

70:34 

70:39 AUDIENCE: Yeah.

70:40 So I misunderstood the prompt.

70:43 But I was thinking that
just because there's a--

70:48 I was thinking that the
decision to build new facilities

70:51 depends on your particular
threshold of customer

70:57 dissatisfaction because of the
cost in building new facilities.

71:01 So even though you're
not meeting the customer

71:04 expectations, there's
still that delay

71:07 until a certain threshold
has been exceeded.

71:11 And then they decide to
create new buildings.

71:13 And they just increase
by, like, a percentage

71:18 based on the current
facilities that they have.

71:20 HAZHIR RAHMANDAD: Yeah.

71:21 So this is not really doing
what you were thinking

71:25 or what you need to do here.

71:27 Because basically,
this one is creating

71:29 a very strong first order
reinforcing loop that says,

71:32 the more facility
you have, the more

71:33 you will build, with
some attenuating

71:38 effect coming from
effective delivery

71:40 delay on capacity expansion.

71:41 So if your total
capacity is very high,

71:46 then probably this delivery
delay effect gets smaller.

71:51 And at some point, it may
slow down or even stop.

71:55 So this is a little bit
additional complexity here

71:59 to understand.

72:00 But this is kind of 1 minus
e to the power of something.

72:03 So it's probably going down
with more gap in delivery delay.

72:11 

72:16 1 minus e to the power of
minus-- so it goes up like this.

72:21 Yeah.

72:22 So if you don't have any
delivery delay, it can go to 0.

72:26 If this goes to 0,
then you wouldn't

72:29 be building new capacity.

72:31 So it may look
like it is working,

72:33 but it kind of works in a very
weird way that doesn't directly

72:36 map into useful
real-world constructs.

72:40 So the solution,
again, is basically

72:43 a factor for replacement
of death to buildings

72:47 and a factor for adjusting
toward your desired level.

72:52 So there is a desired level
of capacity minus facility

72:56 minus current facility.

72:57 And that desired facility could
come from your current facility

73:02 as well multiplied
by some factor that

73:05 is expanding the facility
based on delivery delay.

73:08 So something along
those lines might

73:10 be what you need to have here.

73:14 Backlog part fairly simple--
and simple is good here.

73:20 Just have new orders coming in.

73:24 And you have the orders
versus customers.

73:26 So you have the
change of units here.

73:28 That's fine.

73:29 And then the delivery of
units is determined by what?

73:35 

73:38 Backlog divided
by delivery delay?

73:40 Oh.

73:43 Oh.

73:45 Huh.

73:46 OK.

73:47 Yeah, this works.

73:48 Ann, this is an
interesting piece.

73:51 What you have is right,
but it's not following

73:54 the classical formulations.

73:56 And it creates a little
bit of a confusion for me

73:58 when I first saw it.

74:00 So typically, we would
have the delivery

74:03 to be regulated by the
production capacity.

74:07 So it would be the minimum
of production capacity

74:11 and maximum delivery rate.

74:14 And that maximum
delivery rate would

74:16 come from backlog of orders
divided by a minimum time

74:20 to deliver.

74:21 So that would be
your order delivery.

74:23 Then backlog divided
by order delivery

74:26 gives you the delivery delay.

74:28 The way you have calculated
it is the other way.

74:30 That is, you have calculated
the delivery delay

74:33 using production versus backlog.

74:36 And you have basically
divided the backlog

74:40 by production capacity.

74:43 AUDIENCE: [INAUDIBLE] idea
was like there's a fixed

74:47 capacity for each facility.

74:50 And as the backlog
increases, then there's

74:54 a delay in delivery
to customers.

74:57 HAZHIR RAHMANDAD: No, I'm
not saying it is wrong.

74:59 I'm saying this is kind of not
the typical way we formulate

75:01 this.

75:03 And the way you have
formulated it also kind of

75:06 takes away this constraint
of maximum delivery

75:11 rate coming from not having
enough in the backlog.

75:14 

75:20 Yeah.

75:21 And again, it doesn't make
a big difference here,

75:24 but it is just a little bit
non-standard formulation.

75:29 AUDIENCE: Isn't
deliveries in this case

75:30 always equal to production
capacity [INAUDIBLE]?

75:33 HAZHIR RAHMANDAD: So,
Yes, deliveries will all--

75:37 no.

75:38 So when the backlog goes to 0--

75:40 

75:43 but then you're dividing it by
this delivery delay that is 0.

75:47 Then it is always
production capacity.

75:49 And therefore, you don't
have first order control.

75:52 You will get
problematic behavior.

75:55 You're right.

75:56 

75:59 Ann, what Alexander
noted here is that when

76:05 you multiply your backlog
or divide your backlog

76:09 by your delivery delay, remember
that delivery delay is already

76:13 your backlog divided
by production capacity.

76:15 So the backlogs
cancel out each other.

76:18 And basically,
your order delivery

76:20 becomes production capacity.

76:22 And therefore, you wouldn't
have the first order control.

76:26 That is, you wouldn't
have a limit that avoids

76:30 your backlog going negative.

76:33 Now, in your formulation,
basically the model

76:36 will crash because you
will get to a backlog of 0.

76:39 And then you will
have a division by 0.

76:41 That will be what will happen.

76:45 So, yes, use the
standard formulation.

76:48 That's the summary of this case.

76:53 Then we have potential customers
becoming likely customers.

77:01 And there is kind of
effective delivery

77:03 delay on conversion rate.

77:05 

77:11 So the conversion
rate-- these are

77:12 people who have learned
about the product

77:17 through the sales channel.

77:20 OK.

77:20 So the conceptualization
here, Ann,

77:23 if I'm understanding
it correctly,

77:25 is that the main
effect is happening

77:28 through this conversion rate.

77:30 And once people have
converted, then with the time

77:32 constant they order.

77:34 So this is your order rate,
customers placing orders.

77:38 And then orders are delivered.

77:43 They become customers
with products.

77:45 And after a while, they
go back and buy it again.

77:48 So--

77:49 AUDIENCE: Yep.

77:49 HAZHIR RAHMANDAD: --you are
not using the sales force

77:52 to basically to do two things.

77:57 One is to convince
these people that

78:01 have stopped using the product
to come back and buy it again.

78:06 So this step is
happening automatically.

78:08 Secondly, you are
adding this delay

78:11 between the time people
are contacted and convinced

78:15 by the sales force until
they decide to put an order.

78:19 Now, that second one is fine.

78:22 I think conceptually
that's not a problem.

78:24 The first one is
more problematic.

78:26 You do need sales
force to also convince

78:28 people who need to do
a replacement purchase.

78:34 AUDIENCE: OK.

78:36 HAZHIR RAHMANDAD: OK.

78:38 Let's see.

78:39 Anything else here?

78:40 So sales force-- you have
the replacement time.

78:45 Oh, time sales
force to be fired.

78:48 AUDIENCE: So this
part [INAUDIBLE]

78:49 but I think the idea
was that there's

78:55 a percentage of revenue reserved
to pay the wages of sales force.

78:59 HAZHIR RAHMANDAD: Uh-huh.

79:00 

79:03 AUDIENCE: And if the cash
available is too small,

79:11 then they would fire
some members of the sales

79:14 force so that they always
have that money to pay them.

79:17 And then if the cash
builds up again,

79:20 they would hire [INAUDIBLE].

79:21 I didn't have time
to formulate that.

79:23 HAZHIR RAHMANDAD: I see, I see.

79:24 So basically, you're
kind of having money that

79:27 is put aside for sales force.

79:29 And if you have--

79:30 AUDIENCE: [INAUDIBLE]

79:31 HAZHIR RAHMANDAD: Yeah.

79:32 And if you have
enough money, you

79:35 are keeping your sales force.

79:36 Otherwise, you're firing them.

79:39 AUDIENCE: Yeah.

79:39 HAZHIR RAHMANDAD: And then you
have an exogenous hiring rate.

79:42 You're just hiring people.

79:43 So--

79:45 AUDIENCE: No, that
part is not complete.

79:47 I was supposed to
replace the people fired

79:52 as well when the
cash builds up, but I

79:54 didn't have time to put it in.

79:56 But that's the idea.

79:57 HAZHIR RAHMANDAD: So it
is somewhat convoluted.

80:01 Mostly, people control
their stock of employees

80:04 through hiring.

80:06 Firing does happen.

80:07 So that's OK to have a firing
that is also determined

80:10 based on money you have.

80:14 But adding this stock of cash
that is reserved for salaries

80:19 is kind of not adding
that much value in terms

80:23 of, it kind of just adds
a bunch of parameters

80:26 and additional structure
you need to manage.

80:29 Even having explicit
hiring and firing

80:32 may not be the
most effective way.

80:34 You can just have an
adjustment of sales force using

80:37 a first order
adjustment process.

80:41 And then the desired
sales force can easily

80:43 come from your budget
for the sales force.

80:46 I think that's what others
also had in this formulation.

80:49 That's much simpler.

80:51 If you think people are
less eager to fire people

80:59 than to hire people,
which is part

81:00 of the real
organizational dynamics,

81:03 you can make it an asymmetric
delay and adjustment

81:06 so that, when the desired
level of sales force

81:10 is higher than
the current level,

81:13 you adjust it much faster.

81:15 When the desired level is lower,
then you adjust it more slowly.

81:19 In the extreme, it would be
how long people typically

81:22 stay in your company, which is
for the downward adjustment.

81:25 That is, you just let it happen
through natural turnover,

81:28 not through actually
firing people.

81:31 So that's a simple way to take
care of the hiring and firing,

81:36 even if they are asymmetric
in terms of adjustment.

81:40 AUDIENCE: I think
my confusion was

81:41 like, if there's a fixed amount
that is allocated to the sales

81:44 force, then how do you control
if that amount is [INAUDIBLE]

81:50 HAZHIR RAHMANDAD: So what's
the fixed amount unit?

81:52 So what's the unit of what
is allocated to sales force?

81:56 AUDIENCE: Maybe a dollar
value per time period

81:59 as a percentage of the revenue.

82:01 HAZHIR RAHMANDAD: Great.

82:02 So let's say dollar per month.

82:04 So I have $1,000 per month.

82:07 I mean, $1,000-- who comes to
work for me for that price?

82:10 But let's say $1,000 per month
of budget for my sales force.

82:16 And then each salesperson,
now that we are so cheap,

82:21 is willing to work
for $50 a month.

82:24 So what's the number of
sales force I can have?

82:30 AUDIENCE: [INAUDIBLE]

82:31 HAZHIR RAHMANDAD: So
that's 20 sales force.

82:36 You're adjusting your current
stock towards that desired.

82:38 You take care of all of that.

82:39 You don't need to worry about
another stock that accumulates

82:42 that $1,000 and then
tries to spend it.

82:46 It's just too many things.

82:48 OK.

82:49 Good.

82:49 I think it's a good
time to take a break--

82:51 10 minutes.

82:53 And then we come back,
look at a few more models.

82:55 

82:58 So one very minor
thing here is, you

83:03 are starting the DELAY3
function without initial.

83:06 So it is initializing
it in equilibrium.

83:10 But the stock here of
production capacity, PC,

83:14 is starting with initial PC.

83:17 So this creates an
internal inconsistency.

83:21 So this is a little bit
kind of subtle there.

83:24 Because in this link from PC
completion to PC depreciation,

83:30 there are three stock variables
hidden behind the scenes.

83:35 And they have their
own initial value.

83:37 The initial value used there
is basically the PC completion

83:43 rate at the beginning multiplied
by facility life divided

83:49 by 3 for each of those stocks.

83:52 That's what is being
used in the back end.

83:58 But what you're using as
the sum of those three

84:01 that should be the production
capacity is initial PC.

84:04 And there is no reason here
to automatically expect

84:08 these two to be the same.

84:10 And that can create weird,
unexpected behaviors.

84:14 So I would have it as a DELAY3
EI with initial condition

84:20 and set the initial condition
to be your initial PC divided

84:25 by facility life.

84:27 Then you're all set.

84:28 AUDIENCE: Can I ask how that
takes care of the issue?

84:31 Because PC divided
by facility life

84:34 only happens for the
initial time step.

84:36 So after you drain
whatever fraction is there,

84:39 then you go back to just only--

84:42 like, do you see what I mean?

84:44 You're still draining--

84:46 I guess I'm just asking is--

84:47 HAZHIR RAHMANDAD: So I'm
trying to get the production

84:50 capacity, PC, to be
exactly the same as some

84:53 of those three
initial stocks that

84:57 are hidden behind this link.

85:00 OK?

85:00 Some of those three
initial stocks

85:03 would be whatever I give
it as the initial outflow,

85:07 initial value of the delay.

85:10 The initial value of
delay is the outflow,

85:12 in this case, PC depreciation.

85:15 So it would be that
initial outflow

85:19 multiplied by facility life.

85:23 So by setting that
initial value to be

85:27 initial PC divided
by facility life,

85:30 I achieve this equivalence.

85:32 And once I started from
the equivalent value,

85:35 they will remain
equivalent all the way

85:37 through because the inflow and
outflow of production capacity

85:42 PC is coming from this--

85:43 I mean, the outflow is
coming from this delay.

85:46 That inflow is also this
initial of the delay.

85:48 So then they are always going
to be the same moving forward.

85:54 OK.

85:54 So WIP first order
delay-- that's fine.

86:00 PC building is coming from--

86:03 OK.

86:03 Let's see what is happening.

86:06 Desired PC building--
this is probably max of 0.

86:08 And desired PC building--
something that you always

86:11 want to make sure is in place.

86:14 You have an adjustment for WIP.

86:16 You have indicated
expansion to meet demand

86:21 based on the current
production capacity.

86:28 

86:31 OK.

86:31 So let's see what
is happening here.

86:33 

86:37 So you're looking at the total
need divided by current value.

86:43 So this is desired
stock minus stock.

86:46 So this is a stock adjustment.

86:50 This stock adjustment
plus the replacement--

87:01 and what is the expansion
commitment delay

87:05 you have here, Alban?

87:08 Do you have a kind
of a story there?

87:10 AUDIENCE: So I was
trying to capture,

87:17 you have decision making time.

87:18 Like, you don't come into
inspection immediately

87:21 [INAUDIBLE].

87:22 HAZHIR RAHMANDAD: OK.

87:23 OK.

87:23 That's fine.

87:25 That's conceptually correct--
maybe an overkill here,

87:29 but that's OK.

87:30 And you were missing that unit.

87:32 OK.

87:33 Or maybe I deleted it somehow.

87:35 

87:38 Then desired completion is
just the sum of these two.

87:43 And then you add the
adjustment for WIP.

87:46 So this is fairly standard.

87:47 So the key question is, where
does the indicated total PC need

87:50 come from.

87:52 You are looking at the
excess delay and the current.

87:55 

87:57 AUDIENCE: So you're just scaling
up your production capacity

88:00 but the [INAUDIBLE].

88:01 HAZHIR RAHMANDAD: Yes,
with some delay effect.

88:05 And this excess delay
effect is coming

88:08 from the actual delivery delay
versus desired delivery delay.

88:15 So this is a fairly
rapid perception

88:19 of the delivery delay.

88:21 But because you have this
additional delay for expansion

88:24 commitment, that delay is kind
of captured there in a sense.

88:28 So we didn't have an explicit
separate delay for perception

88:33 of delivery delay by company.

88:35 But instead, we have
an adjustment there.

88:39 And this excess delay is
just a ratio of these two.

88:43 Similar to Kathy,
you are limiting it

88:46 to a floor in this case
because you are using

88:51 the actual versus desired.

88:53 

88:56 And you only care
when the situation is

89:00 that things are getting bigger.

89:03 So this is kind of
an important question

89:04 here-- whether you want to allow
for reductions in the capacity.

89:09 And in this model, I would want
to see reductions in capacity,

89:13 because you could
have a situation where

89:17 the steady state,
long-term replacement is

89:22 much lower than the growth phase
replacement plus new purchase.

89:29 And therefore, you want
to include a pathway

89:32 for reductions in capacity.

89:35 Whereas, if I'm correct,
this model right

89:39 now doesn't allow for
reductions in capacity.

89:42 AUDIENCE: Right.

89:43 HAZHIR RAHMANDAD: So
is the logic clear

89:46 how I made that conclusion?

89:48 So let me backtrack.

89:52 So the indicated total PC need
is current production capacity

89:58 multiplied by this expansion
factor coming from excess delay.

90:02 If excess delay
never goes below 1,

90:05 this indicates that total
production capacity never goes

90:08 below the current
production capacity

90:10 and therefore never can go down
in terms of the desired value.

90:15 So that's why I inferred
that, by this formulation,

90:18 you are making it impossible
for the production capacity

90:23 to go down.

90:24 And that's not what
you really want.

90:26 That takes away some
flexibility you do want to have.

90:31 OK.

90:31 So that's the capacity
management backlog.

90:35 Pretty straightforward-- sales.

90:37 And then you have the
delivery taken out.

90:41 And the delivery is dependent
on the capacity utilization.

90:45 You're using a very
similar formulation

90:49 as we had in the widgets model
with a little bit of more

90:55 complex formulation here.

90:59 AUDIENCE: It's a
fuzzy mean [INAUDIBLE]

91:01 HAZHIR RAHMANDAD: Yeah,
that's the fuzzy mean thing

91:03 that Hassan proposed
a few weeks ago.

91:07 Yeah.

91:09 Cool.

91:11 AUDIENCE: The only
downside of that

91:13 is-- and this is
what I was struggling

91:16 with that formulation.

91:18 Let's say, if the
desired production

91:21 rate is smaller
than the capacity,

91:25 the company can decide to
deliver faster than it's desired

91:32 delivery to gain reputation.

91:36 But that formula
doesn't allow that.

91:37 AUDIENCE: If it goes above that
45-degree line, [INAUDIBLE].

91:40 HAZHIR RAHMANDAD: Yeah.

91:41 So that formula by design wasn't
going above 45-degree line.

91:45 It is actually easy to have
alternatives that go above

91:48 45-degree line.

91:50 But ultimately,
what that will do

91:52 is that the actual
delivery delay will never

91:55 go below desired delivery
delay in this formulation.

92:00 And therefore, this
excess delay actually

92:04 would never go below 1, even if
you didn't put the max function.

92:09 And then that creates
this issue of not tracking

92:15 when the demand is falling.

92:18 It wouldn't be able to
bring down the capacity

92:22 even if you removed that
maximum that we talked about.

92:25 So you see this is kind of
a little bit, again, subtle.

92:28 But this goes back
to the conversation

92:30 we had about whether
using a pressure

92:32 to drive capacity-- so you
are here using a pressure.

92:35 The pressure is coming
from that delivery delay--

92:39 or using the recent
order rate as the driver

92:45 of desired capacity.

92:49 Now, I told you to use
pressure just so that we

92:52 can have these conversations.

92:53 But it is also showing
the failure modes

92:56 built into that pressure.

92:59 Now, the Forrester version
does bring it down as well.

93:01 So he doesn't use this function.

93:04 He uses a table function.

93:06 And that table function
allows for reducing

93:11 the current capacity, which
this one doesn't allow

93:15 for just by these formulations.

93:17 But I want you to
be sensitive to how

93:21 these assumptions
in each equation

93:23 has reverberations
down the road.

93:25 So think about those as you
walk through your formulations.

93:28 OK.

93:28 Good.

93:29 So we have the cells.

93:32 And now you have the
potential customers.

93:33 They become new customers.

93:37 And then you have the return.

93:39 And depreciation and
return is the same.

93:43 So that creates sales.

93:46 This also creates sales.

93:48 But here, again,
similar to Ann's model,

93:55 you are not accounting
for sales force

93:58 being needed for attracting
returning customers.

94:01 So that's an assumption that
might be a bit strong here.

94:06 Now let's look at the capturing
of new customers using

94:09 the current sales force.

94:11 So you have a number of pitches.

94:15 And that number of pitches
can come from productivity.

94:18 That productivity is normal
productivity and some max

94:21 productivity.

94:23 And max productivity depends on
the ratio of current customers

94:30 to the sales force.

94:32 So that's--

94:36 

94:42 AUDIENCE: Sales force times--

94:43 

94:47 HAZHIR RAHMANDAD: Time to pitch.

94:50 AUDIENCE: [INAUDIBLE]

94:51 HAZHIR RAHMANDAD: Yeah.

94:52 AUDIENCE: [INAUDIBLE]

94:54 HAZHIR RAHMANDAD: So it's
similar to that-- yeah.

94:56 So this is logical.

94:58 The constraint works,
creates the effect.

95:01 But it is not a flexible
effect because you

95:04 don't have free
parameters to account

95:07 for non-linear responses.

95:08 Yeah.

95:10 And then productivity
is the minimum

95:13 of these two guys, which
goes into number of pitches.

95:18 And then the conversion
rate, given the number

95:22 of customers you are
pitching, is determined

95:26 by this effect of excess delay.

95:30 So right now, you don't
have any delay perception

95:33 for the customers
here, unless there

95:36 is a delay built into this
equation, which shouldn't be.

95:39 Yeah.

95:39 So I would include
an explicit delay.

95:43 So right now, the excess
delay is coming directly

95:46 from the customer service side.

95:51 And that takes time to be
perceived in the marketplace.

95:55 So that perception delay
is important to have.

95:59 

96:01 Yeah.

96:02 And then the power
function here does fine.

96:06 So you have higher
excess delays.

96:09 You will get lower
conversion rates.

96:12 And that should be OK.

96:15 If you had lower excess
delays, which you can't here

96:18 because of two different
reasons we talked about,

96:21 then faster conversion
rates become feasible here.

96:27 But you have the maximum
function of these--

96:31 no, you are multiplying them.

96:33 So that's a little
bit of a question.

96:36 That is, if you have close to
0 delivery delay-- that is,

96:40 you remove those constraints
that make it hard to reduce

96:44 your delivery delay
below current levels,

96:49 if you have very fast delivery--

96:52 your conversion rate
can go to infinity.

96:55 It can go very high
in this formulation.

96:58 And that's just not realistic.

97:00 So in fact,
conversion rate should

97:02 be conversion probability.

97:05 So it is really a
matter of a probability.

97:08 You want it to also be
dimensionless, I think.

97:11 Yes, it is dimensionless.

97:13 So if you call it
probability, then it

97:16 should never go
above 1, which means

97:18 you need a more
nonlinear function here

97:22 to account for that.

97:25 But then it works fine.

97:26 

97:29 Good.

97:30 So then we have the sales force.

97:32 You have the desired sales
force, adjustment time

97:35 based on wages and budget.

97:37 Budget comes from revenue.

97:41 It's all good.

97:42 If you want to have a more
serious cost-benefit part,

97:47 you would account for the
cost of your operations.

97:51 That is, your production
capacity may have fixed costs.

97:56 You can think about these
sales to be just not product

98:00 price but product
profit so that this

98:04 accounts for the variable
cost of production.

98:07 But still, you would have
the fixed cost of production

98:09 and the cost of building
of the work in process--

98:13 

98:18 yes.

98:19 So where does that cost go?

98:21 Yes, this is here.

98:22 So you have it in
the profitability.

98:25 And you're getting it
out of the revenue.

98:27 That's OK.

98:27 That's OK.

98:30 Yeah.

98:30 And then-- yeah, [? Sally? ?]

98:34 AUDIENCE: So how do we decide
with these types of models

98:37 if the decision to
expand the capacity

98:40 should come from the delivery
delay or the production capacity

98:46 that we have for
the profitability?

98:48 

98:52 HAZHIR RAHMANDAD: So
typically, profitability

98:55 is a constraint on expansion.

98:58 So you have a desired level
of production capacity.

99:03 And you go through whatever
formulation you're going.

99:06 And then you can have
another constraint

99:09 that says, I don't have
enough money to build,

99:12 or, I can't convince
the banks to loan

99:17 me enough money because
I'm not very profitable.

99:20 So that would be the
way I would capture it.

99:22 That is, my total
production rate

99:25 could get affected by
availability of financing

99:29 based on a function of profits.

99:31 

99:34 AUDIENCE: Yeah.

99:35 HAZHIR RAHMANDAD: Thank you.

99:37 AUDIENCE: Could
you go over again

99:38 why you need that
additional value?

99:40 HAZHIR RAHMANDAD: Sure.

99:41 AUDIENCE: Because
I don't quite--

99:44 HAZHIR RAHMANDAD: So let me
give you an extreme condition.

99:46 So let's say initial
PC, I put it as 0.

99:50 OK?

99:52 Now, PC completion at the
beginning is a positive number.

99:58 And therefore, the initial
value of PC depreciation

100:00 is also a positive number.

100:02 OK?

100:02 Because this formulation is just
simply DELAY3 of PC completion.

100:10 And when it is DELAY3, it
starts from equilibrium,

100:12 which means it starts from the
initial value of PC depreciation

100:16 being equal to PC completion.

100:19 OK?

100:20 So now I have zero
production capacity,

100:23 but I have positive
capacity depreciation.

100:26 That's just not right.

100:28 AUDIENCE: Yeah.

100:29 So I see why this past
[INAUDIBLE] but I'm

100:32 a bit confused as to why
the value for the initial

100:36 is PC divided by
facility length.

100:39 Because even if you were to have
all of these stocks laid out,

100:45 that outflow at the end is that
figure divided by 3, right?

100:51 So that's-- yeah.

100:53 HAZHIR RAHMANDAD:
So let's for now

100:56 ignore the order of the thing.

100:58 So in a steady state,
the PC depreciation

101:05 would be PC, or initial PC,
divided by facility life.

101:09 Correct?

101:10 

101:13 That's Little's law.

101:14 So stock divided by
the time constant

101:18 is the flow in equilibrium.

101:22 And that's all we
are using here.

101:24 That is, the initial
value of the outflow

101:26 should be the
equilibrium value so

101:29 that then that's how Vensim
will operationalize it

101:34 inside its hidden three stocks,
or 10 stocks, or one stock

101:38 depending on what the
order you're using--

101:40 will be that total divided
by the order of the stocks.

101:44 You don't need to worry about
that order of the stocks.

101:47 Vensim will take care of that.

101:48 The sum of those
stocks will always

101:50 be what you get
in the initial PC

101:54 once you make the
initial outflow

101:58 to be what it needs to be here.

102:01 AUDIENCE: So Vensim
actually uses

102:02 that outflow to calculate the
value of all of those stocks?

102:05 HAZHIR RAHMANDAD: Yes,
that initial outflow

102:06 is what it uses to calculate
all of those stocks.

102:10 AUDIENCE: [INAUDIBLE]

102:11 HAZHIR RAHMANDAD:
Yeah, and it does that

102:12 by equally distributing
it across all

102:15 of the initial stocks.

102:17 OK.

102:17 So I think the basics
are all in place

102:23 with all of the minor caveats
that we talked about here.

102:29 Who likes us to
look at their model?

102:32 Let's kind of open
it up for volunteers.

102:35 

102:38 Sure.

102:39 AUDIENCE: It's not good.

102:40 HAZHIR RAHMANDAD: It's OK.

102:41 We are not--

102:41 AUDIENCE: [INAUDIBLE]
equilibrium.

102:43 There's a lot of
really bad areas, but--

102:46 HAZHIR RAHMANDAD: That
makes it more fun--

102:48 [LAUGHTER]

102:49 

102:50 --to critique.

102:51 

102:54 Not fun, more educational.

102:56 OK.

102:58 So you have the
facilities, factories.

103:01 You have first order delay.

103:02 We talked about that.

103:03 And then you have
the construction rate

103:06 based on the factory
adjustment, which is comparing

103:09 the authorized or desired.

103:11 And the desired is coming
from something we'll get to--

103:14 versus the current level
with an adjustment time.

103:18 And then you add the
factory construction rate

103:21 so that you don't
have the steady state

103:24 problem that we talked about.

103:25 That's all good.

103:27 Again, this is ignoring the
work in process inventory

103:31 of factories.

103:33 And the units for
factories are in--

103:36 AUDIENCE: Factories.

103:37 HAZHIR RAHMANDAD: --factories.

103:38 OK.

103:38 

103:43 So typically better to make
it in the units of production

103:47 capacity so that it
is easier to think

103:51 without worrying about the
parameter that converts them,

103:55 but it's all right.

103:56 AUDIENCE: Yeah.

103:57 [INAUDIBLE] obviously
discrete amounts.

104:02 So then I did integer
factory, which is wrong now

104:05 that I think about it more.

104:07 The idea was, I
was like, oh, well,

104:09 when I'm building capacity,
if I have 1.5 factories,

104:12 I only have 1 factory.

104:13 Then I wasn't
taking into account,

104:15 as the factories
depreciate, I still

104:17 have the [? local ?] factory
[INAUDIBLE] integer down to 0.

104:20 HAZHIR RAHMANDAD: Yeah.

104:21 So integers are
hard to deal with.

104:25 Don't get into the
integer stuff in Vensim.

104:28 I mean, Vensim is
not the right tool.

104:29 You can do it.

104:30 It's just kind of a headache.

104:32 So I wouldn't touch integer
constraints because then you

104:36 have to be really consistent.

104:38 Like, the inflow
needs to be integer.

104:40 The outflow needs to be integer.

104:41 And it's not worth it.

104:42 So don't worry about that.

104:44 But let's for now
put that aside.

104:48 So now the authorized
number of factories--

104:50 you're starting at equilibrium.

104:52 So the initial number is
the same for both of them.

104:55 That authorization is coming
from some pressure to expand

105:00 and some time to authorize.

105:03 OK.

105:04 I'm not following this yet.

105:07 AUDIENCE: So the
idea there was like,

105:10 here's some delivery delay.

105:12 They have the promised
delivery delay and then some--

105:18 the reference delivery delay--

105:19 I don't actually know
if it makes any sense,

105:21 but the idea of
the company itself

105:24 is OK with the
delivery delay actually

105:26 getting this much higher than
the promised delivery delay.

105:29 And so then there's going to
be like some magical pressure

105:36 variables to come out of that.

105:37 HAZHIR RAHMANDAD: But how do
you get the units for now?

105:40 So let's focus on that.

105:41 So the authorized number
of factories in factory--

105:44 so changing authorization is
factory per month or year, but--

105:49 per month.

105:49 And this one is
pressure to expand

105:53 capacity multiplied by
pressure to factory conversion.

106:00 AUDIENCE: The idea
was just that there's

106:03 some number that would
decide how many factories

106:06 they want to [INAUDIBLE] but
the actual pressure number

106:09 doesn't make any sense.

106:10 This isn't based
in any real idea.

106:14 My idea was just that, oh, some
delivery delay is happening.

106:18 And it's somewhere within or
without the reference of how OK

106:22 they are with the
delivery delay being,

106:24 and that that whether it would
be actually through a table

106:28 or through something
else would be converted

106:30 from that pressure into how many
factories they want to build.

106:32 And then from there,
you can actually--

106:34 HAZHIR RAHMANDAD: So the
thing that you are doing here

106:36 is a little bit tough.

106:38 Because you're trying to
start with the right number

106:42 of factories and then just
expand that, accumulate on that

106:46 or potentially even reduce--

106:47 I haven't looked
at the pressure,

106:49 whether it goes
negative or not--

106:51 without any response or
any feedback about how many

106:56 factories already you have.

106:59 Because there is nowhere here a
feedback from the current number

107:02 of factories.

107:03 So it is not anchored
in the current state.

107:06 It is only accumulating over the
starting point of the factories.

107:15 You see what I'm saying?

107:16 So--

107:18 AUDIENCE: Oh, when the factories
depreciate, [INAUDIBLE]

107:20 HAZHIR RAHMANDAD: It is not
taking that into account.

107:23 If the need for factories
goes down significantly--

107:27 it is basically kind of--

107:30 does it call it dead
something navigation?

107:35 That is, you start
from a point--

107:36 AUDIENCE: Dead reckoning.

107:37 HAZHIR RAHMANDAD:
Dead reckoning.

107:38 It's kind of dead reckoning.

107:39 You start from a point, which is
the current level of factories.

107:43 That's OK.

107:44 And then you just
accumulate into that

107:46 based on some pressure.

107:47 But you're never
getting feedback

107:49 whether this number is close
to some underlying desired

107:53 value that should be
driving it or how far you

107:58 are from the current factory.

108:00 None of that comes into play.

108:03 So--

108:03 AUDIENCE: But isn't the
desired amount this--

108:06 HAZHIR RAHMANDAD: So
the desired amount

108:07 is going to change the
number of factories.

108:09 So there will be connection
between the number

108:14 of factories that you have
and this authorized number.

108:17 So those two will remain
tied to each other.

108:20 But this authorized number
is not tied to anything.

108:23 It is only being accumulated
using some external pressure.

108:28 And therefore, it is
a little bit tough

108:32 to keep it well grounded.

108:35 That's the core
challenge you're facing.

108:38 Now, it may work just
fine in the sense

108:41 that, if the signal
from pressure to expand

108:44 can go both positive and
negative, if it overshoots,

108:48 it brings it down.

108:49 If it goes down,
it brings it up.

108:52 But typical formulations
will make this kind

108:56 of a fractional effect.

108:57 That is, OK, if I have
a number of factories,

109:01 I will multiply that by
this expansion factor

109:04 so that I can grow
fractionally, so that if I start

109:07 with one factory and
my rate of change

109:11 in this change in
authorization is

109:12 in the order of 0.5 factory
per year, 10 years from now,

109:17 now I have 100 factories.

109:19 It doesn't make sense to change
my factory by 0.5 per year.

109:23 I now want to actually be able
to change it by 50 per year

109:26 maybe.

109:28 That is not possible
in this formulation

109:31 because the scale of these
three things coming together

109:34 is always constant based on some
dimensionless thing from here.

109:39 OK.

109:40 AUDIENCE: [INAUDIBLE]

109:42 HAZHIR RAHMANDAD: Could
you speak up a little bit?

109:44 AUDIENCE: Sorry.

109:44 So isn't the pressure to
expand capacity exactly

109:46 the variable we're looking at?

109:48 Doesn't that depend on
delivery delay [INAUDIBLE]?

109:51 HAZHIR RAHMANDAD: Sure, sure.

109:52 All of that is correct.

109:54 And therefore, there
will be a feedback, but--

109:57 AUDIENCE: There will be
feedback [INAUDIBLE] right?

109:59 HAZHIR RAHMANDAD: It
is not proportional--

110:02 so the adjustment
is not proportional.

110:05 And therefore, the feedback
remains very linear-ish.

110:08 So if the scale of
operation is not changing,

110:10 this could work OK.

110:13 But it is blind to the
scale of operation.

110:15 So if you end up with a larger
scale because you are dealing

110:18 with, for example, an
exponential growth,

110:20 it just cannot
catch up with that.

110:23 That's the challenge, especially
with an exponentially growing

110:27 demand, which is the case here.

110:29 This becomes a very
tough bottleneck.

110:31 It just doesn't allow
the capacity to catch up.

110:34 And then you fall
behind and behind.

110:36 Now, you don't fall super behind
because your delivery delay now

110:39 goes up so much that you
can't grow exponentially.

110:42 That creates a kind of a linear
growth type of a dynamic.

110:46 That would be my guess, that
this kind of creates that.

110:48 We can simulate it.

110:50 AUDIENCE: [INAUDIBLE]
so what's the lesson?

110:54 The lesson is you want
comparable units when you're

110:56 doing this type of [INAUDIBLE]?

110:57 HAZHIR RAHMANDAD:
So the real lesson

110:59 is, if you are creating a
desired level for anything,

111:03 you want it to be anchored
to something current,

111:08 whether it is the
current capacity that you

111:10 want to anchor to or
current demand that you

111:12 want to anchor to.

111:13 But anchor that desire
to something current.

111:16 Otherwise, expecting
the dead process

111:20 to get that thing
to the right place

111:22 is too much to ask
from your models.

111:25 That's from your formulations.

111:28 Because the scope
of these adjustments

111:31 are not tuned for different
scales of operation.

111:35 You just multiply everything in
this model by a factor of 100.

111:40 The model will not scale because
this part of the formulation

111:43 for changing authorization--
nothing changes there.

111:45 It's still in the units of half
a unit or one unit per month

111:50 no matter what the
scale of operation is.

111:52 That's kind of the challenge.

111:56 OK.

111:56 Delivery delay--
fairly standard.

111:59 We have the max completion
versus the potential completion

112:02 coming from your factories.

112:04 Let's just skip the
integer stuff here.

112:07 Then you have the purchase rate.

112:09 And then you--
purchase to tasks.

112:13 AUDIENCE: Well, it's
just assuming that the--

112:15 per customer they're
buying [INAUDIBLE].

112:17 HAZHIR RAHMANDAD:
Yeah, that's OK.

112:18 You're just taking care
of the units somehow.

112:22 Then you have the sales
force and the customers.

112:25 So you have customers.

112:26 You have purchase rate.

112:27 You have depreciation.

112:29 This purchase rate is
coming from reputation.

112:32 So you are kind of doing
similar to a few others

112:34 that we saw, that there is
a process to get customers

112:37 into your orbit of customers.

112:41 And then once they are in, they
will continue to buy from you.

112:45 As soon as their
product life ends,

112:48 they go into this interested
customers with a delay.

112:51 They will purchase, but that
is bounded by your reputation.

112:56 So this should be OK.

112:59 

113:03 It's a little bit
tricky kind of how

113:05 the reputation is working here.

113:07 So if you have zero reputation,
yes, this shuts off.

113:13 AUDIENCE: [INAUDIBLE]
no interest.

113:14 HAZHIR RAHMANDAD: Yeah.

113:15 AUDIENCE: But the
formulation was incorrect.

113:17 But that was the idea.

113:19 HAZHIR RAHMANDAD: Yeah.

113:20 So the formulation-- the bigger
part that is missing here

113:23 is the interested
customers going into it.

113:26 So the purchase
rate should not be

113:31 independent of
interested customers.

113:33 This is interested customers
divided by time to purchase.

113:36 And it should be a
short time constant.

113:38 Then you can adjust around
that with the reputation.

113:42 OK.

113:43 And then gaining
interest-- there

113:44 is a max customers visited.

113:49 That's kind of the same idea
that we had in other models.

113:54 AUDIENCE: This is where I
got confused, one, because

113:58 of the revenue constraint.

114:00 But then, secondly, I think it
wasn't something I needed to do.

114:04 But it felt like there
shouldn't be more sales force

114:06 people than there are
[INAUDIBLE] customers.

114:08 HAZHIR RAHMANDAD:
So these things

114:10 depend on that conversion rate.

114:12 So you actually could have 10
different sales force people

114:15 working on a single customer.

114:17 If your single customer
is the US government

114:19 and you are, I
don't know, Boeing

114:21 trying to sell a single
missile to the government,

114:27 you may have a whole army
trying to sell that single unit.

114:30 So that is just a
productivity factor.

114:33 

114:36 OK.

114:36 So let's look at these
sales force formulations.

114:39 So attrition is fine.

114:42 You have hiring that comes from
the adjustment of sales force.

114:46 That adjustment is based
on the desired sales force.

114:49 So what's missing here?

114:50 AUDIENCE: The attrition.

114:51 HAZHIR RAHMANDAD:
So attrition needs

114:53 to be accounted for
for the hiring rate.

114:55 And then you would
have basically

114:57 attrition plus adjustment
max of 0 and that thing.

115:02 Otherwise, you have
a steady state error.

115:04 Once you have your
sales force, you

115:07 have max customers
visited based on the--

115:12 AUDIENCE: This is a little
bit confusing for me.

115:14 AUDIENCE: Yeah.

115:15 I just started getting negative
customers at one point.

115:19 And I was trying
to figure out why.

115:20 I thought that maybe it
was that I was somehow

115:23 visiting more customers.

115:25 HAZHIR RAHMANDAD: Yeah.

115:26 So basically, you
need the minimum.

115:28 This is fine.

115:29 But then the max
customers visited

115:32 and actual customers
visited-- the terminology

115:34 is a bit confusing.

115:36 So this is kind of
potential customers visited

115:39 based on your sales force size.

115:41 And this is the max
customers visited

115:43 based on the potential
interested customers.

115:46 And the equation
for max customers

115:47 visited should simply be
potential interested customers

115:50 divided by minimum
time to visit customers

115:52 or something like that.

115:53 So that's fairly standard.

115:55 Then you can use the--

115:57 and back to the same
point we had with Alban

116:01 and a couple other,
this doesn't give you

116:04 flexibility to have a
non-linear shift in how

116:10 effective your salespeople are.

116:15 OK.

116:16 Good.

116:16 I think the rest are
fairly straightforward.

116:20 And we have sales force wage and
total fraction of the revenue.

116:26 AUDIENCE: So it seems
basically everyone else

116:29 made the same kind of idea
in terms of the sales force,

116:33 that you have some budget coming
from the current money you're

116:35 making.

116:36 But then you would adjust your
sales force with the delay.

116:38 And I just felt kind of weird
about making that simplification

116:41 because it's possible that
suddenly revenue drops,

116:44 but your sales force
doesn't immediately

116:47 change because there's a delay.

116:48 And so there's a
little time period

116:50 in which you're paying
your sales force with money

116:52 you don't have.

116:53 And I guess you
could borrow, right?

116:56 But then that has other
financial implications

116:57 with interest rates
and blah, blah, blah.

116:59 So I don't know.

117:00 It's just the sort of
thing where [INAUDIBLE]

117:02 HAZHIR RAHMANDAD: That's fair.

117:03 So basically, the
assumption there

117:06 is that you're borrowing
to pay your sales force.

117:09 And if you're doing your
cost-benefit correctly,

117:12 that borrowing will show up in
negative cash flow and reduction

117:17 of your cumulative profit
or whatever you call that.

117:21 So it's not wrong.

117:22 It works fine.

117:24 If you want to capture
that more explicitly,

117:27 you would have a stock
of cash or something

117:30 that is accounting for
money in your bank account

117:32 that you can pay.

117:34 And if you don't
have money to pay,

117:36 you're not paying
your sales force.

117:38 That basically should
automatically get them out.

117:40 Or maybe if they are US
government, federal employees,

117:43 maybe they stick
around and try to work

117:45 without out or something.

117:46 So we had this
executive student who

117:51 was telling us this story
about payment system in Canada,

117:55 that they had the project.

117:57 And this was a project that
was to be, I don't know,

117:59 three years, $300 million.

118:01 And now they are--

118:02 for re-vitalizing
their payment system

118:06 for the Canadian
federal employees.

118:11 Everybody who gets
paid basically

118:13 goes through the system.

118:14 And then she said, now we are
10 years later and $3 billion

118:18 of cost, and this project
is not yet finished.

118:22 And not only that, it
has been operational.

118:25 So they have been
paying, but they

118:27 have been paying wrong salaries
and not paying some people.

118:29 And it's not like just
1,000 people were affected.

118:33 50-60% of people were getting
wrong salaries for months

118:37 and not getting salaries
for a few more months.

118:39 It's like-- anyway, it was
a really terrible story,

118:43 but a good anecdote for
project dynamics class.

118:47 So that was just a digression.

118:52 OK.

118:52 So I think this is-- yeah,
we covered much here.

118:57 Other volunteers?

118:58 Actually, one question--
yeah, let's do yours.

119:01 And then we can--

119:02 AUDIENCE: [INAUDIBLE]

119:04 HAZHIR RAHMANDAD: That's OK.

119:05 That's OK.

119:06 AUDIENCE: And I think based
on what you said so far,

119:08 I think [INAUDIBLE]
correctly, so.

119:12 HAZHIR RAHMANDAD:
That's all fine.

119:15 OK.

119:16 So let's take a look here.

119:20 So actually, let's go
with the factories.

119:24 So factory depreciating-- we
talked about it, not important.

119:27 First order draining here--
we talked about that.

119:31 Construction time, first
order-- that's fine.

119:33 But keep that in mind.

119:35 And then you have
target delivery delay

119:37 versus actual delivery delay
with capacity expansion rate--

119:41 so this formulation has the
problem that we just discussed

119:46 about [? Auriana's ?] model.

119:49 

119:53 OK.

119:54 So this is very kind of discrete
way of thinking about it.

120:01 So you're saying, if
you're above, let's expand.

120:04 If you're below, let's
just stop expanding.

120:06 So that's kind of too discrete
for our typical formulation.

120:12 So you want to look at maybe the
ratio of actual delivery delay

120:16 to target delivery delay and
use that as the pressure.

120:20 The second thing is that it
has the problem that it is not

120:23 anchored to any of the kind
of scale of your operations--

120:29 how many factories, what
capacity you currently have.

120:33 So that was kind of very similar
to [? Auriana's ?] challenge.

120:37 So these are the two
main issues here.

120:41 Then we have the delivery delay.

120:43 That is current.

120:45 That's standard.

120:47 Your production capacity
is impacting delivery.

120:51 But this is another
issue that you have.

120:54 The minimum of backlog
divided by target delivery--

120:56 OK.

120:57 So you have the
maximum delivery rate

121:04 taken care of within the
formulation, which is OK.

121:08 It's a little bit
kind of cleaner

121:11 to take out the
maximum delivery rate

121:14 as the ratio of backlog divided
by target delivery delay.

121:19 But that's OK.

121:21 

121:25 And the target
delivery delay here

121:28 being the driver makes things
a little bit more problematic.

121:34 So right now, this delivery rate
will never be below backlog--

121:43 well, not never--

121:44 will not be above backlog
divided by target delivery

121:48 rate, delivery delay.

121:50 And therefore, the
delivery delay, the actual,

121:55 will not go below target
delivery delay under any case.

122:01 Does that make sense?

122:03 AUDIENCE: [INAUDIBLE]

122:04 HAZHIR RAHMANDAD: So that
because you're using the target

122:08 delivery delay in the role of
what we typically call minimum

122:13 delivery delay, delivery rate
will always be small enough that

122:22 you cannot have a situation
where actual delivery delay goes

122:28 below target delivery delay.

122:31 OK?

122:32 And if it never goes below
target delivery delay,

122:36 this [? if and else ?] thingy--

122:39 so if actual delivery rate is
bigger than target delivery

122:44 delay--

122:46 so there are situations
where the two will be equal.

122:49 And therefore, this
thing will go 0.

122:53 But most of the time, this
capacity expansion rate

122:56 will be active.

122:57 So it's not exactly what
you want it to do, I think.

123:02 OK.

123:03 Then we have the
product lifetime.

123:05 People become potential.

123:06 Once they became
potential, they are now

123:10 pitched to pitching
capacity is from sales force

123:15 and limited by a
minimum pitch time--

123:20 so pitch time horizon.

123:24 Yeah.

123:24 So this is a very
similar formulation

123:26 as we had with other folks.

123:29 It works with
similar limitations.

123:32 But the assumption that you
have, which is different here,

123:35 is that once you have been sold,
the next time you come, again

123:39 it takes the same amount
of time to be sold to.

123:42 And that's also OK.

123:43 But we haven't yet seen
any formulation that

123:46 has kind of a balance
between the two

123:48 or allows different
productivities

123:50 for those different
two purposes.

123:52 And then you have the effect of
delivery delay on conversion.

123:56 Again, there is kind of the
delay here for perception

124:00 of the delivery delay.

124:01 That is important, I think.

124:04 Then attrition of
sales force is fine,

124:07 but you want to have replacement
of sales force in the hiring

124:11 process so that you
have desired sales force

124:17 minus sales force for the
adjustment of sales force

124:20 plus the attrition rate as
the total adjustment of the--

124:25 or hiring rate.

124:27 So one thing I kind of see
here in multiple places

124:30 is that you kind of
combine multiple things

124:32 inside the formulation.

124:36 So you have fraction of
revenue to sales force

124:38 multiplied by revenue divided
by cost per salesperson.

124:43 All of this is your
desired sales force.

124:47 OK?

124:48 So rather than this
being the flow,

124:50 it should be the
desired sales force.

124:53 And then you look at
the current sales force

124:55 compared to the desired sales
force divided by some time

124:58 to adjust--

124:59 close the gap for adjusting.

125:02 So this one wouldn't actually
do the job that you want.

125:05 In fact, it may have
even unit problems

125:08 unless you have changed
some of the units to be--

125:14 

125:18 AUDIENCE: [INAUDIBLE]

125:20 HAZHIR RAHMANDAD: Ah,
this should be dollar

125:21 per salesperson per month.

125:23 That's why you don't
get unit problem.

125:26 So cost per sales force is
not dollar per salesperson.

125:31 This is not a slavery.

125:32 You just are paying
the monthly fees.

125:37 So the units are
not balancing here.

125:43 All right.

125:46 What else?

125:47 

125:52 Good.

125:52 I think kind of you
get the basic ideas.

125:57 Question-- anybody has tried
to make the formulation

126:01 for fraction of budget going
to sales force dynamic,

126:06 depending on the size
of the operations

126:10 or kind of the effectiveness
of the sales force?

126:14 

126:16 OK.

126:17 

126:20 OK.

126:21 If nobody has done, that's OK.

126:24 So the idea there--

126:26 I mean, we don't have an example
to go through it in detail.

126:28 But the idea there is
that, right now, you

126:30 have a fraction of budget
that is going to sales force.

126:34 And that as a
heuristic may be fine.

126:37 But during different
stages of operation,

126:40 that fraction should change.

126:42 In practice, early on, you may
actually put a lot more emphasis

126:45 on the sales force.

126:46 Later on, as you have a lot of
customers who already know you

126:50 and therefore the cost for
converting them is lower,

126:53 or because you just have
captured all of the market

126:56 and it's only the replacement
rate that needs people,

126:59 you want to reduce that
budget for the sales force.

127:02 You don't need to keep that
big sales force, pay them.

127:05 And that is right
now not captured here

127:08 in any of the models.

127:10 So how would you think
about capturing that?

127:12 So what would be
high-level, conceptual way

127:18 of capturing that?

127:20 AUDIENCE: [INAUDIBLE]
base fraction of revenue

127:23 that is allocated to
the sales project.

127:25 So if the effectiveness of the
sales is at the maximum level,

127:29 meaning that each sales
person, for example,

127:32 can recruit or teach
10 people, there

127:35 would be no changes
in that base fraction.

127:37 But as soon as
the fraction drops

127:40 because the market
is getting saturated,

127:42 that sales budget can
also drop [INAUDIBLE]

127:46 HAZHIR RAHMANDAD: So
basically calculate

127:48 the net productivity
of sales force

127:52 and then use that net
productivity to adjust.

127:56 If that net productivity goes
down, bring down that fraction.

128:00 So that's a good first step.

128:01 Anybody wants to
improve upon that?

128:04 Alexander.

128:04 AUDIENCE: Just a
very minor thing,

128:06 but you could convert
the productivity

128:08 into the marginal revenue
of each salesperson, right?

128:11 So you just multiply
how many customers

128:14 each salesperson is getting
times the order quantity

128:18 and price.

128:19 Right?

128:19 And then that way
you can compare that

128:22 to the wage of the salesperson.

128:24 So that way, if it's
above 1, then salespeople

128:27 are net profitable.

128:28 You want to hire more of them.

128:30 If it's less than 1, then you
want to decrease [INAUDIBLE].

128:32 HAZHIR RAHMANDAD: OK.

128:33 Very good.

128:34 So that's kind of a very
clean, economically logical way

128:38 of doing it.

128:39 Basically, what is the marginal
profits from each salesperson

128:43 now?

128:44 For each sales
that they do, there

128:45 is a marginal profit
that is generated.

128:48 So is it worth having more
of these salespeople or not?

128:53 That's the question.

128:53 And in fact, if
you do it that way,

128:56 you can basically make the sales
force exposed to a pressure.

129:04 And that pressure
comes from this factor.

129:06 If it is above 1, you expand.

129:08 If it is below 1, you shrink.

129:10 And that 1 is the ratio
of the marginal profit

129:14 per salesperson divided by
the salary of the salesperson.

129:18 So that becomes a pretty
nice endogenous way

129:22 of managing the size
of the sales force

129:24 so that it is consistent
with your profitability

129:27 from those people.

129:28 AUDIENCE: And the sales
force productivity

129:30 would have to come
from some relationship

129:32 between the stock of potential
customers and your [INAUDIBLE]

129:36 HAZHIR RAHMANDAD: So the
sales force productivity--

129:38 you don't need to worry about
doing all of those calculations

129:41 separately.

129:42 You have a total sales
that is happening.

129:45 

129:48 And you have total
sales force you have.

129:53 So you can get the average sales
force productivity right away.

129:57 Now, that is average.

129:58 It is not marginal.

130:00 So this is actually
one level more complex,

130:04 if you want to think
about it this way.

130:06 So calculating the
average is very easy.

130:08 You already have all
of the information.

130:10 You just divide the total
sales to the total--

130:13 but this is not exactly
the marginal productivity.

130:17 Marginal productivity
is, for each extra sales

130:20 force, what will happen?

130:23 And doing that requires actually
a little bit more tracking.

130:28 And the way you do it,
it's not very standard.

130:30 We don't have the infrastructure
built into this structure

130:33 right now.

130:34 So you could do it analytically.

130:37 That is, basically, if you
have simpler formulations,

130:40 you can calculate the
marginal value analytically

130:47 as a separate path
that is saying, OK,

130:50 if my formulation for
sales force impact on sales

130:54 is like this, what is
the marginal productivity

131:01 of the sales force, which is
the derivative of profitability

131:05 with respect to sales force?

131:07 You can write that, and
calculate that, and track that.

131:10 So that would be
one way to do it.

131:12 For more complex models,
it's even harder.

131:16 But one way to do it is
to actually always use a--

131:20 so this is starting to
become more complex.

131:23 So you add a subscript to
track the value of sales

131:32 if you had one more person,
one more salesperson.

131:36 So you're calculating the
current sales force and what

131:40 is the impact on the sales.

131:42 There is one pathway.

131:43 And then you would
add a subscript

131:45 along this pathway for extras
or marginally more sales force

131:50 and calculate the sales under
that alternative formulation.

131:56 And then you look at
that delta and divide it

131:58 by 1, which is in this
case the total difference

132:03 between the two.

132:04 So I haven't seen
many people use it,

132:09 but that's how you would do
it if the formulations are

132:11 too hard to do analytical
tracking of the marginal.

132:16 Is the difference between
marginal and average clear?

132:19 Because that's the
first starting point.

132:21 So marginal productivity
of a salesperson

132:23 is, if I add one more
salesperson, how many dollars

132:26 would they make?

132:28 Average productivity is
saying, I have 100 salespeople

132:32 and I'm making $1 million,
so that's $10,000 per person

132:36 on average.

132:37 The question of, do
I add one more person

132:40 or do I reduce one
more person, should

132:41 be determined by the
marginal, not the average.

132:44 Average is not always but most
of the time overestimating

132:49 the benefit of the salespeople.

132:51 And therefore, expanding or
shrinking based on average

132:55 will give you the wrong answer.

132:56 That is, if you increase
your sales force

132:58 until you have the
average be 0, then

133:03 you already have a very
bloated sales force.

133:06 Many of those
people you shouldn't

133:08 have hired in the first place.

133:09 So that is why using the
marginal is important.

133:12 Good.

133:13 So I think that was kind
of a conversation that

133:15 wasn't obvious without
having it, but I think--

133:21 OK.

133:22 We could look at one more model.

133:25 Anybody wants their
model to be looked at?

133:27 AUDIENCE: I just have a question
about what we just said.

133:30 HAZHIR RAHMANDAD: Sure.

133:30 Go ahead, Jake.

133:32 AUDIENCE: So if we're
looking at a marginal profit

133:36 of another sales person, when
you get into actually making

133:41 that, would you also have to
consider the fact that if you

133:46 add too many too quickly,
[INAUDIBLE] might go down

133:49 because you reputation goes
down because you haven't built

133:51 that factory yet.

133:52 And you've introduced a delay.

133:53 Like, do you need to get
that granular with it?

133:56 Or are you thinking
long run [INAUDIBLE]

133:59 gets to equilibrium state
with a new salesperson?

134:02 HAZHIR RAHMANDAD: Yeah.

134:03 So in the first cut at
it, I would just do this.

134:08 That is, I would
say, OK, sales force

134:11 is creating pitching capacity.

134:13 So I'll make the
pitching capacity

134:15 in this model subscripted
with two versions.

134:18 One is with the
current sales force,

134:20 another with sales
force plus one person.

134:23 And then wherever it goes--
so it is changing the customer

134:26 conversion.

134:27 I'll have two versions
of customer conversion.

134:29 One of them is
operating on the stocks.

134:31 The other version I'm
just-- for keeping track

134:34 of how things are happening.

134:36 And then that customer
conversion somewhere

134:38 shows up in my profits.

134:40 

134:43 Yeah.

134:44 In the accounting
profits, I'm also

134:45 tracking that sales
force and so on.

134:48 So that version is fairly
short term-focused.

134:55 It is not really capturing
the longer-term consequences

134:59 of bringing this
new salesperson.

135:03 Doing those longer-term
consequences is much harder.

135:06 It is actually more precise.

135:08 That is a good calculation
of what the right balance is,

135:13 should account for
second and third order

135:15 effects that would require
adjustments of other stocks.

135:19 But then you basically
would be needing

135:22 to-- for every
time step, you need

135:25 to simulate the model with
that alternative formulation

135:31 or that alternative
number of sales force,

135:33 do a calculation
of the marginal,

135:36 then come back and decide how
many people you want to have.

135:41 So in a way, it is what
organizations are doing.

135:45 Organizations have
their simulation models

135:47 or their spreadsheet
models that try

135:51 to forecast what would be the
impact of each additional sales

135:55 force over the time and
therefore bring it back

135:58 into that decision
every period of time.

136:01 Now, they don't do it every time
step in the simulation sense.

136:04 They would do this
maybe periodically,

136:06 every quarter or something.

136:08 So conceptually, that is not too
far from what the organizations

136:13 also do, but doing it in these
models becomes exceedingly hard.

136:18 

136:21 So that would require a separate
simulation of some simpler

136:27 version of the model-- not
all of the model necessarily,

136:30 but some simpler version of
the model every time period

136:33 to inform just one of the
decisions in the model.

136:36 And that is
logistically hard to do.

136:39 In Vensim, you
basically need to define

136:42 some kind of external function
that goes and calculates

136:45 that, maybe calling
Vensim separately, doing

136:48 that simulation, then
coming back, and plugging

136:50 in that number into
the next time step.

136:52 And it's just a headache I'm not
going to worry too much about.

136:56 But sometimes it becomes
important and you need to do it.

137:00 So in those cases,
yes, think about it.

137:03 So Aria-- for her general
exam, one part of the question

137:09 was about the marginal
value of investing

137:14 in new shows for
streaming services.

137:17 And these investments
have long term impacts.

137:20 Because it is not just, next
period, how many I sell.

137:23 But it is over the life of this
show how many would I sell,

137:28 and how many it kind of reduces
the value for my other shows--

137:35 it cannibalizes my other shows--
and then how many new customers

137:39 it brings to me.

137:40 So it was a very
complex decision.

137:43 So coming up with
a marginal value

137:45 was a very non-trivial task.

137:48 And ultimately, it was
kind of, how can you

137:50 approximate that using
relatively simple,

137:53 manageable analytical
formulations?

137:57 Anyway, that's kind of a long
answer to a question that

138:02 is not easy, ultimately.

138:05 OK.

138:06 But now probably
it's a good time

138:08 to just review the
problem for next week,

138:13 given the limited time we have.

138:15 So next week, we are having
the endogenous diffusion model.

138:27 So this is kind of motivated
by Jack Homer's research

138:32 on pacemakers.

138:35 So this he did for his thesis.

138:39 So this is an old,
old piece of work.

138:41 But he continued
working on this space.

138:44 It's a very generic way of
thinking about diffusion.

138:47 So typically in
diffusion models,

138:48 we think about a single concrete
product and how it gets adopted.

138:53 But if you think about a
product that is evolving over

138:56 time-- it is getting better,
features and functionalities

138:59 are added to it.

139:00 So pacemakers are
a good example.

139:01 Because when they
were introduced--

139:03 I don't know, in the 1970s or
early '80s-- no, '70s, I think.

139:07 They were very big,
bulky, only useful

139:11 for the most critical patients
who would die without them

139:13 or something like that.

139:15 It was a very invasive surgery.

139:18 But over time, they became
more efficient, smaller.

139:21 Their signaling became
more sophisticated.

139:25 Their battery life extended.

139:27 All of those increased
the use cases

139:29 that pacemakers
could be used for so

139:31 that these days many people who
otherwise can survive very well

139:35 and have a decently
normal life would still

139:38 benefit from pacemaker.

139:39 Because on the margin, it
adds value for them as well.

139:43 So that is expanding
the size of the market.

139:46 Now there are
additional things that

139:49 come into play-- that you
add these new features

139:52 and functionalities.

139:53 You make the product
potentially more applicable

139:55 to a larger customer set, but
you're also introducing bugs.

140:00 You're introducing problems that
are not known at the beginning.

140:04 So discovery of those problems,
fixing of those problems,

140:07 and the reputational impact
that those problems have

140:10 on the product are also
important in the adoption.

140:14 So it can even create
oscillatory modes.

140:17 So he showed that,
for example, typically

140:19 in the case of pacemakers,
there is delays in research

140:23 that identifies and captures
those side effects and problems.

140:28 And that delay leads to
some oscillatory mode

140:32 in adoption of pacemakers--
that kind of they

140:35 come out with new versions.

140:37 They create lots of excitement.

140:41 But then early
research typically

140:43 kind shows some
disappointing results

140:46 that then needs to be
fixed, those problems.

140:49 And that brings down
adoption for a while.

140:52 And then it starts to recover.

140:55 So that's what your
task is to formulate,

141:01 a model of adoption that is
not your typical Bass diffusion

141:06 model.

141:07 In fact, the way
Jack formulated it--

141:09 and I suggested that you can
formulate it with that idea--

141:12 doesn't use the Bass
infrastructure at all.

141:17 It kind of says
there is a indicated

141:23 level of potential users.

141:26 And the actual users move
towards that indicated level.

141:29 But the speed by which they move
towards that indicated level,

141:32 the time constant
there, could be

141:34 a function of how many other
adopters are out there.

141:37 So this is a different way of
capturing the Bass diffusion

141:41 model's reinforcing loop.

141:42 So the Bass diffusion
model says people

141:45 who adopt it talk with
people who don't have it.

141:47 And that leads to adoption.

141:50 This alternative says there
is an indicated level of how

141:53 many ultimately would adopt.

141:55 There is a current level.

141:56 And you look at the gap.

141:57 You close that gap
over a time constant.

142:00 But that time constant
can become smaller

142:04 if you have a lot of
people who already

142:05 have adopted because then the
information spreads faster.

142:09 So that's a different
version of a Bass core idea

142:13 which accounts for
the advertisement

142:16 channel or the alternative
channels as well.

142:19 Because the time constant
is never infinite.

142:22 So there is a max time constant.

142:24 If nobody else's have it, there
is still a fractional rate

142:31 of movement towards this level.

142:33 So that's a kind of
an alternative way.

142:35 So think about it.

142:36 Use it just to see how it works.

142:38 

142:41 So you'll see the problem
definition in the folder.

142:47 It is a little bit
less well defined.

142:50 So you will need to make
more architectural choices.

142:53 I think this week,
the problem-- even

142:56 though it was a
broader model boundary

142:57 compared to the previous weeks,
it was fairly well defined.

143:01 So we see a lot of similarity
across different submissions.

143:06 And overall, you
folks had done well.

143:08 I think many of the submissions
were in the right space.

143:14 Now, we could improve and
change some of these things.

143:19 So this one might be a
little bit more challenging.

143:21 That's why I put
it a week later.

143:23 But it shouldn't be too hard.

143:27 OK.

143:28 So that's the plan
for next week.

143:31 Any questions on this exercise?

143:35 

143:41 AUDIENCE: So there is a bit
of word of mouth here, right?

143:44 HAZHIR RAHMANDAD: Yes, there
is a bit of word of mouth.

143:45 AUDIENCE: Both
positive and negative--

143:47 more doctors tell people
about the increased scope

143:49 but also the bugs as a result
of the newly [INAUDIBLE].

143:51 HAZHIR RAHMANDAD: Yeah.

143:52 So how you deal with that
is kind of a little bit

143:55 of an open question.

143:56 So I left it there at this
level, that bugs are there.

144:02 And they get
discovered and fixed.

144:04 But when they get discovered,
they reduce utility.

144:07 In fact, some of
the bugs, they don't

144:10 need to be discovered broadly
and perceived broadly.

144:13 Just the fact that it is there,
you as a user will feel it.

144:18 It does have an impact
on your utility.

144:20 But the people who have
not adopted it usually

144:22 need to hear about it.

144:23 So that discovery
process is important.

144:26 

144:28 OK.

144:30 So that's for the next week.

144:34 Do please also revisit
your proposals.

144:38 Let's kind of finalize those
so that next week everybody has

144:43 a version that is kind of
close to final that others--

144:48 when they go
through the exercise

144:49 we talked about
for the week of 18,

144:52 they can look at those
problem definitions.

144:57 Cool.

144:58 Any questions?

144:59 

145:02 OK.

145:03 So enjoy your weekend, folks.

145:06 Good to see those online.

145:09 And see you next week.

145:11 Yeah.

145:12 

