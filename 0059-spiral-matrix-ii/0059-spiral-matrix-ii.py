class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        self.DIRS = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        self.inBound = lambda x, y: 0 <= x < n and 0 <= y < n
        
        self.matrix = [[0] * n for _ in range(n)]
        self.visited = set()
        
        self.fillSpiralMatrix(0, 0, 1, 0)
        
        return self.matrix
    
    def fillSpiralMatrix(self, row, col, val, curr_dir):
        if len(self.visited) == len(self.matrix) ** 2:
            return 
        self.visited.add((row, col))
        self.matrix[row][col] = val
        
        new_row = row + self.DIRS[curr_dir % 4][0]
        new_col = col + self.DIRS[curr_dir % 4][1]
        if self.inBound(new_row, new_col) and (new_row, new_col) not in self.visited:
            self.fillSpiralMatrix(new_row, new_col, val + 1, curr_dir)
        else:
            curr_dir += 1
            new_row = row + self.DIRS[curr_dir % 4][0]
            new_col = col + self.DIRS[curr_dir % 4][1]  
            self.fillSpiralMatrix(new_row, new_col, val + 1, curr_dir)