def max_of_list(list1): 
    max = list1[0] 
    for i in range(1, len(list1)): 
        if list1[i] > max: 
            max = list1[i] 
    return max

T = [9, 12, 30, -1, 3, 30, 14, 100, -26]
nilaiTerbesar = max_of_list(T)
print(f'Nilai terbesar: {nilaiTerbesar}')