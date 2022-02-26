'''
My initial solution
not very fast and uses quite a bit of memory 
will look over to try and improve 
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root) -> int:
        ans = []
        if root is None: 
            return 0
        #Account for the root
        self.findMinDepth(root, 1, ans)
        return min(ans)
        
    def findMinDepth(self, node, numberOfNodes, result): 
        #At the leaf node
        if node.left is None and node.right is None: 
            print(numberOfNodes)
            result.append(numberOfNodes)
            return
        if node.left is not None: 
            self.findMinDepth(node.left, numberOfNodes + 1, result)
        if node.right is not None: 
            self.findMinDepth(node.right, numberOfNodes + 1, result)
