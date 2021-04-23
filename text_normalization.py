

str = """           Text normalization is the process of transforming a text into a canonical (standard) form.
Text normalization includes about 7 main processes, such as
    converting all letters to lower or upper case
    converting numbers into words or removing numbers
    removing punctuations, accent marks and other diacritics
    removing white spaces
    expanding abbreviations
    removing stop words, sparse terms, and particular words
    text canonicalization         """

# 1. Convert to lower case
lower_str = str.lower()
print(lower_str)

# 2. Removing numbers
# import regex
import re
no_number_str = re.sub(r'\d+','',lower_str)
print(no_number_str)

# 3. Removing punctuations
no_punc_str = re.sub(r'[^\w\s]','', no_number_str)
print(no_punc_str)

#4. Removing white spaces
no_wspace_str = no_punc_str.strip()
print(no_wspace_str)
