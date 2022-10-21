# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        
        def dp(node):
            if not node:
                # IF Selected, not selected
                return [0,0]
            
            left, right = dp(node.left), dp(node.right)
            selected = node.val + left[1] + right[1]
            not_selected = left[0] + right[0]
            
            return [max(selected, not_selected), left[0] + right[0]]
        
        return max(dp(root))