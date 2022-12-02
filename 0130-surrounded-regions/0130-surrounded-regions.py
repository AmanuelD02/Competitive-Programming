class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        free_regions = set()
        M, N = len(board), len(board[0])
        
        inBound = lambda row, col: 0 <= row < M and 0 <= col < N
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def free_region(row, col):
            free_regions.add((row, col))
            
            for x, y in directions:
                nx, ny = x + row, y + col
                if inBound(nx, ny) and board[nx][ny] == 'O' and (nx, ny) not in free_regions:
                    free_region(nx, ny)
            
        
        
        # UP and DOWN
        for col in range(N):
            if board[0][col] == 'O' and (0, col) not in free_regions:
                free_region(0, col)
            
            if board[M - 1][col] == 'O' and (M - 1, col) not in free_regions:
                free_region(M - 1, col)
        
        
        # LEFT and RIGHT
        for row in range(M):
            if board[row][0] == 'O' and (row, 0) not in free_regions:
                free_region(row, 0)
            
            if board[row][N -1] == 'O' and (row, N -1) not in free_regions:
                free_region(row, N - 1)
        
        
        for row in range(M):
            for col in range(N):
                if (row,  col) not in free_regions:
                    board[row][col] = 'X'
        