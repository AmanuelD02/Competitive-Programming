# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0: return []
        memo = {0:[],1:[TreeNode(0)]}
        
        
        def dp(n):
            # print(n)
            if n not in memo:
                ans = []
                for x in range(n):
                    y = n -1 - x
                    # print(x,y)
                    for left in dp(x):
                        for right in dp(y):
                            
                            node = TreeNode(0)
                            node.left = left
                            node.right = right
                            
                            ans.append(node)
                
                memo[n] = ans 
            return memo[n]
        return dp(n)
