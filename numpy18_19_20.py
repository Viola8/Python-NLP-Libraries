# 18 Write a NumPy program to find common values between two arrays.

import numpy as np
array1 = [22,33,44,55,66,77]
array2 = [22,44,66,88]
print(np.intersect1d(array1,array2))

# Output: [22 44 66]

# 19 Write a NumPy program to get the unique elements of an array.

import numpy as np
array1 = [23,34,34,34,45]
print(np.unique(array1))

# 20  Write a NumPy program to find the set difference of two arrays.
# The set difference will return the sorted, unique values in array1 that are not in array2.

import numpy as np
array1 = np.array([0, 10, 20, 40, 60, 80])
array2 = [10, 30, 40, 50, 70]
print("Unique values in array1 that are not in array2:")
print(np.setdiff1d(array1, array2))

# Output: [0 20 60 80]
