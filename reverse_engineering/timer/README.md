# timer

## Challenge

### Description

You will find the flag after analysing this apk

Download [here](./timer.apk).

### Hints

1. Decompile
2. mobsf or jadx

## Solution

Decompile the apk file with jadx. After decompiling we get a lot of files but we can quickly find the flag in picoCTF{} format with `grep` or `ripgrep`. `ripgrep` is a lot faster.

## Flag

picoCTF{t1m3r_r3v3rs3d_succ355fully_17496}"
