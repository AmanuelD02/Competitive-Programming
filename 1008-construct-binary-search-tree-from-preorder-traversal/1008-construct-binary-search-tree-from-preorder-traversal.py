# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        stack = [root]
        
        for i in range(1, len(preorder)):
            cur = TreeNode(preorder[i])
            if cur.val < stack[-1].val:
                stack[-1].left = cur
                
            else:
                prev = None
                while stack:
                    prev = stack.pop()
                    
                    if stack and stack[-1].val > cur.val:
                        break
                        
                if prev: prev.right = cur
            
            stack.append(cur)
        
        return root