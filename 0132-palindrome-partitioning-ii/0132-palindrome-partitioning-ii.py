class Solution:
    def minCut(self, s: str) -> int:
        s_size = len(s)
        
        @cache
        def dp(start = 0):
            nonlocal s_size
            
            if s[start:] == s[start:][::-1]:
                return 0
            
            minCut = float("inf")
            for end in range(start, s_size):
                if s[start: end + 1] == s[start:end + 1][::-1]:
                    minCut = min(minCut, 1 + dp(end + 1))
                    
            return minCut
        
        return dp()