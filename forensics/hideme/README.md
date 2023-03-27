# hideme

## Challenge

### Description

Every file gets a flag.

The SOC analyst saw one image been sent back and forth between two people.

They decided to investigate and found out that there was more than what meets the eye [here](./flag.png).

### Hints

(None)

## Solution

zsteg tells us that there are ZIP archive file tacked onto the end of this file here.

```console
$ zsteg flag.png 
[?] 3319 bytes of extra data after image end (IEND), offset = 0x9b3b
extradata:0         .. file: Zip archive data, at least v1.0 to extract, compression method=store
```

Simply run `unzip flag.png` and we get the ZIP folder, which contains a flag.png file with the flag in image forn.

## Flag

picoCTF{Hiddinng_An_imag3_within_@n_ima9e_85e04ab8}
