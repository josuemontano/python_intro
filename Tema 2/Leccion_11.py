# -*- coding: utf-8 -*-
# Introducción al lenguaje de programacion Python
# Lección 11
# Recursividad


def fibonacci(n):
    """ Devuelve el n-ésimo número de la secuencia de Fibonacci """
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))
print(fibonacci(30))
