# -*- coding: utf-8 -*-
# Conexión a bases de datos
# Lección 3
# SQLAlchemy: Queries

from tema_6.Leccion_1 import Libro
from tema_6.Leccion_2 import session


def todos_libros():
    return session.query(Libro).all()


def libros_recientes():
    return session.query(Libro).filter(Libro.anio_publicacion >= 2010).all()


def libros_por_titulo(titulo):
    return session.query(Libro).filter(Libro.titulo.startswith(titulo)).all()


def main():
    for libro in todos_libros():
        print(libro.titulo)

    for libro in libros_recientes():
        print(libro.fecha_publicacion, libro.titulo)

    for libro in libros_por_titulo('Math'):
        print(libro.fecha_publicacion, libro.titulo)

if __name__ == '__main__':
    main()
