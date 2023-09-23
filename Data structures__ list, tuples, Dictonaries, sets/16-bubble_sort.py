def bubble(array=[3,2,1]):
    length = len(array)

    for i in range(length):
        for k in range(length):
            if array[i] < array[k]:
                array[i], array[k] = array[k], array[i]
                print(array)
bubble()
