# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = TreeNode(val = float('-inf'))
        first = second = None
        def inorder(node):
            nonlocal prev, first, second
            if node:
                inorder(node.left)
                if prev.val >= node.val and not first:
                    first = prev
                    
                if prev.val >= node.val and first:
                    second = node
                prev = node
                inorder(node.right)
                
        inorder(root)
        
        first.val, second.val = second.val, first.val