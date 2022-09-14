class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s)%2 == 1: return False
        flip= opn = close  = 0
        for i, j in enumerate(s):
            if locked[i] == '0':
                flip += 1
            elif j =='(':
                opn += 1
            else:
                close += 1
            
            # print("f round", opn, close, flip,i)
            if flip + opn < close:
                return False
        flip= opn = close  = 0
        locked = locked[::-1]
        for i, j in enumerate(reversed(s)):
            if locked[i] == '0':
                flip += 1
            elif j =='(':
                opn += 1
            else:
                close += 1
            
            # print("s round", opn, close, flip,i)
            if flip + close < opn: 
                return False
        return True