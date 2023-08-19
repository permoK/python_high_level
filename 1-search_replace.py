#function that replaces all occurrences of an element by another in a new list
def search_replace(my_list, search, replace):
    value = list(map(lambda a: replace if a == search else a, my_list))
    print(value)

my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
search = 2
replace = 89
search_replace(my_list,search,replace)