class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        N = len(grid)
        
        queue = deque()
        islands = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        inBound = lambda x, y: 0<= x < N and 0 <= y < N
        
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    queue.append((r,c))
                    islands += 1
        
        
        if islands == 0 or islands == (N*N):
            return -1
        
        
        steps = -1
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                
                for dx, dy in directions:
                    nx, ny = dx + x, dy + y
                    
                    if inBound(nx, ny) and grid[nx][ny] == 0:
                        grid[nx][ny] = 1
                        queue.append((nx, ny))
            
            steps += 1
        
        
        return steps
        