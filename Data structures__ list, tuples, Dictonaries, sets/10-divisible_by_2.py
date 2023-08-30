#this function finds all multiples of 2 in a list
def divisible_by_2(my_list=[0,1,2,3,4,5,6]):
    #find the length of the list
    length = len(my_list)
    #list container to store the newlist
    new_list = []

    #loop through the list checking for multiples of 2
    for i in range(length):
        #check through the list items one by one if it is divisible by 2
        if my_list[i] % 2 == 0:
            
            print("{:d} {:s} divisible by 2".format(my_list[i], "is" ))
            divisible = True
            #append the results in the variable
            new_list.append(divisible)
        else:
            print("{:d} {:s} not divisible by 2".format(my_list[i], "is" ))
            not_divisible = False

            new_list.append(not_divisible)
    print("{}".format(new_list))


#call the function
divisible_by_2()