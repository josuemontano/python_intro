# -*- coding: utf-8 -*-
# Programación funcional
# Ejercicio 2
# Mayores de edad


class Persona(object):

    def __init__(self, nombre, edad):
        super(Persona, self).__init__()
        self.nombre = nombre
        self.edad = edad

    def __repr__(self):
        return self.nombre

    def __str__(self):
        return self.nombre


def main():
    estudiantes = [Persona("Peter", 37), Persona("Laura", 8), Persona("Paul", 22), Persona("Bruce", 18)]
    mayores_edad = filter(lambda x: x if x.edad >= 19 else None, estudiantes)
    print(list(mayores_edad))

if __name__ == '__main__':
    main()