# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool: 
        if root is None: 
            return False
        res = []
        self.dfs(root, 0, targetSum, res)
        return 1 in res
        
    def dfs(self, node, runningSum, targetSum, res): 
        runningSum += node.val
        if node.left is None and node.right is None: 
            if runningSum == targetSum: 
                res.append(True)
        if node.left is not None: 
            self.dfs(node.left, runningSum, targetSum, res)
        if node.right is not None: 
            self.dfs(node.right, runningSum, targetSum, res)    
