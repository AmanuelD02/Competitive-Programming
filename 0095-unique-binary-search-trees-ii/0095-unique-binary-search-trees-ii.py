# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.helper(1, n)
        
    @lru_cache(None)
    def helper(self, start, end):
        if start > end:
            return [None]
    
        if start == end:
            return [TreeNode(start)]
        
        answer = []
        
        for i in range(start, end + 1):
            mid = i
            
            leftSide = self.helper(start, mid - 1)
            rightSide = self.helper(mid + 1, end)

            for left in leftSide:
                for right in rightSide:
                    
                    root = TreeNode(mid)
                    root.left = left
                    root.right = right
                
                    answer.append(root)
        
        return answer