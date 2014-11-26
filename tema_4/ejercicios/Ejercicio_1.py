# -*- coding: utf-8 -*-
# Programación funcional
# Ejercicio 1
# Funciones lambda


def suma_cuadrados(a, b):
    return sum(map(lambda x: x ** 2, range(a, b + 1)))

if __name__ == '__main__':
    a = 11
    b = 20
    print(suma_cuadrados(a, b))
