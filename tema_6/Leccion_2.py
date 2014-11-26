# -*- coding: utf-8 -*-
# Herramientas para computación científica
# Lección 2
# Formato de cadenas

x = 1/3

print("%.5f" % x)
print("%10.5f" % x)

print("{:.5f}".format(x))
print("{:10.5f}".format(x))

tupla = (1, 2)
print("{0} es mayor que {1}".format(*tupla))
