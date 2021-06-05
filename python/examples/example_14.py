import numpy as np

a0 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
a1 = np.array([[9, 10, 11, 12], [13, 14, 15, 16]])

print("Array 0 (a0):")
print(a0)
print("Array 1 (a1):")
print(a1)
print("")

print("Vertical merge, np.vstack((a0,a1)):")
print(np.vstack((a0, a1)))
print("")

print("Horizontal merge, np.hstack((a0,a1)):")
print(np.hstack((a0, a1)))
print("")

print("Vertical split a0 into 2 pieces, np.vsplit(a0,2):")
r = np.vsplit(a0, 2)
print(r[0])
print(r[1])
print("")

print("Horizontal split a0 into 2 pieces, np.hsplit(a0,2):")
r = np.hsplit(a0, 2)
print(r[0])
print(r[1])
print("")
