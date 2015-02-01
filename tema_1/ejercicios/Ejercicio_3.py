# -*- coding: utf-8 -*-
# Programación interactiva en Python
# Ejercicio 3
# Coordenadas polares a rectangulares

from math import cos
from math import sin
from math import pi


def coordenada_x(r, theta):
    """ Dados (r, theta) coordenadas polares, devuelve r*cos(theta) """
    return r * cos(theta)


def coordenada_y(r, theta):
    """ Dados (r, theta) coordenadas polares, devuelve r*sin(theta) """
    return r * sin(theta)

r = 10.0
theta = pi / 3
print(coordenada_x(r, theta), coordenada_y(r, theta))
