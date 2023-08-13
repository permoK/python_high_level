def add_tuple(tuple_a=(1, 89, 6,7), tuple_b=(88,9,7 )):
    
    new = []
    empty_tuple = (0,)

    length_a = len(tuple_a)
    length_b = len(tuple_b)
    length = length_a

    print(length_b)
    
    if length_a > 2:
        length = 2
    
    elif length_b > 2:
        length = 2
    
    if length_a == 1 :
        tuple_a += empty_tuple
    
    elif length_b == 1:
        tuple_b += empty_tuple
        
    print(tuple_b)

    for i in range(length):
       
        new_tuple = (tuple_a[i] + tuple_b[i])

        new.append(new_tuple)
    print(tuple(new))

add_tuple()