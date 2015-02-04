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
    logica = Libro(isbn=486425337, titulo='Mathematical Logic', anio_publicacion=2014, editorial=editorial)
    session.add(logica)

    libreria = Libro(isbn=1584884304, titulo='A Numerical Library in Java for Scientists', anio_publicacion=2003, editorial=editorial)
    session.add(libreria)
    try:
        session.commit()
    except IntegrityError:
        print("Error al persistir. Estos registros ya existen")
        session.rollback()

    print("Los siguientes libros son recientes y empiezan con 'Ma':")
    for libro in libros_recientes_por_titulo('Ma'):
        print(libro.titulo)
    
    print("\nExisten {} libros de la editorial {}".format(cantidad_libros_editorial(editorial), editorial))

if __name__ == '__main__':
    main()
