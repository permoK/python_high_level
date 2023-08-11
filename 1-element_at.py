def element_at(my_list, idx):
    length = len(my_list)
    if idx >= length:
        return None
    elif my_list[idx] < 0:
        return None
    else:
        return my_list[idx  ]


print(element_at([1,2,3,4,-5], 5))