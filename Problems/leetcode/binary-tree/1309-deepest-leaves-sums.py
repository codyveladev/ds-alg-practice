# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root) -> int:
        toAdd = []
        #Find the max depth of the tree
        maxDepth = self.findMaxDepth(root)
        def findSumsToAdd(node, depth): 
            if not node.left and not node.right:
                #If we get to the deepest leave add the value to list
                if depth == maxDepth: 
                    toAdd.append(node.val)
                    return 
            if node.left is not None: 
                findSumsToAdd(node.left, depth + 1)
            if node.right is not None: 
                findSumsToAdd(node.right, depth + 1)
        findSumsToAdd(root, 1)
        return sum(toAdd)
    def findMaxDepth(self, node): 
        if not node: 
            return 0 
        else: 
            return max(self.findMaxDepth(node.left), self.findMaxDepth(node.right)) + 1