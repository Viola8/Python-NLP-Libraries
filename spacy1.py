# using spaCy to create a processed Doc object, which is a container for accessing linguistic annotations,
# for a given input string
import spacy
nlp = spacy.load('en_core_web_sm')
introduction_text = ('This is about Natural Language Processing with SpaCy')
introduction_doc = nlp(introduction_text)

print ([token.text for token in introduction_doc]) # Extract tokens for the given doc
# Output: ['This', 'is', 'about', 'Natural', 'Language','Processing', 'in', 'Spacy']

# Sentence Detection
text = """Sentence Detection is the process of locating the start and end of sentences in a given text.
 This allows you to you divide a text into linguistically meaningful units.
 You’ll use these units when you’re processing your text to perform tasks such as part of speech tagging and entity extraction."""
document = nlp(text)
sentences = list(document.sents)
len(sentences)

for sentence in sentences:
    print (sentence)
