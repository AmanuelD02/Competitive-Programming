class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if start.replace('_','') != target.replace('_',''): return False
        
        sl = [i for i in range(len(start)) if start[i]=='L']
        sr = [i for i in range(len(start)) if start[i]=='R']
        
        tl = [i for i in range(len(target)) if target[i]=='L']
        tr = [i for i in range(len(target)) if target[i]=='R']
        
   
        for i, j in zip(sl, tl):
            if i < j: return False
        
        for i, j in zip(sr, tr):
            if i > j: return False
        
        return True