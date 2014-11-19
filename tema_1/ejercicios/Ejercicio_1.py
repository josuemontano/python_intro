# -*- coding: utf-8 -*-
# Programación interactiva en Python
# Ejercicio 1
# Teorema de pitágoras

from math import sqrt


def teorema_pitagoras(a, b):
    """ Devuelve el valor de la longitud de la hipotenusa de un triángulo
        rectángulo dadas las longitudes de sus catetos
        c^2 = a^2 + b^2
    """
    c = sqrt(a ** 2 + b ** 2)
    return c

print(teorema_pitagoras(3, 4))
