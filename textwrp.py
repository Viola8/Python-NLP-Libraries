from textwrap3 import wrap

text = """ Formatting of paragraphs is needed when we deal with large amount of text and bring it to a presentable format.
We may just want to print each line with specific width or try to increase the indentation for each next line when printing
a poem. In this chapter we use a module named as textwrap3 to format the paragraphs as needed. """
x = wrap(text, 30)
for i in range(len(x)):
    print(x[i])

import textwrap
text2 = '''
    textwrap.dedent(text) removes any of the same prefix blanks from each line of text.
    This can be used to clear the space to the left of the triple quote string line,
    which is still displayed as indented in the source code.
    '''
dedented_text = textwrap.dedent(text2)
print('Dedented:')
print(dedented_text)

# combining dedent and fill
text3 = '''
    The textwrap module can be used to format text for output in
    situations where pretty-printing is desired.  It offers
    programmatic functionality similar to the paragraph wrapping
    or filling features found in many text editors.
    '''
dedented_text = textwrap.dedent(text3).strip()
for width in [40, 50]:
    print('{} Columns:\n'.format(width))
    print(textwrap.fill(dedented_text, width=width))
    print()
