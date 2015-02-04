# -*- coding: utf-8 -*-
# Programación funcional
# Lección 1
# Funciones de orden superior


def f(x):
    return x ** 2


def g(fu, x):
    return fu(x) * fu(x)


def main():
    numero = 3
    print(g(f, numero))

if __name__ == '__main__':
    main()
