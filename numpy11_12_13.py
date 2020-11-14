# 11 Write a NumPy program to convert a list and tuple into arrays.
import numpy as np

list1 = [1,2,3,4,5]
print(np.asarray(list1))

tuple1 = ([7,7,7],[8,8,8])
print(np.asarray(tuple1))

# 12 Write a NumPy program to append values to the end of an array.

import numpy as np

a = np.array([10,15,20])
print(np.append(a,[[25,30,35],[40,45,50]]))

# numpy.append(arr, values, axis=None)

# 13 Write a NumPy program to create an empty and a full array.

import numpy as np

a = np.empty((3,3))
print(a)

b = np.full((3,3),6)
print(b)
