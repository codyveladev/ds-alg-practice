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
    
    def dfs_pre_order(self):
        results = []
        def traverse(current_node): 
            results.append(current_node.value)
            if current_node.left is not None: 
                traverse(current_node.left)
            if current_node.right is not None: 
                traverse(current_node.right)
        traverse(self.root)
        return results
    
    def dfs_post_order(self): 
        results = []
        def traverse(current_node): 
            if current_node.left is not None: 
                traverse(current_node.left)
            if current_node.right is not None: 
                traverse(current_node.right)
            results.append(current_node.value)
        traverse(self.root)
        return results
    
    def dfs_in_order(self): 
        results = []
        def traverse(current_node): 
            if current_node.left is not None: 
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None: 
                traverse(current_node.right)
        traverse(self.root)
        return results


my_bst = BST()
print(my_bst.root)
my_bst.insert(47)
my_bst.insert(21)
my_bst.insert(76)
my_bst.insert(18)
my_bst.insert(27)
my_bst.insert(52)
my_bst.insert(82)

print(my_bst.dfs_in_order())