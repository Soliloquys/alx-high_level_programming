#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    a = len(matrix)
    if a > 0:
        for i in range(0, a):
            new_matrix = matrix[i]
            b = len(new_matrix)
            for i in range(0, b):
                if i < b - 1:
                    print("{:d} ".format(new_matrix[i]), end="")
                else:
                    print("{:d}".format(new_matrix[i]), end="")
            print()
