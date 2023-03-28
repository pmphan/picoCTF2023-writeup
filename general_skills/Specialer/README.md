# Specialer

## Challenge

### Description

Reception of Special has been cool to say the least. That's why we made an exclusive version of Special, called Secure Comprehensive Interface for Affecting Linux Empirically Rad, or just 'Specialer'. With Specialer, we really tried to remove the distractions from using a shell. Yes, we took out spell checker because of everybody's complaining. But we think you will be excited about our new, reduced feature set for keeping you focused on what needs it the most.

Please start an instance to test your very own copy of Specialer.

`ssh -p 64459 ctf-player@saturn.picoctf.net`.

### Hints

1. What programs do you have access to?

## Solution

No more access to `cat`, but we can still use `echo`. Use `echo *` to explore the directory and `echo $(<filename)` to print out content of the file.

```console
$ echo *
abra ala sim
$ echo ala/*
ala/kazam.txt ala/mode.txt
$ echo $(<ala/kazam.txt) 
return 0 picoCTF{y0u_d0n7_4ppr3c1473_wh47_w3r3_d01ng_h3r3_c42168d9}
```

## Flag

picoCTF{y0u_d0n7_4ppr3c1473_wh47_w3r3_d01ng_h3r3_c42168d9}
