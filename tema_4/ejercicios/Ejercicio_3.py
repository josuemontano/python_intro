# -*- coding: utf-8 -*-
# Programación funcional
# Ejercicio 3
# Tamaño total de archivos python

import functools
import os


files = os.listdir(myPath)
files = filter(lambda x: x.endswith(".py"), files)
if len(files) > 0:
    tamano = functools.reduce(operator.add, map(os.path.getsize, files))
    print(tamano)
else
    print(0)
