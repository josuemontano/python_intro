# Introduccion al lenguaje de programacion Python
# Leccion 4
# Estructuras de control de flujo - if


def verificar_calificacion(calificacion=0):
    """ Si la calificacion es mayor o igual a 51 devuelve 'Aprobado', 
        'Reprobado' de lo contrario
    """
    if (calificacion >= 51):
        return "Aprobado"
    else:
        return "Reprobado"


calificacion = input()
verificar_calificacion(calificacion)
verificar_calificacion()
