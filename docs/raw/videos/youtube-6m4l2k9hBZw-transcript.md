---
source_url: https://www.youtube.com/watch?v=6m4l2k9hBZw
source_type: video
ingested: 2026-10-02
published: 2026-10-02
duration_minutes: 3
language: en
sha256: 50b962971f66c5d1f4bc558636928e0c28923b1cc3e3dd876150de5b4d951f71
time_sensitive: False
---

# YouTube Transcript: 8.2.4 An Introduction to Linear Optimization - Video 3: The Problem Formulation

## Video Information
- **Title**: 8.2.4 An Introduction to Linear Optimization - Video 3: The Problem Formulation
- **Video ID**: 6m4l2k9hBZw
- **Published**: Unknown
- **Views**: Unknown
- **Language**: en

## Transcript
00:04 

00:04 For a single route
example, our problem

00:07 is to find the optimal
number of discount seats

00:10 and regular seats to
sell to maximize revenue.

00:14 We'll assume that the price
of regular seats is $617,

00:19 and the price of
discount seats is $238.

00:23 Also, let's assume
that we forecasted

00:25 the demand of regular
seats to be 100,

00:29 and the demand of
discount seats to be 150.

00:32 The capacity of our
airplane is 166 seats.

00:37 Let's go ahead and formulate
this mathematically

00:40 as a linear
optimization problem.

00:44 The first step is to decide
what our decisions are,

00:47 or the variables in our model.

00:49 We need to decide how many
regular seats we went to sell.

00:53 We'll call the number
of regular seats

00:55 we sell R. We also need to
decide the number of discount

00:59 seats we want to sell.

01:01 We'll call the number of
discount seats we sell D.

01:07 The second step
is to decide what

01:09 our objective, or our goal, is.

01:12 In this case, it's to
maximize the total revenue

01:15 to the airline.

01:17 The revenue from
each type of seat

01:19 is equal to the number
of that type of seat

01:21 sold times the seat price.

01:25 In the case of
regular seats, this

01:27 is $617 times R, the number
of regular seats we sell.

01:34 And for discount seats,
this is $230 times D,

01:39 the number of discount
seats we sell.

01:42 We sum these together to
get the total revenue,

01:45 and our objective is
to maximize this sum.

01:51 The third step is to define
the constraints, or limits,

01:54 of our decisions.

01:56 One constraint is that American
Airlines can't sell more seats

02:00 than the aircraft capacity,
which is 166 seats.

02:04 So the total number of seats
sold, R + D has to be less than

02:10 or equal to the capacity of 166.

02:14 Additionally, American Airlines
shouldn't sell more seats

02:17 than the demand for
each type of seat.

02:20 So the regular seats,
R, shouldn't exceed 100.

02:25 So R should be less
than or equal to 100.

02:28 And the discount seats,
D, can't exceed 150.

02:32 So D should be less
than or equal to 150.

02:37 The final step is to make
sure our variables are

02:40 taking reasonable values.

02:42 In this case, it
wouldn't make sense

02:44 to sell a negative
number of seats,

02:46 so we need to make sure
that both R and D are

02:50 greater than or equal to 0.

02:55 So our entire problem is to
maximize total airline revenue,

02:59 subject to the constraints
that seats sold can't exceed

03:02 capacity, seats sold
can't exceed demand,

03:06 and the seats sold
can't be negative.

03:09 Mathematically, this can be
written as maximize 617*R +

03:15 238*D, the total revenue,
subject to the constraints:

03:20 R + D is less than or equal to
166, the capacity constraint;

03:25 R less than or equal to 100,
and D less than or equal to 150,

03:29 which are the
demand constraints;

03:31 and R and D are both
greater than or equal to 0.

03:35 This is called a linear
optimization problem.

03:38 In the next video, we'll see
how to solve this problem using

03:42 the software, LibreOffice.

