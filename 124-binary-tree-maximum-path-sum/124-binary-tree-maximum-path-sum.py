# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maximumPathSum  = -float("inf")
        
        def recur(node):
            nonlocal maximumPathSum 
            if node:
                left = recur(node.left)
                right = recur(node.right)
                
                curPath =  left + right + node.val
                maximumPathSum = max(maximumPathSum, curPath)
                
                leftSide = left + node.val
                rightSide = right + node.val
                
                return max(0, leftSide, rightSide)
                
            
            return 0
        
        recur(root)
        return maximumPathSum
            