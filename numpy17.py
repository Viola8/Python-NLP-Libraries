# Write a NumPy program to test whether each element of a 1-D array is also present in a second array.

import numpy as np

array1 = np.array([0, 10, 20, 40, 60])
array2 = [0, 40]
print(np.in1d(array1, array2))
# Output: [True False False True False]

print(np.in1d(array2, array1))

# Output: [True True]

# numpy.in1d
# Test whether each element of a 1-D array is also present in a second array.
# Returns a boolean array the same length as ar1 that is True where an element of ar1 is in ar2 and False otherwise.
