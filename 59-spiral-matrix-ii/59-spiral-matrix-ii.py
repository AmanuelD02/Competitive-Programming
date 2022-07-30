class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for _ in range(n)]
        isValid = lambda x,y : 0 <= x < n and 0 <= y <n and matrix[x][y] == 0
        
        d, counter  = 0, 1
        direction = [(0,1), (1,0), (0,-1), (-1,0)]
        current = (0,0)
        
        for i in range(n*n):
            r,c = current
            matrix[r][c] = counter
            
            newR, newC = r + direction[d][0], c+ direction[d][1]
            
            if not isValid(newR, newC):
                d = (d+1)%4
            
            current = (r + direction[d][0], c + direction[d][1])
            counter += 1
            
        return matrix
                
        
            
                
                
        
            