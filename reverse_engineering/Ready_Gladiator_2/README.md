# Ready Gladiator 2

## Challenge

### Description

Can you make a CoreWars warrior that wins every single round?

Your opponent is the Imp. The source is available [here](./imp.red). If you wanted to pit the Imp against himself, you could download the Imp and connect to the CoreWars server like this:

`nc saturn.picoctf.net 53907 < imp.red`

To get the flag, you must beat the Imp all 100 rounds.

### Hints

1. If your warrior is close, try again, it may work on subsequent tries... why is that?

## Solution

We can defeat the imp by using the classic imp-gate:

```
JMP 0, <-10
end
```

## Flag

picoCTF{d3m0n_3xpung3r_106bc275}

