# -*- coding: utf-8 -*-
# SymPy
# Lección 10
# Polinomios

from sympy import expand, factor, symbols


x, y = symbols("x y")
print(x + y - x)
print(x + 2 * y - 6 * x - 5 * x)

expr = x + y
expr = x * expr
print(expr)
print(expand(expr))
print(factor(expand(expr)))
