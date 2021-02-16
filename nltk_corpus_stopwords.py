#  list for all the corpus names
import nltk.corpus
dir(nltk.corpus)
print(dir(nltk.corpus))

# list of common stop words in various languages in Python.
from nltk.corpus import stopwords
print (stopwords.fileids())

# Write a Python NLTK program to check the list of stopwords in English, French, Russian and Spanish languages.
import nltk
from nltk.corpus import stopwords
result = stopwords.words('english')
print("List of stopwords in English:")
print(result)
print("\nList of stopwords in French:")
result = stopwords.words('french')
print(result)
print("\nList of stopwords in Russian:")
result = stopwords.words('russian')
print(result)
print("\nList of stopwords in Spanish:")
result = stopwords.words('spanish')
print(result)
