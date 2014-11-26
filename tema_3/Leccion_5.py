# -*- coding: utf-8 -*-
# Programación orientada a objetos
# Lección 5
# Sobrecarga de operadores


class Fraccion(object):
    """ Fraccion, soporta los operadores +, *, == """

    def __init__(self, numerador, denominador=1):
        self.numerador = numerador
        self.denominador = denominador

    def __add__(self, other):
        if not isinstance(other, Fraccion):
            other = Fraccion(other)

        numerador = self.numerador * other.denominador + self.denominador * other.numerador
        denominador = self.denominador * other.denominador
        return Fraccion(numerador, denominador)

    def __mul__(self, other):
        if not isinstance(other, Fraccion):
            other = Fraccion(other)

        n1, d1 = self.numerador, self.denominador
        n2, d2 = other.numerador, other.denominador
        return Fraccion(n1 * n2, d1 * d2)

    def __eq__(self, other):
        if not isinstance(other, Fraccion):
            other = Fraccion(other)

        n1, d1 = self.numerador, self.denominador
        n2, d2 = other.numerador, other.denominador
        return n1 == n2 and d1 == d2

    def __str__(self):
        return "%s/%s" % (self.numerador, self.denominador)

    __repr__ = __str__

if __name__ == '__main__':
    fraccion_1 = Fraccion(1, 2)
    fraccion_2 = Fraccion(5, 3)

    print(fraccion_1 + fraccion_1)
    print(fraccion_1 * fraccion_2)
    print(fraccion_1 == fraccion_1)
