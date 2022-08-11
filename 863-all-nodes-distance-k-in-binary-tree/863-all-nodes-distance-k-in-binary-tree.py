# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                stack.append(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                stack.append(node.right)
        
        ans = []
        visited = set()
        def dfs(node,k):
            visited.add(node)
            if k == 0:
                ans.append(node)
            
            
            for neigh in graph[node]:
                if neigh not in visited:
                    dfs(neigh, k-1)
        
        dfs(target.val,k)
        return ans
                