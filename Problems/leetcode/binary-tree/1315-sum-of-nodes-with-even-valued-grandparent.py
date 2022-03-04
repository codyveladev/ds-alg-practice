# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root) -> int:
        if not root and (root.left is None or root.right is None): 
            return 0
        self.ans = 0
        def traverse(node, parent, grandParent):
            if not node: 
                return 
            if grandParent and grandParent.val % 2 == 0: 
                self.ans += node.val
            if node.left: 
                traverse(node.left, node, parent)
            if node.right: 
                traverse(node.right, node, parent)
        traverse(root, None, None)
        return self.ans