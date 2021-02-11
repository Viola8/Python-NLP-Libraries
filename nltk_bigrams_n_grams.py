import nltk
from nltk.tokenize import word_tokenize
text = """Parsing is the method to identify and understand the syntactic structure of a text.
It is done by analyzing the individual elements of the text. """
text_tokenized = word_tokenize(text)
print(list(nltk.bigrams(text_tokenized)))
# Output: [('Parsing', 'is'), ('is", 'the'), ('the', 'method'), ('method', 'to')......]

print(list(nltk.trigrams(text_tokenized)))
# Output: [('Parsing', 'is', 'the'), ('is', 'the', 'method'), ('the', 'method', 'to')......]

# For extracting n-grams, we can use the function nltk.ngrams and give the argument n for the number of parsers.
print(list(nltk.ngrams(text_tokenized,5)))
