# -*- coding: utf-8 -*-
# Herramientas de computación científica
# Lección 12
# SymPy: Álgebra lineal

from sympy import *


x = Symbol('x')
y = Symbol('y')
a = Matrix([[1, x], [y, 1]])
print(a)
print(a ** 2)
