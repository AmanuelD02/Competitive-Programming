class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        M, N = len(matrix), len(matrix[0])
        newMatrix = [[0 for x in range(M)] for y in range(N)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                newMatrix[j][i] = matrix[i][j]
        
        return newMatrix