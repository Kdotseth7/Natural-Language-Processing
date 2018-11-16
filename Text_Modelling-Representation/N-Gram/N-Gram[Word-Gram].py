# N-Gram Model [ Word Gram ]

# Importing reqd. Libraries
import random
import nltk

# Sample data
text = """Global warming or climate change has become a worldwide concern. It is gradually developing into an unprecedented environmental crisis evident in melting glaciers, changing weather patterns, rising sea levels, floods, cyclones and droughts. Global warming implies an increase in the average temperature of the Earth due to entrapment of greenhouse gases in the earth’s atmosphere."""

# Order of the grams
n = 3

# Creating n-Grams
nGrams = {}

words = nltk.word_tokenize(text)

for i in range(len(words) - n):
    gram = " ".join(words[i: i+n])
    if gram not in nGrams.keys():
        nGrams[gram] = []
    nGrams[gram].append(words[i+n]) # Word that follows the n-gram will be added to list
    
# Testing the n-Gram Model
currentGram = " ".join(words[0: n])
result = currentGram
for i in range(30):
    if currentGram not in nGrams.keys():
        break
    possibilities = nGrams[currentGram]
    nextItem = possibilities[random.randrange(len(possibilities))]
    result += " " + nextItem
    rWords = nltk.word_tokenize(result)
    currentGram = " ".join(rWords[len(rWords)-n: len(rWords)])
    
print(result)
    
