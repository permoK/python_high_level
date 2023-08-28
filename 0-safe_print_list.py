def safe_print_list(my_list=[1, 2, 3, 4, 5], x=0):
    length = len(my_list)
    for i in range(x):
        print(i,end="")

#call the function
safe_print_list()