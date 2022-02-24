# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        if root is None: 
            return result
        current_path = str(root.val)
        #Add the root node to the path if the have children
        if root.left is None and root.right is None: 
            result.append(current_path)
        #DFS left sde
        if root.left is not None: 
            self.dfs(root.left, current_path, result)
        #DFS right side
        if root.right is not None: 
            self.dfs(root.right, current_path, result)
        return result
    
    def dfs(self, node, current_path, result): 
        current_path += '->' + str(node.val)
        if node.left is None and node.right is None: 
            result.append(current_path)
            return 
        if node.left is not None: 
            self.dfs(node.left, current_path, result)
        if node.right is not None: 
            self.dfs(node.right, current_path, result)
