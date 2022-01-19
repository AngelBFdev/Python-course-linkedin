#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

secret = 'swordfish'
pw = ''
auth = False
count = 0
max_attempt = 5

while pw != secret:
    # input to get text
    count +=1
    if count > max_attempt: break
    # continue skip this case like next in ruby
    if count == 3: continue
    pw = input(f"{count}What's the secret word? ")

# else statement after a loop will only be
# executed when finished correctly
else:
    auth=True

print("Authorized" if auth else "Calling the FBI ...")
