class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        obstacles = 0
        self.answer = 0
        in_bound = lambda r,c: 0<= r< len(grid) and 0<=c < len(grid[0])

        def isValid(i, j):
                    return 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] != -1
        ending= starting = None
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == -1:
                    obstacles +=1
                if grid[i][j] == 1:
                    starting = (i,j)
                if grid[i][j] ==2:
                    ending = (i,j)
        path = (len(grid) * len(grid[0])) - obstacles
                    
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        
        def recur(r,c, visited):
            visited.add((r,c))
            if (r,c) == ending and len(visited)== path:
                self.answer += 1
                return
            
            for direction in directions:
                nr , nc = r + direction[0], c + direction[1]
                if isValid(nr, nc) and (nr, nc) not in visited :
                    recur(nr, nc, visited.copy())
                
        recur(starting[0], starting[1], set())
        
        return self.answer
            
            