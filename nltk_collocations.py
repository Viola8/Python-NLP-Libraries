import nltk

text1 = "Sets of two words are commonly used"
tokens = nltk.word_tokenize(text1)
output = list(nltk.bigrams(Tokens))
print(output)

text2 = "This is especially useful in text-based sentimental analysis"
tokens = nltk.word_tokenize(text2)
output = list(nltk.trigrams(Tokens))
print(output)
