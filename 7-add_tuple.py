def add_tuple(tuple_a=(1, 89), tuple_b=(88, 11)):
    new = []
    length = len(tuple_a)
    for i in range(length):
        new_tuple = (tuple_a[i] + tuple_b[i])
        new.append(new_tuple)
    print(tuple(new))

add_tuple()