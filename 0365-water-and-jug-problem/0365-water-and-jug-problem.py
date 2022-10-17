class Solution:
    def canMeasureWater(self, j1: int, j2: int, target: int) -> bool:
        if j1 + j2 < target:
            return False
        
        j1, j2 = sorted([j1, j2])
        
        def GCD(a, b):
            if b == 0:
                return a
            return GCD(b, a%b)
        
        
        return target % GCD(j2, j1) == 0
        