# -*- coding: utf-8 -*-
# Herramientas para computación científica
# Lección 13
# Matplotlib: Títulos

import numpy
from matplotlib import pyplot


x = numpy.linspace(0, 1, 200)
y = numpy.sin(4 * numpy.pi * x) * numpy.exp(-5 * x)


pyplot.xlabel('x')
pyplot.ylabel('f(x)')
pyplot.title('f(x) = sin(4πx) e^(-5x)')

pyplot.axis([0, 1, -0.4, 0.6])
pyplot.grid(True)
pyplot.plot(x, y)

pyplot.show()
