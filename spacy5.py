import re
import spacy
from spacy.tokenizer import Tokenizer
custom_nlp = spacy.load('en_core_web_sm')
text2 = "spaCy allows you to customize tokenization by updating the tokenizer property on the nlp object"
prefix_re = spacy.util.compile_prefix_regex(custom_nlp.Defaults.prefixes)
suffix_re = spacy.util.compile_suffix_regex(custom_nlp.Defaults.suffixes)
infix_re = re.compile(r'''[-~]''')
def customize_tokenizer(nlp): # Adds support to use `-` as the delimiter for tokenization
    return Tokenizer(nlp.vocab, prefix_search=prefix_re.search,suffix_search=suffix_re.search, infix_finditer=infix_re.finditer,token_match=None)
custom_nlp.tokenizer = customize_tokenizer(custom_nlp)
custom_tokenizer_doc = custom_nlp(text2)
print([token.text for token in custom_tokenizer_doc])
# Output: ['spaCy', 'allows', 'you', 'to', 'customize', 'tokenization', 'by', 'updating', 'the', 'tokenizer', 'property', 'on', 'the', 'nlp', 'object']

# nlp.vocab is a storage container for special cases and is used to handle cases like contractions and emoticons.
# prefix_search is the function that is used to handle preceding punctuation, such as opening parentheses.
# infix_finditer is the function that is used to handle non-whitespace separators, such as hyphens.
# suffix_search is the function that is used to handle succeeding punctuation, such as closing parentheses.
# token_match is an optional Boolean function that is used to match strings that should never be split. It overrides the previous rules and is useful for entities like URLs or numbers.
