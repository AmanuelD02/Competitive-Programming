class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited, backtrack, adj = set(), set(), defaultdict(set)
        ans = set()
        for i, j in enumerate(graph):
            adj[i].update(j)
        
        def dfs(node):
            visited.add(node)
            backtrack.add(node)
            
            for neigh in adj[node]:
                if neigh in backtrack:
                    return False
                if neigh not in visited:
                    if not dfs(neigh):
                        return False
                    
            ans.add(node)
            backtrack.remove(node)
            return True
        
        for i in range(len(adj)):
            if i not in visited:
                dfs(i)
        
        ans = list(ans)
        ans.sort()
        
        return ans
            