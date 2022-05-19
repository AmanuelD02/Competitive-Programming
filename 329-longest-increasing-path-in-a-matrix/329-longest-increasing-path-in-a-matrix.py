class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = [(0,1), (1,0), (0, -1), (-1, 0)]
        M, N = len(matrix), len(matrix[0])
        in_bound = lambda x, y: 0 <= x < M and 0 <= y < N
        longest = 1
        
        @lru_cache(None)
        def dfs(r, c):
            long  = 1
            for x, y in directions:
                nr, nc = r + x, c + y
                if in_bound(nr, nc) and matrix[nr][nc] > matrix[r][c]:
                    path = 1 + dfs(nr, nc)
                    long = max(long, path)
                
            return long
        
        for row in range(M):
            for col in range(N):
                longest = max(longest, dfs(row, col))
        
        return longest