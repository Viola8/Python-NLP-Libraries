# 1 pos_tag exercise.
import nltk
text = "Hello, I have to learn a very good lesson, and I love visiting your site."
sentence = nltk.sent_tokenize(text)
for sent in sentence:
	 print(nltk.pos_tag(nltk.word_tokenize(sent)))

# OUTPUT: [('Hello', 'NNP'), (',', ','), ('I', 'PRP'), ('have', 'VBP'), ('learn', 'VBN'),
# ('a', 'DT'), ('very', 'RB'), ('good', 'JJ'), ('lesson', 'NN'), ('and', 'CC'), ('I', 'PRP'),
# ('love', 'VBP'), ('visiting', 'VBG'), ('your', 'PRP$'), ('site', 'NN'), ('.', '.')]

# 2 Pos_tag&RegexpParser exercise
import nltk
text = "learn Python from tutorial"
tokens = nltk.word_tokenize(text)
print(tokens)
tag = nltk.pos_tag(tokens)
print(tag)
grammar = "NP: {<DT>?<JJ>*<NN>}"
cp  =nltk.RegexpParser(grammar)
result = cp.parse(tag)
print(result)
result.draw()    # It draws the pattern graphically which can be seen in Noun Phrase chunking!!!

# Output:
# ['learn', 'Python', 'from', 'tutorial']  -- These are the tokens
# [('learn', 'JJ'), ('Python', 'NN'), ('from', 'IN'), ('tutorial', 'NN')]   -- These are the pos_tag
# (S (NP learn/JJ Python/NN) from/IN (NP tutorial/NN))        -- Noun Phrase Chunking
