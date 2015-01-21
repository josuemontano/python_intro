# -*- coding: utf-8 -*-
# Útiles
# Lección 3
# Archivos: lectura

import os


directorio = os.getcwd()
with open(directorio + os.sep + "Leccion_1.py") as archivo:
    for linea in archivo:
        print(linea, end="")
