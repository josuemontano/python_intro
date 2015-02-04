# -*- coding: utf-8 -*-
# Introducción al lenguaje de programacion Python
# Ejercicio 7
# Movimiento parabólico

from math import cos, sin, pi


def movimiento_parabolico(y0=0, v0=0, angulo=0):
    t = 0
    x = 0
    y = y0
    theta = angulo * pi / 180
    tabla = []
    while y >= 0:
        tabla.append([x, y])
        x = v0 * cos(theta) * t
        y = y0 + v0 * sin(theta) * t - 0.5 * 9.81 * t ** 2
        t = t + 0.05
    
    return tabla


def main():
    tabla = movimiento_parabolico(y0=2, v0=10, angulo=30)
    print(tabla)

main()
