# Ready Gladiator 1

## Challenge

### Description

Can you make a CoreWars warrior that wins?

Your opponent is the Imp. The source is available [here](./imp.red). If you wanted to pit the Imp against himself, you could download the Imp and connect to the CoreWars server like this:

`nc saturn.picoctf.net 63671 < imp.red`

To get the flag, you must beat the Imp at least once out of the many rounds.

### Hints

1. You may be able to find a viable warrior in beginner docs

## Solution

We can defeat the imp by using the classic imp-gate:

```
JMP 0, <-10
end
```

## Flag

picoCTF{1mp_1n_7h3_cr055h41r5_dba6f40d}
