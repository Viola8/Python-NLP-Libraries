# Frequency distribution of each word in the graph
import nltk
a = "It is a distribution because it tells us how the total number of word tokens in the text are distributed across the vocabulary items."
words = nltk.tokenize.word_tokenize(a) # Tokenize each word in the text which is served as input to FreqDist module of nltk
fd = nltk.FreqDist(words)   # Apply each word to nlk.FreqDist in the form of a list
fd.plot() # Plot the words in the graph using plot()

from nltk.probability import FreqDist
sentence= "I count words in this sntence"
tokens = nltk.tokenize.word_tokenize(sentence)
fdist = FreqDist(tokens) # variable fdist is of the type "class 'nltk.probability.FreqDist" and contains the frequency distribution of words
print(fdist) # Output: <FreqDist with 6 samples and 6 outcomes>
