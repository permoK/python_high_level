def simple_delete(a_dictionary, key="languae"):
    # if key not in a_dictionary:
    #     print(a_dictionary)
    # else:
        a_dictionary.pop(key, 'default_value')
        print(a_dictionary)


a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3] }

simple_delete(a_dictionary)