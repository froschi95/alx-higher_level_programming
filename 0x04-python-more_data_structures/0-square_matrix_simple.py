#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_mat = []
    for row in matrix:
        squared_mat.append([i ** 2 for i in row])
    return squared_mat
