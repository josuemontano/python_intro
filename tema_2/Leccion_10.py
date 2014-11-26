# -*- coding: utf-8 -*-
# Introducción al lenguaje de programacion Python
# Lección 10
# Tuplas

import math


tupla = (1, 2)
type(tupla)

print(tupla)
print(tupla[0])
print(tupla[1])

print("La tupla contiene el valor 2?", 2 in tupla)


x = 10
print(math.frexp(x))  # Tupla con la mantisa y exponente de x
print(math.modf(x))   # Tupla con la parte fraccional y entera de x
