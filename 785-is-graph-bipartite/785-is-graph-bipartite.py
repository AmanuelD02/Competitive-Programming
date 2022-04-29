class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        N = len(graph)
        parent = list(range(N))
        rank = [1] *N
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(node1, node2):
            p1, p2 = find(node1), find(node2)
            if p1 != p2:
                p1, p2 = sorted([p1, p2], key = lambda x: rank[x] )
                parent[p1] = p2
                rank[p2] += rank[p1]
        
        
        for i in range(N):
            p = find(i)
            for neigh in graph[i]:
                if p != find(neigh):
                    union(neigh, graph[i][0])
                else:
                    return False
        return True
        
                        
                        
        