# Ready Gladiator 0

## Challenge

### Description

Can you make a CoreWars warrior that always loses, no ties?

Your opponent is the Imp. The source is available [here](./imp.red). If you wanted to pit the Imp against himself, you could download the Imp and connect to the CoreWars server like this: 

`nc saturn.picoctf.net 56752 < imp.red`

### Hints

1. CoreWars is a well-established game with a lot of docs and strategy
2. Experiment with input to the CoreWars handler or create a self-defeating bot

## Solution

Lose by doing nothing.

```console
$ echo "end" | nc saturn.picoctf.net 56752
```

## Flag

picoCTF{h3r0_t0_z3r0_4m1r1gh7_a7bf8a57}
