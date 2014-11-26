# -*- coding: utf-8 -*-
# Herramientas para computación científica
# Lección 3
# NumPy: Atributos de array

from numpy import array


a = array([[0, 1, 2, 3, 4],
           [5, 6, 7, 8, 9],
           [10, 11, 12, 13, 14]])

print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)
print(a.itemsize)
print(a.data)
