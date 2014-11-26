# -*- coding: utf-8 -*-
# Matplotlib
# Ejercicio 1
# Gráfica de la función seno

from numpy import linspace, pi, sin
from matplotlib import pyplot


x = linspace(-pi, pi, 201)

pyplot.plot(x, sin(x))
pyplot.xlabel("ángulo [rad]")
pyplot.ylabel("sin(x)")
pyplot.show()
