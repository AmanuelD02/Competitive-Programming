class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        isVisited = set()
        row = lambda x,y: f'{y} {x} row'
        col = lambda x,y: f'{y} {x} col'
        block = lambda x,y,z: f'{z} {x} - {y} block'
        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                if cur !='.':
                    # print(isVisited)
                    
                    if not( row(i,cur) in isVisited or 
                           col(j,cur) in isVisited or
                           block(i//3,j//3, cur) in isVisited):
                        isVisited.add(row(i,cur))
                        isVisited.add(col(j,cur))
                        isVisited.add(block(i//3,j//3,cur))
                    else: return False
        return True
        
                    