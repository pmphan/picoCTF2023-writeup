# Permissions

## Challenge

### Description

Can you read files in the root file?

The system admin has provisioned an account for you on the main server: `ssh -p 62157 picoplayer@saturn.picoctf.net`

Can you login and read the root file?

### Hints

1. What permissions do you have?

## Solution

```console
$ sudo -l
Matching Defaults entries for picoplayer on challenge:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User picoplayer may run the following commands on challenge:
    (ALL) /usr/bin/vi
```

We can just use `sudo vi` to access the flag file in `root`.

## Flag

picoCTF{uS1ng_v1m_3dit0r_ad091ce1}
