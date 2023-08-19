def common_elements(set_1, set_2):
    c_set = set()
    for i in set_1:
        if i in set_2:
            c_set.add(i)
    print(c_set)
    
set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }

common_elements(set_1, set_2)