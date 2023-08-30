#This function deletes an item at a specific position in a list
def delete_at(my_list=[1,2,3,4,5], idx=5):
    #declare an empty list to store the new list
    new_list = []

    #find the length of the list 
    length = len(my_list)
    
    #check if the idx is negative or out of range
    if idx < 0 or idx >= length:
        print (my_list)
    else:
        #delete the element in idx specified
        for i in range(length):
            if i != idx:
                #store the remaining elements and append them in the new_list variable
                elements = my_list[i]
                new_list.append(elements)
        my_list = new_list
        #print the new and updated list
        print(new_list)
        print(my_list)


#calling the function
delete_at()