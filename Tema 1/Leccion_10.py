# Programación interactiva en Python
# Leccion 10
# Funciones del modulo math

from math import *


x = 900
factorial(x)

x = 7.3890561
fabs(x)
ceil(x)
floor(x)

x = pi
y = e
fmod(x, y) # Preferible para floats, x % y preferible para enteros


# Funciones trigonometricas
x = pi
cos(x)
sin(x)
tan(x)

x = -1
acos(x)
asin(x)
atan(x)

# Funciones hiperbolicas
x = e
cosh(x)
sinh(x)
tanh(x)

x =
acosh(x)
asinh(x)
atanh(x)

# Conversion de angulos
degrees(pi)
radians(90)

# Funciones logaritmicas y exponenciales
x = 9
exp(x)
expm1(x)  # e**x - 1

log(x, 2)
log10(x)  # Mas preciso que log(x, 10)
log1p(x)  # log(1 + x, e)

x = 2
y = 5
sqrt(x)
pow (x, y)
