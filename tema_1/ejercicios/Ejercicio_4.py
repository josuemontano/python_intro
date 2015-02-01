# -*- coding: utf-8 -*-
# Programación interactiva en Python
# Ejercicio 4
# Área de un triángulo

from math import sin
from math import radians


def area_triangulo(a, b, gamma):
    """ Devuelve el area de un triángulo
        A = a * b * sin(gamma)/2
    """
    gamma = radians(gamma)
    return a * b * sin(gamma) / 2

print(area_triangulo(4, 3, 90))
print(area_triangulo(7.1, 8, 31))
