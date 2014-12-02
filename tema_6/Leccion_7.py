# -*- coding: utf-8 -*-
# Conexión a bases de datos
# Lección 7
# SQLAlchemy: Mapeo de relaciones

from sqlalchemy import create_engine, Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

Base = declarative_base()


class Autor(Base):
    __tablename__ = 'bxauthors'

    id     = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column('name', String(100), nullable=False)


class Libro(Base):
    __tablename__ = 'bxbooks'

    isbn             = Column(Integer, primary_key=True)
    titulo           = Column('book_title', String(200), nullable=False)
    anio_publicacion = Column('year_published', Integer, default=2014)
    editorial        = Column('publisher', String(100))
    author_id        = Column(Integer, ForeignKey('bxauthors.id'), nullable=False)

    autor = relationship(Autor)


def main():
    engine = create_engine('sqlite:///books_authors.sqlite')
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    main()
