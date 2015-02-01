# -*- coding: utf-8 -*-
# Introducción al lenguaje de programacion Python
# Lección 11
# Tuplas - Parte 2


def coordenadas_rectangulares(r, theta):
    x = r * cos(theta)
    y = r * sin(theta)
    return (x, y)


def escalar_por_vector(escalar, vector):
    x = escalar * vector[0]
    y = escalar * vector[1]
    return (x, y)


def main():
    vector = (4, 10)
    print(escalar_por_vector(2, vector))
    print(escalar_por_vector(0, vector))

main()
