def print_reversed_list_integer(my_list=[1,2,3,4,5]):
    length = len(my_list)
    for i in range(length):
        print("{}".format(my_list[length-1-i]))

print_reversed_list_integer()