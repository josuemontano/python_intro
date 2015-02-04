# -*- coding: utf-8 -*-
# Herramientas para computación científica
# Lección 20
# 

from sympy import *


x = Symbol('x')
ans = integrate(x/(x**2+2*x+1), x)

print(ans)
print(nsimplify(ans, [pi]))
