---
source_url: https://www.youtube.com/watch?v=ZEsk64C0fJg
source_type: video
ingested: 2026-08-23
published: 2026-08-23
duration_minutes: 8
language: en
sha256: 3f7e33d8f646f9932da097d395a2294b67f600dcb9d307f9f3bdc5239a7b6003
time_sensitive: False
---

# YouTube Transcript: 2.10.1 Árboles: Vídeo

## Video Information
- **Title**: 2.10.1 Árboles: Vídeo
- **Video ID**: ZEsk64C0fJg
- **Published**: Unknown
- **Views**: Unknown
- **Language**: en

## Transcript
00:00 

00:02 PROFESSOR: Trees are about
the most basic data structure

00:05 that you're ever
going to come across.

00:07 They pervade computer
science and other subjects.

00:09 So let's talk about them.

00:11 And the simplest
definition of a tree

00:13 is that a tree is a connected
graph with no cycles.

00:16 In this setting we're talking
about simple graphs, and trees

00:20 with undirected edges.

00:22 Well, in order to
make sense of that,

00:24 we better have a
definition of a cycle.

00:26 There's a picture
of a typical tree,

00:28 but to be precise, what's
a cycle in a simple graph?

00:32 Well, it's a closed walk
of length greater than 2

00:35 that doesn't cross itself.

00:37 So the not crossing itself
is the standard definition

00:40 of a cycle that we were
using in a directed graph.

00:43 It simply means that it's a
path, except that the beginning

00:47 and end vertex are the same.

00:48 So it looks like you
start someplace at v,

00:52 and then you go
around to a and to w,

00:54 and it's all distinct vertices
as you go around in this path.

00:58 Except that the
path ends where it

01:00 starts at v, which is what
keeps it from being a path

01:02 and makes it a cycle.

01:04 Now, the length
greater than 2 is

01:05 what is the difference between
the definition of cycle

01:08 [? between ?] simple
graphs and directed graphs.

01:12 And in a directed graph,
it's perfectly possible

01:14 to have a self-loop
of length, 1,

01:17 that is an interesting and
important kind of cycle

01:19 to have.

01:19 But we forbid them
in simple graphs,

01:22 because there's no way to avoid
having a cycle of length 2,

01:26 because you always
have the ability

01:28 to go back and forth across an
edge-- that's not interesting.

01:31 And so we don't consider
that to be a cycle.

01:34 A cycle, then, has to be
of length greater than 2.

01:37 It also rules out the
cycle of length 0,

01:40 which you get by taking
a vertex all by itself.

01:43 OK, with that
technical definition,

01:45 we now know what a cycle
is in the simple graph,

01:47 and we understand the
definition of tree.

01:50 Here are some more
pictures of trees--

01:52 simple graphs with no cycles.

01:55 Now, they really
come up all the time.

01:58 And why is that?

01:58 Well, there are
family trees, which

02:00 you may be familiar
with-- where you're

02:02 drawing a picture of the
descendants of a given person,

02:06 and they keep branching
out in a tree structure,

02:09 as traditionally displayed.

02:13 There are search trees,
which come up all the time

02:15 in computer science, where
you branch on the answer

02:18 to some question, which tells
you which way to search next.

02:21 There are game trees,
which we've already

02:22 discussed in this
class, which are used

02:24 to define games and strategies.

02:26 There are parse trees, that
come up in compiler technology,

02:31 and in language theory.

02:33 And there are spanning
trees, which we're going

02:35 to be talking about some today.

02:38 Now, in addition to these
places where trees come up,

02:42 there are a lot of
different kinds of trees.

02:44 There's rooted trees, where
there's some designated

02:46 vertex called the
root, and you think

02:48 of getting to all the other
vertices from the root.

02:54 There are ordered trees, where
when you're at a given vertex,

02:57 there's a distinct
order in which the exit

03:04 edges from a vertex-- there's
a first one, and a second one,

03:07 and a third one, or a left one,
and a next, left, most, and so

03:10 on, so that there is
an order in which you

03:12 can choose to leave the vertex.

03:15 There are a binary
trees, in which

03:17 each vertex has two ways
out exactly-- or no ways out

03:22 if it's a so-called leaf.

03:24 And then there are a complete
trees, whose definition

03:28 is not important to
us, because we're not

03:30 going to consider any of these.

03:31 There's also, by the way,
directed trees in which edges

03:35 have a direction, as in
a [? di-graph ?] tree.

03:38 But we're not
considering any of these.

03:40 We're going to focus on
so-called pure trees, which

03:43 are unordered,
unrooted, undirected,

03:46 and that's what
we're talking about.

03:48 So let's examine
some more properties

03:50 of trees and equivalent
definitions of trees.

03:52 It will be important
for theoretical reasons

03:55 and convenience to know lots
of different characterizations

03:58 of trees.

03:58 So we're starting off with
a definition which says,

04:01 it's a connected simple
graph with no cycles,

04:05 but there's other ways
to characterize it.

04:08 So an edge in a simple
graph is called a cut edge,

04:11 if, when you remove
it from the graph,

04:15 two vertices that
used to be connected--

04:17 that is used to have
a path between them--

04:19 cease to have a
path between them.

04:21 So here's a simple
graph illustration.

04:24 And that edge, e, is a cut edge,
because if I delete it, then

04:29 there are now two components.

04:31 There used to be two
vertices-- actually any

04:34 of the vertices here
used to be connected

04:36 to any of the vertices
there via that edge.

04:38 But once I've deleted
that edge, all of those

04:41 vertices here and there that
used to be connected no longer

04:44 are.

04:44 So that makes e a cut edge.

04:47 f is not a cut edge.

04:48 Because even if
I delete f, there

04:51 is, in fact, still a
path from every vertex

04:54 to every other vertex
here, so that f is not

04:56 disconnecting anything.

04:57 

05:00 And as I say, it's still
connected after you delete it.

05:03 So now we get a simple
way to characterize trees

05:06 in terms of cut edges-- because
an edge is not a cut edge if

05:11 and only if it's on a cycle.

05:12 If you think about that,
if it's on a cycle,

05:15 and you cut an edge
out of a cycle,

05:18 then everything on
the cycle is still

05:19 connected by going the other
way around the cycle that

05:22 doesn't use that edge.

05:24 And if it's not on a
cycle, then, in fact,

05:27 you can think through
that deleting it

05:29 means that there's not going
to be two paths between two

05:35 things at its endpoints.

05:37 And so it will separate them.

05:41 OK, so another way,
then, to define

05:44 a tree is to say a tree
is a connected graph where

05:47 every edge is a
cut edge-- that is

05:50 as soon as you cut
any edge out of a tree

05:52 it stops being connected.

05:55 That yields another way
to say that something

05:58 is a tree-- a tree is a
simple graph that is connected

06:02 and is edge-minimal,
which, again,

06:04 means that if you
remove any edge,

06:07 it stops having that
property of being connected.

06:10 So its an edge-minimal
connected graph.

06:12 That's kind of the reason
why trees are so important,

06:14 because if you're trying
to figure out a way

06:17 to get a whole bunch of things--
a whole bunch of vertices--

06:19 connected, a tree
is going to have

06:22 the minimum number of edges that
are sufficient to get them all

06:25 connected.

06:26 If you think about different
nodes in a network that

06:30 need to communicate
with each other,

06:32 and you want to know how many
direct connections that there

06:34 have to be between
these communication

06:37 centers in order for everybody
to talk to everybody else,

06:40 the answer is-- it's got
to be a tree on n vertices.

06:44 And a tree on n
vertices is going

06:45 to have exactly n minus 1 edges.

06:48 So that gives you still
another equivalent definition

06:51 of a tree.

06:52 A tree is a connected
graph that has n vertices,

06:55 and n minus 1 edges.

06:57 

06:59 A kind of dual way
to think about it

07:01 is that a tree is an
acyclic graph that

07:08 has as many edges
as it possibly could

07:10 without having any cycles.

07:12 So typically, an acyclic
graph might not be connected,

07:16 but as long as
it's not connected,

07:17 you can keep adding edges
that will connect things up

07:20 without creating cycles.

07:22 But the minute
you get a tree, so

07:24 that everything is connected,
you can't add another edge.

07:27 So an edge maximal acyclic
graph is still another way

07:31 to characterize trees.

07:33 And maybe the most
useful way is to say

07:36 that a graph, in which there is
a unique path between any two

07:40 vertices, is a tree.

07:43 So of course, if there is a
unique path-- in particular,

07:45 there's a path, so all the
vertices have to be connected.

07:48 But what makes it a tree is that
there aren't two different ways

07:51 to connect between two vertices,
because as soon as there

07:54 were there would be a cycle.

07:56 And those are some of
the basic ways that trees

08:00 can be formulated equivalently.

08:03 And in fact, there's lots more,
but this is enough for today.

