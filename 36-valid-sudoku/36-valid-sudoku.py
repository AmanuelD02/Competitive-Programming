class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRow():
            for r in range(9):
                store = set()
                for c in range(9):
                    if board[r][c] == '.': continue
                    if board[r][c] in store: return False
                    store.add(board[r][c])
            return True

        def checkCol():
            for c in range(9):
                store = set()
                for r in range(9):
                    if board[r][c] == '.': continue
                    if board[r][c] in store: return False
                    store.add(board[r][c])
            return True
        
        def checkBox(r,c):
            store = set()
            for rr in range(r,r+3):
                for cc in range(c, c+3):
                   
                    if board[rr][cc] == '.': continue
                    if board[rr][cc] in store: return False
                    store.add(board[rr][cc])
            return True
        indx = [0,3,6]
        for r in indx:
            for c in indx:
                if not checkBox(r,c): return False
    
        return checkRow() and checkCol()
        
                    