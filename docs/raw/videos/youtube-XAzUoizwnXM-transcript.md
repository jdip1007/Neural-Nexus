---
source_url: https://www.youtube.com/watch?v=XAzUoizwnXM
source_type: video
ingested: 2026-09-15
published: 2026-09-15
duration_minutes: 16
language: en
sha256: af25763401886abc754315a19702c7c00203429629113db420dc6616d430d428
time_sensitive: True
---

# YouTube Transcript: fopen is Magic! - Find Out What You've Been Missing All These Years!

## Video Information
- **Title**: fopen is Magic! - Find Out What You've Been Missing All These Years!
- **Video ID**: XAzUoizwnXM
- **Published**: Unknown
- **Views**: Unknown
- **Language**: en

## Transcript
00:02 Today we're going to talk about one of

00:03 the most boring looking functions in the

00:05 entire C runtime. And I'm going to try

00:06 to convince you that it is secretly one

00:09 of the most important ideas in computing

00:10 hiding behind five little letters. I'm

00:13 talking about fop. Now, if you learn C

00:15 in the normal way, fop probably arrived

00:17 somewhere around the time the textbook

00:19 ran out of interesting things to say

00:20 about arrays. You wrote a little program

00:22 that opened data.ext, text, read a few

00:24 lines, counted some words, had some fun,

00:27 couple laughs, closed the file, and then

00:29 moved on to pointers where the real

00:30 blood letting began. And you're probably

00:32 so traumatized that you've forgotten

00:34 mostly about fop. And because fop is so

00:37 simple on the surface, most programmers

00:38 mentally file it away as plumbing. It

00:40 opens a file. It returns a thing. You

00:43 pass that thing on to print f or f get

00:45 s. And when you're done, you call f

00:47 close, case closed. Except not quite.

00:50 Because under that tiny function is one

00:52 of the deepest ideas in Unix. One of the

00:54 reasons that C became such a practical

00:55 systems language and one of the reasons

00:58 small programs written 50 years ago

00:59 still compose so beautifully today.

01:02 Fopen is simple because the interface is

01:04 small. But it is magical because the

01:06 thing behind that interface might not be

01:08 a disk file at all. It might be your

01:10 keyboard. It might be your terminal. It

01:13 might be a pipe from another process. It

01:15 might be a serial port. It might be the

01:17 bit bucket at dev null or an infinite

01:19 stream of zero bytes from dev zero or

01:21 random data from the kernel or a pseudo

01:23 file in proc that does not exist on disk

01:25 in any normal sense but is actually

01:26 being synthesized by the operating

01:28 system while you read it. And with a

01:30 couple of related tricks, it might even

01:32 be the output of another program, a

01:34 network connection or a stream backed

01:35 entirely by memory. And the beautiful

01:38 part is that your code often does not

01:40 need to know. And that's the trick.

01:42 That's the whole Unix magic act in one

01:44 sentence. Take wildly different things,

01:46 make them look enough like streams of

01:48 bites, and suddenly tiny simple tools

01:50 can do absurdly powerful things. So,

01:53 let's go all the way back to the

01:54 beginning, or close enough to the

01:56 beginning that the beard gets darker and

01:58 the terminals get louder. Lately, I've

02:00 been spending about half my days working

02:02 under the original BSD Unix on my PDB11.

02:05 And everything that we're going to do

02:06 here actually works on any POSIX

02:08 compliant system, which means it'll even

02:10 work on a Windows box in most cases, at

02:12 least with the C runtime on your side.

02:14 And in old Unix, the process did not

02:17 begin life as an isolated little snow

02:18 globe. Instead, it was born with three

02:21 open IO channels already connected.

02:23 Standard input, standard output, and

02:25 standard air. In C, we know those as

02:27 standard in, standard out, and standard

02:29 air. But the names are actually the C

02:31 libraries view of the world. Underneath

02:33 them inside Unix are file descriptors,

02:35 and those are just small integers. For

02:38 example, standard input is descriptor

02:39 zero. Standard output is descriptor one,

02:42 and standard error is descriptor 2.

02:44 That's it. 0, 1, and two. The three most

02:47 famous integers in operating systems.

02:49 And they're not magic because of what

02:50 they are. They're magic because of who

02:52 sets them up. When you run a program

02:54 from the shell, the shell creates the

02:56 environment that the program will

02:58 inherit. If you type a command normally,

03:00 descriptor zero probably points to your

03:02 keyboard or your terminal input.

03:04 Descriptor 1 points at your terminal

03:06 output. And descriptor 2 also points at

03:08 your terminal output, but conceptually,

03:10 it's separate. And that separation turns

03:12 out to matter a great deal. If you run

03:15 program redirected to output.ext, the

03:18 shell arranges things so that on

03:19 descriptor one standard output, it no

03:22 longer points to the terminal. It points

03:24 at a file. The program usually has no

03:26 idea that this just happened. It just

03:28 writes to its standard output. Same as

03:30 always. The shell has swapped the

03:32 plumbing underneath it. So if you run

03:34 program redirected from input text, now

03:36 descriptor zero comes from a file

03:38 instead of your keyboard. And if you run

03:40 program with stream 2 redirected out to

03:42 heirs.ext now descriptor 2 standard air

03:45 goes to a separate file. This last one

03:48 is not some historical afterthought they

03:50 came up with later. It's one of the

03:51 reasons that Unix pipelines work as well

03:53 as they do. Standard output is for the

03:56 useful data that your program produces.

03:58 Standard error is for complaining. If

04:00 your program is generating a list of

04:01 file names and you pipe their list into

04:03 another program, you don't want random

04:05 diagnostic messages mixed into the data

04:07 stream like raisins and an otherwise

04:09 acceptable cookie. And this is the

04:10 genius reason why standard air exists at

04:13 all. It lets your program say, "Hey,

04:14 here's the data you asked for." And

04:16 separately say, "By the way, something

04:17 weird happened. One stream is cargo, the

04:20 other is radio chatter." This is where

04:22 C's file pointer enters the story. When

04:25 you write file pointer f equals f open

04:27 in a relay log with r as your flags,

04:29 what you get back is not the file. It's

04:32 not even strictly speaking the raw

04:33 operating system handle. On Unix, the

04:36 raw primitive is usually the file

04:37 descriptor, that small integer. What f

04:40 open returns is a pointer to a C library

04:42 object called a file. And that object is

04:44 doing more work than people realize.

04:47 Think of the file descriptor as a claim

04:48 ticket at the storage counter. The

04:50 colonel knows what the ticket means. It

04:52 knows whether it represents a real file,

04:54 a terminal, a pipe, or some device. A

04:56 file pointer, on the other hand, is like

04:58 hiring a little clerk to manage that

04:59 ticket for you. The clerk has a buffer.

05:02 The clerk remembers whether you're

05:03 reading or writing. The clerk knows

05:05 whether you hit an end of file or an

05:07 error. The clerk batches your request so

05:09 it doesn't have to run to the kernel

05:10 window for every single bite. That

05:12 buffer is crucial. Without buffering,

05:14 calling get C in a loop would be

05:16 catastrophically expensive because every

05:18 character might require a system call. A

05:20 system call is not just a function call.

05:22 It's a controlled transition from your

05:24 program down into the operating system

05:26 kernel. It's asking the grown-ups in the

05:28 restricted area to do something

05:29 privileged on your behalf. And that's

05:31 powerful, but it's not free. So,

05:33 standard IO cheats in the best way

05:35 possible. You ask for one character. The

05:37 C library quietly reads a larger block

05:39 from the kernel into a buffer. Then the

05:41 next 100 or thousand characters can come

05:43 straight out of memory. To your program,

05:45 it still looks like you're reading a

05:47 stream one bite or one line at a time.

05:49 underneath the library is batching the

05:51 work. That's also why print f sometimes

05:54 seems haunted. If standard out is

05:56 connected to a terminal, it is often

05:57 line buffered, meaning output appears

05:59 when you print the new line. If standard

06:01 out is redirected to a file or a pipe,

06:03 it may be fully buffered, meaning it

06:05 waits until the buffer fills up or you

06:07 flush it. Standard air, meanwhile, is

06:09 usually unbuffered or at least treated

06:10 much more urgently because error

06:12 messages are supposed to appear even

06:14 when things are going wrong. This

06:16 explains one of those little bugs that

06:17 every C programmer eventually meets in a

06:19 dark alley. You print a prompt like

06:21 enter your name and then you call

06:23 something to read the input and on your

06:25 machine it works fine. But in some other

06:27 environment the prompt doesn't show up

06:29 because there was no new line. The

06:30 output got buffered and nobody flushed

06:32 it. The fix isn't mystical. You just

06:34 call f flush on standard out. That's

06:36 like telling the little clerk, stop

06:38 holding on to that. Go deliver it right

06:40 now. And once you understand that file

06:42 pointer is a buffered object sitting on

06:43 top of a lower level OS handle, a bunch

06:46 of weird behavior suddenly starts making

06:48 some sense. If you mix print f with raw

06:50 write calls on the same descriptor, you

06:52 can get surprising results because the C

06:54 library and the kernel do not

06:56 necessarily agree about what data has

06:58 been physically moved yet. If you fork a

07:00 process after printing buffered output

07:02 before flushing it, both parent and

07:04 child may inherit the same pending

07:06 buffer and suddenly a line you thought

07:08 printed once comes out twice. The

07:10 computer's not confused. You are. And I

07:12 mean that in a supportive educational

07:14 sense. Now, let's talk about the little

07:16 mode strings because they look like

07:17 little magic spells. And quite frankly,

07:19 they are. R opens an existing file for

07:22 reading. W opens a file for writing,

07:24 creating it if necessary, and truncating

07:26 if it already exists. And truncating is

07:29 a plate word for everything that used to

07:30 be there is now entirely gone. So, I

07:32 hope you meant that. A opens for

07:34 appending, creating the file first if

07:36 necessary. Then you get the variants

07:38 like R+ and W plus and A+ which allow

07:42 both reading and writing each with its

07:44 own set of rules. On Windows, we also

07:46 care deeply about binary mode. So RB and

07:49 WB matter because text mode may

07:51 translate line endings. On Unix, binary

07:54 and text mode are essentially the same

07:55 thing because Unix looked at carriage

07:57 return line feed translation and decided

07:59 it had better things to do that

08:00 afternoon. But a pen mode deserves

08:02 special attention because it's much

08:04 cooler than it looks. Most programmers

08:06 think a pen mode just means the file

08:08 position starts at the end. That would

08:10 be useful but not magical. The real

08:12 value at least on pix systems is that

08:15 append mode is normally implemented with

08:16 a kernel flag called o append. And that

08:19 means every write goes to the end of the

08:21 file at the moment the write happens.

08:23 Not when you opened it, not when you

08:24 last saw it around when the kernel

08:26 performs the write. And that distinction

08:28 is everything. Imagine two programs both

08:30 writing to the same log file. Without a

08:32 pen mode, each one might do the obvious

08:34 thing. Seek to the end, write a line.

08:37 The problem is that both can seek to the

08:38 same end before either one writes. Then

08:41 one writes its line and the other writes

08:42 its line and either leaves with it or

08:44 over top of it. And now your log file

08:45 looks like it was assembled by raccoons.

08:48 The pen mode moves the go to the end

08:50 operation into the kernel's write path.

08:52 It means the write is attached to the

08:54 current end of the file as part of the

08:55 operation. for log files, audit trails,

08:58 server traces, and anything where

09:00 multiple writers might be adding

09:01 records. This is not just convenient.

09:04 It's the difference between a log and a

09:06 crime scene. There are some caveats

09:08 because there are always some caveats.

09:10 Standard IO buffering can still split

09:12 what you think of as one logical record

09:14 into more than one lower level, right?

09:16 Network file systems have historically

09:18 had their own special collection of

09:19 gremlins. And append mode does not make

09:22 your application protocol magically

09:23 atomic, but the basic idea is still

09:26 incredibly powerful. If you want to add

09:28 to the end of a file, ask the colonel to

09:30 enforce that rule instead of trying to

09:31 fake it in user mode. Let's say you open

09:34 a file with a plus, seek back to the

09:36 beginning, read a little bit, and then

09:37 write something. Most programmers expect

09:39 the write to happen wherever they last

09:41 sought to. But in append mode, that

09:43 write still goes to the end. The file

09:46 position matters for reading. The append

09:48 rule dominates writing. And that's

09:50 exactly the kind of behavior that seems

09:52 weird until you realize it's there to

09:53 prevent a race condition. Now, so far

09:56 we've been talking about regular files.

09:58 Nice normal files. Files with names and

10:00 sizes and blocks on disk and the kind

10:02 that your file explorer understands. But

10:04 if we stop there, we would miss the best

10:06 part. Because in Unix, a path name does

10:08 not have to refer to a regular disk

10:10 file. Open dev null for writing and

10:12 every bite that you write just vanishes.

10:15 It's not a metaphorical trash can. It's

10:16 a device exposed through the file system

10:18 namespace. Your program can f open

10:21 devnull with write and get a file

10:23 pointer and happily frrint f into

10:25 oblivion. Similarly, you can open dev

10:28 zero for reading and you get an endless

10:29 stream of zero bytes, not a giant file

10:32 full of zeros, a device that produces

10:34 zeros on demand forever. Open dev/

10:37 random and you can read random bytes

10:39 from the kernel again through a filelike

10:41 interface. Open dev tty and you can talk

10:43 to the controlling terminal even if

10:45 standard input and standard output have

10:47 been redirected. It's a pretty marvelous

10:49 hack to process pipe data but still ask

10:52 the user a question because your input

10:54 string might be coming from a file. Your

10:56 output might be going to some other

10:57 program but going to dev tty says no I

11:00 mean the actual human terminal attached

11:02 to this process. So it's not often you

11:04 need it but it's invaluable when you do.

11:07 And then there's proc, which is where

11:08 the file system starts to feel like a

11:09 magician is palming cards. On many Unix

11:12 like systems, files under proc are not

11:14 ordinary files sitting on a disk. They

11:17 are views into kernel state. When you

11:19 read them, the kernel synthesizes the

11:21 contents live. You can open something

11:23 that looks like a text file and read

11:25 information about the CPU, memory,

11:26 mounts, or processes. The file is the

11:29 interface. The bites are being invented

11:31 as you ask for them. Now, when I wrote

11:33 Task Manager on Windows, to get the

11:34 information about the running processes,

11:36 you'd call antiquery system information

11:38 twice. Once to figure out how big of a

11:40 buffer you needed, and then a second

11:42 time to deliver a snapshot of the

11:43 process data. Under Unix, you simply

11:45 open a file and read it. It's a vastly

11:48 different approach, superior in some

11:49 ways, inferior in others, but inarguably

11:51 more flexible. And that's the

11:53 philosophy. Don't make every program

11:55 understand every kind of object. Make

11:57 the objects look enough like files that

11:59 existing programs can inspect, redirect,

12:02 filter, log, and compose them. And that

12:04 brings us to one of the most practical

12:06 lessons in C API design. Whenever you

12:09 can write file functions that take a

12:11 file pointer instead of a file name. A

12:13 function that takes only a file name can

12:15 only be a file by name. But a function

12:17 that takes a file pointer can read from

12:19 a file, from standard in, from a pipe,

12:21 or from a device, or from a stream that

12:23 somebody else has already prepared. It's

12:25 much more flexible because it's less

12:27 presumptuous. It does not demand to own

12:29 the plumbing. A cool little example is a

12:32 function called something like copy

12:33 stream with a file in and a file out

12:35 inside. It just reads from one stream

12:37 and writes to the other. You can use it

12:39 to copy one disk file to another. You

12:41 can use it to copy one standard input to

12:43 one standard output. You can pipe

12:45 compressed data through it. You can feed

12:47 it dev zero. You can send its output to

12:49 dev null. It's all the same code,

12:51 different plumbing. It's not merely

12:52 convenience, it's leverage. Now, there

12:54 are some more advanced relatives of F

12:56 open that probably deserve their own

12:57 episodes because each one opens another

12:59 door. There's FD open, which lets you

13:02 take an existing Unix file descriptor

13:04 and wrap it in a file pointer. That

13:06 matters because not everything starts

13:07 life from a file name. Pipes, sockets,

13:10 duplicated descriptors, and inherited

13:12 handles may already exist. With FD open,

13:15 you can say, "I have this low-level

13:16 thing. Please give me back the nice

13:18 buffered standard IO interface on top of

13:20 it." Then there's file no, which goes

13:22 the other direction. given a file

13:24 pointer unless you ask for the

13:25 underlying file descriptor which you

13:26 might need for low-level operations like

13:29 select pull uh fsync fl stuff like that.

13:34 There's also f reopen which can redirect

13:36 an existing stream like standard out or

13:38 standard air from inside the program and

13:40 that's useful for old school logging

13:42 demon setup test harnesses and programs

13:44 that want to reroute their own output

13:45 without changing every printf. There's p

13:47 open for process open which gives you a

13:49 file pointer connected to another

13:51 process. You can run a command and read

13:53 its output as though it were a file.

13:55 That's both incredibly useful and mildly

13:57 dangerous, which is how you know it

13:59 comes from Unix. And then there are

14:01 memorybacked streams, custom streams,

14:03 socket wrap streams, and all kinds of

14:04 clever machinery that prove the same

14:06 point over and over again. File pointer

14:08 is not really about disk files. It's

14:10 about streams. But we don't need to

14:12 chase all those today because the core

14:13 idea is already powerful enough. The

14:16 reason fopen matters is not that it

14:18 opens files. Lots of things open files.

14:20 The reason fopen matters is that it sits

14:22 at the boundary between a very small

14:24 programming interface and a very large

14:26 operating system idea. You ask for a

14:28 stream. The operating system in the C

14:30 runtime conspire to provide you one.

14:32 Maybe the stream comes from flash

14:33 storage, maybe from a terminal, maybe

14:35 from a pipe, maybe from a paper tape

14:37 reader, maybe from a pseudo device,

14:39 maybe from a kernel generated illusion

14:41 wearing a file name as a disguise. Your

14:43 code gets to read bytes, write bytes,

14:45 flush buffers, detect end of file, and

14:47 handle errors using the same small

14:49 vocabulary. That's not accidental.

14:51 That's design. And it is a style of

14:53 design we should still admire. Modern

14:55 software often solves problems by adding

14:57 new layers, new protocols, new object

14:59 models, new services, new formats, new

15:01 dependencies, and so on until the simple

15:03 thing is buried under a parking garage

15:05 of architecture. Unix did something

15:07 different here. It made the interface

15:09 brutally simple, and it made the world

15:10 conform to it. Not perfectly, not

15:13 universally, not without some weird edge

15:14 cases, but well enough that half a

15:16 century later, a C programmer can still

15:18 write a tiny stream processing function

15:20 and automatically make it work with

15:22 files, terminals, pipes, devices, and

15:24 things that the original author never

15:26 imagined. And that's the real magic of

15:28 FOP. It's not a big function, not a

15:31 glamorous function. Does not have a

15:32 logo, a conference, or a certification

15:34 path, or a cloud pricing calculator.

15:36 It's just a little doorway. But on the

15:38 other side of that doorway is one of the

15:40 best ideas in computing. If you can make

15:42 things look like a stream of bytes, you

15:44 can compose them. And once you see that,

15:46 then f open data with R never looks

15:48 quite so boring. Again, if you found

15:50 today's episode interesting or

15:52 entertaining, remember I'm mostly in

15:53 this for the subs and likes. So, I would

15:55 be honored if you would consider leaving

15:56 me one of each before you go today. If

15:58 you have any comments or questions on

15:59 this episode, be sure to leave them in

16:01 the comments below. And if you use a

16:02 question mark, that means Glenn will

16:04 spot it and he will pull it out and we

16:05 will talk about it on Shop Talk on

16:07 Friday or at least the best of the

16:08 questions. We try to get to them all.

16:10 Uh, make sure you check episode out and

16:13 if you like it, subscribe over there.

16:14 It's on the Dave's Attic channel and

16:16 I'll put a link up here. In the

16:17 meantime, and in between time, hope to

16:19 see you next time right here in Dave's

16:21 Garage.

16:22 >> Do it, Lynn. Do it. Do it.

