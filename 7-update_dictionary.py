def update_dictionary(a_dictionary, key, value):
    # new_dict = key=value
    a_dictionary[key] = value
    print(a_dictionary)
    
    
a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
key = "language"
value = "python"
update_dictionary(a_dictionary, key, value)