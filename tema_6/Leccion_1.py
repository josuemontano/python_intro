# -*- coding: utf-8 -*-
# Conexión a bases de datos
# Lección 1
# SQLAlchemy: Mapeo de tablas, creación de la base de datos

from sqlalchemy import create_engine, Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Libro(Base):
    __tablename__ = 'bxbooks'

    isbn             = Column(Integer, primary_key=True)
    titulo           = Column('book_title', String(200), nullable=False)
    anio_publicacion = Column('year_published', Integer, default=2014)
    editorial        = Column('publisher', String(100))


def main():
    engine = create_engine('sqlite:///books.sqlite', echo=True)
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    main()
