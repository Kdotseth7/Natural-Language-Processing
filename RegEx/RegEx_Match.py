# RegEx_Intro - Match

# Importing reqd. Libraries
import re 

sentence = "pac was a killer Lyricist"
word1 = "ab"
word2 = "a"

re.match(r".*", sentence)

re.match(r".+", sentence)

re.match(r"[a-zA-Z]+", sentence) # pac

re.match(r"ab?", word1) # ab

re.match(r"ab?", word2) # a