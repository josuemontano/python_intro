# -*- coding: utf-8 -*-
# Herramientas para computación científica
# Lección 5
# NumPy: Matrices

import numpy


matriz = numpy.array([[1, 0, 0],
                      [0, 1, 0],
                      [0, 0, 1]])

print(matriz, type(matriz))

print(matriz.sum())
print(matriz.prod(axis=1))

print(matriz.diagonal())
print(matriz.transpose())
print(matriz.conj())

print(matriz.mean())
print(matriz.var())
print(matriz.std())


x = numpy.zeros((3, 2))
print(x, type(x))

x = numpy.zeros_like(matriz)
print(x, type(x))


x = numpy.ones((4, 3), dtype=float)
print(x, type(x))

x = numpy.ones_like(matriz)
print(x, type(x))


x = numpy.identity(10)
print(x, type(x))


matriz.fill(5)
print(matriz)
