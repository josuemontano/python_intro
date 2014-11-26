# -*- coding: utf-8 -*-
# Programación funcional
# Ejercicio 1
# Funciones lambda


def suma_cuadrados(a, b):
    return sum(map(lambda x: x ** 2, range(a, b + 1)))

a = 0
b = 5
print(suma_cuadrados(a, b))
