# -*- coding: utf-8 -*-
# Programación interactiva en Python
# Lección 15
# Módulo cmath

from cmath import *


x = complex(-1.0, 0.0)
print(x)

print(x.real)
print(x.imag)

print(phase(x))   # Fase o argumento de x, rango de resultado es [-π, π]
print(polar(x))   # x en coordenadas polares
print(rect(e, 0)) # Numero complejo cuyas coordenadas polares son e y 0

print(exp(x))
print(sqrt(x))

print(abs(x))     # |x|
