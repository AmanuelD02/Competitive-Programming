class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        parent = [[1] * N for _ in range(M)]
        child = [[1] * N for _ in range(M)]
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        in_bound = lambda row, col: 0<= row <len(grid) and 0<= col <len(grid[0])
        
        for i in range(M):
            for j in range(N):
                parent[i][j] = (i, j)     
        def find(node):
            i, j = node
            if parent[i][j] != (i, j):
                parent[i][j] = find(parent[i][j])
            
            return parent[i][j]
        
        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)
            if parent1 != parent2:
                parent1, parent2 = sorted([parent1, parent2], key = lambda x: child[x[0]][x[1]] )
                i, j = parent1
                a, b = parent2
                child[a][b] += child[i][j]
                parent[i][j] = parent2
                
        
        for i in range(M):
            for j in range(N):
                if grid[i][j]:
                    for direction in directions:
                        r, c = i + direction[0], j + direction[1]
                        if in_bound(r,c) and grid[r][c]:
                            union((r,c), (i,j))
        
        max_area = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j]:
                    max_area = max(max_area, child[i][j])
        
        return max_area
             
                