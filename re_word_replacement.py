import re

# Using the sub() Function   Maximum capacity re.sub(pattern, repl, string, count, flags)
print(re.sub(r'(cat|dog)', 'pet', "Dennis owns a dog and Anne owns a cat.")) # re.sub(pattern, repl, string)
# Dennis owns a pet and Anne owns a pet.

print(re.sub(r'(cat|dog)', 'pet', "Dennis owns a DOG and Anne owns a cat.")) # no replacement for a Uppercase.
# Dennis owns a DOG and Anne owns a pet.

# with re.IGNORECASE flag e.i. re.sub(pattern, repl, string, flags)
print(re.sub(r'(cat|dog)','pet', "Dennis owns a DOG and Anne owns a cat.", flags = re.IGNORECASE))
# Dennis owns a pet and Anne owns a pet.

# re.subn(pattern, repl, string, count) returns a tuple with a number of matches
print(re.subn(r'(str)','string', "Replacing the complete str or a part of str is a very frequent requirement in text processing."))
# ("Replacing the complete str or a part of str is a very frequent requirement in text processing.", 2)

pattern = re.compile(r'(blue|brown)')
string_a = pattern.subn("grey", "Among human beings, blue eyes are less common than green eyes.")
string_b = pattern.subn("grey", "Among human beings, green eyes are less common than brown eyes.")
print(string_a) # ("Among human beings, grey eyes are less common than green eyes.",1)
print(string_b) # ("Among human beings, green eyes are less common than grey eyes.",1)
