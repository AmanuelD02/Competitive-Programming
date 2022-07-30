class Solution:
    @lru_cache(None)
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1
            n >>= 1
        
        return count