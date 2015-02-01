# -*- coding: utf-8 -*-
# Introducción al lenguaje de programacion Python
# Ejercicio 2
# Producto de Wallis


def pi_wallis(n):
    """ Producto de Wallis para π """
    producto = 1
    k = 1
    while k <= n:
        producto *= (2 * k) ** 2 / (2 * k + 1) / (2 * k - 1)
        k += 1

    return producto * 2

print(pi_wallis(500))
print(pi_wallis(500000))
