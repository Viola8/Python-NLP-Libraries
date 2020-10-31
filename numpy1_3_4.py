# 1 Write a NumPy program to convert a list of numeric value into a one-dimensional NumPy array.

import numpy as np
l = [12.23, 13.32, 100, 36.32]
print("Original List:",l)
a = np.array(l)
print("One-dimensional NumPy array: ",a)

# Output: Original List: [12.23, 13.32, 100, 36.32]
# One-dimensional NumPy array:  [  12.23   13.32  100.     36.32]

# 2 Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.

import numpy as np
a = np.arange(2,11).reshape(3,3)
print(a)

# [[2 3 4]
# [5 6 7]
# [8 9 10]]

# 3 Write a NumPy program to create a null vector of size 10 and update sixth value to 11.

import numpy as np
a = np.zeros(10)
print(a)
a[6] = 11
print("Unpdated array:", a)
