class Solution:
    def uniquePathsWithObstacles(self, matrix: List[List[int]]) -> int:
        M, N = len(matrix), len(matrix[0])
        if matrix[M -1][N-1] == 1 or  matrix[0][0] == 1:
            return 0
        
        in_bound = lambda x, y: 0 <= x < M and 0 <= y < N
        directions = [(0,1), (1,0) ]
        path = set()
        
        @lru_cache(None)
        def dfs(r, c):
            if (r, c) == (M - 1, N - 1):
                return 1 - matrix[r][c]
                
            path.add((r, c))
            no_ways = 0
            for x, y in directions:
                if in_bound(r + x, c + y) and (r + x, c + y) not in path and  not matrix[r + x][c + y]:
                    no_ways += dfs(r + x, c + y)
            path.remove((r, c))
            return no_ways
        
        
        return dfs(0, 0)
                    