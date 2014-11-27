# -*- coding: utf-8 -*-
# Herramientas para computación científica
# Lección 3
# Archivos: lectura

import os


directorio = os.getcwd()
archivo = open(directorio + os.sep + "Leccion_1.py", "r")

for linea in archivo:
    print(linea, end="")

archivo.close()
