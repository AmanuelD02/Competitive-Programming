# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue, level = deque([root]), 1
        max_sum = (root.val,1)
        while queue:
            level_sum = 0
            for i in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            
            if level_sum > max_sum[0]:
                max_sum = (level_sum,level)
            
            level +=1
        return max_sum[1]
                    
            