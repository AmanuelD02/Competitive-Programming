class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        for i in range(len(matrix)):
            for j in range(1, len(matrix[0])):
                matrix[i][j] += matrix[i][j-1]
        for i in range(len(matrix[0])):
            for j in range(1, len(matrix)):
                matrix[j][i] += matrix[j-1][i]
                
        for i in range(len(matrix)):
            matrix[i].append(0)
        matrix.append([0 for x in range(len(matrix[0]))])
        
        print(matrix)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.matrix[row2][col2] - self.matrix[row2][col1-1] - self.matrix[row1-1][col2] + self.matrix[row1 -1][col1 -1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)