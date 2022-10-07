class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        M, N = len(heights), len(heights[0])
        in_bound = lambda r, c:  0<= r < M and 0<= c < N
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        
        pacific_set, atlantic_set = set(), set()
        
        def dfs(r,c, ocean):
            ocean.add((r,c))
            for x, y in directions:
                xx, yy = x + r, y + c
                if in_bound(xx,yy) and (xx,yy) not in ocean and heights[r][c] <= heights[xx][yy]:
                    dfs(xx, yy, ocean)
        
        
        for row in range(M):
            if (row, 0 ) not in pacific_set: dfs(row, 0, pacific_set)
            if (row, N-1) not in atlantic_set: dfs(row, N - 1, atlantic_set)
        
        for col in range(N):
            if  (0, col) not in pacific_set: dfs(0, col, pacific_set)
            if (M-1, col) not in atlantic_set: dfs(M-1, col, atlantic_set)
        
        ans = pacific_set.intersection(atlantic_set)
        answer = []
        for r, c in ans:
            answer.append([r,c])
        
        
        return answer