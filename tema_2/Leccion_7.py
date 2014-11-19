# -*- coding: utf-8 -*-
# Introducción al lenguaje de programacion Python
# Lección 7
# Estructuras de control de flujo - for


def cuadrados():
    """ Imprime el cuadrado de todos los x enteros tales que
        1 <= x <= 6
    """
    for x in [1, 2, 3, 4, 5, 6]:
        print(x**2)

cuadrados()
