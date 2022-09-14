class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s)%2 == 1: return False
        firstRound = lambda opn, close, flip :  flip + opn < close
        secondRound = lambda opn, close, flip:  flip + close < opn
        def helper(s, locked, validator):
            
            flip= opn = close  = 0
            for i, j in enumerate(s):
                if locked[i] == '0':
                    flip += 1
                elif j =='(':
                    opn += 1
                else:
                    close += 1
            
            # print("f round", opn, close, flip,i)
                if validator(opn,close,flip):
                    return False
            return True
        
        return helper(s,locked,firstRound) and helper(s[::-1], locked[::-1],secondRound)