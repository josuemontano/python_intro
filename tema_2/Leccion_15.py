# -*- coding: utf-8 -*-
# Introducción al lenguaje de programacion Python
# Lección 14
# Argumentos para main

import sys


def main(args):
    print('Número de argumentos:', len(args))
    print('Lista de argumentos:', args)

    print('Versión de python:', sys.version)

if __name__ == '__main__':
    # Este código se ejecutará únicamente cuando el modulo se ejecute como programa
    main(sys.argv[1:])
