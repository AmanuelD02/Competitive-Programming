# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def search(target,node,caller):
            if node:
                if caller != node and node.val == target:
                    return True
                if node.val > target:
                    return search(target,node.left,caller)
                
                return search(target, node.right,caller)
            return False
        
        
        def dfs(node):
            if node:
                if search(k- node.val, root,node):
                    return True
                return dfs(node.left) or dfs(node.right)
            return False
        return dfs(root)
                