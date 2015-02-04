# -*- coding: utf-8 -*-
# Introducción al lenguaje de programacion Python
# Lección 5
# Listas

fibonacci = [2, 34, 5, 1, 21, 3, 8, 13, 4]
print(len(fibonacci))

fibonacci.sort()
print(fibonacci)

fibonacci.reverse()
print(fibonacci)

fibonacci.remove(4)
print(fibonacci)

fibonacci.append(55)
print(fibonacci)

fibonacci.sort()
fibonacci.insert(0, 1)
print(fibonacci)

print(fibonacci.index(21))
print(fibonacci.count(1))

fibonacci.extend([89, 144])
print(fibonacci)

x = fibonacci.pop()
print(fibonacci, x)

# Lista vacía
vacia = []
print(len(vacia))

vacia += [-2, -1, 0]
print(vacia)
