# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        prev = 0
        def dfs(node, prevSum = 0):
            if not node: return prevSum
            prevSum = dfs(node.right, prevSum)
            node.val += prevSum
            return dfs(node.left, node.val)
        
        
        
        dfs(root)
        return root