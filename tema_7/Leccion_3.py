# -*- coding: utf-8 -*-
# Útiles
# Lección 3
# Archivos: lectura

import os


with open(os.getcwd() + os.sep + "README.md") as archivo:
    for linea in archivo:
        print(linea, end="")
