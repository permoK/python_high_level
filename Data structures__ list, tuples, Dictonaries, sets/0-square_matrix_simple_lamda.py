#this fuction computes the square value of all integers of a matrix
def square_matrix_simple(matrix=[[[1,2,3], [4,5,6]], [[1,2,3], [4,5,6]], [[1,2,3], [4,5,6]]]):

    new = list(map(lambda x: list(map(lambda y: list(map(lambda a: a*a, y)), x)), matrix))

    print(new)


square_matrix_simple()