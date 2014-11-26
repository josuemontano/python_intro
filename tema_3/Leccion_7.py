# -*- coding: utf-8 -*-
# Programación orientada a objetos
# Lección 7
# Módulo decimal

from decimal import Decimal, localcontext


a = Decimal(0.1)
b = Decimal(0.2)

print(a + b)
print(a - b)
print(a * b)
print(a / b)

print(a % b)
print(a // b)

print(a ** b)

with localcontext() as ctx:
    ctx.prec = 50
    print(Decimal(1) / Decimal(9))


# Otros constructores
a = Decimal('3e-10')
print(a)
