import nltk
from nltk.stem.porter import PorterStemmer
porter_stemmer  = PorterStemmer()
text = "studies studying learned learns"
tokenization = nltk.word_tokenize(text)
for w in tokenization:
    print("Stemming for {} is {}".format(w,porter_stemmer.stem(w)))

# Output:
# Stemming for studies is studi
# Stemming for studying is studi
# Stemming for learned is learn
# Stemming for learns is learn

import nltk
from nltk.stem import 	WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
text = "studies studying learned learns"
tokenization = nltk.word_tokenize(text)
for w in tokenization:
    print("Lemma for {} is {}".format(w, wordnet_lemmatizer.lemmatize(w)))

# Output:
# Lemma for studies is study
# Lemma for studying is studying
# Lemma for learned is learned
# Lemma for learns is learns
