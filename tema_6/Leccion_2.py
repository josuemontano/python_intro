# -*- coding: utf-8 -*-
# Conexión a bases de datos
# Lección 2
# SQLAlchemy: Conexión y sesión

from sqlalchemy.engine import create_engine
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.orm.session import sessionmaker

from Leccion_1 import Base

engine = create_engine('sqlite:///books.sqlite')
session = scoped_session(sessionmaker(bind=engine))
Base.metadata.bind = engine
