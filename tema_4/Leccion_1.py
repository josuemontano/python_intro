# -*- coding: utf-8 -*-
# Programación funcional
# Lección 1
# Funciones de orden superior


def f(x):
   return x ** 2


def g(fu, x):
   return fu(x) * fu(x)

numero = 10
print(g(f, x))
