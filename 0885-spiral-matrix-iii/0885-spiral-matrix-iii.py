class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        DIRS = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        path = [[rStart, cStart]]
        
        curRow, curCol = rStart, cStart
        curDir = 0
        curStep = 1
        while len(path) != (rows * cols):
            for _ in range(2):
                for i in range(curStep):
                    curRow += DIRS[curDir][0]
                    curCol += DIRS[curDir][1]
                    
                    if self.inBound(curRow, curCol, rows, cols):
                        path.append([curRow, curCol])
                
                curDir = (curDir + 1) % 4
            curStep += 1
        
        return path
    
    def inBound(self, row, col, rowEnd, colEnd):
        return 0 <= row < rowEnd and 0 <= col < colEnd