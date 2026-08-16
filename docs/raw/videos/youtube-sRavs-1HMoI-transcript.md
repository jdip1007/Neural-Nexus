---
source_url: https://www.youtube.com/watch?v=sRavs-1HMoI
source_type: video
ingested: 2026-08-16
published: 2026-08-16
duration_minutes: 15
language: en
sha256: 71b1c5efdedcae13de27a37af5f75d4b7dfb1d741dd3bf08fa2eef1c53afd890
time_sensitive: True
---

# YouTube Transcript: Cicada 3301: The Internet's Greatest Mystery!

## Video Information
- **Title**: Cicada 3301: The Internet's Greatest Mystery!
- **Video ID**: sRavs-1HMoI
- **Published**: Unknown
- **Views**: Unknown
- **Language**: en

## Transcript
00:00 On January 5th, 2012, the following cryptic 
message was posted in the paranormal section

00:05 of an infamous Internet message board. 
Hello. We 
are looking for highly intelligent individuals.

00:11 To find them, we have devised a test. There 
is a message hidden in the image. Find it,

00:17 and it will lead you on the road to finding 
us. 
We look forward to meeting the few

00:22 who will make it all the way through. 
Good luck. 
3301.
And so would begin the most complex and

00:30 maddeningly difficult challenge that the Internet 
had ever seen. While at first some wrote it off

00:35 as a clever marketing stunt, over the span of 
the next ten years it would become increasingly

00:40 clear that it could be no such thing. But what, 
then, could it be? Who, or what, was 3301?

00:47 Many speculated that the whole thing was a 
recruiting tool for an intelligence agency

00:50 like the NSA, CIA, or MI6. Others believed that 
perhaps it was a secret society or cult, but why

00:58 then the need for complex skills in steganography, 
cryptography, mathematics and so on? And what was

01:04 the purpose? Where did it lead to, and how far 
would it take those who followed the trail?

01:08 And to what end? Many would become obsessed with 
finding out.  
Where individuals would fail,

01:14 groups would form, bringing their collective power 
and expertise to bear on solving the puzzles.

01:19 But that always runs the risk of one individual 
in the group going rogue with a discovery.

01:23 Based on recently leaked information that 
appears to bear the correct PGP signature,

01:28 it would appear that at least one person succeeded 
in solving the riddle of 3301. But who or what,

01:34 precisely, did they find? All that and more 
today, right here in Dave's Garage.
[Intro]

01:46 I'm Dave Plummer, a retired software engineer from 
Microsoft going back to the MS-DOS and Windows 95

01:52 days, and today we're investigating the one of the 
greatest technological mysteries that the world

01:56 had ever seen: Cicada 3301.
It all began with that 
simple JPEG image posted to the web. It claimed to

02:04 contain a secret message, but how, and where? The 
file posted that day appeared to be a simple JPG

02:09 image, but hidden away within it was plain text, 
easily extracted from the file with Unix "strings"

02:15 command. When run upon the image, it revealed 
a messages string that contained a reference to

02:20 TIBERIVS CLAVDIVS CAESAR followed by text 
that had clearly been scrambled by encryption.

02:25 But what kind of encryption?
The reference to 
Caesar implied that this was likely a simple

02:30 "Caesar Cipher", wherein each letter is offset by 
some number within the alphabet, or in this case,

02:34 ASCII code. If offset by 3, then A becomes D, 
B becomes E, and so on. A few iterations of the

02:42 cipher solver reveals that, sure enough, in the 
3301 image each letter is offset by 4, and once

02:49 corrected, the result is a URL to an image hosting 
site.
Each step was getting slightly harder,

02:55 and this trend would continue until the challenges 
became maddeningly obscure and difficult - and yet

03:01 some would persevere, even through the Mayan 
alphabet, disappearing ink, ancient poetry

03:05 and cryptic ruins.
Loading the linked image into 
the web browser, we get an image of a duck. More

03:11 specifically, a decoy duck, and one that openly 
admits to being a decoy at that:
The text on the

03:17 message reads "Looks like you can't guess how to 
get the message out". This text is actually our

03:22 one and only clue: combining guess and out to 
yield the name of the outguess tool, a program

03:27 that is able to hide and retrieve information that 
has been intentionally hidden within an image.

03:32 By changing a mathematically predictable set of 
pixels by tiny subtle amounts, the tool is able

03:37 to encode data within an image that can't be 
seen by the naked eye.
As a contrived example,

03:43 let's say we decided to hide text in an image by 
offsetting the blue value in every 131st pixel

03:48 up or down by one bit depending on whether 
we were trying to store a one or a zero.

03:53 Because we're changing the least significant bit 
of the color least sensitive to the human eye,

03:58 it's going to be entirely imperceptible in most 
non-trivial images. And that's basically how

04:01 steganography hides data inside of an image in a 
manner that's hard to detect. The outguess tool

04:03 applies a number of techniques to extract that 
hidden data for you automatically.
And indeed,

04:08 using the outguess tool we can extract a 
character string from the duck decoy's image:

04:12 "Here is a book code. To find 
the book, and more information,

04:16 go to https://www.reddit.com/r/a2e7j6ic78h0j/"
 
Apparently, the next stage of the clue was hidden

04:22 within the subreddit. The header contained a 
numeric code of some kind and a picture of a

04:26 welcome mat. By applying outguess again, we would 
receive perhaps the single most important piece of

04:31 information that 3301 would encode: it's public 
PGP key.
A PGP key is a private-public keypair.

04:40 Only the person with the private key can 
generate messages that will have a signature

04:43 that matches the public key. Thus, you can 
send the public key out freely and then anyone

04:48 at any point can use it to verify that a signed 
message you later send out MUST have been signed,

04:53 with mathematical certainty, by whomever possessed 
the original private key. Put more simply,

04:59 it's a foolproof manner of verifying that a 
message really did come from a particular sender.

05:04 And it meant that from this point forward, no one 
could pretend to be 3301. Only the person truly

05:10 in possession of the official 3301 private 
key could send officially signed messages,

05:15 so it became impossible for anyone else to 
impersonate 3301.
A second image on the subreddit

05:21 also contained a steganographic payload that could 
be extracted with outguess. The message read:
"The

05:26 key has always been right in front of your eyes.
 
This isn't the quest for the Holy Grail. 
Stop

05:31 making it more difficult than it is.
Good luck.
 
3301"
The subreddit also contained encrypted

05:39 text messages, which were found to be a Vigenere 
cipher, where 0 is A, 1 is B, 2 is C, and so on.

05:46 Decoding the text in the subreddit revealed 
an ancient English tale by Thomas Bullfinch

05:50 on King Arthur and his quest for the Holy 
Grail. The original subreddit message header,

05:55 when translated from Mayan, is the key to use with 
the cipher.  
It all decoded to a phone number,

06:00 214-390-9608. When called, that 
number played the following message.

06:37 Besides pointing out that the group's numeric 
name was, in fact, prime in its own right,

06:41 this message sent investigators on a quick hunt 
to find two more prime numbers hidden somewhere

06:46 in the image. A few quickly noted that the 
height and width of the image, 509 and 503,

06:52 were also prime numbers. Combined and multiplied 
with 3301, they would yield the number 845145127.

07:00 With a .com appended, it led them to a website 
that contained an image of a Cicada and a

07:05 countdown timer.
With outguess applied to the 
cicada image, the follow message was revealed:

07:10 "You have done well to come this far.
 
Patience is a virtue.
Check back at 17:00

07:16 UTC.
3301"
Everyone following the puzzle was now 
confronted with the same fate: waiting for the

07:19 countdown timer to expire. It was apparently a way 
to start the race anew, with everyone at the same

07:19 point. What happened next would solidify 3301's 
reputation as an international group and largely

07:20 eliminate the possibility that this was all a 
ruse created by a single hacker.
Was the image

07:21 of the cicada important? An interesting fact about 
cicadas is that while there are over 1500 species,

07:27 they generally gestate underground for periods of 
7, 13, or 17 years. The most popular theory has

07:34 been that this is to eliminate competition amongst 
cicadas by reducing the frequency of how often

07:38 their various gestation periods would overlap with 
each other. Others have advanced the theory that

07:44 a prime gestation period would overlap less often 
with predators that emerged on a 2-year, 3-year,

07:48 or 4-year cycle, for example.  
Regardless of what 
evolutionary pressure led to the prime gestation

07:53 periods, it is likely that this characteristic - 
the prime numbers associated with the gestation

07:58 period - is why 3301 has used cicada imagery. 
Primes are incredibly important to cryptography.

08:21 When the countdown timer reached zero, the 
image changed. It now contained 14 pairs of

08:26 GPS coordinated scattered around the globe: 
California, Australia, Hawaii, South Korea,

08:32 Poland, and many more. In each of those 
physical locations could be found a poster,

08:37 in plain view, that contained an image of a 
cicada and a QR code.
The sudden appearance and

08:53 world-wide distribution of the posters meant that 
at a minimum, cicada was a broadly distributed

08:58 group. Those who believed that 3301 might simply 
be a few hackers in the basement now were faced

09:04 with the reality that at a minimum, 3301 had the 
resources to make a physical appearance in 14

09:09 international locations within a reasonably short 
time period.
But how short? Assuming the posters

09:15 might last a week or two, they would have to 
be all placed within that time limit. A careful

09:20 analysis of the GPS locations reveals that most 
of the locations are within 90 minutes drive an

09:25 international airport, but this is true for most 
urban centers.
It also meant that the puzzle was

09:30 now going "off the grid", or at least offline. 
To continue meant the solvers would have to

09:35 venture out into the real world.
There were two 
variants of the poster. The QR code on the poster

09:40 led to an image from which could be extracted 
a riddle and taken as a whole they contained

09:43 new book ciphers and a curious admonition:
"You've 
shared too much to this point.  
We want the best,

09:50 not the followers.  
Thus, the first few there 
will receive the prize.
Good luck.
3301"

09:57 There was only one problem: the book ciphers 
were plain enough except that the messages never

10:02 indicated to WHICH books the ciphers should 
be run. The hunt was now on to find the very

10:06 books which would contain the encoded message. It 
would take centuries to do so by hand in even a

10:11 modest library, but thanks to the power of the 
internet and modern search, both were found in

10:16 reasonably short order.
The first was found 
to be Encyclopaedia Britannica, 11th Edition,

10:21 Volume 6, Slice Number 3. The second book was 
even more obscure: though written by popular

10:27 author William Gibson, the book Agrippa was 
only released in a book printed in disappearing

10:32 ink and on self-erasing 3.5 inch floppy disc 
back in 1992...and no, I'm not kidding. The book

10:36 was literally printed on photosensitive paper, 
whose pages, when exposed to light even a single,

10:42 would the fade to nothingness. The floppy would 
entirely encrypt itself after a single use.

10:47 The result of these puzzles was a link to a page 
on the web. But it was Tor link, meaning it was a

10:53 link to the Dark Web. The Dark Web, for lack of a 
more thorough explanation, is largely encrypted,

10:59 secret, and unindexed. You generally don't surf 
it, you go directly to it for a particular page.

11:04 The reasons for a page's existence on the dark 
web range from a severe need for privacy to pretty

11:09 much every illegal activity imaginable. You can't 
get there accidentally with a regular web browser,

11:14 in fact. You need special software such as the 
Tor browser.
The Tor link led to a message that

11:19 read:
"Congratulations!
Please create a new email 
address with a public, free, web-based service.

11:26 Once you've never used before, and enter it below. 
We recommend you do this while still using Tor,

11:32 for anonymity.
3301"
It further explained 
where to send the email, but shortly after,

11:37 the message was replaced the following:
 
"We want the best, not the followers."

11:45 Those who did so promptly received an email that 
lead to a page that contained an image of artwork.

11:50 That artwork contained a message with a link that 
purported to offer latecomers a second chance.

11:55 It also contained text that encoded another Tor 
link, which, via a series of prime numbers and

11:59 other puzzles, ultimately led to an audio file, 
known as a MIDI file.
The musical contents of

12:05 the audio file seem unimportant, but the MIDI file 
contents could be laboriously decoded to produce

12:10 the next message:
"Very good. You have proven 
to be most dedicated to come this far to attain

12:16 enlightenment. Create a gpg key for your email 
address and upload it to the mit key servers

12:22 then encrypt the following word list."
It also 
provided a gmail address to send the encrypted

12:28 results to. Those who did so promptly were 
provided with an interesting amonition by email.

12:33 "Each person who has come this far has received 
a unique message encrypted with a unique key. You

12:40 are not to collaborate. Sharing your message or 
key will result in not receiving the next step."

12:46 Those whom were selected were also provided 
with a Tor link, this time to login page.

12:51 For the vast majority, as far as we know, 
this is where the trail went cold.

12:55 Once month later, the following 
message appeared on the subreddit.

12:59 "We have now found the individuals we sought. 
Thus our month-long journey ends. 
For Now.

13:05 Thank-you for your dedication and effort. If 
you were unable to complete the test, or did not

13:10 receive an email, do not despair.
There will be 
more opportunities like this one.
Thank you all.

13:17 3301."
A select few, however, received the 
following explanation. In at least one case

13:23 it was leaked to the web, which is how we know 
of its existence.
"We are not a hacker group.

13:29 We do not engage in illegal activity, nor do our 
members. If you are engaged in illegal activity,

13:35 we ask that you cease any and all illegal 
activities or decline membership at this time.

13:40 We will not ask questions if you decline. 
However, if you lie to us, we will find out."

13:47 "You are undoubtedly wondering what it is that 
we do. We are much like a think tank, in that

13:53 our primary focus is on researching and developing 
techniques to aid the ideas we advocate: liberty,

14:00 privacy, security."
Next, it produced 
three questions to be answered by email:

14:07 "Do you believe that every human being has 
a right to privacy and anonymity?"
"Do you

14:12 believe that information should be free?"
"Do 
you believe that censorship harms humanity?"

14:19 Nothing more was heard from 3301. That 
is until precisely one year later, when,

14:25 on the anniversary of their original 
image, the next puzzle appeared.

14:40 Make sure you're subscribed to my channel for 
part 2, where we learn about the encypted Liber

14:50 Primus and the man who ultimately cracked 
the 3301 puzzle and was offered a chance

14:51 to join.
All next time, right 
here in Dave's Garage.

15:12 [https://votiro.com/blog/image-steganography-example-how-i-created-an-attack/]

