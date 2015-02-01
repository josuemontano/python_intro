# -*- coding: utf-8 -*-
# Introducción al lenguaje de programacion Python
# Lección 3
# Estructuras de control de flujo - if


def es_par(n):
    """ Verifica si el numero n dado es par """
    if (n % 2) == 0 and n >= 0:
        return True
    else:
        return False


def main():
    numero = int(input("Introduzca un numero: "))
    if not es_par(numero):
        print(numero, "es impar")
    else:
        print(numero, "es par")

main()
