def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
                
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except IndexError:
            print('out of range')
            result = 0
        except TypeError:
            print('wrong type') 
        finally:
            new_list.append(result)
    print(new_list)

my_list_1 = [10, 8, 4, 4] 
my_list_2 = [2, 0, "H", 2, 7]
list_length = (max(len(my_list_1), len(my_list_2)))
print(list_division(my_list_1, my_list_2, list_length))