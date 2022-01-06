class Node: 
    def __init__(self, value):
        self.value = value 
        self.right = None
        self.left = None

class BST: 
    def __init__(self):
        self.root = None
    def insert(self, value): 
        new_node = Node(value)
        if self.root is None: 
            self.root = new_node
            return True
        temp = self.root
        while(True):
            if new_node.value == temp.value: 
                return False 
            if new_node.value < temp.value: 
                #go left 
                if temp.left is None: 
                    temp.left = new_node
                    return True 
                temp = temp.left
            else: 
                #go right 
                if temp.right is None: 
                    temp.right = new_node
                    return True 
                temp = temp.right 
    def contains(self, value): 
        temp = self.root 
        while temp is not None:
            if temp.value == value: 
                return True 
            elif temp.value < value: 
                #go right 
                temp = temp.right 
            else: 
                #go left 
                temp = temp.left 
        return False 
    def get_min(self, curr_node):
        while curr_node.left is not None: 
            curr_node = curr_node.left
        return curr_node
    def get_max(self, curr_node): 
        while curr_node.left is not None: 
            curr_node = curr_node.right
        return curr_node.value




        
my_bst = BST()
print(my_bst.root)
my_bst.insert(20)
my_bst.insert(10)
my_bst.insert(15)
my_bst.insert(30)
my_bst.insert(19)
my_bst.insert(89)
my_bst.insert(1)
my_bst.insert(25)

print(my_bst.get_min(my_bst.root.right))

print(my_bst.contains(90)) 

