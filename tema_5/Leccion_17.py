# -*- coding: utf-8 -*-
# Herramientas para computación científica
# Lección 17
# SymPy: Álgebra lineal

from sympy import *


x = Symbol('x')
y = Symbol('y')
a = Matrix([[1, x], [y, 1]])

print(a)
print(a ** 2)

b = Matrix([[1, x], [x, 1]])
print(b.eigenvals())
print(b.eigenvects())
print(b.det_LU_decomposition())
