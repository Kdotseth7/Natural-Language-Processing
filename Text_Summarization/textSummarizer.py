# Text Summarization -> Wikipedia Article Summarizer

import nltk
import urllib
import bs4 as bs # Beautiful Soup 4
import re
import heapq
nltk.download("stopwords")

# Getting the data
source = urllib.request.urlopen("https://en.wikipedia.org/wiki/Cristiano_Ronaldo").read()
soup = bs.BeautifulSoup(source, "lxml") # parsed source

text = ""
for paragraph in soup.find_all("p"): # extracting the text from <p> tag of wikipedia page source
    text += paragraph.text
    
# Pre-processing the text
text = re.sub(r"\[[0-9]*\]", " ", text) # For creating the "Summary"
text = re.sub(r"\s+", " ", text)
clean_Text = text.lower() # For creating the "Histogram"
clean_Text = re.sub(r"\W", " ", clean_Text)
clean_Text = re.sub(r"\d", " ", clean_Text)
clean_Text = re.sub(r"\s+", " ", clean_Text)

# Tokenizing the sentence into sentences
sentences = nltk.sent_tokenize(text)

# Adding all stopwords to a list
stop_Words = nltk.corpus.stopwords.words("english")

# Histogram
word2Count = {}
for word in nltk.word_tokenize(clean_Text):
    if word not in stop_Words:
        if word not in word2Count.keys():
            word2Count[word] = 1
        else:
            word2Count[word] += 1
            
# Weighted Histogram
for key in word2Count.keys():
    word2Count[key] = word2Count[key] / max(word2Count.values())

sent_Score = {}
for sentence in sentences:
    for word in nltk.word_tokenize(sentence.lower()):
        if word in word2Count.keys():
            if len(sentence.split(" ")) < 15: # We only want smaller length sentences
                if sentence not in sent_Score.keys():
                    sent_Score[sentence] = word2Count[word]
                else:
                    sent_Score[sentence] += word2Count[word]

# Summary                
best_Sentences = heapq.nlargest(15, sent_Score, sent_Score.get)  
print("-------------------------------------------------------------------")
for sentence in best_Sentences:
    print(sentence)