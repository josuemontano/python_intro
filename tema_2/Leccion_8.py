# -*- coding: utf-8 -*-
# Introducción al lenguaje de programacion Python
# Lección 8
# La función range()


def cuadrados(n):
    """ Imprime el cuadrado de todos los x enteros tales que
        0 <= x < n
    """
    for x in range(n):
        print(x**2)

cuadrados(30)
