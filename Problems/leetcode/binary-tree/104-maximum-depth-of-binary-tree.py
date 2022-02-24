# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        #base case
        if root is None: 
            return 0 
        #Max of left subtree
        leftMax = self.findMaxDepthOfSubtree(root.left, 0)
        #Max of right subtree
        rightMax = self.findMaxDepthOfSubtree(root.right, 0)
        #return the max of the both but add one to account for the root
        return max(leftMax + 1, rightMax + 1)
    
    def findMaxDepthOfSubtree(self, node, depthSoFar): 
        #base case return the current depth
        if node is None: 
            return depthSoFar
        #increase the depth by one as we go down
        depthSoFar += 1
        #recursive call by returning the max of the left subtree and right subtree
        return max(self.findMaxDepthOfSubtree(node.left, depthSoFar), self.findMaxDepthOfSubtree(node.right, depthSoFar))