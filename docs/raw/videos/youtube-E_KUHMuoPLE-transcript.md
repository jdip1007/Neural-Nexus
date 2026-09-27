---
source_url: https://www.youtube.com/watch?v=E_KUHMuoPLE
source_type: video
ingested: 2026-09-26
published: 2026-09-26
duration_minutes: 8
language: en
sha256: 1c33011400c4945e293373303e4fa033766c909b9af3f62dab60a4e3f4edb6e6
time_sensitive: True
---

# YouTube Transcript: 1.3.4 Working with Data - Video 2: Getting Started in R

## Video Information
- **Title**: 1.3.4 Working with Data - Video 2: Getting Started in R
- **Video ID**: E_KUHMuoPLE
- **Published**: Unknown
- **Views**: Unknown
- **Language**: en

## Transcript
00:04 

00:04 You should have already
downloaded and installed

00:06 R on your computer.

00:09 If you have not downloaded
and installed R yet,

00:12 please follow the instructions
on the course website

00:15 before continuing
with this lecture.

00:18 Once you've installed R,
go ahead and start it.

00:22 You should see the R
console like we see here.

00:26 This is where we'll type
commands and perform

00:28 data analysis.

00:31 In this course, we'll mostly
be working in the R console,

00:35 but sometimes you'll
also want to use

00:37 what are known as
"script files."

00:40 We'll see an example
of how to use a script

00:43 file at the end of this lecture.

00:46 In your R console, you'll always
type commands after the arrow,

00:51 or "greater than" sign.

00:53 Let's start with some
basic calculations.

00:56 So with your cursor
at the arrow,

00:59 let's type 8, and then the
star symbol for "times,"

01:04 the number 6, and hit Enter.

01:06 You should see the
result 48, or 8 times 6.

01:11 In this way, R can be used
as a basic calculator.

01:16 We can perform many other
basic calculations, like 2,

01:20 "raised to the power," by typing
the carrot symbol, and then

01:24 the number 16,
and hitting Enter.

01:27 You should see the result
65,536-- or 2 the power 16.

01:35 Note that each of the results
here are labeled with a 1

01:38 in brackets.

01:40 This is just R's way
of labeling the output

01:43 and we can safely ignore it.

01:46 If you type something
in your R console

01:48 but don't finish it
properly-- for example,

01:52 try typing 2 and
the carrot symbol,

01:55 and hitting Enter-- R
will show you a plus sign

01:59 and will wait for you
to finish the command.

02:02 You can either finish the
command-- in this case,

02:05 by typing a number--
or you can hit Escape,

02:09 and R will take you
back to the arrow sign.

02:13 So if you ever see a plus
sign while working in R,

02:16 it means that R is waiting
for you to finish the line.

02:20 If you're not sure
how to finish it,

02:22 you can always just hit Escape.

02:25 A nice feature of
the R console is

02:27 that you can scroll through
your previous commands

02:31 by using the up and down
arrows on your keyboard.

02:35 If you hit the up
arrow three times,

02:38 you should go back to
the 8 times 6 command.

02:43 If you hit Enter, you can
run this command again.

02:47 You could also adjust
previous commands.

02:50 Hit the up arrow again to go
back to the 8 times 6 command.

02:54 This time, delete the 6,
type a 10, and hit Enter.

03:00 We'll use this
approach to re-run

03:03 or adjust commands many
times in this class.

03:08 Generally, R works in terms
of functions and variables.

03:14 A function can take in
several arguments, or inputs,

03:18 and returns an output value.

03:21 An example is the square
root, or sqrt, function.

03:27 In your R console,
type sqrt, and then

03:31 in parentheses, the
number 2, and hit Enter.

03:36 The function is sqrt, the input,
or argument, is the number 2,

03:43 and the output is 1.414214.

03:49 There are thousands of
functions in R. Some of them

03:52 are built into R--
like this one--

03:55 and some can be added in by
installing packages, which

03:59 we'll do several
times in this class.

04:03 Another example of a function
is the abs, or absolute value

04:07 function, which returns the
absolute value of a number.

04:11 So if we type abs and then
in parentheses negative 65

04:18 and hit Enter, we should get
the result 65 as our output.

04:24 You can get help on
any function in R

04:27 by typing a question mark
and then the function name.

04:31 So if we type ?sqrt
and hit Enter,

04:36 you should see the R Help
Page for the sqrt function.

04:42 The help pages are
often very useful,

04:45 and if you want to learn
more about a function,

04:47 you should refer to
the help page in R.

04:51 Now, get rid of the Help Page,
and go back to your R console.

04:56 Suppose we now want to save
the output of a function.

05:00 We can do this by
saving it to a variable.

05:04 In your R console, type
SquareRoot2 and then an

05:11 equals sign, and then sqrt, and
in parentheses the number 2.

05:17 And hit Enter.

05:19 Now you don't see
the output of sqrt(2)

05:23 because we saved it to the
variable named "SquareRoot2."

05:27 You can see the value of a
variable by typing its name

05:31 and hitting Enter.

05:32 So type SquareRoot2 exactly how
you typed it before, and hit

05:38 Enter.

05:39 You should see that it
takes the value 1.414214.

05:45 SquareRoot2 is a
name that we created,

05:48 and we could have named
it many other things.

05:51 Generally, you have
a lot of freedom

05:53 in naming your variables, but
there are a couple basic rules.

05:57 One is that you should not
use spaces in variable names.

06:02 If you want to easily separate
words in a variable name,

06:06 popular strategies are using
a mix of capital and lowercase

06:09 letters-- as we did
here-- or to separate

06:12 the words using periods.

06:15 Another basic rule is
that you should not

06:17 start variable
names with a number.

06:20 Keep in mind that variable
names in R are case-sensitive.

06:24 Capital and lowercase letters
are seen differently by R.

06:29 When we created our
variable SquareRoot2,

06:32 we used the equals
sign for assignment,

06:35 or to assign the
value of sqrt(2)

06:39 to the variable
named SquareRoot2.

06:42 You could instead use a
"less than" sign with a dash.

06:46 For example, let's create a
new variable called HoursYear,

06:52 and then type the less
than sign and a dash,

06:56 followed by 365 times 24.

07:01 If you hit Enter and then type
HoursYear to look at its value,

07:06 you should see 8,760-- or the
number of hours in a year.

07:12 By doing this, the less
than sign and the dash

07:15 did the exact same
thing as it would

07:17 have done if we used
the equals sign.

07:20 In this course, we'll
typically use the equals sign.

07:23 But if you see this less
than sign and a dash used,

07:28 keep in mind that it means the
same thing as an equals sign.

07:32 Lastly, if you type ls and then
empty parentheses in your R

07:36 console and hit
Enter, you should

07:39 see a list of all
of the variables

07:41 that you've created in
your current R session.

07:45 Here, we've created
two variables--

07:47 HoursYear and SquareRoot2.

07:50 This can be useful if you
forget exactly how you

07:53 typed a variable name.

07:56 These are our basic building
blocks in R-- functions,

08:00 like square root and absolute
value, and variables,

08:04 like HoursYear and SquareRoot2.

