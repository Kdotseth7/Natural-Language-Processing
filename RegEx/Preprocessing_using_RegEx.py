# Preprocessing using RegEx

# Importing reqd. Libraries
import re

#Preprocessing using RegEx
list = ["This is a wolf #scary",
        "Welcome to the jungle #missing",
        "11322 the number to know",
        "Remember the name  s - John",
        "I      love      you"
        ]

for i in range(len(list)):
    list[i] = re.sub(r"\W", " ", list[i]) # Removing non-word characters by space
    list[i] = re.sub(r"\d", " ", list[i]) # Removing digits by space
    list[i] = re.sub(r"\s+[a-z]\s+", " ", list[i], flags=re.I) # Removing single characters by space
    list[i] = re.sub(r"\s+", " ", list[i], flags=re.I) # Removing multiple spaces by single space
    list[i] = re.sub(r"^\s", "", list[i], flags=re.I) # Removing spaces from start of string
    list[i] = re.sub(r"\s+$", "", list[i], flags=re.I) # Removing spaces from end of string