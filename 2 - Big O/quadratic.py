#O(n^2)
#Have to iterate both 
#Quadratic Time 
def print_items(n):
    for i in range(n):
        for j in range(n):
            print([i, j])