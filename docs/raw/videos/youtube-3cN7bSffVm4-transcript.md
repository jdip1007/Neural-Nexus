---
title: YouTube Transcript: 4.2.5 An Introduction to Trees - Video 3: Splitting and Predictions
created: 2026-10-01
updated: 2026-10-01
type: reading
source_url: https://www.youtube.com/watch?v=3cN7bSffVm4-transcript
source_type: video
ingested: 2026-10-01
published: recent
duration_minutes: 20
language: en
time_sensitive: True
---


# YouTube Transcript: 4.2.5 An Introduction to Trees - Video 3: Splitting and Predictions

## Video Information
- **Title**: 4.2.5 An Introduction to Trees - Video 3: Splitting and Predictions
- **Video ID**: 3cN7bSffVm4
- **Published**: Unknown
- **Views**: Unknown
- **Language**: en

## Transcript
00:04 

00:04 In the previous
video, we generated

00:06 a CART tree with
three splits, but why

00:10 not two, or four, or even five?

00:13 There are different
ways to control

00:15 how many splits are generated.

00:18 One way is by setting a lower
bound for the number of data

00:21 points in each subset.

00:23 In R, this is called
the minbucket parameter,

00:27 for the minimum
number of observations

00:29 in each bucket or subset.

00:32 The smaller minbucket is, the
more splits will be generated.

00:36 But if it's too small,
overfitting will occur.

00:40 This means that CART
will fit the training set

00:43 almost perfectly.

00:45 But this is bad because then
the model will probably not

00:48 perform well on test
set data or new data.

00:52 On the other hand, if
the minbucket parameter

00:54 is too large, the model
will be too simple

00:57 and the accuracy will be poor.

01:00 Later in the lecture, we will
learn about a nice method

01:03 for selecting the
stopping parameter.

01:08 In each subset of
a CART tree, we

01:10 have a bucket of
observations, which

01:12 may contain both
possible outcomes.

01:15 In the small example we
showed in the previous video,

01:19 we have classified each
subset as either red or gray

01:22 depending on the
majority in that subset.

01:25 In the Supreme Court case, we'll
be classifying observations

01:29 as either affirm or reverse.

01:32 Instead of just taking
the majority outcome

01:34 to be the prediction, we
can compute the percentage

01:38 of data in a subset of
each type of outcome.

01:42 As an example, if
we have a subset

01:44 with 10 affirms and two
reverses, then 87% of the data

01:50 is affirm.

01:52 Then, just like in
logistic regression,

01:55 we can use a threshold value
to obtain our prediction.

01:59 For this example, we
would predict affirm

02:02 with a threshold of 0.5
since the majority is affirm.

02:07 But if we increase
that threshold to 0.9,

02:10 we would predict reverse
for this example.

02:15 Then by varying the
threshold value,

02:18 we can compute an
ROC curve and compute

02:21 an AUC value to
evaluate our model.

02:25 In the next video, we'll
build a CART tree in R

02:28 to predict the decisions
of Justice Stevens

02:31 and evaluate our model
using a ROC curve.

