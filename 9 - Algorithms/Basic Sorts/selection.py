def selection_sort(arr):
    for i in range(len(arr)-1): 
        min_index = i 
        for j in range(i+1, len(arr)): 
            if arr[j] < arr[min_index]: 
                min_index = j
        if min_index != i: 
            t = arr[i]
            arr[i] = arr[min_index]
            arr[min_index] = t
    return arr


test = [1, 4, 6, 2, 3, 5, 11, 9]
test1 = selection_sort(test)
print(test1)