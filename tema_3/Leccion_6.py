# -*- coding: utf-8 -*-
# Programación orientada a objetos
# Lección 6
# Módulo fractions

from fractions import Fraction


a = Fraction(5, 4)
b = Fraction(7, 16)
print(a + b)
print(a - b)
print(a * b)
print(a / b)

print(a.numerator)
print(a.denominator)

c = a + b
print(float(c))
