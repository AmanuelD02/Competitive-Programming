class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        M, N = len(grid), len(grid[0])
        
        in_bound = lambda x, y: x < M and y< N
        
        def next_index(x,y):
            if in_bound(x, y + 1): return (x, y + 1)
            elif x + 1 < M:    
                return (x+1, 1 - (N - y))
            else:
                return (0, 1 - (len(grid[0]) - y))
    
        temp = grid[0][0]        
        for _ in range(k):
            for i in range(M):
                for j in range(N):
                    grid[i][j] , temp = temp, grid[i][j]
            grid[0][0] = temp
        
        return grid
