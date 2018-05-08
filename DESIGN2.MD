

Makefile  helpers.c  helpers.h  notes.c  synthesize.c  songs/  wav.c  wav.h
Understanding
Let’s read through those files in order to understand them. Moving forward, reading (and understanding!) someone else’s code, whether ours or some library’s, will often be the first step in solving a problem. That way, you can build upon the work of others and solve even more interesting problems yourself!

songs/
First open up songs/, as with cd or CS50 IDE’s file browser. In that directory are a bunch of .txt files, inside of which, it turns out, are a number of songs! Because ASCII alone doesn’t lend itself to beautiful sheet music, we’ve instead adopted for these files a "machine-readable" format for songs instead. On each line of a file is a note and duration, separated by an @. For instance, atop jeopardy.txt (which you’re welcome to open) are these lines:

G4@1/4
C5@1/4
G4@1/4
C4@1/4
G4@1/4
C5@1/4
G4@1/4
The first note in the theme song for Jeopardy is indeed a quarter note (per the 1/4), specifically a G in the fourth octave. The second note is also a quarter note, but that one’s a C in the fifth octave (a few keys to the right of the first one on a piano). Thereafter are five additional quarter notes.

Below those first seven lines in jeopardy.txt, notice, are two blank lines, the implication of which is that the seventh note is followed by two eighth rests (or, equivalently, one quarter rest). After those rests, the song resumes, resting only once more several notes later.

Make sense? Feel free to look through some of the other .txt files in songs. Cryptic though the files' lines might be at first glance, they’re really just a top-down translation of (prettier) sheet music to a machine-readable text format, machine-readable in the sense that you’re soon going to write code that reads those notes and durations!

notes.c
Next open up notes.c. In this file is a program (soon to be called notes) that not only prints the frequencies (in Hz) of all of the notes in an octave, it also outputs a WAV file (an audio file) via which you can hear those same notes. By default, it does so for the fourth octave, but if you pass it a command-line argument (a number between 0 and 8, inclusive), you can see and hear the frequencies of any octave’s notes.

Read through the comments and code in notes.c and try to understand most, if not all, of its lines. Some might look unfamiliar. For instance, by convention, it uses a function called fprintf to print error messages to stderr (aka standard error) rather than printf, which, it turns out, prints to something called stdout (aka standard output). By default, messages printed to stdout and stderr both appear on the user’s screens. But it’s possible to separate them when running a program so that users can distinguish error messages from non-error messages. But more on that perhaps another time!

Notice, too, how main returns 1 in cases of error. That, too, is a convention. To date, we’ve not returned any values from main. But, recall that, all this time, main has had a return type, specifically int. It turns out, when main is done executing, it returns 0 by default, which, by convention, signifies success. If something goes wrong in a program, though, it’s convention to return some value other than 0 (e.g., 1). That value is called an "exit code" and can be used to distinguish one type of error from another. In fact, if you’ve ever seen a cryptic error code on your Mac’s or PC’s screen, it might very well have been the value returned by some (buggy) program’s main function.

Notice too how this program uses a function called sprintf which doesn’t actually print to the screen but instead stores its output in a string (hence the s in sprintf). We’re using it in order to create a string from two placeholders, %s and %i. Notice how we allocate space for a (short) string by declaring an array for 4 chars. We then use sprintf to store a NOTES[i] (a string, ergo the %s) in that memory followed by octave (an int, ergo the %i). That way, we can take values like "A" and 4 and, effectively, concatenate them (i.e., append the latter to the former) in order to create a new string, the value of which is, for instance, A4.

Along the way in this program do we call some (presumably) unfamilar functions called song_open, frequency, note_write, and song_close. It turns out those functions are implemented in other files in this problem’s distribution. Keep an eye out for them!

synthesize.c
In this file is a program (soon to be called synthesize) that synthesizes (i.e., generates) a song from a sequence of notes. Notice how it gets those notes from a user one at a time using get_string. It first checks, though, whether the user’s input is a rest, as would happen if the user simply hits Enter. Else it proceeds to "tokenize" the user’s input into two tokens: a note, which can be found to the left of the @ in the user’s input, and a fraction, which can be found to the right of the @ in the user’s input. The program uses a function called strtok to facilitate such. It then writes that note (or rest) to a file.

wav.h
Next open up wav.h, a header file used by both notes.c and synthesize.c. This file, together with wav.c, represents not a program but a "library," a set of functions that other programs can use as building blocks, much like cs50 and stdio are libraries. This library’s code just so happens to live in your work workspace now.

In wav.h too are definitions of two new data types, one called note and one called song. But more on those (and keywords like typedef and struct another time). For now, just notice how this file declares four functions (note_write, rest_write, song_close, and song_open), which notes and synthesize use.

wav.c
In wav.c, meanwhile, are the actual implementations of those functions plus a few others. Indeed, this file contains functions that implement support for WAV files, a popular (if dated) file format for audio. Those functions allow notes and synthesize to save notes to disk in files ending in .wav. To play those .wav files, simply open them via CS50 IDE’s file browser. Or download them to your Mac or PC to play them locally.

No need to understand all of the code in wav.c, but you’re welcome to read through it if you’d like!

Makefile
Next open up Makefile, the format of which is perhaps quite different from anything you’ve seen before. As its name might suggest, it’s related to make, the program you’ve probably been using compile most of your programs, if only because compiling programs with clang itself tends to require more keystrokes. In previous problems, we’ve not needed a Makefile, which is essentially a configuration file for make, since make can infer how to compile a program that’s composed of a single file (e.g., hello.c). But compiling both notes and synthesize requires multiple files, since both programs rely on wav.h and wav.c, plus two other files, helpers.h and helpers.c.

Simply executing

make notes
or

make synthesize
wouldn’t provide nearly enough information for make to be able to infer which files it needs. So this Makefile exists so that make knows how to compile these programs.

helpers.h
In this file, now, are declarations for three functions:

duration, which should take as input as a string a fraction (e.g., 1/4) and return as an int a corresponding number of eigths (2, in this case, since 1/4 is equivalent to 2/8);

frequency, which should take as input as a string a note formatted as

XY (e.g., A4), where X is any of A through G and Y is any of 0 through 8, or

XYZ (e.g., A#4), where X is any of A through G, Y is # or b, and Z is any of 0 through 8,

and return as an int the note’s corresponding frequency, rounded to the nearest integer; and

is_rest, which should return true if its input, a string, represents a rest in our machine-readable format, otherwise false.

helpers.c
And in this file there should be implementations of those three functions, but no! Not yet. That’s where you come in!

Specification
bday.txt
In bday.txt, type the ASCII representation of Happy Birthday, translating its sheet music, above, to the machine-readable representation prescribed herein. You should find that the song begins with:

D4@1/8
D4@1/8
E4@1/4
D4@1/4
G4@1/4
F#4@1/2
helpers.c
is_rest
Complete the implementation of is_rest in helpers.c. Recall that blank lines represent rests in our machine-readable format. And recall that synthesize will call this function in order to determine if one of the lines a user has typed in is indeed blank.

What does it mean for a line to be blank? To answer that question, start by looking at cs50.h itself, wherein get_string is documented:

https://github.com/cs50/libcs50/blob/develop/src/cs50.h

What do the comments atop get_string say that the function returns if a user simply hits Enter, thereby inputting only a "line ending" (i.e., \n)?

When is_rest is subsequently passed such a string, s, how should it (nay, you!) recognize as much?

duration
Complete the implementation of duration in helpers.c. Recall that this function should take as input as a string a fraction and convert it into some integral number of eighths. You may assume that duration will only be passed a string formatted as X/Y, whereby each of X and Y is a positive decimal digit, and Y is, moreover, a power of 2.

frequency
Finally, complete the implementation of frequency in helpers.c. Recall that this function should take as input as a string a note (e.g., A4) and return its corresponding frequency in hertz as an int.

And recall that:

The frequency, f, of some note is 2n/12 × 440, where n is the number of semitones from that note to A4.

Each key on a piano is said to be one semitone, otherwise known as a half step, away from its adjacent neighbor, whether white or black.

The effect of # and b, otherwise known as accidentals, is to raise or lower, respectively, the pitch of a note by one semitone.

In implementing this function, you might find pow and round, both declared in math.h, of interest.