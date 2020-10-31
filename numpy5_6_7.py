# 5 Write a NumPy program to create an array with values ranging from 12 to 38.
import numpy as np
a = np.arange(12,39)
print(a)

# 6 Write a NumPy program to reverse an array (first element becomes last).
import numpy as np
a = np.arange(10,40)
print(a[::-1])

# 7 Write a NumPy program to convert an array to a float type.
import numpy as np
a = np.arange(1,8)
print(np.asfarray(a))

# Output: [1. 2. 3. 4. 5. 6. 7.]
