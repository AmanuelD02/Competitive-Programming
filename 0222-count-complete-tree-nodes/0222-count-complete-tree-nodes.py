# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_depth = right_depth = 0
        
        left = root.left
        right = root.right
        while left:
            left = left.left
            left_depth += 1
        while right:
            right = right.right
            right_depth += 1
        
        
        if left_depth == right_depth:
            if left_depth == 0:
                return 1
            return (2**(left_depth + 1)) - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)