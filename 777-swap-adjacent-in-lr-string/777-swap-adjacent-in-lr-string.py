class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if start.replace('X','') != end.replace('X', ''): return False

        
        sl = [i for i in range(len(start)) if start[i]=='L']
        sr = [i for i in range(len(start)) if start[i]=='R']
        
        el = [i for i in range(len(end)) if end[i]=='L']
        er = [i for i in range(len(end)) if end[i]=='R']
        for i, j in zip(sl,el):
            if j > i: return False
        for i, j in zip(sr,er):
            if j < i: return False
        
        return True