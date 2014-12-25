# -*- coding: utf-8 -*-
# Herramientas para computación científica
# Lección 2
# NumPy: Colecciones (arrays)

import numpy


vector = numpy.array([3.1, 10, 8.94, 0.4, 2.4])
print(vector, type(vector))

print(len(vector))
print(6 in vector)
print(list(map(lambda x: True if x in [1, 2, 10] else False, vector)))

print(vector[0])
print(vector[1:])
print(vector[:2])
print(vector[2:5])

print(vector.min(), vector.argmin())
print(vector.max(), vector.argmax())

print(vector.copy())
print(vector.tolist())
