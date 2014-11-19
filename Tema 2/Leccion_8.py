# -*- coding: utf-8 -*-
# Introducción al lenguaje de programacion Python
# Lección 8
# Listas de listas

lista = [[1, 2, 4], [1, 1], [], [6]]
len(lista)

lista.sort()
print(lista)

lista.reverse()
print(lista)

lista.remove([6])
print(lista)

lista.append([5, 5, 0, 0, 3])
print(lista)

lista.insert(0, [2, [], 0])
print(lista)

lista.index([1, 1])
lista.count([])

lista.pop()
print(lista)
