# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        
        def recur(node):
            if node:
                left, m1 = recur(node.left)
                right, m2 = recur(node.right)
                
                curPath =  left + right + node.val
                curMax = max(m1, m2, curPath)
                
                leftSide = left + node.val
                rightSide = right + node.val
                
                return [max(0, leftSide, rightSide), curMax]
                
            
            return [0, -float("inf")]
        
        return recur(root)[1]

            