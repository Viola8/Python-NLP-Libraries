#6 Write a Python NLTK program to tokenize a twitter text.
from nltk.tokenize import TweetTokenizer
tknzr = TweetTokenizer(strip_handles=True, reduce_len=True)
tweet_text = "NoSQL introduction - https://www.nltk.org #database #webdev"
result = tknzr.tokenize(tweet_text)
print(result)

# Output: ['NoSQL', 'introduction', '-', 'https://www.nltk.org', '#database', '#webdev']

#7 Write a Python NLTK program that will read a given text through each line and look for sentences.
# Print each sentence and divide two sentences with “==============”.
import nltk.data
text = '''
Tokenization is the process of demarcating and possibly classifying sections of a string of input characters.
The resulting tokens are then passed on to some other form of processing.
The process can be considered a sub-task of parsing input.
'''
sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
print('\n==============\n'.join(sent_detector.tokenize(text.strip())))

# Output:
# Tokenization is the process of demarcating and possibly classifying sections of a string of input characters.
# ==============
# The resulting tokens are then passed on to some other form of processing.
# ==============
# The process can be considered a sub-task of parsing input.
