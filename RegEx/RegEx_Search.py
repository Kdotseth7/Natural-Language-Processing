# RegEx_Intro - Search

# Importing reqd. Libraries
import re

sentence = "1996 was the year when i was born"

re.match(r"[a-zA-Z]+", sentence) # no o/p

re.search(r"[a-zA-Z]+", sentence) # was

#Starts with
if re.search(r"^1996", sentence):
    print("Match")
else:
    print("No Match")

#Ends with
if re.search(r"born$", sentence):
    print("Match")
else:
    print("No Match")