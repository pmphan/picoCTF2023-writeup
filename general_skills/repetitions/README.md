# repetitions

## Challenge

### Description

Can you make sense of this file?

Download the file [here](./enc_flag).

### Hints

1. Multiple decoding is always good.

## Solution

It's a base64 encoded string, after we decode it we get another base64 string. Essentially we have to decode it multiple times.

### You can use the below bash script to automate the process:

```
#!/usr/bin/env bash

if [[ $# -eq 1 && -f "$1" ]]; then

	result=$(cat "$1")
	count=0

        while true; do
                if [[ $result == "picoCTF{"* ]]; then
                        echo "Flag: $result"
                        echo "[!] You would have to decode this manually $count times to reach the flag."
                        break
                else
                        decoded=$(base64 -d <<< "$result" 2>/dev/null)
                        if [[ $? -eq 0 ]]; then
                            result=$decoded
                            (( count++ ))
                        else
                            echo "[-] Error: Input is not valid Base64."
                            exit 1
                        fi
                fi
        done
else
	echo "[-] Store the Base64-encoded string in a file."
        echo "Usage: $0 <filename>"
        exit 1
fi
```

## Flag

picoCTF{base64_n3st3d_dic0d!n8_d0wnl04d3d_4557ec3e}
