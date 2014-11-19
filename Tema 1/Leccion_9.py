# -*- coding: utf-8 -*-
# Programación interactiva en Python
# Lección 9
# Parametros de funciones

from math import pi


def calcular_volumen_esfera(radio):
    """ Funcion que calcula el volumen de una esfera
        de radio dado
        V = (4/3)πr^3
    """
    return 4/3 * pi * radio ** 3


print(calcular_volumen_esfera(7))
