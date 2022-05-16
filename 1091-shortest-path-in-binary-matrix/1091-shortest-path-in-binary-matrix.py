class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        isValid = lambda x,y : 0 <= x < len(grid) and 0 <= y < len(grid[0]) and  grid[x][y] == 0
        directions = ( (0, 1), (1, 0), (0, -1), (-1, 0), (1,1), (-1,-1), (-1, 1), (1, -1))
        endDest = (N - 1, N -1)
        queue = deque()
    
        
        if not isValid(0, 0) or not isValid(N-1, N-1):
            return -1
        queue.append((0,0,1))
        result = float("inf")
        while queue:
            x, y, d = queue.popleft()
            if (x,y) == endDest:
                result = d
                break
            
            for i, j in directions:
                nr, ny = x + i, y + j
                if isValid(nr, ny):
                    grid[nr][ny] = 1
                    queue.append((nr, ny, d + 1))
        
        return result if result != float("inf") else -1 
                
                    
            
            
            