# -*- coding: utf-8 -*-
# NumPy
# Lección 1
# Matrices

import numpy


matriz = numpy.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
print(matriz, type(matriz))
print(matriz.sum())
print(matriz.prod())

print(matriz.mean())
print(matriz.var())
print(matriz.std())


x = numpy.zeros((3, 2))
print(x, type(x))

x = numpy.zeros_like(matriz)
print(x, type(x))


x = numpy.ones((4, 3), dtype=int)
print(x, type(x))

x = numpy.ones_like(matriz)
print(x, type(x))


x = numpy.identity(10)
print(x, type(x))
