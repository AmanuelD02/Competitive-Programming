class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        rgraph, visited = defaultdict(set), set()
        for frm, to in edges:
            rgraph[to].add(frm)
        ancestors = [set() for _ in range(n)]
        
        def dfs(node):
            visited.add(node)
            for ans in rgraph[node]:
                if ans not in visited:
                    dfs(ans)
                ancestors[node].add(ans)
                ancestors[node].update( ancestors[ans])
        
        for i in range(n):
            if i not in visited:
                dfs(i)
        
        return [ sorted(list(x)) for x in ancestors]