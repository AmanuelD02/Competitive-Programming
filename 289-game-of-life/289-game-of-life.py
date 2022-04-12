from copy import copy, deepcopy
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        M, N = len(board), len(board[0])
        
        in_bound = lambda x, y: 0 <= x < M and 0 <= y < N
        directions = [(0,1),(1,0), (0,-1),(-1,0),(-1,1),(1,-1), (-1,-1), (1,1)]
        new_board = deepcopy(board)
        
        def counter(x, y):
            count = 0
            for direction in directions:
                nr, nc = direction[0] + x, direction[1] + y
                if in_bound(nr,nc) and new_board[nr][nc]:
                    count += 1
                    
            return count
        
             
        for i in range(M):
            for j in range(N):
                count = counter(i,j)   
                if board[i][j]:
                    if count < 2 or count >3:
                        board[i][j] = 0
                else:
                    if count ==3:
                        board[i][j] = 1
        
        
        
        
                
        
                    
                    
        
        