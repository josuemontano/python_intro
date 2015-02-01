# -*- coding: utf-8 -*-
# Programación funcional
# Ejercicio 3
# Tamaño total de archivos python

import functools
import os
import operator
import sys


def obtener_tamano_directorio(directorio=None):
    archivos = os.listdir(directorio)
    lista = list(filter(lambda x: x.endswith(".py"), archivos))
    if len(lista) > 0:
        return functools.reduce(operator.add, map(os.path.getsize, lista))
    else:
        return 0


def main():
    if len(sys.argv) > 1:
        tamano = obtener_tamano_directorio(sys.argv[1])
    else:
        tamano = obtener_tamano_directorio()

    print("La carpeta contiene", tamano, "B")

if __name__ == '__main__':    
    main()
