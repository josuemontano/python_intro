# -*- coding: utf-8 -*-
# Programación funcional
# Lección 3
# Funciones lambda

from math import cos, pi, tan


suma_tres = lambda x, y, z: x + y + z
print(suma_tres(1, 2, 3))

coseno = lambda x: cos(x) if x > 0 else None
tan_cos = lambda x: tan(coseno(x))
print(tan_cos(pi))
