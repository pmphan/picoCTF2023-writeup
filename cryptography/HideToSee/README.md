# HideToSee

## Challenge

### Description

How about some hide and seek heh?

Look at this image [here](./atbash.jpg).

### Hints

Download the image and try to extract it.

## Solution

We extract the image with `steghide extract -sf atbash.jpg` and get an `encrypted.txt` file which contains this string: `krxlXGU{zgyzhs_xizxp_1u84w779}`

Decipher it with Atbash cipher and we get the flag.

## Flag

picoCTF{atbash_crack_1f84d779}
