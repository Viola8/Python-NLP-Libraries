# to remove stop words from a given text.
from nltk.corpus import stopwords
stoplist = stopwords.words('english')
text = "This is a sample sentence, showing off the stop words filtration."
clean_word_list = [word for word in text.split() if word not in stoplist]
print(clean_word_list)

# Output: ['This','sample','sentence','showing','stop','words','filtration.']

# to omit some given stop words from the stopwords list.
import nltk
from nltk.corpus import stopwords
result = set(stopwords.words('french'))
stop_words = set(stopwords.words('french')) - set(['notre', 'toi', 'aura'])
print (stop_words)

# to compare the similarity of two given words.
# verbs go and move
from nltk.corpus import wordnet
v1 = wordnet.synset('go.v.01')
v2 = wordnet.synset('move.v.01')
print(v1.wup_similarity(v2))   # 1.0

# nouns bus and boad
n1 = wordnet.synset('bus.n.01')
n2 = wordnet.synset('boat.n.01')
print(n1.wup_similarity(n2)) # 0.7
