class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        inBound = lambda x, y: 0 <= x < N and 0<=y < N
        queue = deque()
        
        def dfs(r, c):
            grid[r][c] = -1
            queue.append((r, c))
            
            for dx, dy in directions:
                nx, ny = dx + r, dy + c
                if inBound(nx, ny) and grid[nx][ny] == 1:
                    dfs(nx, ny)
        
        def findIsland():
            for r in range(N):
                for c in range(N):
                    if grid[r][c] == 1:
                        return r, c
        
        
        dfs(*findIsland())
        steps = 0
        # print(queue, grid)
        while queue:
            for _ in range(len(queue)):
                r, c  = queue.popleft()
                # print(r, c , steps)

                for dx, dy in directions:
                    nx, ny = dx + r, dy + c
                    if inBound(nx, ny) and grid[nx][ny]  == 0:
                        grid[nx][ny] = -1
                        queue.append((nx, ny))
                    elif inBound(nx, ny) and grid[nx][ny]  == 1:
                        return steps
            
            steps += 1
    
    