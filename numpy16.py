# Write a NumPy program to find the number of elements of an array,
# length of one array element in bytes and total bytes consumed by the elements.

import numpy as np

a = np.array([88,89,90,91,92,93,94,95,96,97,98,99,100])

print("Size of the array: ", a.size) # 13
print("Length of one array element in bytes: ", a.itemsize) # 4
print("Total bytes consumed by the elements of the array: ", a.nbytes) # 52


a = np.array([88,89,90,91,92,93,94,95,96,97,98,99,100],dtype=np.float64)

print("Size of the array: ", a.size) # 13
print("Length of one array element in bytes: ", a.itemsize) # 8
print("Total bytes consumed by the elements of the array: ", a.nbytes) # 104
