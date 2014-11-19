# -*- coding: utf-8 -*-
# Introducción al lenguaje de programacion Python
# Ejercicio 4
# Números de Armstrong


def es_numero_Armstrong(n):
    """ Verifica si el número n dado es un número de Armstrong"""
    suma = 0
    temp = n
    while temp > 0:
        digito = temp % 10
        suma += digito ** 3
        temp //= 10
    return sum == n

try:
    numero = int(input("Introduzca un número: "))
except ValueError:
    print("El valor que introdujo no es un número")
else:
    if es_numero_Armstrong(numero):
        print("En número", numero, "es un número de Armstrong")
    else:
        print("En número", numero, "no es un número de Armstrong")
