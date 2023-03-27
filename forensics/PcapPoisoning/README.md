# PcapPoisoning

## Challenge

### Description

How about some hide and seek heh?

Download this [file](./trace.pcap) and find the flag.

### Hints

(None)

## Solution

Most of the packets are useless, but one of them contains the flag in plaintext. We can isolate this packet by filtering by `frame contains "picoCTF"`.

## Flag

picoCTF{P64P_4N4L7S1S_SU55355FUL_4d72dfcc}
