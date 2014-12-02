# -*- coding: utf-8 -*-
# Conexión a bases de datos
# Lección 5
# SQLAlchemy: Creación de registros

from Leccion_1 import Libro
from Leccion_2 import session
from Leccion_3 import libros_recientes_por_titulo, cantidad_libros_editorial
from sqlalchemy.exc import IntegrityError


def main():
    editorial = 'Wiley'
    logica = Libro(isbn='0486425337', titulo='Mathematical Logic', anio_publicacion=2014, editorial=editorial)
    session.add(logica)

    libreria = Libro(isbn='1584884304', titulo='A Numerical Library in Java for Scientists and Engineers', anio_publicacion=2003, editorial=editorial)
    session.add(libreria)

    session.commit()

    for libro in libros_recientes_por_titulo('Ma'):
        print(libro.titulo)
    print("Existen {} libros de la editorial {}".format(cantidad_libros_editorial(editorial), editorial))

if __name__ == '__main__':
    main()
