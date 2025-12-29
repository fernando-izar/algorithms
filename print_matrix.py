import numpy as np


def print_matrix(A: list):
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(A[i][j])


def fill_zero_matrix(rows, cols):
    return [[0] * cols for _ in range(rows)]


def multiply_matrices(A: list, B: list) -> list:
    if len(A[0]) != len(B):
        print("A column numbers must be equal to B line numbers")
    matrix = fill_zero_matrix(len(A), len(B[0]))
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A[0])):
                matrix[i][j] = matrix[i][j] + A[i][k] * B[k][i]
    return matrix


A = [[1, 2, 3]]
B = [
    [1, 1],
    [2, 2],
    [3, 3],
]
C = multiply_matrices(A, B)

A_ = np.array(A)
B_ = np.array(B)

C_ = A_ @ B_

print(C)
print(C_)
