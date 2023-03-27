# FindAndOpen

## Challenge

### Description

Someone might have hidden the password in the trace file.

Find the key to unlock [this file](./flag.zip). [This tracefile](./dump.pcap) might be good to analyze.

### Hints

1. Download the pcap and look for the password or flag.
2. Don't try to use a password cracking tool, there are easier ways here.

## Solution

One of the Ethernet packets carries this data "VGhpcyBpcyB0aGUgc2VjcmV0OiBwaWNvQ1RGe1IzNERJTkdfTE9LZF8=", which looks roughly like a base64 encoded string. We put this through a base64 decoder to get "This is the secret: picoCTF{R34DING_LOKd_".

Use this password "picoCTF{R34DING_LOKd_" to unlock the zip file, and we get the full flag.

## Flag

picoCTF{R34DING_LOKd_fil56_succ3ss_cbf2ebf6}
