# TF-IDF[Term Frequency - Inverse Document Frequency]

# Importing reqd. Libraries
import nltk
import re
import heapq
import numpy as np

paragraph = """Thank you all so very much. Thank you to the Academy.
               Thank you to all of you in this room. I have to congratulate 
               the other incredible nominees this year. The Revenant was 
               the product of the tireless efforts of an unbelievable cast
               and crew. First off, to my brother in this endeavor, Mr. Tom 
               Hardy. Tom, your talent on screen can only be surpassed by 
               your friendship off screen … thank you for creating a t
               ranscendent cinematic experience. Thank you to everybody at 
               Fox and New Regency … my entire team. I have to thank 
               everyone from the very onset of my career … To my parents; 
               none of this would be possible without you. And to my 
               friends, I love you dearly; you know who you are. And lastly,
               I just want to say this: Making The Revenant was about
               man's relationship to the natural world. A world that we
               collectively felt in 2015 as the hottest year in recorded
               history. Our production needed to move to the southern
               tip of this planet just to be able to find snow. Climate
               change is real, it is happening right now. It is the most
               urgent threat facing our entire species, and we need to work
               collectively together and stop procrastinating. We need to
               support leaders around the world who do not speak for the 
               big polluters, but who speak for all of humanity, for the
               indigenous people of the world, for the billions and 
               billions of underprivileged people out there who would be
               most affected by this. For our children’s children, and 
               for those people out there whose voices have been drowned
               out by the politics of greed. I thank you all for this 
               amazing award tonight. Let us not take this planet for 
               granted. I do not take tonight for granted. Thank you so very much."""

# STEP-1 : Collect Data and Pre-process it
               
dataset = nltk.sent_tokenize(paragraph)

for i in range(len(dataset)):
    dataset[i] = dataset[i].lower() # Convert text into Lowercase
    dataset[i] = re.sub(r"\W"," ", dataset[i]) # Substitute non-word characters by a space
    dataset[i] = re.sub(r"\s+"," ", dataset[i]) # Substitute multi-spaces by a single space
    
# STEP-2 : Create HISTOGRAM using Vocabulary using Word Tokenization
    
word2count = {}  # Creating Vocabulary using a Dictionary[has key to value mappings]
for data in dataset:
    words = nltk.word_tokenize(data)
    for word in words:
        if word not in word2count.keys():
            word2count[word] = 1
        else:
            word2count[word] +=1
            
freqWords = heapq.nlargest(100, word2count, key = word2count.get) # 100 most frequent words in dataset

# STEP-2(i) : TF Matrix

tf_matrix = {}
for word in freqWords:
    doc_tf = []
    for data in dataset:
        frequency = 0
        for w in nltk.word_tokenize(data):
            if w == word:
                frequency +=1
        tf_word = frequency/len(nltk.word_tokenize(data))
        doc_tf.append(tf_word)
    tf_matrix[word] = doc_tf

# STEP-2(ii) : IDF Matrix

word_idfs = {}
for word in freqWords:
    docCount = 0
    for data in dataset:
        if word in nltk.word_tokenize(data):
            docCount += 1
    word_idfs[word] = np.log((len(dataset)/docCount) + 1) # +1 is a bias
    
# STEP-3 : TF-IDF CALCULATION

tfidf_matrix = []
for word in tf_matrix.keys():
    tf_idf = []
    for value in tf_matrix[word]:
        score = value * word_idfs[word]
        tf_idf.append(score)
    tfidf_matrix.append(tf_idf)
    
# STEP-4 : Final Representation
    
X = np.asarray(tfidf_matrix) # Convert in 2D array using NumPy
X = np.transpose(X) # Transpose
        
