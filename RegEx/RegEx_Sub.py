# RegEx_Intro - Sub

# Importing reqd. Libraries
import re

sentence = "I love Avengers"
print(re.sub(r"Avengers", "Justice League", sentence)) # I love Justice League
# -----------------------------------------------------------------------------------------
sent = "I love Avengers Avengers"
print(re.sub(r"Avengers", "Justice League", sent)) # I love Justice League Justice League
# -----------------------------------------------------------------------------------------
sent = "I love Avengers Avengers"
print(re.sub(r"[a-z]", "0", sent)) # I 0000 A0000000 A0000000
# -----------------------------------------------------------------------------------------
sent = "I love Avengers Avengers"
print(re.sub(r"[a-z]", "0", sent, flags=re.I)) # 0 0000 00000000 00000000 (Case-Insensitive)
# -----------------------------------------------------------------------------------------
sent = "I love Avengers Avengers"
print(re.sub(r"[a-z]", "0", sent, flags=re.I)) # 0 0000 00000000 00000000 (Case-Insensitive)
# -----------------------------------------------------------------------------------------
sent = "I love Avengers Avengers"
print(re.sub(r"Avengers", "0", sent, count=1, flags=re.I)) # I love 0 Avengers