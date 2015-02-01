# -*- coding: utf-8 -*-
# Introducción al lenguaje de programacion Python
# Lección 3
# Estructuras de control de flujo - while


def obtener_sucesion_fibonacci(n):
    """ Imprime todos los x pertenecientes a la sucesion de Fibonacci
        tales que x > n
    """
    a = 0
    x = 1
    while x < n:
        print(x)
        tmp = x
        x = x + a
        a = tmp


def main():
    obtener_sucesion_fibonacci(50)

main()
