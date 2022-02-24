# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root):
        ans = []
        def traverse(node): 
            if node is None: 
                return 
            ans.append(node.val)
            if node.left is not None: 
                traverse(node.left)
            if node.right is not None:  
                traverse(node.right)
        traverse(root)
        return ans