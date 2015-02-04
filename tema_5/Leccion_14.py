# -*- coding: utf-8 -*-
# Herramientas para computación científica
# Lección 14
# Matplotlib: Rellenado

import numpy
from matplotlib import pyplot


x = numpy.linspace(0, 1, 200)
y = numpy.sin(4 * numpy.pi * x) * numpy.exp(-5 * x)

pyplot.fill(x, y, 'r')
pyplot.grid(True)

pyplot.show()
