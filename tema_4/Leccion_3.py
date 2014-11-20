# -*- coding: utf-8 -*-
# NumPy
# Lección 3
# Operaciones con matrices

from numpy import array
from numpy import sqrt


a = array([[1, 0, 1], [3, 0, 6]], float)
b = array([[9, 4, 3], [5, 2, 8]], float)

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)

print(a ** b)
print(sqrt(a))

print(a > 4)
