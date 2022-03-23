# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        largest, queue = [], deque([root])
        
        while queue:
            larg = float('-inf')
            for i in range(len(queue)):
                node = queue.popleft()
                larg = max(larg, node.val)
                
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            largest.append(larg)
        
        return largest