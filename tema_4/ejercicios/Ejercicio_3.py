# -*- coding: utf-8 -*-
# Programación funcional
# Ejercicio 3
# Tamaño total de archivos python

import functools
import os
import operator
import sys


if __name__ == '__main__':
    files = os.listdir(sys.argv[1])
    files = filter(lambda x: x.endswith(".py"), files)
    if len(list(files)) > 0:
        tamano = functools.reduce(operator.add, map(os.path.getsize, files))
        print(tamano)
    else:
        print(0)
