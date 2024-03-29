class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans, MOD, length = 0, (10**9) +7, 0
        for i in range(1,n+1):
            if i & (i -1) == 0: length += 1
            
            ans = ((ans << length) + i) % MOD
        
        return ans