# -*- coding: utf-8 -*-
# Introducción al lenguaje de programacion Python
# Ejercicio 8
# Suma de matrices


def suma_matricial(A, B):
    """ Función que, dadas las matrices A y B, devuelve la matriz A + B """
    if verificar_matrices_para_suma(A, B):
        # Construimos una matriz de la misma que la matriz B
        ans = [[0 for i in range(len(B[0]))] for j in range(len(B))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                ans[i][j] = A[i][j] + B[i][j]
        return ans
    else:
        return None


def verificar_matrices_para_suma(A, B):
    """ Verifica si las matrices dadas pueden ser sumadas """
    return (len(A) == len(B)) and (len(A[0]) == len(B[0]))

matriz_A = [[1, 1],
            [5, 6],
            [3, 2]]
matriz_B = [[2, 9],
            [7, 7],
            [0, 0]]


def main():
    print(suma_matricial(matriz_A, matriz_B))

main()
