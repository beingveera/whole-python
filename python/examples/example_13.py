import numpy as np

a0 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print("Array 0 (a0):")
print(a0)
print("")

print("Flatten array, a0.ravel():")
print(a0.ravel())
print("")

print("Transpose array, a0.transpose():")
print(a0.transpose())
print("")

print("Array reshape, a0.reshape((4,2))")
print(a0.reshape((4, 2)))
print("")
