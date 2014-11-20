# -*- coding: utf-8 -*-
# Programación orientada a objetos
# Lección 6
# Módulo fractions

from fractions import Fraction
from fractions import gcd


a = Fraction(5, 4)
b = Fraction(7, 16)
print(a + b)
print(a - b)
print(a * b)
print(a / b)

print(a.numerator)
print(a.denominator)
print(a.limit_denominator(50))

print(float(a + b))
print(gcd(10, 6))


# Otros constructores
a = Fraction('7e-6')
print(a)

a = Fraction(10.5)
print(a)

a = Fraction('-9/2')
print(a)
