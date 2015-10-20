# -*- coding: utf-8 -*-
# Útiles
# Lección 3
# Archivos: lectura

import os


def main():
    archivo_path = os.getcwd() + os.sep + "README.md"

    with open(archivo_path) as archivo:
        for linea in archivo:
            print(linea, end="")

if __name__ == '__main__':
    main()
