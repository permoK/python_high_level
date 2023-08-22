def best_score(a_dictionary):

    score = list(a_dictionary.values())
    score.sort(reverse=True)

    for (i, j) in a_dictionary.items():
        if j == score[0]:
            best_key = i
    print(f"Best score: {best_key}")

    

a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}

best_score(a_dictionary)