# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.node = TreeNode()
        dummy = self.node
        
        def inorder(node):
            if node:
                inorder(node.left)
                self.node.right = TreeNode(val = node.val)
                self.node = self.node.right
                inorder(node.right)
        
        
        inorder(root)
        return dummy.right