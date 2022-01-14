def quick_sort(llist): 
    return quick_sort_helper(llist, 0, len(my_list) - 1)

def quick_sort_helper(llist, left, right):
    #base case
    if left < right:  
        pivot_idx = pivot(my_list, left, right)
        quick_sort_helper(llist, left, pivot_idx - 1)
        quick_sort_helper(llist, pivot_idx + 1, right)
    return llist

def pivot(llist, pivot_idx, end_idx):
    swap_idx = pivot_idx
    for i in range(pivot_idx + 1, end_idx + 1): 
         if llist[i] < llist[pivot_idx]: 
             swap_idx += 1 
             swap(llist, swap_idx, i)
    swap(llist, pivot_idx, swap_idx)
    return swap_idx

def swap(llist, idx1, idx2): 
    llist[idx1], llist[idx2] = llist[idx2], llist[idx1]

my_list = [4,6,0,7,3,2,5, 90, 21, -1]
print(pivot(my_list, 0, 6))
print(my_list)
print(quick_sort(my_list))