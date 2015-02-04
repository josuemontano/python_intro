# -*- coding: utf-8 -*-
# Herramientas para computación científica
# Lección 13
# Matplotlib: Gráfica simple

from numpy import exp, linspace, pi, sin
from matplotlib.pyplot import plot, show


def main():
    x = linspace(0, 1, 200)
    y = sin(4 * pi * x) * exp(-5 * x)
    
    plot(x, y)
    show()

if __name__ == '__main__':
    main()
