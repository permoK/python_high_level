def safe_print_list_integers(my_list=[1,2,3,"school",4,5], x=6):
    for i in range(x):
       
        try:
            if my_list[i] == int(my_list[i]):
                print(my_list[i],end='')
        except ValueError:
            pass
        except IndexError:
            print(f" list index out of range")
    
safe_print_list_integers()