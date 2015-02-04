# -*- coding: utf-8 -*-
# Herramientas para computación científica
# Lección 15
# Matplotlib: Rellenado

from numpy import exp, linspace, sin, pi
from matplotlib.pyplot import fill, grid, show


def main():
    x = linspace(0, 1, 200)
    y = sin(4 * pi * x) * exp(-5 * x)

    fill(x, y, 'r')
    grid(True)
    show()

if __name__ == '__main__':
    main()
