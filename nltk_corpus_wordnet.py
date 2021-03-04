# to find the definition and examples of a given word using WordNet.
from nltk.corpus import wordnet
syns = wordnet.synsets("note")
print(syns[0].definition()) # a brief written record
print(syns[0].examples()) # ['he made a note of the appointement']
print(syns[1].definition()) # a short personal letter
print(syns[1].examples())
# to find the sets of synonyms and antonyms of a given word.
# 1
from nltk.corpus import wordnet
syns = wordnet.synsets("night")
print(syns)

# 2
synonyms = []
antonyms = []

for syn in wordnet.synsets("night"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())
print("Set of synonyms of the said word:", synonyms)
print("Set of antonyms of the said word:", antonyms)

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
