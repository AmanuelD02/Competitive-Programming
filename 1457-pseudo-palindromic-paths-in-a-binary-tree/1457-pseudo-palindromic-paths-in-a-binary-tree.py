# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, count = 0):
            if not node: return 0
            count ^= 1 << (node.val - 1)
            res = dfs(node.left, count ) + dfs(node.right, count)
            if not node.right and not node.left:
                if count & (count -1) == 0:
                    res += 1
            return res
        return dfs(root)
                    
                
            
                