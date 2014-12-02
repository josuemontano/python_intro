# -*- coding: utf-8 -*-
# Conexión a bases de datos
# Lección 6
# SQLAlchemy: Estados de una entidad

from Leccion_1 import Libro
from Leccion_2 import session
from sqlalchemy import inspect


def mostrar_estado(objeto):
    estado = inspect(objeto)
    print('Transient: {0}; Pending: {1}; Persistent: {2}; Detached: {3}'.format(estado.transient, estado.pending, estado.persistent, estado.detached))


def main():
    libro = Libro(isbn=814758371, titulo='Gödel\'s Proof', anio_publicacion=2008, editorial='McGraw Hill')
    mostrar_estado(libro)

    session.add(libro)
    mostrar_estado(libro)

    session.commit()
    mostrar_estado(libro)

    session.delete(libro)
    session.commit()
    mostrar_estado(libro)

if __name__ == '__main__':
    main()
