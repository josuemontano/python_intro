# Introduccion al lenguaje de programacion Python
# Ejercicio 1
# Sucesion de Fibonacci


def obtener_sucesion_fibonacci(n):
    """ Devuelve una lista con todos los x pertenecientes a la sucesion de Fibonacci
        tales que x > n
    """
    sucesion = []
    a, x = 0, 1
    while x < n:
        sucesion.append(x)
        a, x = x, a + x
    return sucesion
