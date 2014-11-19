# -*- coding: utf-8 -*-
# Programación interactiva en Python
# Ejercicio 1
# Teorema de pitagoras

from math import sqrt


def teorema_pitagoras(lado_a, lado_b):
    lado_c = sqrt(lado_a ** 2 + lado_b ** 2)
    return lado_c
