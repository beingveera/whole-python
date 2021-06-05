import cmath

def solvequadeq(a, b, c):
    D = b**2 - 4 * a * c
    x1 = (-b - cmath.sqrt(D)) / (2 * a)
    x2 = (-b + cmath.sqrt(D)) / (2 * a)
    return x1, x2


a = 1
b = -4
c = 3

print('Equation: %d*x**2 + %d*x + %d = 0' % (a, b, c))
solutions = solvequadeq(a, b, c)
print('Roots:')
print('x1 = %s' % solutions[0])
print('x2 = %s' % solutions[1])
