class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        M, N = len(grid), len(grid[0])
        
    
        temp = grid[0][0]        
        for _ in range(k):
            for i in range(M):
                for j in range(N):
                    grid[i][j] , temp = temp, grid[i][j]
            grid[0][0] = temp
        
        return grid
