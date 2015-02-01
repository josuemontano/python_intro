# -*- coding: utf-8 -*-
# Introducción al lenguaje de programacion Python
# Lección 12
# Exepciones


def convertir_a_Farenheit(temperatura_Celcius=0):
    """ Devuelve la temperatura dada en escala Farenheit """
    return 9 / 5 * temperatura_Celcius + 32


def main():
    try:
        numero = int(input("Introduzca un numero: "))
    except ValueError:
        print("El valor que introdujo no es un numero")
    else:
        print(convertir_a_Farenheit(numero))

main()