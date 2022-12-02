class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M, N = len(grid), len(grid[0])
        islands = 0

        
        inBound = lambda x, y: 0 <= x < M and 0 <= y < N
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def dfs(row, col):
            grid[row][col] = "0"
            
            for x, y in directions:
                if inBound(row + x, col + y) and grid[row + x][col + y] == "1":
                    dfs(row + x, col + y)
                    
            
            
        
        for row in range(M):
            for col in range(N):
                if grid[row][col] == "1":
                    dfs(row, col)
                    islands += 1
        
        return islands