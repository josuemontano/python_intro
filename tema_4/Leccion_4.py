# -*- coding: utf-8 -*-
# Herramientas de computación científica
# Lección 4
# NumPy: Operaciones con matrices

import numpy
from numpy import array


a = array([[1, 0, 1], [3, 0, 6]], float)
b = array([[9, 4, 3], [5, 2, 8]], float)

print(len(a))
print(6 in a)

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)

print(a ** b)
print(numpy.sqrt(a))

print(a > 4)

print(10 * numpy.sin(a))
