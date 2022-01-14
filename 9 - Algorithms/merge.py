def merge(list1, list2): 
    combined = []
    i = 0 
    j = 0
    while i < len(list1) and j < len(list2): 
        if list1[i] < list2[j]:  
            combined.append(list1[i])
            i += 1
        elif list1[i] > list2[j]: 
            combined.append(list2[j])
            j += 1  
    while i < len(list1): 
         combined.append(list1[i])
         i += 1
    while j < len(list2): 
        combined.append(list2[j])
        j += 1 
    return combined

def merge_sort(llist): 
    if len(llist) == 1: 
        return llist
    mid = len(llist) // 2
    left = llist[:mid]
    right = llist[mid:]
    return merge(merge_sort(left), merge_sort(right))


l1 = [1,3,4,9,11,10,2]
print(merge_sort(l1))