# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        curr = self 
        while True: 
            if value < curr.value: 
                #go left
                if curr.left is None: 
                    curr.left = BST(value)
                    break
                else: 	
                    curr = curr.left
            else: 
                #go right 
                if curr.right is None: 
                    curr.right = BST(value)
                    break
                else:
                    curr = curr.right
        # Do not edit the return statement of this method.
        return self

    def contains(self, value):
        # Write your code here.
        temp = self
        while temp is not None: 
            if value < temp.value: 
                temp = temp.left
            elif value > temp.value: 
                temp = temp.right
            else: 
                return True 
        return False
    
    def getMin(self): 
            temp = self
            while temp.left is not None: 
                temp = temp.left 
            return temp.value

    def remove(self, value, parentNode = None):
        # Write your code here.
        curr = self 
        while curr: 
            #find the node we are trying to remove 
            if value < curr.value:
                parentNode = curr
                curr = curr.left
            elif value > curr.value: 
                parentNode = curr 
                curr = curr.right 
            #Node is found 
            else: 
                #Has two children nodes
                if curr.right is not None and curr.left is not None: 
                    curr.value = curr.right.getMin()
                    #curr.value = smallest value of the right subtree
                    curr.right.remove(curr.value, curr)
                #Node to remove is root 
                elif parentNode is None: 
                    if curr.left is not None: 
                        curr.value = curr.left.value 
                        curr.right = curr.left.right
                        curr.left = curr.left.left
                    elif curr.right is not None: 
                        curr.value = curr.right.value
                        curr.left = curr.right.left
                        curr.right = curr.right.right
                    else: 
                        pass
                elif parentNode.left == curr: 
                    parentNode.left = curr.left if curr.left is not None else curr.right 
                elif parentNode.right == curr: 
                    parentNode.right = curr.left if curr.left is not None else curr.right 
                break 	
        # Do not edit the return statement of this method.
        return self