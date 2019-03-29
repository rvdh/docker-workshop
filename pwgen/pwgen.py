#!/usr/bin/env python
from xkcdpass import xkcd_password as xp

password = xp.generate_xkcdpassword(xp.generate_wordlist())
print(password)
