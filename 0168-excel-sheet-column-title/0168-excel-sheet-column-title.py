class Solution:
    def convertToTitle(self, col: int) -> str:
        A = ord('A')
        res  = []
        
        while col > 0:
            cur = ((col -1) % 26)
            res.append(chr(cur + A))
            col = (col -1) // 26
        
        return ''.join(res[::-1])
        



