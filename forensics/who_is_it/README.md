# who is it

## Challenge

### Description

Someone just sent you an email claiming to be Google's co-founder Larry Page but you suspect a scam.

Can you help us identify whose mail server the email actually originated from?

Download the email file here. Flag: picoCTF{FirstnameLastname}

### Hints

1. whois can be helpful on IP addresses also, not only domain names.

## Solution

Reading through the provided file, the IP of this guy is 173.249.33.206. Then we use `whois 173.249.33.206` like the hint says.

## Flag

picoCTF{WilhelmZwalina}
