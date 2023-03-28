# Virtual Machine 0

## Challenge

### Description

Can you crack this black box?

We grabbed this design doc from enemy servers: [Download](./Virtual-Machine-0.zip). We know that the rotation of the red axle is input and the rotation of the blue axle is output. The following input gives the flag as output: [Download](./input.txt).

### Hints

1. Rotating the axle that number of times is obviously not feasible. Can you model the mathematical relationship between red and blue?

## Solution

Opening the file in Blender and remove all the black box, we see two gears. The gear ratio is `40/8 = 5`. The input is

`39722847074734820757600524178581224432297292490103995908738058203639164185`

The output is the input times 5, which is

`198614235373674103788002620892906122161486462450519979543690291018195820925`.

We convert this number to hex, which gives

`7069636F4354467B67333472355F30665F6D3072335F33353337653530617D`

We convert this again to ASCII, giving

picoCTF{g34r5_0f_m0r3_3537e50a}

## Flag

picoCTF{g34r5_0f_m0r3_3537e50a}
