def number_keys(a_dictionary):
    nb_keys = 0
    for i in a_dictionary:
        nb_keys += 1


    print(nb_keys)


a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level"  }

number_keys(a_dictionary)