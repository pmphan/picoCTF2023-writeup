# Special

## Challenge

### Description

Don't power users get tired of making spelling mistakes in the shell? Not anymore! Enter Special, the Spell Checked Interface for Affecting Linux. Now, every word is properly spelled and capitalized... automatically and behind-the-scenes! Be the first to test Special in beta, and feel free to tell us all about how Special streamlines every development process that you face. When your co-workers see your amazing shell interface, just tell them: That's Special (TM)

Start your instance to see connection details.

`ssh -p 50429 ctf-player@saturn.picoctf.net`

The password is `483e80d4`

### Hints

1. Experiment with different shell syntax

## Solution

The shell auto capitalize the first word and spell correct any commands, which is a pain, but it means we can still use `cat`, and if we manage to skip the first word then `cat` wouldn't be auto capitalize.

The syntax I use is `""; cat <file>`.

```console
$ "" | cat *
I | cat * 
sh: 1: I: not found
cat: blargh: Is a directory
```

This tells us there is a `blargh` directory.

```console
$ ""; cat blargh/*
""; cat blargh/* 
sh: 1: : Permission denied
picoCTF{5p311ch3ck_15_7h3_w0r57_b741d1b1}
```

## Flag

picoCTF{5p311ch3ck_15_7h3_w0r57_b741d1b1}
