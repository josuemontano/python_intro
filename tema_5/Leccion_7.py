# -*- coding: utf-8 -*-
# Herramientas para computación científica
# Lección 7
# SciPy: Álgebra lineal

from numpy import array
from scipy.linalg import *


a = array([[5, 6, 2], [0, 4, 1], [3, 7, 1]])
d = array([[3, 2, 6], [0, 0, 9], [8, 2, 2]])

print(det(a))

print(inv(a))
print(a.dot(inv(a)))
print(solve(d, a))
print(eigvals(d))
print(svd(d))

print(a.trace(offset=1))
print(a.diagonal())
