# No way out

## Challenge

### Description

Put this flag in standard picoCTF format before submitting. If the flag was h1_1m_7h3_f14g submit picoCTF{h1_1m_7h3_f14g} to the platform.

### Hints

(None)

## Solution

The game said to escape and reach the flag to find the flag, so what I did was decompiling the `pico_Data/Managed/Assembly-CSharp.dll` file with dnSpyEx, and then modify the variable to allow the user to climb onto the ladder.

The flag is actually also viewable in plaintext in the `level0` file, but it's not in standard flag format so it's a lot harder to tell.

## Flag

picoCTF{welcome_to_unity!!}
