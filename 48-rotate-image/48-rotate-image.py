class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        """
        n = len(matrix)
        def rotate_cell(r,c):
            cur = matrix[r][c]
            for i in range(4):
                r, c= c, (n - 1 - r)
                next = matrix[r][c]
                matrix[r][c] = cur
                cur = next
        
        for i in range(math.ceil(n/2)):
            for j in range(i, n-i-1):
                rotate_cell(i, j)
                
         