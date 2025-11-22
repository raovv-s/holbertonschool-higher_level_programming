#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
# I used map twice because we need to access each element like 2 for loops but with map
    squared_matrix = list(map(lambda row: list(map(lambda x: x**2, row)), matrix))
    return squared_matrix
