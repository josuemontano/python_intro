# -*- coding: utf-8 -*-
# Herramientas para computación científica
# Lección 13
# Matplotlib: Gráfica simple

import numpy
from matplotlib import pyplot


x = numpy.linspace(0, 1, 200)
y = numpy.sin(4 * numpy.pi * x) * numpy.exp(-5 * x)

pyplot.plot(x, y)

pyplot.show()
