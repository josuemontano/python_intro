# -*- coding: utf-8 -*-
# Programación interactiva en Python
# Lección 14
# Módulo random

from random import *


print(random())                 # Float randómico en el intervalo [0.0, 1.0)
print(uniform(0.8, 10))         # Float randómico N tal que 0.8 <= N <= 10
print(triangular(0.8, 10, 0.2)) # 

print(gammavariate(3.1, 0.8))   # Distribución gamma
print(gauss(3.1, 0.8))          # Distribución normal. 3.1 = media, 0.8 = desviación estándar

print(randrange(0, 10))         # Entero de 0 a 9
print(randrange(0, 10, 4))      # Entero de 0 a 9 divisible entre 4
print(randint(0, 10))           # randrange(0, 10+1)
