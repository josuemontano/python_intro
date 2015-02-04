# -*- coding: utf-8 -*-
# Programación orientada a objetos
# Lección 6
# Encapsulación


class Vector(object):
    """ Vector de 2D """

    def __init__(self, x, y):
        super(Vector, self).__init__()
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise Exception("No es un dato valido")
        self.__x = x


def main():
    velocidad = Vector(2, 0)
    velocidad.x = 2

    print(velocidad.x)

if __name__ == '__main__':
    main()
