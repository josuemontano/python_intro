# -*- coding: utf-8 -*-
# Programación interactiva en Python
# Lección 14
# Módulo random

from random import *


print(random())
print(uniform(0.8, 10))
print(triangular(0.8, 10, 0.2))

print(gammavariate(3.1, 0.8))
print(gauss(3.1, 0.8))

print(randrange(0, 10))
print(randrange(0, 10, 4))
print(randint(0, 10))
