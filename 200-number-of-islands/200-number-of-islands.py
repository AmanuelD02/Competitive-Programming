class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        M, N = len(grid), len(grid[0])
        in_bound = lambda r,c: 0 <= r < M and 0<= c < N
        
        def dfs(r,c):
            grid[r][c] = "0"
            
            for x, y in directions:
                newR, newC = r + x, c + y
                if in_bound(newR, newC) and grid[newR][newC] =='1':
                    dfs(newR,newC)
        
        
        total_island = 0
        for r in range(M):
            for c in range(N):
                if grid[r][c] =="1":
                    total_island += 1
                    dfs(r,c)
        return total_island
            