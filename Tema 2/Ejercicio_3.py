# -*- coding: utf-8 -*-
# Introducción al lenguaje de programacion Python
# Ejercicio 3
# Series de Taylor

from math import factorial


def series_taylor_seno(x, n=50):
    ans = 0
    for i in range(n):
        _2np1 = (2 * n + 1)
        ans += ((-1) ** n) * (x ** _2np1) / factorial(_2np1)
    return ans

print(series_taylor_seno(5))
