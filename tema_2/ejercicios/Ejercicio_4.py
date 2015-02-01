# -*- coding: utf-8 -*-
# Introducción al lenguaje de programacion Python
# Ejercicio 4
# Expansión de Taylor para la función seno

from math import factorial


def seno_taylor(x, n=10):
    """ Aproximación de la función seno por expansión de Taylor """
    ans = 0
    for i in range(1, n):
        _2nm1 = (2 * i - 1)
        ans += pow(-1, i - 1) * pow(x, _2nm1) / factorial(_2nm1)
    return ans

print(seno_taylor(0.5))
print(seno_taylor(-0.01, 6))
