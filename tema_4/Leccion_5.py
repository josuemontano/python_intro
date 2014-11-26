# -*- coding: utf-8 -*-
# Programación funcional
# Lección 5
# map

import math
import operator


cuadrados = map(lambda x: x ** 2, [1, 2, 3, 4, 5])
print(list(cuadrados))

absolutos = map(operator.abs, [-1, 2, -3, 4, -5])
print(list(absolutos))

suma = map(operator.add, [1, 2, 3], [4, 5, 6])
print(list(suma))

senos = map(math.sin, [1, 2, 3, 4, 5])
print(list(senos))

cadenas = map(str, range(1, 11))
print(list(cadenas))

contador = map([1, 2, 3, 4].count, [1, 2, 3, 4, 1, 1, 2])
print(list(contador))
