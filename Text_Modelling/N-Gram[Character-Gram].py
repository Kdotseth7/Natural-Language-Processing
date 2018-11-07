# N-Gram Model [ Character Gram ]

# Importing reqd. Libraries
import random

# Sample data
text = """Global warming or climate change has become a worldwide concern. It is gradually developing into an unprecedented environmental crisis evident in melting glaciers, changing weather patterns, rising sea levels, floods, cyclones and droughts. Global warming implies an increase in the average temperature of the Earth due to entrapment of greenhouse gases in the earth’s atmosphere."""

# Order of the grams
n = 5

# Creating n-Grams
nGrams = {}

for i in range(len(text) - n):
    gram = text[i: i+n]
    if gram not in nGrams.keys():
        nGrams[gram] = []
    nGrams[gram].append(text[i+n]) # Character that follows the n-gram will be added to list
    
# Testing the n-Gram Model
currentGram = text[0:n]
result = currentGram
for i in range(100):
    if currentGram not in nGrams.keys():
        break
    possibilities = nGrams[currentGram]
    nextItem = possibilities[random.randrange(len(possibilities))]
    result += nextItem
    currentGram = result[len(result) - n: len(result)]
    
print(result)
    