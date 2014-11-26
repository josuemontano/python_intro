# -*- coding: utf-8 -*-
# Programación funcional
# Lección 6
# filter

pares = filter(lambda x: x if (x % 2) == 0 else None, range(10))
print(list(pares))

menores_6 = filter(lambda x: x < 6, range(10))
print(list(menores_6))
