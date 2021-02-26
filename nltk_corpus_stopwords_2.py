# 1 to remove stop words from a given text.
from nltk.corpus import stopwords
stoplist = stopwords.words('english')
text = "This is a sample sentence, showing off the stop words filtration."
clean_word_list = [word for word in text.split() if word not in stoplist]
print(clean_word_list) # Output: ['This','sample','sentence','showing','stop','words','filtration.']

# 2 to remove stop words from a given text.
from nltk.corpus import stopwords
en_stops = set(stopwords.words('english'))
all_words = ['There', 'is', 'a', 'tree','near','the','river']
for word in all_words:
    if word not in en_stops:
        print(word)

# to omit some given stop words from the stopwords list.
import nltk
from nltk.corpus import stopwords
result = set(stopwords.words('french'))
stop_words = set(stopwords.words('french')) - set(['notre', 'toi', 'aura'])
print (stop_words)
