#this function finds the biggest integer of a list 
def max_integer(my_list=[1, 90, 2, 13, 34, 5, -13, 3]):
    #declare variable
    max_value = 0
    #find the length of the string
    length = len(my_list)

    #search for the largest integer in the loop
    for i in range(length):
        #check if the largest variable is the largest in the loop
        if max_value < my_list[i]:
            max_value = my_list[i]
    #print the largest integer after the loop reaches the end
    print("Max: {}".format(max_value))


#calling the function
max_integer()