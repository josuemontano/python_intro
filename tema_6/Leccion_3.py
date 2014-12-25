# -*- coding: utf-8 -*-
# Conexión a bases de datos
# Lección 3
# SQLAlchemy: Queries

from Leccion_1 import Libro
from Leccion_2 import session


def todos_libros():
    return session.query(Libro).all()


def libros_recientes():
    return session.query(Libro).filter(Libro.anio_publicacion >= 2010).all()


def libros_por_titulo(titulo):
    return session.query(Libro).filter(Libro.titulo.startswith(titulo)).all()


def libros_recientes_por_titulo(titulo):
    return session.query(Libro).filter(Libro.anio_publicacion >= 2010, Libro.titulo.startswith(titulo)).all()


def cantidad_libros_editorial(editorial):
    return session.query(Libro).filter(Libro.editorial == editorial).count()


def main():
    print("Libros registrados:")
    for libro in todos_libros():
        print(libro.titulo)

    print("\nLibros recientes:")
    for libro in libros_recientes():
        print(libro.anio_publicacion, libro.titulo)

    print("\nLibros cuyo titulo empieza con 'Math':")
    for libro in libros_por_titulo('Math'):
        print(libro.anio_publicacion, libro.titulo)

if __name__ == '__main__':
    main()
