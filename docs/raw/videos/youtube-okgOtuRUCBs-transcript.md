---
title: YouTube Transcript: Video okgOtuRUCBs
created: 2026-10-01
updated: 2026-10-01
type: reading
source_url: https://www.youtube.com/watch?v=okgOtuRUCBs-transcript
source_type: video
ingested: 2026-10-01
published: recent
duration_minutes: 20
language: en
time_sensitive: True
---


# YouTube Transcript: Video okgOtuRUCBs

## Video Information
- **Title**: Video okgOtuRUCBs
- **Video ID**: okgOtuRUCBs
- **Published**: 2026-09-25
- **Views**: Unknown
- **Language**: en

## Transcript
00:00 [SQUEAKING]

00:01 [RUSTLING]

00:03 [CLICKING]

00:07 

00:09 SPEAKER: Thanks for
having me here today,

00:11 and also thanks for
accepting my request

00:17 for presenting on this topic.

00:20 So just for some context,
shamelessly reintroducing

00:24 myself, I work as a
research engineer at Hugging

00:28 Face I try to focus on different
facets of diffusion models

00:35 for image and video generation.

00:39 Part of my time
at Hugging Face is

00:40 focused on maintaining and
growing the diffusers library,

00:45 but this talk is not going to
be about the diffusers library,

00:48 and the rest of my
time at Hugging Face

00:50 is also spent around
researching diffusion models

00:54 from many different
perspectives.

00:56 And I'm going to be covering
some of that in this talk.

01:01 As this talk
suggests, it's going

01:03 to be about optimizing
the full stack for image

01:08 and video generation models.

01:10 In particular, we will
see how the optimization

01:15 aspects of these models are
a little nontrivial and also

01:19 kind of atypical in
nature, and also some

01:25 perspectives into how
the whole optimization

01:28 landscape can transcend
beyond latency and speed.

01:34 So with that, I'll start.

01:38 I'll try to also give you a
very hand-wavy introduction

01:43 to diffusion models
because diffusion model

01:47 itself will take another
lecture to cover.

01:50 So I'll try to give
you just enough context

01:52 so that we can step through
the rest of the discussion

01:56 for this talk, and hopefully,
by the end of this talk,

02:01 there will be time for some
Q&A. In case there isn't, you

02:05 can always reach
out to me via email,

02:07 and we can always
discuss things offline.

02:10 

02:12 I want to get the excitement
rolling by giving you

02:16 some outputs from some of the
recent text-to-image models,

02:22 but this is from PixArt-Alpha.

02:23 This is from back in
the days in 2024--

02:26 I think 2023, not even 2024.

02:29 So this is quite old, but you
can see the quality is not bad.

02:35 This is from DALL-E 3, OpenAI,
and this is from 2024 September

02:41 if I remember correctly.

02:42 This is from Flux.

02:44 And this example is by
far my most favorite

02:48 because even imagining a
tiny astronaut, let alone

02:52 trying to imagine it hatching
from an egg, is wild.

02:57 It's simply wild.

02:58 But somehow, these models
are expressive enough

03:01 to be able to come up with
something as real as this.

03:04 

03:07 There's an ongoing emergence
around text-to-video models

03:10 and the whole moniker
around world models as well.

03:15 This is one of those.

03:17 And then we have
got this cool cat.

03:21 And then you have got very
cinematic light landscape

03:25 frames.

03:26 All of these are open
models except for DALL-E 3

03:29 that I've shown in
the previous slide.

03:34 As a cautionary note, I'm going
to be interchangeably using

03:40 diffusion and flow in this
talk, which also means

03:43 that the points
and the discussions

03:46 that we'll do in this talk, they
will apply to both diffusion

03:52 and flow models.

03:54 Flow model-- I like
to explain them

03:58 is a generalization
of diffusion models.

04:03 But they are not
exactly the same.

04:05 But for the purposes
of this talk,

04:08 I'll interchangeably use them.

04:12 Now let me try to give
you some context as to how

04:15 diffusion models work.

04:17 I like to think of diffusion
models as the following.

04:20 What happens when we start
from a random noise drawn

04:25 from a Gaussian?

04:26 And we then try to slowly
denoise it over a period of time

04:32 unless we get
something realistic.

04:34 It can be an image.

04:35 It can be a video.

04:36 Or it can be even a
piece of audio as well.

04:40 But the crucial point
is we are starting

04:46 from a pure random
noise, and then we

04:48 are iterating over a period
of time, denoising it,

04:52 so that it becomes a clean and
realistic representation of what

04:56 we want, so it can be considered
as some of an iterative

05:01 denoising process.

05:03 And we can also condition
this denoising process.

05:06 When we try to condition
with text descriptions,

05:09 we can do tasks
like text-to-image

05:13 like we are seeing here.

05:14 

05:18 Now the thing is,
diffusion models

05:20 can have different variants,
like when we are operating

05:26 directly on the pixel
space, that family of model

05:32 is typically referred to as
pixel space diffusion model.

05:36 But pixel space
diffusion is pretty

05:38 intensive from both memory
and compute standpoints, which

05:43 is exactly why operating
on the latent space

05:47 is almost the de facto
for diffusion models.

05:51 And in this diagram, we
can get a sense of how

05:54 latent space diffusion works.

05:56 Now we need to have some
of an encoder and a decoder

06:01 in order to be able to encode
the pixel representation

06:05 of an image into its
latent representation.

06:08 And then when we are
converting that latent space

06:12 into the pixel space, we
need to have some decoder.

06:15 Or typically, for the case of
latent space diffusion models,

06:19 we usually use a VAE, which
has an encoder variant as well

06:25 as a decoder variant.

06:27 So yeah, just note that
this talk is mostly

06:32 going to be about latent
space diffusion models.

06:35 But the approaches are
fairly general enough.

06:38 They will also apply equally.

06:40 They should apply equally to
pixel space diffusion models

06:44 as well.

06:46 Now, let's try to also see
how different components

06:51 within a diffusion model are
connected with one another

06:56 because unlike language models
or visual language models,

06:59 diffusion, any modern state
of that diffusion model

07:03 is not a single model.

07:05 That's a very important
distinction to be aware of.

07:08 Now let's say we want to
take this text prompt,

07:13 and we want to generate
a video out of it.

07:15 Now let's see what are the
typical components that

07:19 are involved and how
they are connected.

07:23 Now, to be able to have
salient representations

07:26 of the textual
description, we need

07:28 to have text encoder,
which is fairly intuitive.

07:32 And then once we have
the text embeddings out,

07:35 we start the-- this is the
inference workflow, by the way.

07:40 Now, with the text
embeddings out,

07:42 we start off with a pure random
noise as I was mentioning.

07:48 These are our noisy latents as
we are operating on the latent

07:52 space, and we also
need to have access

07:55 to a component we
term as scheduler,

07:58 which is a nonparametric
component, which

08:00 takes care of--
which basically makes

08:03 the model aware of the position
it is in the entire denoising

08:08 trajectory.

08:10 And this is the beast that
we will try to optimize.

08:15 But more on that later.

08:17 It can be a typical
unit-like architecture

08:20 or a transformer-like
architecture.

08:23 And broadly, this is referred to
as the diffusion network, which

08:28 is conditioned on the time
step, like the position

08:31 in the denoising
iterations that it is in,

08:34 the text embeddings
in this case,

08:36 and also the noisy latents.

08:38 And then we invoke it over a
period of time, hence the loop.

08:43 Now, once we get our refined
legends out the diffusion

08:46 network, it's passed
off to a decoder,

08:50 and we finally get our frames.

08:52 In case of an image, it will
just be a single frame or just

08:55 the single final image.

08:58 Now, now that we have some
very basic understanding

09:03 of the different components
that are involved

09:06 in a standard text-to-image or
text-to-video diffusion model,

09:10 and how those components are
connected with one another,

09:13 how they draw the chronology in
the whole inference workflow.

09:17 I'll try to now
motivate why we might

09:21 have to optimize them to
be able to make anything

09:25 useful out of them.

09:28 Now let's try to
look at the memory

09:30 footprint of the individual
model-level components

09:33 in a fairly state of the art
and recent model called Flux.

09:38 It uses two text
encoders, which is also

09:42 kind of common in the literature
of text-to-image diffusion

09:45 models.

09:48 For Flux, it uses
two text encoders.

09:51 It has got a T5-XXL, and
it has got a clip large.

09:55 If you are interested in knowing
why we need different text

10:01 encoders and why that
might be beneficial,

10:03 we can talk about it later.

10:05 But in the interest of
time, I'll just keep going.

10:07 But that's an interesting
question to ask.

10:11 And then you have got
the transformer, which

10:13 is like the diffusion network.

10:15 And as we can see, it has
got the highest footprint.

10:18 And you have got
the decoder, which

10:21 will be responsible for
taking the defined latents out

10:24 of the transformer and
then decoding it back

10:26 to the pixel space.

10:28 

10:31 And as I was mentioning,
the transformer

10:33 or the diffusion network here is
the most compute intensive unit.

10:39 And it's compute bound,
unlike language models.

10:42 Hence, consequently, the
optimization literature

10:48 from the language
modeling world might not

10:51 carry over to the diffusion
world very gracefully.

10:57 Now, even when using
the brain float16, which

11:00 is very common in
the diffusion world,

11:03 it takes about 34 gigs
to generate a 1024

11:08 by 1024 resolution
image, which is standard,

11:11 and it takes about 7 seconds on
a fairly beefy GPU such as H100,

11:17 without any optimizations.

11:18 So I hope you we can see
how these numbers are

11:23 kind of staggeringly
high because if we have

11:27 to wait for about 7 seconds
to generate one single image,

11:31 it's not good.

11:34 And then videos can be
even worse, like a fight.

11:36 So just to give you some
perspective, a 5 second, 16 FPS,

11:42 720p video can take about 30
minutes to generate fairly

11:48 state-of-the-art open
video generation model.

11:53 Now these numbers are heavy.

11:55 These numbers should
concern us in case

11:59 we are interested in
operationalizing some

12:01 of these models because
long-running tasks

12:04 are bad for user-facing
applications.

12:07 It hinders interactions because
if the interactivity aspect

12:12 of creative applications
is hindered,

12:17 it's not good for your users,
and it's also power inefficient.

12:21 And it also slows
down the overall rate

12:25 at which you would want
to iterate and make

12:27 some improvements
to these models.

12:29 So it's kind of a bad experience
for both the developers

12:33 as well as the users
of these models.

12:37 Now, as I was hinting at
the iterative transformer.

12:43 It's at the root
of all evil here,

12:46 basically, because
it's both compute bound

12:49 and same time very memory hungry
now and a natural question

12:55 because the transformer
takes the most

12:58 amount of time in the
whole generation workflow.

13:01 A natural question
here to ask would be

13:04 do we just optimize for speed?

13:07 But what happens
when you also try

13:10 to motivate the
entire optimization

13:14 landscape with an
application, the application

13:17 in which this diffusion
network is going to get used?

13:21 If we consider things
from that perspective.

13:26 There will be other
factors that will influence

13:28 the whole process, like the use
case in which this network is

13:32 used, the level of
user interaction,

13:34 the rapidity of the
user interaction,

13:37 the kind of throughput
we will have to meet,

13:39 and also the deployment
hardware that's available to us.

13:43 

13:46 So I think I was
able to motivate

13:50 why you would want to work
with an optimized version

13:56 of the diffusion network, and
also why speed might not just

14:01 be the only factor that we want
to care about in this case.

14:07 Hence, I am going to talk
a little more about how

14:12 optimization becomes a
factor that transcends well

14:16 beyond just speed.

14:17 

14:20 Effectively and
essentially, I like

14:22 to think of the
whole optimization

14:25 landscape as a few guiding
principles, when should,

14:31 when should the
optimization take place?

14:34 And in this case, the motivation
basically comes from the app

14:38 where should we
perform optimization.

14:42 And in this case,
it's roughly going

14:43 to be the diffusion network,
the transformer model.

14:47 That's the most
compute-intensive element

14:50 in our workflow.

14:51 And do we know what
we want to optimize?

14:54 Do we want to
optimize throughput?

14:56 Do we want to optimize memory?

14:58 Or do we want to optimize both?

15:02 And how should we optimize?

15:03 This is where this talk is
going to be focusing on.

15:08 So yeah, if we are
going to be discussing

15:10 a couple of different
recipes and approaches

15:13 as to how we can optimize
the transformer network

15:17 and also how we
can go beyond that.

15:22 Now I think there needs to
be more motivation and more

15:28 awareness to be put when it
comes to the kind of hardware

15:33 that we have access to
especially when we are deploying

15:37 these models.

15:38 Now in this picture, we can see
how the throughput immediately

15:43 improves when we try to use
shapes that are particularly

15:48 optimized for a given hardware.

15:50 Now, on the extreme
right-hand side,

15:52 the bar shows, it's
basically configured

15:58 with the most optimized
shapes for a given hardware,

16:01 and it gives us the most
amount of throughput.

16:04 And the number of total model
parameters is not changing.

16:08 That's not changing.

16:09 We are just using the shapes
within the model, maybe,

16:13 the number of attention heads
or maybe the hidden dimension

16:20 of the transformer
blocks and so on.

16:22 And it shows how
just changing that

16:24 and how optimizing that with
respect to the given hardware

16:28 can immediately render
some positive gains

16:32 in terms of throughput.

16:34 So that's what I was mentioning.

16:38 Nontrivial gains can
come from kernels

16:41 that are hyper specialized
for a given hardware,

16:44 and also model architectures
where the shapes of the model

16:49 are kind of optimized and have
been made efficient with respect

16:55 to the hardware.

16:56 It's going to be
operationalized.

17:00 Now there's also this
aspect of efficiency

17:05 that's going to keep
coming up because we

17:07 want to make our model
as efficient as possible.

17:11 But efficiency is also often a
term that has so many misnomers.

17:16 The popular belief is smaller
models are almost always faster

17:20 and more efficient.

17:21 The reality is no, not always.

17:24 And I have this very popular
figure from this paper called

17:29 "the efficiency misnomer" as
the title of my slide goes.

17:33 It basically shows how models
with higher number of parameters

17:38 may not have the
highest number of flops,

17:42 and also it may not
have a lower throughput.

17:48 Now, in this case, it's
basically reversed.

17:51 That is, the models with a
lower number of parameters

17:55 has more flops and
has a lower amount

17:58 of throughput than their
apparently heavier counterparts.

18:04 So that kind of drives
this point home.

18:07 That efficiency may not
always be related to models

18:11 being smaller.

18:13 There are more angles
to take a look at it.

18:16 

18:19 Now the big elephant
is also transformer.

18:22 I'm going to keep coming back
to this transformer thing.

18:26 But also, when it comes to high
resolution generation of images

18:31 and videos, the effects of
the compute-bounded regime

18:39 of our transformer can become
really, really evident.

18:43 First, the inputs are
of high dimensional.

18:46 For example, for 4K
image generation,

18:51 even if we were to operate with
a compression factor of 8x,

18:55 we have got this huge
dimensionality problem.

18:58 We have got batch size.

18:59 Then we have nominating
channels, which

19:02 can be 64, 128, and so on.

19:05 And then you have got your
latent width and latent--

19:09 you have got your latent
height and latent width,

19:11 which is also like 512 and 512.

19:14 Now doing attention at this
high-dimensional space can

19:19 immediately restrict--

19:21 can immediately impose memory
implications as well as

19:27 speed implications.

19:28 Two very popular ways to deal
with this high-dimensionality

19:32 problem, in order to achieve
some efficiency gains,

19:36 is we increase the compression
factor, like from 8x,

19:41 we compress even higher,
maybe 16x or 24x,

19:45 and we try to recover the lost
information through other means.

19:52 There are several works
that have explored this,

19:55 but I just wanted to give
you a high-level overview

19:58 of the typical
things that are done

20:00 when we have this problem of
high-dimensional representation

20:04 spaces.

20:05 Now when we-- just to elaborate
a bit further on this point,

20:11 when we try to compress
higher and higher,

20:14 we also end up losing a lot of
information redundancy, which

20:18 might be actually
necessary study in order

20:21 to model the expressivity
into the overall workflow.

20:25 And if we do miss out on that,
our quality can take a huge hit.

20:31 Now, that's also why
it's essential to try

20:35 to recover the
information loss incurred

20:38 during this heavy compression,
so some kinds of other means.

20:44 And as a motivating
example, I want

20:46 to show you this picture
from this very popular

20:52 high resolution image
synthesis model called SANA,

20:55 which also happens to operate
on a highly compressed latent

20:59 space.

21:00 And as we can see, using
extreme compression

21:05 can have significant
gains on the speed.

21:11 So in this case, we can see a
25x reduction in the generation

21:15 latency when operating
with 4K images.

21:19 

21:24 Now, the good thing
about trying to do

21:31 this more from a first
principles approach

21:34 is these approaches
should be complemented

21:38 with the kinds of
techniques that we

21:39 have for latency
optimization, for example,

21:42 maybe an optimized
kernel or maybe

21:45 using things like
FlashAttention.

21:47 

21:50 So at this point
in time, I would

21:52 expect us to have a good
understanding of how

21:58 we can optimize the
model architecture

22:00 and also have a
model architecture

22:05 that respects the hardware
that it will get deployed to.

22:10 Now, ultimately,
since we are also

22:12 focusing on the applications
in which these models are going

22:17 to be used, I think
it also makes sense

22:20 to try to think about
how we can also optimize

22:23 a little bit for the use case.

22:25 So let's see how.

22:28 So we know that my
model is topping

22:33 all the standard
generation benchmarks.

22:35 That's all well and good.

22:38 But the use cases
in which the model

22:40 is going to get deployed
to, they might be different.

22:44 For example, maybe
the model would

22:46 be needed for photorealism.

22:48 So in that case, the users would
demand for specific attributes

22:53 to be better than others.

22:55 And then maybe the model
will be used in the context

22:59 of interactive generation.

23:00 In those cases, we would rather
have real-time interaction

23:05 and lowest possible latency.

23:07 And maybe quality
doesn't matter that much.

23:11 So in these cases, we will
have to finetune whatever model

23:17 that we have for specific needs.

23:19 And that entire process should
be driven by the use cases.

23:25 Now one such way to do
that, one such way to inject

23:30 some form of use
case awareness would

23:32 be to do preference alignment,
where the model is finetuned

23:35 to output what's preferred.

23:38 In this case, you have got
a text prompt, a cyberpunk

23:41 cat with a neon
sign that says Sana,

23:44 and you have got two
images, two candidates.

23:48 Now, the model will be
trained on this triplet,

23:51 and it will be basically
trained to output what

23:55 the users typically prefer.

23:57 

23:59 We might also want to extend the
way users prompt these models.

24:06 So far, we have been seeing
text-to-image models, which

24:10 is basically users provide
natural text description of what

24:16 they want to see in
the final outputs.

24:18 Maybe that's not sufficient.

24:19 Maybe I also want
the output image

24:23 to follow a particular pose.

24:26 Maybe I want to condition the
model with more structural forms

24:30 of inputs such as pose,
segmentation, map,

24:33 Canny map for example.

24:35 And in this case, I'm
basically prompting the model

24:38 with a certain pose as well
as a textual description.

24:43 And as you can see,
it works, basically.

24:46 So maybe the textual
prompt was not enough.

24:49 And hence there
was a need to allow

24:52 the users to have more
control over what they can

24:55 provide to the model as inputs.

25:00 If training is not
possible because training

25:02 is an expensive gig, even with
parameter efficient finetuning,

25:05 the results might be
far from expected.

25:09 In those cases, we can
also incorporate things

25:11 like inference time
scaling, where we might want

25:16 to search for better noise.

25:18 As we saw a couple slides
back, when performing inference

25:23 with diffusion models, we try
to start from a random noise,

25:27 and then we try to denoise it.

25:29 We could search
for better noise,

25:31 like the initial noise
could be better because not

25:35 all noises are equal.

25:37 They are not going to lead
to same quality outputs.

25:42 So we might want to
search for better noise,

25:46 or maybe we want to search
for a better prompt.

25:49 And it's also possible to
search for both, actually.

25:54 Now this gives us a depiction
of what I wanted to convey.

26:00 So you basically generate an
image from a language prompt.

26:05 And then you
compute some metric.

26:08 In this case, it's
the ClipScore.

26:11 And then if the metric
is OK, then all good.

26:16 Our job is done.

26:18 If the metric is
not OK, maybe we

26:20 ask some language model to
come up with a better prompt.

26:24 And then we enter into this
interactive scaling framework.

26:34 Now Clip Score here I used clip
score as a motivating example.

26:39 But this metric should
be use case-specific.

26:44 So this is the last
section of my talk, where

26:47 I want to give you
a flavor of some

26:49 of the more advanced
optimization techniques

26:52 that we can incorporate.

26:55 So knowledge distillation
is already very popular.

26:58 We have had many
papers in the community

27:01 that talk about this technique.

27:04 So the basic idea
is we have a larger

27:08 model that is probably memory
intensive and also slower and so

27:15 on.

27:15 And we want to distill that
large model into a smaller

27:19 one, which is
often known as some

27:22 of a compressed representation
of that larger model.

27:27 And in the case of
diffusion models,

27:29 we have got large
number of iterations.

27:32 And we can typically
reduce the number

27:34 of steps or iterations needed to
generate something reasonable.

27:39 And in the literature
of diffusion models,

27:42 it's known as time
step distillation.

27:45 And also, one advantage of
working with diffusion models

27:50 is that we can combine
architectural compression

27:54 with time step
distillation and come

27:58 to be able to benefit from
the best of both worlds.

28:05 So at a glance, if
I were to give you

28:09 an overview of the things
that I find to be beneficial

28:14 when trying to approach
the optimization

28:17 landscape for diffusion
or flow models is

28:21 we should incorporate
hardware awareness

28:24 when designing the
model architecture

28:26 and also shapes
that are optimized

28:30 for a given hardware for
potentially better efficiency.

28:35 And it also can be very
beneficial to make the model

28:38 architecture flexible,
to be able to extrapolate

28:42 to use cases like high
resolution image and video

28:44 synthesis.

28:47 And we can complement
the benefits

28:51 that come from
model architectures

28:54 with latency optimization
techniques such as better

28:59 kernels, FlashAttention,
and those techniques.

29:04 And if the use cases demand
for it, we should post train.

29:08 And if latency
requirements, demand for it,

29:12 we might want to
just distill as well.

29:16 So I think that's about it.

29:19 That went quicker
than I was expecting.

29:23 And most of the
content of this talk

29:26 I have written in
this blog post.

29:29 So yeah, that's
about it from my end.

29:33 So if there's any questions,
I'm happy to take them.

29:37 So yeah.

29:38 HOST: Awesome,
thank you so much.

29:40 

