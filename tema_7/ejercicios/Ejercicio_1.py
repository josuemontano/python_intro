# -*- coding: utf-8 -*-
# Útiles
# Ejercicio 1
# Lectura de archivo de coordenadas

import os
from random import randint


def parsear_archivo(archivo_path):
    """ Funcion que recibe la direccion completa de un archivo, lo lee y
        convierte cada linea en una lista. Todas estas se almacenan en
        una lista llamada coordenadas la cual se devuelve.
    """
    coordenadas = []
    with open(archivo_path) as archivo:
        for linea in archivo:
            coordenadas.append(linea.split())
    return coordenadas


def main():
    coordenadas = parsear_archivo(os.getcwd() + os.sep + "coordenadas.txt")
    print("El archivo contiene", len(coordenadas), "coordenadas")
    
    rand_i = randint(0, len(coordenadas) - 1)
    print("Coordenada randomica", coordenadas[rand_i])

if __name__ == '__main__':
    main()
