def max_sum(arr=[-2, 1, -3, 4, -1, 2, 1, -5, 4]):
    length = len(arr)

    left = 0
    right = length - 1
    t = 0
    s = []
    print(length)

    for i in range(length):
        
        max_sum = sum(arr[left:right+1])
        t  = max_sum
        
        if max_sum > t:
            s.append(max_sum)
            right -= i
        
        elif max_sum < t:
            left += i
        
        print(s)

max_sum()
