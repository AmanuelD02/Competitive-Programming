# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def helper(node1,node2):
            if node1 and node2:
                if node1.val == node2.val:
                    return helper(node1.left, node2.left) and helper(node1.right, node2.right)
                return False
            return not (node1 or node2)
        
        
        def recur(node):
            if node:
                x = False
                if node.val == subRoot.val:
                    x = helper(node, subRoot)
                return recur(node.left) or recur(node.right) or x
        
        return recur(root)
                
                
                