# -*- coding: utf-8 -*-
# Herramientas para computación científica
# Lección 8
# SciPy: Estadística

from scipy import median, corrcoef, cov


a = [[1, 2, 3], [4, 5, 6]]

print(median(a))
print(corrcoef(a))
print(cov(a))
