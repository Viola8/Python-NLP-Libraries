# 4 Write a Python NLTK program to create a list of words from a given string.

from nltk.tokenize import TreebankWordTokenizer
tokenizer = TreebankWordTokenizer()
text = "NLTK is a leading platform for building Python programs to work with human language data."
print("\nOriginal string:")
print(text)
print("\nList of words:")
print(tokenizer.tokenize(text))

# 5 Write a Python NLTK program to split all punctuation into separate tokens.
from nltk.tokenize import WordPunctTokenizer
text = "I can't believe!"
result = WordPunctTokenizer().tokenize(text)
print("\nSplit all punctuation into separate tokens:")
print(result)

# Output: ['I', 'can', "'", 't', 'believe' '!']
