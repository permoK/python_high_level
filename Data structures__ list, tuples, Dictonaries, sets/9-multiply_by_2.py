def multiply_by_2(a_dictionary):

    keys = (list(a_dictionary.keys()))
    keys.sort()
    length = len(keys)

    for i in range(length):
        print(f"{keys[i]}: {a_dictionary[keys[i]]*2}")


a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}

multiply_by_2(a_dictionary)