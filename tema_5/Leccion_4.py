# -*- coding: utf-8 -*-
# Herramientas para computación científica
# Lección 4
# NumPy: Generación de colecciones

from numpy import arange, linspace


x = arange(5, 50 + 1, 3)
print(type(x))
print(x)

y = linspace(0, 2, 100)
print(type(y))
print(y)
