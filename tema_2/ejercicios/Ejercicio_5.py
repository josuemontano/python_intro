# -*- coding: utf-8 -*-
# Introducción al lenguaje de programacion Python
# Ejercicio 5
# Aproximación de log(1 + x)


def log_1px(x, n=15):
    """ Aproximación de la función log(1+x) por expansión de Taylor """
    suma = 0
    k = 1
    while k <= n:
        suma = suma + ((-1) ** k * x ** k) / k
        k = k + 1

    return suma


def main():
    print(log_1px(0.1))
    print(log_1px(0.1, 100))

main()
