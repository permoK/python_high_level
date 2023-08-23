def square_matrix_map(matrix=[[1, 2, 3],[4, 5, 6],[7, 8, 9]]):
    square = list(map(lambda x: list(map(lambda y: y*y, x)), matrix))

    print(square)



square_matrix_map()