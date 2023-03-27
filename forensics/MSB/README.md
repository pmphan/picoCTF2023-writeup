# MSB

## Challenge

### Description

This image passes LSB statistical analysis, but we can't help but think there must be something to the visual artifacts present in this image...

Download the image [here](./Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png)

### Hints

1. What's causing the 'corruption' of the image?

## Solution

Following the hint given in the title, the corruption was caused because the most significant bit in each pixel was changed, similar to the LSB method.

We write [a script](./solve.py) to extract these changed bits and reassemble them into messages.

```console
$ python solve.py Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png -w decoded
$ grep pico decoded
```

## Flag

picoCTF{15_y0ur_que57_qu1x071c_0r_h3r01c_06326238}
