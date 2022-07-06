#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new_mat = list(map(lambda x: list(map(lamda y: y ** 2, x)), matrix))
