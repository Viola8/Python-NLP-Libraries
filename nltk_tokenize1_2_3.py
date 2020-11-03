# 1
from nltk.tokenize import word_tokenize
text = "This exercise is easy to do! Looks nice."
print(word_tokenize(text))

# Output: ['This','exercise', 'is', 'easy', 'to', 'do' '!','Looks', 'nice', '.']

# 2
from nltk.tokenize import sent_tokenize
text = "This exercise is easy to do! Looks nice."
print(sent_tokenize(text))

# Output: ['This exercise is easy to do!', 'Looks nice.']

# 3 Write a Python NLTK program to tokenize sentences in languages other than English.
text = "A force de forger on devient forgeron"

from nltk.tokenize import sent_tokenize
token_text = sent_tokenize(text, language='french')
print(token_text)
