def new_in_list(my_list, idx, element):
    new_list = my_list[0:]
    length = len(my_list)
    if idx >= length:
        print(my_list)

    elif idx < 0:
        print(my_list)

    else:
        new_list[idx] = element
        print(new_list)
        print(my_list)


new_in_list([1,2,3,4,5], -1, 9)