def replace_in_list(my_list, idx, element):
    length = len(my_list)
    if idx > length:
        print(my_list)
    elif idx < 0:
        print(my_list)
    else:
        my_list[idx] = element
        print(my_list)


replace_in_list([1,2,3,4,5], 0, 9)