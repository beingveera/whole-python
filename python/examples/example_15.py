import numpy as np

A = np.array([[3, 2, 1], [10, 5, 16], [7, 8, 9]])
B = np.array([[19, 11, 15], [13, 16, 12], [13, 41, 11]])

print("A =\n%s" % A)
print("B =\n%s" % B)
print("Ax = B")
x = np.linalg.solve(A, B)
print("x =\n%s" % x)
print("")
print("Check the solution:")
print("Ax =\n%s" % A.dot(x))
print("")
