def simple_delete(a_dictionary, key="language"):
    a_dictionary.pop(key)
    print(a_dictionary)


a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3] }

simple_delete(a_dictionary)