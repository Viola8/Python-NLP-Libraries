# Write a Python NLTK program to find parenthesized expressions in a given string and divides the string into a sequence of substrings.

from nltk.tokenize import SExprTokenizer
text = '(a b (c d)) e f (g)'
print("\nOriginal Tweet:")
print(text)
print(SExprTokenizer().tokenize(text))
text = '(a b) (c d) e (f g)'
print("\nOriginal Tweet:")
print(text)
print(SExprTokenizer().tokenize(text))
text = '[(a b (c d)) e f (g)]'
print("\nOriginal Tweet:")
print(text)
print(SExprTokenizer().tokenize(text))
print(text)
print(SExprTokenizer().tokenize(text))
text = '{a b {c d}} e f {g}'
print("\nOriginal Tweet:")
print(text)
print(SExprTokenizer().tokenize(text))

# Original Tweet:
# (a b (c d)) e f (g)
# ['(a b (c d))', 'e', 'f', '(g)']

# Original Tweet:
# (a b) (c d) e (f g)
# ['(a b)', '(c d)', 'e', '(f g)']

# Original Tweet:
# [(a b (c d)) e f (g)]
# ['[', '(a b (c d))', 'e', 'f', '(g)', ']']
# [(a b (c d)) e f (g)]
# ['[', '(a b (c d))', 'e', 'f', '(g)', ']']

# Original Tweet:
# {a b {c d}} e f {g}
# ['{a b {c d}} e f {g}']
