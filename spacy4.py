# Tokenization in spaCy. SpaCy provides various attributes for the Token class
import spacy
nlp = spacy.load('en_core_web_sm')
text = """Tokenization allows you to identify the basic units in your text.
Tokenization is useful because it breaks a text into meaningful units called tokens. """
document = nlp(text)
# text_with_ws prints token text with trailing space (if present).
# is_alpha detects if the token consists of alphabetic characters or not.
# is_punct detects if the token is a punctuation symbol or not.
# is_space detects if the token is a space or not.
# shape_ prints out the shape of the word.
# is_stop detects if the token is a stop word or not.
for token in document:
    print (token, token.idx, token.text_with_ws, token.is_alpha, token.is_punct, token.is_space, token.shape_, token.is_stop)

# Tokenization 0 Tokenization True False False Xxxx False
# allows 13 allows True False False xxxx False
# you 20 you True False False xxx True
# to 24 to True False False xx True
# identify 27 identify True False False xxxx False
# the 36 the True False False xxx True
# basic 40 basic True False False xxxx False
# units 46 units True False False xxxx False
# in 52 in True False False xx True
# your 55 your True False False xxxx True
# text 60 text True False False xxxx False
# . 64 . False True False . False
# 65
# False False True
# False
# Tokenization 66 Tokenization True False False Xxxxx False
# is 79 True False False xx True
# useful 82 useful True False False xxxx False
# because 89 because True False False xxxx True
# it 97 it True False False xx True
# breaks 100 breaks True False False xxxx False
# a 107 a True False False x True
# text 109 text True False False xxxx False
# into 114 into True False False xxxx True
# meaningful 119 meaningful True False False xxxx False
# units 130 units True False False xxxx False
# called 136 called True False False xxxx False
# tokens 143 tikens True False False xxxx False
# . 149 . False True False . False
