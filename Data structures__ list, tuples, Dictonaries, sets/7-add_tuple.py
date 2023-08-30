#This function adds two tuple elemets
def add_tuple(tuple_a=(1, 89, 6,7), tuple_b=(88,9,7 )):
    #initiate an empty list and a tuple whose contents are zero
    new = []
    zero_tuple = (0,)
    #find the length of the tuples
    length_a = len(tuple_a)
    length_b = len(tuple_b)
    length = length_a
    # restrict the number of elements to add in a tuple
    if length_a > 2:
        length = 2
    elif length_b > 2:
        length = 2
    #add the zero tuple when there is a tuple with less than one element
    if length_a == 1 :
        tuple_a += zero_tuple
    elif length_b == 1:
        tuple_b += zero_tuple
    #iterate while adding the tuple elements
    for i in range(length):
       #add the elements
        new_tuple = (tuple_a[i] + tuple_b[i])
        #append the elements in a list
        new.append(new_tuple)
    #convert and print out the list as a tuple
    print(tuple(new))
# call the function
add_tuple()