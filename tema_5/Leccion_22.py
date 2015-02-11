# -*- coding: utf-8 -*-
# Herramientas para computación científica
# Lección 22
# Plotly: Gráficos en coordenadas polares

from numpy import linspace
from scipy import sin, radians
from plotly.graph_objs import Data, Scatter
from plotly.plotly import plot, sign_in


def main():
    theta = linspace(0, 360, 360)
    r = 1 + sin(radians(theta))
    f = Scatter(r=r, t=theta)

    # Reemplazar por las credenciales de su cuenta en plot.ly
    sign_in('', '')
    plot(Data([f]), filename='1 + sin(theta)')

if __name__ == '__main__':
    main()
