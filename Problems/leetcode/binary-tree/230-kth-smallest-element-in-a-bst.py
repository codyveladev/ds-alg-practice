# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root, k: int) -> int:
        self.vals = []
        def inorderTraverse(node): 
            if not node: 
                return 
            if node.left: 
                inorderTraverse(node.left)
            self.vals.append(node.val)
            if node.right: 
                inorderTraverse(node.right)
        inorderTraverse(root)
        return self.vals[k - 1]