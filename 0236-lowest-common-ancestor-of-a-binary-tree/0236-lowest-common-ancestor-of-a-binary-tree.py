# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        def dfs(node):
            if not node:
                return None
            
            curr = node if p == node or q == node else None
            
            left, right = dfs(node.left), dfs(node.right)
            if left and right: return node
            if curr and (left or right): return curr
            if left: return left
            if right: return right
            return curr

        
        return dfs(root)
                