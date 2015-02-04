# -*- coding: utf-8 -*-
# Herramientas para computación científica
# Ejercicio 2
# Gráfica de f(x) = x*sin(x) y f'(x)

from numpy import linspace, pi, sin
from matplotlib.pyplot import plot, show


def f(x):
    return x * sin(x)


def derivada(f, x):
    """ Devuelve la derivada de una funcion f dada
        en el punto x
    """
    dx = 0.01
    dy = f(x + dt) - f(x)
    return dy / dx


def main():
    t = linspace(-pi, pi, 200)

    plot(t, f(t))
    plot(t, derivada(f, t), '+')
    show()

main()
