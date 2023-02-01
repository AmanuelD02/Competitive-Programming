class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        M, N = len(mat), len(mat[0])
        
        prefix = [[0] * N for _ in range(M)]
        
        for row in range(M):
            sum = 0
            for col in range(N):
                sum += mat[row][col]
                prefix[row][col] += sum
                
                if row > 0:
                    prefix[row][col] += prefix[row - 1][col]
        
        result = [[0] * N for _ in range(M)]
        
        for row in range(M):
            for col in range(N):
                min_r, max_r = max(0, row - k), min(M - 1, row + k)
                min_c, max_c = max(0, col - k), min(N - 1, col + k)
                
                result[row][col] += prefix[max_r][max_c]
                if min_r > 0:
                    result[row][col] -= prefix[min_r - 1][max_c]
                if min_c > 0:
                    result[row][col] -= prefix[max_r][min_c -1]
                
                if min_r > 0 and min_c > 0:
                    result[row][col] += prefix[min_r - 1][min_c - 1]
        
        return result
                 