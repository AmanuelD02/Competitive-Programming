class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        parent = list(range(N))
        child = [1] * N
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)
            if parent1 != parent2:
                parent1, parent2 = sorted([parent1, parent2], key= lambda x: child[x] )
                parent[parent1] = parent2
                child[parent2] += child[parent1]
                return True
            return False
        
        
        all_edges = []
        for i in range(N):
            for j in range(i+1):
                weight = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                all_edges.append((weight, i, j))
        all_edges.sort()
        
        edges_used = cost = 0
        
        for weight, node1, node2 in all_edges:
            if union(node1, node2):
                cost += weight
                edges_used += 1
                if edges_used +1 == N:
                    break
        return cost