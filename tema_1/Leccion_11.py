# -*- coding: utf-8 -*-
# Programación interactiva en Python
# Lección 11
# Módulo math: Funciones exponenciales y logarítmicas

from math import *


x = 9
print(exp(x))

""" Para valores de x muy pequenos, la resta exp(x) - 1 puede resultar
     en una significante perdida de precision
"""
print(expm1(x))

print(log(x))
print(log1p(x))

base = 5
print(log(x, base))

print(log2(x))
print(log10(x))

x = 2
y = 5
print(sqrt(x))
print(pow(x, y))
