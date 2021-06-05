import numpy as np

a0 = np.array([5, 6, 7, 8])

print("Array 0 (a0):")
print(a0)
print("")

print("a0[1]:")
print(a0[1])
print("")

print("a0[2:4]")
print(a0[2:4])
print("")

print("Reverse, a0[::-1]")
print(a0[::-1])
print("")

print("Multiple assignment, a0[2:4]=10:")
a0[2:4] = 10
print(a0)
print("")
