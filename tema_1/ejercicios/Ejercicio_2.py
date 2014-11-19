# -*- coding: utf-8 -*-
# Programación interactiva en Python
# Ejercicio 2
# Resolución de triangulos: regla de senos

from math import degrees
from math import acos


def calcular_angulo(a, b, c):
    """ a/sin(A) == b/sin(B) == c/sin(C) """
    angulo = acos((c**2 - b**2 - a**2)/(-2.0 * a * b))
    return degrees(angulo)
