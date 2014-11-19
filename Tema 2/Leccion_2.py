# -*- coding: utf-8 -*-
# Introducción al lenguaje de programacion Python
# Lección 2
# Cadenas

print("Por favor introduzca su nombre completo:")
nombre = input()

print("Bienvenido, " + nombre + "!")
print("Tu nombre en mayusculas:", nombre.upper())
print("Tu nombre en minusculas:", nombre.lower())
print("Tu nombre sin espacios al inicio ni al final:", nombre.strip())
print("Tu nombre tiene", len(nombre), "caracteres")
print("Tu nombre tiene la vocal 'a'", nombre.count("a"), "veces")
print("Tu nombre con 50 caracteres (llenamos con 0s los faltantes)", nombre.zfill(50))
print("Tu nombre con 'f's en vez de 'a's", nombre.replace('a', 'f'))
