class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        power = []
        for num in range(lo, hi + 1):
            power.append((self.transform(num), num))
        
        power.sort()
        
        return power[k - 1][1]
    
    
    def transform(self, num):
        count = 0
        while num != 1:
            if num % 2 == 0:
                num //= 2
            else:
                num = 3*num + 1
            
            count += 1
        
        return count