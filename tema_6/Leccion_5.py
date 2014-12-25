# -*- coding: utf-8 -*-
# Conexión a bases de datos
# Lección 5
# SQLAlchemy: Actualización y eliminación de registros

from Leccion_1 import Libro
from Leccion_2 import session


def main():
    libro_a = session.query(Libro).filter(Libro.isbn == 1584884304).one()
    libro_a.titulo += ' and Engineers'
    session.commit()
    print("El libro {} ha sido actualizado".format(libro_a.isbn))

    libro_b = session.query(Libro).filter(Libro.isbn == 1584884304).one()
    session.delete(libro_b)
    session.commit()
    print("El libro {} ha sido eliminado".format(libro_b.titulo))

if __name__ == '__main__':
    main()
