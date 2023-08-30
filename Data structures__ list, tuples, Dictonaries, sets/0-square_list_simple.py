#this fuction computes the square value of all integers of a matrix

def square_matrix_simple(matrix=[1,2,3]):
    new_matrix = matrix.copy()

    for i in range(len(matrix)):
        square = matrix[i] * matrix[i]
        new_matrix[i] = square

    print(new_matrix)
    print(matrix)



square_matrix_simple()