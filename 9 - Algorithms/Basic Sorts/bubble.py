def bubble_sort(llist): 
    if len(llist) == 0: 
        return False 
    for i in range(len(llist) - 1, 0, -1):
        for j in range(i):
            if llist[j] > llist[j+1]: 
                t = llist[j]
                llist[j] = llist[j+1]
                llist[j+1] = t
    return llist

    

my_list = [4,2,6,5,1,3]
sorted_list = bubble_sort(my_list)
print(sorted_list)