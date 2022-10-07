class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        in_bound = lambda r,c : 0<= r < M and 0<= c < N
        direction = [[0,1],[1,0],[0,-1], [-1,0]]
        visited = set()
        total = 0
        
        def dfs(r,c):
            visited.add((r,c))
            perimeter = 0
            for x, y in direction:
                xx, yy = x + r, c + y
                if (xx,yy) in visited: continue
                if not in_bound(xx, yy) or grid[xx][yy] == 0:
                    perimeter += 1
                    
                else:
                    perimeter += dfs(xx, yy)
            return perimeter
        
        
        for row in range(M):
            for col in range(N):
                if (row,col) not in visited and grid[row][col] == 1:
                    total += dfs(row, col)
        
        return total
                    
                    
        