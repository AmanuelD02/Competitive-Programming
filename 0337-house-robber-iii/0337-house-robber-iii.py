# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @lru_cache(None)
        def dfs(node, prev):
            if not node:
                return 0
            if prev:
                return dfs(node.left, not prev) + dfs(node.right, not prev)
            one = node.val +  dfs(node.left, not prev) + dfs(node.right, not prev)
            two = dfs(node.left, prev) + dfs(node.right,prev)
            
            return max(one, two)
        
        return dfs(root, False)