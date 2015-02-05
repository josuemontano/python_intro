# -*- coding: utf-8 -*-
# Herramientas para computación científica
# Lección 21
# Plotly

from numpy import linspace
from scipy import sin, pi
from plotly.graph_objs import Data, Scatter
from plotly.plotly import plot, sign_in


def main():
    x = linspace(0, 3 * pi, 300)
    t = x * sin(x)
    f = Scatter(x=x, y=t)

    # Reemplazar por las credenciales de su cuenta en plot.ly
    sign_in('', '')
    plot(Data([f]), filename='x sin(x)')


if __name__ == '__main__':
    main()
