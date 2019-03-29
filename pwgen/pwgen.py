#!/usr/bin/env python
from flask import Flask
from xkcdpass import xkcd_password as xp

app = Flask(__name__)

@app.route("/")
def hello():

  password = xp.generate_xkcdpassword(xp.generate_wordlist())

  try:
    with open("/volume/password.txt", "r") as fh:
        password = fh.readlines()[0]
  except:
    with open("/volume/password.txt", "w") as fh:
      fh.write(password)
 
  return password
