def print_matrix_integer(matrix=[[1,2,3],[4,5,6],[7,8,9]]):
    length = len(matrix)
    for i in range(length):
        print(matrix[i])


print_matrix_integer()


# !/usr/bin/python3
# def print_matrix_integer(matrix=[[]]):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if (j != 0):
#                 print(" ", end="")
#             print("{:d}".format(matrix[i][j]), end="")
#         print()