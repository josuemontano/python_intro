# -*- coding: utf-8 -*-
# Programación orientada a objetos
# Lección 1
# Objetos y clases

import math


class Vector(object):
    """ Vector de 2D """

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __repr__(self):
        return str(tuple((self.x, self.y)))

    def magnitud(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def sumar(self, vector):
        """ Suma un vector a este vector """
        self.x += vector.x
        self.y += vector.y

    def multiplicar(self, escalar):
        """ Multiplica un escalar a este vector """
        self.x *= escalar
        self.y *= escalar

    def normalizar(self):
        self.x /= self.magnitud()
        self.y /= self.magnitud()

if __name__ == '__main__':
    velocidad = Vector(14.2, 18)
    print(velocidad.magnitud())

    velocidad.sumar(Vector(5, 1))
    velocidad.multiplicar(2.1)
    velocidad.normalizar()
    print(velocidad)
