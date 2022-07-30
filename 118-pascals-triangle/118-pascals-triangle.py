class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal =  [[1]]
        for i in range(1, numRows):
            ans = [1]
            for j in range(i-1):
                ans.append( pascal[i-1][j] + pascal[i-1][j+1] ) 
            ans.append(1)
            pascal.append(ans)
        return pascal
                           