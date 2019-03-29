#!/usr/bin/env python
from xkcdpass import xkcd_password as xp

password = xp.generate_xkcdpassword(xp.generate_wordlist())

with open("/volume/password.txt", "w") as fh:
  fh.write(password)

print(password)
