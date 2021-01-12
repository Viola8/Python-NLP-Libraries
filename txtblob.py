# Sentiment analysis with TextBlob.
from textblob import TextBlob
text="It was a very pleasant day"
blob=TextBlob(text)

print(blob.sentiment)
if(blob.sentiment.polarity > 0):
  print("Positive") # Output: Sentiment(polarity=0.9533333333333333, subjectivity=1.0)  Positive

# 2
opinion = TextBlob("The food was great!")
print(opinion.sentiment) # Output: Sentiment(polarity=1.0, subjectivity=0.75)

# How to do spell correction in a given text.
text2="He is a gret person. He beleives in bod"
# Using textblob's correct() function
text2=TextBlob(text2)
print(text2.correct())

# How to convert text into a plural or singular form using the pluralize and singularize methods.
text3 = ("Hockey is a good game. It has many health benefit")
text_blob_object = TextBlob(text3)
print(text_blob_object.words.pluralize()) # ['Hockeys', 'iss', 'some', 'goods', 'games', 'Its', 'hass', 'manies', 'healths', 'benefits']

text4 = "People like his movies"
text_blob_object = TextBlob(text4)
print(text_blob_object.words.singularize()) # ['person', 'like', 'he', 'movie']
