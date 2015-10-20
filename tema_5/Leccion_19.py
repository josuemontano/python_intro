# -*- coding: utf-8 -*-
# Herramientas para computación científica
# Lección 19
# SymPy: Manipulación algebraica

from sympy import expand, factor, simplify, symbols


def main():
    x, y = symbols("x y")
    print(x + y - x)
    print(x + 2 * y - 6 * x - 5 * x)

    expr = (x + x * y) / x
    print(simplify(expr))

    expr = x + y
    expr = x * expr
    print(expr)
    print(expand(expr))
    print(factor(expand(expr)))

if __name__ == '__main__':
    main()
