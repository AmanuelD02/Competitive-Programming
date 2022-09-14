# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def validator(freq):
            p = 0
            # print(freq)
            for k, f in freq.items():
                if f % 2 ==1 and p > 0: return 0
                elif f%2 == 1: p+=1
            return 1
        answer = 0
        def dfs(node, store):
            nonlocal answer
            if  node:
                store[node.val] += 1
                left = dfs(node.left, store)
                right = dfs(node.right, store)
                store[node.val] -= 1
                if not node.left and not node.right:
                    answer += left
                return 0
            return validator(store)
        
        store = defaultdict(int)
        dfs(root, store)
        return answer
            
                