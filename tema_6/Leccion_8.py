# -*- coding: utf-8 -*-
# Conexión a bases de datos
# Lección 8
# SQLAlchemy: Uso de relaciones de entidades

from Leccion_7 import Base, Libro
from sqlalchemy.exc import OperationalError
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.orm.session import sessionmaker

engine = create_engine('sqlite:///books_authors.sqlite')
session = scoped_session(sessionmaker(bind=engine))
Base.metadata.bind = engine


def main():
    try:
        libros = session.query(Libro).all()
        for libro in libros:
            print(libro.titulo, libro.autor.nombre)
    except OperationalError:
        print("Error al obtener los registros")

if __name__ == '__main__':
    main()
