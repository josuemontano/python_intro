# -*- coding: utf-8 -*-
# Herramientas para computación científica
# Lección 14
# Matplotlib: Títulos

from numpy import exp, linspace, sin, pi
from matplotlib import pyplot


def main():
    x = linspace(0, 1, 200)
    y = sin(4 * pi * x) * exp(-5 * x)

    pyplot.xlabel('x')
    pyplot.ylabel('f(x)')
    pyplot.title('f(x) = sin(4πx) e^(-5x)')

    pyplot.axis([0, 1, -0.4, 0.6])
    pyplot.grid(True)
    pyplot.plot(x, y)
    pyplot.show()

if __name__ == '__main__':
    main()
