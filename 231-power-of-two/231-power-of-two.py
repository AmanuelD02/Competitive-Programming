class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0: return False
        count = 0
        while n:
            count += n & 1
            if count>1:
                return False
            n >>= 1
        
        return True