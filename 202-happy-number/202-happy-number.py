class Solution:
    def isHappy(self, n: int) -> bool:
        if n ==1: return True
        seen = set()
        while n!=1 and n not in seen:
            seen.add(n)
            sums = 0
            while n >0:
                sums += (n%10)**2
                n = n//10
            n = sums
        
        return n == 1
        