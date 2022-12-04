class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        M, N = len(maze), len(maze[0])
        
        inBound = lambda row, col : 0 <= row < M and 0 <= col < N
        directions  = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        queue = deque()
        queue.append(entrance)
        
        steps = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                for dx, dy in directions:
                    nx, ny = dx + r, dy + c
                    
                    if not inBound(nx, ny) and [r, c] != entrance:
                        return steps
                    
                    elif not inBound(nx, ny) and [r, c] == entrance:
                        continue
                        
                    elif inBound(nx, ny) and maze[nx][ny] == '.':
                        queue.append((nx, ny))
                        maze[nx][ny] = '+'
            
            steps += 1
        return -1 
                 