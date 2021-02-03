import spacy
custom_nlp = spacy.load('en_core_web_sm')
spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS

for stop_word in list(spacy_stopwords)[:10]:
    print(stop_word)
# using
# becomes
# had
# itself
# once
# often
# is
# herein
# who
# too

doc = "You can remove stop words from the input text"
for token in doc:
    if not token.is_stop:
        print (token)
no_stopword_doc = [token for token in doc if not token.is_stop]
print (no_stopword_doc)
