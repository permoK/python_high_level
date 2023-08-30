def print_sorted_dictionary(a_dictionary):
        
    key = list(a_dictionary.keys())
    key.sort()

    for i in key:
        print(f"{i}:{a_dictionary[i]}")


a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }

print_sorted_dictionary(a_dictionary)