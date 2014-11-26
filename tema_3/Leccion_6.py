# -*- coding: utf-8 -*-
# Programación orientada a objetos
# Lección 6
# Encapsulación


class Vector(object):

    def __init__(self, x, y):
        super(Vector, self).__init__()
        self.__x = x
        self.__y = y

if __name__ == '__main__':
    velocidad = Vector(2, 0)
    velocidad.__x
