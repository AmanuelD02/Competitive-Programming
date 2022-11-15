# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        h =  0 
        self.total = 0
        
        self.dfs(root)
        
        return self.total
    def dfs(self, node):
        if node:
            right = self.dfs(node.right)
            self.total += 1
            left = self.dfs(node.left)
        
        