# Sentence detection using ellipsis `...` as the delimiter for sentence detection.
import spacy
def set_custom_boundaries(doc):
    for token in doc[:-1]:
        if token.text == '...':
            doc[token.i+1].is_sent_start = True
    return doc

ellipsis_text = """ We can also ... maybe you know ...
 customize the sentence detection to detect sentences on custom delimiters ... """

custom_nlp = spacy.load('en_core_web_sm') # Load a new model instance
custom_nlp.add_pipe(set_custom_boundaries, before='parser')
custom_ellipsis_doc = custom_nlp(ellipsis_text)
custom_ellipsis_sentences = list(custom_ellipsis_doc.sents)
for sentence in custom_ellipsis_sentences:
    print(sentence)
# We can also ...
# maybe you know ...
# customize the sentence detection to detect sentences on custom delimiters ...

# Sentence Detection with no customization
nlp = spacy.load('en_core_web_sm')
ellipsis_doc = nlp(ellipsis_text)
ellipsis_sentences = list(ellipsis_doc.sents)
for sentence in ellipsis_sentences:
    print(sentence)
