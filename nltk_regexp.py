from nltk import pos_tag
from nltk import RegexpParser
text ="learn python every day and make study easy".split()
print("After Split:",text) # ['learn','python','every','day', 'and', 'make','study','easy']
tokens_tag = pos_tag(text)
print("After Token:",tokens_tag) # [('learn','VB),('python', 'NN'),('every','DT'),('day','NN'), ('and', 'CC'), ('make','VB'),('study','NN'),('easy', JJ)]
patterns= """mychunk:{<NN.?>*<VBD.?>*<JJ.?>*<CC>?}"""
chunker = RegexpParser(patterns)
print("After Regex:",chunker) # After Regex: chunk.RegexpParser with 1 stages: ,ChunkRule: <NN.?>*<VBD.?>*<JJ.?>*<CC>?>
output = chunker.parse(tokens_tag)

from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')
filterdText=tokenizer.tokenize('Hello Viola, you study very well.') # ['Hello', 'Viola', 'you', 'study', 'very', 'well']
print(filterdText)

# "RegexpTokenizer" is a module of NLTK that removes all the expression, symbol, character, numeric or any things whatever you want
# "tokenize" module tokenizes the words.
