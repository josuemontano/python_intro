# -*- coding: utf-8 -*-
# Programación interactiva en Python
# Lección 10
# Módulo math

from math import *


print(factorial(900))   # 900!

x = pi
y = e

print(fabs(x))          # |x|
print(ceil(x))          # Función techo
print(floor(x))         # Función piso
print(trunc(x))         # Truncamiento a entero

print(fmod(x, y))       # Módulo de x / y (preferible para floats)
print(copysign(x, -1))  # Float con la magnitud de x pero el signo de -1

print(gamma(x))         # Función gamma
print(lgamma(x))        # Logaritmo natural del valor absoluto de gamma(x)
