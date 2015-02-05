# -*- coding: utf-8 -*-
# Herramientas para computación científica
# Ejercicio 1
# Gráfica de f(x) = x*sin(x)

from numpy import linspace, pi, sin
from matplotlib.pyplot import plot, show, xlabel, ylabel


def f(x):
    return x * sin(x)


def main():
    t = linspace(0, 3 * pi, 250)
    
    plot(t, f(t))
    xlabel("t [sec]")
    ylabel("f(t) = t*sin(t)")
    show()

main()
