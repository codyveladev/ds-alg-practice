def inOrderTraverse(tree, array):
    # Write your code here.
    def traverse(node): 
        if node.left is not None: 
            traverse(node.left)
        array.append(node.value)
        if node.right is not None: 
            traverse(node.right)
    traverse(tree)
    return array 


def preOrderTraverse(tree, array):
    # Write your code here.
    def traverse(node): 
        array.append(node.value)
        if node.left is not None: 
            traverse(node.left)
        if node.right is not None: 
            traverse(node.right)
    traverse(tree)
    return array 


def postOrderTraverse(tree, array):
    # Write your code here.
    def traverse(node): 
        if node.left is not None: 
            traverse(node.left)
        if node.right is not None: 
            traverse(node.right)
        array.append(node.value)
    traverse(tree)
    return array 