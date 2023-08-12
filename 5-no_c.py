def no_c(my_string):
    length = len(my_string)
    for i in range(length):
       if my_string[i] != 'c':
           print(my_string[i], end='')
no_c("kfc is my school")