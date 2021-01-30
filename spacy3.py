# Tokenization in spaCy
import spacy
nlp = spacy.load('en_core_web_sm')
text = """Tokenization allows you to identify the basic units in your text.
Tokenization is useful because it breaks a text into meaningful units called tokens. """
document = nlp(text)
for token in document:
    print (token, token.idx)
# Tokenization 0
# allows 13
# you 20
# to 24
# identify 27
# the 36
# basic 40
# units 46
# in 52
# your 55
# text 60
# . 64
# 65
# Tokenization 66
# is 79
# useful 82
# because 89
# it 97
# breaks 100
# a 107
# text 109
# into 114
# meaningful 119
# units 130
# called 136
# tokens 143
# . 149
