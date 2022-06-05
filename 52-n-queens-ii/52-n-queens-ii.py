class Solution:
    def totalNQueens(self, n: int) -> int:
        results = 0
        grid =[["." for x in range(n)] for y in range(n)]
        
        def isValid():
            for i in range(n):
                count = grid[i].count("Q")
                if count > 1:
                    return False
            for i in range(n):
                count = 0
                for j in range(n):
                    if grid[j][i] == "Q": count += 1
                if count > 1: return False
            
            positive_diag = defaultdict(int)
            negative_diag = defaultdict(int)
            for i in range(n):
                for j in range(n):
                    if grid[i][j] == 'Q':
                        positive_diag[i + j] += 1
                        negative_diag[j - i] += 1
                    if positive_diag[i + j] > 1 or negative_diag[j -i] > 1:
                        return False
                        
            return True
        
        
        
        
        def recur(i):
            nonlocal results
            if i >= n:
                results += 1
                return
            
            for j in range(n):
                grid[i][j] = "Q"
                # print(isValid())
                if isValid():
                    recur(i + 1)
                grid[i][j] = "."
        
        
        
        
        recur(0)
        return results