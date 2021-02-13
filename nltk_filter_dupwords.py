# to eliminate the duplicate words from the text.
from nltk.tokenize import word_tokenize
text = "The Sky is blue also the ocean is blue also Rainbow has a blue colour."

# 1. without preserving the order
print(set(word_tokenize(text)))
# Output:{'is', 'the', 'has', 'The', 'Sky', 'also', 'colour', 'ocean', 'Rainbow', '.', 'a', 'blue'}

# 2. preserving the Order
text_tokens = word_tokenize(text)
ordered_tokens = set()
result = []
for word in text_tokens:
    if word not in ordered_tokens:
        ordered_tokens.add(word)
        result.append(word)
print(result)
# Output: ['The', 'Sky', 'is', 'blue', 'also', 'the', 'ocean', 'Rainbow', 'has', 'a', 'colour','.']
