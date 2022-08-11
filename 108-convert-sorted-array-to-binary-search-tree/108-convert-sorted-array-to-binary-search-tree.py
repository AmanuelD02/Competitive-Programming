# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def recur(node, lst):
            if len(lst)==0:
                return
            mid = len(lst)//2

            if node.val < lst[mid]:
                node.right = TreeNode(lst[mid])
                recur(node.right, lst[0:mid])
                recur(node.right, lst[mid+1:])
            else:
                node.left = TreeNode(lst[mid])
                recur(node.left, lst[0:mid])
                recur(node.left, lst[mid+1:])
        
        
        dummy = TreeNode(-float("inf"))
        recur(dummy,nums)
        return dummy.right