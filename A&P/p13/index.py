def bubbleSort(lst):
    for passnum in range(len(lst)-1, 0, -1):
        for i in range(passnum):
            if lst[i] < lst[i+1]:
                temp = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = temp
    return lst

lst = [19, 20, 53, 2, 0, 5, 29]
sorted_list = bubbleSort(lst)
print(sorted_list)
