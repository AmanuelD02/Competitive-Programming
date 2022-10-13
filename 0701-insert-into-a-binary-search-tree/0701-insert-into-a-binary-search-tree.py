# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def bst(node):
            if node:
                if node.val > val:
                    if node.left:
                        return bst(node.left)
                    node.left = TreeNode(val)
                    
                else:
                    if node.right:
                        return bst(node.right)
                    node.right = TreeNode(val)
        if not root: return TreeNode(val)
        bst(root)
        return root