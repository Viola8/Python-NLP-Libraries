# Noun Phrase Extraction
from textblob import TextBlob
document = """ TextBlob aims to provide access to common text-processing operations through a familiar interface.
You can treat TextBlob objects as if they were Python strings that learned how to do Natural Language Processing.
"""
text_blob_object = TextBlob(document)
for noun_phrase in text_blob_object.noun_phrases:
    print(noun_phrase)
# Output:
# textblob
# familiar interface
# textblob
# python
# language processing

# Frequency of occurrence of a particular word
text_blob_object = TextBlob(document)
print(text_blob_object.word_counts['natural']) # 1
print(text_blob_object.words.count('natural')) # 1

# Converting to Upper and Lowercase
text = "As an NLP library for Python, TextBlob has been around for a while"
text_blob_object = TextBlob(text)
print(text_blob_object.upper())
text_blob_object = TextBlob(text)
print(text_blob_object.lower())

# Finding N-Grams
text_blob_object = TextBlob(text)
for ngram in text_blob_object.ngrams(2):
    print(ngram)
