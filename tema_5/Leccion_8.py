# -*- coding: utf-8 -*-
# Herramientas para computación científica
# Lección 9
# SciPy: Estadística

from scipy import median, corrcoef, cov


def main():
    a = [[1, 2, 3], [4, 5, 6]]

    print(median(a))
    print(corrcoef(a))
    print(cov(a))

if __name__ == '__main__':
    main()
