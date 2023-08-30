def safe_print_list(my_list=[1, 2, 3, 4, 5], x=9):
    # length = len(my_list)
    try:
        for i in range(x):
            print(my_list[i],end="")
    except IndexError:
        print("  x is greater than the length of the list")

#call the function
safe_print_list()