# Shorthand Character Classes

# Importing reqd. Libraries
import re

sent1 = "Welcome to the year 2018"
sent2 = "Just ~% ++++---- arrived at @Jack's place. #fun"
sent3 = "I           love            football"

sent1_modified = re.sub(r"\d", "", sent1 )

sent2_modified = re.sub(r"[~%+\-@#'\.]", "", sent2 )

sent2_modified2 = re.sub(r"\w", "", sent2 ) # \w - [a-zA-Z0-9]

sent2_modified2 = re.sub(r"\W", " ", sent2 ) # \W - [^a-zA-Z0-9]

sent2_modified2_modified = re.sub(r"\s+", " ", sent2_modified2 ) # Replaces one or more whitespace by single whitespace

sent2_modified2_modified2 = re.sub(r"\s[a-z]\s", " ", sent2_modified2_modified, flags=re.I )

sent3_modified = re.sub(r"\s+love\s+", " hate ", sent3)