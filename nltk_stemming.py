# NLTK has an algorithm named as "PorterStemmer".
# This algorithm accepts the list of tokenized word and stems it into root word.

from nltk.stem import PorterStemmer
e_words = ["wait", "waiting", "waited", "waits"]
ps = PorterStemmer()    # An object is created which belongs to class nltk.stem.porter.PorterStemmer.
for w in e_words:
    rootWord = ps.stem(w)
    print(rootWord)

# OUTPUT:
# wait
# wait
# wait
# wait

from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
sentence = "Stemming is a kind of normalization for words." # Output: stem is a kind of normal for word .
words = word_tokenize(sentence)
ps = PorterStemmer()
for w in words:
	rootWord = ps.stem(w)
	print(rootWord)
