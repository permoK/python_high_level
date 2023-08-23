def complex_delete(a_dictionary, value):
    for i in a_dictionary:
        if a_dictionary[i] != value:
            values = (a_dictionary[i])
            key = i
            print(f"{key}: {values}")


complex_delete(a_dictionary={'lang': "C", 'track': "Low", 'pref': "C", 'ids': [1, 2, 3]}, value='C')