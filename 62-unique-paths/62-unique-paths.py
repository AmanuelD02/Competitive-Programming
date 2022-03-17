class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.total, squares, visited, end = 0, m*n, set(), (m-1, n-1)
        in_bound = lambda r, c: 0 <= r< m and 0 <= c < n
        directions = ((0, 1), (1, 0))
        
        @cache
        def dfs(r,c):
            if (r,c) == end:
                return 1
            
            visited.add((r,c))
            total = 0
            for direction in directions:
                new_r, new_c = r + direction[0], c + direction[1]
                
                if in_bound(new_r, new_c) and (new_r, new_c) not in visited:
                    total += dfs(new_r, new_c)
            
            visited.remove((r,c))
            return total
            
        return dfs(0,0)
        
        return self.total
                
            
            