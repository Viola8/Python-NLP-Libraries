# 8 Write a NumPy program to create a 2d array with 1 on the border and 0 inside.
import numpy as np
a = np.ones((5,7))
a[1:-1,1:-1] = 0
print(a)

#  9 Write a NumPy program to add a border (filled with 0's) around an existing array.

import numpy as np
a = np.ones((3,3))

# numpy.pad(array, pad_width, mode='constant', **kwargs)
print(np.pad(a, pad_width=1, mode='constant', constant_values=0))

# constant_valuessequence or scalar, optional
# Used in ‘constant’. The values to set the padded values for each axis.
