# Introduccion al lenguaje de programacion Python
# Leccion 7
# Accediento a listas

fibonacci = [1, 1, 2, 3, 4, 5, 8, 13, 21, 34]

fibonacci[0]
fibonacci[3:]
fibonacci[:3]
fibonacci[2:7]

fibonacci[3:6] = []
print(fibonacci)

copia = fibonacci[:]
copia.reverse()
print(copia, fibonacci)
