def weight_average(my_list=[]):
    if my_list == []:
        print(0)
    else:
        total_prod = []
        div_by = []
        for i, j in my_list:
            product = i*j
            total_prod.append(product)
            div_by.append(j)
        average = (sum(total_prod))/ (sum(div_by))
        print(f"Average: {average:0.2f}")

weight_average()
      