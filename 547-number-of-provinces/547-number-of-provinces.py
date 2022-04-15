class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        parent = list(range(N))
        child = [1] * N
        
        def find(node):
            if parent[node] != node:
                parent[node]  =  find(parent[node])  
                
            return parent[node]
            
                
        def parentConnected(node1, node2):
            return find(node1) == find(node2)
            
        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)
            if parent1 != parent2:
                parent1, parent2 = sorted([parent1, parent2], key = lambda x: child[x] )
                child[parent2] += child[parent1]
                parent[parent1] = parent2
                
        for i in range(N):
            for j in range(N):
                if i != j and  (isConnected[i][j] or parentConnected(i, j) ):
                    union(i,j)

        return len(set(parent))         
                    