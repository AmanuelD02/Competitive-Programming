class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        M, N = len(dungeon), len(dungeon[0])
        def getValue(r, c):
            if 0 <=r < M and 0 <= c < N:
                return dungeon[r][c]
            return -float("inf")
        
        for row in range(M-1,-1,-1):
            for col in range(N-1,-1,-1):
                if not (row == M-1 and col == N-1):
                    down = getValue(row + 1, col)
                    right = getValue(row, col + 1)
                    
                    dungeon[row][col] += max(down, right)

                dungeon[row][col] = min(dungeon[row][col], 0)
                if dungeon[row][col] == -float("inf"):
                    dungeon[row][col] = 0
                    

                    
        return abs(dungeon[0][0]) + 1