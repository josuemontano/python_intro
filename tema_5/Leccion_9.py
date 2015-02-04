# -*- coding: utf-8 -*-
# Herramientas para computación científica
# Lección 9
# SciPy: Derivación numérica

from scipy.misc import derivative
from scipy import sin, exp, pi


def f(t):
    return exp(-t) * sin(t)


def main():
    print("f'(0) =", derivative(f, 0))
    print("f''(0) =", derivative(f, 0, n=2))

if __name__ == '__main__':
    main()
