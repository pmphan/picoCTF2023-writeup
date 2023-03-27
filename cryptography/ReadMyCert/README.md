# ReadMyCert

## Challenge

### Description

How about we take you on an adventure on exploring certificate signing requests

Take a look at this CSR file [here](./readmycert.csr).

### Hints

1. Download the certificate signing request and try to read it.

## Solution

Just as the title say, we read the CSR file, the flag is stored in the subject field

```console
$ openssl req -in readmycert.csr -noout -subject
```

## Flag

picoCTF{read_mycert_a7163be8}
