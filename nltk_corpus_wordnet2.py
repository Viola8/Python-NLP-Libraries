# all Lemmas
from nltk.corpus import wordnet as wn
print(wn.synset('locomotive.n.01').lemma_names())
# ['locomotive', 'engine', 'locomotive_engine', 'railway_locomotive']

# word Definition
print(wn.synset('ocean.n.01').definition())
# a large body of water constituting a principal part of the hydrosphere

# usage Examples
print(wn.synset('good.n.01').examples())
# ['for your own good', "what's the good of worrying?"]

# opposite Words
print(wn.lemma('horizontal.a.01.horizontal').antonyms())
# [Lemma('inclined.a.02.inclined'), Lemma('vertical.a.01.vertical')]
