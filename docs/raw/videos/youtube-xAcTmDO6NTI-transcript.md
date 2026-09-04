---
source_url: https://www.youtube.com/watch?v=xAcTmDO6NTI
source_type: video
ingested: 2026-09-03
published: 2026-09-03
duration_minutes: 63
language: en
sha256: 27266cd2c28185b4d9535bf60912a404c0e2aa2243e95a08f7b1566780323fe2
time_sensitive: True
---

# YouTube Transcript: Lecture 1: Introduction to CS and Programming Using Python

## Video Information
- **Title**: Lecture 1: Introduction to CS and Programming Using Python
- **Video ID**: xAcTmDO6NTI
- **Published**: Unknown
- **Views**: Unknown
- **Language**: en

## Transcript
00:00 [SQUEAKING]
[RUSTLING] [CLICKING]

00:16 ANA BELL: All right, so welcome
to the first lecture of 6.100L.

00:21 That's our new number. My name is Ana Bell. That's two separate
names, first name Ana,

00:26 last name Bell--
super confusing. But I've been a lecturer
here in the EECS Department for probably almost
10 years now.

00:33 And I've been doing the
intro course for a while. I'm really happy to be teaching
this full semester version

00:39 of 6.100A. So today what we're
going to do is go over

00:45 a little bit of course
administrative information, and then we'll dive
right into some thoughts

00:50 about computers, high
level how they work. And then we'll start going
into some Python basics.

00:56 So we're going to get
coding right away. So I highly encourage you,
since you're in this class,

01:01 to download the lecture
slides beforehand, to take notes, and
run code when I do.

01:08 Some of the lectures
are interactive. And we'll have
breaks, so there'll be a place where
you can take a break

01:14 to actually do some coding. And that's important-- I call them "you try it" breaks. That's important to make
sure that you're actually

01:21 practicing what we are
learning right at this time. The main idea for lectures is,
yes, I will do some teaching,

01:28 but there will also
be opportunities for questions and for you
guys to try some programming

01:33 right on the spot. Even if you don't
finish writing a program that we start talking
about, I will finish it,

01:39 and we can all talk
about it together. And I'll show you some
pitfalls and things like that.

01:46 There will be lots
of opportunities to practice in this class at
various degrees of granularity.

01:52 And then there's also
lots of opportunities that I have in the handouts
to do extra practice

01:58 at home and through a bunch of
different resources as well. The reason why I stress
participation and practice is

02:05 because part of the
reason you're here is you want to learn how to program. You don't know how
to program yet.

02:12 And programming is
actually a skill. it's like math or reading. It's something that
you have to practice.

02:18 You can't just watch me type
in a bunch of lines of code And then when it comes
time to do the quiz,

02:23 you automatically
know how to do it. You need to do it often,
more and more so that it

02:29 becomes sort of second nature. So the three big things you'll
get out of this class are

02:35 knowledge of
concepts, obviously-- we're going to learn some
computer science ideas-- programming skill,
and problem solving--

02:43 problem solving skills. Lectures and exams
basically help you with your knowledge of-- test
your knowledge of concepts

02:50 and help you get
knowledge of concepts. Finger exercises give you
the programming skills.

02:56 And the problem sets help
you with problem solving. Basically, if you're given an
English version of-- a problem

03:04 in English, how do
you go from that to thinking about what computer
science concepts can I apply?

03:10 And then after that, how do
I take those computer science concepts and actually
do the programming?

03:17 So what are some topics
we'll be covering? We will be, at the
core of it, learning

03:23 computational thinking. So in the future, when
you encounter a problem,

03:28 your first thought shouldn't
be, How do I mathematically solve this? or, How
do I brute force

03:34 or manually solve this problem? How can I apply computation
to help me solve this problem?

03:39 And throughout these
lectures, you're going to see some examples
of us applying computation

03:44 to a problem you might
have already seen and maybe solved mathematically,
which is pretty cool.

03:51 Obviously, to get
that, we're going to learn the Python
programming language. Once we get the
basics, we're going

03:56 to see how we can start
to structure our code to look a little bit
better so we don't just

04:01 have a bunch of code
dumped in a file. We're going to start
to organize our code and see how we can make it
neat, readable, and modular.

04:11 And then towards the-- not in this lecture but
in a couple of lectures

04:16 and as a theme
throughout this class, we're going to look
at some algorithms. They're not super
complicated, but they're

04:23 kind of the base algorithms
for a bunch of algorithms you might see in
the future if you decide to take more CS classes.

04:30 Lastly, towards the
end of the class, we're going to see algorithmic
complexity, which basically means we're going to start
asking or trying to answer

04:37 the question, how do
we know the programs we write are efficient? We can write programs, but how
do we know that they're fast,

04:44 and how do we know
that they don't take up all the memory in the computer? So things like that,
comparing different algorithms

04:51 that do the same thing
against each other. So if there's no questions--

04:58 again, as I said, a
bunch of this information is already in the
handout plus more-- we can begin.

05:05 OK, so let's start by
talking about knowledge.

05:11 Declarative knowledge
is a statement of fact, and a lot of us probably
in math and in the past

05:17 have worked with
declarative knowledge. But this is not how computer
science, this is not how this class works.

05:23 In computer science
what we do is we work with imperative knowledge,
which is basically a recipe,

05:28 how to do something. And when we're programming,
all we're doing is writing a recipe for the
computer to do something.

05:35 That's it. So here's a numerical example. The first statement is
a declarative statement.

05:44 The square root of a number
x is y such that y times y is equal to x. There are many possible
values for x and y

05:50 that this statement
can be true, right? But if we gave that
statement to a computer,

05:55 it wouldn't know
what to do with it. What we need to do
is tell the computer how to find the square
root of a number

06:03 and then tell us what the
square root of that number is. And so the computer
then needs a recipe.

06:09 So the recipe, a
really simple one for finding the square
root of a number, is steps one, two, three.

06:15 So what we do is--
let's say we want to find the square root of 16.

06:20 We obviously know it's four,
but the computer doesn't. And so we give it
an initial guess. Let's say the guess is three.

06:27 How do we go from there? So the steps we follow-- step one, if 3 times 3,
9, is close enough to 16,

06:35 we can stop. It's not really
close enough for me. So let's keep going.

06:41 Step two-- otherwise,
we're going to make a new guess
by averaging g,

06:46 which is our original
guess, 3, and x over g, which is 16 over 3.

06:52 16 was the square root
we wanted to find. So our next guess is 4.17.

06:58 OK, using the new guess,
repeat the process until we are close enough. So we go back to step one.

07:03 That's the first
part of the process. We find guess squared. 4.17 squared is 17.36.

07:10 So now we say, is
that close enough? Not really. It's not. It's 17.

07:15 It's not really
even close to 16. So let's do it again. We make a new guess by averaging
4.17 and 16 divided by 4.17.

07:26 That gives us our
new guess, 4.0035. OK, next step, using the new
guess, we repeat the process.

07:34 So 4.0035 squared is 16.277-- .0277.

07:40 Is that close enough to x? Yeah, I could be
happy with this. I could stop there because we're
within sort of plus/minus 1.

07:47 So I'm OK with that. But if we want it to be within
plus or minus 1 times 10 to the negative 6 or 7
or something like that,

07:55 then we would
continue the process. So really what we had
there is an algorithm.

08:01 It's a sequence of steps-- step one, step two, step three. There's some sort
of flow of control.

08:07 We had a place where we said
if the guess is close enough, then we can stop.

08:13 Otherwise, we do something else. We had another flow
of control where we said repeat this thing.

08:19 So we're kind of
not going linearly, but we're changing the flow. And then lastly
is a way to stop.

08:25 We don't want the
algorithm to go on forever. We would like to
stop at some point. And this stopping point, I
was kind of vague about it.

08:32 But it could be when we
were within plus or minus 1 of the actual answer.

08:39 And so recipes are
basically algorithms, right?

08:44 My grandmother was basically
teaching algorithms when she would teach
me to bake a cake.

08:52 She didn't call it that,
but she was really. And so even recipes have
that same structure.

08:58 There's a sequence of steps. There's a flow of control. Like, if you don't have
egg, use egg substitute. Or repeat sticking
a toothpick to see

09:06 if it comes out clean every
minute or something like that. And then there's a way to stop.

09:12 When the toothpick
comes out clean, you take it out of the
oven, and you eat it. And so computers are machines
that execute these algorithms.

09:19 They're actually dumb. Computers are not very smart. They don't make
decisions on their own.

09:26 They just follow these
sequences of steps that we told them to do. Computers are good at storing
lots and lots of data.

09:35 We can't really do
that, but computers can store gigabytes of
storage, terabytes even.

09:40 And computers can do
operations really, really quickly, which is
something we can't do. They're good at
those two things,

09:46 but they're not very smart. They can't make
decisions unless they're told to make the decisions.

09:54 So really, the computer only
does what you tell it to do.

09:59 And that's one of the big ideas
that I want you to come away from this lecture with.

10:05 Computer only does
what you tell it to do. The sequences of steps
that you tell it to do, that's the only
thing it follows.

10:12 So a little brief history
just to make you appreciate programming, Python programming
language before we actually get

10:19 started with it is-- so before the 1940s,
we had these things

10:24 called fixed program computers. A pocket calculator
as an example of that. Every button was an operation.

10:33 In the little screen,
you could use parentheses to put a bunch of different
operations together, but there was no way to store
all these operations together

10:41 to later put in different
inputs for that same sequence of operations.

10:46 You had to input it every
single-- input those sequences of operations every single time.

10:52 After the 1940s, stored programs
computers came into play. And they were able to store
instructions to do things

11:03 as data. And there was a special program
called an interpreter that

11:09 executed these instructions. It knew how to follow
simple sequences of steps. When the program told it to
go to a different location,

11:17 it did. So it was basically
executing these instructions.

11:23 And the instructions that it
did were arithmetic and logical, so addition, subtraction,
things like that;

11:30 simple tests like checking for
equality between two values; and moving data, so
taking this value

11:36 and putting it at a
different memory location. So I just wanted to give
you a really brief overview,

11:41 and this is not super
accurate, but it gives you a sense of how
exactly things happen

11:47 low level in the computer. So the computer
basically has memory,

11:52 where things are stored. It has an arithmetic logic
unit that does operations.

11:57 It knows how to add things,
subtract things, multiply things, compare things. And then it has the
control unit, where

12:03 this program counter is set. And this is where
you put a program in. So let's see if this works.

12:10 This is a program. And up here is our memory. So we have a bunch of memory
locations, 3456, 3457.

12:18 And at each of these
memory locations, we have some values
stored, prefilled.

12:24 So when we first run this
program, what ends up happening is that the interpreter
sees the first instruction,

12:31 Add, the values at
3456 and 3457 together. So it goes to these
memory locations here,

12:38 grabs the 3 and the
4, and sends them to the Arithmetic Logic Unit. The ALU knows how
to do the addition.

12:44 So it adds 3 plus 4, 7, and
sends the result back here. Now, we never told it to
store that result anywhere.

12:52 But the next
instruction says Store the value you just
got back from the ALU at this memory location, 3458.

12:59 So the next step
basically takes that 7 and stores it at
memory location 3458.

13:08 Super tedious-- all we
did was add 3 plus 4. We do that again.

13:14 We add the values
at 7889 and 7890. So it goes in the memory.

13:19 It grabs the 5 and the
2, sends it to the ALU. The ALU calculates it
as 7, brings it back,

13:26 and then we store
that in location 7891.

13:32 And then after that, all
we've done is two additions. And then the next instruction
says Compare the values

13:38 at memory locations
3458 and 7891. So we're going to
compare the 7 with the 7.

13:45 The ALU again does this
comparison and says, all right, well, 7
and 7 are equivalent.

13:51 So this is true or whatever
it wants to give back to the interpreter.

13:56 And then the last
instruction here we have is Print the result
of that comparison. So we print True
because they were equal.

14:04 Again, super high
level, but it kind of gives you an appreciation
for programming languages

14:10 these days. This is very tedious to write
if we had to write programs in this manner.

14:16 Alan Turing a long
time ago showed that you can compute
anything with actually an even more basic
set of primitives,

14:22 not addition, subtraction. But instead, with a
tape, you would actually have six primitives-- move the
tape left, move the tape right,

14:29 read the value at the tape,
put a value on the tape, erase the value from the
tape, and no operation.

14:38 And so since he showed this what
the result of it actually was

14:43 is down here. Anything computable
in one language is computable in any other
programming language.

14:50 So if we had some
program written in Java, that basically boils
down to something super

14:57 long but something that is made
up of these six primitives.

15:02 That means that if we boil
down this program to these six primitives, we can build
back up the same program

15:08 in a completely
different language. And that's really powerful. That's a really cool statement.

15:14 Now, we're not going to be
working with those primitives. We're going to be using the
Python primitives, which

15:21 are more convenient,
and they allow us to do a lot more
things in much less time. I'm going to do a
little comparison

15:28 as we talk about the primitives
of Python with English. So in English, some of the
primitives might be words

15:36 or even we can do
letters or characters. But we can say it's words.

15:41 With characters, we
can build up words. With words, we can
build up sentences. With sentences, we
can build up stories. With stories, we can build up
books and things like that.

15:50 In programming
languages, the primitives are numbers, sequences
of characters, operators

15:58 like addition,
multiplication, division,

16:04 checking for equality, checking
that something is greater than, things like that. So once we have these
primitives in a language,

16:12 we can start to build up
the syntax of the language. So in English, having something
like noun and noun and noun

16:20 doesn't make any sense. Cat dog boy doesn't
make much sense. It's not syntactically valid.

16:26 But noun verb noun is
syntactically valid.

16:31 Similarly, in
programming languages, we can have two objects
kind of side by side.

16:37 So here, this is a sequence
of characters h and i. And this is the number 5
right beside that sequence

16:43 of characters. But that doesn't make
any sense, right? What does it mean to have
this sequence of characters

16:49 and that number right beside it? It has no meaning in Python. Instead, what we
have to do is we

16:54 have to add an operator in
between these two objects. So here we add a
little star operator in between the sequence
of characters "hi"

17:01 and the number 5. And in Python, the
meaning to this is I want to repeat the
sequence of characters "hi,"

17:08 h-i, five times. So this would basically
give me hi, hi, hi, hi, hi.

17:13 So once we have
sentences in English and expressions that
are syntactically valid,

17:21 we can now talk about the static
semantics of the language. So in English, saying
something like "I are hungry"

17:27 is syntactically correct,
but it's not static-- it's not-- sorry, it doesn't
have good static semantics.

17:37 There's no meaning-- there is
no meaning to that because the "are" is for you or plural.

17:44 Similarly, in
programming languages, and this will differ depending
on what programming language you use--

17:51 here, in the previous
slide, we saw that you can use the star
operator between the sequence

17:56 of characters and the number. And that meant repeat
that sequence many times.

18:01 But if we use a plus operator
in between the sequence of characters and a
number, that doesn't

18:07 have any meaning in Python. So it has a static
semantic error, even though it's
syntactically valid, right?

18:14 We have operator-- sorry,
object operator object.

18:21 So, so far, we've been able
to find really nice parallels with English, the English
language and the programming

18:28 languages. But this is kind of
where things break down, when we talk about the
semantics of a language.

18:33 So in English, you can have
many different meanings. The chicken is ready to eat
means let's eat this chicken.

18:41 Or the chicken is ready to
eat means the chicken wants to eat something. Programming languages, there
is no multiple meanings

18:49 to a program that you write. Because the computer,
the machine, the language follows the
set of instructions to a T,

18:58 there is no ambiguity
about what it needs to do. It just follows the
instructions and does

19:03 what it needs to do to the
end, till it reaches the-- it terminates the program.

19:10 And so programs only
have one meaning, but the problem is it
might not be the meaning that you intended it to have.

19:17 And that's when things
start to go wrong. We can have syntactic errors
in our program, spelling errors

19:24 and indentation errors,
things like that. And those are easy to catch. Static semantic errors are
90% probably easy to catch.

19:31 But the problem comes
in with the semantics. The meaning that you
intended this program to have

19:39 might not be what
it's actually doing. And that's where most
of my errors happen.

19:44 And that's where I get super
frustrated when I program. And that's probably where you
guys will get super frustrated too because you write a
program that you think

19:51 is doing one thing, but instead,
either it crashes right away, or it runs forever and doesn't
really stop, or it terminates,

19:59 but it gives you an
incorrect answer. It's not what you
were expecting. And we'll talk about
this in a few lectures.

20:08 So when we write
programs, we're basically writing sequences of
definitions and commands.

20:14 And we're going to write
these either in a file editor or in a shell. The first, today at least, we're
writing in the shell directly.

20:22 And half of tomorrow,
we'll write in the shell because we're not
really writing any--

20:30 we're not really writing
many lines of code. We're just going to be-- I'm just going to be showing
you some really quick things

20:39 that we can do with the
Python programming language. So hopefully you all have
installed the programming

20:45 environment. This is the Code Editor. So tomorrow, we'll
start working in here.

20:51 But for today, we're really
just going to work in the shell. And even in the
future, you can still

20:57 type commands in the shell. I find the shell very useful if
there's just something really quick that I want
to check, that I

21:04 don't want to write a
program for and then run. It's just like a
simple command that I want to check to
make sure it's doing

21:09 what I think it's doing before
I insert it in my code editor. So here we have this.

21:19 So mine is-- I guess I'm using the white
theme just because I find it easier for you guys to see.

21:25 This is the file editor. And this is just a bunch
of expressions or-- yeah, a bunch of code that
we're going to type in today.

21:32 And we're going to type it in
the shell today, so the thing on the right-hand side.

21:40 OK, so what exactly do we
do when we write a program?

21:45 At the base of it, we
are going to create objects inside our programs, and
we're going to manipulate them.

21:53 That's it. That's what programming is
mostly about at its core.

22:00 Now, when we create
objects, it's important-- this is
kind of something we're going to
come back to again

22:06 and again in a more
high-level setting. But right now what I
want you to understand is that when we create an
object, an object has a type.

22:16 And the type that an
object has tells Python the things you're allowed
to do with that object.

22:23 So here are two examples. The number 30, it's a number.

22:29 The type we'll talk
about it in a bit. The type is an integer. It's a whole number. But basically,
what are the things

22:35 we can do with this
integer, with this number? We can add it to another number. We can subtract it
to another number.

22:40 We can take it to another power. We can take some other
number to this power of 30.

22:47 A bunch of mathematical
operations, as you would expect. So that's pretty
straightforward.

22:53 What about this one here,
this quotation capital A, lowercase a--

22:59 lowercase n,
lowercase a quotation? So this is something we'll
talk about next lecture. It's called a string.

23:05 And it's a sequence
of characters. The quotations tell Python
it's a sequence of characters.

23:10 And the characters part of it
are capital A, lowercase n, and lowercase a. The kinds of things I
can do with this string

23:19 are not the same kinds
of things I'm allowed to do with the number, right? If I tried to take
Ana and divide it

23:25 by the sequence
of characters Bob, Python would complain
very much because you

23:31 can't divide a string
by another string, a sequence of characters. It doesn't make
sense to divide it by another sequence
of characters.

23:37 Similarly, I can't
take Ana to some power. I can't multiply--

23:42 I can't multiply by
itself, things like that. But the kinds of things
that I am allowed to do on a sequence
of characters

23:48 is different than
the kinds of things I'm allowed to do on a number. So the things I can do with
a sequence of characters

23:53 is I can say, well,
what's the character at the first position? What's the middle character?

23:59 How long is the
sequence of characters? How many characters do I have? And so now you can see
that the type of the object

24:07 is actually really important. Python uses it to know
the kinds of operations you're allowed to do with it.

24:13 And so there's actually
scalar objects, and these are Python's
primitives, numbers

24:19 and truth values. And there are nonscalar objects. We're not talking
about these yet. We'll talk about these
in a few lectures.

24:26 But these have some
sort of structure. So for example,
a list of numbers has a structure because there's
a number at the beginning

24:33 of the list, there's a number
at the end of the list, things like that. But a number itself
doesn't have a structure.

24:39 It's just the number. So what are the types
of the scalar objects?

24:44 What are the types of
the primitives in Python? Integers, so number 5, 0,
negative 100, 1 million.

24:52 Float is another type. It represents all the
real numbers, so 3.27.

24:58 2.0 is a float because it
has a decimal number even though to us that just means 2.

25:04 But to Python, if
you put in 2.0, it says that's a type float. Negative 3.14159,
things like that.

25:12 Bool is a Boolean. It represents truth values. And there's only two possible
values that a Boolean type has,

25:20 True and False. And it has to be capital T
True and capital F False.

25:26 And the last one is
this NoneType type. It's literally called NoneType.

25:33 And it has only one
special value, None. We're not going to talk
about it for a bit, but we will sometime
in the future.

25:41 So to figure out the
type of an object when you create that object,
you use the type command.

25:47 So we can say something
like type parentheses. And this is a command. And inside the parentheses,
you say, what do you

25:54 want to find the type of? So if we do type of 7,
it tells me it's an int.

25:59 And if you want to do
the same command again, I hit the up arrow,
and it automatically puts in what I wrote previously.

26:04 And then if I want
to do type of 0.0, it's a float because
there's a decimal point.

26:13 So this is basically
what I said. So we type this in the shell. And the shell tells
us what the output is.

26:23 So just to reiterate,
int, float, bool, and NoneType are
types of objects.

26:31 And there can be many
different objects you can create of that type. So if you think about
it, ints and floats,

26:38 we basically have
an infinite number of objects we can
create of those types

26:44 because we can have 0, 1, 2,
3, 100, 200, 300, 1 million, and all the negatives.

26:49 There's almost an infinite
number of values or objects that we can create of
type int and float.

26:56 But bool, there's only two,
the truth values True or False. And the NoneType, there's
only one, this None.

27:04 So that's the type, and these
are the possible values, possible objects we can create.

27:11 You try it. So you can just yell
out the answers. There's nothing to type unless
you want to check yourself so

27:17 what is the type of 1234? AUDIENCE: Int. ANA BELL: Int. Type of 8.99?

27:24 Float. Type of 9.0? Float. Type of True?

27:29 Bool. And type of False? Bool. Perfect. If you ever wonder what
the type of something is,

27:35 you type it in here. You guys are doing well. Type is bool. Type of lowercase
t true is an error,

27:43 just wanted to point that out
just to reiterate the fact that capitalization
matters in Python.

27:49 This is our first
error, by the way, guys. Very exciting. The error is a
NameError, and this is

27:55 the message associated with it. You also know that it's
something special in Python

28:04 when you have color-coded stuff. So you see capital T
True, capital F False are

28:10 this dark blue here,
whereas anything that's not special in
Python is just black.

28:17 So type is a special command. This is a float, so you
see they're color coded.

28:23 OK. So once we create
objects, one thing we can do with these
objects is to cast them

28:30 to a different type. Now, this is a little
bit maybe confusing

28:36 because we're not actually
changing the object once we've created it. So once we create the integer
3, it's there in memory.

28:46 If we cast that integer
to a float version of it, we're creating a new
object in memory.

28:52 We're not changing the 3. The 3 already exists. We're just getting the
float version of it

28:57 and storing it as a
new object in memory. So when we do float
3, this is a command

29:03 that gets for me the float
version of the integer 3. So that will give me 3.0.

29:10 So for example, this
is what I had, float 3.

29:16 The output is 3.0. If I do int of 5.2,
it truncates it,

29:26 and it gives me the integer
portion of this float. If I do int of 5.9,
it still truncates it

29:33 and gives me the integer
version of this float. It doesn't round. I'm just asking for the
integer version of this float.

29:42 Some operations like
round is an operation we can do has an
implicit cast in it.

29:48 So if I round 5.9, it's actually
going to round it to 6.0 and then cast it to an integer.

29:55 So notice it doesn't
give me as an output 6.0. It then rounds it to just six.

30:03 So that's basically what
I said in the example. So let's have you try this.

30:10 What are the types
of the following? I don't need the
values but the types. So if I get type of float of
123, what is the type of that?

30:23 Float, yeah, exactly. Yep. What if I round 7.9?

30:28 What's the type of the result? Int, yep. What if I create a float
of the round of 7.2?

30:35 AUDIENCE: Float. ANA BELL: Yes, good. Float would be 7.0. And the int of 7.2?

30:41 AUDIENCE: 7. Int. ANA BELL: Int, yes, exactly. I want the type not the value. And the int of 7.9
is an int, exactly.

30:51 Awesome, good. OK, so we've created
a bunch of objects.

30:57 We know that we can
create a bunch of objects in our programs. What do we do with them? Well, we can combine
them into expressions.

31:05 So let's say we have 3 plus 2. I've got object,
operator, object.

31:11 Cool, syntactically
valid in Python and has no static
semantic error. So if I do that in Python,
it's going to be OK.

31:21 3 plus 2, 5. And the type of 3
plus 2 is an integer.

31:31 So basically what
I've done here, I've put an expression
within this type command.

31:38 And that's OK. That's, in fact,
encouraged in Python. You don't just want to
calculate and then stick in.

31:44 That would be
very, very tedious. So you can insert expressions
in many, many different places.

31:50 So here we have 3 plus
2, 5 divided by 3. Again, we've got 5 divided
by 3 has this decimal value.

31:56 And the result has a float-- is of type float.

32:01 So the important
thing to remember when we're doing expressions
is Python reads the expression,

32:08 but it does not store
the expression in memory. What it does is it
reads the expression,

32:15 evaluates it to
one single value, and then it stores the
result value in memory.

32:22 So it never stores
the expression. It evaluates the expression
and then stores the value.

32:27 And so this is the syntax for an
expression-- object, operator, object, as we just saw.

32:33 And that's really-- and
the idea I said before, where Python stores
values of expressions,

32:40 not the expressions themselves,
is really, really important.

32:45 So this is my first
big idea slide. I decided to insert
these because I

32:50 think they stress the
importance of several concepts. So I hope this is one. So we're taking expressions.

32:57 They can be as
complex as you'd like. We can use parentheses,
a bunch of-- it doesn't just have to be
object, operator, object.

33:05 It can be more
complex than that. But basically, however
complex that expression

33:10 is, we evaluate it, and we
replace it with one value. And the expression can
be something like this.

33:18 It doesn't just have to be
something that's mathematical. This was a mathematical
expression, but this is also an expression.

33:24 And it evaluates. So this entire thing evaluates
to this word, this word which

33:31 represents the type integer. So here are some more examples.

33:36 3 plus 2, again. We've got these examples
with the parentheses,

33:42 4 plus 2 times 6
minus 1 obviously gives us the number, 35. And then we can insert
expressions wherever we'd like.

33:49 So here I'm inserting
that specific expression in the type command.

33:54 And this is also an
expression, like I just said. And its result is int.

34:00 And similarly, we can also
insert that expression here. And then we can wrap
that around cast.

34:06 And it gives us a float. Yes? AUDIENCE: So when you're
inserting expressions

34:11 [INAUDIBLE] include
the operators-- [INAUDIBLE] operators in? ANA BELL: When you're
inserting-- sorry,

34:17 when you're inserting what? AUDIENCE: Well, since you
said they're expressions, and you said that you need
like object, operator, object,

34:24 expression, type. What would be the
operators in this case? ANA BELL: Oh, I see.

34:30 AUDIENCE: How are they defined? ANA BELL: Yeah, that's a
good-- that's a good question. So in this particular case, the
type and the float are not--

34:41 there is no operator I guess
in this particular case. It's more like a command
that gives us an output.

34:48 But there is still some-- there is still an
output that it gives us.

34:54 So we can then take
the result of this and save it somewhere else.

35:00 Sorry, yeah, I guess the example
I gave on the previous slide was just an example
of an expression

35:06 where we could do
object, operator, object. Yeah.

35:14 Yeah, so when we have these-- I guess it works for
mathematical expressions. Mathematical expressions
work left to right, just

35:21 like in math. Parentheses can override
certain precedents.

35:29 If we have commands
that have computations, then we have this command
with the parentheses.

35:36 And we evaluate what's
inside the parentheses first. So we work our way in to
out in that particular case.

35:42 So here are some examples. Let's have you try these.

35:47 So we can type these
in our console. What are the values of
the following expressions?

35:53 So 13 minus 4 divided
by 12 times 12. So we can try that.

35:58 I don't know off
the top of my head,

36:04 so we'll have to type it in. 0.0625, OK. So the value of that
expression is a float, right?

36:10 0.0625. What's the value of the
expression type 4 times 3?

36:17 AUDIENCE: Int. ANA BELL: Int, yeah. What about the type of the
expression 4.0 times 3?

36:23 AUDIENCE: Float. ANA BELL: Yes, exactly. That's very good. So type of 4 times 3 is int.

36:30 But 4.0 times 3 is a float. Good. And then what about int
of a half or of 1 over 2?

36:37 AUDIENCE: So it's 0.

36:42 ANA BELL: Yeah, exactly, it's 0. Yep, because it's 0.5,
and we truncate to 0.

36:50 The reason I had this here
is because it leads nicely into this slide. You don't have to
memorize these rules.

36:56 You can always check
it out in the console. But there are some
rules for the resulting

37:01 types when we do operations. So when we do
operations with numbers,

37:06 addition, subtraction,
and multiplication always yield an integer if both of
the operators are integers.

37:15 If one is a float
or both are floats, then it gives me a float. Division is different.

37:20 No matter what types you divide,
you will always get a float.

37:27 Now what about this
// and this percent? These are actually
useful operations.

37:32 They kind of go hand
in hand with division. So when I do 5 divided
by 3, it's this 1.667.

37:41 // is basically a floor or
getting the integer portion

37:48 of the division. So 5//3 gives me one. It truncates the fraction.

37:57 The percent gives
me the remainder. So 5%3 gives me the remainder
when I divide 5 by 3.

38:05 So it's going to give me-- give
it to me in a whole number. So that's going to be 2 because
there's 2 left over when

38:12 I divide 5 by 3. So these are pretty
useful operations,

38:17 the // and the percent, when
we do mathematical programs.

38:23 The last thing is
the ** is how we denote power, exponentiation,
kind of different

38:30 than you might be
used to in math. So 2 to the power of 3, 8.

38:36 2 to the power of 3.0, 8.0. And the rules for integer
division, percent,

38:45 and exponentiation are just
like addition, subtraction, multiplication. If one is a float, then the
result will be a float as well.

38:52 Yeah.

39:00 OK, and we talked about
the type of output. So I think I briefly
mentioned this.

39:06 The operator precedence
is exponentiation and then multiplication, division,
percent or remainder

39:12 at the next level,
and then addition, subtraction at the bottom. But you can always override
these using parentheses.

39:20 OK, questions so far
before we move on? Yes.

39:25 AUDIENCE: So why does
division-- why does it always result in float
if you have 9 by 3 and that's [INAUDIBLE]
why does it [INAUDIBLE]??

39:32 ANA BELL: Yeah, so the
question is, why does it always result in a float? If it didn't, I think it would
the operation itself would have

39:40 to do extra work to figure out
whether it's a whole number or not. So I think it's just easier
that it gives us always a float,

39:49 I guess. Previous versions of
Python, the / was actually, I think, integer division,
which is super counterintuitive

39:58 because you would use
that in your program. And then you would
basically integer divide, and things would go wrong.

40:03 But again, just a design choice
on behalf of the programmers. Other questions so far?

40:11 OK, so we have a lot of objects. Objects have different types,
again, floats, integers,

40:18 Booleans. What can we do with them? So far, they're kind of
just sitting in there,

40:24 and we can get
properties about them. But what we'd like to
do is write programs, basically trying to
automate some things

40:30 about these objects,
manipulate them to help us achieve a more
complicated and interesting

40:36 program. So what we can do
to get to that end

40:42 is to start assigning names
to some of these objects.

40:48 If I create an object for pi in
my program to 20 decimal places

40:54 somehow, and I have that
number in my program, that float in my program-- if I want to use that number
in many different places

41:02 in my program, I'd
have to copy and paste it a whole bunch of times so
far, which is very tedious,

41:10 lots of errors will happen. I don't want to do that. So instead what I can
do is I can give a name

41:16 to this ridiculously long
value of pi called pi. And then I can just
use this name anywhere

41:23 I want to grab that
ridiculously long value for pi in my program. It's a lot easier to read.

41:29 It's a lot easier for me
to write this program. And it leads to a really
nice and neat program.

41:38 So what we can do
is we can start saying that the float 0.001
will be referenced by the name

41:45 "small" or the 100.4 will be
referenced by the name "temp."

41:52 So what we want to do is create
these things called variables. And a variable is different
in computer science

42:00 from a mathematical
variable or variables that you've known
so far in math. So math variables
come back to the idea

42:06 of declarative knowledge,
a declarative statement. You can have something like a
plus b is equal to b minus 1

42:12 in math, or x is equal to--
or x times x is equal to y, and that's perfectly OK.

42:19 In math, we basically say
that variable x represents all the square roots of y.

42:24 That's not going to fly
in computer science. In computer science,
we don't have--

42:30 we don't do
declarative knowledge. We do imperative knowledge. And so what we're working
with in computer science

42:35 is a bunch of
assignment statements. So what we can do
in computer science

42:42 is we're going to basically
bind a value to a variable.

42:47 So we're going to say
this variable name is bound to this value. Every time I want
to grab this value, I'm going to invoke
this variable name.

42:55 So here are some examples. I've got a is equal to b plus 1. The thing on the right-hand
side will evaluate to some value

43:03 as long as I have something
that b has a value for.

43:09 I've got here m is equal to 10. So m is a variable. Its value is 10.

43:14 I've got F is equal
to m times 9.98. So again, I have an expression
on the right-hand side,

43:21 and that's OK. I'm going to use the value of
10, so F's value will be 99.8.

43:27 Yeah. AUDIENCE: Can you put
it so that for F--

43:32 is it like this one value of m? Or can you have it
so it's going to be whatever m assigned recently?

43:38 ANA BELL: Yeah. The question is, can you have
m whatever it recently is? So in this particular case,
I just have these two lines.

43:45 And m will be whatever 10 is. But we'll see in a couple
lectures that we can write

43:51 a loop where you change m. And then every time you change
m, you immediately calculate F.

43:58 And then it'll calculate F
based on the new value of m. But if we just have these two
lines, that's all there is.

44:05 It just uses 10. Was there another question?

44:11 So in computer science,
you have only one variable to the left of this equal sign,
called the assignment operator.

44:18 And you have a value
to the right-hand side of the equal sign, the
assignment operator.

44:24 So one variable basically
maps to or binds to one value.

44:29 So the equal sign is an
assignment statement. It's not equality.

44:35 It's not a solve for
x type of situation. It's just an assignment. It binds this name
to this value.

44:42 So the way that we figure
out the name with the value is, well, if we have this
assignment statement here,

44:49 we first look at
the right-hand side. So we always start with
the right-hand side. And we evaluate it.

44:55 Remember, we have an
expression on the right. We have to evaluate
it to one value.

45:00 So this will be 3.14,
whatever it is, 1.159. And then we take that value
and bind it to the name pi.

45:09 So anytime I type in p-i, "pi,"
in my program from now on, Python will automatically
grab 3.14159 from memory.

45:18 So it's bound to that value now. OK, there are some rules. Did I have them on
the previous one?

45:24 Yes, there are some
rules to variable names,

45:32 but we'll talk
about that in a bit. For now, I want you to tell
me if any of the following are allowed.

45:37 If I do x is equal to 6,
is that allowed in Python? AUDIENCE: Yes. ANA BELL: Yes, it is. Good.

45:42 Because I have one variable
name bound to one value, 6. What about 6 equals x? It's just backward. AUDIENCE: No.

45:48 ANA BELL: OK, good. 6 equals x is bad, syntax error.

45:53 How about x times
y equals 3 plus 4? AUDIENCE: No. ANA BELL: No, exactly,
because the thing on the left

45:59 has an operator in it. And operators are special. So it can't have-- you can't
have a variable with that *

46:06 as a name. How about xy equals 3 plus 4? AUDIENCE: Yes. ANA BELL: Allowed, yes, exactly.

46:11 I was hoping to get you guys
with that, but I didn't. Xy equals 3 plus 4 is OK.

46:17 There was no error. And then I can invoke the
name of the variable I just created simply by typing it in.

46:23 So if I type in
xy, it gives me 7. And then I can do operations
with it, xy plus 1 is 8.

46:32 Yeah. AUDIENCE: Before you
were putting the strings with apostrophes. So wouldn't you need that?

46:37 ANA BELL: So those are strings,
right, sequences of characters. Here, these are variables. So these are names that I
am giving as a variable.

46:47 Yeah, that's a great question. So this is going to be a string. And you notice it changed color.

46:52 It has some meaning in Python. But xy is a variable
that I create.

47:03 OK, so why do we want to
give names to variables? Because as I showed you
with the pi example,

47:10 it's a lot easier to
write readable code if you have variable names
within your programs.

47:18 So when you grab-- when you write programs,
it's important to choose variable names wisely.

47:25 You don't want to use
just single letters. You don't want to
name it something that doesn't have something
to do with the program you're

47:31 writing, because
you're going to want to reread these programs
sometime in the future.

47:36 Or others might want to
read your programs sometime in the future. So here's an example
of a nice program.

47:43 It's just basically four
assignment statements that do some calculations.

47:48 The first line of the
program is not really a line. It's called a comment. You can have as many
of these as you like.

47:54 They start with a hash. It's a line that
starts with a hash. And it's basically
a text that you

48:00 write that helps you or
others figure out what the code is supposed to do.

48:07 And usually we comment large
chunks of code at a time, not line by line.

48:13 Then we have these four
assignment statements. So here I'm defining variable
named pi bound to the value

48:22 here, so not the
division but 3.14159. Variable named radius
bound to this float 2.2.

48:28 And then I have a
variable named area which is bound to the
result of this expression.

48:34 So when Python sees
my pi and my radius, it grabs them from memory,
replaces them with the values,

48:42 evaluates the expression,
grabs that one value that we evaluated to
15-point-something, whatever

48:49 this is, and binds the
15-point-something to the name area. Same with circumference.

48:55 Code style is something
that we're actually

49:01 going to look at in
your problem sets. So I just wanted to
quickly talk about that. Here is a program that
has really bad style.

49:09 Actually, that shouldn't be meh. It should be terrible
or something like that. But in case you
haven't noticed, it's

49:15 the same program as
on the previous slide. But if I gave you this
program straight off the bat, you probably wouldn't
know what it's doing.

49:23 It's reusing 355
over 113 twice here. It's using just a and
c as variable names.

49:30 Its description is
"do calculations." So pretty bad. This is a little bit better.

49:36 I've recognized that 355
over 113 is being used twice. So I'm saving it as a variable.

49:43 But my variables are
still single characters. And my comments are pretty bad.

49:51 I'm basically saying
what the code is doing. Please don't do that.

49:56 We can see that a equals
p times r times r. I see that I'm multiplying
p with r squared.

50:03 I don't need to read
that in English. What I would like to see
is a comment like this.

50:10 Here I'm commenting
a chunk of code. And someone who doesn't want
to read this chunk of code

50:17 just reads the
comment, and I already know that I'm calculating the
area and circumference using an approximation for pi.

50:23 That's a pretty nice comment
there and good descriptive names and all that.

50:31 So we can actually--
once we create an object, a variable-- sorry, once we
create an object and bind it

50:37 to a variable, we can
change the bindings. So we can take
that variable name

50:43 and bind it to a
completely different value. This might not be
useful right now,

50:49 but it will be useful
when we introduce control flow in our programs.

50:55 So to rebind a variable
what that means is we're going to take
the name, we're

51:01 going to lose the binding
to the previous value, and we're going to
rebind it to a new value. So I'm going to show you how
this looks like in memory.

51:08 I'm going to use this
sort of cloud picture to represent what
happens behind the scenes

51:14 whenever we write programs. And it's like a little animation
to help you understand line by line what's going on.

51:20 So here we have pi equals 3.14. So the green 3.14 is
my value in memory.

51:27 Cloud is memory. That's my value in memory. And it's bound to this name pi. So this is my variable name.

51:35 The next line, radius
equals 2.2, same thing. I've got 2.2 as my value
in memory, my object.

51:41 And radius is the
name for that object. Area equals pi times
radius squared.

51:47 So what happens
behind the scenes is it calculates this value. It doesn't store the expression.

51:52 It stores the value resulting
from the calculation, and then it saves it--

51:58 or binds it to the name area. OK, everything OK so far? We've seen this code before.

52:04 Cool. So now what happens
when we do this, radius equals radius plus 1?

52:09 In math, that would
say 0 equals 1.

52:15 But we're not in math here. We're in computer science,
and this is perfectly valid.

52:20 We're following the rule when
we have an assignment that says look at the right-hand
side first and evaluate it

52:29 and then bind it to
the left-hand side. So if we look at the right-hand
side first, we see radius.

52:37 Well, what's the value? 2.2. We see add 1 to it, 3.2.

52:43 Save that in memory. And then we see the assignment. Now save it with
the name radius.

52:52 OK, so we can only have
one variable assigned to one value at a time.

52:58 This is not math. This is computer science. So you can only have radius
point to one thing at a time.

53:05 With this line of code,
radius equals radius plus 1. We've lost the binding to
2.2, this object in memory,

53:12 and we've rebound
it to the value 3.2. And that's perfectly fine.

53:19 2.2 is now just
sitting in memory. We can't get back to it unless
we say maybe radius equals 2.2.

53:25 It just sits in
memory and then might be collected later
on by-- or reclaimed by garbage collection
or something like that.

53:31 But for now, we
can't get back to it. Now, what's the value for area
at the end of these lines?

53:39 Well, according to
this, it's 15.1976. So it's using the old
2.2 value for radius.

53:47 And that's OK because
the program never told--

53:52 never had a line that
said recalculate area after we changed the radius.

53:59 It's just following,
dumb, line by line. It doesn't know that, hey,
if I change the radius,

54:05 the user might want
the area changed. It doesn't make
those connections. It's just following
instructions.

54:12 And that's OK. If we want it to
change the area, we would have to copy
this line and paste it

54:18 after we've changed the radius. And then the area
would change as well.

54:24 Does that make sense? That's kind of an important
part of this lecture. OK, cool.

54:30 So big idea here is our
lines are evaluated one after the other. We're not skipping. We're not repeating things.

54:36 That's something we're
going to learn about later. But for now, line by line.

54:41 So here's a little you try it. These three lines are
executed in order. What are the values
for meters and feet

54:49 variables at each line? So how about at the first line,
what's the value for meters

54:54 after we execute the first line? 100. What about feet?

55:01 So at the end of the first line,
there is no value for feet yet. How about after the second line?

55:07 328.08. Right? How about the value for meters? AUDIENCE: 100. ANA BELL: 100 still.

55:13 And what about after
the third line? I'm changing meters to 200.

55:20 Exactly, yeah. Meters is 200, but
feet is still 328.08.

55:26 And this is something I
want to show you guys today. And we're going
to use this Python

55:31 Tutor a lot more in the future. Python Tutor is a nice
website that allows

55:37 you to step in your code-- step through your
code step by step. So at each line
that you execute,

55:44 you get to see the values of
all the variables in the code. It's a very useful
debugging tool. I hope you'll try it out
today and on Monday, maybe,

55:52 for the finger exercises
if you're having trouble. And you can use it for
quizzes to help you debug.

55:59 But I can just show you. It's pretty simple here because
it's just a step by step. So we step through.

56:05 So the red says the line
I'm going to execute. Green is the line
I just executed. So I just executed meters 100.

56:12 So here I have my meters
variable with the value 100. Step through next.

56:17 So I just executed
feet equals this. So I now have a variable named
feet with a value 328.08.

56:24 Meters still 100. And then meters 200,
feet remained 328.08.

56:33 So obviously, this is
a pretty simple program to run the Python
Tutor on, but you can imagine using it in
more complex settings.

56:44 How about one more? And this is my last example. I want you to try to
write a program that

56:49 swaps the values of x and y. So originally--
and I'll draw this, the memory diagram real quick.

56:55 So we have-- this is our memory. We have x is bound to 1.

57:00 Y is bound to 2. And what I want to do
without saying x equals 2,

57:08 y equals 1, what I want
to do is swap the values. I want x to be associated with
2 and y to be associated with 1

57:14 but only using
commands like this. And so the code here is buggy.

57:22 That means it's wrong. It has an error in it. Well, let's step
through-- let's step

57:28 through a little bit at a time. Y equals x. What do I do when
y equals x here?

57:34 Yeah, exactly, y is going
to move from 2 to 1.

57:43 Now, what happens
when I do x equals y?  Yes, x stays the same.

57:49 My first line, y equals
x, lost the binding to 2. And now it's all messed up
because I can't get it back.

57:58 So instead-- so if you
didn't understand this, you can click Python Tutor
and just step through step

58:03 by step on your own. But how can we fix this? AUDIENCE: Create
a third variable.

58:09 ANA BELL: Create
a third variable? Yeah, that's a great idea. Yeah, we can create
a third variable. So x is 1, y is 1--

58:16 y is 2. So we can create
a third variable. What do you want to make
the variable equal to?

58:23 X or y? Yeah, either one. I made it y, so let's do y.

58:30 So here I've got a temporary
variable called "temp," and I made it equal to 2.

58:36 And now what can I do?  Which one can I reassign now?

58:43 X equals y, or y equals x? Exactly, y equals--
if I do x equals y,

58:49 I lose my binding to 1,
and it messed up again. So y equals x is OK to do.

58:55 So I'm going to lose the
binding from y from 2 and bind it up to 1.

59:01 And now what do I do? Yeah, now I can safely
reassign x to temp.

59:10 So I can say x is equal to
temp because temp points to 2. And I want to make x
point to 2 as well.

59:19 So in terms of code,
that's sort of the diagram. But we can write the code. So you don't-- let's see.

59:27 We don't write it in
here, but on your own, you can write it in
here if you'd like.

59:32 Or we can do it together. So x is equal-- oops. X equals 1, y equals 2.

59:39 And then we had temp. We wanted to assign
it to whatever y was.

59:45 So we say temp is equal to y. And if you want to check
the values of the variables,

59:50 you can just invoke the names. So x is 1, y is 2, and temp
should be whatever y is, 2.

59:59 OK, good so far. So now I'm at the step
here, I think, right?

60:07 I've just created this. And then the last
thing I need to do is lose the binding from
x to whatever temp is.

60:15 So I want to do
this operation here, which means I want to assign
x to be equal to temp.

60:23 So now x is 2, y is 1.

60:29 What did I do? Yeah, so this happens sometimes.

60:36 We can just start all over. So y equals temp.

60:41 Sorry. Temp equals y.

60:49 Y equals x. Y is one. X is 1.

60:54 And then x equals temp. Y is one, x is 2.

61:00 So it's OK if things go wrong. They will go wrong. We can just start all over
in this particular case

61:08 by redefining our
variables and just trying it out all over again. So that's kind of
what the shell is for.

61:13 That's what I use it for. That's what we're going to
use it for in the future, just to do quick things
like this and also things

61:20 like checking the types
and other commands we've done earlier.

61:27 OK, so any questions
before we do the summary? Was this all right pace
or was it too fast?

61:33 Or it was OK? OK, good. Thumbs up is good. So let's do a quick summary.

61:40 We saw that we can
create programs by manipulating objects. We created objects in Python.

61:47 And we saw that objects
have a particular type. The type that the object
has tells Python the things

61:53 that you can do
with that object. We can combine objects
in expressions.

62:00 And these expressions
evaluate or boil down to one particular value.

62:06 Objects or values can
be stored in variables. And these variables allow
us to access these values

62:13 with nicer names later
on in our program. And then we're able to write
neater, more legible programs

62:20 as well. So the equal sign-- I showed you a couple of
differences between math and computer science.

62:26 The equal sign was one
notable difference. The equal sign in
math is declarative,

62:31 and the equal sign in computer
science is an assignment. You're basically saying this
is associated with this.

62:38 And we're not doing any sort of
equality in computer science.

62:44 And yes, computers do
what you tell them to do. That's kind of the
big thing here.

62:51 Line by line, it executes
starting from the top, goes line by line. So far, we haven't
seen any places where

62:58 the computer makes a decision. But next lecture,
we will see how we can insert decision
points in our programs

63:06 for the computer to either
execute one set of code or another set of code.

63:12 All right, so that's the
end of today's lecture. Thank you all for joining. I will see you on Monday.

