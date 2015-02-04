# -*- coding: utf-8 -*-
# Introducción al lenguaje de programacion Python
# Ejercicio 1
# Sucesión de Fibonacci


def obtener_sucesion_fibonacci(n):
    """ Devuelve una lista con todos los x pertenecientes a la sucesión de
        Fibonacci tales que x > n
    """
    sucesion = []
    a, x = 0, 1
    while x < n:
        sucesion.append(x)
        a, x = x, a + x
    return sucesion


def main():
    print(obtener_sucesion_fibonacci(180))
    print(obtener_sucesion_fibonacci(1800))

main()
