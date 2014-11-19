# Programación interactiva en Python
# Leccion 8
# Importacion de modulos

from math import pi


def calcular_volumen_esfera():
    """ Funcion que calcula el volumen de una esfera
        de radio 7
        V = (4/3)πr^3
    """
    radio = 7
    return 4/3 * pi * radio ** 3


print(calcular_volumen_esfera())
