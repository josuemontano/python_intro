# -*- coding: utf-8 -*-
# Herramientas de computación científica
# Lección 2
# NumPy: Arrays

import numpy


vector = numpy.array([3.1, 10, 8.94, 0.4, 2.4])
print(vector, type(vector))

print(vector[0])
print(vector[1:])
print(vector[:2])
print(vector[2:5])

print(vector.min(), vector.argmin())
print(vector.max(), vector.argmax())

print(vector.copy())
print(vector.tolist())
