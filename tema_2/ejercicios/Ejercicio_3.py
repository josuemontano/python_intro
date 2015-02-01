# -*- coding: utf-8 -*-
# Introducción al lenguaje de programacion Python
# Ejercicio 3
# Números primos


def es_numero_primo(n):
    """ Verifica si el número n dado es primo """
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return False
        return True
    else:
        return False


def main():
    print(es_numero_primo(401))

main()
