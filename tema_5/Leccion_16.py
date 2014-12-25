# -*- coding: utf-8 -*-
# Herramientas para computación científica
# Lección 16
# 

from sympy import *

x = Symbol('x')
ans = integrate(x/(x**2+2*x+1), x)

nsimplify(ans, [pi])
