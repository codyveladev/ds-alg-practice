# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root): 
        output = []
        def dfs(node, level, output): 
            #base case
            if node is None: 
                return 
            #check if we need to add a new index
            if len(output) <= level: 
                output.append([])
            #Traverse the tree 
            dfs(node.left, level + 1, output)
            dfs(node.right, level + 1, output)
            #If we are at an even level add from right to left
            if level % 2 == 0: 
                output[level].append(node.val)
            #If we are at an odd level add from left to right
            else: 
                output[level].insert(0, node.val)
        dfs(root, 0, output)
        return output