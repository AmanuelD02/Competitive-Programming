class Solution:
    def romanToInt(self, s: str) -> int:
        romDict = {'CM':900,  'CD':400,  "XC":90, 
               "XL":40,  "IX":9,   "IV":4,
                   "XL":40,
               'M':1000,  "D":500,  "C":100,
              "L":50,   "X":10,  "I":1 ,"V":5}
        
        
        i = num = 0
        N = len(s)
        while i + 1 < N:
            if s[i:i + 2] in romDict:
                num += romDict[s[i : i + 2]]
                i += 2
            else:
                num += romDict[s[i]]
                i += 1
        
        if i < N:
            num += romDict[s[i]]
        
        return num