# -*- coding: utf-8 -*-
# Programación interactiva en Python
# Lección 8
# Importación de módulos, función principal (main)

from math import pi


def calcular_volumen_esfera():
    """ Función que calcula el volumen de una esfera
        de radio 7
        V = (4/3)πr^3
    """
    radio = 7
    return 4 / 3 * pi * radio ** 3


def main():
    print(calcular_volumen_esfera())

main()
