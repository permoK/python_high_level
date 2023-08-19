#this fuction computes the square value of all integers of a matrix
def square_matrix_simple(matrix=[[1, 2, 3],[4, 5, 6],[7, 8, 9]]):
    new_matrix = []

    for i in matrix:
        row = []
        for j in i:
            row.append(j**2)
        new_matrix.append(row)
            # new_matrix[i][j] = square
            # print(square)

    print(matrix)
    print(new_matrix)


square_matrix_simple()