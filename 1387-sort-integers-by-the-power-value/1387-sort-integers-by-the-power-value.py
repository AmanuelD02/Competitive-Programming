class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        power = []
        for num in range(lo, hi + 1):
            power.append((self.transform(num), num))
        
        power.sort()
        
        return power[k - 1][1]
    
    @lru_cache(None)
    def transform(self, num):
        if num == 1:
            return 0
        
        if num %2 == 0:
            return 1 + self.transform(num//2)
        
        return 1 + self.transform(3*num + 1)