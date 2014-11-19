# -*- coding: utf-8 -*-
# Programación interactiva en Python
# Ejercicio 2
# Teorema de cosenos

from math import cos
from math import sqrt
from math import radians


def teorema_cosenos(a, b, gamma):
    """ Resulve un triángulo aplicando el teorema de cosenos
        c^2 = a^2 + b^2 - 2ab*cos(gamma)
    """
    gamma = radians(gamma)
    return sqrt(a ** 2 + b ** 2 - 2 * a * b * cos(gamma))

print(teorema_cosenos(4, 3, 90))
print(teorema_cosenos(7.1, 8, 31))
