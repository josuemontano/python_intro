# -*- coding: utf-8 -*-
# Introducción al lenguaje de programacion Python
# Ejercicio 5
# Suma de matrices


def suma_matricial(matriz_A, matriz_B):
    """ Funcion que, dadas las matrices A y B, devuelve la matriz A + B """
    if verificar_matrices_para_suma(matriz_A, matriz_B):
        # Construimos una matriz de la misma que la matriz B
        ans = [[0 for i in range(len(matriz_B[0]))] for j in range(len(matriz_B))]
        for i in range(len(matriz_A)):
            for j in range(len(matriz_A[0])):
                ans[i][j] = matriz_A[i][j] + matriz_B[i][j]
        return ans
    else:
        return None


def verificar_matrices_para_suma(matriz_A, matriz_B):
    """ Funcion que verifica si las matrices dadas pueden ser sumadas """
    return (len(matriz_A) == len(matriz_B)) and (len(matriz_A[0]) == len(matriz_B[0]))

matriz_A = [[1, 1],
            [5, 6],
            [3, 2]]
matriz_B = [[2, 9],
            [7, 7],
            [0, 0]]

print(suma_matricial(matriz_A, matriz_B))
