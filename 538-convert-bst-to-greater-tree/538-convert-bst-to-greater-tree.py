# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.total = 0
        def dfs(node):
            if node:
                dfs(node.right)
                self.total += node.val
                node.val = self.total
                dfs(node.left)
            return node
        
        dfs(root)
        return root