# -*- coding: utf-8 -*-
# SymPy
# Lección 11
# Cálculo diferencial e integral

from sympy import *


x = symbols("x")

fx = sin(x) * exp(x)
print(limit(fx, x, 0))

fx = sin(x) * exp(x)
print(diff(fx, x))

fx = sin(x ** 2)
print(integrate(fx, (x, -oo, oo)))

fx = cos(x) ** 2
print(latex(Integral(fx, (x, 0, pi))))
