def insertion_sort(arr): 
    for i in range(1, len(arr)): 
        temp = arr[i]
        j = i - 1
        while temp < arr[j] and j > -1: 
            arr[j+1] = arr[j]
            arr[j] = temp
            j -= 1
    return arr

unsorted_arr = [1,5,9,2,10, -1]
sorted_arr = insertion_sort(unsorted_arr)
print(sorted_arr)