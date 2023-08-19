#this fuction computes the square value of all integers of a matrix
def square_matrix_simple(matrix=[[1, 2, 3],[4, 5, 6],[7, 8, 9]]):
    new = [[i * i for i in row] for row in matrix]

    print(new)

square_matrix_simple()
